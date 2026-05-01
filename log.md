
## [2026-04-30] synthesis | Crypto策略挖掘分析汇总报告
- 新增合成报告: [[crypto-strategies-analysis-2026-04-30]]
- 分析范围: 8策略 × 4 crypto品种 (BTC/ETH/SOL/DOGE)
- 核心结论: 趋势跟踪 > 突破 > 动量 > 均值回归 (Crypto适配度)
- 最佳策略: Crypto Trend Combo BTC (Sharpe=1.741, 回撤-4.99%)
- 关键发现: BTC需长Donchian窗口(38日)，ETH高波动率目标危险(-298%回撤)
- 应避免: 均值回归策略在crypto上普遍失效，DOGE上所有策略失效
- 可操作建议: P0=Crypto Trend Combo(BTC)+NR7 Breakout(BTC), P1=Donchian ADX(ETH+SOL)
- 更新: index.md (添加合成报告条目)

## [2026-04-30] update | Crypto策略回测结果汇总写入Wiki
- 更新: [[strategy-repro-crypto-trend-combo]] — 添加BTC结果 (Sharpe=1.741, 回撤-4.99%)，更新最佳品种为BTC
- 新增: [[strategy-repro-bitcoin-momentum]] — Bitcoin Momentum Strategy在BTC上Yellow评级 (Sharpe=0.476, 598交易, 回撤-54%)
- 更新: [[strategy-repro-nr7_breakout]] — 添加crypto回测图表 (BTC/ETH/SOL/DOGE)
- 复制图表: raw/assets/nr7_breakout_*_chart.png (4张)
- 更新: index.md (已验证策略表更新BTC最佳品种 + 新增Bitcoin Momentum条目)
- Crypto表现最佳: [[strategy-repro-crypto-trend-combo]] BTC Sharpe=1.741 | [[strategy-repro-nr7_breakout]] BTC Sharpe=1.021 | [[strategy-repro-donchian-adx-breakout]] ETH Sharpe=1.192 | SOL Sharpe=1.104

## [2026-04-30] pipeline | 策略复现 rsi_range_momentum
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_rsi_range_momentum_20260430_093310.json`
- Results: 🟢 Green=0 | 🟡 Yellow=0 | 🔴 Red=5 | Total=5

## [2026-05-01] fix | cta_developer RSI/RSI2策略混淆bug修复
- 问题: `pipeline.py --strategy RSI2_MR` 误匹配到 `RsiMeanReversionStrategy`（RSI）
- 根因: `resolve_strategy()` 模糊匹配 `k.upper() in name.upper()` 导致短别名 `RSI` 匹配长输入 `RSI2_MR`
- 修复: `pipeline.py` `resolve_strategy()` 改为 4 级优先级（精确→大小写不敏感精确→标准化→子串长度降序）
- 同步: `run_batch.py` `STRATEGY_OPT_PARAMS` 补全 `Rsi2Mr`/`rsi2mr`/`RsiMeanReversion`/`RSI`/`rsi` 别名
- 验证: `RSI2_MR` → `Rsi2MrStrategy` ✓ | `rsi2mr` → `Rsi2MrStrategy` ✓ | `RSI` → `RsiMeanReversionStrategy` ✓
- 新增 source: [[2026-05-01_cta-developer-rsi-strategy-confusion-fix]]
- 更新: index.md（添加概念条目 + source 条目）

## [2026-05-01] backtest | RSI vs RSI2 crypto日线回测（BTC/ETH/SOL/DOGE）
- 策略: `RsiMeanReversionStrategy`（RSI）+ 硬性 50 次交易约束 + GA pop=200 ngen=50
- 结果: 4/4 交易次数达标（54-66 笔），但夏普全负
  - BTC: 62 trades, Sharpe=-0.01 | ETH: 66 trades, Sharpe=-0.09
  - DOGE: 66 trades, Sharpe=-0.15, 总收益=-56% | SOL: 54 trades, Sharpe=-0.52
- 结论: RSI 均值回归在 crypto 强趋势市场失效，频繁止损导致亏损
- 对比: `Rsi2MrStrategy`（RSI2）在同一条件下硬性 50 次约束 → 无组合达标（6 年交易 <20 次）
- 产出: `/root/.openclaw/workspace/cta_developer/data/batch_results/rsi_crypto_20260501_114331/`

## [2026-04-30] pipeline | 策略复现 nr7_breakout
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_nr7_breakout_20260430_083327.json`
- Results: 🟢 Green=4 | 🟡 Yellow=0 | 🔴 Red=3 | Total=7
- Best: SPY | Sharpe=1.212 | Trades=459 | MaxDD=-6.51% | Annual=4.88%
- Optimal params: {"nr_lookback": 3, "trend_ma_period": 15, "use_long_only": 1.06, "use_trend_filter": 0.7}

## [2026-04-29] ingest | SetupAlpha — 3x Leveraged ETF Strategy
- 新增 raw: `raw/articles/setup4alpha-leveraged-etf-strategy.md`
- 新增 source: `wiki/sources/2025-10-05_leveraged-etf-strategy.md`
- 更新: `index.md` (+4 concepts, +source entry)
- 关键内容: TQQQ+TMF 50/50 双月再平衡，15年 CAGR 19.6%，崩溃过滤器

## [2026-04-29] ingest | Algorithmicguys — Tradable Futures Portfolio
- 新增 raw: `raw/articles/algorithmicguys-tradable-futures-portfolio.md`
- 新增 source: `wiki/sources/2025-11-04_tradable-futures-portfolio.md`
- 更新: `index.md` (实体 + 来源)
- 关键内容: 12策略期货组合构建法，仅用 incubation/live 数据，Monte Carlo验证

## [2026-04-28] pipeline | 策略复现 macd_histogram_rev_20260416
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_macd_histogram_rev_20260416_20260428_233544.json`
- Results: 🟢 Green=1 | 🟡 Yellow=0 | 🔴 Red=3 | Total=4
- Best: QQQ | Sharpe=1.397 | Trades=152 | MaxDD=-34.35% | Annual=63.95%
- Optimal params: {"decline_days": 2, "fast_period": 11, "signal_period": 9, "slow_period": 41}

## [2026-04-28] pipeline | 策略复现 macd_histogram_rev_20260416
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_macd_histogram_rev_20260416_20260428_231105.json`
- Results: 🟢 Green=0 | 🟡 Yellow=0 | 🔴 Red=4 | Total=4

## [2026-04-28] pipeline | 策略复现 simple_trend_following
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_simple_trend_following_20260428_192347.json`
- Results: 🟢 Green=2 | 🟡 Yellow=1 | 🔴 Red=1 | Total=4
- Best: QQQ | Sharpe=1.023 | Trades=263 | MaxDD=-4.37% | Annual=5.66%
- Optimal params: {"ma_period": 33, "fixed_stop_pct": 0.013, "trailing_stop_pct": 0.0219, "cond_lookback_1": 1, "cond_lookback_2": 2}

## [2026-04-28] pipeline | 策略复现 simple_trend_following
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_simple_trend_following_20260428_192347.json`
- Results: 🟢 Green=2 | 🟡 Yellow=1 | 🔴 Red=1 | Total=4
- Best: QQQ | Sharpe=1.023 | Trades=263 | MaxDD=-4.37% | Annual=5.66%
- Optimal params: {"ma_period": 33, "fixed_stop_pct": 0.013, "trailing_stop_pct": 0.0219, "cond_lookback_1": 1, "cond_lookback_2": 2}

## [2026-04-28] pipeline | 策略复现 simple_trend_following
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_simple_trend_following_20260428_192347.json`
- Results: 🟢 Green=2 | 🟡 Yellow=1 | 🔴 Red=1 | Total=4
- Best: QQQ | Sharpe=1.023 | Trades=263 | MaxDD=-4.37% | Annual=5.66%
- Optimal params: {"ma_period": 33, "fixed_stop_pct": 0.013, "trailing_stop_pct": 0.0219, "cond_lookback_1": 1, "cond_lookback_2": 2}

## [2026-04-28] pipeline | 策略复现 simple_trend_following
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_simple_trend_following_20260428_192347.json`
- Results: 🟢 Green=2 | 🟡 Yellow=1 | 🔴 Red=1 | Total=4
- Best: QQQ | Sharpe=1.023 | Trades=263 | MaxDD=-4.37% | Annual=5.66%
- Optimal params: {"ma_period": 33, "fixed_stop_pct": 0.013, "trailing_stop_pct": 0.0219, "cond_lookback_1": 1, "cond_lookback_2": 2}

## [2026-04-28] pipeline | 策略复现 simple_trend_following
- Action: `strategy_factory` auto pipeline (build → run → evaluate → wiki sync)
- Eval file: `eval_simple_trend_following_20260428_192347.json`
- Results: 🟢 Green=2 | 🟡 Yellow=1 | 🔴 Red=1 | Total=4
- Best: QQQ | Sharpe=1.023 | Trades=263 | MaxDD=-4.37% | Annual=5.66%
- Optimal params: {"ma_period": 33, "fixed_stop_pct": 0.013, "trailing_stop_pct": 0.0219, "cond_lookback_1": 1, "cond_lookback_2": 2}

## [2026-04-27] pipeline | 策略复现 spy_overnight_200sma
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_spy_overnight_200sma_20260427_193301.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 equity_curve_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_equity_curve_mean_reversion_20260427_192143.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 equity_curve_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_equity_curve_mean_reversion_20260427_191234.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-27] pipeline | 策略复现 sp500_trend_following
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_trend_following_20260427_121454.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 profitable_systematic_rules
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_profitable_systematic_rules_20260427_091031.json`
- Results:  Green=0 |  Yellow=1 |  Red=1 | Total=2

## [2026-04-27] pipeline | 策略复现 mean_reversion_curve_portfolio
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mean_reversion_curve_portfolio_20260427_090548.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 larry_connors_b_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_larry_connors_b_strategy_20260427_090530.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-27] pipeline | 策略复现 olmar_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_olmar_mean_reversion_20260427_090513.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 pullback_trading_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pullback_trading_strategy_20260427_090458.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-27] pipeline | 策略复现 intraday_fade_breakout_30m
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_intraday_fade_breakout_30m_20260427_090443.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 five_rules_systematic_trading
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_five_rules_systematic_trading_20260427_090435.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-27] pipeline | 策略复现 systematic_trading_rules
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_systematic_trading_rules_20260427_090432.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-27] pipeline | 策略复现 sp500_trend_following
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_trend_following_20260427_090423.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 five_rules_profitable_trading
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_five_rules_profitable_trading_20260427_090402.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 sp500_trend_following
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_trend_following_20260427_090335.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-27] pipeline | 策略复现 sp500_trend_following
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_trend_following_20260427_090019.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1


## [2026-04-26] ingest | The Intraday Alpha Atlas: What Works on 30-Minute Bars

- 作者: Delphic Alpha
- 来源: Substack (用户分享)
- 新增: wiki/sources/2026-04-26-delphic-intraday-alpha-atlas.md
- 新增概念: [[Intraday-Alpha]], [[Fade-Breakout]]
- 新增实体: [[Delphic Alpha]]
- 更新: index.md, log.md
- 存档: substack-strategy-tracker/articles/delphicalpha/

## [2026-04-26] synthesis | 反转策略全景分析

- 新增: wiki/syntheses/reversal-strategy-landscape.md
- 分析 10+ 反转策略 × 24 ETF 的品种分类匹配规律
- 提出 4 大类反转策略 + 5 类品种的适配矩阵
- 更新: index.md, log.md

## [2026-04-26] pipeline | 策略复现 larry_connors_b_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_larry_connors_b_strategy_20260426_121738.json`
- Results:  Green=0 |  Yellow=4 |  Red=1 | Total=5

## [2026-04-26] pipeline | 策略复现 larry_connors_b_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_larry_connors_b_strategy_20260426_090519.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-26] ingest | Pullback Trading Strategies (QuantifiedStrategies)

- 作者: QuantifiedStrategies
- 来源: Substack
- 新增: wiki/sources/2023-12-25-pullback-trading-strategies-backtest.md
- 更新: index.md, log.md
- 存档: substack-strategy-tracker/articles/quantifiedstrategies/

## [2026-04-26] ingest | Taming OLMAR's 1222% Backtest into a Sustainable 106% CAGR

- 作者: Stuart Farmer (Paper to Profit)
- 来源: Substack (用户分享)
- 新增: wiki/sources/2025-05-20-taming-olmar-1222-backtest-into.md
- 新增概念: [[OLMAR]], 在线投资组合选择
- 更新: index.md, log.md
- 存档: substack-strategy-tracker/articles/papertoprofit/

## [2026-04-26] pipeline | 策略复现 mean_reversion_curve_portfolio
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mean_reversion_curve_portfolio_20260426_090331.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-26] pipeline | 策略复现 larry_connors_b_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_larry_connors_b_strategy_20260426_090024.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-26] ingest | Trading the Mean Reversion Curve

- 作者: Quantitativo (Quant Trading Rules)
- 来源: Substack (用户分享)
- 新增: wiki/sources/2026-04-26_trading-the-mean-reversion-curve.md
- 新增实体: [[Quantitativo]]
- 新增概念: 均值回归曲线 / 参数分散组合
- 更新: index.md, log.md
- 存档: substack-strategy-tracker/articles/quantitativo/
- Git: 待推送

## [2026-04-25] merge | Wiki 合并整理：quant-wiki + obsidian-vault → llm-wiki

- Action: 将 quant-wiki (7.3MB, 本地仓库) 和 obsidian-vault (688KB, 独立 GitHub 仓库) 合并至 llm-wiki，然后清理原目录
- [... rest of existing entry]
- 状态: 合并完成，已 git commit + push + 清理

## [2026-04-25] import | 补录 substack-tracker 今日下载的 74 篇文章

- Action: 将 substack-tracker 今天(2026-04-25)定时任务下载的 471 篇文章中，尚未导入的 74 篇补入 llm-wiki
- TradeQuantiX: 66 篇（All-Weather Portfolio Research, Portfolio Development Series, Trading System Investigation Series, ETF Mean Reversion 等）
- Algomatic Trading: 2 篇（How Correlation Between Strategies Affects Your Portfolio Risk, Portfolio 7 Gold Portfolio）
- QuantSeeker: 2 篇（Pairs Trading in the Metals Complex, Weekly Research Recap）
- 去重: 391 篇(quant-wiki 已合并) + 4 篇(之前已有) = 跳过 397 篇，实际导入 74 篇
- sources 页面: 0 缺失（已有对应 source 页面来自之前的 batch 导入）
- Git: 5e61100, 70 files, +9177 lines
- quant-wiki 迁移:
  - raw/articles/ → 391 篇 QuantifiedStrategies Substack 文章
  - wiki/sources/ → 391 篇摘要（0 文件名冲突）
  - wiki/entities/ → 5 篇 (Larry Connors, QQQ, SPY, XLP, QuantifiedStrategies-com)
  - wiki/concepts/ → 6 篇 (IBS, Mean-Reversion, Overnight-Edge, Position-Sizing, RSI, Williams %R)
  - wiki/strategies/ → 5 篇
  - wiki/syntheses/ → 1 篇
- obsidian-vault 迁移:
  - raw/notes/ → 17 篇手动日内策略笔记
  - raw/articles/ → 34 篇 Substack 日内策略原文（6 篇 unique 文件名）
  - raw/articles/ → 1 篇独立文章（商品期货分类笔记）
- 新增合并 source 页面: wiki/sources/2026-04-25_quant-wiki-merge.md + 2026-04-25_obsidian-vault-merge-intraday-notes.md
- llm-wiki 总计: raw/articles 1237 篇, raw/notes 26 篇, wiki/sources 2102 篇, entities 6, concepts 24, syntheses 4, strategies 7
- 待清理: rm -rf ~/quant-wiki ~/obsidian-vault ~/Obsidian\ Vault
- 更新: index.md (实体+概念+来源+最近活动), log.md
- 状态: 合并完成，待 git commit + push + 清理

- Action: 扩展 NR7 ETF 批量优化脚本支持 24 个 IB 期货品种
- 修改文件:
  - `cta/pipeline/asset_registry.py` — 新增 IB_FUTURES 模板 + 24个品种合约规格字典
  - `pipeline_batch_nr7_etf.py` — 支持完整 vt_symbol（`@ES.CME`），新增 FUTURES_SYMBOLS + --futures/--futures-only
  - `scripts/run_nr7_etf_batch.py` — 新增 FUTURES_SYMBOLS + FUTURES_EXCHANGE_MAP + futures_mode 参数
- 数据库验证: 24个期货品种均可在 vnpy SQLite 中找到日线数据，最早数据自 2014 年起
- 新增 wiki: [[2026-04-25-nr7-futures-batch-pipeline]]
- 更新: index.md (Sources + 最近活动)
- 状态: 待运行首轮期货优化

## [2026-04-25] sync | 8个反转策略复现结果同步至wiki

- Action: 将pipeline queue中8个有回测数据但未同步的反转策略复现结果批量同步至llm-wiki
- 新增 wiki/sources/:
  - strategy-repro-gold-envelope.md | Gold Envelope 黄金包络线 | GLD Sharpe=1.357, 93笔交易, Green 🟢
  - strategy-repro-stochastic-extremes-gold.md | 随机指标极值黄金系统 | 全品种RED, 交易次数严重不足 🔴
  - strategy-repro-weekly-mean-reversion-sp500.md | SP500周线均值回归 | Sharpe=0.954, 193笔交易, Green 🟢
  - strategy-repro-bollinger-band-squeeze.md | 布林带收缩策略 | 全品种RED, QQQ Sharpe=0.766, 48笔交易 🔴
  - strategy-repro-macd-bitcoin.md | 比特币MACD交叉策略 | Sharpe=0.944, 回撤51.76%, RED 🔴
  - strategy-repro-pullback-trading.md | 回调交易策略 | SPY Sharpe=0.895, 96笔交易, YELLOW 🟡
  - strategy-repro-rsi2-did-you-miss.md | RSI-2隐藏策略 | GLD Sharpe=1.479, IWM Sharpe=1.170, 2品种Green 🟢
  - strategy-repro-trading-hour-best.md | 最佳交易时段 | 无有效回测结果 🔴
- 结果汇总: 3只Green (gold_envelope, weekly_mr, rsi2), 1只Yellow (pullback), 4只Red/无结果
- 更新: index.md (Sources表格 + 最近活动 + 里程碑列表)
- 状态: 等待git推送

## [2026-04-23] ingest | Counter-Trend ES Model (Alpha Algo Trading Research)
- 新增: wiki/sources/2026-04-22_Counter-Trend-ES-Model.md
- 新增概念: [[Counter-Trend Trading]], [[Snapback Trading]], [[Intraday Strategy]]
- 更新: index.md (最近活动)
- 状态: 文章已保存，待获取ES 15m数据完成完整复现
- 文章结果: 1,482 trades, 1.64 PF, 48.99% WR, 2,335% Ret/DD over 28.5 years

## [2026-04-23] fix | OKX Data Platform - get_bar_overview() timeout
- 修复: okx/okx_download_vnpy.py _get_data_range_from_db() — SQLite直接查询替代get_bar_overview()
- 效果: 4小时超时 → ~5分钟完成31品种K线+20品种资金费率更新
- 关联: crypto-data-platform-maintenance skill Pitfalls #1 已同步更新

## [2026-04-23] synthesis | 均值回归/反转策略汇编
- Action: 深度加工知识库中所有反转/均值回归策略，生成综合汇编页面
- 新增 wiki/syntheses/:
  - mean-reversion-strategies-compendium.md (汇编 12+ 策略，按5类信号类型分析，给10项关键注意事项，2套组合建议)
- 核心结论:
  - Green级可上实盘: Consecutive Down Days (SPY Sharpe 1.76), MACD Hook Gold (GLD Sharpe 1.22), MACD Histogram Rev (QQQ Sharpe 1.04), ETF MR Mini-Portfolio
  - 趋势过滤器是反转策略生死线
  - 出场规则比入场更重要 (`Close > yesterday's High` 是灵魂)
  - 过拟合税: 回测 Sharpe 打 75 折
  - Portfolio Effect 是唯一圣杯
- 更新: index.md, log.md
- 状态: 已推送远程仓库

## [2026-04-22] deep-process | 日内策略汇编 + Checklist
- Action: 深度处理知识库中所有日内策略，生成汇编和 Checklist
- 新增 wiki/sources/:
  - 2026-04-22-session-high-retest-intraday-strategy.md (Session High Retest 深度处理，包含完整规则、回测数据、伪代码框架)
  - 2026-02-23-systematic-intraday-trend-following-strategy.md (系统性日内趋势跟踪深度处理，SPY Sharpe 1.33)
- 新增 wiki/concepts/:
  - intraday-trading-strategies-compendium.md (汇编 7+篇日内策略，按类型分类、模板化)
  - intraday-strategy-design-checklist.md (十项检查清单 + 3 个设计模板)
- 涵盖策略: Session High Retest, Systematic Intraday TF, VWAP+StochRSI, VSO Momentum, ORB, Late Lunch, Next-Day Signal
- 更新 index.md

## [2026-04-22] ingest | 补录 2 篇未导入 Substack 文章
- Action: 将 substack-strategy-tracker 中未入库的 2 篇文章导入 llm-wiki
- 新增 raw/articles/:
  - 2026-04-22-Bollinger-Band-Squeeze-Trading-Strategy.md (布林带挤压，yellow)
  - 2025-04-22-etf-mean-reversion-methods-mean-reversion-mini-portfolio-creation-part-2.md (ETF均值回归组合，green)
- 新增 wiki/sources/ 对应骨架
- 更新 index.md

## [2026-04-22] ingest | Delphic Alpha 多资产 Alpha 图谱文章
- Action: 导入 Substack 文章至 llm-wiki
- 新增: wiki/sources/2025-04-22-simple-alpha-atlas-what-actually-works-across-markets-daily.md
- 内容: 12 alphas × 5 资产类别零优化回测，核心结论是无通用 alpha，必须匹配信号类型与市场微观结构
- 更新: index.md


## [2026-04-22] pipeline | 策略复现 weekly_etf_rotation
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_weekly_etf_rotation_20260422_090207.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 volatility_swing_trade_nasdaq_sp500
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_volatility_swing_trade_nasdaq_sp500_20260422_040627.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 vix_fear_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_mean_reversion_20260422_041718.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 vix_fear_indicator
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_indicator_20260422_092325.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 vix_fear_gauge
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_gauge_20260422_092319.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 vix_100_sma_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_100_sma_cross_20260422_033554.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 unfilled_gap_inside_day
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_unfilled_gap_inside_day_20260422_092302.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 unfilled_gap_down_inside_day
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_unfilled_gap_down_inside_day_20260422_040859.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 turn_of_the_month
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_turn_of_the_month_20260422_041947.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 tuesday_vti
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_tuesday_vti_20260422_094236.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 trend_following_gold_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_trend_following_gold_breakout_20260422_035256.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 thanksgiving_holiday_effect
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_thanksgiving_holiday_effect_20260422_040724.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 stochastic_short_term_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_stochastic_short_term_mean_reversion_20260422_040503.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 stochastic_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_stochastic_mean_reversion_20260422_092244.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 spy_gld_rotation
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_spy_gld_rotation_20260422_032114.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 sp500_monthly_sma_momentum
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_monthly_sma_momentum_20260422_040404.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 sp500_momentum_monthly_sma
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_momentum_monthly_sma_20260422_030534.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 sma200_trend_following_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sma200_trend_following_20260420_20260420_104244.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=0.686 | Trades=105 | MaxDD=-321.54% | Annual=102.16%
- Optimal params: {"sma_period": 112, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 simple_momentum_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_simple_momentum_4_etfs_20260422_092234.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 russell_2000_death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_russell_2000_death_cross_20260422_031813.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_strategy_20260422_092217.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2_larry_connors
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_larry_connors_20260422_092211.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 pullback_trading_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pullback_trading_strategy_20260422_061907.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 price_action_seasonal_filter_bonds
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_price_action_seasonal_filter_bonds_20260422_042514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 pairs_trading_metals_complex
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pairs_trading_metals_complex_20260422_092202.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 one_simple_momentum_strategy_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_one_simple_momentum_strategy_4_etfs_20260422_092152.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 one_simple_momentum_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_one_simple_momentum_4_etfs_20260422_041814.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 nr7_enhanced
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_nr7_enhanced_20260422_031526.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 nr7_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_nr7_breakout_20260422_094223.json`
- Results:  Green=1 |  Yellow=1 |  Red=4 | Total=6
- Best: SPY | Sharpe=1.288 | Trades=460 | MaxDD=-0.52% | Annual=0.60%
- Optimal params: {"nr_lookback": 2, "use_trend_filter": 0.7, "trend_ma_period": 15, "use_long_only": 0.94, "fixed_size": 1}

## [2026-04-22] pipeline | 策略复现 moving_average_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_moving_average_crossover_20260422_033024.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 metals_pairs_trading_reality_check
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_metals_pairs_trading_reality_check_20260422_091916.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 mae_mfe_excursion_optimizer
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mae_mfe_excursion_optimizer_20260422_091858.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 mae_mfe_analysis
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mae_mfe_analysis_20260422_041440.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 macd_hook_gold_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_strategy_20260422_062912.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 macd_hook_gold
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_20260420_171931.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: GLD | Sharpe=1.223 | Trades=33 | MaxDD=-135.25% | Annual=207.83%
- Optimal params: {"fast_period": 15, "slow_period": 19, "signal_period": 10, "hull_period": 10, "fixed_size": 70, "bullish_days": 5, "max_holding_days": 7, "stop_loss_pct": 3.69}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev_20260416
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260416_20260416_064027.json`
- Results:  Green=1 |  Yellow=1 |  Red=0 | Total=2
- Best: QQQ | Sharpe=1.038 | Trades=92 | MaxDD=-40.25% | Annual=38.79%
- Optimal params: {"decline_days": 3, "signal_period": 12, "slow_period": 34}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260422_094000.json`
- Results:  Green=0 |  Yellow=0 |  Red=6 | Total=6

## [2026-04-22] pipeline | 策略复现 macd_histogram_auto_test
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_auto_test_20260417_154346.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-22] pipeline | 策略复现 macd_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_crossover_20260422_031201.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 friday_gld
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_friday_gld_20260422_093855.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 end_of_month_strategy_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_end_of_month_strategy_20260420_20260420_140544.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=1.029 | Trades=137 | MaxDD=-90.70% | Annual=71.59%
- Optimal params: {"target_pct": 0.009399999999999999, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 donchian_channel_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_donchian_channel_breakout_20260422_035102.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 donchian_adx_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_donchian_adx_breakout_20260422_093345.json`
- Results:  Green=2 |  Yellow=1 |  Red=3 | Total=6
- Best: ETHUSDT_SWAP_OKX.GLOBAL | Sharpe=1.192 | Trades=30 | MaxDD=-14.21% | Annual=14.76%
- Optimal params: {"donchian_window": 5, "exit_window": 5, "adx_window": 12, "adx_threshold": 18, "adx_mode": 1, "use_long_only": 1.06, "ma_period": 130, "fixed_size": 15}

## [2026-04-22] pipeline | 策略复现 death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_death_cross_20260422_035514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 crypto_trend_combo_v2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_crypto_trend_combo_v2_20260422_090825.json`
- Results:  Green=4 |  Yellow=0 |  Red=0 | Total=4
- Best: GLD | Sharpe=1.224 | Trades=651 | MaxDD=-653.67% | Annual=1599.65%
- Optimal params: {"target_vol": 0.21, "max_leverage": 1.5039999999999998, "vol_lookback": 67, "rebalance_threshold": 0.47}

## [2026-04-22] pipeline | 策略复现 crypto_trend_combo
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_crypto_trend_combo_20260422_090538.json`
- Results:  Green=4 |  Yellow=0 |  Red=0 | Total=4
- Best: BTCUSDT_SWAP_OKX.GLOBAL | Sharpe=1.741 | Trades=23 | MaxDD=-4.99% | Annual=14.31%
- Optimal params: {"donchian_window": 38, "vol_lookback": 44, "target_vol": 0.13299999999999998, "max_leverage": 0.63}

## [2026-04-22] pipeline | 策略复现 consecutive_down_days_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_strategy_20260422_042101.json`
- Results:  Green=0 |  Yellow=0 |  Red=3 | Total=3

## [2026-04-22] pipeline | 策略复现 consecutive_down_days
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_20260419_065041.json`
- Results:  Green=11 |  Yellow=0 |  Red=7 | Total=18
- Best: SPY | Sharpe=1.762 | Trades=174 | MaxDD=-2.25% | Annual=6.78%
- Optimal params: {"decline_days": 3, "trend_ma_period": 90, "max_hold_days": 5, "rsi_exit_threshold": 25, "fixed_size": 15}

## [2026-04-22] pipeline | 策略复现 commodity_skewness_premium
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_commodity_skewness_premium_20260422_042318.json`
- Results:  Green=0 |  Yellow=0 |  Red=8 | Total=8

## [2026-04-22] pipeline | 策略复现 combined_candlestick_top5
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_top5_20260422_090418.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 combined_candlestick_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_strategy_20260422_041242.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 bollinger_band_squeeze
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_bollinger_band_squeeze_20260422_090710.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 bollinger_band_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_bollinger_band_breakout_20260422_092936.json`
- Results:  Green=0 |  Yellow=1 |  Red=5 | Total=6

## [2026-04-22] pipeline | 策略复现 backtested_bollinger_bands_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_backtested_bollinger_bands_strategy_20260422_090221.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 backtested_bollinger_bands
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_backtested_bollinger_bands_20260422_033235.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 weekly_etf_rotation
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_weekly_etf_rotation_20260422_090207.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 volatility_swing_trade_nasdaq_sp500
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_volatility_swing_trade_nasdaq_sp500_20260422_040627.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 vix_fear_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_mean_reversion_20260422_041718.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 vix_fear_indicator
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_indicator_20260422_092325.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 vix_fear_gauge
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_gauge_20260422_092319.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 vix_100_sma_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_100_sma_cross_20260422_033554.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 unfilled_gap_inside_day
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_unfilled_gap_inside_day_20260422_092302.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 unfilled_gap_down_inside_day
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_unfilled_gap_down_inside_day_20260422_040859.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 turn_of_the_month
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_turn_of_the_month_20260422_041947.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 tuesday_vti
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_tuesday_vti_20260422_092256.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 trend_following_gold_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_trend_following_gold_breakout_20260422_035256.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 thanksgiving_holiday_effect
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_thanksgiving_holiday_effect_20260422_040724.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 stochastic_short_term_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_stochastic_short_term_mean_reversion_20260422_040503.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 stochastic_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_stochastic_mean_reversion_20260422_092244.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 spy_gld_rotation
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_spy_gld_rotation_20260422_032114.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 sp500_monthly_sma_momentum
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_monthly_sma_momentum_20260422_040404.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 sp500_momentum_monthly_sma
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_momentum_monthly_sma_20260422_030534.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 sma200_trend_following_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sma200_trend_following_20260420_20260420_104244.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=0.686 | Trades=105 | MaxDD=-321.54% | Annual=102.16%
- Optimal params: {"sma_period": 112, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 simple_momentum_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_simple_momentum_4_etfs_20260422_092234.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 russell_2000_death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_russell_2000_death_cross_20260422_031813.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_strategy_20260422_092217.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2_larry_connors
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_larry_connors_20260422_092211.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 pullback_trading_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pullback_trading_strategy_20260422_061907.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 price_action_seasonal_filter_bonds
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_price_action_seasonal_filter_bonds_20260422_042514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 pairs_trading_metals_complex
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pairs_trading_metals_complex_20260422_092202.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 one_simple_momentum_strategy_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_one_simple_momentum_strategy_4_etfs_20260422_092152.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 one_simple_momentum_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_one_simple_momentum_4_etfs_20260422_041814.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 nr7_enhanced
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_nr7_enhanced_20260422_031526.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 nr7_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_nr7_breakout_20260422_092135.json`
- Results:  Green=1 |  Yellow=1 |  Red=4 | Total=6
- Best: SPY | Sharpe=1.288 | Trades=460 | MaxDD=-0.52% | Annual=0.60%
- Optimal params: {"nr_lookback": 2, "use_trend_filter": 0.82, "trend_ma_period": 15, "use_long_only": 1.1800000000000002, "fixed_size": 1}

## [2026-04-22] pipeline | 策略复现 moving_average_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_moving_average_crossover_20260422_033024.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 metals_pairs_trading_reality_check
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_metals_pairs_trading_reality_check_20260422_091916.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 mae_mfe_excursion_optimizer
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mae_mfe_excursion_optimizer_20260422_091858.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 mae_mfe_analysis
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mae_mfe_analysis_20260422_041440.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 macd_hook_gold_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_strategy_20260422_062912.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 macd_hook_gold
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_20260420_171931.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: GLD | Sharpe=1.223 | Trades=33 | MaxDD=-135.25% | Annual=207.83%
- Optimal params: {"fast_period": 15, "slow_period": 19, "signal_period": 10, "hull_period": 10, "fixed_size": 70, "bullish_days": 5, "max_holding_days": 7, "stop_loss_pct": 3.69}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev_20260416
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260416_20260416_064027.json`
- Results:  Green=1 |  Yellow=1 |  Red=0 | Total=2
- Best: QQQ | Sharpe=1.038 | Trades=92 | MaxDD=-40.25% | Annual=38.79%
- Optimal params: {"decline_days": 3, "signal_period": 12, "slow_period": 34}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260422_091841.json`
- Results:  Green=0 |  Yellow=0 |  Red=6 | Total=6

## [2026-04-22] pipeline | 策略复现 macd_histogram_auto_test
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_auto_test_20260417_154346.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-22] pipeline | 策略复现 macd_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_crossover_20260422_031201.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 friday_gld
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_friday_gld_20260422_091736.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 end_of_month_strategy_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_end_of_month_strategy_20260420_20260420_140544.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=1.029 | Trades=137 | MaxDD=-90.70% | Annual=71.59%
- Optimal params: {"target_pct": 0.009399999999999999, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 donchian_channel_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_donchian_channel_breakout_20260422_035102.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 donchian_adx_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_donchian_adx_breakout_20260422_091226.json`
- Results:  Green=1 |  Yellow=1 |  Red=4 | Total=6
- Best: SOLUSDT_SWAP_OKX.GLOBAL | Sharpe=1.104 | Trades=60 | MaxDD=-6.63% | Annual=9.65%
- Optimal params: {"donchian_window": 22, "exit_window": 2, "adx_window": 12, "adx_threshold": 15, "adx_mode": 3, "use_long_only": 0.82, "ma_period": 159, "fixed_size": 15}

## [2026-04-22] pipeline | 策略复现 death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_death_cross_20260422_035514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 crypto_trend_combo_v2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_crypto_trend_combo_v2_20260422_090825.json`
- Results:  Green=4 |  Yellow=0 |  Red=0 | Total=4
- Best: GLD | Sharpe=1.224 | Trades=651 | MaxDD=-653.67% | Annual=1599.65%
- Optimal params: {"target_vol": 0.21, "max_leverage": 1.5039999999999998, "vol_lookback": 67, "rebalance_threshold": 0.47}

## [2026-04-22] pipeline | 策略复现 crypto_trend_combo
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_crypto_trend_combo_20260422_090538.json`
- Results:  Green=4 |  Yellow=0 |  Red=0 | Total=4
- Best: BTCUSDT_SWAP_OKX.GLOBAL | Sharpe=1.741 | Trades=23 | MaxDD=-4.99% | Annual=14.31%
- Optimal params: {"donchian_window": 38, "vol_lookback": 44, "target_vol": 0.13299999999999998, "max_leverage": 0.63}

## [2026-04-22] pipeline | 策略复现 consecutive_down_days_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_strategy_20260422_042101.json`
- Results:  Green=0 |  Yellow=0 |  Red=3 | Total=3

## [2026-04-22] pipeline | 策略复现 consecutive_down_days
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_20260419_065041.json`
- Results:  Green=11 |  Yellow=0 |  Red=7 | Total=18
- Best: SPY | Sharpe=1.762 | Trades=174 | MaxDD=-2.25% | Annual=6.78%
- Optimal params: {"decline_days": 3, "trend_ma_period": 90, "max_hold_days": 5, "rsi_exit_threshold": 25, "fixed_size": 15}

## [2026-04-22] pipeline | 策略复现 commodity_skewness_premium
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_commodity_skewness_premium_20260422_042318.json`
- Results:  Green=0 |  Yellow=0 |  Red=8 | Total=8

## [2026-04-22] pipeline | 策略复现 combined_candlestick_top5
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_top5_20260422_090418.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 combined_candlestick_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_strategy_20260422_041242.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 bollinger_band_squeeze
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_bollinger_band_squeeze_20260422_090710.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 bollinger_band_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_bollinger_band_breakout_20260422_090413.json`
- Results:  Green=0 |  Yellow=1 |  Red=5 | Total=6

## [2026-04-22] pipeline | 策略复现 backtested_bollinger_bands_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_backtested_bollinger_bands_strategy_20260422_090221.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 backtested_bollinger_bands
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_backtested_bollinger_bands_20260422_033235.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 combined_candlestick_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_strategy_20260422_041242.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 volatility_swing_trade_nasdaq_sp500
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_volatility_swing_trade_nasdaq_sp500_20260422_040627.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 vix_fear_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_mean_reversion_20260422_041718.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 vix_100_sma_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_100_sma_cross_20260422_033554.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 unfilled_gap_down_inside_day
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_unfilled_gap_down_inside_day_20260422_040859.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 turn_of_the_month
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_turn_of_the_month_20260422_041947.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 trend_following_gold_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_trend_following_gold_breakout_20260422_035256.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 thanksgiving_holiday_effect
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_thanksgiving_holiday_effect_20260422_040724.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 stochastic_short_term_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_stochastic_short_term_mean_reversion_20260422_040503.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 spy_gld_rotation
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_spy_gld_rotation_20260422_032114.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 sp500_monthly_sma_momentum
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_monthly_sma_momentum_20260422_040404.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 sp500_momentum_monthly_sma
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_momentum_monthly_sma_20260422_030534.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 sma200_trend_following_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sma200_trend_following_20260420_20260420_104244.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=0.686 | Trades=105 | MaxDD=-321.54% | Annual=102.16%
- Optimal params: {"sma_period": 112, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 russell_2000_death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_russell_2000_death_cross_20260422_031813.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 pullback_trading_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pullback_trading_strategy_20260422_061907.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 price_action_seasonal_filter_bonds
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_price_action_seasonal_filter_bonds_20260422_042514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 one_simple_momentum_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_one_simple_momentum_4_etfs_20260422_041814.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 nr7_enhanced
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_nr7_enhanced_20260422_031526.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 moving_average_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_moving_average_crossover_20260422_033024.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 mae_mfe_analysis
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mae_mfe_analysis_20260422_041440.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 macd_hook_gold_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_strategy_20260422_062912.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 macd_hook_gold
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_20260420_171931.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: GLD | Sharpe=1.223 | Trades=33 | MaxDD=-135.25% | Annual=207.83%
- Optimal params: {"fast_period": 15, "slow_period": 19, "signal_period": 10, "hull_period": 10, "fixed_size": 70, "bullish_days": 5, "max_holding_days": 7, "stop_loss_pct": 3.69}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev_20260416
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260416_20260416_064027.json`
- Results:  Green=1 |  Yellow=1 |  Red=0 | Total=2
- Best: QQQ | Sharpe=1.038 | Trades=92 | MaxDD=-40.25% | Annual=38.79%
- Optimal params: {"decline_days": 3, "signal_period": 12, "slow_period": 34}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260416_073639.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-22] pipeline | 策略复现 macd_histogram_auto_test
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_auto_test_20260417_154346.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-22] pipeline | 策略复现 macd_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_crossover_20260422_031201.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 end_of_month_strategy_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_end_of_month_strategy_20260420_20260420_140544.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=1.029 | Trades=137 | MaxDD=-90.70% | Annual=71.59%
- Optimal params: {"target_pct": 0.009399999999999999, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 donchian_channel_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_donchian_channel_breakout_20260422_035102.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_death_cross_20260422_035514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 consecutive_down_days_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_strategy_20260422_042101.json`
- Results:  Green=0 |  Yellow=0 |  Red=3 | Total=3

## [2026-04-22] pipeline | 策略复现 consecutive_down_days
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_20260419_065041.json`
- Results:  Green=11 |  Yellow=0 |  Red=7 | Total=18
- Best: SPY | Sharpe=1.762 | Trades=174 | MaxDD=-2.25% | Annual=6.78%
- Optimal params: {"decline_days": 3, "trend_ma_period": 90, "max_hold_days": 5, "rsi_exit_threshold": 25, "fixed_size": 15}

## [2026-04-22] pipeline | 策略复现 commodity_skewness_premium
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_commodity_skewness_premium_20260422_042318.json`
- Results:  Green=0 |  Yellow=0 |  Red=8 | Total=8

## [2026-04-22] pipeline | 策略复现 combined_candlestick_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_strategy_20260422_041242.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 backtested_bollinger_bands
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_backtested_bollinger_bands_20260422_033235.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 volatility_swing_trade_nasdaq_sp500
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_volatility_swing_trade_nasdaq_sp500_20260422_040627.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 vix_fear_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_fear_mean_reversion_20260422_041718.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 vix_100_sma_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_vix_100_sma_cross_20260422_033554.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 unfilled_gap_down_inside_day
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_unfilled_gap_down_inside_day_20260422_040859.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 turn_of_the_month
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_turn_of_the_month_20260422_041947.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 trend_following_gold_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_trend_following_gold_breakout_20260422_035256.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 thanksgiving_holiday_effect
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_thanksgiving_holiday_effect_20260422_040724.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 stochastic_short_term_mean_reversion
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_stochastic_short_term_mean_reversion_20260422_040503.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 spy_gld_rotation
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_spy_gld_rotation_20260422_032114.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 sp500_monthly_sma_momentum
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_monthly_sma_momentum_20260422_040404.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 sp500_momentum_monthly_sma
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sp500_momentum_monthly_sma_20260422_030534.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 sma200_trend_following_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_sma200_trend_following_20260420_20260420_104244.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=0.686 | Trades=105 | MaxDD=-321.54% | Annual=102.16%
- Optimal params: {"sma_period": 112, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 russell_2000_death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_russell_2000_death_cross_20260422_031813.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 pullback_trading_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_pullback_trading_strategy_20260422_061907.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 price_action_seasonal_filter_bonds
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_price_action_seasonal_filter_bonds_20260422_042514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 one_simple_momentum_4_etfs
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_one_simple_momentum_4_etfs_20260422_041814.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 nr7_enhanced
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_nr7_enhanced_20260422_031526.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 moving_average_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_moving_average_crossover_20260422_033024.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 mae_mfe_analysis
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_mae_mfe_analysis_20260422_041440.json`
- Results:  Green=0 |  Yellow=0 |  Red=4 | Total=4

## [2026-04-22] pipeline | 策略复现 macd_hook_gold_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_strategy_20260422_062912.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 macd_hook_gold
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_hook_gold_20260420_171931.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: GLD | Sharpe=1.223 | Trades=33 | MaxDD=-135.25% | Annual=207.83%
- Optimal params: {"fast_period": 15, "slow_period": 19, "signal_period": 10, "hull_period": 10, "fixed_size": 70, "bullish_days": 5, "max_holding_days": 7, "stop_loss_pct": 3.69}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev_20260416
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260416_20260416_064027.json`
- Results:  Green=1 |  Yellow=1 |  Red=0 | Total=2
- Best: QQQ | Sharpe=1.038 | Trades=92 | MaxDD=-40.25% | Annual=38.79%
- Optimal params: {"decline_days": 3, "signal_period": 12, "slow_period": 34}

## [2026-04-22] pipeline | 策略复现 macd_histogram_rev
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_rev_20260416_073639.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-22] pipeline | 策略复现 macd_histogram_auto_test
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_histogram_auto_test_20260417_154346.json`
- Results:  Green=0 |  Yellow=1 |  Red=0 | Total=1

## [2026-04-22] pipeline | 策略复现 macd_crossover
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_macd_crossover_20260422_031201.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 end_of_month_strategy_20260420
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_end_of_month_strategy_20260420_20260420_140544.json`
- Results:  Green=1 |  Yellow=0 |  Red=0 | Total=1
- Best: SPY | Sharpe=1.029 | Trades=137 | MaxDD=-90.70% | Annual=71.59%
- Optimal params: {"target_pct": 0.009399999999999999, "fixed_size": 35}

## [2026-04-22] pipeline | 策略复现 donchian_channel_breakout
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_donchian_channel_breakout_20260422_035102.json`
- Results:  Green=0 |  Yellow=0 |  Red=2 | Total=2

## [2026-04-22] pipeline | 策略复现 death_cross
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_death_cross_20260422_035514.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 consecutive_down_days_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_strategy_20260422_042101.json`
- Results:  Green=0 |  Yellow=0 |  Red=3 | Total=3

## [2026-04-22] pipeline | 策略复现 consecutive_down_days
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_consecutive_down_days_20260419_065041.json`
- Results:  Green=11 |  Yellow=0 |  Red=7 | Total=18
- Best: SPY | Sharpe=1.762 | Trades=174 | MaxDD=-2.25% | Annual=6.78%
- Optimal params: {"decline_days": 3, "trend_ma_period": 90, "max_hold_days": 5, "rsi_exit_threshold": 25, "fixed_size": 15}

## [2026-04-22] pipeline | 策略复现 commodity_skewness_premium
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_commodity_skewness_premium_20260422_042318.json`
- Results:  Green=0 |  Yellow=0 |  Red=8 | Total=8

## [2026-04-22] pipeline | 策略复现 combined_candlestick_strategy
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_combined_candlestick_strategy_20260422_041242.json`
- Results:  Green=0 |  Yellow=0 |  Red=0 | Total=0

## [2026-04-22] pipeline | 策略复现 backtested_bollinger_bands
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_backtested_bollinger_bands_20260422_033235.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1

## [2026-04-22] pipeline | 策略复现 rsi_2
- Action: `cta-strategy-factory` auto pipeline (build → run → evaluate)
- Eval file: `eval_rsi_2_20260422_062303.json`
- Results:  Green=0 |  Yellow=0 |  Red=1 | Total=1
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

## [2026-04-24] auto-ingest | Substack 文章批量导入
- 扫描: 105 篇
- 导入: 1 篇
- 跳过重复: 104 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-24] auto-ingest | Substack 文章批量导入
- 扫描: 106 篇
- 导入: 1 篇
- 跳过重复: 105 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-25] auto-ingest | Substack 文章批量导入
- 扫描: 3 篇
- 导入: 1 篇
- 跳过重复: 2 篇
- 跳过 Paywall: 0 篇
- 通知: 1 篇

## [2026-04-25] auto-ingest | Substack 文章批量导入
- 扫描: 4 篇
- 导入: 1 篇
- 跳过重复: 3 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-25] auto-ingest | Substack 文章批量导入
- 扫描: 5 篇
- 导入: 1 篇
- 跳过重复: 4 篇
- 跳过 Paywall: 0 篇
- 通知: 1 篇

## [2026-04-25] auto-ingest | Substack 文章批量导入
- 扫描: 6 篇
- 导入: 1 篇
- 跳过重复: 5 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## 2026-04-25 09:13 - Substack 批量导入

- 从 Substack Strategy Tracker 批量导入文章到 wiki/sources/
- 成功导入: 920 篇
- 跳过(已存在): 388 篇
- 涉及订阅源: Quantified Strategies, QuantSeeker, Algomatic Trading, TradeQuantiX, Delphic Alpha, TradingRiot


## 2026-04-25 08:35 - 反转策略全量分类与汇编

- 从 1701 篇 Substack 文章中自动识别出 **1043 篇反转策略** (61.3%)
- 按八大类别系统分类：
  1. 指标型均值回归 (346篇) — RSI、Williams R、Connors系列
  2. 季节性均值回归 (190篇) — Turnaround Tuesday、月末效应
  3. 隔夜/日内均值回归 (131篇) — 5日低点隔夜、开盘区间
  4. 价格行为型均值回归 (87篇) — IBS、NR7、布林带
  5. 连续下跌/极端事件反弹 (66篇) — 恐慌后反弹
  6. 形态反转 (48篇) — 十字星、双顶双底
  7. 统计套利/配对交易 (80篇) — 金银比、SPY/TLT
  8. 资产配置轮动 (95篇) — Dual Momentum、ETF轮动
- 生成汇编文档: wiki/syntheses/reversal-strategies-compendium.md
- 建立复现优先级矩阵: P0(季节性+隔夜) > P1(指标型+价格行为) > P2(极端事件+形态) > P3(配对+轮动)

## [2026-04-25] ingest | NR7 Narrow Range Breakout 策略复现报告
- 来源: Quantified Strategies Substack
- 新增: wiki/sources/nr7-breakout-reproduction.md | NR7窄幅突破策略
- SPY Sharpe=1.288, 最大回撤仅0.52%, Green 🟢
- QQQ Yellow (Sharpe=0.902), 加密货币4品种全Red
- 结论: 策略适合股票指数，不适合数字货币
- 更新: index.md (修正旧条目格式+替换为准确指标值)

## [2026-04-25] synthesis | 反转策略深度分析 — Karpathy 视角

- 新文件: wiki/syntheses/reversal-deep-analysis-karpathy.md (17,150 chars)
- 分析框架: Karpathy 式"什么在说谎，什么在赚钱"
- 核心发现：
  - ~13 个策略 × 多品种 ≈ 200 次回测后，仅 Consecutive Down Days, MACD Histogram, RSI-2 三种在默认参数下有真实 edge
  - 过拟合税估算: 回测 Sharpe 1.7 → 实盘期望 Sharpe 0.4-0.6（折扣 ~75%）
  - GLD 结构性偏倚: GLD 在 100% 的反转策略上有弱 edge — 这是 GLD 特质，非策略能力
  - 推荐实盘组合: Consecutive Down Days(SPY) + MACD Histogram(QQQ) + ETF MR Mini-Portfolio
- 识别三大自欺欺人陷阱: "Sharp 1.7 但 MaxDD 2%"综合征、OAT 76% 过拟合税、GLD 幻觉
- 更新: index.md (合成页面列表添加 reversal-deep-analysis-karpathy)


## [2026-04-26] auto-ingest | Substack 文章批量导入
- 扫描: 503 篇
- 导入: 1 篇
- 跳过重复: 502 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-26] ingest | Larry Connors %B Strategy
- 新增: wiki/sources/2026-04-25_connors-percent-b-strategy.md
- 更新: index.md

## [2026-04-26] ingest + repro | Larry Connors %B Strategy
- 新增: wiki/sources/2026-04-25_connors-percent-b-strategy.md
- 复现: strategy_factory SPY 默认参数回测完成 (Sharpe 0.47, 72 trades)
- 更新: index.md

\n## [2026-04-26] repro | Connors %B Strategy — 完整6步流程
- 复现: strategy_factory 完整流程（SPY 0.84/30, GLD 0.82/64, IWM 0.88/54, DIA 0.91/26, QQQ 0.99/11）
- 修复: 3个已知Bug（参数名/N[-1]/percent_b未定义）
- 验证: evaluate 4 Yellow / 1 Red, wiki sync 自动完成
- 更新: wiki/sources/2026-04-25_connors-percent-b-strategy.md

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 505 篇
- 导入: 1 篇
- 跳过重复: 504 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 58 篇
- 导入: 1 篇
- 跳过重复: 57 篇
- 跳过 Paywall: 0 篇
- 通知: 1 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 506 篇
- 导入: 1 篇
- 跳过重复: 505 篇
- 跳过 Paywall: 0 篇
- 通知: 1 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 1 篇
- 导入: 1 篇
- 跳过重复: 0 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 2 篇
- 导入: 1 篇
- 跳过重复: 1 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 3 篇
- 导入: 1 篇
- 跳过重复: 2 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 4 篇
- 导入: 1 篇
- 跳过重复: 3 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-27] auto-ingest | Substack 文章批量导入
- 扫描: 5 篇
- 导入: 1 篇
- 跳过重复: 4 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇

## [2026-04-29] auto-ingest | Substack 文章批量导入
- 扫描: 510 篇
- 导入: 1 篇
- 跳过重复: 509 篇
- 跳过 Paywall: 0 篇
- 通知: 1 篇

## [2026-04-30] auto-ingest | Substack 文章批量导入
- 新增 source: [[2026-04-30_Martingale-Strategy-for-Stocks]] — Martingale 风险教育
- 更新 source: [[2026-04-30_Martingale-Strategy-for-Stocks]] — 从空壳 preview-only 补全为完整分析

## [2026-05-01] fix | 修正 RSI 策略复现档案错误
- **修正**: `wiki/syntheses/rsi2mr-cn-futures-batch-2026-04-30.md`
  - 策略名称: RSI2_MR → **RSI Mean Reversion**（实际跑的是 `RsiMeanReversionStrategy`，非 Connor RSI-2）
  - 别名: RSI2_MR → **RSI_Mean_Reversion**
  - tag: strategy/RSI2-MR → **strategy/RSI-Mean-Reversion**
- **更新**: `wiki/sources/strategy-repro-rsi2-did-you-miss.md`
  - 新增扩展测试章节: 国内期货 AU888 + GLD 再验证 (2026-04-30)
  - AU888: RED, Sharpe=0.23, 16笔交易, 回撤-9.3%
  - GLD 再验证: YELLOW, Sharpe=0.72, 15笔交易（vs 上次 Sharpe=1.48）
  - 更新评级汇总: Green=2 | Yellow=2 | Red=2 | Total=6
- **更新**: `index.md` — RSI2_MR CN Futures → **RSI Mean Reversion CN Futures**

## [2026-04-30] ingest | Substack 积压文章补录
- 新增 source: [[2026-04-27_RSI-30-50-Strategy-for-Beginners]] — RSI 30-50 回调买入策略 (concrete_score: 85)
- 新增 source: [[2026-04-27_Trend-Following-Strategy-for-SP500]] — S&P 500 趋势跟踪 (concrete_score: 40, 付费墙遮挡)
- 新增 source: [[2026-04-27_Larry-Connors-pctB-Strategy]] — Larry Connors %B 均值回归 (concrete_score: 75)
- 新增 source: [[2026-04-29_Ken-Griffin-Trading-Strategy]] — Ken Griffin/Citadel 系统分析 (concrete_score: 10, 非策略)
- 新增 raw: quantifiedstrategies-2026-04-27-RSI-30-50-Strategy-for-Beginners.md
- 新增 raw: quantifiedstrategies-2026-04-27-A-Trend-Following-Strategy-for-the-S&P-500.md
- 新增 raw: quantifiedstrategies-2026-04-27-Larry-Connors-pctB-Strategy.md
- 新增 raw: quantifiedstrategies-2026-04-29-Ken-Griffin-Trading-Strategy-Explained.md
- 更新 index.md: 新增 5 条来源记录
- 修复: Substack tracker 自动同步机制（见下方）
- 扫描: 511 篇
- 导入: 1 篇
- 跳过重复: 510 篇
- 跳过 Paywall: 0 篇
- 通知: 0 篇
