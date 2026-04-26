# Fade Breakout 5-Bar Strategy — 复现报告

**来源**: [[2024-11-24_fade_breakout_strategy_quantifiedstrategies]]
**复现日期**: 2026-04-27
**状态**: ✅ 已复现

## 策略核心

30分钟K线，前5根bar的最高/最低作为区间。前一根bar的收盘价突破区间上沿→做空（fade breakout），突破下沿→做多（fade breakdown），否则空仓。持仓仅1根bar，开盘进、下一根开盘出。

## 回测图表（Top 5 Positive Sharpe）

| 品种 | 图表 |
|------|------|
| SI (白银) | ![SI Equity Curve](../raw/assets/fade_breakout_5bar_SI.png) |
| NQ (纳斯达克) | ![NQ Equity Curve](../raw/assets/fade_breakout_5bar_NQ.png) |
| ES (标普) | ![ES Equity Curve](../raw/assets/fade_breakout_5bar_ES.png) |
| GC (黄金) | ![GC Equity Curve](../raw/assets/fade_breakout_5bar_GC.png) |
| ZN (10Y国债) | ![ZN Equity Curve](../raw/assets/fade_breakout_5bar_ZN.png) |

## 回测结果（10品种，22个月数据）

| 品种 | 交易次数 | Sharpe | 回报% | 最大回撤% | 状态 |
|------|---------|--------|------|----------|------|
| **SI (白银)** | 1,719 | **3.550** | 0.15 | -0.02 | ✅ 正 |
| **NQ (纳斯达克)** | 20 | **2.448** | 0.12 | -0.01 | ✅ 正 |
| **ES (标普)** | 111 | **2.230** | 0.05 | -0.02 | ✅ 正 |
| **GC (黄金)** | 1,119 | **1.332** | 1.15 | -0.47 | ✅ 正 |
| **ZN (10Y国债)** | 739 | **1.219** | ~0 | ~0 | ✅ 正 |
| CL (原油) | 244 | -0.988 | ~0 | ~0 | ❌ 负 |
| NG (天然气) | 322 | -0.252 | ~0 | ~0 | ❌ 负 |
| YM (道指) | 110 | -0.353 | -0.11 | -0.40 | ❌ 负 |
| RTY (罗素) | 102 | -1.099 | -0.01 | -0.02 | ❌ 负 |
| ZB (30Y国债) | 528 | -2.230 | -0.01 | -0.02 | ❌ 负 |

**Positive Sharpe: 5/10**

## 与文章一致性

文章结论：Fade Breakout 在商品和债券上有效，在股指上效果差。

- ✅ **商品**：GC (+1.33), SI (+3.55) 强正；CL, NG 负（能源可能需不同参数）
- ⚠️ **债券**：ZN 正、ZB 负，混合
- ⚠️ **股指**：NQ, ES 正；YM, RTY 负 — 与文章"股指无效"部分一致、部分矛盾

## 关键限制

1. **数据仅22个月**（文章是4年）
2. **无成本、无滑点、无杠杆、1手固定仓位** → 绝对回报极低（<1%）
3. **无趋势过滤** — 文章提到加趋势过滤器可能提升表现
4. **单bar持仓** — 可能错过部分反转后的延续

## 代码位置

- 策略：`/root/.openclaw/workspace/strategy_factory/generated/fade_breakout5bar_strategy.py`
- Spec：`/root/.openclaw/workspace/strategy_factory/specs/fade_breakout_5bar.yaml`
- Batch脚本：`/root/.openclaw/workspace/strategy_factory/scripts/batch_fade_breakout.py`

## 后续优化方向

- [ ] 加入交易成本（IB期货佣金 + 滑点）
- [ ] 测试杠杆/仓位管理
- [ ] 加趋势过滤器（如 SMA200）
- [ ] 测试不同 lookback（3, 7, 10 bar）
- [ ] 数据延长后重新回测

## 相关概念

- [[Mean Reversion]] — 均值回归策略家族
- [[Fade Breakout]] — 假突破/假跌破策略类型
- [[BarGenerator]] — vnpy分钟级K线合成
- [[IB Futures Data]] — 数据来源

## 相关实体

- [[QuantifiedStrategies]] — 策略来源网站
