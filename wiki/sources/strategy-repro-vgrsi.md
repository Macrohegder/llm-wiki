---
id: strategy-repro-vgrsi
title: "Strategy Repro: vgrsi"
source: "Strategy Factory"
reproduced_at: 2026-05-07
status: completed
rating: red
source_note: vgrsi
---

# vgrsi — 策略复现报告

## 原文信息
- **策略 ID**: `vgrsi`
- **复现日期**: 2026-05-07
- **评估报告**: `reports/eval_vgrsi_20260507_104546.json`

## 回测结果汇总

| 指标 | 数值 |
|------|------|
| 🟢 Green | 0 |
| 🟡 Yellow | 0 |
| 🔴 Red | 2 |
| 总计 | 2 |

## 各品种详细结果

| 品种 | 评级 | Sharpe | 交易数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|--------|----------|----------|--------|
| BTCUSDT_SWAP_OKX.GLOBAL | 🔴 Red | -8.852 | 300 | -23.74% | -95.27% | -23.49% |
| ETHUSDT_SWAP_OKX.GLOBAL | 🔴 Red | -4.066 | 316 | -5.04% | -14.49% | -3.57% |

## 最优参数（最佳品种）

| 参数 | 最优值 |
|------|--------|
| aggregation_mode | A0 |
| fixed_size | 1 |
| long_threshold | 30 |
| max_positions | 2 |
| min_trade_interval | 30 |
| price_add_rate | 0.0 |
| short_threshold | 70 |
| sl_tp_lookback | 20 |
| sl_tp_multiplier | 5.0 |
| ws_1m | 20 |
| ws_30m | 20 |
| ws_5m | 20 |
| wv_1m | 20 |
| wv_30m | 20 |
| wv_5m | 20 |

## 复现产物

- YAML: `strategies/inbox/vgrsi.yaml`
- 代码: `generated/vgrsi_strategy.py`
- 评估报告: `reports/eval_vgrsi_20260507_104546.json`

## 历史复现记录

| 日期 | 事件 | 结果 |
|------|------|------|
| 2026-05-07 | 自动同步 | 见本报告 |

---

*自动同步于 2026-05-07*