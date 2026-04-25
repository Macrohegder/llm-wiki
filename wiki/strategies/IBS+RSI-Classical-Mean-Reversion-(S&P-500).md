---
tags:
  - strategy
asset: "equity"
strategy-type: "mean-reversion"
status: "processed"
sharpe: ""
max_dd: ""
cagr: ""
lookback: "21 days"
rebalance: "signal-based"
created: "2026-04-18"
---

# IBS+RSI Classical Mean Reversion (S&P 500)

> 类型：#strategy/mean-reversion | 资产：#asset/equity | 状态：#status/processed

---

## 一句话摘要
被评价为"经典方法"的 IBS + RSI(21) 均值回归策略，在 S&P 500 上自 2000 年以来表现可观，特别强调了参数反转/置换测试的重要性。

## 策略逻辑
### 信号生成
1. 入场条件：IBS < 0.25 且 RSI(21) < 45，两条件同时满足
2. 入场时间：于收盘价买入
3. 出场条件：收盘价 > 昨日收盘价
4. 过滤条件：无

### 风险管理
- 仓位管理：100% 仓位复利运行（回测设定，未扣税）
- 止损设置：以出场规则替代硬止损
- 资金管理：建议实战中降低仓位以应对回撤

## 参数设置
| 参数 | 默认值 | 说明 |
|------|--------|------|
| IBS 阈值 | < 0.25 | 日线 |
| RSI 周期 | 21 日 | 标准周期 |
| RSI 阈值 | < 45 | 略低于传统超卖阈值 |
| 标的 | S&P 500 | 可通过 SPY 或期货实现 |
| 出场触发 | 昨日收盘价 | 收盘价 > 昨日收盘价 |

## 回测表现
| 指标 | 数值 |
|------|------|
| 初始资金 | $100,000 |
| 运行方式 | 复利，100% 仓位，未扣税 |
| 回测区间 | 2000-今 |

## 优势与局限
### 优势
- 双重筛选，IBS 捕捉日内极端，RSI 过滤弱势市场
- 经典组合，被多个研究验证
- 文章提供参数反转测试，稳健性得到验证

### 局限
- 未提供具体 CAGR、Sharpe 等统计数据
- 100% 仓位复利在实战中风险较大
- 未扣除税收，实际收益会降低

### 适用市场环境
- 适合：振荡市、牛市回调
- 不适合：强势熊市、高波动率环境

## 相关概念
- [[concept:IBS (Internal Bar Strength)]]
- [[concept:RSI (Relative Strength Index)]]
- [[concept:Parameter Robustness]]

## 参考来源
- [[source:S&P 500 Mean Reversion Using IBS and RSI: Classical Approach Analysis]]

## 待验证事项
- [ ] 回测验证（获取具体 CAGR、Sharpe、回撤数据）
- [ ] 过拟验证（IBS 0.2/0.25/0.3 × RSI 40/45/50 组合）
- [ ] 考虑税收后的实际收益
- [ ] 实盘测试
