---
tags:
  - mining
  - cn-etf
  - cta-developer
created: "2026-06-14"
---

# CN ETF 策略挖掘结果汇总 (2026-06)

> 来源: `cta_developer` CN ETF 批量挖掘
> 生成时间: 2026-06-14 11:34:12
> 筛选标准: Sharpe > 0.8 且 交易次数 > 50
> 额外过滤: 仅保留实际回测中无空头交易的组合（国内 ETF 不能做空）

## 概览

- 达标策略数: **7**
- 达标品种数: **79**

### 按策略统计

| 策略 | 达标品种数 | 最佳品种 | 最佳 Sharpe |
|------|-----------|----------|------------|
| MacdHistogramRevStrategy | 5 | 513050.SSE | 0.976 |
| MrxBandStrategy | 7 | 159570.SZSE | 1.330 |
| NgStochPivotMeanRevStrategy | 21 | 515080.SSE | 1.321 |
| TigerRsiStrategy | 15 | 159570.SZSE | 1.533 |
| Tt1Strategy | 1 | 511360.SSE | 2.333 |
| WilliamsRVolFilterStrategy | 16 | 561380.SSE | 2.210 |
| WohuStrategy | 14 | 159570.SZSE | 1.926 |

## MacdHistogramRevStrategy

达标品种数: **5**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 513050 | SSE | 0.976 | 98 | 75.51% | -0.76% | ![513050](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/513050_SSE.png) |
| 159915 | SZSE | 0.885 | 58 | 65.20% | -0.61% | ![159915](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/159915_SZSE.png) |
| 159852 | SZSE | 0.833 | 62 | 57.53% | -0.76% | ![159852](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/159852_SZSE.png) |
| 588200 | SSE | 0.832 | 70 | 111.17% | -1.43% | ![588200](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/588200_SSE.png) |
| 510300 | SSE | 0.824 | 56 | 20.99% | -0.22% | ![510300](MEDIA:raw/assets/cn_etf_mining_2026-06/MacdHistogramRevStrategy/510300_SSE.png) |

## MrxBandStrategy

达标品种数: **7**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159570 | SZSE | 1.330 | 60 | 463.81% | -3.17% | ![159570](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/159570_SZSE.png) |
| 159509 | SZSE | 1.101 | 54 | 251.16% | -2.02% | ![159509](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/159509_SZSE.png) |
| 513050 | SSE | 1.093 | 91 | 163.61% | -2.33% | ![513050](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/513050_SSE.png) |
| 513130 | SSE | 1.075 | 57 | 75.92% | -0.65% | ![513130](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/513130_SSE.png) |
| 588220 | SSE | 0.963 | 63 | 318.69% | -2.64% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/588220_SSE.png) |
| 511090 | SSE | 0.937 | 65 | 44.49% | -0.45% | ![511090](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/511090_SSE.png) |
| 511380 | SSE | 0.837 | 54 | 38.60% | -0.33% | ![511380](MEDIA:raw/assets/cn_etf_mining_2026-06/MrxBandStrategy/511380_SSE.png) |

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

## TigerRsiStrategy

达标品种数: **15**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159570 | SZSE | 1.533 | 52 | 428.54% | -1.97% | ![159570](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159570_SZSE.png) |
| 159816 | SZSE | 1.397 | 58 | 16.55% | -0.07% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159816_SZSE.png) |
| 513120 | SSE | 1.359 | 62 | 150.50% | -0.71% | ![513120](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/513120_SSE.png) |
| 511260 | SSE | 1.209 | 63 | 20.94% | -0.27% | ![511260](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/511260_SSE.png) |
| 159636 | SZSE | 1.093 | 62 | 133.04% | -0.77% | ![159636](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159636_SZSE.png) |
| 512400 | SSE | 1.073 | 51 | 432.06% | -4.43% | ![512400](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/512400_SSE.png) |
| 159892 | SZSE | 0.998 | 70 | 64.89% | -0.75% | ![159892](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159892_SZSE.png) |
| 159796 | SZSE | 0.993 | 52 | 104.77% | -2.06% | ![159796](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159796_SZSE.png) |
| 588220 | SSE | 0.923 | 52 | 58.73% | -0.38% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/588220_SSE.png) |
| 159869 | SZSE | 0.892 | 348 | 147.51% | -2.79% | ![159869](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159869_SZSE.png) |
| 511380 | SSE | 0.876 | 80 | 28.35% | -0.42% | ![511380](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/511380_SSE.png) |
| 513630 | SSE | 0.836 | 52 | 72.40% | -0.85% | ![513630](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/513630_SSE.png) |
| 515220 | SSE | 0.833 | 66 | 286.02% | -4.39% | ![515220](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/515220_SSE.png) |
| 511090 | SSE | 0.824 | 79 | 33.00% | -0.63% | ![511090](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/511090_SSE.png) |
| 159870 | SZSE | 0.817 | 51 | 111.29% | -2.53% | ![159870](MEDIA:raw/assets/cn_etf_mining_2026-06/TigerRsiStrategy/159870_SZSE.png) |

## Tt1Strategy

达标品种数: **1**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 511360 | SSE | 2.333 | 145 | 8.11% | -0.04% | ![511360](MEDIA:raw/assets/cn_etf_mining_2026-06/Tt1Strategy/511360_SSE.png) |

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

达标品种数: **14**

| 品种 | 交易所 | Sharpe | 交易数 | 年化收益% | 最大回撤% | 图表 |
|------|--------|--------|--------|-----------|-----------|------|
| 159570 | SZSE | 1.926 | 60 | 569.83% | -2.18% | ![159570](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/159570_SZSE.png) |
| 159816 | SZSE | 1.348 | 79 | 15.66% | -0.10% | ![159816](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/159816_SZSE.png) |
| 513750 | SSE | 1.270 | 72 | 220.03% | -1.83% | ![513750](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/513750_SSE.png) |
| 159636 | SZSE | 1.236 | 88 | 152.66% | -1.15% | ![159636](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/159636_SZSE.png) |
| 513050 | SSE | 1.170 | 106 | 114.08% | -1.25% | ![513050](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/513050_SSE.png) |
| 562800 | SSE | 1.035 | 79 | 183.34% | -2.38% | ![562800](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/562800_SSE.png) |
| 588220 | SSE | 0.927 | 68 | 245.62% | -2.63% | ![588220](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/588220_SSE.png) |
| 511260 | SSE | 0.920 | 119 | 15.95% | -0.27% | ![511260](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/511260_SSE.png) |
| 515450 | SSE | 0.848 | 97 | 114.59% | -1.47% | ![515450](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/515450_SSE.png) |
| 515220 | SSE | 0.847 | 62 | 307.72% | -6.80% | ![515220](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/515220_SSE.png) |
| 513980 | SSE | 0.845 | 58 | 46.21% | -0.63% | ![513980](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/513980_SSE.png) |
| 159920 | SZSE | 0.822 | 86 | 43.24% | -1.04% | ![159920](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/159920_SZSE.png) |
| 511580 | SSE | 0.817 | 62 | 4.97% | -0.05% | ![511580](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/511580_SSE.png) |
| 511180 | SSE | 0.812 | 105 | 30.43% | -0.37% | ![511180](MEDIA:raw/assets/cn_etf_mining_2026-06/WohuStrategy/511180_SSE.png) |
