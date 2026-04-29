---
id: 2025-11-04-tradable-futures-portfolio
title: "How I Create a Tradable Futures Portfolio"
source: "Algorithmicguys (TraderDunn/Eric)"
url: https://algorithmicguys.substack.com/p/how-i-create-a-tradable-futures-portfolio
published: 2025-11-04
saved_at: 2026-04-29
tags: [futures, portfolio, diversification, live-trading, monte-carlo, mean-reversion, breakout, incubation]
---

# How I Create a Tradable Futures Portfolio

**来源**: Algorithmicguys Substack — TraderDunn (Eric)  
**日期**: 2025-11-04  
**标签**: #futures #portfolio #diversification #live-trading #monte-carlo

## 一句话摘要

作者公开其个人实盘交易的12策略期货组合构建方法论——仅用 incubation/live 数据、严控同时持仓≤4市场、追求负相关性分散化，并用 Monte Carlo 验证组合鲁棒性。

## 关键要点

1. **实盘数据优先**: 所有绩效数据来自 incubation 和 live trading，**明确排除回测**——作者认为没亲眼看到的成交不算数
2. **12策略/4市场/1手**: 小资金 ($60K) 模板，峰值敞口4手合约
3. **Profit/MaxDD = 15**: 组合级风险收益比目标
4. **Monte Carlo 验证**: 1,000+次重排，5th percentile 仍高于盈亏平衡
5. **策略类型混合**: 均值回归 + 突破 + 季节性 + 混合，部分市场同时运行多空
6. **保留亏损策略**: KW 和 MNQ 在 incubation 阶段亏损，但为分散化保留

## 组合构成

| 类别 | 品种 | 策略数 | 类型 |
|------|------|--------|------|
| 指数 | MES | 5 (4多1空) | MR/BO/Hybrid |
| 指数 | MNQ | 1 | MR |
| 谷物 | Wheat, Soybeans, KW | 3 | MR/BO/SEAS |
| 牲畜 | Live Cattle | 1 | MR |
| 金属 | Micro Gold | 1 | MR |
| Crypto | Micro BTC | 2 | BO |

## 改进方向（作者自述）

- 加入能源 (CL/NG)
- 加入金属多头 (Gold/Silver)
- MNQ 增加空头模型
- 增加日内策略（当前 8/12 是日线）
- 扩大资金到 $100K+

## 相关实体

- [[Algorithmicguys]]
- [[TraderDunn]]
- [[Portfolio Analyst]] (trademaid.info)

## 相关概念

- [[Portfolio Diversification]]
- [[Monte Carlo Simulation]]
- [[Incubation Testing]]
- [[Mean Reversion]]
- [[Breakout Strategy]]
- [[Seasonal Trading]]

## 原始资料

- [[algorithmicguys-tradable-futures-portfolio]] (raw/articles/)
