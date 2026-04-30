# KAMA ATR RTY Trend Strategy

## 策略概述

基于 KAMA（Kaufman Adaptive Moving Average）和 ATR（Average True Range）的趋势跟踪策略，专为 E-mini Russell 2000 (RTY) 和 E-mini S&P 500 (ES) 期货设计。

## 策略规则

### 入场条件

1. **趋势判断**：价格与 KAMA 的关系
   - 价格 > KAMA → 准备做多
   - 价格 < KAMA → 准备做空

2. **ATR 过滤入场**：
   - 做多：价格 ≥ 当前价格 + ATR × `atr_entry_mult`
   - 做空：价格 ≤ 当前价格 - ATR × `atr_entry_mult`

### 止损规则

1. **硬止损**：
   - 做多：价格 ≤ 入场价 - ATR × `atr_stop_mult`
   - 做空：价格 ≥ 入场价 + ATR × `atr_stop_mult`

2. **跟踪止损**：
   - 做多：最高价 - ATR × `atr_trail_mult`（只上移）
   - 做空：最低价 + ATR × `atr_trail_mult`（只下移）

### 日内平仓

- **夏令时**：北京时间 03:00（美东时间 15:00）强制平仓
- **冬令时**：北京时间 04:00（美东时间 15:00）强制平仓
- 平仓后当天不再开仓

## 参数配置

| 参数 | 值 | 说明 |
|------|-----|------|
| `kama_period` | 10 | KAMA 周期 |
| `kama_fast` | 2 | KAMA 快速平滑常数 |
| `kama_slow` | 30 | KAMA 慢速平滑常数 |
| `atr_period` | 10 | ATR 周期 |
| `atr_entry_mult` | 0.5 | ATR 入场乘数 |
| `atr_stop_mult` | 1.5 | ATR 止损乘数 |
| `atr_trail_mult` | 2.0 | ATR 跟踪止损乘数 |
| `fixed_size` | 1 | 固定仓位 |

## 回测结果

### RTY（2025-07-01 ~ 2025-12-15）

| 指标 | 结果 |
|------|------|
| **Sharpe Ratio** | 0.87 |
| **总交易次数** | 206 |
| **最大回撤** | -14.2% |

### ES（2024-06-05 ~ 2025-12-15）

| 指标 | 结果 |
|------|------|
| **Sharpe Ratio** | **2.36** |
| **总交易次数** | 239 |
| **最大回撤** | -21.0% |

![ES 回测资金曲线](/raw/assets/kama_atr_rty_trend_es_chart.png)
![RTY 回测资金曲线](/raw/assets/kama_atr_rty_trend_rty_chart.png)

## 实现细节

### 夏令时/冬令时自动判断

```python
def is_dst(date):
    year = date.year
    # 3月第2个周日
    march = datetime(year, 3, 1)
    while march.weekday() != 6:  # 周日=6
        march += timedelta(days=1)
    dst_start = march + timedelta(days=7)
    # 11月第1个周日
    november = datetime(year, 11, 1)
    while november.weekday() != 6:
        november += timedelta(days=1)
    dst_end = november
    return dst_start.date() <= date <= dst_end.date()
```

### 平仓逻辑修复

原 `send_orders` 存在 bug：当 `target=0, pos=-1` 时，`0 > -1` 为 True，导致执行 `buy` 而非 `cover`。

修复后优先判断 `target == 0` 的情况，确保正确平仓。

## 品种适配

| 品种 | 表现 | 备注 |
|------|------|------|
| ES | ⭐⭐⭐⭐⭐ Sharpe 2.36 | 强烈推荐 |
| RTY | ⭐⭐⭐ Sharpe 0.87 | 可接受 |

## 代码位置

- 策略文件：`/root/.openclaw/workspace/strategy_factory/generated/kama_atr_rty_trend_strategy.py`
- 配置 YAML：`/root/.openclaw/workspace/strategy_factory/strategies/inbox/kama_atr_rty_trend.yaml`

## 状态

- [x] 策略复现
- [x] OAT 参数优化
- [x] 多品种测试（RTY + ES）
- [x] 日内平仓逻辑修复
- [x] 夏令时/冬令时自动判断
- [x] 图表生成
- [x] Wiki 文档更新
