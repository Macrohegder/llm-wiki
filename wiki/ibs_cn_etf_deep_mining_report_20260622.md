# IbsMeanReversionStrategy 全 CN ETF 深度挖掘报告

- 生成时间: 2026-06-22
- 策略: IbsMeanReversionStrategy
- 标的范围: 110 只 CN ETF（上交所 72 + 深交所 38）
- 回测区间: 2020-01-01 ~ 2026-04-29
- GA 参数: pop=50, ngen=20, workers=4
- WFO 参数: expanding, train=3y, test=1y, pop=30, ngen=12

## 策略逻辑
- IBS = (Close - Low) / (High - Low)，取最近 `ibs_window` 天均值
- 做多条件：IBS < `ibs_entry`
- 平仓条件：IBS > `ibs_exit`
- 可选 MA 过滤：当 `use_ma_filter=1` 时，要求 close > MA(`ma_period`)

## GA 批量回测结果

| 统计项 | 数值 |
|---|---|
| 总品种数 | 110 |
| GA 达标候选 | 22 |

## WFO 样本外验证结果

**可实盘组合数: 2 / 22**

| 品种 | WFE | Consistency | Avg Test Sharpe | Concat OOS Sharpe | OOS Trades | Risk | GA Sharpe |
|---|---|---:|---:|---:|---:|---|---:|

## 可实盘组合参数
