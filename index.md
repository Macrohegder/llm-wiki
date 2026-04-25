# LLM Wiki 索引

本知识库基于 Karpathy 的 LLM Wiki 模式构建，是一个持久的、由 LLM 维护的 Markdown 知识资产。

---

## 📚 实体 (Entities)

| 实体 | 类型 | 描述 |
|------|------|------|
|| [[Andrej Karpathy]] | 人物 | OpenAI 联合创始人之一，著名 AI 研究者，Tesla AI 前总监 |
|| [[Larry Connors]] | 人物 | 均值回归策略大师，Connors Research 创始人 |
|| [[QuantifiedStrategies-com]] | 网站 | Substack 量化策略网站，提供大量回测策略 |
|| [[QQQ]] | ETF | Invesco QQQ Trust，追踪纳斯达克100指数 |
|| [[SPY]] | ETF | SPDR S&P 500 ETF Trust |
|| [[XLP]] | ETF | Consumer Staples Select Sector SPDR Fund |

---

## 💡 概念 (Concepts)

| 概念 | 领域 | 描述 |
|------|------|------|
| [[mean-reversion]] | 交易 | 均值回归：短期价格偏离后向均值回归的倾向 |
| [[trend-filter]] | 交易 | 趋势过滤器：只在特定趋势方向下执行交易 |
| [[high-beta-bias]] | 交易 | 高贝塔偏好：高波动资产对策略回报的放大效应 |
| [[LLM Wiki]] | 知识管理 | 由 LLM 持续维护的结构化 Markdown 知识库 |
| [[RAG]] | AI | 检索增强生成，传统的文档问答方案 |
| [[Memex]] | 历史 | Vannevar Bush 1945 年提出的"记忆延伸机器"构想 |
| [[IBS (Internal Bar Strength)]] | 交易 | 内部柱强度指标，衡量收盘价在当日/当周区间内的位置 |
| [[Mean-Reversion]] | 交易 | 均值回归策略大类 |
| [[Overnight-Edge]] | 交易 | 隔夜持仓的统计优势 |
| [[Position-Sizing]] | 风控 | 头寸规模管理方法 |
| [[RSI (Relative Strength Index)]] | 指标 | 相对强弱指数 |
| [[Williams %R]] | 指标 | 威廉指标，超买超卖判断 |

---

## 📄 资料来源 (Sources)

| 来源 | 日期 | 来源类型 | 一句话摘要 |
|------|------|----------|------|
|| [[2026-04-25_quant-wiki-merge]] | 2026-04-25 | 合并 | quant-wiki 早期量化知识库整体合并：391 篇量化策略文章、5 实体、6 概念 |
|| [[2026-04-25_obsidian-vault-merge-intraday-notes]] | 2026-04-25 | 合并 | obsidian-vault 独立仓库合并：17 篇手动日内策略笔记、34 篇 Substack 原文 |
|| [[2026-04-25-substack-batch-quantified-strategies]] | 2026-04-25 | 文章批量 | Substack Quantified Strategies 批量导入 407 篇策略文章 |
| [[2026-04-25-substack-batch-unknown]] | 2026-04-25 | 文章批量 | Substack Unknown 批量导入 371 篇策略文章 |
| [[2026-04-25-substack-batch-tradequantix]] | 2026-04-25 | 文章批量 | Substack TradeQuantiX 批量导入 67 篇策略文章 |
| [[2025-05-01-macd-hook-gold-strategy]] | 2025-05-01 | 策略/文章 | MACD Hook 黄金多头策略：三重过滤+动态定量，规则极简可复现 |
| [[strategy-repro-sma200-trend-following]] | 2026-04-20 | 策略复现 | S&P 500 200日SMA趋势跟踪：Sharpe 0.686，最大回撤 3.22% |
| [[strategy-repro-end-of-month-spy]] | 2026-04-20 | 策略复现 | 月末SPY交易策略：Sharpe 1.029，最大回撤仅 0.91%，本批最佳 |
| [[2026-03-28-simplest-intraday-momentum-strategy]] | 2026-03-28 | 文章 | 最简单的日内动量策略：VWAP控制过滤 + StochRSI时机入场 |
| [[2026-03-19-5-swing-trading-strategies-for-beginners]] | 2026-03-19 | 文章 | 5 个适合初学者的波段交易均值回归策略 |
| [[2026-04-18-consecutive-down-days-strategy]] | 2026-04-18 | 文章 | 连续下跌日均值回归策略：在长期上升趋势中抓住短期恐惧买入 |
| [[2025-04-13_karpathy_llm_wiki]] | 2025-04-13 | 文章 | Karpathy 分享的公开构建个人本地知识库的详细方法 |
| [[strategy-repro-consecutive-down-days]] | 2026-04-19 | 策略复现 | 连续下跌日均值回归：SPY Sharpe 1.762，最大回撤 2.25% |
| [[strategy-repro-crypto-trend-combo]] | 2026-04-22 | 策略复现 | 加密货趋势组合：BTC Sharpe 1.741，最大回撤 4.99% |
| [[strategy-repro-crypto-trend-combo-v2]] | 2026-04-22 | 策略复现 | 加密货趋势组合V2：GLD Sharpe 1.224，多模型集成 |
| [[strategy-repro-donchian-adx-breakout]] | 2026-04-22 | 策略复现 | Donchian+ADX突破：ETH Sharpe 1.192，最大回撤 14.21% |
|| [[strategy-repro-nr7-breakout]] | 2026-04-22 | 策略复现 | NR7窄幅突破：SPY Sharpe 1.288，最大回撤仅0.52%，Green |
|| [[strategy-repro-macd-histogram-rev-20260416]] | 2026-04-16 | 策略复现 | MACD Histogram均值回归：QQQ Sharpe 1.038，最大回撤 40.25%，扩展测试9品种Green |
| [[strategy-repro-macd-hook-gold]] | 2026-04-20 | 策略复现 | MACD Hook 黄金策略：GLD Sharpe 1.223，最大回撤 135.25% |
| [[2025-04-22-simple-alpha-atlas-what-actually-works-across-markets-daily]] | 2025-04-22 | 文章 | Delphic Alpha 多资产 Alpha 图谱：12 个信号族×5 市场，零优化回测实证 |
| [[2026-04-22-Bollinger-Band-Squeeze-Trading-Strategy]] | 2026-04-22 | 策略/文章 | 布林带挤压波动性突破策略，周线+RSI过滤，付费文章 |
| [[2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2]] | 2025-04-22 | 策略/文章 | ETF均值回归四系统组合构建：Portfolio Effect是唯壹圣杯 |
| [[2026-04-22-session-high-retest-intraday-strategy]] | 2026-04-22 | 策略/文章 | Session High Retest 量化日内策略：10品种、17年数据、Portfolio Sharpe 1.15 |
| [[2026-02-23-systematic-intraday-trend-following-strategy]] | 2026-02-23 | 策略/文章 | 系统性日内趋势跟踪：动态边界+VWAP，SPY Sharpe 1.33 |
| [[intraday-trading-strategies-compendium]] | 2026-04-22 | 概念/综合 | 日内交易策略汇编：7+篇文章总结 |
|| [[intraday-strategy-design-checklist]] | 2026-04-22 | 概念/Checklist | 日内策略设计十项检查清单 |
|| [[2026-04-25-nr7-futures-batch-pipeline]] | 2026-04-25 | 基础设施扩展 | NR7 Breakout 期货批量挖掘 Pipeline：24个IB期货品种 |
||| [[tradingriot-analytics-platform]] | 2026-03-05 | 文章 | TradingRiot 自建多资产分析平台：1000+市场、Z-score筛选器、风险溢价分析 ||| [[strategy-repro-gold-envelope]] | 2026-04-25 | 策略复现 | Gold Envelope 黄金包络线均值回归：GLD Sharpe 1.357，最大回撤 0.22% |
|| [[strategy-repro-stochastic-extremes-gold]] | 2026-04-25 | 策略复现 | 随机指标极值黄金系统：Sharpe 0.956，全品种RED，交易次数严重不足 |
|| [[strategy-repro-weekly-mean-reversion-sp500]] | 2026-04-25 | 策略复现 | SP500周线均值回归：Sharpe 0.954，193笔交易，Green |
|| [[strategy-repro-bollinger-band-squeeze]] | 2026-04-25 | 策略复现 | 布林带收缩策略：全品种RED，QQQ Sharpe 0.766，信号稀疏 |
|| [[strategy-repro-macd-bitcoin]] | 2026-04-25 | 策略复现 | 比特币MACD交叉策略：Sharpe 0.944，最大回撤 51.76%，RED |
|| [[strategy-repro-pullback-trading]] | 2026-04-25 | 策略复现 | 回调交易策略：Sharpe 0.895，96笔交易，最大回撤 2.62%，YELLOW |
|| [[strategy-repro-rsi2-did-you-miss]] | 2026-04-25 | 策略复现 | RSI-2隐藏策略：GLD Sharpe 1.479，IWM Sharpe 1.170，2 Green |
|| [[strategy-repro-trading-hour-best]] | 2026-04-25 | 策略复现 | 最佳交易时段：无有效回测结果，需重新建模 |


---

## 🧠 综合结论 (Syntheses)

| 综合页面 | 日期 | 描述 |
|----------|------|------|
| [[intraday-trading-strategies-compendium]] | 2026-04-22 | 日内交易策略汇编：7+ 篇文章核心结论 |
|| [[mean-reversion-strategies-compendium]] | 2026-04-23 | 均值回归/反转策略汇编：12+ 策略分类、表现、10项关键注意事项 |
|| [[reversal-strategies-compendium]] | 2026-04-25 | 反转策略全量汇编：从1701篇文章识别1043篇反转策略，八大类别、复现优先级矩阵 |

---

## ❌ 问题与答案 (Queries)

*暂无查询页面*

---

## 最近活动

|- [2026-04-25] **Wiki 合并整理** | quant-wiki(391篇) + obsidian-vault(68篇) 合并至 llm-wiki，新增 6 实体、6 概念、2 综合页面
|- [2026-04-25] 策略复现 `gold_envelope` | GLD Sharpe=1.357, 93笔交易, Green
|- [2026-04-25] 策略复现 `stochastic_extremes_gold` | 全品种RED, GLD Sharpe=0.956, 交易不足
|- [2026-04-25] 策略复现 `weekly_mean_reversion_sp500` | Sharpe=0.954, 193笔交易, Green
|- [2026-04-25] 策略复现 `bollinger_band_squeeze` | 全品种RED, QQQ Sharpe=0.766, 48笔交易
|- [2026-04-25] 策略复现 `macd_trading_strategy_for_bitcoin` | BTC Sharpe=0.944, 回撤51.76%, RED
|- [2026-04-25] 策略复现 `pullback_trading` | SPY Sharpe=0.895, 96笔交易, YELLOW
|- [2026-04-25] 策略复现 `rsi_2` (Did You Miss This) | GLD Sharpe=1.479, IWM Sharpe=1.170, 2 Green
|- [2026-04-25] 策略复现 `what_trading_hour_is_the_best` | 无有效回测结果
||- [2026-04-25] 反转策略8只全量同步至wiki | gold_envelope, stochastic_extremes, weekly_mr, bollinger_squeeze, macd_btc, pullback, rsi2, trading_hour
|- [2026-04-25] NR7 期货批量 Pipeline 扩展 | asset_registry 新增24个IB期货合约规格 + 期货批量挖掘脚本
- [2026-04-23] 策略复现 `counter_trend_es_model` | 文章保存至llm-wiki，待获取ES 15m数据
- [2026-04-23] 修复 OKX 数据下载 `get_bar_overview()` 超时问题 | 4小时→5分钟
- [2026-04-22] 策略复现 `weekly_etf_rotation` | 无绿色结果
- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_indicator` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_gauge` | 无绿色结果
- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
- [2026-04-22] 策略复现 `unfilled_gap_inside_day` | 无绿色结果
- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
- [2026-04-22] 策略复现 `tuesday_vti` | 无绿色结果
- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `stochastic_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
- [2026-04-22] 策略复现 `simple_momentum_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2_larry_connors` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
- [2026-04-22] 策略复现 `pairs_trading_metals_complex` | 无绿色结果
- [2026-04-22] 策略复现 `one_simple_momentum_strategy_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
- [2026-04-22] 策略复现 `nr7_breakout` | SPY Sharpe=1.288 MaxDD=-0.52%
- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `metals_pairs_trading_reality_check` | 无绿色结果
- [2026-04-22] 策略复现 `mae_mfe_excursion_optimizer` | 无绿色结果
- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `friday_gld` | 无绿色结果
- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `donchian_adx_breakout` | ETHUSDT_SWAP_OKX.GLOBAL Sharpe=1.192 MaxDD=-14.21%
- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `crypto_trend_combo_v2` | GLD Sharpe=1.224 MaxDD=-653.67%
- [2026-04-22] 策略复现 `crypto_trend_combo` | BTCUSDT_SWAP_OKX.GLOBAL Sharpe=1.741 MaxDD=-4.99%
- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_top5` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `bollinger_band_squeeze` | 无绿色结果
- [2026-04-22] 策略复现 `bollinger_band_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `backtested_bollinger_bands_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
- [2026-04-22] 策略复现 `weekly_etf_rotation` | 无绿色结果
- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_indicator` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_gauge` | 无绿色结果
- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
- [2026-04-22] 策略复现 `unfilled_gap_inside_day` | 无绿色结果
- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
- [2026-04-22] 策略复现 `tuesday_vti` | 无绿色结果
- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `stochastic_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
- [2026-04-22] 策略复现 `simple_momentum_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2_larry_connors` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
- [2026-04-22] 策略复现 `pairs_trading_metals_complex` | 无绿色结果
- [2026-04-22] 策略复现 `one_simple_momentum_strategy_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
- [2026-04-22] 策略复现 `nr7_breakout` | SPY Sharpe=1.288 MaxDD=-0.52%
- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `metals_pairs_trading_reality_check` | 无绿色结果
- [2026-04-22] 策略复现 `mae_mfe_excursion_optimizer` | 无绿色结果
- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `friday_gld` | 无绿色结果
- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `donchian_adx_breakout` | SOLUSDT_SWAP_OKX.GLOBAL Sharpe=1.104 MaxDD=-6.63%
- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `crypto_trend_combo_v2` | GLD Sharpe=1.224 MaxDD=-653.67%
- [2026-04-22] 策略复现 `crypto_trend_combo` | BTCUSDT_SWAP_OKX.GLOBAL Sharpe=1.741 MaxDD=-4.99%
- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_top5` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `bollinger_band_squeeze` | 无绿色结果
- [2026-04-22] 策略复现 `bollinger_band_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `backtested_bollinger_bands_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
1. **🔥 批量录入 Substack 策略文章库 (745 篇)** - 2026-04-22 - 全部可在 `wiki/sources/` 查看，Obsidian 手机端同步
2. 录入 "MACD Hook 黄金多头策略" - 2025-05-01 - 规则完整，可复现 - 🔒 Green
3. 策略复现 "End of Month Trading Strategy in S&P 500" - 2026-04-20 - Sharpe 1.029, 最大回撤 0.91% - 🔒 Green
4. 策略复现 "S&P 500 200-Day SMA Trend Following" - 2026-04-20 - Sharpe 0.686, 最大回撤 3.22% - 🔒 Green
5. 录入 "The SIMPLEST Intraday Momentum Strategy" 文章 - 2026-03-28 - 🟡 Yellow 评级
6. 录入 "5 Swing Trading Strategies for Beginners" 文章 - 2026-03-19 - 🔒 Green 评级
7. 录入 "Consecutive Down Days Strategy" 文章 - 2026-04-18 - 🟡 Yellow 评级
8. 初始化 LLM Wiki 知识库 - 2025-04-13
9. 录入 Karpathy LLM Wiki 文章 - 2025-04-13

10. 策略复现 "Consecutive Down Days Strategy" - 2026-04-19 - SPY Sharpe=1.762, 最大回撤 2.25% - 🔒 Green
11. 策略复现 "Crypto Trend Combo" - 2026-04-22 - BTC Sharpe=1.741, 最大回撤 4.99% - 🔒 Green
12. 策略复现 "Crypto Trend Combo V2" - 2026-04-22 - GLD Sharpe=1.224 - 🔒 Green
13. 策略复现 "Donchian ADX Breakout" - 2026-04-22 - ETH Sharpe=1.192, 最大回撤 14.21% - 🔒 Green
14. 策略复现 "NR7 Breakout" - 2026-04-22 - SPY Sharpe=1.288, 最大回撤 0.52% - 🔒 Green
15. 策略复现 "MACD Histogram Mean Reversion" - 2026-04-16 - QQQ Sharpe=1.038, 最大回撤 40.25% - 🔒 Green
16. 策略复现 "MACD Hook Gold Strategy" - 2026-04-20 - GLD Sharpe=1.223, 最大回撤 135.25% - 🔒 Green
17. 策略复现 "Gold Envelope" - 2026-04-25 - GLD Sharpe=1.357, 93笔交易 - 🟡 Yellow (单品种Green)
18. 策略复现 "Weekly Mean Reversion SP500" - 2026-04-25 - Sharpe=0.954, 193笔交易 - 🔒 Green
19. 策略复现 "RSI-2 (Did You Miss This)" - 2026-04-25 - GLD Sharpe=1.479, IWM Sharpe=1.170 - 🔒 Green (2品种)
20. 8个策略复现结果同步至wiki - 2026-04-25 - 反转策略批量化wiki同步完成


## 最新录入
- 2026-04-25: 自动导入 1 篇 Substack 文章
- 2026-04-25: 自动导入 1 篇 Substack 文章
- 2026-04-25: 自动导入 1 篇 Substack 文章
- 2026-04-25: 自动导入 1 篇 Substack 文章
- 2026-04-24: 自动导入 1 篇 Substack 文章
- 2026-04-24: 自动导入 1 篇 Substack 文章
- 2026-04-25: 录入 TradingRiot 多资产分析平台文章
