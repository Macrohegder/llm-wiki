# Why Is the WTIOIL Contract on Hyperliquid Paying -400% Funding?

**Source**: [Trading Research Hub](https://www.tradingresearchub.com/p/why-is-the-wtioil-contract-on-hyperliquid)
**Author**: pedma
**Date**: 2026-04-09
**Tags**: #funding-rate #commodity-perp #contract-roll #backwardation #hyperliquid

## One-Sentence Summary

Hyperliquid 的 WTIOIL 永续合约在合约滚动 (roll) 期间支付 -400% 资金费率，是因为跟踪的 front-month 期货正处于 backwardation，perp 价格被动折价向下个月份靠拢——这种"粘性折价"导致巨大的负资金费率。

## Core Mechanism

### 1. 跟踪目标与合约滚动

- HL 的 WTIOIL-USDC 跟踪 CME 的 front-month WTI 期货（目前是 CLK6 = 5 月合约）
- 每个月 8-14 日进行合约滚动 (roll)，从当前月份滚到下一个月份
- 滚动后将跟踪 CLM6 (6 月合约，约 $86.56)

### 2. Backwardation 的影响

- 当前市场处于 **backwardation**：近月价格 (~$93.36) > 远月价格 (~$86.56)
- 这意味着 perp 合约在滚动期间会"自动打折"——每天向 6 月合约价格靠拢
- 这种打折是 **确定性价格移动**，不是随机波动

### 3. 资金费率的来源

- 负资金费率 (-400% 年化 ≈ -1.1%/天) 是对多头持有者的补偿
- 补偿的是 perp 价格相对于现货/期货的"粘性折价"
- 如果资金费率不存在，多头可以免费收取这个确定性打折，形成无风险套利

### 4. 为什么套利不可行

| 项目 | 数值 |
|------|------|
| Short HL perp @ | $93.36 |
| Long CLM6 @ | $86.56 |
| Basis 收益 | ~$6.8/桶 |
| Funding 成本 (6.5 天) | ~$7.25/桶 |
| **净收益** | **≈ 0** |

- Basis 收益刚好被 funding 成本吃掉
- 加上手续费和市场冲击，实际为负收益

## Why Cross-Exchange Spread Exists

### 对于 OKX vs HL 的 CL 合约价差：

1. **Oracle 设计不同**
   - HL: 跟踪 CME front-month 期货，每月 roll，在 backwardation 时会产生粘性折价
   - OKX: 通常跟踪自己的指数/指标组合，roll 机制可能不同

2. **Roll 时间窗口不同**
   - 不同交易所的 roll 日期可能存在几天差异
   - 在这几天里，两边的合约跟踪的是不同月份的期货
   - 导致价格和 funding 率出现持续差异

3. **持仓结构差异**
   - HL: 散户为主，对冲基金/机构参与度较低
   - OKX: 机构参与度更高，对冲行为更成熟
   - 持仓不平衡导致 funding 率持续偏离零值

4. **流动性差异**
   - CL 在加密货币交易所的流动性远低于传统期货市场
   - 小规模流量就能放大 funding 偏差
   - 套利者的资金不足以平活这种偏差

## Key Takeaway

> 这不是市场失效，而是机制设计的必然结果。CL 永续合约在滚动期间的资金费率差异，反映的是 front-month 期货向 back-month 靠拢的确定性价格移动，而非无风险套利机会。

## Related
- [[Funding Rate Arbitrage]]
- [[Contract Roll]]
- [[Backwardation]]
- [[Cross-Exchange Arbitrage]]
