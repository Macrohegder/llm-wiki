# 主题深度分析: strategy/mean-reversion

**生成时间**: 2026-04-23 19:48:20
**分析文章数**: 2 篇
**可复现策略**: 2 篇

## 文章清单

| # | 标题 | 日期 | Concrete | 状态 |
|---|------|------|----------|------|
| 1 | [ETF Mean Reversion Methods: Mean Reversi...](https://www.tradequantixnewsletter.com/p/etf-mean-reversion-methods-mean-reversion) | 2025-04-22 | 6 | ✅ 可复现 |
| 2 | [Session High Retest: A Quantitative Intr...](https://open.substack.com/pub/delphicalpha/p/session-high-retest-a-quantitative) | 2026-04-22 | 6 | ✅ 可复现 |

## 策略规则对比

| 文章 | 入场规则 | 出场规则 | 止损 | 时间框架 | 指标 |
|------|---------|---------|------|---------|------|
| ETF Mean Reversion Methods: Me... | my personal systematic trading portfolio | systems, each measuring oversold conditi | - | 252-day | rsi, ema, sma |
| Session High Retest: A Quantit... | after a pullback, holding to the session | i expected; dax or s&p is more likely a  | - | 5-minute | rsi, ema, sma |

## 回测数据对比

| 文章 | CAGR | Sharpe | 最大回撤 | 胜率 | 交易次数 |
|------|------|--------|---------|------|---------|
| ETF Mean Reversion Methods: Me... | - | 1 | - | - | 10 |
| Session High Retest: A Quantit... | 13.6 | 0.58 | 16.2 | 54.6 | 7 |

## 共同参数区间

| 参数 | 最小值 | 最大值 | 中位数 | 出现次数 |
|------|--------|--------|--------|---------|
| lookback | 2008 | 2011 | 2011 | 2 |

## 可复现策略配置

以下策略已生成 YAML 配置文件，可直接用于回测：

1. [ETF Mean Reversion Methods: Mean Reversion Mini-Portfolio Creation - Part 2](strategies/ETF_Mean_Reversion_Methods__Me.yaml)
2. [Session High Retest: A Quantitative Intraday Strategy Across 10 Futures Markets](strategies/Session_High_Retest__A_Quantit.yaml)

## strategy/mean-reversion 策略设计 Checklist

### 数据
- [ ] 确认品种历史数据覆盖回测期
- [ ] 检查数据质量（缺失值、异常值）
- [ ] 确认交易成本（佣金、滑点）

### 信号
- [ ] 入场条件是否明确、可量化
- [ ] 出场条件是否完整（止盈/止损/时间）
- [ ] 信号是否存在 lookahead bias

### 风险管理
- [ ] 单笔风险是否控制在 1-2%
- [ ] 是否有最大回撤限制
- [ ] 是否有仓位上限

### 回测验证
- [ ] 样本外测试（walk-forward）
- [ ] 参数敏感性分析
- [ ] 不同市场环境表现

### 实盘准备
- [ ] 执行延迟评估
- [ ] 流动性检查
- [ ] 极端行情应对预案


## 矛盾观点与局限

（需手动补充：不同文章对同一参数的建议是否矛盾）
