## [2025-05-01] pipeline | MACD Hook 黄金多头策略 OAT 复现
- Action: `cta-strategy-factory` OAT pipeline (build → run → evaluate) on GLD
- Period: 2005-01-01 ~ 2025-12-31, Capital $100,000
- Method: OAT with GA 100/30
- Results: 🔒 Green 1/1 | Sharpe=1.223 | Trades=33 | MaxDD=-1.35% | Annual=2.078%

## [2026-04-22] ingest | 批量录入 Substack 策略文章库 (745 篇)
- Action: 将 substack-strategy-tracker 中所有尚未录入的策略文章批量导入 llm-wiki
- 来源: quantifiedstrategies, quantseeker, algomatictrading, delphicalpha 等 Substack 博客
- 新增 raw/articles: 829 篇原始文章
- 新增 wiki/sources: 745 篇 source 摘要页面（含 frontmatter、一句话摘要、复现状态占位）
- 已有 source 页面保留（含复现结果的 14 篇未覆盖）
- 更新 index.md 最近活动
- 所有文章均可在 Obsidian 手机端查看

## [2025-05-01] pipeline | MACD Hook 黄金多头策略 OAT 复现
- Optimal params: MACD(15,19,10), Hull=10, bullish_days=5, max_holding=7, stop=3.69%, size=70
- Key finding: 所有参数均被 GA 改写—原文的默认参数远未最优；Sharpe 1.223 为目前所有复现策略中最高
- Files: `reports/eval_macd_hook_gold_20260420_171931.json`, `generated/macd_hook_gold_strategy.py`
- Updated: wiki/sources/2025-05-01-macd-hook-gold-strategy.md (追加复现结果表)
- Bug fixes: runner.py 修复了 _ensure_strategy_loaded 传入 id 而非 YAML 路径的 bug，以及 f-string 格式化的 Python 3.11 兼容性问题

## [2025-05-01] ingest | MACD Hook 黄金多头策略
- Source: https://algomatictrading.substack.com/p/escape-discretionary-trading-automate
- Action: 抓取全文包含 ProRealTime 源代码，整理策略规则表，评价 Green
- Files: raw/articles/2025-05-01-macd-hook-gold-strategy.md, wiki/sources/2025-05-01-macd-hook-gold-strategy.md
- Rating: 🔒 Green (规则完整，可复现，提供完整源代码)
- Notes: 入场三重过滤（MACD>0 + histogram hook + Hull MA确认），出场3连阳/10日，ATR(39)动态定量，回测2005-2025，OOS自2022-04。未提供具体数值指标。可用cta-strategy-factory复现。

## [2026-04-20] pipeline | 季节性策略批量复现（SMA200 + End of Month + Dual Momentum）
- Action: `cta-strategy-factory` OAT pipeline 分别跑三个策略
- Universe: SPY
- Period: 2014-04-14 ~ 2025-12-31, Capital $100,000
- Results:
  - SMA200 Trend Following: GA优化后 sma_period=112, fixed_size=35 | Sharpe=0.686 | Trades=105 | 最大回撤 -3.22% | 总收益 11.93%
  - End of Month Strategy: GA优化后 target_pct=0.94%, fixed_size=35 | Sharpe=1.029 | Trades=137 | 最大回撤 -0.91% | 总收益 8.36%
  - Dual Momentum (Gary Antonacci): 跳过 — 跨资产轮动需多资产，当前单资产框架不支持
- 关键发现: End of Month 是本批最佳（Sharpe 1.029），风险收益比远优于 SMA200；SMA200 的 112 日最优周期显著优于原文的 200 日，提示超参数风险
- Files: wiki/sources/strategy-repro-sma200-trend-following.md, wiki/sources/strategy-repro-end-of-month-spy.md
- Updated: wiki/index.md

## [2026-04-20] analysis | CL 跨市场套利深度分析
- Action: 基于 HL/OKX API 数据和官方合约规则，系统性评估三条套利路径
- 核心发现: HL CL 合约已下架；OKX index 50% 权重引用下架合约；OKX funding 平均仅+3.25%年化但波动极大；CME roll cost 年化13-27%
- 评估结论: HL↔OKX ❌不可行；OKX内部 ❌不可行；CME↔OKX ⚠️边际可行但不适合个人
- Files: wiki/sources/2026-04-20-cl-cross-exchange-arbitrage-analysis.md
- Data: OKX CL-USDT-SWAP 169个 funding 周期(46天)、指数成分、流动性指标

- Source: https://www.tradingresearchub.com/p/why-is-the-wtioil-contract-on-hyperliquid
- Action: 抓取文章，解释了 CL perp 在合约滚动期间资金费率为-400%的机制原因
- Files: raw/articles/2026-04-09-wtioil-hyperliquid-funding.md, wiki/sources/2026-04-09-wtioil-hyperliquid-funding.md
- Rating: 🟢 Green (机制说明清晰，套利不可行的论证完整)
- Notes: 核心是 backwardation + 合约滚动导致的"粘性折价"。funding 刚好抵消 basis 收益，实际套利为零或负。

## [2026-03-28] ingest | The SIMPLEST Intraday Momentum Strategy in 2026
- Source: https://tradinginvestingstrategies.substack.com/p/the-simplest-intraday-momentum-strategy
- Action: Ingested article, extracted VWAP framework + StochRSI timing concept
- Files: raw/articles/2026-03-28-simplest-intraday-momentum-strategy.md, wiki/sources/2026-03-28-simplest-intraday-momentum-strategy.md
- Rating: 🟡 Yellow (strong concept, paywalled rules, no backtest data)
- Notes: VWAP used as control filter (not S/R). Complements existing swing strategies. Exact PineScript + screener filters behind paywall.
## [2026-03-19] ingest | 5 Swing Trading Strategies for Beginners
- Source: https://quantifiedstrategies.substack.com/p/5-swing-trading-strategies-for-beginners
- Action: Ingested article, extracted 5 strategies, created comparison table, rated Green
- Files: raw/articles/2026-03-19-5-swing-trading-strategies-for-beginners.md, wiki/sources/2026-03-19-5-swing-trading-strategies-for-beginners.md
- Rating: 🟢 Green (complete rules, 32-year backtest, actionable)
- Notes: All 5 strategies share same exit rule (Close > yesterday's High). Combined portfolio: 11.1% annual, 23% max DD. Strategy 3 (5-Day Low) is simplest and best starting point.

## [2026-04-18] ingest | Consecutive Down Days Strategy
- Source: https://quantifiedstrategies.substack.com/p/consecutive-down-days-strategy
- Action: Ingested article, extracted insights, wrote source summary
- Files: raw/articles/2026-04-18-consecutive-down-days-strategy.md, wiki/sources/2026-04-18-consecutive-down-days-strategy.md
- Rating: 🟡 Yellow (promising but rules paywalled)
- Notes: SMH outperforms SPY (1.5% vs 0.7% avg gain). Trend filter is likely the edge.

## [2026-04-19] pipeline | Consecutive Down Days Strategy 全品种回测
- Action: `cta-strategy-factory` OAT pipeline (build → run → evaluate) on 18 ETFs
- Universe: SPY, QQQ, IWM, XLK, XLI, XLV, XLF, XLE, DIA, VTI, EFA, EEM, XLB, XLP, XLU, XLRE, TLT, GLD
- Period: 2020-01-01 ~ 2026-04-18, Capital $1M
- Method: OAT with GA 100/30
- Results: 🟢 Green 11 / 🔴 Red 7 → 61.1% 探索率
- Top performers: SPY (Sharpe 1.76), VTI (1.27), DIA (1.19), XLK (1.23), XLI (1.10), GLD (1.07)
- Key finding: 默认参数 (MA=200, rsi=70) 被 GA 全面改写—SPY 最佳参数为 MA=90, rsi=25，说明短周期趋势过滤 + 低 RSI 阈值更优
- Files: `reports/eval_consecutive_down_days_20260419_065041.json`, data in `data/pipeline/ConsecutiveDownDaysStrategy_*/`
- Updated: wiki/sources/2026-04-18-consecutive-down-days-strategy.md (appended full backtest table + findings)

## [2026-04-19] ingest | Fridays for Gold, Tuesdays for Stocks
- Source: https://beyondpassive.substack.com/p/fridays-for-gold-tuesdays-for-stocks
- Action: Ingested article, extracted day-of-week ensemble strategy, wrote source summary
- Files: raw/articles/2026-03-28-fridays-for-gold-tuesdays-for-stocks.md, wiki/sources/2026-03-28-fridays-for-gold-tuesdays-for-stocks.md
- Rating: 🟢 Green (complete rules, rigorous statistics, portfolio-level reasoning)
- Notes: Tuesday VTI ensemble (D10+Monday-down → +0.469% mean, t=3.29, Sharpe 0.75) + Friday GLD (Sharpe 0.93) = Combined Sharpe 1.18. Zero overlap, -0.003 correlation. VIX/VIX3M decile filter is the key edge. Replication requires VIX3M data which is not in current database.

## [2026-04-19] ingest | 2 Years, 1M PnL and Life as a Solo Crypto Quant
- Source: https://research.hangukquant.com/p/2-years-1m-pnl-and-life-as-a-solo
- Action: Ingested article, saved raw text + source summary
- Files: raw/articles/2026-04-10-hangukquant-2-years-1m-pnl.md, wiki/sources/2026-04-10-hangukquant-2-years-1m-pnl.md
- Rating: 🟡 Yellow (experience sharing, no replicable strategy)
- Notes: Solo crypto quant journey from funding arb (~10 Sharpe, 40% APR) to HFT (~50 Sharpe). Key message: "Fear is good marketing. Do not be the product." quantpylib mentioned as multi-exchange connector framework.

## [2026-04-19] data | Downloaded VIX & VIX3M index data from IB
- Source: Interactive Brokers API (IND on CBOE)
- VIX: 5,011 bars (2006-04-24 ~ 2026-04-17)
- VIX3M: 4,195 bars (2009-08-12 ~ 2026-04-17)
- Destination: ~/.vntrader/database.db (dbbardata + dbbaroverview)
- Notes: Enables VIX/VIX3M ratio decile-10 filter for "Fridays for Gold, Tuesdays for Stocks" replication

## [2026-04-19] pipeline | Fridays for Gold, Tuesdays for Stocks 回测
- Action: `cta-strategy-factory` OAT pipeline 分别跑 TVTI + FGLD，合并 df 计算 ensemble
- TVTI (VTI): GA优化后 holding_days=7, qty=1050 | Sharpe=0.14 | Trades=32 | 总收益 2.87%
- FGLD (GLD): GA优化后 holding_days=6, qty=1950 | Sharpe=1.01 | Trades=293 | 总收益 49.32%
- Ensemble (50/50): 年化2.24% | Sharpe=0.97 | 最大回撤 -5.32% | 总收益 25.53%
- 对比文章: Friday GLD 验证成功 (1.01 vs 0.93声称)；TVTI 低于声称 (0.14 vs 0.75)，主因是未实现 Condition B (非 D10 + 两日连跌)
- Files: data/pipeline/ensemble_stats.json, ensemble_fridays_gold_tuesdays_stocks.csv
- Updated: wiki/sources/2026-03-28-fridays-for-gold-tuesdays-for-stocks.md (追加 pipeline 结果表 + 对比分析)

## [2026-04-19] pipeline | Fridays for Gold, Tuesdays for Stocks v2 (补全 Condition B)
- Action: 补全 TVTI 的 Condition B (非 D10 + 两日连跌)后重新跑 OAT+GA，重新合并 ensemble
- TVTI v2 (VTI): GA优化后 holding_days=9, qty=350 | Sharpe=0.59 | Trades=128 | 总收益 4.99%
- FGLD (GLD): 不变 | Sharpe=1.01 | Trades=293 | 总收益 49.32%
- Ensemble v2 (50/50): 年化2.32% | Sharpe=1.08 | 最大回撤 -5.28% | 总收益 26.59%
- 对比文章: Combined Sharpe 1.08 非常接近声称的 1.18；Friday GLD 一致 (1.01 vs 0.93)；TVTI 接近 (0.59 vs 0.75)
- Files: data/pipeline/ensemble_stats_v2.json, ensemble_fridays_gold_tuesdays_stocks_v2.csv
- Updated: wiki/sources/2026-03-28-fridays-for-gold-tuesdays-for-stocks.md (追加 v2 结果 + v1/v2 对比)

## [2025-04-13] init | 初始化 LLM Wiki 知识库
- 创建目录结构: raw/ (articles, papers, notes, assets) 和 wiki/ (sources, entities, concepts, syntheses, queries)
- 创建规范文档: AGENTS.md
- 创建索引: index.md
- 创建日志: log.md
- 初始化 Git 仓库

## [2025-04-13] ingest | Karpathy LLM Wiki 文章
- 来源: https://mp.weixin.qq.com/s/jTpAQ22APpNFGYEcPMPAiA
- 新增摘要页面: wiki/sources/2025-04-13_karpathy_llm_wiki.md
- 新增实体页面: wiki/entities/Andrej_Karpathy.md
- 新增概念页面:
  - wiki/concepts/LLM_Wiki.md
  - wiki/concepts/RAG.md
  - wiki/concepts/Memex.md
- 更新索引: index.md
- 摘要: 提出了三层架构（原始资料/Wiki/Schema）、三种核心操作（录入/查询/检查）

- [2026-04-20 21:45] 新增来源: `20250314-paper-review-effective-intraday-momentum` — SPY日内动量策略论文综述 (Yellow)

- [2026-04-21 01:45] 新增来源: `20250725-futures-overreact-weekly-edge` — 期货差价反转策略 (Yellow)

- [2026-04-21 02:05] OAT 复现 `20250725-futures-overreact-weekly-edge` — 加密货趋势跟踪策略近似版，GLD 最佳: Sharpe=1.32, 年化=9.46%, MaxDD=-5.28%

- [2026-04-21 02:31] V2 复现 `20250725-futures-overreact-weekly-edge` — 9模型ensemble+合约乘数修复, GLD: Sharpe=1.21/年化=18.9%, BTC: Sharpe=0.59/年化=8.5%
