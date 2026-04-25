---
tags:
  - strategy
asset: "equity"
strategy-type: "mean-reversion"
status: "processed"
sharpe: ""
max_dd: "-34%"
cagr: "9%"
lookback: "2 days"
rebalance: "signal-based"
created: "2026-04-18"
---

# RSI-2 Mean Reversion (SPY)

> 类型：#strategy/mean-reversion | 资产：#asset/equity | 状态：#status/processed

---

## 一句话摘要
Larry Connors 提出的经典短期均值回归策略，利用 2 周期 RSI 极端敏感性捕捉 SPY 短期超卖反弹。

## 策略逻辑
### 信号生成
1. 入场条件：SPY 的 RSI(2) < 10，于收盘价买入
2. 出场条件：RSI(2) 穿越 80，于收盘价卖出
3. 过滤条件：无

### 风险管理
- 仓位管理：建议单笔仓位不超过总资金的 10-15%（因最大回撤达 34%）
- 止损设置：本策略未设置硬止损，依赖 RSI 出场规则
- 资金管理：可与趋势策略组合使用

## 参数设置
| 参数 | 默认值 | 说明 |
|------|--------|------|
| lookback | 2 日 | RSI 周期 |
| 买入阈值 | 10 | RSI(2) < 10 |
| 卖出阈值 | 80 | RSI(2) > 80 |
| 标的 | SPY | S&P 500 ETF |

## 回测表现
| 指标 | 数值 |
|------|------|
| CAGR | 9% |
| 最大回撤 | -34% |
| 市场占用率 | 28% |
| 平均每笔收益 | 0.9% |
| 回测区间 | 1993-今 |

## 优势与局限
### 优势
- 规则极简，无需复杂计算
- 市场占用率低，资金效率高
- 与趋势策略相关性低

### 局限
- 最大回撤 34%，心理承受难度大
- 信号频率低，可能长期无信号
- 在强势下跌中可能连续亏损

### 适用市场环境
- 适合：振荡市、牛市回调
- 不适合：熊市主升浪、高波动率市场

## 相关概念
- [[concept:RSI (Relative Strength Index)]]
- [[concept:Mean Reversion]]
- [[concept:Position Sizing]]

## 参考来源
- [[source:RSI 2 Strategy Explained: Larry Connors' 2-Period RSI Trading Rules]]

## 待验证事项
- [ ] 回测验证
- [ ] 过拟验证（VIX 筛选、多标的测试）
- [ ] 实盘测试
