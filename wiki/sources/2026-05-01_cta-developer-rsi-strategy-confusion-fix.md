# cta_developer RSI 策略混淆排查与修复

**来源**: cta_developer 批量回测现场排查
**日期**: 2026-05-01
**标签**: #cta_developer #rsi #策略混淆 #bug修复 #crypto回测 #pipeline

## 一句话摘要

`Rsi2MrStrategy`（RSI2）与 `RsiMeanReversionStrategy`（RSI）在 cta_developer 中因命名相似导致长期混淆，`pipeline.py` 的模糊匹配逻辑使 `RSI2_MR`/`rsi2mr` 误匹配到 `RSI`，进而导致策略运行错误、回测结果不可比。本次彻底区分两者机制并修复匹配逻辑。

---

## 两个策略的核心区别

| 维度 | `Rsi2MrStrategy`（RSI2 / rsi2mr） | `RsiMeanReversionStrategy`（RSI / RsiMeanReversion） |
|------|-----------------------------------|-----------------------------------------------------|
| **来源** | Quantitativo Substack "Trading the Mean Reversion Curve" | 通用 RSI 均值回归模板 |
| **RSI 周期** | 2-period（极短，捕捉极端超卖） | 14-period（标准周期） |
| **入场条件** | RSI2 < 阈值 **AND** Close > SMA200（趋势过滤） | RSI < 买入阈值（默认 30，无趋势过滤） |
| **出场条件** | Close > 昨日 High → 次日开盘卖出 | RSI > 卖出阈值（默认 70）或 ATR 止损 |
| **止损机制** | 无独立止损，靠出场规则 | ATR 止损（`sl_atr_multiplier` × ATR） |
| **核心参数** | `rsi_entry`, `rsi_period`, `sma_period` | `rsi_window`, `rsi_buy_threshold`, `rsi_sell_threshold`, `atr_window`, `sl_atr_multiplier` |
| **交易频率** | **极低**（条件苛刻：需同时满足超卖+趋势向上） | **中等**（仅 RSI 超卖即入场） |
| **适用市场** | 股票/ETF（趋势明确、有隔夜跳空） | 通用，但 crypto 趋势强时效果差 |

### 策略类文件位置

- `Rsi2MrStrategy`: `/root/.openclaw/workspace/cta_developer/cta/strategies/rsi2_mr_strategy.py`
- `RsiMeanReversionStrategy`: `/root/.openclaw/workspace/cta_developer/cta/strategies/rsi_mean_reversion_strategy.py`

---

## 混淆 bug 根因

### 现象

- `pipeline.py --strategy RSI2_MR` → 实际运行 `RsiMeanReversionStrategy`
- `pipeline.py --strategy rsi2mr` → 实际运行 `RsiMeanReversionStrategy`
- 只有 `pipeline.py --strategy Rsi2Mr` → 才正确运行 `Rsi2MrStrategy`

### 根因：`pipeline.py` `resolve_strategy()` 的模糊匹配逻辑

```python
# 原代码（buggy）
matches = [k for k in STRATEGY_MAP.keys() 
           if name.upper() in k.upper() or k.upper() in name.upper()]
```

当 `name = 'RSI2_MR'` 时：
- `'RSI' in 'RSI2_MR'` → **True**，所以 `RSI` 被匹配到
- `RSI` 映射到 `RsiMeanReversionStrategy`

### 修复：`resolve_strategy()` 改为 4 级优先级匹配

```python
def resolve_strategy(name: str):
    """匹配优先级：精确 → 大小写不敏感精确 → 标准化 → 子串长度降序"""
    # 1. 精确匹配
    if name in STRATEGY_MAP:
        return STRATEGY_MAP[name]
    
    # 2. 大小写不敏感精确匹配
    name_upper = name.upper()
    for k, v in STRATEGY_MAP.items():
        if k.upper() == name_upper:
            return v
    
    # 3. 标准化匹配（去掉下划线/连字符/末尾数字）
    import re
    def normalize(s):
        s = re.sub(r'[_\-]', '', s)
        s = re.sub(r'\d+$', '', s)
        return s.upper()
    
    name_norm = normalize(name)
    for k, v in STRATEGY_MAP.items():
        if normalize(k) == name_norm:
            return v
    
    # 4. 子串匹配：name 是 key 的子串，按 key 长度降序（避免短别名误匹配）
    matches = [(k, v) for k, v in STRATEGY_MAP.items() if name_upper in k.upper()]
    if matches:
        matches.sort(key=lambda x: len(x[0]), reverse=True)
        return matches[0][1]
    
    return None
```

### 修复后验证

| 输入 | 修复前 | 修复后 |
|------|--------|--------|
| `Rsi2Mr` | `Rsi2MrStrategy` ✓ | `Rsi2MrStrategy` ✓ |
| `RSI2_MR` | `RsiMeanReversionStrategy` ✗ | `Rsi2MrStrategy` ✓ |
| `rsi2mr` | `RsiMeanReversionStrategy` ✗ | `Rsi2MrStrategy` ✓ |
| `RSI2` | `Rsi2MrStrategy` ✓ | `Rsi2MrStrategy` ✓ |
| `RSI` | `RsiMeanReversionStrategy` ✓ | `RsiMeanReversionStrategy` ✓ |

### 同步修复 `run_batch.py`

- `STRATEGY_OPT_PARAMS` 补全别名：`Rsi2Mr`, `rsi2mr`, `RsiMeanReversion`, `RSI`, `rsi`
- `task_factory` 增加 `--min-trades` 和 `--strict-trade-constraints` 传递

---

## Batch 回测结果（crypto 日线，2020-01-01 ~ 2026-04-29）

### `Rsi2MrStrategy`（rsi2mr）

**硬性 50 次交易约束 → 无组合达标**。6 年回测交易次数：

| 品种 | 交易次数 | 说明 |
|------|---------|------|
| BTC | 8 | 条件过于苛刻（RSI2<5 + Close>SMA200） |
| ETH | 4 | 同上 |
| SOL | 14 | 同上 |
| DOGE | 8 | 同上 |

**结论**：该策略在 crypto 日线级别**不适合**，交易频率天然极低。

### `RsiMeanReversionStrategy`（RSI）

**硬性 50 次交易约束 → 全部达标**，但夏普全负：

| 品种 | 交易次数 | 夏普 | 总收益% | 最大回撤% |
|------|---------|------|--------|----------|
| BTC | 62 | -0.01 | -0.00 | -0.03 |
| ETH | 66 | -0.09 | -0.01 | -0.02 |
| DOGE | 66 | -0.15 | -56.04 | -92.40 |
| SOL | 54 | -0.52 | -0.14 | -0.23 |

**最优参数示例（BTC）**：
- `rsi_window=13`, `rsi_buy_threshold=33`, `rsi_sell_threshold=82`
- `atr_window=16`, `sl_atr_multiplier=1.8`

**结论**：该策略在 crypto 日线级别**交易次数达标但收益为负**，说明 RSI 均值回归在强趋势 crypto 市场中效果差，频繁止损导致亏损。

---

## 关键教训

1. **策略命名必须严格区分**：`RSI2` 和 `RSI` 只差一个字符，但逻辑完全不同
2. **模糊匹配必须防短别名误匹配**：`RSI` 不能匹配到 `RSI2_MR`
3. **crypto 日线不适合均值回归策略**：趋势性强，RSI 超卖后可能继续下跌
4. **交易次数约束需配合策略特性**：硬性 50 次对 RSI2 不可能，对 RSI 可能但收益差

---

## 相关实体
- [[cta_developer]]
- [[vn.py]]
- [[pipeline.py]]
- [[run_batch.py]]

## 相关概念
- [[RSI2 Mean Reversion]]
- [[RSI Mean Reversion]]
- [[策略别名解析]]
- [[crypto 日线回测]]
- [[交易次数约束]]

## 产出路径
- 报告 CSV: `/root/.openclaw/workspace/cta_developer/data/batch_results/rsi_crypto_20260501_114331/report.csv`
- 报告 MD: `/root/.openclaw/workspace/cta_developer/data/batch_results/rsi_crypto_20260501_114331/report.md`
