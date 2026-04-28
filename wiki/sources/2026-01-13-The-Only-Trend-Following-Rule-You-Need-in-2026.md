# The Only Trend Following Rule You Need in 2026 (Rule + Pine Script Code)

**原文链接**: https://tradinginvestingstrategies.substack.com/p/this-simple-trend-following-strategy

**发布时间**: Jan 13, 2026

**作者**: Trading & Investing Strategies

**类型**: 🔒 付费文章

---

## 摘要

一个适合初学者的趋势跟踪交易系统，通过智能止损保护资本。核心规则：让盈利奔跑，亏损严格控制在 1%。

**SPY 回测结果 (1993-01 ~ 2026-01)**：

| 指标 | 数值 |
|------|------|
| 总回报 | +19.31% |
| 最大回撤 | 2.40% |
| 总交易次数 | 256 |
| 胜率 | 41.80% (107/256) |
| 盈亏比 | 1.84 |

## 已知策略规则

### 入场条件
- **做多**: 价格穿越移动平均线之上
- **做空**: 价格穿越移动平均线之下

### 出场条件（双止损系统）
1. **固定止损**: 入场价下方 1%
2. **移动止损 (Trailing Stop)**: 随价格上涨而上移，锁定利润
3. **实际出场**: 两个止损中更紧（更靠近当前价）的那个被触发时出场

### 核心逻辑
- 小亏损被严格限制在 1%
- 大盈利让趋势决定何时出场
-  whichever stop is tighter (closer to current price) is the active stop

### 时间框架
- 日线周期
- 适合波段交易者，无需日内盯盘

## 缺失信息（付费内容）

以下关键参数在付费墙后，未获取：

- [ ] 移动平均线周期（如 SMA 20/50/200？）
- [ ] Trailing Stop 具体计算方法（如 ATR 倍数、固定百分比、 chandelier exit？）
- [ ] Pine Script 完整代码
- [ ] 参数优化建议
- [ ] 最佳时间框架和市场建议
