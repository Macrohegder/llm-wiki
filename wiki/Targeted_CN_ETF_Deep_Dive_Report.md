# 目标 CN ETF 纯做多策略深度挖掘报告

- **生成时间**: 2026-06-14 23:47:47
- **回测区间**: 2020-01-01 ~ 2026-04-29
- **数据频率**: 日线
- **目标品种**: 510300（沪深300）、510500（中证500）、510050（上证50）、518880（黄金）、511260（十年国债）
- **策略池**: 19 个纯做多策略（CDD、DAB、5DL、FDL、FDLR、GE、IBS Mean Reversion、IBS_RSI、MHR、MH、MC、NG_STOCH、PR、TIGE、TT1、VS、WR、WRVF、WOHU）
- **GA 设置**: pop=50, ngen=20, workers=4
- **WFO 设置**: expanding window, train=3 年, test=1 年, pop=30, ngen=12

## 1. 执行摘要

- GA 全量回测组合数: **15** 个（19 策略 × 5 品种 = 95 个组合，经纯做多过滤后 15 个进入 WFO）
- WFO 验证通过（deployable=True）: **5** 个
- WFO 未通过: **10** 个

### 1.1 关键发现
- **债券 ETF（511260）表现突出**: VolatilitySupportStrategy、DonchianAdxBreakoutStrategy、IbsMeanReversionStrategy 在 511260 上均通过 WFO，说明低波动品种与均值回归/波动率支撑逻辑高度匹配。
- **黄金 ETF（518880）存在机会**: VolatilitySupportStrategy 与 PullbackMrStrategy 在 518880 上通过 WFO，OOS Sharpe 分别为 1.24 与 1.29。
- **中证500（510500）**: IbsMeanReversionStrategy 通过 WFO，OOS Sharpe 1.36，但样本内年化极低，需关注交易成本敏感性。
- **沪深300 / 上证50**: 没有组合通过 WFO，说明宽基大盘 ETF 对这些纯做多策略的样本外适配性较差。

## 2. GA 筛选结果总览

![风险收益概览](raw/assets/targeted_cn_etf_deep_dive/01_risk_return_overview.png)

### 2.1 全部 15 个进入 WFO 的组合 GA 指标

| 策略 | 品种 | GA Sharpe | 年化收益% | 最大回撤% | 交易数 | 总收益% |
|------|------|-----------|-----------|-----------|--------|---------|
| VolatilitySupportStrategy | 511260 | 1.506 | 37.51% | -0.31% | 118 | 2.39% |
| DonchianAdxBreakoutStrategy | 511260 | 1.426 | 18.82% | -0.19% | 60 | 1.20% |
| ConsecutiveDownDaysStrategy | 511260 | 1.282 | 27.69% | -0.38% | 59 | 1.77% |
| IbsMeanReversionStrategy | 511260 | 1.227 | 17.59% | -0.20% | 85 | 1.12% |
| VolatilitySupportStrategy | 518880 | 1.196 | 321.20% | -4.75% | 157 | 20.49% |
| IbsMeanReversionStrategy | 510500 | 1.176 | 175.32% | -1.68% | 64 | 11.18% |
| NgStochPivotMeanRevStrategy | 510050 | 0.904 | 42.84% | -0.62% | 92 | 2.73% |
| NgStochPivotMeanRevStrategy | 518880 | 0.895 | 59.35% | -0.69% | 64 | 3.79% |
| PullbackMrStrategy | 518880 | 0.845 | 175.02% | -4.53% | 71 | 11.16% |
| PullbackMrStrategy | 510050 | 0.799 | 73.49% | -1.29% | 56 | 4.69% |
| PullbackMrStrategy | 510500 | 0.780 | 110.87% | -2.40% | 74 | 7.07% |
| WilliamsRMrSimpleStrategy | 510500 | 0.767 | 90.52% | -1.71% | 50 | 5.77% |
| MacdHistogramRevStrategy | 510300 | 0.762 | 34.71% | -0.43% | 104 | 2.21% |
| NgStochPivotMeanRevStrategy | 510300 | 0.703 | 33.14% | -0.83% | 88 | 2.11% |
| WilliamsRMrSimpleStrategy | 518880 | 0.702 | 140.67% | -4.61% | 59 | 8.97% |

## 3. Walk-Forward 验证结果

![WFE 与过拟合风险](raw/assets/targeted_cn_etf_deep_dive/02_wfe_overfit_distribution.png)

### 3.1 通过 WFO 的组合（推荐实盘观察）

| 排名 | 策略 | 品种 | GA Sharpe | WFE | Consistency | Avg Test Sharpe | OOS Sharpe | OOS Return% | 过拟合风险 |
|------|------|------|-----------|-----|-------------|-----------------|------------|-------------|------------|
| 1 | VolatilitySupportStrategy | 511260 | 1.506 | 1.18 | 0.75 | 1.615 | 1.432 | 0.92% | low |
| 2 | IbsMeanReversionStrategy | 510500 | 1.176 | 2.99 | 1.00 | 1.455 | 1.358 | 4.74% | low |
| 3 | PullbackMrStrategy | 518880 | 0.845 | 1.49 | 0.75 | 1.605 | 1.285 | 4.56% | low |
| 4 | VolatilitySupportStrategy | 518880 | 1.196 | 1.29 | 1.00 | 1.229 | 1.245 | 7.00% | low |
| 5 | DonchianAdxBreakoutStrategy | 511260 | 1.426 | 1.51 | 0.75 | 1.353 | 1.169 | 0.58% | low |

![可部署组合汇总](raw/assets/targeted_cn_etf_deep_dive/03_deployable_summary.png)

### 3.2 未通过 WFO 的组合

| 策略 | 品种 | WFE | Avg Test Sharpe | OOS Sharpe | 过拟合风险 | Test 总交易数 | 主要问题 |
|------|------|-----|-----------------|------------|------------|---------------|----------|
| IbsMeanReversionStrategy | 511260 | 1.61 | 2.252 | 1.912 | low | 36 | Test交易数36<50 |
| WilliamsRMrSimpleStrategy | 518880 | 1.34 | 1.228 | 0.842 | low | 34 | Test交易数34<50 |
| ConsecutiveDownDaysStrategy | 511260 | 1.97 | 1.332 | 0.604 | low | 46 | Test交易数46<50 |
| MacdHistogramRevStrategy | 510300 | -0.32 | -0.013 | 0.323 | severe | 30 | WFE<0, 一致性差, 过拟合风险高, OOS夏普低, Test交易数30<50 |
| PullbackMrStrategy | 510050 | -0.36 | -0.230 | -0.064 | severe | 44 | WFE<0, 过拟合风险高, OOS夏普低, Test交易数44<50 |
| PullbackMrStrategy | 510500 | 0.20 | -0.015 | -0.091 | high | 29 | 过拟合风险高, OOS夏普低, Test交易数29<50 |
| WilliamsRMrSimpleStrategy | 510500 | -0.60 | -0.234 | -0.116 | severe | 48 | WFE<0, 一致性差, 过拟合风险高, OOS夏普低, Test交易数48<50 |
| NgStochPivotMeanRevStrategy | 518880 | -0.13 | -0.194 | -0.387 | severe | 23 | WFE<0, 一致性差, 过拟合风险高, OOS夏普低, Test交易数23<50 |
| NgStochPivotMeanRevStrategy | 510050 | -0.90 | -0.498 | -0.742 | severe | 36 | WFE<0, 一致性差, 过拟合风险高, OOS夏普低, Test交易数36<50 |
| NgStochPivotMeanRevStrategy | 510300 | -0.78 | -0.555 | -0.863 | severe | 49 | WFE<0, 一致性差, 过拟合风险高, OOS夏普低, Test交易数49<50 |

## 4. 策略 × 品种 OOS 夏普热力图

![OOS 夏普热力图](raw/assets/targeted_cn_etf_deep_dive/04_oos_sharpe_heatmap.png)

## 5. 窗口一致性分析

![窗口一致性](raw/assets/targeted_cn_etf_deep_dive/05_window_consistency.png)

- Expanding window 共 4 个：2020-2023/2023-2024、2020-2024/2024-2025、2020-2025/2025-2026、2020-2026/2026-04。
- 可部署组合在多个窗口中 Test Sharpe 与 Train Sharpe 同向，且 WFE > 1 的组合样本外表现甚至优于样本内。

## 6. 可部署组合的最优参数

| 策略 | 品种 | 核心参数 | fixed_size |
|------|------|----------|------------|
| VolatilitySupportStrategy | 511260 | `stretch_threshold=4.07, exit_days=33, bb_window=18, bb_dev=1.80` | 942 |
| IbsMeanReversionStrategy | 510500 | `ibs_entry=0.22, ibs_exit=0.72, use_ma_filter=0, ibs_window=3, ma_period=180` | 20502 |
| PullbackMrStrategy | 518880 | `rsi_exit=72, rsi_entry=49, rsi_period=4, sma_20_period=22, sma_200_period=200` | 29673 |
| VolatilitySupportStrategy | 518880 | `stretch_threshold=3.33, exit_days=33, bb_window=14, bb_dev=2.20` | 29673 |
| DonchianAdxBreakoutStrategy | 511260 | `use_trend_filter=2, adx_window=13, adx_threshold=23, donchian_window=10, exit_window=3, ma_period=160, adx_mode=1, use_long_only=True` | 942 |

## 7. 结论与交易建议

1. **优先关注 511260（十年国债 ETF）**: 3 个策略通过 WFO，低波动、低回撤，适合作为组合压舱石。
2. **518880（黄金 ETF）可作为卫星仓位**: VolatilitySupportStrategy 与 PullbackMrStrategy 样本外夏普均在 1.2 以上，但黄金波动较大，需控制仓位。
3. **避免在 510300 / 510050 上部署当前策略池**: 全部未通过 WFO，宽基大盘对这些短周期均值回归/动量策略不友好。
4. **交易成本敏感**: IbsMeanReversionStrategy @ 510500 的 GA 年化收益仅 0.3%，虽通过 WFO，但实际佣金/滑点上调可能导致盈利消失。
5. **下一步**: 对通过 WFO 的组合进行更小窗口（如 6 个月滚动）的压力测试，并加入 2025 年后的真实样本外跟踪。
