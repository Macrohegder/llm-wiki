---
tags:
  - entity
type: "product"
created: "2026-04-18"
---

# SPY

> 类型：#entity/product | 创建日期：2026-04-18

---

## 基本信息
SPY 是 State Street Global Advisors 发行的 SPDR S&P 500 ETF Trust，是全球最流动的 ETF 之一，跟踪 S&P 500 指数。

## 主要特征
- 成立时间：1993 年 1 月
- 总资产规模：超过 4000 亿美元
- 流动性极高，是量化策略回测的首选标的之一

## 与量化交易的关联
- 常见策略类型：均值回归、趋势跟踪、季节性效应
- 相关策略：[[strategy:RSI-2 Mean Reversion (SPY)]] [[strategy:3 Days Down Overnight (SPY)]] [[strategy:IBS+RSI Classical Mean Reversion (S&P 500)]]

## 相关文章
```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, [[SPY]]) OR contains(file.inlinks, [[SPY]])
SORT date DESC
```

## 资源链接
- 官方网站：https://www.sectorspdr.com/sectorspdr/sectors/technology
