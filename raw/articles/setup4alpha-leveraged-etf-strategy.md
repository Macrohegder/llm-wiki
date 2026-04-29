---
id: setup4alpha-leveraged-etf-strategy
title: "3x Leveraged ETF Strategy: TQQQ + TMF Rebalancing Backtest"
source: "SetupAlpha"
url: https://setup4alpha.substack.com/p/leveraged-etf-strategy-tqqq-tmf-rebalancing-backtest
published: 2025-10-05
saved_at: 2026-04-29
tags: [leveraged-etf, TQQQ, TMF, rebalancing, portfolio, beta-slippage, crash-filter, academic]
---

# 3x Leveraged ETF Strategy: 2,600% Return With 38% Drawdown

> 作者: SetupAlpha  
> 发布时间: 2025-10-05  
> 来源: https://setup4alpha.substack.com/p/leveraged-etf-strategy-tqqq-tmf-rebalancing-backtest  
> 付费文章（部分规则可见）

---

## 核心摘要

基于 **Dr. Lewis A. Glenn 2020年 SSRN 论文** "Long-Term Investing in Triple Leveraged Exchange Traded Funds" 的复现与扩展。

**核心思想**: TQQQ(3x纳指) + TMF(3x长期国债) 50/50 等权配置，每2个月再平衡，加一个黑天鹅崩溃过滤器。

**回测结果 (2010-01 ~ 2025-10)**:

| 指标 | 数值 |
|------|------|
| **起始资金** | $100,000 |
| **最终权益** | **$1,581,916** |
| **CAGR** | **19.58%** |
| **最大回撤** | **-28.48%** |
| **MAR Ratio** | 0.69 |
| **总交易数** | 167 |
| **胜率** | 76.05% |
| **Profit Factor** | 2.71 |
| **Sharpe Ratio** | 0.87 |
| **Sortino Ratio** | 1.42 |
| **波动率** | 23.75% |

---

## 策略规则（完整版）

### 持仓配置

| 标的 | 权重 | 说明 |
|------|------|------|
| TQQQ | 50% | ProShares UltraPro QQQ (3x纳指) |
| TMF | 50% | Direxion Daily 20+ Year Treasury Bull 3X (3x长期国债) |

### 再平衡规则

- **频率**: 每 **2个月** 再平衡一次
- **时点**: 每第二个月的最后一个交易日
- **操作**: 检查当前权重，卖出超配标的、买入低配标的，恢复 50/50

### 崩溃过滤器 (Crash Filter)

| 条件 | 操作 |
|------|------|
| TQQQ 单日跌幅 ≥ **20%** | 立即清仓 TQQQ 和 TMF，100% 转入 IEF (7-10年期国债ETF) |
| TQQQ 恢复并超过崩溃前价格 | 重新建立 50/50 TQQQ/TMF 配置 |

---

## 理论基础

### Beta Slippage (杠杆衰减)

> 杠杆ETF每日再平衡以维持3x敞口，在震荡市中产生衰减。

**示例**:
- 标的: +25% 后 -20% → 回到原点 `(1+0.25)×(1-0.20)=1.0`
- 3x ETF: +75% 后 -60% → **亏损30%** `(1+0.75)×(1-0.60)=0.70`

### 负相关性对冲

科技股与长期国债通常呈负相关：
- 恐慌时 → 卖股票买债券
- 乐观时 → 卖债券买股票

这种结构性关系（而非统计巧合）为策略提供了天然对冲。

---

## 历史表现分析

### COVID 崩溃 (2020-03)
- TQQQ 暴跌，TMF 飙升（避险资金涌入债券）
- 崩溃过滤器触发，转入 IEF
- 策略避开了最糟糕的下跌

### 2022 加息周期
- TMF 暴跌（长期债券因加息崩溃）
- 但 TQQQ 相对抗跌
- 再平衡强制卖出 TQQQ(赢家) 买入 TMF(输家)
- 债券企稳后，这种逆向布局获得回报

---

## 策略弱点

| 弱点 | 说明 |
|------|------|
| **加息环境** | 若利率持续上升且科技股同时下跌（滞胀），负相关性失效 |
| **震荡市衰减** | 多年横盘高波动环境下，beta slippage 无法完全抵消 |
| **跳空风险** | 崩溃过滤器基于日收盘，若日内暴跌30%但收盘仅跌18%，过滤器不触发 |
| **资金门槛** | 至少 $50K-$100K 才能覆盖滑点和再平衡成本 |
| **ETF结构风险** | TQQQ/TMF 是 swap-based ETF，发行人风险/监管变化可能导致重组或清盘 |

---

## 学术来源

- **论文**: "Long-Term Investing in Triple Leveraged Exchange Traded Funds"
- **作者**: Dr. Lewis A. Glenn
- **年份**: 2020
- **链接**: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3722318

---

## RealTest 代码（付费订阅者可见完整版）

```
▼ Import:
	DataSource: 	Norgate
	IncludeList: 	TQQQ
	IncludeList: 	TMF
	IncludeList: 	IEF
	IncludeList: 	SPY
	StartDate: 	Earliest
	EndDate: 	Latest
	SaveAs: 	          tqqq_tmf_ief_daily.rtd

▼ Settings:
	DataFile: 	tqqq_tmf_ief_daily.rtd
	StartDate: 	1/1/2010
	EndDate: 	Latest
	BarSize: 	Daily
	AccountSize: 	100000

▼ Parameters:
	k_months: 	2
```

完整 step-by-step 规则实现仅对付费订阅者开放。

---

## 对 Raymond 的启示

1. **杠杆ETF + 再平衡**: 简单规则（50/50 + 定期再平衡）可以抵消杠杆衰减，这是对抗 "杠杆ETF不能长期持有" 常识的有力反例
2. **崩溃过滤器**: 20% 单日跌幅作为黑天鹅保护，可考虑融入我们的策略框架
3. **负相关性配对**: 股票+债券的经典组合，但用3x杠杆放大收益——我们的 ETF batch pipeline 可测试类似配对（如 SPY/TLT, QQQ/TLT）
4. **再平衡频率**: 2个月再平衡 vs 我们的日线策略——不同时间框架的分散化
5. **学术验证**: Glenn 的论文提供了理论基础，建议下载原文深入阅读
