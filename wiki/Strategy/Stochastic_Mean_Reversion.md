# Stochastic Mean-Reversion Strategy (随机均值回归策略)

## 1. 策略概述

基于随机指标（Stochastic Oscillator）的均值回归策略，核心思想是在趋势方向上的超卖/超买区域寻找反转机会。

**来源**: Substack 文章 "The Stochastic Mean-Reversion Strategy" by Quantified Strategies

---

## 2. 核心规则

### 2.1 入场条件

| 方向 | 条件 |
|------|------|
| **做多 (Long)** | 1. %K < 30（超卖区）<br>2. %K 上穿 %D（金叉）<br>3. 收盘价 > 50日均线（趋势向上） |
| **做空 (Short)** | 1. %K > 80（超买区）<br>2. %K 下穿 %D（死叉）<br>3. 收盘价 < 50日均线（趋势向下） |

### 2.2 出场条件

| 类型 | 规则 |
|------|------|
| **固定止损** | 入场价 ± 1.5% |
| **移动止盈** | ATR(14) × 2.0  trailing stop |

### 2.3 参数设置

| 参数 | 值 | 说明 |
|------|-----|------|
| Stochastic K | 14 | 计算周期 |
| Stochastic D | 3 | %D 平滑周期 |
| Stochastic Smooth | 3 | %K 平滑周期 |
| 超卖阈值 | 30 | 做多触发区 |
| 超买阈值 | 80 | 做空触发区 |
| ATR 周期 | 14 | 波动率计算 |
| 趋势均线 | 50 | 趋势过滤器 |
| 固定止损 | 1.5% | 硬止损 |
| 移动止盈 ATR 倍数 | 2.0 | 动态止盈 |
| 单笔风险 | 1% | 仓位管理 |

---

## 3. 回测结果

### 3.1 测试标的
- **品种**: GC (Gold Futures) - COMEX 黄金期货
- **周期**: 日线 (1D)
- **数据区间**: 2022-06 至 2026-04
- **初始资金**: $20,000

### 3.2 绩效指标

| 指标 | 数值 |
|------|------|
| 总收益率 | **+65.22%** |
| CAGR | **13.78%** |
| 最大回撤 | **-2.00%** |
| MAR 比率 | **6.87** |
| 交易次数 | **24 笔** |
| 胜率 | **54.17%** |
| 盈亏比 | **8.59** |
| 最终权益 | **$33,043** |

### 3.3 权益曲线

![Stochastic Mean-Reversion GC Equity Curve](Stochastic_Mean_Reversion_GC_equity.png)

> 上图：绿色曲线为权益曲线，红色区域为回撤。策略在约4年时间内实现稳健增长，回撤控制极为出色（最大仅2%）。

---

## 4. 策略特点分析

### 4.1 优势
- ✅ **回撤极低**: 最大回撤仅2%，风险可控
- ✅ **盈亏比高**: 8.59，盈利单笔远大于亏损单笔
- ✅ **MAR优秀**: 6.87，收益/风险比出色
- ✅ **趋势过滤**: 50日均线过滤避免逆势交易

### 4.2 劣势与风险
- ⚠️ **交易频率低**: 4年仅24笔，样本量偏小
- ⚠️ **依赖趋势环境**: 震荡市可能频繁止损
- ⚠️ **参数敏感**: Stochastic阈值（30/80）和ATR倍数需适配品种
- ⚠️ **未考虑滑点/佣金**: 回测为理想条件，实盘需额外成本缓冲

### 4.3 适用场景
- 趋势明确的商品期货（黄金、原油等）
- 中等波动率环境
- 日线级别波段交易

---

## 5. 改进方向

| 方向 | 思路 |
|------|------|
| **多品种测试** | 扩展至 CL、NG、ES 等期货 |
| **参数优化** | 对 Stochastic阈值、ATR倍数进行 walk-forward 优化 |
| **仓位动态** | 根据波动率调整仓位（Volatility Targeting） |
| **组合配置** | 与趋势策略组合，降低整体回撤 |

---

## 6. 相关文件

| 文件 | 路径 |
|------|------|
| 权益曲线数据 | `/root/.openclaw/workspace/cta_developer/stoch_gold_equity.csv` |
| 权益曲线图表 | `/root/.openclaw/workspace/cta_developer/stoch_gold_equity.png` |
| 回测脚本 | `/root/.openclaw/workspace/cta_developer/save_equity.py` |

---

## 7. 标签

#strategy #mean-reversion #stochastic #gold #futures #backtest #cta #momentum

---

*Created: 2026-04-24*
