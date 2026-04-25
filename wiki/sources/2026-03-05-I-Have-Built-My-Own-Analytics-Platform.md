# I Have Built My Own Analytics Platform

**Source**: [[2026-03-05-I-Have-Built-My-Own-Analytics-Platform]] | [TradingRiot]()
**Date**: 2026-03-05
**Tags**: #article #substack

## One-Sentence Summary

> Substack article about trading strategies.

## Key Insights

1. **原文来源**: TradingRiot

## Full Content

---
title: "I Have Built My Own Analytics Platform"
author: "Adam (TradingRiot)"
url: "https://blog.tradingriot.com/p/i-have-built-my-own-analytics-platform"
date: "2026-03-05"
topics: ["analytics", "multi-asset", "futures", "crypto", "equities", "bonds", "forex", "options", "data-platform", "risk-premium"]
source: "TradingRiot Substack"
---

# I Have Built My Own Analytics Platform

> Multi-asset analytics across 1,000+ futures, crypto, stocks, and ETFs with deep historical data.

## 作者背景与动机

Adam 的交易路径与大多数人相似：
- 从日内交易起步（看 DOM、盯盘 12 小时）
- 逐渐转向系统化策略构建
- 目标：建立一个**多资产、多策略组合**，收割不同风险溢价（risk premiums）

已开发的策略类型：
- 动量/均值回归策略（使用 dark pool 成交量、期权 skew、crypto 衍生品数据、期货 COT 持仓）
- 方差风险溢价（variance risk premium）：卖出定价过高的期权合约
- 财报事件波动率交易
- 日历价差表达远期波动率观点

**痛点**：订阅了多个平台，每月花费数千美元，仍缺少想要的功能。于是决定自建平台。

---

## 平台概览

**TradingRiot Analytics**（tradingriot.com）
- 覆盖 1,000+ 期货、加密货币、股票、ETF
- 深度历史数据
- 一系列专有指标
- 免费账户可访问部分工具和数据
- Premium 解锁全部功能

---

## 一、加密货币 (Cryptocurrencies)

### 数据覆盖
- 150+ 币种
- 聚合 8 家中心化交易所数据
- 5 年历史数据

### 核心指标
1. **永续合约数据**：持仓量 (open interest)、资金费率 (funding rates)、清算量 (liquidations)
   - 附带 **Z-score 功能**：快速标记相对历史水平的极端持仓
2. **现货订单簿 Delta**：识别现货市场的供需力量
3. **期权数据**（BTC、ETH）：波动率与 skew 持仓
4. **综合市场情绪指标 (Composite Regime Indicator)**
   - 作者自有模型，综合衍生品数据衡量情绪
   - 用途：识别市场状态切换、历史极端恐惧/狂热

### 筛选器 (Screener)
- 每个资产类别都有专属筛选器
- 自动标记极端值、发现可交易标的

---

## 二、股票 (Equities)

### 数据覆盖
- 900+ 市场
- 10 年历史数据

### 核心指标
1. **IV 期限结构** (Implied Volatility Term Structure)
2. **波动率风险溢价** (Volatility Risk Premium)
3. **Skew**
4. **暗池活动** (Dark Pool Activity)
5. **财报表现历史**：12 个季度财报历史，含隐含波动率变动和准确性追踪
6. **新闻与公告流**

---

## 三、期货 (Futures)

### 数据覆盖
- 覆盖 CME、CBOT、COMEX、NYMEX、ICE、Eurex
- 从 2014 年起的历史数据

### 核心指标
1. **COT 报告数据** (Commitment of Traders)
   - 商业/非商业持仓分解
   - Z-score 标记极端值
2. **期限结构** (Term Structure)
   - Contango/Backwardation 可视化
3. **季节性分析** (Seasonality)
   - 多年月度表现统计
4. **波动率分析**

---

## 四、外汇 (Forex)

### 数据覆盖
- 主要货币对 + 新兴市场货币
- 历史数据回溯多年

### 核心指标
1. **CFTC COT 数据**：外汇期货持仓
2. **波动率指标**
3. **利差分析**

---

## 五、债券 (Bonds)

### 数据覆盖
- 美国国债、欧洲主权债、企业债
- 长期历史数据

### 核心指标
1. **收益率曲线** (Yield Curve)
2. **期限结构变化**
3. **与期货的跨市场分析**

---

## 六、期权 (Options)

### 数据覆盖
- 股票/ETF 期权
- 指数期权
- 期货期权

### 核心指标
1. **隐含波动率曲面** (IV Surface)
2. **Skew 分析**
3. **期限结构**
4. **波动率风险溢价计算**

---

## 平台技术架构（推测）

从描述推断：
- **后端**：Python 数据处理管道
- **数据源**：
  - 加密货币：8 家 CEX API（可能是 CCXT 聚合）
  - 股票/期权：可能是 Polygon、TradeAlert 或类似数据商
  - 期货：CME、ICE、Eurex 数据
  - COT/CFTC：政府公开数据
- **前端**：Web Dashboard（可能是 Streamlit、Dash 或 React）
- **数据库**：时序数据库或 PostgreSQL + 分区

---

## 可借鉴的理念

1. **数据整合优于单一数据源**：聚合多交易所/多平台数据，减少单点偏差
2. **Z-score 标准化**：所有指标都提供相对历史水平的 Z-score，便于快速识别极端
3. **从数据到信号**：不仅提供原始数据，还提炼为可操作的筛选器和信号
4. **跨资产类别统一框架**：同样的分析范式（持仓、波动率、期限结构）应用于不同市场
5. **自建平台的成本效益**：当订阅费用超过自建成本时，自建是更优选择

---

## 与现有基础设施的关联

| TradingRiot 功能 | 用户现有能力 |
|-----------------|-------------|
| 多交易所 Crypto 数据 | ✅ OKX/Binance/Hyperliquid 网关 |
| 期货数据 | ✅ IB Gateway + vnpy |
| 股票/ETF 数据 | ✅ IB Gateway + vnpy |
| COT 数据 | ⚠️ 需额外获取 |
| 暗池数据 | ❌ 未覆盖 |
| 期权数据 | ⚠️ IB 有，但未系统分析 |
| 综合情绪指标 | ❌ 需自建 |
| Z-score 筛选器 | ❌ 需自建 |

---

## 参考链接

- 平台地址：https://tradingriot.com
- 优惠码：ANALYTICS（首月 50% off）
- 原文：https://blog.tradingriot.com/p/i-have-built-my-own-analytics-platform


---

*Imported from Substack on 2026-04-25*
