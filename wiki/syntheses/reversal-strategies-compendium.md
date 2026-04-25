---
id: reversal-strategies-compendium
title: "反转策略汇编 — 可复现策略清单"
date: 2026-04-25
source: Substack Strategy Tracker
status: catalogued
---

# 反转策略汇编 — 可复现策略清单

> 从 1701 篇 Substack 策略文章中识别出 **1043 篇反转策略**（61.3%），按八大类别整理。本文档用于指导后续策略复现优先级。

---

## 📊 总体统计

| 指标 | 数值 |
|------|------|
| 总文章数 | 1701 篇 |
| 反转策略 | **1043 篇 (61.3%)** |
| 趋势/其他 | 658 篇 (38.7%) |

---

## 🎯 八大反转策略类别

### 1. 指标型均值回归 (346 篇, 33.2%)

**核心逻辑**: 基于RSI、Williams %R、Stochastic等超买超卖指标，在极端读数时反向交易。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| RSI 2 Strategy (Larry Connors) | Quantified Strategies | rsi, 2-period, connors | [[2026-04-25-RSI-2-Strategy-Explained-Larry-Connors-2-Period-RSI-Trading-Rules]] |
| Williams R Trading Strategy | Quantified Strategies | williams %r, mean reversion | [[2026-04-25-Williams-R-Trading-Strategy-81-Win-Rate]] |
| Stochastic Trading Strategies | Quantified Strategies | stochastic, oversold | [[2026-04-25-Stochastic-Trading-Strategies-Backtest-Indicator-Settings-Rules-and-example]] |
| Larry Connors Double Seven | Quantified Strategies | double seven, connors | [[2026-04-25-Larry-Connors-Double-Seven-Trading-Strategy-Double-7-Trading-System]] |
| Larry Connors R3 Strategy | Quantified Strategies | r3, connors | [[2026-04-25-Larry-Connors-R3-Strategy-It-Still-Works]] |
| Larry Connors b Strategy | Quantified Strategies | bollinger, connors | [[2026-04-25-Larry-Connors-b-Strategy-Bollinger-Band]] |
| TRIN Arms Index | Quantified Strategies | trin, arms index | [[2026-04-25-TRIN-Arms-Index-Trading-Strategy-What-is-it-Backtest]] |
| CCI Trading Strategy | Quantified Strategies | cci, commodity channel | [[2026-04-25-CCI-Trading-Strategy-What-is-it-Backtest-Indicator-Settings-Rules-and-example]] |
| Chande Momentum Oscillator | Quantified Strategies | chande, momentum | [[2026-04-25-Chande-Momentum-Oscillator-Trading-Strategy-Setup-Rules-Python-Backtest]] |
| Triple RSI Strategy | Quantified Strategies | triple rsi, 90% win rate | [[2026-04-25-Triple-RSI-Trading-Strategy-Elevate-Your-Win-Rate-to-90-Advanced-Insights]] |

**复现优先级**: ⭐⭐⭐⭐⭐ (指标明确，规则清晰)

---

### 2. 季节性均值回归 (190 篇, 18.2%)

**核心逻辑**: 基于日历效应（如Turnaround Tuesday、月末效应、节假日效应）的定时交易。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| Turnaround Tuesday | Quantified Strategies | tuesday, turnaround | [[2026-04-25-Turnaround-Tuesday-Strategy-Backtest]] |
| Turn of Month Strategy | Quantified Strategies | turn of month, end of month | [[2026-04-25-Turn-of-The-Month-Strategy]] |
| Options Expiration Week | Quantified Strategies | opex, options expiration | [[2026-04-25-The-Options-Expiration-Week-Effect]] |
| Holiday Effect | Quantified Strategies | holiday, seasonal | [[2026-04-25-The-Holiday-Effect-in-Stock-Markets-Explained-Strategies-and-Seasonal-Insights]] |
| Santa Claus Rally | Quantified Strategies | santa claus, year end | [[2026-04-25-The-End-Of-The-Year-Rally-In-Stocks-Santa-Claus-RallyEffect-Strategy]] |
| Easter Trading | Quantified Strategies | easter, holiday | [[2026-04-25-Easter-Trading-Strategy-Does-the-Stock-Market-Rally-Before-the-Holiday]] |
| Monday Tuesday Trade | Quantified Strategies | monday, tuesday, nasdaq | [[2026-04-25-MondayTuesday-Trade-In-Nasdaq-Update-System-Enhanced-Trading-Strategy]] |
| OPEX Week of September | Quantified Strategies | opex, september | [[2026-04-25-Performance-of-the-OPEX-Week-of-September]] |

**复现优先级**: ⭐⭐⭐⭐⭐ (规则极简，无参数优化)

---

### 3. 隔夜/日内均值回归 (131 篇, 12.6%)

**核心逻辑**: 利用隔夜跳空或日内波动的均值回归特性。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| 5 Day Low Overnight | Quantified Strategies | 5 day low, overnight | [[2026-04-25-The-5-Day-Low-Overnight-Trading-Strategy-ExplainedSP-500-Overnight]] |
| 3 Days Down Overnight | Quantified Strategies | 3 days down, overnight | [[2026-04-25-3-Days-Down-Overnight-Trading-Strategy-SP-500-Nasdaq-Rules-Performance-Analysis]] |
| The Overnight Edge | Quantified Strategies | overnight, edge | [[2026-04-25-The-Overnight-Edge---Is-It-Still-Working]] |
| Opening Range Breakout | Quantified Strategies | orb, opening range | [[2026-04-25-OPENING-RANGE-BREAKOUT-STRATEGY-ORB-FOR-DAY-TRADING-5-MINUTE-BACKTEST-AND-SYSTEM]] |
| Session High Retest | Delphic Alpha | session high, retest | [[2026-04-22-session-high-retest-intraday-strategy]] |
| Intraday Trading Strategies | Quantified Strategies | intraday, day trading | [[2026-04-25-Intraday-Trading-Strategies-Backtest-Results-and-Practical-Examples]] |
| Day Trading Price Action | Quantified Strategies | price action, day trading | [[2026-04-25-Day-Trading-Price-Action-Strategy-Overview-and-Backtest]] |

**复现优先级**: ⭐⭐⭐⭐⭐ (高Sharpe，低回撤)

---

### 4. 价格行为型均值回归 (87 篇, 8.3%)

**核心逻辑**: 基于价格形态（IBS、布林带、NR7等）的均值回归。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| IBS Indicator | Quantified Strategies | ibs, internal bar strength | [[2026-04-25-The-Internal-Bar-Strength-IBS-Indicator---Trading-Strategies-Rules]] |
| NR7 Trading Strategy | Quantified Strategies | nr7, narrow range | [[2026-04-25-NR7-Trading-Strategy-The-Narrow-Range-7-Enhanced-and-Improved-Version]] |
| Bollinger Band Squeeze | Quantified Strategies | bollinger, squeeze | [[2026-04-25-Bollinger-Band-Squeeze-Strategy-Explained-Backtest-And-Performance]] |
| Outside Day Bar | Quantified Strategies | outside day, bar | [[2026-04-25-Outside-Day-Bar-Trading-Strategy-Rules-Settings-Performance-and-Backtest-Insight]] |
| Keltner Channel | Quantified Strategies | keltner, channel | [[2026-04-25-Keltner-Channel-Strategy]] |

**复现优先级**: ⭐⭐⭐⭐ (规则清晰，参数少)

---

### 5. 连续下跌/极端事件反弹 (66 篇, 6.3%)

**核心逻辑**: 在极端下跌或恐慌事件后做反弹。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| Consecutive Down Days | Quantified Strategies | consecutive down, decline | [[2026-04-18-consecutive-down-days-strategy]] |
| What Happens When Oversold | Quantified Strategies | oversold, extreme | [[2026-04-25-What-Happens-When-Stock-Markets-Are-Oversold-Historical-Analysis]] |
| What Happens After Big Fall | Quantified Strategies | big fall, crash | [[2026-04-25-What-Happens-After-an-Extraordinary-Big-Fall-in-the-SP-500-Volatility-Trading-St]] |
| Rubber Band Strategy | Quantified Strategies | rubber band, extreme | [[2026-04-25-The-Rubber-Band-Strategy]] |
| VIX Spike Trading | Quantified Strategies | vix, spike, fear | [[2026-04-25-The-VIX-Indicator-A-Simple-Way-to-Measure-Fear-in-the-Market]] |

**复现优先级**: ⭐⭐⭐⭐ (事件驱动，频率低但胜率高)

---

### 6. 形态反转 (48 篇, 4.6%)

**核心逻辑**: 基于经典K线形态（十字星、吞没、双顶双底等）的反转交易。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| Doji Candlestick Strategy | Quantified Strategies | doji, candlestick | [[2026-04-25-Doji-Candlestick-Strategy-for-Stocks-Backtested-Rules-and-Result]] |
| 3 Bullish Candlestick Patterns | Quantified Strategies | candlestick, bullish | [[2026-04-25-3-Bullish-Candlestick-Patterns-That-Work-Backtesting-and-Performance-Analysis]] |
| Double Top Chart Pattern | Quantified Strategies | double top, pattern | [[2026-04-25-Double-Top-Chart-Pattern-Trading-Strategy-Backtest-Example-Analysis]] |
| Triple Top Chart Pattern | Quantified Strategies | triple top, pattern | [[2026-04-25-Triple-Top-Chart-Pattern-Trading-Strategy-Explained-Does-It-Work-Backtest-Analys]] |
| 123 Pattern Reversal | Quantified Strategies | 123 pattern, reversal | [[2026-04-25-123-Pattern-Reversal-Trading-Strategy-Setup-and-Backtest]] |
| Reversal Day Strategy | Quantified Strategies | reversal day, bullish | [[2026-04-25-Reversal-Day-Strategy-Backtest-Does-It-Work-Bullish-Reversal-Market-Turnaround]] |
| Lower Highs Lower Lows | Quantified Strategies | lower highs, pattern | [[2026-04-25-Lower-Highs-And-Lower-Lows-Pattern-Trading-Strategy-Setup-and-Backtest-Analysis]] |

**复现优先级**: ⭐⭐⭐ (形态识别有主观性，需量化定义)

---

### 7. 统计套利/配对交易 (80 篇, 7.7%)

**核心逻辑**: 基于统计关系的配对交易，如金银比、SPY/TLT配对。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| Gold Silver Ratio | Quantified Strategies | gold silver, ratio | [[2026-04-25-Gold-Silver-Chart-Ratio-Strategy-Rules-and-Backtest]] |
| Pairs Trading SPY TLT | Quantified Strategies | pairs trading, spy tlt | [[2026-04-25-A-PAIR-TRADE-IN-SPY-AND-TLT-TESTING-PAIRS-TRADING-STRATEGIES-IN-BONDS-AND-SP500]] |
| Lumber Gold Ratio | Quantified Strategies | lumber, gold, ratio | [[2026-04-25-LumberGold-Ratio-Trading-Strategy-For-Stocks-And-Bonds-Rules-Backtest-Performanc]] |
| QQQ TLT Ratio | Quantified Strategies | qqq, tlt, ratio | [[2026-04-25-QQQTLT-Ratio---Does-It-Work]] |

**复现优先级**: ⭐⭐⭐⭐ (对冲特性，低相关)

---

### 8. 资产配置轮动 (95 篇, 9.1%)

**核心逻辑**: 基于相对强弱在资产间轮动，部分含均值回归特征。

| 策略名称 | 来源 | 关键词 | 文件 |
|---------|------|--------|------|
| Dual Momentum (Gary Antonacci) | Quantified Strategies | dual momentum, antonacci | [[2026-04-25-Dual-Momentum-Trading-Strategy-Gary-Antonacci-Rules-Setup-Backtest-Analysis]] |
| Meb Faber Trend Following | Quantified Strategies | meb faber, trend | [[2026-04-25-Trend-Following-Strategy-in-SP-500-Meb-Faber-and-Paul-Tudor-Jones]] |
| SPY GLD Rotation | Quantified Strategies | spy, gld, rotation | [[2026-04-25-Rotation-Strategy-In-SP-500-And-Gold-SPY-GLD]] |
| Monthly ETF Rotation | Quantified Strategies | etf, rotation, monthly | [[2026-04-25-Monthly-ETF-Rotation-Strategy]] |
| Weekly SPY XLU Rotation | Quantified Strategies | spy, xlu, utilities | [[2026-04-25-Weekly-Rotating-System-Between-SP-500-And-Utilities-SPY-And-XLU]] |

**复现优先级**: ⭐⭐⭐ (趋势跟踪为主，部分含均值回归)

---

## 🔥 复现优先级矩阵

| 优先级 | 类别 | 代表策略 | 理由 |
|--------|------|---------|------|
| **P0** | 季节性 | Turnaround Tuesday, Turn of Month | 规则极简，无参数，高胜率 |
| **P0** | 隔夜 | 5 Day Low Overnight | 高Sharpe，低回撤 |
| **P1** | 指标型 | RSI 2, Williams R, IBS | 指标明确，规则清晰 |
| **P1** | 价格行为 | NR7, Bollinger Squeeze | 形态量化容易 |
| **P2** | 极端事件 | Consecutive Down Days | 事件驱动，频率低 |
| **P2** | 形态 | Doji, Double Top | 需主观判断量化 |
| **P3** | 配对交易 | Gold/Silver Ratio | 需两个品种数据 |
| **P3** | 轮动 | Dual Momentum | 偏趋势跟踪 |

---

## 📝 复现检查清单

复现前确认以下信息已提取：

- [ ] **入场规则**: 明确的买入条件（指标阈值/形态识别/日期条件）
- [ ] **出场规则**: 明确的卖出条件（持有周期/指标反转/止损）
- [ ] **标的资产**: 具体交易品种（SPY/QQQ/GLD/TLT等）
- [ ] **时间框架**: 日线/周线/日内
- [ ] **回测区间**: 原文提供的回测时间段
- [ ] **过滤条件**: 趋势过滤器/市场环境要求
- [ ] **仓位管理**: 固定金额/百分比/波动率调整

---

## 🔗 相关链接

- [[mean-reversion]] — 均值回归概念
- [[trend-filter]] — 趋势过滤器概念
- [[strategy-repro-consecutive-down-days]] — 已复现策略示例
- [[strategy-repro-end-of-month-spy]] — 已复现策略示例

---

*Generated: 2026-04-25 | Source: Substack Strategy Tracker | Total Articles: 1701 | Reversal Strategies: 1043*
