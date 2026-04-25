---
tags:
  - strategy
asset: "equity"
strategy-type: "mean-reversion"
status: "processed"
sharpe: ""
max_dd: ""
cagr: ""
lookback: "3 days"
rebalance: "signal-based"
created: "2026-04-18"
---

# 3 Days Down Overnight (SPY)

> 类型：#strategy/mean-reversion | 资产：#asset/equity | 状态：#status/processed

---

## 一句话摘要
极简的隔夜均值回归策略：SPY 连跌 3 天后于第 3 天收盘价买入，次日开盘价出场，持仓仅一个隔夜。

## 策略逻辑
### 信号生成
1. 入场条件：SPY 连续 3 天收盘价下跌（close-to-close）
2. 入场时间：第 3 天收盘价
3. 出场条件：次日开盘价
4. 过滤条件：无

### 风险管理
- 仓位管理：单次隔夜持仓，无需夜间风险管理
- 止损设置：次日开盘自动出场，无需硬止损
- 资金管理：适合作为辅助策略

## 参数设置
| 参数 | 默认值 | 说明 |
|------|--------|------|
| 连跌天数 | 3 天 | 必须连续 3 天收盘价下跌 |
| 标的 | SPY | S&P 500 ETF |
| 持仓时间 | 1 隔夜 | 第 3 天收盘买入 → 次日开盘卖出 |

## 回测表现
| 指标 | 数值 |
|------|------|
| 回测工具 | Amibroker |
| 回测区间 | 1993-今 |
| 测试标的 | SPY |

## 优势与局限
### 优势
- 规则极简，无需任何技术指标
- 持仓时间极短，市场占用率低
- 执行成本低，适合辅助策略

### 局限
- 信号频率低（连续 3 天下跌不常见）
- 需要在收盘前完成信号判断
- 对执行时间精度要求高

### 适用市场环境
- 适合：振荡市、牛市中的短期回调
- 不适合：快速熊市（连续下跌可能持续）

## 相关概念
- [[concept:Overnight Edge]]
- [[concept:Mean Reversion]]
- [[concept:Behavioral Finance]]

## 参考来源
- [[source:3 Days Down Overnight Trading Strategy (S&P 500, Nasdaq, Rules, Performance)]]

## 待验证事项
- [ ] 回测验证（多标的：QQQ、IWM）
- [ ] 过拟验证（连跌 2 天 vs 4 天 vs 5 天）
- [ ] 实盘测试
