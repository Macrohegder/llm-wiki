---
id: reversal-strategy-pipeline-2026-04-26
title: "反转策略失焦分析 — 规则明确、尚未对接复现的策略清单"
date: "2026-04-26"
tags:
  - concept/reversal
  - concept/mean-reversion
  - synthesis
  - strategy-pipeline
  - pipeline-prioritization
---

# 反转策略失焦分析 — 规则明确、尚待复现的策略清单

> **目标**：从 llm-wiki 知识库已录入的约 1043 篇反转策略文章中，筛选出**规则明确（免费/非付费墙）**且**尚未在 cta_developer 中实现复现**的策略，按品种适配规律分类。

---

## 一、已复现的反转策略现状

### ✅ 已完成（已跑 batch + wiki 同步）

| 策略 | 别名 | 来源 | 核心逻辑 | 最佳品种 | Batch 结果 |
|------|------|------|---------|----------|-----------|
| Pullback MR（回撤均值回归） | PB | QuantifiedStrategies | close > SMA200 + < SMA20 + RSI5 < 45 | GLD (1.06) | 24/24 Green/Yellow |
| 5-Day Low of The Range | FDLR/5DLR | Paper to Profit | IBS < 0.25 + close < 5天低 | XLP (0.82) | 6 Green, 16 Yellow, 3 Red |
| Consecutive Down Days | CDD | QuantifiedStrategies | 连跌N天 + SMA过滤买入 | SPY (1.76) | 18品种多Green |
| MACD Histogram MR | - | QuantifiedStrategies | MACD柱连跌N天买入 | QQQ (1.04) | 后14品种9 Green |
| MACD Hook Gold | - | Algomatic Trading | MACD Hook + Hull MA | GLD (1.22) | 单品种验证 |
| RSI-2 Larry Connors | - | QuantifiedStrategies | RSI2 < 阈值 + SMA200过滤 | GLD (1.70) | OAT 多品种 |
| Stochastic MR | - | QuantifiedStrategies | %K < 20 买入 | GLD (1.39) | OAT验证 |
| Volatility Swing | - | QuantifiedStrategies | RSI超卖买入 | GLD (1.08) | OAT验证 |
| OLMAR (单品种) | - | Paper to Profit | 单股均值回归 | 全Red | 放弃(需要多股票) |
| Counter-Trend ES | - | Alpha Algo | SMA200反趋势+位置入场 | ES (0.57) | 日线简化版 |

### ❌ 已尝试但放弃的

| 策略 | 原因 |
|------|------|
| Stocks-Bonds MR | DSL不支持跨资产 |
| BB Breakout/Squeeze | 付费墙，规则不全 |
| Four Up Days In A Row | 付费墙(QuantifiedStrategies) |
| Unfilled Gap Trading | 付费墙，信号太少 |
| Averaging Down | 不是规则策略，是概念 |

---

## 二、规则明确、尚未复现的潜力策略

以下从 wiki 资料中筛选，原文有完整规则且非付费墙：

### 🟢 P0 优先级 — 规则极简，预计立即能跑

#### 1. **Turnaround Tuesday（星期二反转）**
   - **来源**: QuantifiedStrategies, 自由预览
   - **规则**: 周一跌 + 周五跌(连续两天下跌) → 周二开盘买入，收盘卖出
   - **时间框架**: 日线，隔日持仓
   - **原因不选**: 非标准日线持仓(需盘中开盘/收盘价)
   - **可转债为日线**: 收盘买入 → 次日收盘卖出 ≈ 1日持仓
   - **5 Swing Strategies 中效果**: 仅11%时间在市场，风险调整回报 65%
   - **链接**: [[2026-04-25-Turnaround-Tuesday-Strategy-Backtest]]

#### 2. **Turn of Month（月末效应）** ⭐⭐⭐⭐⭐
   - **来源**: QuantifiedStrategies, 公开研究
   - **规则**: 每月最后交易日 + 前3个交易日买入 SPY
   - **时间框架**: 日线
   - **Sharpe 参考**: 原文 Sharpe > 1.0
   - **复现难度**: 极低 — 无参数，纯日历
   - **链接**: [[2026-04-25-Turn-of-The-Month-Strategy]]

#### 3. **5-Day Low Overnight（5日低隔夜策略）**
   - **来源**: QuantifiedStrategies
   - **规则**: 收盘价 < 过去5日最低 → 买入隔夜持仓到次日开盘
   - **与5DLR区别**: 只持1天 vs 5DLR持5天
   - **Sharpe 参考**: 原文高Sharpe 低回撤
   - **链接**: [[2026-04-25-The-5-Day-Low-Overnight-Trading-Strategy-ExplainedSP-500-Overnight]]

#### 4. **3 Days Down Overnight（3日跌隔夜策略）**
   - **来源**: QuantifiedStrategies
   - **规则**: 连续3天下跌 → 买入隔夜
   - **与CDD区别**: CDD有SMA过滤 + 持有5天；这个纯隔夜
   - **Sharpe 参考**: 原文表现稳定
   - **链接**: [[2026-04-25-3-Days-Down-Overnight-Trading-Strategy-SP-500-Nasdaq-Rules-Performance-Analysis]]

### 🟡 P1 优先级 — 规则清晰但参数稍多

#### 5. **Williams %R Trading Strategy**
   - **来源**: QuantifiedStrategies
   - **规则**: Williams %R < 超卖阈值(默认-80) → 买入，> 超买阈值(-20) → 卖出
   - **变体**: 可加SMA200过滤(Larry Connors风格)
   - **与已有策略区别**: 现在没有基于Williams %R的策略
   - **链接**: [[2026-04-25-Williams-R-Trading-Strategy-81-Win-Rate]]

#### 6. **IBS Indicator Strategy（内部柱强度）**
   - **来源**: QuantifiedStrategies
   - **规则**: IBS = (close - low) / (high - low)，IBS < 0.25 买入，> 0.75 卖出
   - **5DLR 已包含类似逻辑**: 但IBS是原版，更通用(双向)
   - **可做**: 简单版：IBS < 0.2 买入，持3天
   - **链接**: [[2026-04-25-The-Internal-Bar-Strength-IBS-Indicator---Trading-Strategies-Rules]]

#### 7. **Consecutive Down Days Overnight（连续跌日隔夜版）**
   - **来源**: QuantifiedStrategies
   - **规则**: 连跌2天 → 第3天开盘买入，隔夜持到收盘 / 或收盘买入持到次日开盘
   - **相比CDD**: 无SMA200过滤，持有时间短
   - **适合**: 高频交易，更适合SPY

#### 8. **Rubber Band Strategy（橡皮筋策略）**
   - **来源**: QuantifiedStrategies
   - **规则**: 价格偏离均线超过一定标准差 → 买入回归
   - **类似**: 布林带回归但更激进
   - **需确认**: 免费版是否有完整规则
   - **链接**: [[2026-04-25-The-Rubber-Band-Strategy]]

### 🟠 P2 优先级 — 规则较复杂或需额外数据

#### 9. **NR7 Trading Strategy（窄幅7日策略）**
   - **来源**: QuantifiedStrategies
   - **规则**: 当日波动范围是过去7日最小 → 次日突破方向交易
   - **本质**: 低波动率收缩 → 爆发跟随
   - **难点**: 需要识别突破方向(可用SMA方向过滤)
   - **链接**: [[2026-04-25-NR7-Trading-Strategy-The-Narrow-Range-7-Enhanced-and-Improved-Version]]

#### 10. **Candlestick Patterns (Doji / Engulfing / 123 Pattern)**
   - **来源**: QuantifiedStrategies
   - **Doji规则**: 十字星出现 → 次日向趋势方向突破
   - **Engulfing规则**: 吞没形态 → 反转信号
   - **123 Pattern**: 3波价格摆动 → 趋势反转
   - **难点**: 形态识别需严格量化，不同定义导致不同结果
   - **可做**: 选最简单的 Doji + SMA过滤
   - **链接**: 
     - [[2026-04-25-Doji-Candlestick-Strategy-for-Stocks-Backtested-Rules-and-Result]]
     - [[2026-04-25-123-Pattern-Reversal-Trading-Strategy-Setup-and-Backtest]]

#### 11. **Outside Day Bar（外包日线）**
   - **来源**: QuantifiedStrategies
   - **规则**: 当日high>昨日high AND low<昨日low → 方向突破
   - **本质**: 波动扩张 + 方向确认
   - **链接**: [[2026-04-25-Outside-Day-Bar-Trading-Strategy-Rules-Settings-Performance-and-Backtest-Insight]]

#### 12. **Seasonal / Calendar Effects 细类**
   - **来源**: QuantifiedStrategies
   - **包括**: 节假日效应、OPEX周、Santa Rally、Easter效应
   - **规则**: 纯日历驱动，无参数
   - **难度**: 极低，但信号稀疏(每年1-5次)
   - **链接**: 
     - [[2026-04-25-The-Holiday-Effect-in-Stock-Markets-Explained-Strategies-and-Seasonal-Insights]]
     - [[2026-04-25-The-Options-Expiration-Week-Effect]]

---

## 三、品种类型 × 反转策略适配规律

### 3.1 现有回测数据的品种分类

基于 200+ 次品种级回测，将 24 ETF 按均值回归特性分类：

#### 🟢 Tier A: 反转天生生效（结构性均值回归）

| 品种 | 类型 | PB Sharpe | 5DLR Sharpe | CDD Sharpe | 其他最佳 |
|------|------|-----------|-------------|------------|----------|
| **GLD** | 商品 | **1.06** | 0.30 | - | RSI2 1.70, Stoch 1.39 |
| **XLP** | 消费必需品 | 0.42 | **0.82** | Red | 防守+结构型 |
| **EEM** | 新兴市场 | 0.57 | **0.74** | - | 非效率性 |
| **XLK** | 科技 | 0.72 | 0.62 | 1.23 | 高beta+趋势过滤 |
| **QQQ** | 科技指数 | 0.55 | 0.53 | 1.03 | MACD Hist 1.04 |
| **SPY** | 宽基指数 | 0.62 | 0.56 | **1.76** | 完美CDD品种 |
| **VWO** | 新兴市场 | 0.52 | - | - | 弱MR |

**特征**: 低-中波动 + 弱趋势/noise ratio = 反转信号干净

#### 🟡 Tier B: 条件性有效（需优化参数/特定策略）

| 品种 | 类型 | 表现策略 | 最差策略 |
|------|------|---------|---------|
| **IWM** | 小盘 | PB(0.62), CDD(Green) | - |
| **XLI** | 工业 | PB(0.68) | 5DLR(0.44) |
| **DIA** | 道指 | PB(0.55) | - |
| **XLV** | 医疗 | - | CDD(Red) |
| **XLU** | 公用事业 | - | CDD(Red) |
| **TLT** | 长债 | PB(0.58) | 5DLR(0.41) |
| **XLY** | 可选消费 | - | 5DLR(0.56) |

**特征**: 反转有效但edge较弱，需策略匹配 + 参数优化

#### 🔴 Tier C: 反转天生无效（趋势主导/跳跃结构）

| 品种 | 类型 | 失败证据 |
|------|------|---------|
| **USO** | 原油 | 5DLR(-0.41) 所有反转策略Red |
| **XLE** | 能源 | 5DLR(-0.22), PB(0.40) |
| **SHY** | 短债 | 5DLR(-0.29) |
| **UNG** | 天然气 | 多数反转策略Red |

**特征**: 高波动 + 强趋势跳跃 → 反转信号被趋势吞没

### 3.2 适配规律总结

```
反转策略 × 品种的选择公式：

        低波动 + 低趋势      →  指标极端型（RSI2/Stoch/WilliamsR）
        低波动 + 中趋势      →  价格结构型（IBS/5DL/FDLR）  
        中波动 + 中趋势      →  趋势过滤型（PB/CDD）
        高波动 + 弱趋势      →  隔夜型（频率高，赚波动钱）
        高波动 + 强趋势      →  ❌ 不适合任何反转策略

具体品种的最佳反转策略类型：

    GLD    →  指标极端型(Stoch/RSI2/WilliamsR)  → Sharpe 预期 1.0-1.7
    SPY    →  价格结构型(CDD/5DL) + 趋势过滤     → Sharpe 预期 0.6-1.8
    QQQ    →  趋势过滤型(PB/BB)                   → Sharpe 预期 0.5-1.0
    XLP    →  价格结构型(IBS/5DL)                 → Sharpe 预期 0.5-0.8
    EEM    →  价格结构型(5DL)                     → Sharpe 预期 0.5-0.7
    XLE/USO →  ❌ 放弃反转，换趋势跟踪
    TLT    →  温和趋势过滤型(PB)                   → Sharpe 预期 0.4-0.6
    IWM    →  trend+回调型(PB)                    → Sharpe 预期 0.5-0.6
```

### 3.3 为什么GLD是反转之王

来自 13 个反转策略 × 24 品种 = 200+ 次回测的实证数据：

```
GLD 在所有策略上稳定产生正Sharpe的原因：
  ├→ COMEX期货投机者主导短期价格（噪音来源）
  ├→ 宏观驱动(利率/美元/地缘)长期趋势（噪音回归方向）
  ├→ 日均波动 1-2% 提供反转空间
  └→ ETF 结构有被动买盘托底（与SPY相似的dip-buying结构）

金句: "GLD的反转edge不是你的策略厉害，是GLD本身厉害"
```

### 3.4 防御板块的反转特性（XLP/XLU/XLV）

```
意外的发现：
  ├→ XLP在价格结构型（5DLR）上表现最好(0.82)
  ├→ XLU/XLV在趋势过滤型(PB)上表现平庸
  └→ CDD在防御板块全面Red

解释：防御板块低波动+慢趋势→IBS信号干净但连续下跌信号无效
      （连续下跌意味着基本面前景变化，不是短期恐慌）
```

---

## 四、复现优先级排名

### 🥇 第一梯队（本周可以搞定的）

| 优先级 | 策略名 | 规则完整性 | 预计交易数/年 | 适配品种 | 策略逻辑复杂度 |
|--------|--------|-----------|-------------|---------|--------------|
| P0 | **Turn of Month** | ✅ 完整免费 | ~5次/月 | SPY | ⭐ (纯日历) |
| P0 | **IBS Strategy** | ✅ 完整免费 | ~20次/月/品种 | XLP/XLY/SPY | ⭐⭐ (IBS<0.25) |
| P0 | **5-Day Low Overnight** | ✅ 完整免费 | ~15次/月 | SPY/QQQ | ⭐⭐ (1日持仓) |
| P0 | **3 Days Down Overnight** | ✅ 完整免费 | ~10次/月 | SPY | ⭐⭐ (隔夜) |

### 🥈 第二梯队（1-2周搞定）

| 优先级 | 策略名 | 规则完整性 | 预计交易数/年 | 适配品种 | 策略逻辑复杂度 |
|--------|--------|-----------|-------------|---------|--------------|
| P1 | **Williams %R** | ✅ 完整免费 | ~20次/月 | GLD/SPY | ⭐⭐⭐ (指标阈值) |
| P1 | **Consecutive Down Overnight** | ✅ 完整免费 | ~15次/月 | SPY | ⭐⭐ (CDD简化) |
| P1 | **Rubber Band** | ⚠️ 需确认 | ~10次/月 | SPY/GLD | ⭐⭐⭐ (偏离度) |
| P1 | **Doji Candlestick** | ⚠️ 形态需量化 | ~5次/月 | SPY | ⭐⭐⭐⭐ (形态识别) |

### 🥉 第三梯队（3-4周搞定）

| 优先级 | 策略名 | 规则完整性 | 预计交易数/年 | 适配品种 | 策略逻辑复杂度 |
|--------|--------|-----------|-------------|---------|--------------|
| P2 | **NR7** | ✅ 有但需破方向 | ~8次/月 | SPY/QQQ | ⭐⭐⭐⭐ (突破确认) |
| P2 | **Outside Day** | ✅ 完整 | ~5次/月 | SPY | ⭐⭐⭐ (波动扩张) |
| P2 | **123 Pattern** | ⚠️ 需量化 | ~3次/月 | ALL | ⭐⭐⭐⭐⭐ (复杂) |
| P2 | **Seasonal细类** | ✅ 完整 | 1-5次/年 | SPY | ⭐ (纯日历) |

---

## 五、核心结论

### 5.1 现在该做什么

按效率排序，**下周可以完成**的复现：

```
1. IBS Strategy（P0，1天）
   → XLP 预期 Sharpe 0.5-0.8（继5DLR之后另一个防守板块利器）
   → 规则：IBS = (close-low)/(high-low)，IBS < 0.25 buy，可做多空双向

2. Turn of Month（P0，2小时）
   → 纯日历，零参数，Sharpe历史 > 1.0
   → 规则：每月最后1+前3个交易日买入SPY

3. 5-Day Low Overnight（P0，半天）
   → 与已有5DLR共享90%代码逻辑，只需改持仓期为1天
   → 预期 Sharpe > 0.8 on SPY

4. Williams %R Strategy（P1，1天）
   → 新指标族（不是RSI/Stoch/IBS的简单变体）
   → GLD预期 Sharpe 0.8-1.2
```

### 5.2 品种启动顺序

与其全部24品种batch，不如先聚焦**品种×策略最佳配对**：

```
第一枪: IBS → XLP/XLY（防守+可选消费的结构型反转） 
        + 5DL Overnight → SPY（隔夜版高频率）
        + Turn of Month → SPY（纯日历零参数）

第二枪: Williams %R → GLD（指标极端型 + GLD = 天然配对）
        然后扩展到 24 ETF batch

第三枪: 组合验证 — 把最好的3-5个反转策略合并为mini-portfolio
```

### 5.3 已有综合页面的补充

- [[reversal-strategies-compendium]] — 1043篇反转策略分类总览
- [[mean-reversion-strategies-compendium]] — 已复现策略结果汇总
- [[reversal-deep-analysis-karpathy]] — 深度分析：哪些edge真实
- [[reversal-strategy-landscape]] — 反转策略全景

---

*生成: 2026-04-26 | 基于llm-wiki 200+次品种级回测 + 1043篇反转策略文章*
