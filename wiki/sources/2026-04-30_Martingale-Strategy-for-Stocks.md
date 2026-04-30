---
date: "2026-04-30"
author: "Quantified Strategies"
source: "quantifiedstrategies"
url: "https://quantifiedstrategies.substack.com/p/martingale-strategy-for-stocks"
status: "not-a-strategy"
concrete_score: 20
tags:
  - topic/position-sizing
  - topic/risk-management
  - topic/martingale
  - topic/behavioral-finance
---

# Martingale Strategy for Stocks

> 来源：[https://quantifiedstrategies.substack.com/p/martingale-strategy-for-stocks](https://quantifiedstrategies.substack.com/p/martingale-strategy-for-stocks) | 摄入日期：2026-04-30

---

## 核心观点

Martingale 是一种**仓位管理方法**而非交易策略：每次亏损后加倍下注，期望一次盈利即可收回所有亏损并获利。起源于 18 世纪赌博（轮盘），在交易中被实现为"摊平成本"（averaging down）或网格交易。

**核心数学**：亏损几何增长（1, 2, 4, 8, 16...），但单次盈利可覆盖全部亏损。

---

## 策略规则

| 维度 | 描述 |
|------|------|
| **核心逻辑** | 亏损后加倍仓位，直到盈利 |
| **入场条件** | 初始建仓 |
| **加仓条件** | 前一笔交易亏损 → 下一笔仓位翻倍 |
| **出场条件** | 盈利时出场（覆盖所有前期亏损 + 初始利润） |
| **止损设置** | **无** — 这是 Martingale 的致命缺陷 |
| **仓位管理** | 几何级数增长（1x, 2x, 4x, 8x...） |
| **时间框架** | 任意 |
| **适用品种** | 理论上任意，但风险极高 |
| **交易方向** | 任意 |

---

## 回测数据（原文）

原文进行了两组对比回测：

**无 Martingale 的均值回归策略（基准）**:
- S&P 500 均值回归策略

**加入 Martingale 仓位管理后**:
- 产生许多小盈利
- 最终遭遇灾难性大亏损
- 权益曲线看起来平滑 —— 直到突然崩塌
- 风险调整回报差，尽管胜率高

---

## 关键洞察

1. **指数级风险** — 5 次连续亏损后仓位是初始的 32 倍，10 次后超过 1000 倍
2. **两个致命风险**:
   - **资本耗尽** — 资金有限，无法无限加倍
   - **市场 ≠ 抛硬币** — 市场会趋势运行、跳空、崩盘，不保证反转
3. **肥尾效应** — 市场异常值远比正态分布频繁
4. **行为金融陷阱** — "锚定"于初始价格，不断摊平导致风险失控

---

## 为什么不要用它

- 将频繁的小盈利转化为罕见的灾难性亏损
- 理论上无法永远亏损，但**实践中会爆仓**
- 即使胜率 99%，剩下的 1% 足以毁灭账户

---

## 提取的实体
- [[entity: Quantified Strategies]] — 策略回测博客

## 提取的概念
- [[concept: Martingale System]] — 亏损后加倍下注的仓位管理方法
- [[concept: Averaging Down]] — 价格下跌时加仓摊平成本
- [[concept: Grid Trading]] — 在固定价格网格上买卖的系统
- [[concept: Geometric Growth]] — 几何级数增长的仓位/风险
- [[concept: Tail Risk]] — 极端市场事件的风险

## 个人批注
- **这不是一个可交易的策略**，而是一篇风险教育文章。
- concrete_score 20，因为规则简单但不可交易（无止损 = 必死）。
- 价值在于理解为什么"摊平成本"和"网格交易"在极端行情下会爆仓。
- 可作为风险管理和仓位 sizing 概念的反面教材。

## 原文备份
详见 raw/articles/quantifiedstrategies-2026-04-29-Martingale-Strategy-for-Stocks.md
