# CTA 策略挖掘覆盖矩阵

- 生成时间: 2026-05-15T19:16:44.347687
- 数据来源: `data/batch_results/` 下所有批量挖掘结果

## Mean Reversion 策略

| 策略 | 文件 | CN期货 | Crypto | ETF | 日内 | 高潜力空白 |
|---|---|---|---|---|---|---|
| ConsecutiveDownDaysStrategy | `consecutive_down_days_strategy.py` | 🟢 T888<br>Sharpe=0.99, n=71 | 🟢 BTC<br>Sharpe=1.04, n=104 | 🟢 IWM<br>Sharpe=1.29, n=76 | ❌ 未挖掘 | — |
| FiveDayLowOvernightStrategy | `five_day_low_overnight_strategy.py` | 🟢 TF888<br>Sharpe=1.06, n=163 | 🟢 SPY<br>Sharpe=0.85, n=166 | 🟢 IWM<br>Sharpe=0.97, n=210 | ❌ 未挖掘 | — |
| FiveDayLowRangeStrategy | `five_day_low_range_strategy.py` | 🟡 TF888<br>Sharpe=0.65, n=121 | 🟡 BTC<br>Sharpe=1.24, n=26 | 🟢 SPY<br>Sharpe=1.24, n=168 | ❌ 未挖掘 | — |
| FiveDayLowStrategy | `five_day_low_strategy.py` | 🟢 IC888<br>Sharpe=0.85, n=263 | 🟡 BTC<br>Sharpe=0.52, n=475 | 🟢 SPY<br>Sharpe=1.08, n=260 | ❌ 未挖掘 | — |
| GoldEnvelopeStrategy | `gold_envelope_strategy.py` | 🟡 IC888<br>Sharpe=0.61, n=58 | 🟡 GLD<br>Sharpe=0.95, n=38 | 🟢 GLD<br>Sharpe=0.89, n=60 | ❌ 未挖掘 | — |
| IbsMeanReversionStrategy | `ibs_mean_reversion_strategy.py` | 🟢 T888<br>Sharpe=1.02, n=85 | 🔴 BTC<br>Sharpe=0.27, n=97 | 🟡 SPY<br>Sharpe=0.61, n=66 | ❌ 未挖掘 | — |
| IbsRsiMeanReversionStrategy | `ibs_rsi_mean_reversion_strategy.py` | 🟢 TL888<br>Sharpe=1.07, n=102 | 🔴 BTC<br>Sharpe=-0.47, n=64 | 🟢 SPY<br>Sharpe=0.97, n=254 | ❌ 未挖掘 | — |
| LarryConnorsBStrategy | `larry_connors_bstrategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| MacdHistogramRevStrategy | `macd_histogram_rev_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| MacdHistogramStrategy | `macd_histogram_strategy.py` | 🟢 T888<br>Sharpe=1.30, n=118 | 🟡 XAU<br>Sharpe=1.10, n=25 | 🟢 QQQ<br>Sharpe=1.22, n=102 | ❌ 未挖掘 | — |
| MarketConditionStrategy | `market_condition_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OscillatorReversionStrategy | `oscillator_reversion_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| PanicReliefStrategy | `panic_relief_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| PullbackMrLongShortStrategy | `pullback_mr_longshort_strategy.py` | 🟡 PS888<br>Sharpe=2.42, n=21 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | Crypto, ETF |
| PullbackMrStrategy | `pullback_mr_strategy.py` | 🟢 TF888<br>Sharpe=1.27, n=50 | 🟡 BTC<br>Sharpe=2.12, n=8 | 🟢 SPY<br>Sharpe=1.35, n=116 | ❌ 未挖掘 | — |
| Rsi2MrStrategy | `rsi2_mr_strategy.py` | 🟡 T888<br>Sharpe=0.85, n=10 | 🟡 SOL<br>Sharpe=1.05, n=2 | ❌ 未挖掘 | ❌ 未挖掘 | ETF |
| Rsi2Strategy | `rsi2_strategy.py` | ❌ 未挖掘 | 🟡 XAU<br>Sharpe=1.33, n=1 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, ETF |
| RsiMeanReversionStrategy | `rsi_mean_reversion_strategy.py` | 🟡 TF888<br>Sharpe=1.06, n=14 | 🟢 TF888<br>Sharpe=1.25, n=68 | 🟢 SPY<br>Sharpe=0.87, n=82 | ❌ 未挖掘 | — |
| StochasticMrStrategy | `stochastic_mr_strategy.py` | 🟡 TL888<br>Sharpe=1.48, n=14 | ❌ 未挖掘 | 🟡 IWM<br>Sharpe=0.67, n=50 | ❌ 未挖掘 | Crypto |
| TripleRsiLongShortStrategy | `triple_rsi_longshort_strategy.py` | 🟡 PS888<br>Sharpe=2.38, n=12 | 🟢 BTC<br>Sharpe=1.13, n=66 | 🟢 TLT<br>Sharpe=1.05, n=64 | ❌ 未挖掘 | — |
| VolatilitySupportStrategy | `volatility_support_strategy.py` | 🟢 TL888<br>Sharpe=1.20, n=64 | 🔴 BTC<br>Sharpe=0.34, n=266 | 🟢 GLD<br>Sharpe=1.46, n=151 | ❌ 未挖掘 | — |
| WilliamsRMrSimpleStrategy | `williams_r_mr_simple_strategy.py` | 🟢 TF888<br>Sharpe=0.80, n=68 | 🟢 GLD<br>Sharpe=1.67, n=99 | 🟢 IWM<br>Sharpe=1.09, n=56 | ❌ 未挖掘 | — |

## Trend Following 策略

| 策略 | 文件 | CN期货 | Crypto | ETF | 日内 | 高潜力空白 |
|---|---|---|---|---|---|---|
| CtaTrendStrategy | `cta_trend_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| DonchianAdxBreakoutStrategy | `donchian_adx_breakout_strategy.py` | 🟡 T888<br>Sharpe=0.69, n=86 | 🟡 XAU<br>Sharpe=1.75, n=10 | 🟡 GLD<br>Sharpe=0.74, n=62 | ❌ 未挖掘 | — |
| MacdHookGoldStrategy | `macd_hook_gold_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| Nr7BreakoutStrategy | `nr7_breakout_strategy.py` | 🟢 TF888<br>Sharpe=0.87, n=244 | 🟢 XAU<br>Sharpe=2.37, n=60 | 🟢 SPY<br>Sharpe=0.86, n=304 | ❌ 未挖掘 | — |
| OpenMomentumStrategy | `open_momentum_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| StochMomentumFilterStrategy | `stoch_momentum_filter_strategy.py` | ❌ 未挖掘 | 🟡 ETH<br>Sharpe=2.12, n=6 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, ETF |
| TangoStrategy | `tango_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| TurningPointStrategy | `turning_point_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VolumeSpikeMomentumDownStrategy | `volume_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VolumeSpikeMomentumUpStrategy | `volume_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VpMacdStrategy | `vp_macd_strategy.py` | 🟢 IM888<br>Sharpe=1.07, n=362 | 🟢 XAU<br>Sharpe=1.48, n=114 | 🟢 TLT<br>Sharpe=0.98, n=324 | ❌ 未挖掘 | — |

## Intraday 策略

| 策略 | 文件 | CN期货 | Crypto | ETF | 日内 | 高潜力空白 |
|---|---|---|---|---|---|---|
| CincoLongOnlyStrategy | `cinco_strategy_longonly.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| CincoStrategy | `cinco_strategy.py` | ❌ 未挖掘 | 🟡 XAU<br>Sharpe=3.05, n=20 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, ETF |
| DemarkScalperStrategy | `demark_scalper_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| Han123Strategy | `han123_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| IntradayBreakoutStrategy | `intraday_breakout_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| IntradayOpenAtrBreakoutHybridStrategy | `intraday_open_atr_breakout_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| IntradayOpenAtrBreakoutIntradayStrategy | `intraday_open_atr_breakout_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| IntradayOpenAtrBreakoutStrategy | `intraday_open_atr_breakout_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| LimitedDualThrustStrategy | `limited_dual_thrust_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| MomentumMeanReversionStrategy | `momentum_mean_reversion_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OrbLongBar15Strategy | `orb_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OrbLongBar1Strategy | `orb_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OrbPullbackStrategy | `orb_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OrbShortBar15Strategy | `orb_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OrbShortBar1Strategy | `orb_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| Ou60MinStrategy | `ou_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OuThreshold15Strategy | `ou_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OuThreshold20Strategy | `ou_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| OuThreshold25Strategy | `ou_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| UltimaStrategy | `ultima_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VolumeDryUpDownStrategy | `volume_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VolumeDryUpUpStrategy | `volume_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VvgCloseFadeStrategy | `vvg_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VvgContinuationStrategy | `vvg_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| VvgReversalStrategy | `vvg_falsification_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| YmTradingStrategy | `ym_trading_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |

## Portfolio 策略

| 策略 | 文件 | CN期货 | Crypto | ETF | 日内 | 高潜力空白 |
|---|---|---|---|---|---|---|
| BensdorpMetaStrategy | `bensdorp_meta_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| DonchianEnsembleCryptoTrendStrategy | `donchian_ensemble_crypto_trend_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |
| TrendMeanReversionPortfolioStrategy | `trend_mean_reversion_portfolio_strategy.py` | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | CN期货, Crypto, ETF |

## Hybrid 策略

| 策略 | 文件 | CN期货 | Crypto | ETF | 日内 | 高潜力空白 |
|---|---|---|---|---|---|---|
| MoneyGrabberStrategy | `money_grabber_strategy.py` | 🟢 T888<br>Sharpe=2.46, n=60 | ❌ 未挖掘 | ❌ 未挖掘 | ❌ 未挖掘 | Crypto, ETF |
| ThermostatStrategy | `thermostat_strategy.py` | 🟢 TL888<br>Sharpe=1.60, n=66 | 🔴 BTC<br>Sharpe=0.00, n=0 | ❌ 未挖掘 | ❌ 未挖掘 | ETF |

## Pattern 策略

| 策略 | 文件 | CN期货 | Crypto | ETF | 日内 | 高潜力空白 |
|---|---|---|---|---|---|---|
| CandlestickPatternStrategy | `candlestick_pattern_strategy.py` | 🔴 AU888<br>Sharpe=0.00, n=0 | 🔴 BTC<br>Sharpe=0.00, n=0 | 🔴 TLT<br>Sharpe=0.47, n=1 | ❌ 未挖掘 | — |

## 汇总统计

- 策略总数: 65
- 至少在一个市场挖掘过的策略: 25 (38.5%)
- 在三个主要市场（CN/Crypto/ETF）都挖掘过的策略: 17

## 关键发现

### 🔥 Crypto 高潜力空白（均值回归策略未挖掘）
- [[LarryConnorsBStrategy]]
- [[MacdHistogramRevStrategy]]
- [[MarketConditionStrategy]]
- [[OscillatorReversionStrategy]]
- [[PanicReliefStrategy]]
- [[PullbackMrLongShortStrategy]]
- [[StochasticMrStrategy]]

### ✅ 已验证富矿
- **国债期货（T/TF/TL）**: 均值回归策略的富矿，PullbackMR/IBS_RSI/5DL/VolatilitySupport 表现最佳
- **SPY/QQQ/IWM**: ETF 均值回归覆盖充分
