     1|# LLM Wiki 索引
     2|
     3|本知识库基于 Karpathy 的 LLM Wiki 模式构建，是一个持久的、由 LLM 维护的 Markdown 知识资产。
     4|
     5|---
     6|
     7|## 📚 实体 (Entities)
     8|
     9|| 实体 | 类型 | 描述 |
    10||------|------|------|
    11||| [[Andrej Karpathy]] | 人物 | OpenAI 联合创始人之一，著名 AI 研究者，Tesla AI 前总监 |
    12||| [[Larry Connors]] | 人物 | 均值回归策略大师，Connors Research 创始人 |
    13||| [[QuantifiedStrategies-com]] | 网站 | Substack 量化策略网站，提供大量回测策略 |
    14||| [[Quantitativo]] | 作者 | Quant Trading Rules Substack，均值回归 / 参数分散策略专家 |
    15||| [[Delphic Alpha]] | 作者 | Substack 量化策略博客，专注日内 alpha 研究 |
|| [[QQQ]] | ETF | Invesco QQQ Trust，追踪纳斯达克100指数 |
||| [[SPY]] | ETF | SPDR S&P 500 ETF Trust |
||| [[XLP]] | ETF | Consumer Staples Select Sector SPDR Fund |
||| [[Algorithmicguys]] | 作者/团队 | Substack 量化策略博客，TraderDunn/Eric 主理，专注期货策略与组合构建 |
    18|
    19|---
    20|
    21|## 💡 概念 (Concepts)
    22|
    23|| 概念 | 领域 | 描述 |
    24||------|------|------|
    25|| [[mean-reversion]] | 交易 | 均值回归：短期价格偏离后向均值回归的倾向 |
    26|| [[trend-filter]] | 交易 | 趋势过滤器：只在特定趋势方向下执行交易 |
    27|| [[high-beta-bias]] | 交易 | 高贝塔偏好：高波动资产对策略回报的放大效应 |
    28|| [[LLM Wiki]] | 知识管理 | 由 LLM 持续维护的结构化 Markdown 知识库 |
    29|| [[RAG]] | AI | 检索增强生成，传统的文档问答方案 |
    30|| [[Memex]] | 历史 | Vannevar Bush 1945 年提出的"记忆延伸机器"构想 |
    31|| [[IBS (Internal Bar Strength)]] | 交易 | 内部柱强度指标，衡量收盘价在当日/当周区间内的位置 |
||| [[Mean-Reversion]] | 交易 | 均值回归策略大类 |
||| [[Intraday-Alpha]] | 交易 | 日内 alpha 信号研究，30分钟/日线多时间框架 |
||| [[Fade-Breakout]] | 交易 | 突破失败策略：价格突破区间后反向交易 |
||| [[Overnight-Edge]] | 交易 | 隔夜持仓的统计优势 |
|| [[Position-Sizing]] | 风控 | 头寸规模管理方法 |
|| [[RSI (Relative Strength Index)]] | 指标 | 相对强弱指数 |
|| [[RSI2 Mean Reversion]] | 策略 | 2-period RSI + SMA200趋势过滤的均值回归策略，交易频率极低 |
|| [[RSI Mean Reversion]] | 策略 | 14-period RSI 标准均值回归，带ATR止损，交易频率中等 |
|| [[Williams %R]] | 指标 | 威廉指标，超买超卖判断 |
|| [[Portfolio Diversification]] | 组合管理 | 通过分散化降低组合波动，追求负相关性 |
|| [[Monte Carlo Simulation]] | 统计 | 通过随机重排交易序列评估策略/组合鲁棒性 |
|| [[Incubation Testing]] | 风控 | 策略上线前的实盘孵化测试阶段 |
|| [[Beta Slippage]] | 交易 | 杠杆ETF因每日再平衡在震荡市中产生的收益衰减 |
|| [[Leveraged ETF]] | 产品 | 使用衍生品提供2x/3x日收益倍数的交易所交易基金 |
|| [[Portfolio Rebalancing]] | 组合管理 | 定期调整持仓权重以维持目标配置的纪律性操作 |
|| [[Crash Filter]] | 风控 | 极端市场条件下自动减仓/清仓的保护机制 |
    37|
    38|---
    39|
    40|## 📥 最新录入

- 2026-05-03: RSI CN 批量回测 — [[rsi-cn-batch-2026-05-03]]
- 2026-05-03: RSI CRYPTO 批量回测 — [[rsi-crypto-batch-2026-05-03]]
- 2026-05-03: RSI ETF 批量回测 — [[rsi-etf-batch-2026-05-03]]
- 2026-05-03: RSI CN 批量回测 — [[rsi-cn-batch-2026-05-03]]
- 2026-05-03: RSI CRYPTO 批量回测 — [[rsi-crypto-batch-2026-05-03]]
- 2026-05-03: RSI ETF 批量回测 — [[rsi-etf-batch-2026-05-03]]
- 2026-05-03: RSI CN 批量回测 — [[rsi-cn-batch-2026-05-03]]
- 2026-05-03: RSI CRYPTO 批量回测 — [[rsi-crypto-batch-2026-05-03]]
- 2026-05-03: RSI ETHUSDT_SWAP_OKX 批量回测 — [[rsi-ethusdt_swap_okx-batch-2026-05-03]]
- 2026-05-03: RSI CN 批量回测 — [[rsi-cn-batch-2026-05-03]]
- 2026-05-03: RSI CRYPTO 批量回测 — [[rsi-crypto-batch-2026-05-03]]
- 2026-05-03: SMR CN 批量回测 — [[smr-cn-batch-2026-05-03]]
| 来源 | 日期 | 类型 | 摘要 |
|------|------|------|------|
| [[delphicalpha-exotic-alpha-atlas-beyond-textbook]] | 2026-05-02 | source | Delphic Alpha: 18 exotic alphas × 5 asset classes on 30-min bars. Keltner Reversion dominant. Commodities disaster OOS. |

---

## ✅ 已验证策略 (Verified Strategies)

| 策略 | 原文 | 复现报告 | 最佳品种 | Sharpe | 评级 | 日期 |
|------|------|----------|----------|--------|------|------|
|| KAMA + ATR RTY Trend | [[2025-07-01-kama-atr-rty-trend]] | [[strategy-repro-kama-atr-rty-20260430]] | RTY/ES | 1.783 | 🟢 Green | 2026-04-30 |
||| Consecutive Down Days | [[2026-04-19-Consecutive-Down-Days-Strategy]] | [[strategy-repro-consecutive-down-days]] | SPY | 1.762 | 🟢 Green | 2026-04-19 |
|| Catching Crypto Trends | [[2026-04-22-Catching-Crypto-Trends]] | [[strategy-repro-crypto-trend-combo]] | BTC | 1.741 | 🟢 Green | 2026-04-22 |
| RSI-2 Did You Miss This | [[2026-04-08-Did-You-Miss-This]] | [[strategy-repro-rsi2-did-you-miss]] | GLD | 1.479 | 🟢 Green | 2026-04-25 |
| Gold Envelope | [[2023-12-15-Gold-Envelope-Trading-Strategy---Rules-And-Performance]] | [[strategy-repro-gold-envelope]] | GLD | 1.357 | 🟡 Yellow | 2026-04-25 |
| NR7 Breakout | [[2026-04-22-NR7-Breakout-Strategy]] | [[strategy-repro-nr7-breakout]] | SPY | 1.288 | 🟢 Green | 2026-04-22 |
| Crypto Trend Combo V2 | [[2026-04-22-Crypto-Trend-Combo-V2]] | [[strategy-repro-crypto-trend-combo-v2]] | GLD | 1.224 | 🟢 Green | 2026-04-22 |
| MACD Hook Gold | [[2025-05-01-macd-hook-gold-strategy]] | [[strategy-repro-macd-hook-gold]] | GLD | 1.223 | 🟢 Green | 2026-04-20 |
|| NR7 Breakout (Updated) | [[2026-04-22-NR7-Breakout-Strategy]] | [[strategy-repro-nr7_breakout]] | SPY | 1.212 | 🟢 Green | 2026-04-30 |
|| Bitcoin Momentum | [[2026-04-24-Bitcoin-Momentum-Strategy]] | [[strategy-repro-bitcoin-momentum]] | BTC | 0.476 | 🟡 Yellow | 2026-04-24 |
| Donchian ADX Breakout | [[2026-04-05-Strategy-8-The-Easiest-Trend-System-Youll-Ever-Trade-Donchian-Channel-Breakout]] | [[strategy-repro-donchian-adx-breakout]] | ETH | 1.192 | 🟢 Green | 2026-04-22 |
| MACD Histogram Mean Reversion | [[2024-03-07-MACD-Histogram-Trading-Strategy--Rules-Setup-Backtest-Example-Insights]] | [[strategy-repro-macd-histogram-rev-20260416]] | QQQ | 1.038 | 🟢 Green | 2026-04-16 |
| End of Month SPY | [[2026-04-04_End-of-Month-Trading-Strategy-in-S&P-500-—-Update]] | [[strategy-repro-end-of-month-spy]] | SPY | 1.030 | 🟢 Green | 2026-04-20 |
| 2026-04-28-simple-trend-following-with-dual-stop | [[2026-04-28-simple-trend-following-with-dual-stop]] | [[strategy-repro-simple_trend_following]] | QQQ | 1.023 | 🟢 Green | 2026-04-28 |
| Double Seven | [[2024-01-22-Larry-Connors-Double-Seven-Trading-Strategy-Double-7-Trading-System]] | [[strategy-repro-double-seven]] | SPY | 0.944 | 🟢 Green | 2026-04-24 |
| 5-Day Low | [[2026-04-14-Buy-Weakness-Win-Big-The-5-Day-Low-Trading-Strategy]] | [[strategy-repro-five-day-low]] | SPY | 0.925 | 🟢 Green | 2026-04-24 |
| Pullback Trading | [[2023-12-25-pullback-trading-strategies-backtest]] | [[strategy-repro-pullback-trading]] | SPY | 0.895 | 🟡 Yellow | 2026-04-25 |
|| SMA200 Trend Following | [[2024-03-03-A-Simple-Trend-Following-System-and-Strategy-in-the-SP-500-Insights-from-Meb-Faber-and-Paul-Tudor-Jones]] | [[strategy-repro-sma200-trend-following]] | SPY | 0.591 | 🟢 Green | 2026-04-20 |
|| Simple Trend Following (Dual Stop) | [[Simple Trend Following with Dual Stop]] | [[strategy-repro-simple-trend-dual-stop]] | QQQ | 1.02 | 🟡 Yellow | 2026-04-28 |
| Weekly Mean Reversion SP500 | [[2023-04-23-Weekly-Mean-Reversion-System-For-SP-500-Stocks]] | [[strategy-repro-weekly-mean-reversion-sp500]] | SPY | 0.954 | 🟢 Green | 2026-04-25 |
| strategy-repro-macd-histogram-rev-20260416 | [[strategy-repro-macd-histogram-rev-20260416]] | [[strategy-repro-macd_histogram_rev_20260416]] | QQQ | 1.397 | 🟢 Green | 2026-04-28 |
|| RSI Mean Reversion CN Futures | [[rsi2mr-cn-futures-batch-2026-04-30]] | TF888 (5年国债) | 1.25 | 🟢 Green | 2026-04-30 |
||| Crypto策略挖掘分析 | [[crypto-strategies-analysis-2026-04-30]] | BTC/ETH/SOL/DOGE | — | 合成报告 | 2026-04-30 |
|||| PivotShift BTC | [[2026-05-01-this-nasdaq-strategy-has-a-75-win-rate]] | [[strategy-repro-pivot-shift-btc]] | BTC | 0.718 | 🟡 Yellow | 2026-05-01 |
||| Connors %B Long Only | [[2026-04-30-Connors-%B-Long-Only-Portfolio-Addition]] | [[strategy-repro-connors-percent-b-long-only]] | ES/SPY | TBD | 🟡 Yellow | 2026-05-01 |

> **规则**: 策略列 → 原文 source 页 | 复现报告列 → 复现详情页 | 按 Sharpe 降序排列
> **管理规则**: [[WIKI_REPRODUCTION_RULES]]

---

## 📄 资料来源 (Sources)

    41|
    42|| 来源 | 日期 | 来源类型 | 一句话摘要 |
    43||------|------|----------|------|
    44||| [[reversal-strategy-landscape]] | 合成 | 反转策略全景分析：品种分类 × 策略类型 × 适用性图谱 |
|| [[reversal-strategy-pipeline-2026-04-26]] | 2026-04-26 | 合成 | 反转策略失焦分析：规则明确尚未复现的策略清单 + 品种适配规律 + 优先级排名 |
    45||| [[2026-04-25_obsidian-vault-merge-intraday-notes]] | 2026-04-25 | 合并 | obsidian-vault 独立仓库合并：17 篇手动日内策略笔记、34 篇 Substack 原文 |
    46||| [[2026-04-25-substack-batch-quantified-strategies]] | 2026-04-25 | 文章批量 | Substack Quantified Strategies 批量导入 407 篇策略文章 |
    47|| [[2026-04-25-substack-batch-unknown]] | 2026-04-25 | 文章批量 | Substack Unknown 批量导入 371 篇策略文章 |
    48|| [[2026-04-25-substack-batch-tradequantix]] | 2026-04-25 | 文章批量 | Substack TradeQuantiX 批量导入 67 篇策略文章 |
    49|| [[2026-04-26-delphic-intraday-alpha-atlas]] | 2026-04-26 | 策略研究 | Delphic Alpha 日内 Alpha Atlas：30分钟K线上12个参数无关alpha信号的回测研究，Fade Breakout最强 |
    50|| [[strategy-repro-sma200-trend-following]] | 2026-04-20 | 策略复现 | S&P 500 200日SMA趋势跟踪：Sharpe 0.686，最大回撤 3.22% |
    51|| [[strategy-repro-end-of-month-spy]] | 2026-04-20 | 策略复现 | 月末SPY交易策略：Sharpe 1.029，最大回撤仅 0.91%，本批最佳 |
    52|| [[2026-03-28-simplest-intraday-momentum-strategy]] | 2026-03-28 | 文章 | 最简单的日内动量策略：VWAP控制过滤 + StochRSI时机入场 |
    53|| [[2026-03-19-5-swing-trading-strategies-for-beginners]] | 2026-03-19 | 文章 | 5 个适合初学者的波段交易均值回归策略 |
    54|| [[2026-05-01_cta-developer-rsi-strategy-confusion-fix]] | 2026-05-01 | 排查记录 | cta_developer RSI/RSI2策略混淆bug修复与crypto回测结论 |
|| [[2026-04-18-consecutive-down-days-strategy]] | 2026-04-18 | 文章 | 连续下跌日均值回归策略：在长期上升趋势中抓住短期恐惧买入 |
    55|| [[2025-04-13_karpathy_llm_wiki]] | 2025-04-13 | 文章 | Karpathy 分享的公开构建个人本地知识库的详细方法 |
    56|| [[strategy-repro-consecutive-down-days]] | 2026-04-19 | 策略复现 | 连续下跌日均值回归：SPY Sharpe 1.762，最大回撤 2.25% |
    57|| [[strategy-repro-crypto-trend-combo]] | 2026-04-22 | 策略复现 | 加密货趋势组合：BTC Sharpe 1.741，最大回撤 4.99% |
    58|| [[strategy-repro-crypto-trend-combo-v2]] | 2026-04-22 | 策略复现 | 加密货趋势组合V2：GLD Sharpe 1.224，多模型集成 |
    59|| [[strategy-repro-donchian-adx-breakout]] | 2026-04-22 | 策略复现 | Donchian+ADX突破：ETH Sharpe 1.192，最大回撤 14.21% |
    60||| [[strategy-repro-nr7-breakout]] | 2026-04-22 | 策略复现 | NR7窄幅突破：SPY Sharpe 1.288，最大回撤仅0.52%，Green |
    61||| [[strategy-repro-macd-histogram-rev-20260416]] | 2026-04-16 | 策略复现 | MACD Histogram均值回归：QQQ Sharpe 1.038，最大回撤 40.25%，扩展测试9品种Green |
    62|| [[strategy-repro-macd-hook-gold]] | 2026-04-20 | 策略复现 | MACD Hook 黄金策略：GLD Sharpe 1.223，最大回撤 135.25% |
    63|| [[2025-04-22-simple-alpha-atlas-what-actually-works-across-markets-daily]] | 2025-04-22 | 文章 | Delphic Alpha 多资产 Alpha 图谱：12 个信号族×5 市场，零优化回测实证 |
    64|| [[2026-04-22-Bollinger-Band-Squeeze-Trading-Strategy]] | 2026-04-22 | 策略/文章 | 布林带挤压波动性突破策略，周线+RSI过滤，付费文章 |
    65|| [[2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2]] | 2025-04-22 | 策略/文章 | ETF均值回归四系统组合构建：Portfolio Effect是唯壹圣杯 |
    66|| [[2026-04-22-session-high-retest-intraday-strategy]] | 2026-04-22 | 策略/文章 | Session High Retest 量化日内策略：10品种、17年数据、Portfolio Sharpe 1.15 |
|| [[2026-04-30-Connors-%B-Long-Only-Portfolio-Addition]] | 2026-04-30 | 策略/文章 | Connors %B 纯做多均值回归：2009年公开策略，加入组合后Return/DD从16.82提升至20.64 |
    67|| [[2026-02-23-systematic-intraday-trend-following-strategy]] | 2026-02-23 | 策略/文章 | 系统性日内趋势跟踪：动态边界+VWAP，SPY Sharpe 1.33 |
    68|| [[intraday-trading-strategies-compendium]] | 2026-04-22 | 概念/综合 | 日内交易策略汇编：7+篇文章总结 |
    69||| [[intraday-strategy-design-checklist]] | 2026-04-22 | 概念/Checklist | 日内策略设计十项检查清单 |
    70||| [[2026-04-25-nr7-futures-batch-pipeline]] | 2026-04-25 | 基础设施扩展 | NR7 Breakout 期货批量挖掘 Pipeline：24个IB期货品种 |
    71|||| [[tradingriot-analytics-platform]] | 2026-03-05 | 文章 | TradingRiot 自建多资产分析平台：1000+市场、Z-score筛选器、风险溢价分析 ||| [[strategy-repro-gold-envelope]] | 2026-04-25 | 策略复现 | Gold Envelope 黄金包络线均值回归：GLD Sharpe 1.357，最大回撤 0.22% |
    72||| [[strategy-repro-stochastic-extremes-gold]] | 2026-04-25 | 策略复现 | 随机指标极值黄金系统：Sharpe 0.956，全品种RED，交易次数严重不足 |
    73||| [[strategy-repro-weekly-mean-reversion-sp500]] | 2026-04-25 | 策略复现 | SP500周线均值回归：Sharpe 0.954，193笔交易，Green |
    74||| [[strategy-repro-bollinger-band-squeeze]] | 2026-04-25 | 策略复现 | 布林带收缩策略：全品种RED，QQQ Sharpe 0.766，信号稀疏 |
| [[2026-04-27_RSI-30-50-Strategy-for-Beginners]] | 2026-04-27 | 策略/文章 | RSI 30-50 回调买入：RSI(5)跌破30入场、回升至50出场，SPY胜率81% |
| [[2026-04-27_Trend-Following-Strategy-for-SP500]] | 2026-04-27 | 策略/文章 | S&P 500 趋势跟踪：1960年以来CAGR 6%，回撤25%（vs买入持有55%），付费墙遮挡规则 |
| [[2026-04-27_Larry-Connors-pctB-Strategy]] | 2026-04-27 | 策略/文章 | Larry Connors %B均值回归：%B<0超卖入场，1993年以来63笔交易，平均收益1.3% |
| [[2026-04-29_Ken-Griffin-Trading-Strategy]] | 2026-04-29 | 人物/系统 | Ken Griffin/Citadel多策略机器分析：非可复现策略，系统构建哲学参考 |
|| [[2026-04-30_Martingale-Strategy-for-Stocks]] | 2026-04-30 | 风险教育 | Martingale仓位管理批判：指数级风险，必爆仓，反面教材 |
|| [[2026-05-01-this-nasdaq-strategy-has-a-75-win-rate]] | 2026-05-01 | 策略/文章 | PivotShift: 75%胜率纳斯达克策略，日线枢轴压缩+12月过滤，付费墙遮挡关键参数 |
    75||| [[strategy-repro-macd-bitcoin]] | 2026-04-25 | 策略复现 | 比特币MACD交叉策略：Sharpe 0.944，最大回撤 51.76%，RED |
    76||| [[strategy-repro-pullback-trading]] | 2026-04-25 | 策略复现 | 回调交易策略：Sharpe 0.895，96笔交易，最大回撤 2.62%，YELLOW |
    77||| [[strategy-repro-rsi2-did-you-miss]] | 2026-04-25 | 策略复现 | RSI-2隐藏策略：GLD Sharpe 1.479，IWM Sharpe 1.170，2 Green |
    78||| [[strategy-repro-trading-hour-best]] | 2026-04-25 | 策略复现 | 最佳交易时段：无有效回测结果，需重新建模 |
|| [[2025-11-04_tradable-futures-portfolio]] | 2025-11-04 | 文章 | Algorithmicguys 12策略期货组合构建法：仅用实盘数据，Monte Carlo验证，Profit/MaxDD=15 |
|| [[2025-10-05_leveraged-etf-strategy]] | 2025-10-05 | 文章/策略 | SetupAlpha 3x杠杆ETF组合：TQQQ+TMF 50/50双月再平衡，15年CAGR 19.6%，回撤28.5% |
    79|
    80|
    81|---
    82|
    83|## 🧠 综合结论 (Syntheses)
    84|
    85|| 综合页面 | 日期 | 描述 |
    86||----------|------|------|
    87||| [[intraday-trading-strategies-compendium]] | 2026-04-22 | 日内交易策略汇编：7+ 篇文章核心结论 |
    88|||| [[mean-reversion-strategies-compendium]] | 2026-04-23 | 均值回归/反转策略汇编：12+ 策略分类、表现、10项关键注意事项 |
    89|||| [[reversal-strategies-compendium]] | 2026-04-25 | 反转策略全量汇编：从1701篇文章识别1043篇反转策略，八大类别、复现优先级矩阵 |
    90|||| [[reversal-deep-analysis-karpathy]] | 2026-04-25 | 反转策略深度分析 — Karpathy 视角：过拟合税、可信度分级、实盘路径 |
    91|
    92|---
    93|
## 📰 博客来源 (Blog Sources)

| 来源 | 日期 | 类型 | 文章数 | 一句话摘要 |
|------|------|------|--------|-----------|
| [[2026-04-27_quantinsti-blog-merge]] | 2026-04-27 | 博客批量 | 712 | QuantInsti Blog (2012-2026)：量化交易教育平台，561篇策略相关 |

---

## ❌ 问题与答案 (Queries)

*暂无查询页面*
    97|
    98|---
    99|
   100|## 最近活动
- [2026-04-30] 批量回测 `RSI Mean Reversion` 国内期货 8 品种 | TF888 Sharpe=1.25, T888 Sharpe=1.14, 6/8 Green | [[rsi2mr-cn-futures-batch-2026-04-30]]
- [2026-04-30] 策略复现 `rsi_range_momentum` | 无绿色结果
- [2026-04-30] 策略复现 `nr7_breakout` | SPY Sharpe=1.212 MaxDD=-6.51%
- [2026-05-01] 策略复现 `pivot_shift_btc` | BTC Sharpe=0.718 MaxDD=-32.6% Yellow (参数推断, 单品种, 出场bug修复)
- [2026-04-28] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.397 MaxDD=-34.35%
- [2026-04-28] 策略复现 `macd_histogram_rev_20260416` | 无绿色结果
- [2026-04-28] 策略复现 `simple_trend_following` | QQQ Sharpe=1.023 MaxDD=-4.37%
- [2026-04-28] 策略复现 `simple_trend_following` | QQQ Sharpe=1.023 MaxDD=-4.37%
- [2026-04-28] 策略复现 `simple_trend_following` | QQQ Sharpe=1.023 MaxDD=-4.37%
- [2026-04-28] 策略复现 `simple_trend_following` | QQQ Sharpe=1.023 MaxDD=-4.37%
- [2026-04-28] 策略复现 `simple_trend_following` | QQQ Sharpe=1.023 MaxDD=-4.37%
- [2026-04-28] 策略复现 `simple_trend_following_dual_stop` | QQQ Sharpe 1.02, GLD Sharpe 1.01, IWM Sharpe 0.17 (推断实现, Yellow)
- [2026-04-27] 策略复现 `spy_overnight_200sma` | 无绿色结果
- [2026-04-27] 策略复现 `equity_curve_mean_reversion` | 无绿色结果
- [2026-04-27] 策略复现 `equity_curve_mean_reversion` | 无绿色结果
- [2026-04-27] 策略复现 `sp500_trend_following` | 无绿色结果
- [2026-04-27] 策略复现 `profitable_systematic_rules` | 无绿色结果
- [2026-04-27] 策略复现 `mean_reversion_curve_portfolio` | 无绿色结果
- [2026-04-27] 策略复现 `larry_connors_b_strategy` | 无绿色结果
- [2026-04-27] 策略复现 `olmar_mean_reversion` | 无绿色结果
- [2026-04-27] 策略复现 `pullback_trading_strategy` | 无绿色结果
- [2026-04-27] 策略复现 `intraday_fade_breakout_30m` | 无绿色结果
- [2026-04-27] 策略复现 `five_rules_systematic_trading` | 无绿色结果
- [2026-04-27] 策略复现 `systematic_trading_rules` | 无绿色结果
- [2026-04-27] 策略复现 `sp500_trend_following` | 无绿色结果
- [2026-04-27] 策略复现 `five_rules_profitable_trading` | 无绿色结果
- [2026-04-27] 策略复现 `sp500_trend_following` | 无绿色结果
- [2026-04-27] 策略复现 `sp500_trend_following` | 无绿色结果
- [2026-04-26] 策略复现 `larry_connors_b_strategy` | 无绿色结果
   101|
   102|- [2026-04-26] 策略复现 `larry_connors_b_strategy` | 无绿色结果
   103|- [2026-04-26] 策略复现 `mean_reversion_curve_portfolio` | 无绿色结果
   104|- [2026-04-26] 策略复现 `larry_connors_b_strategy` | 无绿色结果
   105||- [2026-04-25] **Wiki 合并整理** | quant-wiki(391篇) + obsidian-vault(68篇) 合并至 llm-wiki，新增 6 实体、6 概念、2 综合页面
   106||- [2026-04-25] 策略复现 `gold_envelope` | GLD Sharpe=1.357, 93笔交易, Green
   107||- [2026-04-25] 策略复现 `stochastic_extremes_gold` | 全品种RED, GLD Sharpe=0.956, 交易不足
   108||- [2026-04-25] 策略复现 `weekly_mean_reversion_sp500` | Sharpe=0.954, 193笔交易, Green
   109||- [2026-04-25] 策略复现 `bollinger_band_squeeze` | 全品种RED, QQQ Sharpe=0.766, 48笔交易
   110||- [2026-04-25] 策略复现 `macd_trading_strategy_for_bitcoin` | BTC Sharpe=0.944, 回撤51.76%, RED
   111||- [2026-04-25] 策略复现 `pullback_trading` | SPY Sharpe=0.895, 96笔交易, YELLOW
   112||- [2026-04-25] 策略复现 `rsi_2` (Did You Miss This) | GLD Sharpe=1.479, IWM Sharpe=1.170, 2 Green
   113||- [2026-04-25] 策略复现 `what_trading_hour_is_the_best` | 无有效回测结果
   114|||- [2026-04-25] 反转策略8只全量同步至wiki | gold_envelope, stochastic_extremes, weekly_mr, bollinger_squeeze, macd_btc, pullback, rsi2, trading_hour
   115||- [2026-04-25] NR7 期货批量 Pipeline 扩展 | asset_registry 新增24个IB期货合约规格 + 期货批量挖掘脚本
   116|- [2026-04-23] 策略复现 `counter_trend_es_model` | 文章保存至llm-wiki，待获取ES 15m数据
   117|- [2026-04-23] 修复 OKX 数据下载 `get_bar_overview()` 超时问题 | 4小时→5分钟
   118|- [2026-04-22] 策略复现 `weekly_etf_rotation` | 无绿色结果
   119|- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
   120|- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
   121|- [2026-04-22] 策略复现 `vix_fear_indicator` | 无绿色结果
   122|- [2026-04-22] 策略复现 `vix_fear_gauge` | 无绿色结果
   123|- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
   124|- [2026-04-22] 策略复现 `unfilled_gap_inside_day` | 无绿色结果
   125|- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
   126|- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
   127|- [2026-04-22] 策略复现 `tuesday_vti` | 无绿色结果
   128|- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
   129|- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
   130|- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
   131|- [2026-04-22] 策略复现 `stochastic_mean_reversion` | 无绿色结果
   132|- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
   133|- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
   134|- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
   135|- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
   136|- [2026-04-22] 策略复现 `simple_momentum_4_etfs` | 无绿色结果
   137|- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
   138|- [2026-04-22] 策略复现 `rsi_2_strategy` | 无绿色结果
   139|- [2026-04-22] 策略复现 `rsi_2_larry_connors` | 无绿色结果
   140|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   141|- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
   142|- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
   143|- [2026-04-22] 策略复现 `pairs_trading_metals_complex` | 无绿色结果
   144|- [2026-04-22] 策略复现 `one_simple_momentum_strategy_4_etfs` | 无绿色结果
   145|- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
   146|- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
   147|- [2026-04-22] 策略复现 `nr7_breakout` | SPY Sharpe=1.288 MaxDD=-0.52%
   148|- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
   149|- [2026-04-22] 策略复现 `metals_pairs_trading_reality_check` | 无绿色结果
   150|- [2026-04-22] 策略复现 `mae_mfe_excursion_optimizer` | 无绿色结果
   151|- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
   152|- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
   153|- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
   154|- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
   155|- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
   156|- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
   157|- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
   158|- [2026-04-22] 策略复现 `friday_gld` | 无绿色结果
   159|- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
   160|- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
   161|- [2026-04-22] 策略复现 `donchian_adx_breakout` | ETHUSDT_SWAP_OKX.GLOBAL Sharpe=1.192 MaxDD=-14.21%
   162|- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
   163|- [2026-04-22] 策略复现 `crypto_trend_combo_v2` | GLD Sharpe=1.224 MaxDD=-653.67%
   164|- [2026-04-22] 策略复现 `crypto_trend_combo` | BTCUSDT_SWAP_OKX.GLOBAL Sharpe=1.741 MaxDD=-4.99%
   165|- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
   166|- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
   167|- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
   168|- [2026-04-22] 策略复现 `combined_candlestick_top5` | 无绿色结果
   169|- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
   170|- [2026-04-22] 策略复现 `bollinger_band_squeeze` | 无绿色结果
   171|- [2026-04-22] 策略复现 `bollinger_band_breakout` | 无绿色结果
   172|- [2026-04-22] 策略复现 `backtested_bollinger_bands_strategy` | 无绿色结果
   173|- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
   174|- [2026-04-22] 策略复现 `weekly_etf_rotation` | 无绿色结果
   175|- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
   176|- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
   177|- [2026-04-22] 策略复现 `vix_fear_indicator` | 无绿色结果
   178|- [2026-04-22] 策略复现 `vix_fear_gauge` | 无绿色结果
   179|- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
   180|- [2026-04-22] 策略复现 `unfilled_gap_inside_day` | 无绿色结果
   181|- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
   182|- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
   183|- [2026-04-22] 策略复现 `tuesday_vti` | 无绿色结果
   184|- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
   185|- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
   186|- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
   187|- [2026-04-22] 策略复现 `stochastic_mean_reversion` | 无绿色结果
   188|- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
   189|- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
   190|- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
   191|- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
   192|- [2026-04-22] 策略复现 `simple_momentum_4_etfs` | 无绿色结果
   193|- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
   194|- [2026-04-22] 策略复现 `rsi_2_strategy` | 无绿色结果
   195|- [2026-04-22] 策略复现 `rsi_2_larry_connors` | 无绿色结果
   196|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   197|- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
   198|- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
   199|- [2026-04-22] 策略复现 `pairs_trading_metals_complex` | 无绿色结果
   200|- [2026-04-22] 策略复现 `one_simple_momentum_strategy_4_etfs` | 无绿色结果
   201|- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
   202|- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
   203|- [2026-04-22] 策略复现 `nr7_breakout` | SPY Sharpe=1.288 MaxDD=-0.52%
   204|- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
   205|- [2026-04-22] 策略复现 `metals_pairs_trading_reality_check` | 无绿色结果
   206|- [2026-04-22] 策略复现 `mae_mfe_excursion_optimizer` | 无绿色结果
   207|- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
   208|- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
   209|- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
   210|- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
   211|- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
   212|- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
   213|- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
   214|- [2026-04-22] 策略复现 `friday_gld` | 无绿色结果
   215|- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
   216|- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
   217|- [2026-04-22] 策略复现 `donchian_adx_breakout` | SOLUSDT_SWAP_OKX.GLOBAL Sharpe=1.104 MaxDD=-6.63%
   218|- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
   219|- [2026-04-22] 策略复现 `crypto_trend_combo_v2` | GLD Sharpe=1.224 MaxDD=-653.67%
   220|- [2026-04-22] 策略复现 `crypto_trend_combo` | BTCUSDT_SWAP_OKX.GLOBAL Sharpe=1.741 MaxDD=-4.99%
   221|- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
   222|- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
   223|- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
   224|- [2026-04-22] 策略复现 `combined_candlestick_top5` | 无绿色结果
   225|- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
   226|- [2026-04-22] 策略复现 `bollinger_band_squeeze` | 无绿色结果
   227|- [2026-04-22] 策略复现 `bollinger_band_breakout` | 无绿色结果
   228|- [2026-04-22] 策略复现 `backtested_bollinger_bands_strategy` | 无绿色结果
   229|- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
   230|- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
   231|- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
   232|- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
   233|- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
   234|- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
   235|- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
   236|- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
   237|- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
   238|- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
   239|- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
   240|- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
   241|- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
   242|- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
   243|- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
   244|- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
   245|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   246|- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
   247|- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
   248|- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
   249|- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
   250|- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
   251|- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
   252|- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
   253|- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
   254|- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
   255|- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
   256|- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
   257|- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
   258|- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
   259|- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
   260|- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
   261|- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
   262|- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
   263|- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
   264|- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
   265|- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
   266|- [2026-04-22] 策略复现 `volatility_swing_trade_nasdaq_sp500` | 无绿色结果
   267|- [2026-04-22] 策略复现 `vix_fear_mean_reversion` | 无绿色结果
   268|- [2026-04-22] 策略复现 `vix_100_sma_cross` | 无绿色结果
   269|- [2026-04-22] 策略复现 `unfilled_gap_down_inside_day` | 无绿色结果
   270|- [2026-04-22] 策略复现 `turn_of_the_month` | 无绿色结果
   271|- [2026-04-22] 策略复现 `trend_following_gold_breakout` | 无绿色结果
   272|- [2026-04-22] 策略复现 `thanksgiving_holiday_effect` | 无绿色结果
   273|- [2026-04-22] 策略复现 `stochastic_short_term_mean_reversion` | 无绿色结果
   274|- [2026-04-22] 策略复现 `spy_gld_rotation` | 无绿色结果
   275|- [2026-04-22] 策略复现 `sp500_monthly_sma_momentum` | 无绿色结果
   276|- [2026-04-22] 策略复现 `sp500_momentum_monthly_sma` | 无绿色结果
   277|- [2026-04-22] 策略复现 `sma200_trend_following_20260420` | SPY Sharpe=0.686 MaxDD=-321.54%
   278|- [2026-04-22] 策略复现 `russell_2000_death_cross` | 无绿色结果
   279|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   280|- [2026-04-22] 策略复现 `pullback_trading_strategy` | 无绿色结果
   281|- [2026-04-22] 策略复现 `price_action_seasonal_filter_bonds` | 无绿色结果
   282|- [2026-04-22] 策略复现 `one_simple_momentum_4_etfs` | 无绿色结果
   283|- [2026-04-22] 策略复现 `nr7_enhanced` | 无绿色结果
   284|- [2026-04-22] 策略复现 `moving_average_crossover` | 无绿色结果
   285|- [2026-04-22] 策略复现 `mae_mfe_analysis` | 无绿色结果
   286|- [2026-04-22] 策略复现 `macd_hook_gold_strategy` | 无绿色结果
   287|- [2026-04-22] 策略复现 `macd_hook_gold` | GLD Sharpe=1.223 MaxDD=-135.25%
   288|- [2026-04-22] 策略复现 `macd_histogram_rev_20260416` | QQQ Sharpe=1.038 MaxDD=-40.25%
   289|- [2026-04-22] 策略复现 `macd_histogram_rev` | 无绿色结果
   290|- [2026-04-22] 策略复现 `macd_histogram_auto_test` | 无绿色结果
   291|- [2026-04-22] 策略复现 `macd_crossover` | 无绿色结果
   292|- [2026-04-22] 策略复现 `end_of_month_strategy_20260420` | SPY Sharpe=1.029 MaxDD=-90.70%
   293|- [2026-04-22] 策略复现 `donchian_channel_breakout` | 无绿色结果
   294|- [2026-04-22] 策略复现 `death_cross` | 无绿色结果
   295|- [2026-04-22] 策略复现 `consecutive_down_days_strategy` | 无绿色结果
   296|- [2026-04-22] 策略复现 `consecutive_down_days` | SPY Sharpe=1.762 MaxDD=-2.25%
   297|- [2026-04-22] 策略复现 `commodity_skewness_premium` | 无绿色结果
   298|- [2026-04-22] 策略复现 `combined_candlestick_strategy` | 无绿色结果
   299|- [2026-04-22] 策略复现 `backtested_bollinger_bands` | 无绿色结果
   300|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   301|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   302|- [2026-04-22] 策略复现 `rsi_2` | 无绿色结果
   303|1. **🔥 批量录入 Substack 策略文章库 (745 篇)** - 2026-04-22 - 全部可在 `wiki/sources/` 查看，Obsidian 手机端同步
   304|2. 录入 "MACD Hook 黄金多头策略" - 2025-05-01 - 规则完整，可复现 - 🔒 Green
   305|3. 策略复现 "End of Month Trading Strategy in S&P 500" - 2026-04-20 - Sharpe 1.029, 最大回撤 0.91% - 🔒 Green
   306|4. 策略复现 "S&P 500 200-Day SMA Trend Following" - 2026-04-20 - Sharpe 0.686, 最大回撤 3.22% - 🔒 Green
   307|5. 录入 "The SIMPLEST Intraday Momentum Strategy" 文章 - 2026-03-28 - 🟡 Yellow 评级
   308|6. 录入 "5 Swing Trading Strategies for Beginners" 文章 - 2026-03-19 - 🔒 Green 评级
   309|7. 录入 "Consecutive Down Days Strategy" 文章 - 2026-04-18 - 🟡 Yellow 评级
   310|8. 初始化 LLM Wiki 知识库 - 2025-04-13
   311|9. 录入 Karpathy LLM Wiki 文章 - 2025-04-13
   312|
   313|10. 策略复现 "Consecutive Down Days Strategy" - 2026-04-19 - SPY Sharpe=1.762, 最大回撤 2.25% - 🔒 Green
   314|11. 策略复现 "Crypto Trend Combo" - 2026-04-22 - BTC Sharpe=1.741, 最大回撤 4.99% - 🔒 Green
   315|12. 策略复现 "Crypto Trend Combo V2" - 2026-04-22 - GLD Sharpe=1.224 - 🔒 Green
   316|13. 策略复现 "Donchian ADX Breakout" - 2026-04-22 - ETH Sharpe=1.192, 最大回撤 14.21% - 🔒 Green
   317|14. 策略复现 "NR7 Breakout" - 2026-04-22 - SPY Sharpe=1.288, 最大回撤 0.52% - 🔒 Green
   318|15. 策略复现 "MACD Histogram Mean Reversion" - 2026-04-16 - QQQ Sharpe=1.038, 最大回撤 40.25% - 🔒 Green
   319|16. 策略复现 "MACD Hook Gold Strategy" - 2026-04-20 - GLD Sharpe=1.223, 最大回撤 135.25% - 🔒 Green
   320|17. 策略复现 "Gold Envelope" - 2026-04-25 - GLD Sharpe=1.357, 93笔交易 - 🟡 Yellow (单品种Green)
   321|18. 策略复现 "Weekly Mean Reversion SP500" - 2026-04-25 - Sharpe=0.954, 193笔交易 - 🔒 Green
   322|19. 策略复现 "RSI-2 (Did You Miss This)" - 2026-04-25 - GLD Sharpe=1.479, IWM Sharpe=1.170 - 🔒 Green (2品种)
   323|20. 8个策略复现结果同步至wiki - 2026-04-25 - 反转策略批量化wiki同步完成
   324|
   325|
## 最新录入
- 2026-05-01: 自动导入 1 篇 Substack 文章 (roguequant - PivotShift)
- 2026-04-30: 自动导入 1 篇 Substack 文章
- 2026-04-29: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章
- 2026-04-27: 自动导入 1 篇 Substack 文章

1. [[reversal-strategy-pipeline-2026-04-26]] - 反转策略失焦分析：品种适配规律 + 优先级排名 + 新4策略复现
2. (处理中: 5DL_ON Batch | WR Batch | CD_ON Batch)

### 最新动态
   328|- 2026-04-26: [[Trading the Mean Reversion Curve]] - Quantitativo - 参数分散均值回归策略组合
   329|- 2026-04-25: 自动导入 1 篇 Substack 文章
   330|- 2026-04-25: 自动导入 1 篇 Substack 文章
   331|- 2026-04-25: 自动导入 1 篇 Substack 文章
   332|- 2026-04-25: 自动导入 1 篇 Substack 文章
   333|- 2026-04-24: 自动导入 1 篇 Substack 文章
   334|- 2026-04-24: 自动导入 1 篇 Substack 文章
   335|- 2026-04-25: 录入 TradingRiot 多资产分析平台文章
   336|