---
id: strategy-repro-rsi_range_momentum
title: "Strategy Repro: rsi_range_momentum"
source: "Strategy Factory"
reproduced_at: 2026-04-30
status: completed
rating: red
source_note: rsi_range_momentum
---

# rsi_range_momentum — 策略复现报告

## 原文信息
- **策略 ID**: `rsi_range_momentum`
- **原文摘要**: [[2026-04-04-RSI-Based-Range-Momentum-System]]
- **复现日期**: 2026-04-30
- **评估报告**: `reports/eval_rsi_range_momentum_20260430_093310.json`

## 回测结果汇总

| 指标 | 数值 |
|------|------|
| 🟢 Green | 0 |
| 🟡 Yellow | 0 |
| 🔴 Red | 5 |
| 总计 | 5 |

## 各品种详细结果

| 品种 | 评级 | Sharpe | 交易数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|--------|----------|----------|--------|
| SPY | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |
| QQQ | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |
| GLD | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |
| BTCUSDT_SWAP_OKX.GLOBAL | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |
| ETHUSDT_SWAP_OKX.GLOBAL | 🔴 Red | 0.000 | 0 | 0.00% | 0.00% | 0.00% |

## 最优参数（最佳品种）

| 参数 | 最优值 |
|------|--------|
| fixed_size | 1 |
| lookback_days | 100 |
| price_add_rate | 0.0 |
| rsi_bull_momentum_threshold | 70 |
| rsi_bull_range_high | 100 |
| rsi_bull_range_low | 40 |
| rsi_period | 14 |

## 回测图表

![[raw/assets/strategy_charts/rsi_range_momentum/rsirangemomentumstrategy_spy_chart.png]]
![[raw/assets/strategy_charts/rsi_range_momentum/rsirangemomentumstrategy_qqq_chart.png]]
![[raw/assets/strategy_charts/rsi_range_momentum/rsirangemomentumstrategy_gld_chart.png]]
![[raw/assets/strategy_charts/rsi_range_momentum/rsirangemomentumstrategy_btcusdt_swap_okx_chart.png]]
![[raw/assets/strategy_charts/rsi_range_momentum/rsirangemomentumstrategy_ethusdt_swap_okx_chart.png]]

## 复现产物

- YAML: `strategies/inbox/rsi_range_momentum.yaml`
- 代码: `generated/rsi_range_momentum_strategy.py`
- 评估报告: `reports/eval_rsi_range_momentum_20260430_093310.json`

## 历史复现记录

| 日期 | 事件 | 结果 |
|------|------|------|
| 2026-04-30 | 自动同步 | 见本报告 |

---

*自动同步于 2026-04-30*