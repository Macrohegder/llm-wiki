---
tags:
  - mining
  - cn-etf
  - cta-developer
created: "2026-06-14"
---

# CN ETF 策略挖掘结果汇总 (2026-06)

> 来源: `cta_developer` CN ETF 批量挖掘
> 生成时间: 2026-06-14 11:55:01
> 筛选标准: Sharpe > 0.8 且 交易次数 > 50
> 额外过滤: 仅保留实际回测中无空头交易的组合（国内 ETF 不能做空）

## 概览

- 达标策略数: **19**
- 达标品种数: **152**

### 按策略统计

| 策略 | 达标品种数 | 最佳品种 | 最佳 Sharpe |
|------|-----------|----------|------------|
| ConsecutiveDownDaysStrategy | 5 | 159816.SZSE | 1.214 |
| DonchianAdxBreakoutStrategy | 3 | 511360.SSE | 6.062 |
| FiveDayLowOvernightStrategy | 2 | 513920.SSE | 1.560 |
| FiveDayLowRangeStrategy | 7 | 513920.SSE | 1.675 |
| FiveDayLowStrategy | 10 | 513920.SSE | 1.772 |
| GoldEnvelopeStrategy | 3 | 515080.SSE | 0.981 |
| IbsMeanReversionStrategy | 15 | 511260.SSE | 1.502 |
| IbsRsiMeanReversionStrategy | 9 | 159326.SZSE | 1.317 |
| MacdHistogramRevStrategy | 5 | 513050.SSE | 0.976 |
| MacdHistogramStrategy | 8 | 159516.SZSE | 1.532 |
| MarketConditionStrategy | 6 | 159980.SZSE | 0.976 |
| NgStochPivotMeanRevStrategy | 21 | 515080.SSE | 1.321 |
| PullbackMrStrategy | 8 | 588220.SSE | 1.318 |
| TigerRsiStrategy | 3 | 159816.SZSE | 1.397 |
| Tt1Strategy | 1 | 511360.SSE | 2.333 |
| VolatilitySupportStrategy | 25 | 159650.SZSE | 2.431 |
| WilliamsRMrSimpleStrategy | 3 | 511030.SSE | 0.983 |
| WilliamsRVolFilterStrategy | 16 | 561380.SSE | 2.210 |
| WohuStrategy | 2 | 159816.SZSE | 1.348 |

## ConsecutiveDownDaysStrategy

达标品种数: **5**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159816 | SZSE | 1.214 | 94 | 11.95% | -0.10% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/ConsecutiveDownDaysStrategy/159816_SZSE.png) |
| 588200 | SSE | 1.130 | 56 | 391.82% | -3.07% | ![588200](MEDIA:raw/assets/cn_etf_mining_2026-06/ConsecutiveDownDaysStrategy/588200_SSE.png) |
| 511220 | SSE | 0.907 | 111 | 14.23% | -0.29% | ![511220](MEDIA:raw/assets/cn_etf_mining_2026-06/ConsecutiveDownDaysStrategy/511220_SSE.png) |
| 515450 | SSE | 0.905 | 118 | 121.65% | -1.31% | ![515450](MEDIA:raw/assets/cn_etf_mining_2026-06/ConsecutiveDownDaysStrategy/515450_SSE.png) |
| 562800 | SSE | 0.850 | 55 | 97.14% | -2.12% | ![562800](MEDIA:raw/assets/cn_etf_mining_2026-06/ConsecutiveDownDaysStrategy/562800_SSE.png) |

## DonchianAdxBreakoutStrategy

达标品种数: **3**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 511360 | SSE | 6.062 | 59 | 13.23% | -0.03% | ![511360](MEDIA:raw/assets/cn_etf_mining_2026-06/DonchianAdxBreakoutStrategy/511360_SSE.png) |
| 511220 | SSE | 2.130 | 67 | 21.90% | -0.13% | ![511220](MEDIA:raw/assets/cn_etf_mining_2026-06/DonchianAdxBreakoutStrategy/511220_SSE.png) |
| 513500 | SSE | 0.909 | 93 | 93.22% | -1.47% | ![513500](MEDIA:raw/assets/cn_etf_mining_2026-06/DonchianAdxBreakoutStrategy/513500_SSE.png) |

## FiveDayLowOvernightStrategy

达标品种数: **2**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 513920 | SSE | 1.560 | 68 | 111.42% | -0.47% | ![513920](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowOvernightStrategy/513920_SSE.png) |
| 159509 | SZSE | 0.974 | 70 | 230.50% | -1.48% | ![159509](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowOvernightStrategy/159509_SZSE.png) |

## FiveDayLowRangeStrategy

达标品种数: **7**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 513920 | SSE | 1.675 | 60 | 142.06% | -0.63% | ![513920](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/513920_SSE.png) |
| 588220 | SSE | 1.402 | 74 | 291.12% | -2.77% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/588220_SSE.png) |
| 588200 | SSE | 1.191 | 100 | 315.11% | -3.36% | ![588200](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/588200_SSE.png) |
| 513630 | SSE | 1.039 | 56 | 81.40% | -0.79% | ![513630](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/513630_SSE.png) |
| 513310 | SSE | 1.034 | 90 | 422.19% | -3.15% | ![513310](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/513310_SSE.png) |
| 513120 | SSE | 0.896 | 108 | 131.77% | -2.20% | ![513120](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/513120_SSE.png) |
| 513130 | SSE | 0.836 | 102 | 74.73% | -0.97% | ![513130](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowRangeStrategy/513130_SSE.png) |

## FiveDayLowStrategy

达标品种数: **10**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 513920 | SSE | 1.772 | 109 | 0.00% | -0.00% | ![513920](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/513920_SSE.png) |
| 159566 | SZSE | 1.621 | 127 | 0.00% | -0.00% | ![159566](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/159566_SZSE.png) |
| 513630 | SSE | 1.317 | 107 | 0.00% | -0.00% | ![513630](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/513630_SSE.png) |
| 159570 | SZSE | 1.198 | 93 | 0.00% | -0.00% | ![159570](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/159570_SZSE.png) |
| 159326 | SZSE | 1.147 | 81 | 0.00% | -0.00% | ![159326](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/159326_SZSE.png) |
| 513120 | SSE | 0.992 | 157 | 0.00% | -0.00% | ![513120](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/513120_SSE.png) |
| 159509 | SZSE | 0.979 | 86 | 0.00% | -0.00% | ![159509](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/159509_SZSE.png) |
| 513500 | SSE | 0.841 | 240 | 0.00% | -0.00% | ![513500](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/513500_SSE.png) |
| 517520 | SSE | 0.833 | 107 | 0.00% | -0.00% | ![517520](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/517520_SSE.png) |
| 563360 | SSE | 0.808 | 53 | 0.00% | -0.00% | ![563360](MEDIA:raw/assets/cn_etf_mining_2026-06/FiveDayLowStrategy/563360_SSE.png) |

## GoldEnvelopeStrategy

达标品种数: **3**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 515080 | SSE | 0.981 | 67 | 136.21% | -1.81% | ![515080](MEDIA:raw/assets/cn_etf_mining_2026-06/GoldEnvelopeStrategy/515080_SSE.png) |
| 515100 | SSE | 0.972 | 53 | 128.81% | -1.98% | ![515100](MEDIA:raw/assets/cn_etf_mining_2026-06/GoldEnvelopeStrategy/515100_SSE.png) |
| 510880 | SSE | 0.855 | 68 | 91.36% | -1.44% | ![510880](MEDIA:raw/assets/cn_etf_mining_2026-06/GoldEnvelopeStrategy/510880_SSE.png) |

## IbsMeanReversionStrategy

达标品种数: **15**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 511260 | SSE | 1.502 | 89 | 20.20% | -0.20% | ![511260](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/511260_SSE.png) |
| 515220 | SSE | 1.166 | 58 | 188.87% | -1.53% | ![515220](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/515220_SSE.png) |
| 513980 | SSE | 1.138 | 102 | 107.47% | -0.93% | ![513980](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/513980_SSE.png) |
| 510500 | SSE | 1.130 | 56 | 154.89% | -1.71% | ![510500](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/510500_SSE.png) |
| 511380 | SSE | 1.077 | 52 | 39.72% | -0.57% | ![511380](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/511380_SSE.png) |
| 511180 | SSE | 0.964 | 69 | 53.59% | -0.64% | ![511180](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/511180_SSE.png) |
| 159792 | SZSE | 0.956 | 58 | 88.33% | -1.12% | ![159792](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/159792_SZSE.png) |
| 515880 | SSE | 0.946 | 86 | 254.37% | -2.94% | ![515880](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/515880_SSE.png) |
| 562500 | SSE | 0.917 | 58 | 63.74% | -0.85% | ![562500](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/562500_SSE.png) |
| 518600 | SSE | 0.862 | 51 | 87.89% | -1.00% | ![518600](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/518600_SSE.png) |
| 159892 | SZSE | 0.858 | 52 | 107.40% | -1.27% | ![159892](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/159892_SZSE.png) |
| 512100 | SSE | 0.845 | 54 | 134.67% | -3.53% | ![512100](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/512100_SSE.png) |
| 516150 | SSE | 0.844 | 70 | 162.49% | -2.20% | ![516150](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/516150_SSE.png) |
| 513310 | SSE | 0.838 | 70 | 380.65% | -4.63% | ![513310](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/513310_SSE.png) |
| 159636 | SZSE | 0.824 | 68 | 119.32% | -1.44% | ![159636](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsMeanReversionStrategy/159636_SZSE.png) |

## IbsRsiMeanReversionStrategy

达标品种数: **9**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159326 | SZSE | 1.317 | 71 | 210.38% | -0.80% | ![159326](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/159326_SZSE.png) |
| 513310 | SSE | 1.146 | 164 | 308.74% | -2.22% | ![513310](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/513310_SSE.png) |
| 588170 | SSE | 1.122 | 52 | 264.66% | -1.08% | ![588170](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/588170_SSE.png) |
| 159363 | SZSE | 1.067 | 54 | 258.63% | -1.62% | ![159363](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/159363_SZSE.png) |
| 159570 | SZSE | 1.056 | 114 | 315.00% | -5.00% | ![159570](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/159570_SZSE.png) |
| 159566 | SZSE | 1.005 | 60 | 140.44% | -1.02% | ![159566](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/159566_SZSE.png) |
| 515080 | SSE | 0.882 | 60 | 35.44% | -0.41% | ![515080](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/515080_SSE.png) |
| 159636 | SZSE | 0.876 | 52 | 81.22% | -1.01% | ![159636](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/159636_SZSE.png) |
| 511380 | SSE | 0.821 | 56 | 24.27% | -0.30% | ![511380](MEDIA:raw/assets/cn_etf_mining_2026-06/IbsRsiMeanReversionStrategy/511380_SSE.png) |

## MacdHistogramRevStrategy

达标品种数: **5**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 513050 | SSE | 0.976 | 98 | 75.51% | -0.76% | ![513050](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/513050_SSE.png) |
| 159915 | SZSE | 0.885 | 58 | 65.20% | -0.61% | ![159915](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/159915_SZSE.png) |
| 159852 | SZSE | 0.833 | 62 | 57.53% | -0.76% | ![159852](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/159852_SZSE.png) |
| 588200 | SSE | 0.832 | 70 | 111.17% | -1.43% | ![588200](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/588200_SSE.png) |
| 510300 | SSE | 0.824 | 56 | 20.99% | -0.22% | ![510300](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/510300_SSE.png) |

## MacdHistogramStrategy

达标品种数: **8**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159516 | SZSE | 1.532 | 64 | 172.29% | -1.11% | ![159516](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/159516_SZSE.png) |
| 588200 | SSE | 1.167 | 52 | 117.10% | -0.57% | ![588200](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/588200_SSE.png) |
| 159852 | SZSE | 0.999 | 54 | 64.55% | -0.48% | ![159852](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/159852_SZSE.png) |
| 513050 | SSE | 0.940 | 80 | 66.03% | -0.76% | ![513050](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/513050_SSE.png) |
| 159901 | SZSE | 0.897 | 80 | 43.01% | -0.60% | ![159901](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/159901_SZSE.png) |
| 159819 | SZSE | 0.846 | 58 | 49.76% | -0.43% | ![159819](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/159819_SZSE.png) |
| 159915 | SZSE | 0.814 | 142 | 103.07% | -2.15% | ![159915](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/159915_SZSE.png) |
| 159892 | SZSE | 0.813 | 59 | 35.01% | -0.58% | ![159892](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramStrategy/159892_SZSE.png) |

## MarketConditionStrategy

达标品种数: **6**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159980 | SZSE | 0.976 | 120 | 0.00% | -0.00% | ![159980](MEDIA:raw/assets/cn_etf_mining_2026-06/MarketConditionStrategy/159980_SZSE.png) |
| 159326 | SZSE | 0.944 | 53 | 0.00% | -0.00% | ![159326](MEDIA:raw/assets/cn_etf_mining_2026-06/MarketConditionStrategy/159326_SZSE.png) |
| 563360 | SSE | 0.921 | 53 | 0.00% | -0.00% | ![563360](MEDIA:raw/assets/cn_etf_mining_2026-06/MarketConditionStrategy/563360_SSE.png) |
| 518880 | SSE | 0.893 | 315 | 0.00% | -0.00% | ![518880](MEDIA:raw/assets/cn_etf_mining_2026-06/MarketConditionStrategy/518880_SSE.png) |
| 517520 | SSE | 0.830 | 74 | 0.00% | -0.00% | ![517520](MEDIA:raw/assets/cn_etf_mining_2026-06/MarketConditionStrategy/517520_SSE.png) |
| 513500 | SSE | 0.814 | 158 | 0.00% | -0.00% | ![513500](MEDIA:raw/assets/cn_etf_mining_2026-06/MarketConditionStrategy/513500_SSE.png) |

## NgStochPivotMeanRevStrategy

达标品种数: **21**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 515080 | SSE | 1.321 | 64 | 75.80% | -0.74% | ![515080](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/515080_SSE.png) |
| 560860 | SSE | 1.259 | 52 | 141.05% | -0.79% | ![560860](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/560860_SSE.png) |
| 159816 | SZSE | 1.118 | 108 | 11.04% | -0.09% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/159816_SZSE.png) |
| 516650 | SSE | 1.083 | 82 | 174.85% | -2.14% | ![516650](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/516650_SSE.png) |
| 159901 | SZSE | 1.074 | 80 | 92.73% | -1.02% | ![159901](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/159901_SZSE.png) |
| 515220 | SSE | 1.067 | 64 | 132.06% | -1.40% | ![515220](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/515220_SSE.png) |
| 159915 | SZSE | 1.048 | 74 | 116.46% | -1.10% | ![159915](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/159915_SZSE.png) |
| 159611 | SZSE | 1.039 | 66 | 57.18% | -0.48% | ![159611](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/159611_SZSE.png) |
| 513690 | SSE | 1.032 | 60 | 42.24% | -0.41% | ![513690](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/513690_SSE.png) |
| 512400 | SSE | 1.014 | 88 | 174.30% | -2.08% | ![512400](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/512400_SSE.png) |
| 513310 | SSE | 0.984 | 54 | 381.48% | -5.36% | ![513310](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/513310_SSE.png) |
| 515880 | SSE | 0.978 | 54 | 97.63% | -0.95% | ![515880](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/515880_SSE.png) |
| 510880 | SSE | 0.946 | 118 | 62.93% | -1.09% | ![510880](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/510880_SSE.png) |
| 159980 | SZSE | 0.911 | 68 | 74.23% | -0.78% | ![159980](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/159980_SZSE.png) |
| 510050 | SSE | 0.904 | 92 | 42.84% | -0.62% | ![510050](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/510050_SSE.png) |
| 518880 | SSE | 0.895 | 64 | 59.35% | -0.69% | ![518880](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/518880_SSE.png) |
| 510180 | SSE | 0.873 | 72 | 33.46% | -0.32% | ![510180](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/510180_SSE.png) |
| 159949 | SZSE | 0.870 | 88 | 120.55% | -2.45% | ![159949](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/159949_SZSE.png) |
| 562800 | SSE | 0.851 | 64 | 80.75% | -1.65% | ![562800](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/562800_SSE.png) |
| 511380 | SSE | 0.833 | 56 | 28.89% | -0.57% | ![511380](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/511380_SSE.png) |
| 513090 | SSE | 0.826 | 58 | 86.21% | -0.84% | ![513090](MEDIA:raw/assets/cn_etf_mining_2026-06/NgStochPivotMeanRevStrategy/513090_SSE.png) |

## PullbackMrStrategy

达标品种数: **8**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 588220 | SSE | 1.318 | 66 | 215.29% | -1.52% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/588220_SSE.png) |
| 159816 | SZSE | 1.115 | 68 | 12.15% | -0.07% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/159816_SZSE.png) |
| 511030 | SSE | 0.985 | 66 | 10.18% | -0.18% | ![511030](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/511030_SSE.png) |
| 511260 | SSE | 0.896 | 56 | 14.17% | -0.27% | ![511260](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/511260_SSE.png) |
| 518880 | SSE | 0.848 | 63 | 170.28% | -4.54% | ![518880](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/518880_SSE.png) |
| 560860 | SSE | 0.846 | 67 | 160.83% | -3.98% | ![560860](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/560860_SSE.png) |
| 516650 | SSE | 0.831 | 51 | 180.83% | -3.97% | ![516650](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/516650_SSE.png) |
| 513500 | SSE | 0.804 | 90 | 100.85% | -1.75% | ![513500](MEDIA:raw/assets/cn_etf_mining_2026-06/PullbackMrStrategy/513500_SSE.png) |

## TigerRsiStrategy

达标品种数: **3**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159816 | SZSE | 1.397 | 58 | 16.55% | -0.07% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159816_SZSE.png) |
| 588220 | SSE | 0.923 | 52 | 58.73% | -0.38% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/588220_SSE.png) |
| 513630 | SSE | 0.836 | 52 | 72.40% | -0.85% | ![513630](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/513630_SSE.png) |

## Tt1Strategy

达标品种数: **1**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 511360 | SSE | 2.333 | 145 | 8.11% | -0.04% | ![511360](MEDIA:raw/assets/cn_etf_mining_2026-06/Tt1Strategy/511360_SSE.png) |

## VolatilitySupportStrategy

达标品种数: **25**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159650 | SZSE | 2.431 | 51 | 13.56% | -0.04% | ![159650](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159650_SZSE.png) |
| 159363 | SZSE | 2.353 | 55 | 1136.25% | -1.87% | ![159363](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159363_SZSE.png) |
| 511580 | SSE | 2.175 | 57 | 18.04% | -0.07% | ![511580](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511580_SSE.png) |
| 511520 | SSE | 2.023 | 52 | 41.89% | -0.29% | ![511520](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511520_SSE.png) |
| 511360 | SSE | 1.667 | 77 | 12.75% | -0.14% | ![511360](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511360_SSE.png) |
| 511220 | SSE | 1.470 | 93 | 31.28% | -0.43% | ![511220](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511220_SSE.png) |
| 511090 | SSE | 1.381 | 75 | 88.18% | -1.20% | ![511090](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511090_SSE.png) |
| 511260 | SSE | 1.359 | 114 | 31.40% | -0.31% | ![511260](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511260_SSE.png) |
| 159816 | SZSE | 1.275 | 94 | 30.58% | -0.16% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159816_SZSE.png) |
| 159566 | SZSE | 1.229 | 63 | 483.63% | -2.95% | ![159566](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159566_SZSE.png) |
| 517520 | SSE | 1.179 | 85 | 636.94% | -5.03% | ![517520](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/517520_SSE.png) |
| 518880 | SSE | 1.171 | 151 | 311.08% | -4.78% | ![518880](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/518880_SSE.png) |
| 513310 | SSE | 1.135 | 114 | 684.72% | -7.22% | ![513310](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/513310_SSE.png) |
| 159516 | SZSE | 1.134 | 76 | 377.29% | -3.05% | ![159516](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159516_SZSE.png) |
| 513920 | SSE | 1.115 | 55 | 256.26% | -1.52% | ![513920](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/513920_SSE.png) |
| 518600 | SSE | 1.094 | 147 | 231.80% | -3.91% | ![518600](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/518600_SSE.png) |
| 511100 | SSE | 1.084 | 55 | 22.55% | -0.29% | ![511100](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/511100_SSE.png) |
| 513750 | SSE | 1.009 | 101 | 257.28% | -2.42% | ![513750](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/513750_SSE.png) |
| 560860 | SSE | 1.003 | 89 | 306.37% | -4.66% | ![560860](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/560860_SSE.png) |
| 159980 | SZSE | 0.955 | 132 | 221.72% | -3.85% | ![159980](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159980_SZSE.png) |
| 159326 | SZSE | 0.954 | 51 | 279.14% | -2.99% | ![159326](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/159326_SZSE.png) |
| 513630 | SSE | 0.927 | 51 | 187.48% | -1.69% | ![513630](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/513630_SSE.png) |
| 515880 | SSE | 0.908 | 249 | 348.33% | -6.67% | ![515880](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/515880_SSE.png) |
| 512890 | SSE | 0.895 | 139 | 157.93% | -1.61% | ![512890](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/512890_SSE.png) |
| 513500 | SSE | 0.866 | 111 | 215.70% | -4.33% | ![513500](MEDIA:raw/assets/cn_etf_mining_2026-06/VolatilitySupportStrategy/513500_SSE.png) |

## WilliamsRMrSimpleStrategy

达标品种数: **3**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 511030 | SSE | 0.983 | 70 | 15.25% | -0.30% | ![511030](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRMrSimpleStrategy/511030_SSE.png) |
| 159611 | SZSE | 0.908 | 64 | 90.27% | -1.55% | ![159611](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRMrSimpleStrategy/159611_SZSE.png) |
| 515450 | SSE | 0.819 | 74 | 101.99% | -1.45% | ![515450](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRMrSimpleStrategy/515450_SSE.png) |

## WilliamsRVolFilterStrategy

达标品种数: **16**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 561380 | SSE | 2.210 | 97 | 833.83% | -2.93% | ![561380](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/561380_SSE.png) |
| 159363 | SZSE | 1.981 | 79 | 1005.38% | -2.29% | ![159363](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159363_SZSE.png) |
| 588170 | SSE | 1.904 | 53 | 863.28% | -2.84% | ![588170](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/588170_SSE.png) |
| 159326 | SZSE | 1.747 | 109 | 591.50% | -2.61% | ![159326](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159326_SZSE.png) |
| 159201 | SZSE | 1.416 | 82 | 190.59% | -1.29% | ![159201](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159201_SZSE.png) |
| 563360 | SSE | 1.406 | 81 | 180.89% | -0.95% | ![563360](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/563360_SSE.png) |
| 513920 | SSE | 1.332 | 151 | 281.84% | -1.31% | ![513920](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/513920_SSE.png) |
| 159206 | SZSE | 1.271 | 67 | 535.66% | -3.51% | ![159206](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159206_SZSE.png) |
| 513310 | SSE | 1.199 | 199 | 716.18% | -6.22% | ![513310](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/513310_SSE.png) |
| 159566 | SZSE | 1.191 | 153 | 467.04% | -2.74% | ![159566](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159566_SZSE.png) |
| 159816 | SZSE | 1.131 | 347 | 16.99% | -0.18% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159816_SZSE.png) |
| 588220 | SSE | 1.078 | 183 | 309.66% | -2.67% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/588220_SSE.png) |
| 560860 | SSE | 1.005 | 203 | 311.44% | -5.25% | ![560860](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/560860_SSE.png) |
| 159516 | SZSE | 0.983 | 183 | 353.86% | -3.20% | ![159516](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159516_SZSE.png) |
| 159509 | SZSE | 0.962 | 143 | 393.73% | -3.66% | ![159509](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/159509_SZSE.png) |
| 588200 | SSE | 0.901 | 211 | 402.69% | -7.13% | ![588200](MEDIA:raw/assets/cn_etf_mining_2026-06/WilliamsRVolFilterStrategy/588200_SSE.png) |

## WohuStrategy

达标品种数: **2**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159816 | SZSE | 1.348 | 79 | 15.66% | -0.10% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/159816_SZSE.png) |
| 511580 | SSE | 0.817 | 62 | 4.97% | -0.05% | ![511580](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/511580_SSE.png) |
