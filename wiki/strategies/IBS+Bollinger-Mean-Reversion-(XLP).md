---
tags:
  - strategy
asset: "equity"
strategy-type: "mean-reversion"
status: "processed"
sharpe: ""
max_dd: ""
cagr: ""
lookback: "25 days"
rebalance: "signal-based"
created: "2026-04-18"
---

# IBS+Bollinger Mean Reversion (XLP)

> 类型：#strategy/mean-reversion | 资产：#asset/equity | 状态：#status/processed

---

## 一句话摘要
结合 IBS 指标、25 日波动率带和 Bollinger 下轨的均值回归策略，专门用于 XLP 消费必需品 ETF。

## 策略逻辑
### 信号生成
1. 计算 25 日 H-L 均值
2. 计算每日 IBS = (C-L)/(H-L)
3. 计算下轨 = 近25日最高价 - 2.25 × 25日H-L均值
4. 入场条件：XLP 收盘价 < 下轨 且 IBS < 0.6
5. 出场条件：收盘价 > 昨日最高价

### 风险管理
- 仓位管理：100% 仓位复利运行（回测设定）
- 止损设置：以出场规则替代硬止损
- 资金管理：可与其他均值回归策略组合

## 参数设置
| 参数 | 默认值 | 说明 |
|------|--------|------|
| H-L 均值周期 | 25 日 | 测量短期波动率 |
| 下轨倍数 | 2.25 | 下轨 = 最高价 - 2.25×H-L均值 |
| IBS 阈值 | 0.6 | IBS < 0.6 |
| 标的 | XLP | Consumer Staples ETF |
| 出场触发 | 昨日最高价 | 收盘价 > 昨日最高价 |

## 回测表现
| 指标 | 数值 |
|------|------|
| 初始资金 | $100,000 |
| 运行方式 | 复利，100% 仓位 |
| 回测区间 | 至今 |

## 优势与局限
### 优势
- 多重筛选条件，过滤虚假信号
- XLP 波动率低，均值回归效应明显
- 规则清晰，可复现性强

### 局限
- 信号频率可能较低
- 仅适用于低波动率防御类资产
- 未提供具体回测统计数据

### 适用市场环境
- 适合：振荡市、牛市回调中的防御类股票
- 不适合：高波动率成长股、熊市

## 相关概念
- [[concept:IBS (Internal Bar Strength)]]
- [[concept:Bollinger Bands]]
- [[concept:Mean Reversion]]

## 参考来源
- [[source:3 Best Mean Reversion Strategies: Backtested Buy and Sell Signals Analysis]]

## 待验证事项
- [ ] 回测验证（Python/Amibroker 复现）
- [ ] 过拟验证（IBS 阈值 0.5 vs 0.6 vs 0.7）
- [ ] 实盘测试
