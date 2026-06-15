# CN 期货候选组合 Walk-Forward 验证报告

- **生成时间**: 2026-06-15 11:37:34
- **数据来源**: 2026-05-05 CN 期货推荐报告
- **验证方法**: Walk-Forward Optimization (expanding window, train=3y, test=1y)
- **回测区间**: 2020-01-01 ~ 2026-04-29
- **总候选组合**: 29
- **通过 WFO (deployable=True)**: 6 个
- **真正可推荐 (deployable=True & OOS Sharpe > 0)**: 5 个

## 1. 执行摘要

本报告对 2026-05-05 报告中按 GA 全样本优化筛选出的 29 个 CN 期货组合进行了 Walk-Forward 样本外验证。
结果显示，绝大多数 GA 高夏普组合在样本外未能保持表现，甚至完全失效（无交易）。
最终只有 **5 个组合** 同时满足 deployable=True 且 OOS Sharpe > 0，可作为实盘观察候选。

## 2. GA vs WFO 夏普对比

![GA vs OOS Sharpe](raw/assets/cn_futures_wfo_20260615/01_ga_vs_oos_sharpe.png)

- 大量组合集中在 OOS Sharpe ≈ 0 区域，说明 GA 全样本结果具有欺骗性。
- 仅 VolatilitySupportStrategy 在 T/TL/AU 三个品种上表现稳定。

## 3. 可实盘推荐组合

| 排名 | 策略 | 品种 | 实盘品种 | GA Sharpe | WFE | Consistency | Avg Test Sharpe | OOS Sharpe | OOS Return% | 过拟合风险 |
|------|------|------|----------|-----------|-----|-------------|-----------------|------------|-------------|------------|
| 1 | VolatilitySupportStrategy | T888.CFFEX | T2606.CFFEX | 0.801 | 1.72 | 0.75 | 1.738 | 1.311 | 9.64% | low |
| 2 | PullbackMrStrategy | AU888.SHFE | AU2606.SHFE | 0.826 | 1.27 | 0.75 | 1.597 | 0.639 | 19.02% | low |
| 3 | VolatilitySupportStrategy | AU888.SHFE | AU2606.SHFE | 0.826 | 1.13 | 0.75 | 0.755 | 0.585 | 22.48% | low |
| 4 | VolatilitySupportStrategy | TL888.CFFEX | TL2606.CFFEX | 0.846 | 0.44 | 0.67 | 0.601 | 0.523 | 8.69% | moderate |
| 5 | MacdHistogramStrategy | TL888.CFFEX | TL2606.CFFEX | 0.846 | 0.73 | 1.00 | 0.927 | 0.396 | 2.39% | low |

![WFE 分布](raw/assets/cn_futures_wfo_20260615/02_wfe_distribution.png)

![可部署组合](raw/assets/cn_futures_wfo_20260615/03_deployable_oos_sharpe.png)

### 3.1 需注意的组合

以下组合虽然 `deployable=True`，但拼接 OOS Sharpe ≤ 0，不建议直接实盘：

| 策略 | 品种 | WFE | Avg Test Sharpe | OOS Sharpe | 说明 |
|------|------|-----|-----------------|------------|------|
| FiveDayLowOvernightStrategy | AU888.SHFE | 1.32 | 0.818 | -0.106 | 样本外收益为负，需观察 |

## 4. 未通过 WFO 的组合

| 策略 | 品种 | WFE | Avg Test Sharpe | OOS Sharpe | 过拟合风险 | 主要问题 |
|------|------|-----|-----------------|------------|------------|----------|
| TripleRsiLongShortStrategy | AU888.SHFE | 0.60 | 0.625 | 0.795 | low | 综合不达标 |
| RsiMeanReversionStrategy | T888.CFFEX | 0.26 | 0.515 | 0.529 | high | 过拟合风险高 |
| MacdHistogramStrategy | TF888.CFFEX | 0.24 | 0.049 | 0.258 | high | 过拟合风险高 |
| TripleRsiLongShortStrategy | TF888.CFFEX | 0.12 | 0.244 | 0.138 | high | 过拟合风险高 |
| IbsRsiMeanReversionStrategy | TL888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| PullbackMrStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| PullbackMrStrategy | TF888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| IbsMeanReversionStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| IbsRsiMeanReversionStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| FiveDayLowOvernightStrategy | TF888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| ConsecutiveDownDaysStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| FiveDayLowOvernightStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| IbsMeanReversionStrategy | TF888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| ConsecutiveDownDaysStrategy | IF888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| ConsecutiveDownDaysStrategy | TL888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| Nr7BreakoutStrategy | TF888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| Nr7BreakoutStrategy | AU888.SHFE | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| FiveDayLowOvernightStrategy | IH888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| FiveDayLowStrategy | IC888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| WilliamsRMrSimpleStrategy | TF888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| FiveDayLowStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| WilliamsRMrSimpleStrategy | T888.CFFEX | 0.00 | 0.000 | 0.000 | severe | WFO窗口无交易, 一致性差, 过拟合风险高 |
| RsiMeanReversionStrategy | AU888.SHFE | -0.22 | 0.144 | -0.326 | severe | WFE<0, 一致性差, 过拟合风险高, OOS夏普为负 |

![可部署热力图](raw/assets/cn_futures_wfo_20260615/04_deployable_heatmap.png)

## 5. 按品种统计

| 品种 | 候选数 | 通过数 | 通过率 |
|------|--------|--------|--------|
| TL888.CFFEX | 4 | 2 | 50.0% |
| AU888.SHFE | 6 | 2 | 33.3% |
| T888.CFFEX | 9 | 1 | 11.1% |
| TF888.CFFEX | 7 | 0 | 0.0% |
| IF888.CFFEX | 1 | 0 | 0.0% |
| IH888.CFFEX | 1 | 0 | 0.0% |
| IC888.CFFEX | 1 | 0 | 0.0% |

## 6. 结论与交易建议

1. **VolatilitySupportStrategy 是 CN 期货最稳健的策略**：在 T888、TL888、AU888 上均通过 WFO，OOS Sharpe 0.52-1.31。
2. **国债期货（T/TF/TL）整体表现分化**：T/TL 有通过组合，但 TF 上多个 GA 高夏普策略 WFO 完全失效。
3. **股指期货（IF/IH/IC）无通过组合**：当前 29 个候选中 IF/IH/IC 策略全部未通过 WFO。
4. **WFO 暴露了大量 GA 过拟合**：23 个未通过组合中，多数在 WFO 窗口中完全无交易，说明 GA 全样本结果不可直接用于实盘。
5. **建议**：优先部署 VolatilitySupportStrategy @ T888，其次观察 MacdHistogramStrategy @ TL888。其他组合需更长样本外跟踪。
