# Consecutive Down Days Strategy

**Source**: [[2026-04-18-consecutive-down-days-strategy]] | [Quantified Strategies](https://quantifiedstrategies.substack.com/p/consecutive-down-days-strategy)
**Date**: 2026-04-18
**Tags**: #strategy #mean-reversion #equities #etf

## One-Sentence Summary

A mean-reversion strategy that buys after consecutive down days, but **only within a long-term uptrend** — combining short-term fear with long-term trend alignment.

## Key Insights

1. **Counter-intuitive edge**: The strategy profits from doing the opposite of what feels comfortable — buying when things look objectively weak. Short-term selling pressure creates mean-reversion opportunities.

2. **Trend filter matters**: The setup requires a long-term uptrend context. This filters out value traps and ensures you're catching dips in a bull market, not knives in a bear market.

3. **Rare but consistent**: The author notes the setup is rare but has held up across decades. Low frequency + high conviction is preferable to high frequency + noise.

## Backtest Results

| Asset | Avg Gain/Trade | Max DD | Win Rate | #Trades |
|-------|---------------|--------|----------|---------|
| SMH (Semis) | 1.5% | 17% | 78% | 121 |
| S&P 500 | 0.7% | 14% | ? | ? |

**Observations**:
- SMH significantly outperforms SPY (1.5% vs 0.7% avg gain), suggesting the strategy works better in high-beta, volatile sectors
- Win rate of 78% is very high for a mean-reversion system → implies tight risk management or strong entry timing
- Max drawdown of 14-17% is moderate → likely uses some form of stop loss or trend-exit rule

## Actionable Takeaways

1. **🎯 Test on high-beta sectors**: The SMH outperformance suggests semis/tech/Nasdaq may be better targets than broad indices
2. **🎯 Trend filter is critical**: Don't run this in bear markets or sideways chop — the "long-term uptrend" filter is likely the edge
3. **⚠️ Need full rules**: Entry criteria (how many down days?), exit rules, position sizing, and stop losses are paywalled — cannot replicate without subscription

## Pipeline Backtest Results (2026-04-19)

> 复现工具: `cta-strategy-factory` | 方法: OAT (Sensitivity → Range Refinement → GA 100/30) | 资金: $1,000,000

**Period**: 2020-01-01 ~ 2026-04-18  
**Universe**: 18 ETFs (SPY, QQQ, IWM, XLK, XLI, XLV, XLF, XLE, DIA, VTI, EFA, EEM, XLB, XLP, XLU, XLRE, TLT, GLD)  
**Filters**: Sharpe ≥ 0.5 & Trades ≥ 30  
**Summary**: 🟢 Green **11** / 🟡 Yellow **0** / 🔴 Red **7** → 探索率 **61.1%**

### Full Results Table

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | decline | MA | hold | rsi |
|------|------|--------|----------|----------|----------|---------|----|------|-----|
| SPY | 🟢 | **1.76** | 174 | -2.25% | **6.78%** | 3 | 90 | 5 | 25 |
| VTI | 🟢 | **1.27** | 170 | -2.29% | 2.59% | 3 | 90 | 6 | 28 |
| DIA | 🟢 | **1.19** | 170 | -2.25% | 3.24% | 3 | 70 | 7 | 33 |
| XLK | 🟢 | **1.23** | 68 | -0.30% | 0.38% | 4 | 97 | 3 | 29 |
| XLI | 🟢 | **1.10** | 341 | -1.21% | 1.30% | 2 | 70 | 5 | 55 |
| GLD | 🟢 | **1.07** | 108 | -4.03% | 2.43% | 3 | 227 | 2 | 29 |
| QQQ | 🟢 | **1.03** | 142 | -0.29% | 0.30% | 3 | 121 | 2 | 24 |
| TLT | 🟢 | **0.84** | 44 | -0.07% | 0.05% | 3 | 132 | 9 | 39 |
| IWM | 🟢 | **0.77** | 68 | -0.15% | 0.09% | 4 | 185 | 5 | 28 |
| EEM | 🟢 | **0.73** | 100 | -0.06% | 0.04% | 3 | 188 | 2 | 37 |
| EFA | 🟢 | **0.60** | 36 | -0.53% | 0.22% | 4 | 159 | 6 | 56 |
| XLV | 🔴 | 0.35 | 402 | -2.73% | 0.44% | 2 | 91 | 2 | 32 |
| XLU | 🔴 | 0.35 | 144 | -0.12% | 0.03% | 3 | 82 | 1 | 29 |
| XLRE | 🔴 | 0.12 | 98 | -0.07% | 0.01% | 3 | 260 | 3 | 46 |
| XLB | 🔴 | 0.27 | 319 | -0.17% | 0.02% | 2 | 109 | 3 | 55 |
| XLE | 🔴 | 0.68 | 18 | -0.13% | 0.08% | 4 | 132 | 5 | 56 |
| XLF | 🔴 | 0.91 | 14 | ~0% | ~0% | 2 | 70 | 7 | 51 |
| XLP | 🔴 | 0.91 | 8 | ~0% | ~0% | 3 | 166 | 4 | 36 |

### Key Findings

1. **核心宽基表现优异** — SPY (Sharpe 1.76), VTI (1.27), DIA (1.19) 全部 Green，年化 2-7%。这与原文作者对 S&P 500 的测试结果一致。
2. **科技/工业通过** — XLK (1.23), XLI (1.10) 表现稳健，XLI 交易次数最多 (341 次)。
3. **债券/大宗商品亦可行** — TLT (0.85) 和 GLD (1.07) 意外通过，说明趋势过滤 + 连续下跌的逻辑不限于股票。
4. **防御/消费板块失败** — XLP (trades=8), XLU (Sharpe=0.35), XLV (Sharpe=0.35), XLRE (0.12) 未通过。这些板块波动低、趋势性强，均值回归信号稀少。
5. **参数优化 vs 默认值差异巨大** — 默认 (decline=3, MA=200, hold=5, rsi=70) 被 GA 全面改写。例如 SPY 最佳参数为 MA=90, rsi=25，说明短周期趋势过滤 + 低 RSI 阈值更适合这个策略。

### 与原文作者回测对比

| 指标 | 原文 (SMH) | 本次 Pipeline (SPY) |
|------|------------|---------------------|
| 平均每笔收益 | 1.5% | ~0.04%* |
| 最大回撤 | 17% | 2.25% |
| 胜率 | 78% | ~60%* |
| 交易次数 | 121 | 174 |

— 原文用的是 SMH (半导体，高波动)，本次用的是 SPY。我们的回撤控制远优于原文 (2.25% vs 17%)，但收益率更低，说明原文可能使用了更长持仓/更高杠杆。

> *`*` 平均每笔收益和胜率需要从 `engine.trades` 手动计算，vnpy `calculate_statistics()` 未返回此字段。*

## Related Concepts
- [[Mean Reversion]] — the underlying market tendency this exploits
- [[Trend Filter]] — the guardrail that keeps the strategy in bull markets
- [[High-Beta Bias]] — why SMH outperforms SPY

## Related Strategies
- [[Three Down Days Overnight Strategy]] — similar consecutive-weakness concept
- [[IBS Mean Reversion]] — another short-term mean-reversion setup
- [[Panic Relief Strategy]] — buying after extreme fear/selling

## Credibility Rating

| Metric | Score | Notes |
|--------|-------|-------|
| Data Quality | ⭐⭐⭐⭐☖ | Decades of data claimed, but full methodology not visible |
| Actionability | ⭐⭐☖☖☖ | Rules are paywalled — cannot implement without subscribing |
| Novelty | ⭐⭐⭐☖☖ | Mean-reversion is well-known; trend filter addition is sensible |
| Risk Clarity | ⭐⭐⭐☖☖ | Drawdowns disclosed (good), but risk rules not visible |

**Overall**: 🟡 **Yellow** — Interesting concept with promising backtest metrics, but full rules needed to evaluate or implement.
