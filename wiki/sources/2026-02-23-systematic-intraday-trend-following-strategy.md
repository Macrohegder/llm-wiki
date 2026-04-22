---
id: systematic-intraday-trend-following-strategy
title: "Systematic Intraday Trend-Following Strategy"
source: "QuantifiedStrategies / Carlo Zarattini (Concretum)"
url: https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following
date: "2026-02-23"
tags:
  - strategy/intraday
  - strategy/trend-following
  - asset/equity
  - topic/backtesting
  - topic/dynamic-boundary
rating: green
status: deep-processed
---

# Systematic Intraday Trend-Following Strategy

> 来源: [QuantifiedStrategies](https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following) / Carlo Zarattini at Concretum | 摄入日期: 2026-02-23 | 评级: 🟢 Green

## 一句话摘要

基于**动态噪音边界**的系统性日内趋势跟踪策略。使用过去 14 天的平均日内波动构建随时间变化的上下边界，价格突破边界时信号产生。核心原理：**强势会在交易日内产生更多强势**。

---

## 策略架构

### 核心组件

| 组件 | 说明 |
|------|------|
| **Dynamic Boundaries** | 交易区间随日内时间变化，基于过去 14 天从开盘价的平均价格移动 |
| **Overnight Gap Adjustment** | 边界根据隔夜跳空调整，反映供需突变 |
| **Entry Signals** | 价格突破上边界→做多；跌破下边界→做空 |
| **Stop Loss** | VWAP 作为保护性止损 |
| **Dynamic Position Sizing** | 根据日内市场波动率调整仓位 |
| **Semi-Hourly Execution** | 仅在每小时整点/半点执行，过滤短期噪音 |

### 动态边界机制

策略的关键创新点在于**噪音阈值是动态的**，随日内时间变化：

- 平均日内波动从开盘价开始随时间增长，通常在 16:00 达峰
- **10:30** 时，跌幅仅需 -0.30% 即可触发信号
- **15:30** 时，需要更大的移动（约 -0.60%）才能触发同样信号
- 这反映了日内波动率的**非均匀分布**：开盘和收盘附近波动率更高，午间更低

### 规则摘要

```
1. 计算过去 14 天每个时间点的平均价格移动（从开盘价起）
2. 根据当日隔夜跳空调整上下边界
3. 每半小时检查一次价格位置
4. 突破上边界 → 开多单
5. 跌破下边界 → 开空单
6. 价格穿越 VWAP → 平仓（止损）
7. 根据当日波动率调整仓位大小
```

---

## 回测结果（SPY）

| 指标 | 数值 | 备注 |
|------|-------|-------|
| 总回报 | +1,985% | 历史期间累计 |
| 年化回报 | 19.6% | 稳定持续 |
| Sharpe Ratio | **1.33** | SPY buy-and-hold 仅 0.45 |
| Beta | 略小于 0 | 市场中性，多样化好处 |
| VIX>40 时 Sharpe | **3.50** | 高波动率环境表现更佳 |
| 仓位管理 | 动态 | 基于日波动率 |

### 关键发现
- **高波动率环境表现更佳**: VIX > 40 时 Sharpe 达 3.50，这与趋势策略通常的特性一致
- **市场中性**: Beta 略小于零，适合作为组合多样化工具
- **参数鲁棒性**: 14 天回看有效，但宽范围的回看长度也产生盈利结果

---

## 复现框架（伪代码）

```python
# 简化版框架
import pandas as pd

# 1. 计算动态边界
def calculate_dynamic_boundaries(df_intraday, lookback=14):
    """
    df_intraday: 5min or 30min bars with 'time_of_day' column
    计算过去 lookback 天每个时间点的平均价格移动（相对于开盘价）
    """
    boundaries = {}
    for t in unique_time_points:
        moves = []
        for day in last_lookback_days:
            open_price = day.open
            price_at_t = day[t].close
            moves.append((price_at_t - open_price) / open_price)
        boundaries[t] = {
            'upper': np.mean(moves) + k * np.std(moves),
            'lower': np.mean(moves) - k * np.std(moves)
        }
    return boundaries

# 2. 隔夜跳空调整
gap = (today_open - yesterday_close) / yesterday_close
adjusted_upper = base_upper + f(gap)
adjusted_lower = base_lower + f(gap)

# 3. 半小时执行
for timestamp in ['10:00', '10:30', '11:00', ..., '15:30']:
    current_price = df.loc[timestamp].close
    if current_price > upper_boundary[timestamp]:
        enter_long()
    elif current_price < lower_boundary[timestamp]:
        enter_short()
    
    # 4. VWAP 止损
    if has_position() and price_crosses_vwap():
        close_position()
    
    # 5. 动态仓位
    position_size = target_risk / (atr * point_value)
```

---

## 局限与风险

1. **未含滑点** — 回测假定信号产生时立即执行，实盘滑点可能显著降低表现
2. **仅 SPY 回测** — 未在其他品种上验证稳健性
3. **佣金假设** — 使用 $0.0035/股（IB 入门级），实际成本可能更高
4. **半小时执行的延迟** — 信号产生后可能需要等待整点/半点才执行，延迟可能消耗 alpha
5. **论文发表后表现** — 论文首发于 2024 夏季，作者声称 out-of-sample 表现持续强劲

---

## 与其他日内策略的对比

| 策略 | 核心机制 | 数据频率 | 止损 | 特点 |
|------|----------|----------|------|------|
| **Systematic Intraday TF** | 动态边界 + VWAP | 半小时 | VWAP | 双向，动态仓位 |
| **Session High Retest** | 回撤深度过滤 | 5min | 无 | 长仅，持有至 close |
| **VSO Momentum** | 波动率锥突破 | 5min | VWAP + EOD | 双向，凸性 |
| **Simple Intraday** | VWAP + StochRSI | 5min | 付费 | 新闻驱动 |

---

## 评价

| 指标 | 评分 | 备注 |
|--------|-------|-------|
| 数据质量 | ⭐⭐⭐⭐☆ | SPY 回测详细，但缺少多品种验证 |
| 规则完整性 | ⭐⭐⭐☆☆ | 框架清晰但缺少具体参数（需参考论文代码） |
| 可操作性 | ⭐⭐⭐☆☆ | 需要日内每个时间点的历史数据 |
| 风险透明度 | ⭐⭐⭐⭐☆ | 明确讨论了滑点风险、论文偏差 |
| 新题性 | ⭐⭐⭐⭐☆ | 动态边界 + 日内波动率季节性是亮点 |

**总体**: 🟢 **Green** — 学术背景强，回测数据丰富，但实盘需要注意滑点。最适合作为日内策略组合的一部分。

---

## 相关链接
- 原文: https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following
- 论文: Beat the Market: An Effective Intraday Momentum Strategy for S&P 500 ETF (SPY) by Carlo Zarattini, Andrew Aziz, Andrea Barbon. Swiss Finance Institute Research Paper No. 24-97
- 原文备份: raw/articles/2026-04-04-Systematic-Intraday-Trend-Following-Strategy.md
