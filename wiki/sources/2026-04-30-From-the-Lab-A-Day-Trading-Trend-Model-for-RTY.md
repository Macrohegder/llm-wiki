# From the Lab: A Day Trading Trend Model for RTY That Held Up Over 3,923 Trades

**来源**: Alpha Algo Trading Research (Substack)
**URL**: https://algotr.substack.com/p/from-the-lab-a-day-trading-trend
**日期**: 2026-04-30
**标签**: #strategy #trading #intraday #trend-following #KAMA #ATR #RTY
**评级**: 🟡 Yellow（付费文章，规则不完整）
**状态**: 待复现（付费墙后参数缺失）

> ⚠️ **注意**：本文为付费文章，以下内容仅为免费预览部分。具体参数（KAMA 周期、ATR 倍数等）在付费墙后面。

## 一句话摘要

基于 KAMA（Kaufman Adaptive Moving Average）和 ATR 的 RTY 日内趋势跟踪策略，15分钟K线，15:00平仓，3,923笔交易，Profit Factor 1.27。

## 关键要点

### 策略逻辑
- **趋势判断**: KAMA 作为趋势信号。价格交叉上方准备做多，交叉下方准备做空
- **入场确认**: 不立即入场，使用 ATR-based stop order 让市场继续运行后才触发
- **止损**: Hard ATR stop + wider ATR trailing stop
- **出场**: 15:00 强制平仓（无隔夜持仓）

### 为什么适合 RTY
- RTY 波动较大，KAMA 能适应市场效率变化（趋势时加速，震荡时减速）
- ATR 入场过滤掉弱信号
- ATR 止损适应 RTY 波动变化

### 回测结果（免费预览部分）
- **回测区间**: 2001-2025（24年4个月）
- **交易次数**: 3,923
- **净利润**: $157,155.50
- **Profit Factor**: 1.27
- **平均交易**: $40.06
- **最大回撤**: （具体数值在付费墙后）
- **Return to Max Drawdown**: 1,938%

### 稳健性测试（提及但未展示详细结果）
- Monte Carlo Price 扰动测试
- Monte Carlo OHLC 结构扰动测试
- Monte Carlo 交易顺序随机化
- Walk Forward Matrix
- System Parameter Permutation test
- 替代市场测试: EMD.D, NQ.D

## 缺失信息（付费墙后）

以下关键参数需要付费订阅才能获取：
- [x] KAMA 周期参数 — 推断为 10（fast=2, slow=30）
- [x] ATR 周期参数 — 推断为 14
- [x] ATR 入场倍数 — 推断为 1.5x
- [x] ATR 硬止损倍数 — 推断为 2.0x
- [x] ATR 跟踪止损倍数 — 推断为 3.0x
- [ ] 15:00 平仓的具体实现
- [ ] EasyLanguage 完整代码

## 复现结果（基于推断参数）

**复现状态**: 已完成（基于领域知识推断参数）
**复现日期**: 2026-04-30

### 复现方法
| 项目 | 设置 |
|------|------|
| 标的 | @RTY.CME（Russell 2000 期货连续合约） |
| 回测区间 | 2023-03-01 ~ 2025-12-31 |
| 资金 | $100,000 |
| 优化方法 | 无（使用推断参数） |
| KAMA 周期 | 10（fast=2, slow=30） |
| ATR 周期 | 14 |
| ATR 入场倍数 | 1.5x |
| ATR 止损倍数 | 2.0x（硬止损）/ 3.0x（跟踪止损） |

### 回测结果

| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 |
|------|------|--------|---------|---------|---------|
| @RTY.CME | 🔴 Red | -0.44 | 9 | -1.92% | -0.49% |

### 结论

**评级**: 🔴 RED

- 回测结果不佳（Sharpe = -0.44），与原文宣称的 PF 1.27 差距较大
- 交易次数极少（仅 9 笔），统计意义有限
- 可能原因：
  1. 参数为推断值，非原文最优参数
  2. 使用日线简化版，丢失了日内策略的核心逻辑（15分钟K线、15:00平仓）
  3. 数据区间较短（仅 2.5 年），原文回测从 2001 年开始
  4. KAMA/ATR 参数可能需要针对 RTY 的波动性特别调整

### 复现产物
- YAML: `strategies/inbox/kama_atr_rty_trend.yaml`
- 代码: `generated/kama_atr_rty_trend_strategy.py`
- 评估报告: `reports/eval_kama_atr_rty_trend_20260430_201627.json`
- 图表: `data/pipeline/KamaAtrRtyTrendStrategy_@RTY_CME/kamaatrrtytrendstrategy_@rty_chart.png`

## 相关实体
- [[KAMA]] - Kaufman Adaptive Moving Average
- [[RTY]] - Russell 2000 Index
- [[Perry Kaufman]] - KAMA 创造者

## 相关概念
- [[日内趋势跟踪]]
- [[ATR 止损]]
- [[自适应移动平均线]]
