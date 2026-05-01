---
id: trend-following-compendium-2026-05
title: "趋势跟踪策略完整汇编 (Trend-Following Compendium)"
date: "2026-05-01"
tags:
  - synthesis
  - trend-following
  - strategy-compendium
  - verified-strategies
---

# 趋势跟踪策略完整汇编

> **范围**: 涵盖 llm-wiki 中所有趋势跟踪、动量、突破类策略
> **统计**: 2,195 篇 sources 中 168 篇标记为 strategy/trend-following，30 篇经深度处理
> **生成时间**: 2026-05-01

---

## 1. 本月主题分布变化

### 1.1 全库主题分布 (Top 10)
| 主题 | 文章数 | 占比 |
|------|--------|------|
| asset/equity | 338 | 15.4% |
| topic/backtesting | 281 | 12.8% |
| **strategy/trend-following** | **168** | **7.7%** |
| strategy/mean-reversion | 146 | 6.7% |
| strategy/seasonal | 109 | 5.0% |
| topic/risk-management | 95 | 4.3% |
| asset/commodity | 72 | 3.3% |
| asset/crypto | 68 | 3.1% |
| strategy/volatility | 54 | 2.5% |
| asset/bond | 37 | 1.7% |

### 1.2 趋势跟踪子主题分布
| 子主题 | 文章数 | 说明 |
|--------|--------|------|
| EMA/SMA 交叉 | ~45 | 20/50/200日均线系统 |
| 突破类 | ~38 | Donchian、NR7、通道突破 |
| 动量轮动 | ~28 | ETF轮动、行业轮动 |
| 日内趋势 | ~22 | Session High、VWAP、动态边界 |
| 加密货币趋势 | ~18 | BTC/ETH动量策略 |
| 多因子组合 | ~17 | 趋势+波动率+过滤 |

---

## 2. 已验证策略 (Green/Yellow 评级)

### 2.1 🟢 Green 级 (复现通过)
| 策略 | 来源 | 最佳品种 | Sharpe | 最大回撤 | 评级 |
|------|------|----------|--------|----------|------|
| KAMA + ATR RTY Trend | [[2025-07-01-kama-atr-rty-trend]] | RTY/ES | 1.783 | - | 🟢 |
| NR7 Breakout | [[2026-04-22-NR7-Breakout-Strategy]] | SPY | 1.288 | -0.52% | 🟢 |
| NR7 Breakout (Updated) | [[2026-04-22-NR7-Breakout-Strategy]] | SPY | 1.212 | -6.51% | 🟢 |
| Donchian ADX Breakout | [[2026-04-05-Strategy-8]] | ETH | 1.192 | -14.21% | 🟢 |
| Simple Trend Following (Dual Stop) | [[Simple Trend Following with Dual Stop]] | QQQ | 1.023 | -4.37% | 🟢 |
| SMA200 Trend Following | [[2024-03-03-A-Simple-Trend-Following-System]] | SPY | 0.591 | -3.22% | 🟢 |
| Session High Retest | [[2026-04-22-session-high-retest-intraday-strategy]] | 多品种 | 1.15 (Portfolio) | - | 🟢 |

### 2.2 🟡 Yellow 级 (规则完整但未全绿)
| 策略 | 来源 | 最佳品种 | Sharpe | 问题 |
|------|------|----------|--------|------|
| Bitcoin Momentum | [[2026-04-24-Bitcoin-Momentum-Strategy]] | BTC | 0.476 | 回撤较大 |
| Simple Trend Following (Dual Stop) | [[Simple Trend Following with Dual Stop]] | QQQ | 1.02 | 推断实现 |

---

## 3. 策略规则对比矩阵

### 3.1 均线系统
| 策略 | 入场 | 出场 | 止损 | 时间框架 |
|------|------|------|------|----------|
| SMA200 | 价格>SMA200做多 | 价格<SMA200平仓 | 无 | 日线 |
| 20 EMA | 价格>20EMA做多 | 价格<20EMA平仓 | 3% | 日线 |
| 13/48 EMA | 13EMA上穿48EMA | 下穿 | 无 | 日线 |
| 9 EMA | 价格>9EMA做多 | 价格<9EMA平仓 | 无 | 日线/小时 |

### 3.2 突破系统
| 策略 | 入场 | 出场 | 过滤条件 | 时间框架 |
|------|------|------|----------|----------|
| NR7 Breakout | NR7后突破高点做多 | 跌破低点平仓 | NR7识别 | 日线 |
| Donchian ADX | 突破20日高点 + ADX>25 | 跌破10日低点 | ADX趋势确认 | 日线 |
| 52周新高 | 价格创52周新高 | 跌破20日均线 | 无 | 周线 |
| Session High Retest | 突破Session High后回踩 | 固定止损/时间 | VWAP确认 | 30分钟 |

### 3.3 动量轮动
| 策略 | 入场 | 出场 | 资产池 | 再平衡 |
|------|------|------|--------|--------|
| ETF Sector Rotation | 选最强Sector ETF | 排名掉出前N | SPY/TLT/LQD等 | 月度 |
| Crypto Trend Combo | BTC+ETH动量加权 | 动量转负 | BTC/ETH/SOL/DOGE | 动态 |
| Dual Momentum | 选最高12月收益 | 收益<无风险利率 | 股票/债券/商品 | 月度 |

---

## 4. 共同参数区间

| 参数 | 最小值 | 最大值 | 中位数 | 常见值 | 出现次数 |
|------|--------|--------|--------|--------|----------|
| 短期均线 | 9 | 20 | 13 | 20 EMA | 45+ |
| 长期均线 | 48 | 200 | 50 | 200 SMA | 38+ |
| 突破回看周期 | 7 | 20 | 10 | 20日 | 28+ |
| ADX阈值 | 20 | 25 | 25 | 25 | 12 |
| 止损比例 | 2% | 5% | 3% | 3% | 22 |
| 仓位比例 | 1% | 5% | 2% | 2%风险 | 15 |

---

## 5. 可复现策略 YAML 配置清单

本次批量处理生成 **29 个 YAML 配置文件**，保存在 `wiki/strategies/`：

### 5.1 高优先级复现队列
1. `Systematic_Intraday_Trend_Foll.yaml` — 日内动态边界+VWAP (Sharpe 1.33)
2. `A_Simple_Trend_Following_System_and_Stra.yaml` — SMA200经典趋势 (已验证)
3. `A_Trend_Following_Strategy__18__Annually.yaml` — 1926年以来18%年化
4. `52_WEEK_HIGH_TRADING_STRATEGY__BACKTEST_.yaml` — 52周新高突破
5. `A_Monthly_Momentum_Strategy_In_ETFs__Sec.yaml` — ETF月度轮动

### 5.2 配置文件模板结构
```yaml
strategy:
  name: "策略名称"
  description: "来源URL"
  symbols: [SPY]          # 默认品种，需手动调整
  exchange: SMART
  interval: d             # d=日线, 30m=30分钟
  start_date: "2014-01-01"
  end_date: "2024-12-31"
  signal_type: trend_breakout   # 或 session_high_retest / momentum_crossover
  params:
    lookback: 20
    fast_period: 13
    slow_period: 48
  stop_loss_pct: 0.03     # 3%止损
  position_size: 1.0
```

---

## 6. 关键洞察与注意事项

### 6.1 什么有效
- **趋势过滤器是必需品**: 所有成功的趋势策略都有某种形式的趋势确认 (ADX>25、价格>均线、突破确认)
- **时间框架决定夏普**: 日线策略Sharpe普遍0.5-1.0，日内30分钟策略可达1.15-1.33
- **多品种分散**: Portfolio Sharpe > 单一品种Sharpe (Session High Retest: 单品种0.8-1.0, Portfolio 1.15)
- **加密货币趋势更强**: BTC/ETH的趋势持续性显著高于股票指数

### 6.2 什么无效/危险
- **无过滤的突破**: 纯价格突破无波动率/趋势确认，假突破率高
- **过短均线**: 9 EMA策略在震荡市频繁假信号，需配合趋势过滤器
- **杠杆ETF长期持有**: TQQQ/TMF等因beta slippage，长期持有在震荡市衰减严重
- **Martingale加仓**: 指数级风险，必爆仓 (见 [[2026-04-30_Martingale-Strategy-for-Stocks]])

### 6.3 品种适配规律
| 品种类型 | 最佳策略类型 | 原因 |
|----------|-------------|------|
| 股指ETF (SPY/QQQ) | SMA200/EMA交叉 | 长期趋势明确，回撤可控 |
| 小盘股 (IWM/RTY) | KAMA+ATR | 波动大，需要自适应指标 |
| 黄金 (GLD) | 趋势+均值回归组合 | 既有趋势又有反转特性 |
| 加密货币 (BTC/ETH) | 动量突破 | 趋势持续性强，波动大 |
| 国债期货 (ZB/ZN) | 日内Session策略 | 开盘区间突破有效 |

---

## 7. 组合构建建议

### 7.1 趋势跟踪组合 (保守型)
| 策略 | 权重 | 品种 | 预期Sharpe |
|------|------|------|-----------|
| SMA200 Trend | 30% | SPY | 0.59 |
| NR7 Breakout | 25% | SPY/QQQ | 1.21 |
| ETF Rotation | 25% | SPY/TLT/LQD | 0.80 |
| Gold Trend | 20% | GLD | 1.22 |
| **组合预期** | **100%** | — | **~1.0** |

### 7.2 趋势跟踪组合 (激进型)
| 策略 | 权重 | 品种 | 预期Sharpe |
|------|------|------|-----------|
| Session High Retest | 30% | NQ/ES | 1.15 |
| Crypto Trend Combo | 25% | BTC/ETH | 1.74 |
| KAMA+ATR | 25% | RTY/ES | 1.78 |
| Donchian ADX | 20% | ETH | 1.19 |
| **组合预期** | **100%** | — | **~1.4** |

---

## 8. 数据与工具链

### 8.1 数据源
- **美股ETF**: Yahoo Finance (yfinance)
- **期货**: Interactive Brokers (ib_futures_data_pipeline)
- **加密货币**: CCXT / Binance / OKX

### 8.2 回测框架
- **vn.py**: 国内期货+加密货币
- **Backtrader**: 美股ETF策略验证
- **cta_developer**: 批量参数优化

### 8.3 关键指标监控
- Sharpe Ratio > 1.0 (Green门槛)
- Max Drawdown < 15%
- Profit/MaxDD > 2.0
- 交易次数 > 50 (统计显著性)

---

## 9. 相关链接

### 9.1 来源页面
- [[strategy-repro-sma200-trend-following]]
- [[strategy-repro-nr7-breakout]]
- [[strategy-repro-donchian-adx-breakout]]
- [[strategy-repro-crypto-trend-combo]]
- [[strategy-repro-crypto-trend-combo-v2]]
- [[strategy-repro-kama-atr-rty-20260430]]
- [[2026-04-22-session-high-retest-intraday-strategy]]
- [[2026-02-23-systematic-intraday-trend-following-strategy]]

### 9.2 概念页面
- [[trend-filter]]
- [[mean-reversion]]
- [[high-beta-bias]]
- [[Portfolio Diversification]]
- [[Monte Carlo Simulation]]

### 9.3 其他汇编
- [[mean-reversion-strategies-compendium]]
- [[reversal-strategies-compendium]]
- [[intraday-trading-strategies-compendium]]
- [[crypto-strategies-analysis-2026-04-30]]

---

*Last updated: 2026-05-01*
*Next review: 当新增 10+ 篇趋势跟踪策略文章时*
*Generated by: batch_deep_process.py --theme strategy/trend-following --max-articles 30*
