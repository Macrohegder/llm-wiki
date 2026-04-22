---
id: session-high-retest-intraday-strategy
title: "Session High Retest: A Quantitative Intraday Strategy Across 10 Futures Markets"
source: "Delphic Alpha"
url: https://open.substack.com/pub/delphicalpha/p/session-high-retest-a-quantitative
date: "2026-04-22"
tags:
  - strategy/intraday
  - strategy/breakout
  - strategy/mean-reversion
  - asset/futures
  - topic/backtesting
  - topic/market-microstructure
rating: green
status: deep-processed
---

# Session High Retest: 量化日内策略（10 期货市场，17 年数据）

> 来源: [Delphic Alpha](https://open.substack.com/pub/delphicalpha/p/session-high-retest-a-quantitative) | 摄入日期: 2026-04-22 | 评级: 🟢 Green

## 一句话摘要

日内交易者熟悉的经典设定：开盘涨、回撤、回测高点。但大多数人从未测试哪种版本真正有效。本文在 10 个期货品种上测试了 16 种配置，发现**回撤深度是关键筛选器**，且不同品种的最优过滤器存在明确分裂。

---

## 策略架构

### 四阶段开发流程

```
Rally → Pullback → Retest → Entry & Hold
```

| 阶段 | 说明 | 具体规则 |
|------|------|----------|
| **Rally** | 开盘后价格上涨 | 至少超过 RTH Open 75–150 bps |
| **Pullback** | 从当日高点回撤 | 至少回撤 10 bps |
| **Retest** | 价格回到高点附近 | 回到离 session high 10 bps 范围内 |
| **Entry** | 长仅入场 | 在 retest bar 收盘价做多，持有至 RTH close |

- **Long-only** 策略，不做空
- **无止损** （实盘建议加突发性止损防止跳空风险）

### 回撤深度过滤器（核心发现）

测试了四种过滤器，发现**品种分裂**：

**Shallow pullback (≤ 38.2% Fibonacci retracement) 最适合:**
- NQ (Nasdaq), PL (铂金), HG (铜), SI (白银), GC (黄金), PA (钯金)
- 大多数是金属 + 纳斯达克
- 浅度回撤表明需求强劲，突破后继续性高

**Deep pullback (≥ 50% retracement) 最适合:**
- FDAX (DAX), NKD (日经), ES (S&P 500), YM (道琼斯)
- 均为股票指数（除 NQ 外）
- 深度回撤后的 V-recovery 证明买盘是真实的，而非追涨

> NQ 行为像"金属"，反映其集中度（大型科技股）——机构买家要买纳斯达克时更激进，不等深回撤。

---

## 各品种最优配置

| 品种 | Rally 阈值 | 过滤器 | Sharpe | 交易次数 | 胜率 | bps/笔 |
|-------|-----------|--------|--------|--------|------|--------|
| **FDAX** | 150 bps | deep | **+4.56** | 46 | 67.4% | 56.0 |
| **NQ** | 75 bps | shallow | +2.24 | 830 | 56.9% | 7.8 |
| **PL** | 75 bps | shallow | +2.50 | 395 | 56.5% | ~ |
| **GC** | 150 bps | shallow | +2.46 | 104 | 48.1% | 4.6 |
| **NKD** | 125 bps | deep | +2.40 | 56 | 64.3% | ~ |
| **HG** | 125 bps | shallow | +1.98 | 355 | 51.3% | ~ |
| **YM** | 125 bps | deep | +1.85 | 74 | 59.5% | ~ |
| **ES** | 125 bps | deep | +1.80 | 95 | 58.9% | ~ |
| **SI** | 100 bps | shallow | +1.05 | 354 | 50.8% | ~ |
| **PA** | 75 bps | shallow | +0.91 | 312 | 52.9% | ~ |

### 组合级数据（每品种最优配置）
- **Portfolio Sharpe (long-only):** 1.15
- **Annual Return:** +13.6%
- **Annual Volatility:** 11.8%
- **Max Drawdown:** -16.2%
- **Win Rate:** 54.6%

### Expansion Rate (回测后创新高概率)
- **ES:** 97.9% | **NKD:** 96.4% | **FDAX:** 95.7% — 深回撤后几乎必定突破
- **NQ:** 89.4% — 浅回撤后仍高
- 金属: 77–87% — 较低但频率补偿

---

## 完整规则步骤

```python
# 伪代码框架
for bar in 5min_bars_during_RTH:
    if not rally_confirmed:
        if price >= open * (1 + rally_threshold):
            rally_confirmed = True
            session_high = price
            rally_low = price  # 跟踪上涨幕后最低点
    else:
        session_high = max(session_high, price)
        
        # 检测 pullback
        if price <= session_high * (1 - 0.0010):  # 至少 10 bps 回撤
            pullback_bottomed = check_next_bar_higher_low(bar)
            if pullback_bottomed:
                pullback_depth = (session_high - pullback_low) / (session_high - open)
                
                # 应用品种特定过滤器
                if instrument in [NQ, PL, HG, SI, GC, PA]:
                    if pullback_depth <= 0.382:  # shallow
                        valid_signal = True
                elif instrument in [FDAX, NKD, ES, YM]:
                    if pullback_depth >= 0.50:   # deep
                        valid_signal = True
        
        # 检测 retest
        if valid_signal and price >= session_high * (1 - 0.0010):
            entry_price = bar.close
            hold_until_rth_close()
```

### 具体步骤
1. 加载 5 分钟 K 线，限定 Regular Trading Hours
2. 记录 RTH Open 价格
3. 跟踪运行 session high
4. 等待超过 rally threshold（75–150 bps）
5. 等待至少 10 bps 回撤，确认回撤已触底（下一根 bar 的 Low 高于 pullback Low）
6. 应用品种特定过滤器（见上表）
7. 监控 retest：价格回到离 session high 10 bps 范围内
8. 在 retest bar 收盘价做多
9. 持有至 RTH close，无止损

---

## 为什么有效？

**原始信号几乎无用**: 无过滤器时 Sharpe 仅 0.21，几乎噪音。大多数尝试此设定后放弃的交易者都是在交易未过滤的版本。

**回撤深度过滤器的微观结构意义**:
- **浅回撤 (金属/NQ)**：需求强劲，买盘立即接力。回测只是突破前的确认。
- **深回撤 (股指)**：价格需要探索下方、在支撑位找到真正买盘。V-recovery 证明买盘是真实的，而非追涨动能。

---

## 局限与风险

1. **无止损** — 日内回撤可能很大，特别是金属。实盘建议加突发性止损防止跳空风险。
2. **Long-only** — 仅捕捉上行延续。下行方向的 session low retest 是待测试的镜像策略。
3. **未含交易成本** — bps/笔从 4.6 (GC) 到 56 (FDAX)，大多数品种足以覆盖零售期货佣金。
4. **样本内选参数** — grid scan 寻找最优参数引入了 look-ahead bias。walk-forward 验证可能降低 Sharpe 20–40%。
5. **单一策略** — 应作为日内策略组合的一部分，而非单独使用。

---

## 可复现性

- **数据**: FRD 连续比仸期货，5 分钟线，2008–2025
- **品种**: GC, SI, HG, PL, PA, ES, NQ, FDAX, NKD, YM
- **复现难度**: 中等。规则清晰，但需要 5 分钟 RTH 数据和当日开盘价。
- **建议优先复现**: FDAX (deep, 150 bps) 或 NQ (shallow, 75 bps)

---

## 评价

| 指标 | 评分 | 备注 |
|--------|-------|-------|
| 数据质量 | ⭐⭐⭐⭐⭐ | 17 年、10 品种、5 分钟级别，直接透明 |
| 规则完整性 | ⭐⭐⭐⭐⭐ | 每个参数都已说明，包括品种特定过滤器 |
| 可操作性 | ⭐⭐⭐⭐☆ | 规则极简，但需要实时监控多个品种 |
| 风险透明度 | ⭐⭐⭐⭐☆ | 明确讨论了无止损、look-ahead bias、交易成本 |
| 新题性 | ⭐⭐⭐⭐☆ | 常见设定的量化验证，品种分裂是亮点 |

**总体**: 🟢 **Green** — 规则完整、数据充分、实现简单、风险透明，是目前知识库中最完整的日内策略。

---

## 相关链接
- 原文: https://open.substack.com/pub/delphicalpha/p/session-high-retest-a-quantitative
- 系列: Day Trading Playbook #1（后续还有 Opening Dip Buy 等）
- 原文备份: raw/articles/2026-04-22-session-high-retest-a-quantitative-intraday-strategy-across-10-futures-markets.md
