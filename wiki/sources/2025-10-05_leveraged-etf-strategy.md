---
id: 2025-10-05-leveraged-etf-strategy
title: "3x Leveraged ETF Strategy: TQQQ + TMF Rebalancing"
source: "SetupAlpha"
url: https://setup4alpha.substack.com/p/leveraged-etf-strategy-tqqq-tmf-rebalancing-backtest
published: 2025-10-05
saved_at: 2026-04-29
tags: [leveraged-etf, TQQQ, TMF, rebalancing, portfolio, beta-slippage, crash-filter, academic]
---

# 3x Leveraged ETF Strategy: TQQQ + TMF Rebalancing

**来源**: SetupAlpha Substack  
**日期**: 2025-10-05  
**标签**: #leveraged-etf #rebalancing #portfolio #beta-slippage

## 一句话摘要

基于 Dr. Lewis Glenn 2020年 SSRN 论文的复现：TQQQ(3x纳指) + TMF(3x国债) 50/50 配置，每2个月再平衡，加20%单日跌幅崩溃过滤器，15年回测 CAGR 19.6%，最大回撤 28.5%。

## 关键要点

1. **杠杆ETF可以长期持有** — 通过再平衡和负相关性配对抵消 beta slippage
2. **50/50 等权 + 双月再平衡** — 强制低买高卖，利用股债负相关性
3. **20% 单日跌幅崩溃过滤器** — TQQQ 单日跌≥20% 时转入 IEF，恢复后回归
4. **学术基础扎实** — Glenn 2020 SSRN 论文，非曲线拟合
5. **覆盖多种市场体制** — 2010-2025 包含复苏、波动、修正、COVID、加息、AI rally

## 回测结果

| 指标 | 数值 |
|------|------|
| CAGR | 19.58% |
| 最大回撤 | -28.48% |
| MAR Ratio | 0.69 |
| 总交易数 | 167 |
| 胜率 | 76.05% |
| Profit Factor | 2.71 |
| Sharpe | 0.87 |
| Sortino | 1.42 |

## 策略弱点

- 滞胀环境：股债同时下跌，负相关性失效
- 多年震荡市：beta slippage 无法完全抵消
- 跳空风险：日内暴跌30%但收盘仅跌18%，过滤器不触发
- 资金门槛：至少 $50K-$100K

## 相关实体

- [[SetupAlpha]]
- [[Dr. Lewis A. Glenn]]

## 相关概念

- [[Beta Slippage]]
- [[Leveraged ETF]]
- [[Portfolio Rebalancing]]
- [[Crash Filter]]
- [[Negative Correlation Hedging]]

## 原始资料

- [[setup4alpha-leveraged-etf-strategy]] (raw/articles/)
