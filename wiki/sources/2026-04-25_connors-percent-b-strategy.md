# Larry Connors %B Strategy: A Simple Mean Reversion Edge Explained

**来源**: https://open.substack.com/pub/quantifiedstrategies/p/larry-connors-b-strategy-a-simple
**作者**: QuantifiedStrategies.com
**日期**: 2026-04-25
**标签**: #mean-reversion #connors #bollinger-bands #percent-b #paywall-preview

## 一句话摘要

Larry Connors 的 %B 均值回归策略——当市场在长期上升趋势中价格跌破 Bollinger 下轨（%B < 0）时买入做多，等待短期反弹后快速出场。

> ⚠️ **注意**：本文为付费文章，以下内容仅为免费预览部分。完整回测表格和详细交易规则被付费墙遮挡。

## 策略核心逻辑

基于 Larry Connors 的理念，利用 Bollinger Bands 衍生指标 %B 来量化价格偏离程度：

| 规则 | 描述 |
|------|------|
| **前提条件** | 市场处于长期上升趋势（如 > 200日均线） |
| **入场信号** | %B 跌至 0 以下（价格跌破 Bollinger 下轨） |
| **做多方向** | 仅在多头方向交易（均值回归，逆势做多） |
| **出场** | 快速反弹后出场（通常几天内） |
| **持仓周期** | 短线持仓，通常几根 K 线 |

## %B 指标

%B 是 Bollinger Bands 的归一化指标：

- %B > 1 → 价格在 Bollinger 上轨上方
- %B < 0 → 价格在 Bollinger 下轨下方
- 公式：%B = (close - lower_band) / (upper_band - lower_band)

## 回测数据（免费预览部分）

| 品种 | 时间范围 | 交易次数 | 平均盈利 | 持仓时间占比 |
|------|---------|---------|---------|------------|
| SPY | 1993–2026 | 63 | 1.3% | 4% |

## 备注

- 本文为完整文章的自由预览部分，`Trading Rules` 章节仅显示了 "We made the following trading rules:" 后即进入付费墙
- 该策略与之前复现的 Connors RSI2 策略思路类似，都是基于超卖反弹的均值回归，区别在于用 %B 指标替代 RSI 作为超卖信号
- 原文提到 "mean reversion works mainly for stocks, and not so well for other assets"
- 策略产生了 "many winners and occasionally a nasty loser" 的收益分布特征（正偏分布，但存在尾部风险）
