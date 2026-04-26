---
id: weekly-summary-2026-04-26
title: "周度策略汇总报告 (2026-04-19 ~ 2026-04-26)"
date: "2026-04-26"
tags:
  - weekly-summary
  - synthesis
---

# 📊 周度策略汇总报告 (2026-04-19 ~ 2026-04-26)

> 自动生成于 2026-04-26 | 数据来源: llm-wiki 知识库

---

## 一、本周统计概览

| 指标 | 数量 |
|------|------|
| 新入库文章 | **419** 篇 |
| 新增策略配置 (.yaml) | **2** 个 |
| 新增主题报告 (.md) | **7** 份 |
| 可复现策略文章 | **281** 篇 |

---

## 二、本周入库文章列表

### 2.1 按标签分布

| 标签 | 数量 | 说明 |
|------|------|------|
| #article | 397 | 文章剪藏 |
| #substack | 397 | Substack来源 |
| #strategy | 281 | 策略相关 |
| #backtest | 115 | 含回测数据 |
| #equities | 51 | 股票策略 |
| #mean | 43 | 均值回归 |
| #intraday | 41 | 日内策略 |
| #trend | 36 | 趋势策略 |
| #bonds | 21 | 债券策略 |
| #seasonality | 20 | 季节性策略 |

### 2.2 本周重点文章（Top 20）

| # | 文章标题 | 标签 | Concrete |
|---|---------|------|----------|
| 1 | CL 跨市场套利深度分析报告 | #arbitrage #cross #funding | N/A |
| 2 | Consecutive Down Days Strategy | #article #substack #strategy | N/A |
| 3 | Price Action and Seasonal Filter Strategy for Bond... | #strategy #trading | N/A |
| 4 | Is The Death Cross The Kiss of Death? | #strategy #trading | N/A |
| 5 | Portfolio #7: The Ultimate Gold Portfolio + Annive... | #7 #strategy #trading | N/A |
| 6 | Pairs Trading in the Metals Complex: A Reality Che... | #strategy #trading | N/A |
| 7 | # 一句话摘要 | #strategy #trading | N/A |
| 8 | Bollinger Band Squeeze Trading Strategy | - | N/A |
| 9 | Session High Retest: 量化日内策略（10 期货市场，17 年数据） | #1 | N/A |
| 10 | From the Lab: A Counter Trend ES Model That Buys P... | #counter #ES #intraday | N/A |
| 11 | Last Chance To Lock In $99 For Life | - | N/A |
| 12 | Bitcoin Momentum Strategy | - | N/A |
| 13 | Q1 2026: TQX Portfolio Performance Review | - | N/A |
| 14 | ETF Mean Reversion Methods: Four Systems Built for... | - | N/A |
| 15 | Why Simplicity Beats Complexity in Trading System ... | - | N/A |
| 16 | Robustness Testing Methods: A Complete Guide for S... | - | N/A |
| 17 | Choppiness Index Trading Strategy | #article #substack #strategy | N/A |
| 18 | Portfolio #7: The Ultimate Gold Portfolio + Annive... | #7 #7 #article | N/A |
| 19 | How Correlation Between Strategies Affects Your Po... | #article #substack #strategy | N/A |
| 20 | Portfolio #7: The Ultimate Gold Portfolio + Annive... | #7 #7 #article | N/A |

---

## 三、🔥 可复现策略推荐（Top 5）

基于规则明确性、Concrete评分和复现难度排序：

### 1. **Turn of Month（月末效应）**
- **来源**: QuantifiedStrategies
- **Concrete评分**: 9.0/10
- **推荐理由**: 纯日历驱动，零参数，历史Sharpe > 1.0，复现难度极低
- **标签**: #seasonality #calendar

### 2. **IBS Indicator Strategy（内部柱强度）**
- **来源**: QuantifiedStrategies
- **Concrete评分**: 8.5/10
- **推荐理由**: 规则极简：IBS=(close-low)/(high-low)，IBS<0.25买入，XLP预期Sharpe 0.5-0.8
- **标签**: #mean-reversion #price-action

### 3. **5-Day Low Overnight（5日低隔夜策略）**
- **来源**: QuantifiedStrategies
- **Concrete评分**: 8.0/10
- **推荐理由**: 收盘价<过去5日最低即买入隔夜，与已有5DLR共享90%代码
- **标签**: #overnight #mean-reversion

### 4. **Williams %R Trading Strategy**
- **来源**: QuantifiedStrategies
- **Concrete评分**: 7.5/10
- **推荐理由**: 新指标族（非RSI/Stoch变体），GLD预期Sharpe 0.8-1.2
- **标签**: #indicator #mean-reversion

### 5. **Session High Retest（日内策略）**
- **来源**: Delphic Alpha
- **Concrete评分**: 7.0/10
- **推荐理由**: 10期货市场17年数据验证，已生成.yaml配置，需vnpy对接
- **标签**: #intraday #futures #session-high

---

## 四、📈 主题分布变化

### 4.1 本周新增主题报告

- `mean-reversion-strategies-compendium.md`
- `strategy-mean-reversion-analysis.md`
- `reversal-strategies-compendium.md`
- `mean-reversion-strategies-comparison.md`
- `reversal-deep-analysis-karpathy.md`
- `reversal-strategy-landscape.md`
- `reversal-strategy-pipeline-2026-04-26.md`

### 4.2 本周新增策略配置

- `ETF_Mean_Reversion_Methods__Mean_Reversi.yaml`
- `Session_High_Retest__A_Quantitative_Intr.yaml`

### 4.3 策略类型分布（本周新文章）

| 策略类型 | 数量 | 占比 |
|----------|------|------|
| 指标型均值回归 | 43 | 10.3% |
| 季节性/日历效应 | 20 | 4.8% |
| 日内/隔夜策略 | 41 | 9.8% |
| 趋势跟踪 | 36 | 8.6% |
| 其他 | 279 | - |

---

## 五、🎯 下周行动建议

1. **立即复现**: Turn of Month + IBS Strategy（P0优先级，预计1-2天完成）
2. **扩展回测**: Williams %R → GLD batch（验证新指标族效果）
3. **对接开发**: Session High Retest 日内策略 vnpy 实现
4. **组合验证**: 将最好的3-5个反转策略合并为mini-portfolio

---

## 六、相关链接

- [[reversal-strategies-compendium]] — 反转策略汇编（1043篇分类）
- [[reversal-strategy-pipeline-2026-04-26]] — 复现优先级清单
- [[mean-reversion-strategies-comparison]] — 5个经典均值回归策略对比
- [[mean-reversion-strategies-compendium]] — 已复现策略结果汇总

---

*Generated: 2026-04-26 | 基于 llm-wiki 419 篇本周入库文章 + 2 个策略配置 + 7 份主题报告*
