---
title: "QuantInsti 可复现策略筛选报告"
date: "2026-04-27"
type: report
tags: [quantinsti, strategy-screening, reproducibility]
sources: [2026-04-27_quantinsti-blog-merge]
---

# QuantInsti 可复现策略筛选报告

**生成日期**: 2026-04-27 20:36
**数据来源**: QuantInsti Blog (blog.quantinsti.com)
**总策略文章**: 561 篇

## 筛选标准

可复现性评分基于以下维度:

| 维度 | 权重 | 说明 |
|------|------|------|
| 入场规则 | 1x | 明确的买入/做多条件 |
| 离场规则 | 1x | 明确的卖出/止损/止盈条件 |
| 具体参数 | 1x | 指标周期、阈值等数值参数 |
| 回测数据 | 1x | Sharpe、回撤、胜率等性能指标 |
| 代码示例 | +5 | 有 Python/R 代码实现 |
| 时间框架 | +2 | 明确日线/小时/分钟级别 |
| 概念文章惩罚 | -0.5x | Introduction/Basics/Overview 等 |
| 职业文章惩罚 | -1x | Career/Salary/Course 等 |

## 可复现性分级

| 级别 | 数量 | 分数范围 | 说明 |
|------|------|----------|------|
| 🟢 高可复现 | 33 | ≥15 | 规则完整，有代码/回测，可直接实现 |
| 🟡 中等可复现 | 120 | 8-14 | 有规则但缺少部分细节，需补充 |
| 🔴 低可复现 | 408 | <8 | 概念性/介绍性，缺乏具体规则 |

## 按策略类型分布（高可复现性）

| 策略类型 | 数量 | 代表策略 |
|----------|------|----------|
| Mean Reversion | 2 | RSI Indicator Formula and Calc, Mean Reversion Strategies Intr |
| Pairs Trading | 3 | Dynamic Selection of Pairs for, Kalman Filter Techniques And S, Cointegrated Pairs Trading Str |
| Ml Based | 3 | Optimal Portfolio Construction, Gold Price Prediction Using Ma, Machine Learning Strategy usin |
| Portfolio | 1 | Linear Discriminant Analysis F |
| Other | 24 | Turtle Trading In Python, Backtrader What it is How to I, Basic Operations On Stock Data |

## Top 33 高可复现策略清单

| # | 策略名称 | 分数 | 关键特征 |
|---|----------|------|----------|
| 1 | Turtle Trading In Python | 32.0 | 有代码, 有回测, 参数完整 |
| 2 | Backtrader What it is How to Install Str | 23.0 | 有代码, 有回测, 参数完整 |
| 3 | Basic Operations On Stock Data Using Pyt | 22.0 | 有代码, 参数完整 |
| 4 | Optimal Portfolio Construction Using Mac | 21.0 | 有代码, 有回测, 参数完整 |
| 5 | Quantitative Trading  Building Entry Ide | 21.0 | 参数完整 |
| 6 | Bias Variance Decomposition for Trading  | 20.5 | 有回测, 参数完整 |
| 7 | Dynamic Selection of Pairs for Statistic | 20.5 | 有代码, 有回测, 参数完整 |
| 8 | Futures Trading Explained | 20.5 | 参数完整 |
| 9 | Technical Indicators Use for Trading Lis | 20.0 | 有代码, 参数完整 |
| 10 | Linear Discriminant Analysis For Quantit | 19.5 | 有代码, 有回测 |
| 11 | Gold Price Prediction Using Machine Lear | 19.5 | 有回测, 参数完整 |
| 12 | Optimizing Exit Conditions Using a Varia | 19.0 | 有回测, 参数完整 |
| 13 | Impact of COVID 19 and Oil Price War on  | 19.0 | 有回测, 参数完整 |
| 14 | RSI Indicator Formula and Calculation Tr | 18.5 | 有代码, 有回测 |
| 15 | Directional Change in Trading Indicators | 18.5 | 有回测, 参数完整 |
| 16 | Autoregressive Drift Detection Method AD | 18.0 | 有代码, 有回测 |
| 17 | Dynamic Money Management | 18.0 | 有代码, 有回测 |
| 18 | Sharpe Ratio Explained Formula Calculati | 17.5 | 有回测, 参数完整 |
| 19 | Retrospective Simulation in Trading Test | 17.0 | 有代码, 有回测 |
| 20 | Cross Validation in Finance Purging Emba | 17.0 | 有回测 |
| 21 | Python Numpy Tutorial Installation Array | 17.0 | 有代码, 有回测 |
| 22 | Machine Learning Strategy using Blueshif | 16.5 | 有代码, 有回测 |
| 23 | Trading Index TRIN Formula Calculation S | 16.5 | 有回测, 参数完整 |
| 24 | Turning data into insights and building  | 16.0 | 有回测, 参数完整 |
| 25 | 10 ways your Trading Strategy can fail | 16.0 | 有回测, 参数完整 |
| 26 | Using Quadratic Discriminant Analysis To | 15.5 | 有代码, 有回测 |
| 27 | Kalman Filter Techniques And Statistical | 15.5 | 有回测, 参数完整 |
| 28 | Decision Trees | 15.5 | 有代码, 参数完整 |
| 29 | The Hidden Truths About Stop loss In Tra | 15.5 | 有回测 |
| 30 | Mean Reversion Strategies Introduction T | 15.0 | 规则明确 |
| 31 | Cointegrated Pairs Trading Strategy in I | 15.0 | 有代码, 有回测 |
| 32 | Algo Trading Stages Explained Simply | 15.0 | 有回测 |
| 33 | Shorting at High Algo Trading Strategy i | 15.0 | 参数完整 |

## 建议优先复现的策略（Top 10）

基于规则完整性 + 回测数据 + 代码可用性，建议优先复现以下策略:

1. **Turtle Trading In Python** (score: 32.0)
   - 入场规则: 13处 | 离场规则: 11处 | 参数: 11个 | 有回测数据 | 有代码示例
   - 文件: `2017-10-27-Turtle-Trading-In-Python.md`

2. **Backtrader What it is How to Install Strategies Trading and ** (score: 23.0)
   - 入场规则: 8处 | 离场规则: 4处 | 参数: 4个 | 有回测数据 | 有代码示例
   - 文件: `2022-05-09-Backtrader-What-it-is-How-to-Install-Strategies-Trading-and-.md`

3. **Basic Operations On Stock Data Using Python** (score: 22.0)
   - 入场规则: 4处 | 参数: 12个 | 有代码示例
   - 文件: `2017-09-14-Basic-Operations-On-Stock-Data-Using-Python.md`

4. **Optimal Portfolio Construction Using Machine Learning** (score: 21.0)
   - 入场规则: 21处 | 离场规则: 31处 | 参数: 4个 | 有回测数据 | 有代码示例
   - 文件: `2018-08-10-Optimal-Portfolio-Construction-Using-Machine-Learning.md`

5. **Quantitative Trading  Building Entry Ideas and Idea flow** (score: 21.0)
   - 入场规则: 29处 | 离场规则: 15处 | 参数: 5个
   - 文件: `2020-06-18-Quantitative-Trading--Building-Entry-Ideas-and-Idea-flow.md`

6. **Bias Variance Decomposition for Trading ML Pipeline with PCA** (score: 20.5)
   - 入场规则: 22处 | 离场规则: 6处 | 参数: 15个 | 有回测数据
   - 文件: `2025-05-13-Bias-Variance-Decomposition-for-Trading-ML-Pipeline-with-PCA.md`

7. **Dynamic Selection of Pairs for Statistical Arbitrage** (score: 20.5)
   - 入场规则: 31处 | 离场规则: 12处 | 参数: 6个 | 有回测数据 | 有代码示例
   - 文件: `2022-02-07-Dynamic-Selection-of-Pairs-for-Statistical-Arbitrage.md`

8. **Futures Trading Explained** (score: 20.5)
   - 入场规则: 25处 | 离场规则: 13处 | 参数: 8个
   - 文件: `2021-07-19-Futures-Trading-Explained.md`

9. **Technical Indicators Use for Trading List Trading Strategy** (score: 20.0)
   - 入场规则: 17处 | 参数: 8个 | 有代码示例
   - 文件: `2021-09-30-Technical-Indicators-Use-for-Trading-List-Trading-Strategy.md`

10. **Linear Discriminant Analysis For Quantitative Portfolio Mana** (score: 19.5)
   - 入场规则: 9处 | 离场规则: 7处 | 参数: 2个 | 有回测数据 | 有代码示例
   - 文件: `2018-07-27-Linear-Discriminant-Analysis-For-Quantitative-Portfolio-Mana.md`

## 自动化建议

1. **高可复现策略 (33篇)**: 可直接加入 strategy_factory 队列自动处理
2. **中等可复现策略 (120篇)**: 需人工补充参数后处理
3. **低可复现策略 (408篇)**: 作为概念参考，不适合直接复现

## 文件位置

- 原始文章: `~/llm-wiki/raw/articles/` (712篇)
- 筛选结果: `/tmp/quantinsti_reproducible_strategies.json`
- 本报告: `~/llm-wiki/wiki/concepts/quantinsti-reproducible-strategies.md`

*Generated on 2026-04-27*