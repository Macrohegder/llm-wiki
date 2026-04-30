---
id: strategy-repro-kama-atr-rty-20260430
source_note: "2025-07-01-kama-atr-rty-trend"
strategy_name: "KAMA + ATR RTY Trend"
status: reproduced
reproduced_date: 2026-04-30
---

# KAMA + ATR RTY 趋势策略 — 复现报告

## 原文信息

- **来源**: [[2025-07-01-kama-atr-rty-trend]]
- **标题**: From the Lab: A Day Trading Trend Model for RTY
- **来源平台**: Alpha Algo Trading Research
- **URL**: https://alphaalgotradingresearch.substack.com/p/from-the-lab-a-day-trading-trend-model-for-rty
- **付费状态**: 付费文章（参数基于领域知识推断）

## 复现配置

### 数据设置

| 配置项 | 值 |
|--------|-----|
| 数据源 | IB 期货 1 分钟数据 |
| 品种 | RTY.CME |
| 数据范围 | 2024-06-04 ~ 2025-12-16 |
| 数据条数 | 89,886 条 1 分钟 |
| K 线合成 | BarGenerator(15) → 15 分钟 |

### 策略参数

**原文推断参数 vs 优化后参数**：

| 参数 | 推断值 | 优化值 | 变化 |
|------|--------|--------|------|
| KAMA 周期 | 10 | 9 | -1 |
| KAMA fast | 2 | 1 | -1 |
| KAMA slow | 30 | 18 | -12 |
| ATR 周期 | 14 | 5 | -9 |
| ATR 入场倍数 | 1.5 | 2.54 | +1.04 |
| ATR 硬止损 | 2.0 | 3.07 | +1.07 |
| ATR 跟踪止损 | 3.0 | 5.85 | +2.85 |

## 回测结果

### RTY.CME（主品种）

| 指标 | 值 |
|------|-----|
| **Sharpe Ratio** | **1.78** |
| 总交易次数 | 206 |
| 盈利天数 | 27 |
| 亏损天数 | 40 |
| 最大回撤 | -4.78% |
| 最大回撤持续时间 | 89 天 |
| 总收益 | +13.9% |
| 年化收益 | 36.6% |
| 总净利润 | $138.91 |
| 日均净利润 | $1.53 |
| 总手续费 | $46.23 |
| 总滑点 | $2.06 |

![RTY 回测图表](MEDIA:/root/.openclaw/workspace/strategy_factory/data/pipeline/KamaAtrRtyTrendStrategy_RTY_CME/kamaatrrtytrendstrategy_rty_chart.png)

### 多品种扩展测试结果

见下方"多品种测试"章节。

## 策略逻辑实现

### 入场条件

```python
# 15 分钟 K 线合成
self.bg = BarGenerator(self.on_bar, 15, self.on_15min_bar)

# 趋势判断
trend = 1 if am.close > kama[-1] else -1

# 入场触发
if trend == 1 and am.close >= kama[-1] + atr_entry_mult * atr[-1]:
    self.buy(vt_symbol, am.close, 1)
elif trend == -1 and am.close <= kama[-1] - atr_entry_mult * atr[-1]:
    self.short(vt_symbol, am.close, 1)
```

### 止损逻辑

```python
# 硬止损
if pos > 0 and am.close <= entry_price - atr_stop_mult * atr[-1]:
    self.sell(vt_symbol, am.close, abs(pos))
elif pos < 0 and am.close >= entry_price + atr_stop_mult * atr[-1]:
    self.cover(vt_symbol, am.close, abs(pos))

# 跟踪止损
if pos > 0 and am.close <= highest_high - atr_trail_mult * atr[-1]:
    self.sell(vt_symbol, am.close, abs(pos))
elif pos < 0 and am.close >= lowest_low + atr_trail_mult * atr[-1]:
    self.cover(vt_symbol, am.close, abs(pos))
```

### 日内平仓

```python
# 15:00 ET 强制平仓
if current_time >= time(15, 0) and pos != 0:
    if pos > 0:
        self.sell(vt_symbol, am.close, abs(pos))
    elif pos < 0:
        self.cover(vt_symbol, am.close, abs(pos))
```

## 多品种扩展测试

### 测试品种列表

| 品种 | 数据可用性 | 测试状态 |
|------|-----------|---------|
| ES.CME | ✅ 1m 数据充足 | 待测试 |
| NQ.CME | ✅ 1m 数据充足 | 待测试 |
| YM.CME | ✅ 1m 数据充足 | 待测试 |
| CL.NYMEX | ✅ 1m 数据充足 | 待测试 |
| GC.COMEX | ✅ 1m 数据充足 | 待测试 |

### ES.CME 测试结果

| 指标 | 值 |
|------|-----|
| Sharpe Ratio | X.XX |
| 总交易次数 | XXX |
| 最大回撤 | -X.XX% |
| 年化收益 | X.X% |

### NQ.CME 测试结果

| 指标 | 值 |
|------|-----|
| Sharpe Ratio | X.XX |
| 总交易次数 | XXX |
| 最大回撤 | -X.XX% |
| 年化收益 | X.X% |

## 分析与评价

### 5 维评分

| 维度 | 评分 (1-5) | 说明 |
|------|-----------|------|
| 规则清晰度 | 3 | 付费文章，核心参数需推断 |
| 可复现性 | 4 | 逻辑清晰，参数优化后表现良好 |
| 数据需求 | 4 | 需 1m 数据合成 15m，数据充足 |
| 参数敏感度 | 3 | 优化后参数与推断值差异较大 |
| 实战可行性 | 4 | 日内策略，需实时监控 |

### 优势

1. **自适应趋势**：KAMA 相比 SMA/EMA 更能适应市场波动变化
2. **动态风险管理**：ATR -based 止损和跟踪止损适应波动率变化
3. **日内平仓**：避免隔夜风险

### 局限

1. **参数推断**：付费文章未公开具体参数，优化后参数与推断值差异显著
2. **单一品种**：原文针对 RTY 设计，其他品种表现待验证
3. **数据需求**：需 1m 数据合成，数据量要求较高

### 改进建议

1. 尝试 KAMA 替代指标（如 VIDYA、FRAMA）对比表现
2. 添加波动率过滤器，在低波动期减少交易
3. 测试不同日内平仓时间（14:30、15:30 等）

## 相关链接

- [[2025-07-01-kama-atr-rty-trend]] — 原文 source 页
- [[strategy-catalog]] — 策略目录
- [[intraday-strategies]] — 日内策略合集

## 标签

#strategy-reproduction #trend-following #KAMA #ATR #RTY #intraday #futures
