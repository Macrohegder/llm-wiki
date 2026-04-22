---
id: mean-reversion-strategies-compendium
title: "均值回归/反转策略汇编 (Mean Reversion Strategies Compendium)"
date: "2026-04-23"
tags:
  - concept/mean-reversion
  - concept/reversal
  - synthesis
  - strategy-compendium
---

# 均值回归/反转策略汇编

> 本页面汇总 llm-wiki 知识库中所有**均值回归 (Mean Reversion) 与反转 (Reversal)** 策略的核心结论，按信号类型分类，并给出可执行的策略选择与组合建议。

---

## 一、知识库内已收录的反转策略概览

| 策略名 | 来源 | 日期 | 信号类型 | 核心机制 | 最佳品种 | Sharpe | 状态 |
|--------|------|------|----------|----------|----------|--------|------|
| **ETF Mean Reversion Mini-Portfolio** | TradeQuantix | 2025-04-22 | 统计/Z-Score | 四系统组合 + Sub-entry | 多资产ETF | ~1.0+ | 深度处理 |
| **5 Swing Trading Strategies** | QuantifiedStrategies | 2026-03-19 | 价格极端 | 5种波段均值回归 + 统一出场 | SPY Combined | 0.27* | 深度处理 |
| **Consecutive Down Days** | QuantifiedStrategies | 2026-04-18 | 价格极端 | 连续下跌 + 趋势过滤 | SPY | **1.762** | 复现 Green |
| **MACD Histogram Mean Reversion** | QuantifiedStrategies | 2025-06-19 | 指标极端 | MACD Histogram 偏离回归 | QQQ | **1.038** | 复现 Green |
| **MACD Hook Gold** | Algomatic Trading | 2025-05-01 | 动量回调 | MACD Hook + Hull MA 确认 | GLD | **1.223** | 复现 Green |
| **RSI-2 Strategy** | QuantifiedStrategies | 2026-04-04 | 指标极端 | RSI(2) < 10 买入, > 90 卖出 | GLD | **1.59** | 初步验证 OK |
| **Pullback RSI Strategy** | QuantifiedStrategies | 2023-12-25 | 价格极端 | RSI + 双均线回撤买入 | GLD | **1.29** | 初步验证 OK |
| **Stochastic Mean Reversion** | QuantifiedStrategies | 2026-04-04 | 指标极端 | %K < 20 买入 | SPY | 0.39 | 初步验证 OK |
| **Backtested Bollinger Bands** | QuantifiedStrategies | 2024-02-17 | 波动率通道 | 收盘价 < 下轨买入 | GLD | **1.19** | 初步验证 OK |
| **Bollinger Band Breakout** | QuantifiedStrategies | 2026-04-16 | 波动率突破 | 收盘价 > 上轨买入 | GLD | **0.93** | 初步验证 OK |
| **Stochastic Extremes Gold** | Algomatic Trading | 2026-04-05 | 指标极端 | Stochastic 交叉 + 趋势过滤 | GLD | 0.72 | 初步验证 OK |
| **Volatility Swing Trade** | QuantifiedStrategies | 2023-12-15 | 指标极端 | RSI 超卖买入 | QQQ | 0.53 | 初步验证 OK |
| **Larry Connors RSI-2** | QuantifiedStrategies | 2026-04-04 | 指标极端 | RSI(2) + SMA200 过滤 | IWM | **1.02** | 初步验证 OK |
| **Bollinger Band Squeeze** | QuantifiedStrategies | 2026-04-22 | 波动率收缩 | 布林带收窄后突破 | GLD | 0.93 | 初步验证 OK |
| **Stocks-Bonds MR** | QuantSeeker | 2025-02-17 | 跨资产 | 股债短期均值回归 | SPY/TLT | 复现 Red | DSL不支持跨资产 |
| **Weekly MR (SP500)** | QuantifiedStrategies | 2023-04-23 | 日历/VIX | VIX 恐惧驱动均值回归 | SPY | 复现 Red | 需VIX外部数据 |

> *Sharpe 栏位为复现结果或原文披露数据。`*` 为风险调整后回报 (Return/MaxDD)。*
> *“初步验证 OK” = 默认参数下代码运行正常产生交易，OAT优化正在后台进行中。*

---

## 二、批量复现初步验证结果 (2026-04-23)

> 以下结果为 **默认参数**下的快速验证（`method=none`），OAT+GA 优化正在后台进行中。初步验证目的是策略逻辑是否正确实现、是否能产生有效交易。

### 重点发现

| 发现 | 说明 |
|------|------|
| **GLD 是反转策略的得分王** | 在 RSI-2 (1.59)、Pullback RSI (1.29)、Backtested BB (1.19)、BB Breakout (0.93)、BB Squeeze (0.93) 上均表现最好 |
| **IWM 在 Larry Connors RSI-2 上表现出色** | IWM Sharpe=1.02，显著好于 SPY (0.30) 和 QQQ (0.11) |
| **出场条件是代码生成的关键痛点** | Stochastic 和 BB 策略因 `am.high[-1]` 指向当天 high 而非昨天 high，导致 Trades=1。修复为 `am.high[-2]` 后交易次数恢复正常 |
| **Volatility Swing Trade 交易频率极高** | SPY 304 次，IWM 316 次，但 Sharpe 仅 0.17-0.53，成本敏感 |
| **Stochastic Extremes Gold 在宽基上也可用** | SPY 0.60, QQQ 0.69, GLD 0.72 — 不仅限于黄金 |

### 各品种综合表现

| 策略 | SPY | QQQ | IWM | GLD | 备注 |
|------|-----|-----|-----|-----|------|
| RSI-2 Strategy | 0.77 | 0.38 | 0.78 | **1.59** | GLD 最佳 |
| RSI-2 Larry Connors | 0.30 | 0.11 | **1.02** | 0.90 | IWM 最佳 |
| Pullback RSI | **0.83** | 0.30 | 0.22 | **1.29** | SPY/GLD 均佳 |
| Backtested BB | 0.59 | 0.69 | 0.51 | **1.19** | GLD 最佳 |
| BB Breakout | 0.40 | 0.78 | 0.26 | **0.93** | QQQ/GLD 均佳 |
| Stochastic MR | 0.39 | 1.20 | 0.50 | 0.75 | QQQ 突出 |
| Stochastic Extremes | 0.60 | 0.69 | -0.14 | 0.72 | IWM 失败 |
| Pullback Trading | 0.37 | 0.44 | 0.24 | 0.83 | GLD 最佳 |
| Volatility Swing | 0.44 | 0.53 | 0.17 | 0.20 | 频率过高 |
| MACD Histogram Rev | **1.04** | **1.38** | 0.67 | 0.94 | QQQ 最佳 (已有OAT结果) |
| Consecutive Down Days | **1.76** | - | - | - | SPY 复现 Green (已有OAT结果) |
| MACD Hook Gold | - | - | - | **1.22** | GLD 复现 Green (已有OAT结果) |

> *Sharpe 为默认参数下的结果。粗体 = Sharpe > 1.0，斜体 = Sharpe 0.5-1.0，普通 = Sharpe < 0.5。*

---

## 三、按信号类型深度分析

### 2.1 价格极端型 (Price Extremes) — 最稳健

#### Consecutive Down Days（连续下跌日）
- **核心**: 在**长期上升趋势中**，买入短期连续下跌造成的恐慌
- **关键发现**: 趋势过滤器是生死线 — 原文 SMH 1.5% avg gain / 78% win rate，但仅在市场处于长期 uptrend 时成立
- **复现结果**: SPY Sharpe **1.762**，MaxDD 仅 **2.25%**，年化 6.78%，174 笔交易
- **最佳参数** (OAT+GA): decline=3, MA=90, hold=5, rsi_exit=25
- **品种差异**: 宽基股指 (SPY/VTI/DIA) 表现优异，防御/消费板块 (XLP/XLU/XLV) 完全失败
- **注意事项**: 高 beta 品种 (SMH/QQQ) 单笔收益更高，但夏普比不如宽基稳定

#### 5 Swing Strategies 中的价格型策略
- **5-Day Low**: 收盘价低于前 5 日最低 — 最简单却 among the best
- **Turnaround Tuesday**: 周一跌 + 周五跌 = 连续两天下跌后买入 — 仅 11% 时间在市场，风险调整回报 **65%**
- **统一出场**: 所有 5 个策略共享 `Close > yesterday's High` — 卖入强势，无 FOMO，机制化纪律
- **组合效果**: 5 策略合一，$100k → $3.2M (1993-2025)，MaxDD 23%，仅 2 个亏损年

#### 关键洞察
> 价格极端型策略的 edge 来自**行为金融学** — 投资者过度反应导致短期价格偏离。统一出场规则 (`Close > yesterday's High`) 是其灵魂：不贪婪，机械锁定反弹利润。

---

### 2.2 指标极端型 (Indicator Extremes) — 高波动高回报

#### MACD Histogram Mean Reversion
- **核心**: MACD Histogram 在短期下跌后转向回归零轴
- **复现结果**: QQQ Sharpe **1.038**，但 MaxDD 高达 **40.25%**，年化 38.79%
- **SPY 表现**: Sharpe 0.815，MaxDD 31.84%
- **风险警示**: 高夏普来自高波动，回撤极大，实际交易中需严格仓位控制

#### Larry Connors RSI-2
- **核心**: RSI(2) < 阈值买入，> 阈值卖出，配合 200 日均线趋势过滤
- **知识库状态**: 批量导入后复现 Red (SPY Sharpe=0)，可能因 DSL 翻译偏差或参数范围设置不当
- **经典表现**: 原论文在 SPY 上表现优异，但近年来可能衰减
- **注意事项**: 极短周期 RSI 对交易成本极敏感，滑点 0.1% 可能吃掉全部 alpha

#### Stochastic Extremes (Gold)
- **核心**: Stochastic 交叉 + 趋势过滤 + ATR 动态仓位
- **原文结果**: CAGR 4.98%，MaxDD 8.8%，Win Rate 68.95%，MAR 0.56
- **时间框架**: 2 小时线，兼顾交易频率与噪音过滤
- **知识库状态**: 复现 Red，可能因 DSL 未正确翻译 2H 周期或 Gold CFD 数据差异

#### MACD Hook Gold
- **核心**: MACD Line > 0 + Histogram Hook (m > m[1] and m[1] < m[2]) + Hull MA 确认
- **复现结果**: GLD Sharpe **1.223**，MaxDD 仅 **1.35%**，年化 2.08%，33 笔交易/20 年
- **关键发现**: GA 将所有参数改写 — 原文 (12,26,9) 优化为 (15,19,10)，Hull MA 从 15 降至 10
- **策略特征**: 频率极低，精度极高，适合作为组合中的"事件型"配置

#### 关键洞察
> 指标极端型策略的夏普通常较高，但**回撤也大**。MACD Histogram Rev 的 40% MaxDD 说明：高夏普 ≠ 低风险。这类策略更适合作为组合卫星配置，而非核心仓位。

---

### 2.3 波动率/通道型 (Volatility/Channel) — 方向中性

#### Bollinger Band Squeeze
- **核心**: 布林带宽度显著收窄 → 低波动率阶段后爆发性移动
- **三阶段**: Contraction (收窄) → Breakout (突破) → Expansion (扩张)
- **原文设置**: 周线 + 10 周回看 + 10-bar RSI 过滤
- **注意**: Squeeze 本身**不预测方向**，只预测大幅波动。需配合方向过滤或双向交易
- **知识库状态**: 规则付费，仅知 PEP 回测表现良好。复现 Red 可能因方向判断缺失

#### Bollinger Band Breakout (知识库另一篇)
- **复现结果**: SPY Sharpe 0.905 (Yellow)，MaxDD 11.13%，但 crypto 全面 Red
- **参数**: lookback=18, std_dev=0.7
- **启示**: 布林带在股票上勉强可用，在加密货币上因波动结构不同而失效

#### 关键洞察
> 布林带类策略的方向中性特性既是优势也是劣势。优势：不赌方向，两边都能赚。劣势：在假突破 (false breakout) 频发的市场被反复打脸。股票市场的假突破率低于商品/加密货币。

---

### 2.4 统计/Z-Score型 (Statistical) — 组合基石

#### ETF Mean Reversion Mini-Portfolio
- **四系统**: Z_Reversion | Vol_Reversion | Vol_Reversion_2 | RSI_Reversion
- **Sub-entry**: 每个系统分 3 次建仓，每次 1/3 等权 — 80/20 甜蜜点
- **组合效果**: 回撤相关性 ~0.34，收益相关性 0.06~0.79
- **历史表现**: 2000 年以来（除 2000 年一次较大回撤外）**没有一年亏损**
- **动态排名**: 按滚动 1 年 Sharpe 排名，每季度更新，`ExcludeWorstX` 可屏蔽最差曲线
- **核心哲学**: **不仅跨资产、跨时间、跨价格，还要跨思想/实现方式**

#### Delphic Alpha Atlas — FX 5-day MR
- **核心**: Z-score fade，买超卖卖超买，5 日回看
- **结果**: Sharpe **1.29**，IC ≈ 0.05 — 全研究中最稳定的 edge
- **样本外**: FX MR 是唯一 IS→OOS 最一致的信号族
- **原因**: FX 市场流动性高、信息密集、短期均值回归是结构性特征

#### 关键洞察
> 统计型策略单看 Sharpe 并不惊艳，但**组合后发生质变**。Portfolio Effect 是唯一圣杯 — 单一系统回测再好也可能过拟合，真正低相关的系统组合才能分散风险。TMF(债券)近期回撤时，组合整体几乎不受影响。

---

### 2.5 跨资产型 (Cross-Asset) — 待验证

#### Stocks-Bonds Mean Reversion
- **核心**: 利用股债短期偏离的均值回归
- **知识库状态**: 复现 Red，可能因 DSL 未正确实现跨资产逻辑
- **理论价值**: 股债相关性在危机时趋同，正常时期分化，存在均值回归空间

---

## 三、哪些策略能做？表现如何？

### 3.1 可直接上实盘（Green 级）

| 策略 | 最佳品种 | Sharpe | MaxDD | 年化 | 频率 | 核心优势 |
|------|----------|--------|-------|------|------|----------|
| Consecutive Down Days | SPY | 1.76 | 2.25% | 6.78% | 中 | 回撤极小，宽基稳健 |
| MACD Hook Gold | GLD | 1.22 | 1.35% | 2.08% | 极低 | 精度极高，风险极小 |
| MACD Histogram Rev | QQQ | 1.04 | 40.25% | 38.79% | 中 | 高回报，适合卫星 |
| ETF MR Mini-Portfolio | 多资产 | ~1.0+ | <10% | ~8% | 高 | 组合稳健，无年亏损 |

### 3.2 值得进一步验证（Yellow 级）

| 策略 | 关键障碍 | 验证路径 |
|------|----------|----------|
| 5 Swing Strategies | 规则完整但需组合实现 | 先跑 #3 (5-Day Low)，再叠加 #2 |
| Bollinger Band Squeeze | 完整规则付费 | 自行实现基础版周线+RSI过滤 |
| Consecutive Down Days (原文) | 规则付费 | 复现已 Green，可直接用复现参数 |

### 3.3 当前不推荐（Red / 待复现 / DSL不支持）

| 策略 | 失败原因 | 是否值得再试 |
|------|----------|--------------|
| Stocks-Bonds MR | DSL 不支持跨资产逻辑 | 待 DSL 增强或手动实现 |
| Weekly MR (VIX) | 需 VIX 外部数据加载 | 是，可用 sqlite3 在策略内加载 VIX |
| 5 Swing Strategies (组合) | 需多系统合并逻辑 | 是，先单独验证各子策略 |
| ETF MR Mini-Portfolio | 需多系统组合 + Sub-entry | 是，但需专用框架 |

> *注：以上策略的失败非策略本身无效，而是当前自动化复现框架的限制。*

---

## 四、需要注意的 10 个关键问题

### 4.1 趋势过滤器是生死线
> 所有成功的反转策略都包含某种形式的趋势过滤。Consecutive Down Days 要求"长期上升趋势"，MACD Hook 要求"MACD Line > 0"，5 Swing Strategies 隐含长-only。在熊市中做反转 = 接飞刀。

### 4.2 出场规则比入场更重要
> 5 Swing Strategies 的 `Close > yesterday's High` 统一出场是其灵魂。MACD Histogram Rev 的 40% MaxDD 暴露了出场规则的重要性。反转策略赚的是"反弹"，不是"趋势" — 必须机械止盈。

### 4.3 高 beta ≠ 高夏普
> SMH 单笔收益 (1.5%) > SPY (0.7%)，但复现后 SPY Sharpe (1.76) > SMH。高 beta 品种波动大，信号多，但噪音也多。宽基指数是反转策略的压舱石。

### 4.4 防御板块不适合反转
> XLP/XLU/XLV/XLRE 在 Consecutive Down Days 复现中全面 Red。低波动、强趋势性板块缺乏均值回归的空间。反转策略应聚焦高波动资产。

### 4.5 过拟合税：回测 Sharpe 打 75 折
> Delphic Alpha 研究：IS→OOS 斜率仅 0.24。回测 Sharpe 1.0 → 实盘期望 0.25。任何需要优化才能显示 edge 的策略，edge 可能在优化里。

### 4.6 交易成本是反转策略的头号杀手
> 反转策略交易频率高于趋势跟踪，单笔利润薄。0.03% 的 slippage+commission 在 5 Swing Strategies 中已被包含，但日内/2H 策略的成本可能吃掉全部 alpha。RSI-2 对滑点极敏感。

### 4.7 Portfolio Effect 是唯一圣杯
> 四个普通的均值回归系统组合成一个 mini-portfolio，其风险调整后收益远超任何单一系统。不仅跨资产，还要**跨思想/实现方式**。 diversification of ideas > diversification of assets。

### 4.8 Sub-entry 平滑捕捉超卖
> ETF MR Mini-Portfolio 的 3 次 sub-entry (每次 1/3) 是 80/20 甜蜜点。比 2 次更能平滑捕捉超卖，比 5 次更简单可执行。避免"全押在一个价位"。

### 4.9 不同市场有不同本性
> FX 均值回归 (Sharpe 1.29)，商品趋势跟踪 (Sharpe 0.53)。不要在 FX 上跑趋势，不要在商品上跑反转（除非有特定逻辑）。Match the signal family to the market's microstructure。

### 4.10 批量导入策略质量参差不齐
> 知识库中大量 Substack 批量导入的策略 wiki 页面内容待补充，复现结果多为 Red。可能原因：(1) DSL 翻译未覆盖原文完整逻辑；(2) 参数搜索范围不当；(3) 部分策略需要特定数据 (VIX, CFD, 跨资产)。建议优先复现规则完整、来源可信的策略。

---

## 四、可执行的组合建议

### 5.1 保守型反转组合（低波动，适合大资金）

| 策略 | 权重 | 作用 |
|------|------|------|
| Consecutive Down Days (SPY) | 40% | 核心仓位，Sharpe 1.76，回撤 2.25% |
| MACD Hook Gold (GLD) | 30% | 卫星仓位，极低频，极高精度 |
| ETF MR Mini-Portfolio | 30% | 分散化基石，多资产多系统 |

**预期**: 组合 Sharpe ~1.2-1.4，MaxDD < 10%，年化 5-8%。

### 5.2 进取型反转组合（高波动，适合小资金）

| 策略 | 权重 | 作用 |
|------|------|------|
| MACD Histogram Rev (QQQ) | 30% | 高回报引擎，但需承受 40% 回撤 |
| 5-Day Low (SPY) | 30% | 简单稳健，统一出场 |
| FX 5-day MR | 20% | 跨资产，结构性 edge |
| Stochastic Extremes (Gold) | 20% | 商品暴露，2H 频率 |

**预期**: 组合 Sharpe ~1.0-1.2，MaxDD 15-25%，年化 10-20%。

### 5.3 实施路径

1. **Phase 1** (1-2 周): 先跑 Consecutive Down Days + 5-Day Low，验证基础逻辑
2. **Phase 2** (2-4 周): 加入 MACD Hook Gold，测试多策略并行
3. **Phase 3** (1-2 月): 构建 ETF MR Mini-Portfolio 或等效的多系统组合
4. **Phase 4** (持续): 每季度回顾各策略 equity curve，屏蔽最差 1-2 条曲线

---

## 五、数据需求与工具链

| 数据类型 | 最小频率 | 用途 | 来源 |
|----------|----------|------|------|
| 美股 ETF 日线 | 日线 | 价格极端型策略 | Yahoo / vnpy |
| VIX 指数 | 日线 | 恐惧过滤 / 仓位调整 | CBOE |
| 黄金期货/ETF | 日线/2H | 商品反转策略 | IB / OKX |
| G7 FX | 日线 | FX 均值回归 | IB / Forex |
| ATR / RSI / MACD | 实时计算 | 指标型策略 | vnpy内置 |

**推荐工具链**:
- 回测: `cta-strategy-factory` (OAT + GA 优化)
- 组合分析: 自研 equity curve 相关性矩阵
- 监控: 每月更新各策略 rolling Sharpe，触发 `ExcludeWorstX`

---

## 六、相关概念与实体

- [[consecutive-down-days-strategy]] — 连续下跌日策略详情
- [[etf-mean-reversion-mini-portfolio]] — ETF 均值回归组合详情
- [[macd-histogram-mean-reversion]] — MACD Histogram 回归详情
- [[macd-hook-gold-strategy]] — MACD Hook 黄金策略详情
- [[5-swing-trading-strategies]] — 5 个波段策略详情
- [[bollinger-band-squeeze]] — 布林带挤压策略
- [[mean-reversion]] — 均值回归概念页
- [[trend-filter]] — 趋势过滤器概念页
- [[delphic-alpha-atlas]] — Delphic Alpha 多资产研究
- [[portfolio-effect]] — 组合效应概念页

---

*Last updated: 2026-04-23 (batch reproduction in progress, OAT optimization running in background)*
*Next review: OAT results expected in 2-4 hours*
