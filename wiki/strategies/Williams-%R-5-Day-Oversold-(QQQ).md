---
tags:
  - strategy
asset: "equity"
strategy-type: "mean-reversion"
status: "processed"
sharpe: ""
max_dd: "-18% (single trade)"
cagr: "11.5%"
lookback: "5 days"
rebalance: "signal-based"
created: "2026-04-18"
---

# Williams %R 5-Day Oversold (QQQ)

> 类型：#strategy/mean-reversion | 资产：#asset/equity | 状态：#status/processed

---

## 一句话摘要
仅凭 2 条规则的 Williams %R 均值回归策略，在 QQQ 上实现 72% 胜率和 11.5% 年化收益，市场占用率仅 21%。

## 策略逻辑
### 信号生成
1. 入场条件：5 日 Williams %R 收盘价 < -90，于收盘价买入
2. 出场条件：收盘价高于昨日最高价
3. 过滤条件：无

### 风险管理
- 仓位管理：建议单笔小仓位（因无硬止损）
- 止损设置：本策略不使用硬止损，以出场规则替代
- 资金管理：年均交易约 15 次，资金效率极高

## 参数设置
| 参数 | 默认值 | 说明 |
|------|--------|------|
| lookback | 5 日 | Williams %R 周期 |
| 买入阈值 | -90 | %R < -90 时买入 |
| 出场触发 | 昨日最高价 | 收盘价 > 昨日最高价 |
| 标的 | QQQ | Nasdaq 100 ETF |

## 回测表现
| 指标 | 数值 |
|------|------|
| CAGR | 11.5% |
| 胜率 | 72% |
| 市场占用率 | 21% |
| 年均交易次数 | ~15 次 |
| 平均每笔收益 | 0.9% |
| 单笔最大亏损 | 18% (20 年仅 1 次超过 10%) |
| 回测区间 | QQQ 至今 |

## 优势与局限
### 优势
- 规则极简（2 条规则）
- 市场占用率极低，资金效率极高（有效年化约 55%）
- 心理压力小（高胜率、低频率）

### 局限
- 无硬止损，心理承受力要求极高
- 仅适用于股票型 ETF，商品和金属上无效
- 在极端市场中可能出现连续大幅亏损

### 适用市场环境
- 适合：股票指数 ETF（QQQ、SPY、IWM）
- 不适合：商品、金属、外汇

## 相关概念
- [[concept:Williams %R]]
- [[concept:Mean Reversion]]
- [[concept:Position Sizing]]

## 参考来源
- [[source:Profitable Williams %R Strategy For Mean Reversion Trading (Only 2 Rules)]]

## 待验证事项
- [ ] 回测验证（SPY、IWM 对比）
- [ ] 过拟验证（%R 阈值 -85 vs -90 vs -95）
- [ ] 实盘测试
