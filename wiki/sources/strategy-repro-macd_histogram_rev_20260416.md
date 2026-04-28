---
id: strategy-repro-macd_histogram_rev_20260416
title: "Strategy Repro: macd_histogram_rev_20260416"
source: "Strategy Factory"
reproduced_at: 2026-04-28
status: completed
rating: green
source_note: macd_histogram_rev_20260416
---

# macd_histogram_rev_20260416 — 策略复现报告

## 原文信息
- **策略 ID**: `macd_histogram_rev_20260416`
- **复现日期**: 2026-04-28
- **评估报告**: `reports/eval_macd_histogram_rev_20260416_20260428_233544.json`

## 回测结果汇总

| 指标 | 数值 |
|------|------|
| 🟢 Green | 1 |
| 🟡 Yellow | 0 |
| 🔴 Red | 3 |
| 总计 | 4 |

## 各品种详细结果

| 品种 | 评级 | Sharpe | 交易数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|--------|----------|----------|--------|
| SPY | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |
| QQQ | 🟢 Green | 1.397 | 152 | -34.35% | 63.95% | 317.21% |
| IWM | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |
| GLD | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |

## 最优参数（最佳品种）

| 参数 | 最优值 |
|------|--------|
| decline_days | 2 |
| fast_period | 11 |
| signal_period | 9 |
| slow_period | 41 |

## 回测图表

![[raw/assets/strategy_charts/macd_histogram_rev_20260416/macdhistogramrev20260416strategy_spy_chart.png]]
![[raw/assets/strategy_charts/macd_histogram_rev_20260416/macdhistogramrev20260416strategy_qqq_chart.png]]
![[raw/assets/strategy_charts/macd_histogram_rev_20260416/macdhistogramrev20260416strategy_iwm_chart.png]]
![[raw/assets/strategy_charts/macd_histogram_rev_20260416/macdhistogramrev20260416strategy_gld_chart.png]]

## 复现产物

- YAML: `strategies/inbox/macd_histogram_rev_20260416.yaml`
- 代码: `generated/macd_histogram_rev_20260416_strategy.py`
- 评估报告: `reports/eval_macd_histogram_rev_20260416_20260428_233544.json`

---

*自动同步于 2026-04-28*