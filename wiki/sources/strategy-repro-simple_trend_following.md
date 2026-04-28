---
id: strategy-repro-simple_trend_following
title: "Strategy Repro: simple_trend_following"
source: "Strategy Factory"
reproduced_at: 2026-04-28
status: completed
rating: green
source_note: simple_trend_following
---

# simple_trend_following — 策略复现报告

## 原文信息
- **策略 ID**: `simple_trend_following`
- **复现日期**: 2026-04-28
- **评估报告**: `reports/eval_simple_trend_following_20260428_192347.json`

## 回测结果汇总

| 指标 | 数值 |
|------|------|
| 🟢 Green | 2 |
| 🟡 Yellow | 1 |
| 🔴 Red | 1 |
| 总计 | 4 |

## 各品种详细结果

| 品种 | 评级 | Sharpe | 交易数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|--------|----------|----------|--------|
| QQQ | 🟢 Green | 1.023 | 263 | -4.37% | 5.66% | 43.97% |
| GLD | 🟢 Green | 1.007 | 202 | -3.47% | 2.93% | 22.75% |
| SPY | 🟡 Yellow | 0.718 | 293 | -6.57% | 2.78% | 33.28% |
| IWM | 🔴 Red | 0.167 | 560 | -6.46% | 0.39% | 4.49% |

## 最优参数（最佳品种）

| 参数 | 最优值 |
|------|--------|
| cond_lookback_1 | 1 |
| cond_lookback_2 | 2 |
| fixed_stop_pct | 0.013 |
| ma_period | 33 |
| trailing_stop_pct | 0.0219 |

## 回测图表

![[raw/assets/strategy_charts/simple_trend_following/simpletrendfollowingstrategy_qqq_chart.png]]
![[raw/assets/strategy_charts/simple_trend_following/simpletrendfollowingstrategy_gld_chart.png]]
![[raw/assets/strategy_charts/simple_trend_following/simpletrendfollowingstrategy_spy_chart.png]]

## 复现产物

- YAML: `strategies/inbox/simple_trend_following.yaml`
- 代码: `generated/simple_trend_following_strategy.py`
- 评估报告: `reports/eval_simple_trend_following_20260428_192347.json`

---

*自动同步于 2026-04-28*