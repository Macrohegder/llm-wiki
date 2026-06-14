---
tags:
  - strategy
  - cta-developer
  - overview
created: "2026-05-20"
---

# CTA-Developer 策略管理体系总览

> 生成时间: 2026-05-20 10:28:44
> 管理规范: 方案 B - 系统重建

---

## 策略分级体系

| 级别 | 状态 | 数量 | 说明 |
|------|------|------|------|
| **Tier 1** | ✅ 已验证 | 13 | Sharpe ≥ 0.8, 交易数 ≥ 50, 多资产表现稳定 |
| **Tier 2** | 🔄 待验证 | 6 | 有数据但需进一步验证 |
| **Tier 3** | ⏳ 未挖掘 | 52 | 有代码但未系统挖掘 |
| **Tier 4** | ❌ 已证伪 | 1 | 0交易或全部亏损 |

---

## Tier 1 - 已验证策略 (13 个)

| 策略 | 最佳品种 | Sharpe | 交易数 | 资产类别 |
|------|---------|--------|--------|---------|
| [[ConsecutiveDownDaysStrategy]] | IWM | 1.507 | 86 | ['etf', 'crypto', 'cn_futures'] |
| [[DonchianAdxBreakoutStrategy]] | IC888 | 0.814 | 52 | ['etf', 'crypto', 'cn_futures'] |
| [[FiveDayLowStrategy]] | SPY | 1.078 | 272 | ['etf', 'crypto', 'cn_futures'] |
| [[IbsMeanReversionStrategy]] | T888 | 1.041 | 105 | ['etf', 'crypto', 'cn_futures'] |
| [[MacdHistogramStrategy]] | T888 | 1.300 | 118 | ['etf', 'crypto', 'cn_futures'] |
| [[MarketConditionStrategy]] | AU888 | 1.126 | 189 | ['etf', 'crypto', 'cn_futures'] |
| [[PullbackMrStrategy]] | GLD | 1.227 | 71 | ['etf', 'cn_futures', 'crypto'] |
| [[RsiMeanReversionStrategy]] | T888 | 0.946 | 52 | ['etf', 'crypto', 'cn_futures'] |
| [[TripleRsiLongShortStrategy]] | TLT | 1.666 | 50 | ['etf'] |
| [[Tt1Strategy]] | TL888 | 1.850 | 59 | ['cn_futures'] |
| [[VolatilitySupportStrategy]] | GLD | 1.478 | 143 | ['etf', 'crypto', 'cn_futures'] |
| [[WilliamsRMrSimpleStrategy]] | GLD | 1.023 | 75 | ['etf', 'crypto', 'cn_futures'] |
| [[YmTradingStrategy]] | IM888 | 1.244 | 136 | ['intraday'] |

---

## Tier 2 - 待验证策略 (6 个)

| 策略 | 说明 |
|------|------|
| [[CandlestickPatternStrategy]] | Sharpe=1.015 @ TLT (3笔) |
| [[FiveDayLowOvernightStrategy]] | Sharpe=0.775 @ GLD (148笔) |
| [[FiveDayLowRangeStrategy]] | Sharpe=0.758 @ T888 (90笔) |
| [[GoldEnvelopeStrategy]] | Sharpe=1.241 @ XAU (10笔) |
| [[IbsRsiMeanReversionStrategy]] | Sharpe=0.603 @ SPY (268笔) |
| [[Rsi2Strategy]] | Sharpe=1.015 @ GLD (1笔) |

---

## Tier 3 - 未挖掘策略 (52 个)

### 跨日策略 (30 个)
- [[BensdorpMetaStrategy]]
- [[CincoLongOnlyStrategy]]
- [[CincoStrategy]]
- [[CtaTrendStrategy]]
- [[DonchianEnsembleCryptoTrendStrategy]]
- [[Han123LongStrategyFilter10min]]
- [[Han123LongStrategyFilterLongShort]]
- [[Han123StrategyAtrHL]]
- [[IntradayOpenAtrBreakoutHybridStrategy]]
- [[IntradayOpenAtrBreakoutStrategy]]
- [[LarryConnorsBStrategy]]
- [[MacdHistogramRevStrategy]]
- [[MacdHookGoldStrategy]]
- [[MomentumMeanReversionStrategy]]
- [[MoneyGrabberStrategy]]
- [[MrxBandStrategy]]
- [[OscillatorReversionStrategy]]
- [[PanicReliefStrategy]]
- [[PullbackMrLongShortStrategy]]
- [[Rsi2MrStrategy]]
- [[StochMomentumFilterStrategy]]
- [[StochasticMrStrategy]]
- [[TangoStrategy]]
- [[ThermostatStrategy]]
- [[TigerRsiStrategy]]
- [[TrendMeanReversionPortfolioStrategy]]
- [[TurningPointStrategy]]
- [[UltimaStrategy]]
- [[VpMacdStrategy]]
- [[WohuStrategy]]

### 日内策略 (22 个)
- [[DemarkScalperStrategy]]
- [[Han123Strategy]]
- [[IntradayBreakoutStrategy]]
- [[IntradayOpenAtrBreakoutIntradayStrategy]]
- [[LimitedDualThrustStrategy]]
- [[OpenMomentumStrategy]]
- [[OrbLongBar15Strategy]]
- [[OrbLongBar1Strategy]]
- [[OrbPullbackStrategy]]
- [[OrbShortBar15Strategy]]
- [[OrbShortBar1Strategy]]
- [[Ou60MinStrategy]]
- [[OuThreshold15Strategy]]
- [[OuThreshold20Strategy]]
- [[OuThreshold25Strategy]]
- [[VolumeDryUpDownStrategy]]
- [[VolumeDryUpUpStrategy]]
- [[VolumeSpikeMomentumDownStrategy]]
- [[VolumeSpikeMomentumUpStrategy]]
- [[VvgCloseFadeStrategy]]
- [[VvgContinuationStrategy]]
- [[VvgReversalStrategy]]

---

## CTA 实盘配置

| 资产类别 | 有效配置数 | 说明 |
|---------|-----------|------|
| CN 期货 | 32 | T/TF/TL 国债 + IF/IC/IH/IM 股指 + AU 黄金 |
| ETF | 18 | SPY/QQQ/IWM/GLD/TLT |
| Crypto | 2 | 当前无策略满足 Sharpe ≥ 0.8 |

---

## 最近更新

- 清理 2026-05-20: 空目录 + 重复挖掘去重
- 策略分级 2026-05-20: Tier1/Tier2/Tier3 分级
- CTA 配置过滤 2026-05-20: 仅保留 Sharpe ≥ 0.8 且交易数 ≥ 50
- Wiki 系统化 2026-05-20: 分级标签 + 总览页