---
id: algorithmicguys-tradable-futures-portfolio
title: "How I Create a Tradable Futures Portfolio"
source: "Algorithmicguys (TraderDunn/Eric)"
url: https://algorithmicguys.substack.com/p/how-i-create-a-tradable-futures-portfolio
published: 2025-11-04
saved_at: 2026-04-29
tags: [futures, portfolio, diversification, live-trading, monte-carlo, mean-reversion, breakout]
---

# How I Create a Tradable Futures Portfolio

> 作者: TraderDunn (Eric) @ Algorithmicguys  
> 发布时间: 2025-11-04  
> 来源: https://algorithmicguys.substack.com/p/how-i-create-a-tradable-futures-portfolio

---

## 核心摘要

作者构建了一个 **12策略期货组合**，实盘交易，最大同时持仓4个市场，每个策略1手合约。所有数据来自 incubation 和 live trading 阶段，**排除了回测部分**（因为作者认为没看到实盘成交就不算数）。

---

## 组合约束条件

| 约束 | 设定 |
|------|------|
| **资金** | ~$60,000 USD |
| **目标** | 平滑权益曲线，最小化负相关性 |
| **风险限制** | 日内回撤可控；同时交易不超过4-5个策略 |
| **多样性** | 尽可能多配置商品（非指数）品种 |

---

## 组合构成 (12个系统)

**品种分布:**
- **指数**: MES(5策略, 4多1空), MNQ
- **商品**: Wheat, Soybeans, Live Cattle
- **金属**: Micro Gold
- ** crypto**: Micro BTC (2策略)
- **谷物**: KW (Kansas Wheat)

**策略类型:**
- MR = Mean Reversion (均值回归)
- BO = Breakout (突破)
- Hybrid = MR + BO 混合
- S = Short (空头)
- SEAS = Seasonal (季节性)

> 注: KW 和 MNQ 在 incubation/live 阶段是亏损的，但作者保留它们用于分散化。

---

## 关键绩效指标

| 指标 | 数值/特征 |
|------|-----------|
| 峰值敞口 | 4手合约 |
| Profit / Max DD | **15** |
| 月度收益 | 以绿色月份为主，红色月份可控 |
| 相关性 | 大多数策略对呈中性或负相关 |

---

## Monte Carlo 分析

- **黑线**: 实盘权益曲线
- **红线**: 5th percentile (1,000+次重排的最差路径)
- **蓝线**: 95th percentile (最佳路径)

**结论**: 即使最差路径也保持在盈亏平衡之上，说明分散化有效，不存在单一策略主导或灾难性路径风险。

---

## 作者做得对的事

1. **只用实盘数据** (incubation + live)，不用回测
2. **强市场分散化**: 指数、谷物、金属、crypto
3. **策略类型平衡**: 突破 + 均值回归混合，部分市场同时运行多空策略

---

## 作者计划改进的方向

| 改进方向 | 说明 |
|----------|------|
| 月度跟踪 | 记录每个系统对月度收益的贡献 |
| 加入能源 | 在 CL/NG 上添加突破和均值回归策略 |
| 加入金属多头 | Gold/Silver 提供强分散化效益 |
| MNQ 空头偏差 | 当前 Nasdaq 系统偏多头，需加空头模型 |
| 加入长期趋势系统 | 整合 swing/weekly 系统稳定跨周期表现 |
| 增加日内分散化 | 当前 8/12 策略是日线/1440分钟，需更多日内策略 |
| 扩大资金规模 | 至少 $100K，改善资金效率，允许更大合约 |

---

## 工具

- **Portfolio Analyst** (TradeStation 配套软件): https://trademaid.info/pa.html
  - 非 affiliat 推荐

---

## 付费策略列表 (截至发文)

1. 2 ES Seasonal for Q4
2. NQ 30 Minute (intraday)
3. Orange Juice Daily
4. Silver 364 min (intraday)
5. ES.D 3Day OR one 1 prof close
6. KC 65 min

---

## 对 Raymond 的启示

1. **实盘数据优先**: 作者明确排除回测，只用 incubation/live 数据 — 这与 cta_developer 的 "先 OAT 后 GA 再 incubation" 流程一致
2. **12策略/4市场/1手**: 小资金 ($60K) 的分散化模板，可直接参考用于我们的 ETF/期货组合
3. **Profit/MaxDD = 15**: 可作为组合筛选标准
4. **Monte Carlo 验证**: 建议对 cta_developer 的 batch pipeline 结果也做 MC 分析
5. **日内策略缺口**: 我们目前以日线为主，可考虑增加日内策略提升分散化
