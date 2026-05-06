# RSI 批量回测报告

- 生成时间: 2026-05-06 08:07:44
- 回测截止: 2026-04-29
- 共 4 个品种完成

## Universe

| vt_symbol | 产品类型 | 持有区间 |
|---|---:|---:|
| BTCUSDT_SWAP_OKX.GLOBAL | BTC | 2020-01-01 ~ 2026-04-29 |
| ETHUSDT_SWAP_OKX.GLOBAL | ETH | 2020-01-01 ~ 2026-04-29 |
| SOLUSDT_SWAP_OKX.GLOBAL | SOL | 2020-01-01 ~ 2026-04-29 |
| XAUUSDT_SWAP_OKX.GLOBAL | XAU | 2020-01-01 ~ 2026-04-29 |

## Top 50 结果（按夏普降序）

| 排名 | 品种 | 产品类型 | 夏普 | 年化收益% | 总收益% | 最大回撤% | 交易笔数 | 胜率% |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | XAUUSDT_SWAP_OKX.GLOBAL | XAU | 0.13 | 0.00 | 0.00 | -0.00 | 6 | N/A |
| 2 | BTCUSDT_SWAP_OKX.GLOBAL | BTC | -0.01 | -0.00 | -0.00 | -0.03 | 62 | N/A |
| 3 | ETHUSDT_SWAP_OKX.GLOBAL | ETH | -0.08 | -0.00 | -0.01 | -0.02 | 110 | N/A |
| 4 | SOLUSDT_SWAP_OKX.GLOBAL | SOL | -0.52 | -0.03 | -0.14 | -0.23 | 54 | N/A |

## 最优参数

| 品种 | atr_window | auto_daily_end | capital | contract_size | daily_end_hour | daily_end_minute | risk_percent | rsi_buy_threshold | rsi_exit_mean | rsi_sell_threshold | rsi_window | sl_atr_multiplier |
|------|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT_SWAP_OKX.GLOBAL | 16 | True | 1000000 | 300 | 14 | 59 | 0.020 | 33 | 50 | 82 | 13 | 2.200 |
| ETHUSDT_SWAP_OKX.GLOBAL | 13 | True | 1000000 | 300 | 14 | 59 | 0.020 | 33 | 50 | 82 | 10 | 2.600 |
| SOLUSDT_SWAP_OKX.GLOBAL | 13 | True | 1000000 | 300 | 14 | 59 | 0.020 | 33 | 50 | 82 | 13 | 1.400 |
| XAUUSDT_SWAP_OKX.GLOBAL | 13 | True | 1000000 | 300 | 14 | 59 | 0.020 | 27 | 50 | 82 | 16 | 2.600 |

## 可实盘候选

- 无

---

