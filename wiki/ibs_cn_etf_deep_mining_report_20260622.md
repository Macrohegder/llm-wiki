# IbsMeanReversionStrategy 全 CN ETF 深度挖掘报告

- 生成时间: 2026-06-22
- 策略: IbsMeanReversionStrategy
- 标的范围: 110 只 CN ETF（上交所 72 + 深交所 38）
- 回测区间: 2020-01-01 ~ 2026-04-29
- GA 参数: pop=50, ngen=20, workers=4
- WFO 参数: expanding, train=3y, test=1y, pop=30, ngen=12

## 策略逻辑
- IBS = (Close - Low) / (High - Low)，取最近 `ibs_window` 天均值
- 做多条件：IBS < `ibs_entry`
- 平仓条件：IBS > `ibs_exit`
- 可选 MA 过滤：当 `use_ma_filter=1` 时，要求 close > MA(`ma_period`)

## GA 批量回测结果

| 统计项 | 数值 |
|---|---|
| 总品种数 | 110 |
| GA 达标候选 | 22 |

## WFO 样本外验证结果

**可实盘组合数: 7 / 22**

| 品种 | WFE | Consistency | Avg Test Sharpe | Concat OOS Sharpe | OOS Trades | Risk | GA Sharpe |
|---|---|---:|---:|---:|---:|---|---:|
| 510500.SSE | 1.56 | 100% | 1.40 | 1.18 | 52 | low | 1.176 |
| 512100.SSE | 1.18 | 75% | 1.29 | 0.71 | 54 | low | 1.012 |
| 511380.SSE | 1.56 | 100% | 1.21 | 1.00 | 88 | low | 1.077 |
| 511180.SSE | 0.73 | 100% | 0.81 | 0.79 | 64 | low | 0.964 |
| 515220.SSE | 0.56 | 75% | 0.80 | 0.47 | 54 | low | 1.166 |
| 159792.SZSE | 1.03 | 75% | 0.69 | 0.90 | 68 | low | 0.963 |
| 513980.SSE | 0.96 | 50% | 0.60 | 0.97 | 64 | low | 1.138 |

## 可实盘组合参数

### 510500.SSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_510500_SSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 12929
  - `ibs_entry`: 0.22
  - `ibs_exit`: 0.72
  - `ibs_window`: 3
  - `ma_period`: 160
  - `use_ma_filter`: 0

### 512100.SSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_512100_SSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 32141
  - `ibs_entry`: 0.26
  - `ibs_exit`: 0.72
  - `ibs_window`: 3
  - `ma_period`: 160
  - `use_ma_filter`: 0

### 511380.SSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_511380_SSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 7212
  - `ibs_entry`: 0.26
  - `ibs_exit`: 0.5599999999999999
  - `ibs_window`: 3
  - `ma_period`: 200
  - `use_ma_filter`: 1

### 511180.SSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_511180_SSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 7777
  - `ibs_entry`: 0.22
  - `ibs_exit`: 0.72
  - `ibs_window`: 3
  - `ma_period`: 140
  - `use_ma_filter`: 0

### 515220.SSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_515220_SSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 96711
  - `ibs_entry`: 0.22
  - `ibs_exit`: 0.5599999999999999
  - `ibs_window`: 3
  - `ma_period`: 180
  - `use_ma_filter`: 0

### 159792.SZSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_159792_SZSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 113378
  - `ibs_entry`: 0.22
  - `ibs_exit`: 0.5599999999999999
  - `ibs_window`: 3
  - `ma_period`: 200
  - `use_ma_filter`: 0

### 513980.SSE
- WFO 汇总: `data/batch_results/ibs_cn_etf_wfo_20260622_233226/IbsMeanReversionStrategy_513980_SSE/wfo_summary.json`
- 最优参数:
  - `daily_end_minute`: 59
  - `fixed_size`: 134770
  - `ibs_entry`: 0.26
  - `ibs_exit`: 0.5599999999999999
  - `ibs_window`: 3
  - `ma_period`: 180
  - `use_ma_filter`: 0

## 风险提示
1. ETF 回测中的 `max_ddpercent` 字段因仓位计算方式可能出现异常百分比，实际 `balance` 回撤应作为更可靠的参考。
2. 部分品种（如 513980.SSE）consistency 仅为 50%，样本外稳定性一般。
3. 2025 年后上市的新 ETF 历史数据较短，WFO 窗口训练集不足，结果需谨慎对待。
4. 实盘部署前建议先用小仓位验证，并映射到实际主力合约/ETF 代码。

## 相关文件
- GA 批量回测报告: `data/batch_results/ibsmeanreversionstrategy_cn_etf_20260622_194700/report.csv`
- WFO 结果目录: `data/batch_results/ibs_cn_etf_wfo_20260622_233226`
- 实盘配置 JSON: `reports/ibs_cn_etf_live_configs_20260622.json`
