# Pairs Trading Crypto Perpetuals: The Methodology

**Source**: [[2026-04-11-Pairs-Trading-Crypto-Perpetuals:-The-Methodology]] | [Delphic Alpha]()
**Date**: 2026-04-11
**Tags**: #article #substack

## One-Sentence Summary

> Substack article about trading strategies.

## Key Insights

1. **原文来源**: Delphic Alpha

## Full Content

---
title: "Pairs Trading Crypto Perpetuals: The Methodology"
author: "Oracle (Delphic Alpha)"
url: "https://delphicalpha.substack.com/p/pairs-trading-crypto-perpetuals-the"
date: "2026-04-11"
topics: ["pairs-trading", "statistical-arbitrage", "crypto", "perpetuals", "mean-reversion", "hedge-ratio", "z-score", "hyperliquid"]
source: "Delphic Alpha Substack"
---

# Pairs Trading Crypto Perpetuals: The Methodology

> Part 1 of 3 — Spread construction, hedge ratios, z-score signals, and PnL math

## 核心思想

配对交易（Pairs Trading）是统计套利的一种形式——对两个相关资产的价格关系偏离均值时进行押注，预期其会回归。

**市场中性**：不需要预测加密货币涨跌方向，只需要预测两个币种是否会收敛。

**三大难点**（也是整个策略的核心）：
1. **配对选择** — 大多数配对不会均值回归，找到会回归的配对是游戏的全部
2. **对冲比率估计** — 两个资产之间的关系不是静态的，需要滚动估计每单位 quote 需要持有多少 base
3. **信号时机** — 均值回归确实存在，但可能比你的风险预算允许的时间更长

---

## 一、价差构建 (The Spread)

### 对数价格空间

```
spread_t = log(quote_t) - alpha_t - beta_t * log(base_t)
```

- `quote_t` / `base_t`：t 时刻收盘价
- `beta_t`：**对冲比率** — 每美元 quote 需要持有多少美元 base
- `alpha_t`：截距（吸收两个对数价格序列之间的水平差异）

**为什么用对数价格？**
1. 收益率是乘法复合的，对数变换使其变为加法
2. 自然处理币种间巨大的价格差异（BTC $60K vs DOGE $0.15）

### 关键前提

如果关系稳定，这个残差（spread）应该是**平稳的（stationary）** — 围绕零波动，不会趋势性偏离。这正是均值回归所需的条件。

---

## 二、滚动 OLS 对冲比率 (Rolling OLS Hedge Ratio)

### 估计方法

在每个 bar t，取最近 W 个 bar 拟合：

```
log(quote_i) = alpha + beta * log(base_i) + epsilon_i,   for i in [t-W, t)
```

然后用拟合的参数计算 out-of-sample 的 spread：

```
spread_t = log(quote_t) - alpha - beta * log(base_t)
```

**注意窗口是 `[t-W, t)`** — 使用 t 之前的 bar，确保 spread 计算是 out-of-sample 的。

### 窗口选择

- 太短：beta 估计噪声大
- 太长：无法捕捉关系变化
- 经验值：**30-90 天**（Hyperliquid 1 小时数据约 720-2160 bar）

---

## 三、Z-Score 信号 (Z-Score Signals)

### 计算

```
zscore_t = (spread_t - mean(spread over W)) / std(spread over W)
```

同样使用 lookback 窗口 `[t-W, t)` 计算均值和标准差。

### 入场规则

| 信号 | 条件 | 操作 |
|------|------|------|
| 做多 spread | zscore < -entry_z | 做多 quote，做空 base |
| 做空 spread | zscore > +entry_z | 做空 quote，做多 base |
| 平仓 | \|zscore\| < exit_z | 平仓两边 |

### 参数选择

- `entry_z`：典型值 **2.0-3.0**（标准差倍数）
- `exit_z`：典型值 **0.0-0.5**
- 更宽的 entry_z → 更少交易，但每笔预期收益更高
- 更紧的 exit_z → 更快锁定利润，但可能错过更大回归

---

## 四、PnL 计算 (PnL Math)

### 逐日 PnL

对于持有期为 T 的交易：

```
PnL = (quote_return - beta * base_return) * position_size
```

其中：
- `quote_return = log(quote_T) - log(quote_0)`
- `base_return = log(base_T) - log(base_0)`
- `position_size` 以 quote 的名义金额计

### 关键理解

- 当 spread 从 -2σ 回归到 0 时，PnL ≈ 2σ * position_size
- 但路径依赖：如果 spread 先跌到 -3σ 再回归，中间会有浮亏
- 这就是"均值回归可能比你的风险预算更长"的含义

---

## 五、完整流水线 (Full Pipeline)

```
1. 数据获取 → Hyperliquid 永续合约 1h K 线
2. 配对选择 → 相关性筛选 + ADF 检验（平稳性）
3. 滚动 OLS → 估计 alpha, beta
4. 计算 Spread → out-of-sample 残差
5. Z-Score 计算 → 标准化 spread
6. 信号生成 → entry/exit 阈值
7. PnL 计算 → 逐日盈亏
8. 风险管理 → 止损、仓位管理
```

---

## 六、Hyperliquid 优势

- **24/7 交易**：没有周末缺口，关系更连续
- ** tight spreads**：永续合约流动性好
- **高杠杆**：可以用较少资金建立对冲头寸
- **无资金费率干扰**：配对交易两边同时持有，资金费率大致抵消

---

## 七、待解决问题（Part 2/3 预告）

1. **配对选择的具体方法** — 如何筛选出真正均值回归的配对
2. **ADF 检验与协整** — 统计检验方法
3. **参数优化** — entry_z, exit_z, W 的最优组合
4. **风险管理** — 止损、最大持仓时间、仓位管理
5. **实盘执行** — 滑点、手续费、API 延迟

---

## 与用户现有基础设施的关联

| 组件 | 用户已有 | 状态 |
|------|---------|------|
| Hyperliquid 数据 | ✅ vnpy-hyperliquid 网关 | 可用 |
| 永续合约 K 线 | ✅ 1m/1h 数据 | 可用 |
| 配对交易回测框架 | ❌ 需自建 | 缺失 |
| 滚动 OLS 估计 | ❌ 需实现 | 缺失 |
| Z-Score 信号系统 | ❌ 需实现 | 缺失 |
| ADF/协整检验 | ❌ 需实现 | 缺失 |

---

## 参考链接

- 原文：https://delphicalpha.substack.com/p/pairs-trading-crypto-perpetuals-the
- 平台：Delphic Alpha
- 数据：Hyperliquid 永续合约
- 方法：滚动 OLS + Z-Score 均值回归


---

*Imported from Substack on 2026-04-25*
