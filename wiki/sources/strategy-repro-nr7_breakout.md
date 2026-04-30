---
id: strategy-repro-nr7_breakout
title: "Strategy Repro: nr7_breakout"
source: "Strategy Factory"
reproduced_at: 2026-04-30
status: completed
rating: green
source_note: nr7_breakout
---

# nr7_breakout — 策略复现报告

## 原文信息
- **策略 ID**: `nr7_breakout`
- **原文摘要**: [[strategy-repro-nr7-breakout]]
- **复现日期**: 2026-04-30
- **评估报告**: `reports/eval_nr7_breakout_20260430_083327.json`

## 回测结果汇总

| 指标 | 数值 |
|------|------|
| 🟢 Green | 4 |
| 🟡 Yellow | 0 |
| 🔴 Red | 3 |
| 总计 | 7 |

## 各品种详细结果

| 品种 | 评级 | Sharpe | 交易数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|--------|----------|----------|--------|
| SPY | 🟢 Green | 1.212 | 459 | -6.51% | 4.88% | 34.09% |
| QQQ | 🟢 Green | 1.149 | 413 | -6.88% | 7.37% | 42.53% |
| GLD | 🟢 Green | 1.027 | 162 | -1.44% | 1.43% | 8.24% |
| BTCUSDT_SWAP_OKX.GLOBAL | 🟢 Green | 1.021 | 300 | -13.42% | 12.54% | 76.49% |
| ETHUSDT_SWAP_OKX.GLOBAL | 🔴 Red | 0.703 | 334 | -10.84% | 6.33% | 38.57% |
| SOLUSDT_SWAP_OKX.GLOBAL | 🔴 Red | 0.396 | 266 | -9.41% | 2.49% | 12.32% |
| DOGEUSDT_SWAP_OKX.GLOBAL | 🔴 Red | 0.274 | 360 | -29.64% | 5.00% | 27.43% |

## 最优参数（最佳品种）

| 参数 | 最优值 |
|------|--------|
| nr_lookback | 3 |
| trend_ma_period | 15 |
| use_long_only | 1.06 |
| use_trend_filter | 0.7 |

## 回测图表

![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_spy_chart.png]]
![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_qqq_chart.png]]
![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_gld_chart.png]]
![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_btcusdt_swap_okx_chart.png]]
![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_ethusdt_swap_okx_chart.png]]
![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_solusdt_swap_okx_chart.png]]
![[raw/assets/strategy_charts/nr7_breakout/nr7breakoutstrategy_dogeusdt_swap_okx_chart.png]]

## 复现产物

- YAML: `strategies/inbox/nr7_breakout.yaml`
- 代码: `generated/nr7_breakout_strategy.py`
- 评估报告: `reports/eval_nr7_breakout_20260430_083327.json`

## 历史复现记录

| 日期 | 事件 | 结果 |
|------|------|------|
| 2026-04-30 | 自动同步 | 见本报告 |

---

*自动同步于 2026-04-30*