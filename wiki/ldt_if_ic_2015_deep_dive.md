# LimitedDualThrustStrategy 在 IF88 / IC88 上的深度挖掘报告（2015-2025）

> **Report Date**: 2026-06-26 12:58
> **Strategy**: LimitedDualThrustStrategy (LDT)
> **Symbols**: IF88.CFFEX, IC88.CFFEX
> **Period**: 2015-01-01 ~ 2025-12-31
> **Data Frequency**: 1-minute (ClickHouse)

---

## 1. 执行摘要

本报告对 **LimitedDualThrustStrategy** 在 **沪深300股指期货（IF88）** 和 **中证500股指期货（IC88）** 上执行完整深度挖掘流程：

1. **GA 全样本优化**（pop=50, ngen=20, workers=4）
2. **Expanding Walk-Forward 验证**（train=3y, test=1y, pop=30, ngen=12）
3. **Rolling Walk-Forward 验证**（train=3y, test=1y, pop=30, ngen=12）

### 核心结论

| 品种 | GA 通过 | Expanding WFO 通过 | Rolling WFO 通过 | 综合判定 |
|------|---------|--------------------|------------------|----------|
| IF88.CFFEX | ✅ | ✅ | ✅ | ✅ 推荐实盘 |
| IC88.CFFEX | ✅ | ❌ | ✅ | ❌ 不推荐 |

---

## 2. GA 全样本优化结果 (IS)

### 2.1 IF88.CFFEX

#### 最优参数

| 参数 | 值 | 说明 |
|------|-----|------|
| k1 | 0.36 | 多头突破系数 |
| k2 | 0.54 | 空头突破系数 |
| trailpercent | 0.35 | 移动止损百分比 |
| range_cap | 3 | 波动区间上限 |
| exit_time_type | 2 | 收盘平仓时间类型 |
| need_lock | 2 | 锁仓开关 |
| fixed_size | 1 | 每次交易手数 |
| trade_limit | 2 | 日内交易次数限制 |

#### 回测统计

| 指标 | 数值 |
|------|------|
| 夏普比率 (Sharpe) | 1.20 |
| 总收益 (Total Return) | 108.44% |
| 年化收益 (Annual Return) | 9.73% |
| 最大回撤 (Max DD) | -7.98% |
| 总交易数 | 6995 |
| 日均交易数 | 2.62 |
| 期末权益 | 2,084,402.90 CNY |
| 期初权益 | 1,000,000.00 CNY |

### 2.2 IC88.CFFEX

#### 最优参数

| 参数 | 值 | 说明 |
|------|-----|------|
| k1 | 0.27999999999999997 | 多头突破系数 |
| k2 | 0.78 | 空头突破系数 |
| trailpercent | 0.65 | 移动止损百分比 |
| range_cap | 2 | 波动区间上限 |
| exit_time_type | 1 | 收盘平仓时间类型 |
| need_lock | 2 | 锁仓开关 |
| fixed_size | 1 | 每次交易手数 |
| trade_limit | 2 | 日内交易次数限制 |

#### 回测统计

| 指标 | 数值 |
|------|------|
| 夏普比率 (Sharpe) | 1.29 |
| 总收益 (Total Return) | 190.29% |
| 年化收益 (Annual Return) | 17.52% |
| 最大回撤 (Max DD) | -6.71% |
| 总交易数 | 6052 |
| 日均交易数 | 2.32 |
| 期末权益 | 2,902,876.30 CNY |
| 期初权益 | 1,000,000.00 CNY |

![IS Equity Curves](ldt_if_ic_2015_deep_dive/is_equity_curves.png)

---

## 3. Walk-Forward 样本外验证结果 (OOS)

### 3.1 IF88.CFFEX

#### Expanding WFO

| 指标 | 数值 |
|------|------|
| 窗口数 | 8 |
| WFE | 0.40 |
| Consistency | 62.5% |
| Avg Test Sharpe | 0.61 |
| Avg Test Return | 6.58% |
| Avg Test Max DD | -6.92% |
| Concatenated OOS Sharpe | 0.66 |
| Concatenated OOS Return | 52.61% |
| 过拟合风险 | **MODERATE** |
| 可实盘 | **True** |

| 窗口 | Train 期 | Test 期 | Train Sharpe | Test Sharpe | Test Return | Test Max DD | 交易数 |
|------|----------|---------|--------------|-------------|-------------|-------------|--------|
| W1 | 2015-01-01 ~ 2018-01-01 | 2018-01-01 ~ 2019-01-01 | 1.73 | 1.95 | 19.54% | -3.39% | 482 |
| W2 | 2015-01-01 ~ 2019-01-01 | 2019-01-01 ~ 2020-01-01 | 1.77 | 1.85 | 21.00% | -5.22% | 680 |
| W3 | 2015-01-01 ~ 2020-01-01 | 2020-01-01 ~ 2021-01-01 | 1.76 | -0.39 | -5.65% | -14.81% | 742 |
| W4 | 2015-01-01 ~ 2021-01-01 | 2021-01-01 ~ 2022-01-01 | 1.56 | 1.69 | 18.26% | -3.00% | 670 |
| W5 | 2015-01-01 ~ 2022-01-01 | 2022-01-01 ~ 2023-01-01 | 1.60 | -0.32 | -3.03% | -7.71% | 584 |
| W6 | 2015-01-01 ~ 2023-01-01 | 2023-01-01 ~ 2024-01-01 | 1.49 | 0.57 | 4.59% | -3.78% | 572 |
| W7 | 2015-01-01 ~ 2024-01-01 | 2024-01-01 ~ 2025-01-01 | 1.40 | -1.21 | -8.10% | -9.79% | 636 |
| W8 | 2015-01-01 ~ 2025-01-01 | 2025-01-01 ~ 2025-12-31 | 1.24 | 0.71 | 6.00% | -7.64% | 599 |

#### Rolling WFO

| 指标 | 数值 |
|------|------|
| 窗口数 | 8 |
| WFE | 0.42 |
| Consistency | 87.5% |
| Avg Test Sharpe | 0.75 |
| Avg Test Return | 7.96% |
| Avg Test Max DD | -6.09% |
| Concatenated OOS Sharpe | 0.83 |
| Concatenated OOS Return | 63.71% |
| 过拟合风险 | **MODERATE** |
| 可实盘 | **True** |

| 窗口 | Train 期 | Test 期 | Train Sharpe | Test Sharpe | Test Return | Test Max DD | 交易数 |
|------|----------|---------|--------------|-------------|-------------|-------------|--------|
| W1 | 2015-01-01 ~ 2017-12-31 | 2017-12-31 ~ 2018-12-31 | 1.69 | 2.01 | 26.26% | -4.97% | 470 |
| W2 | 2016-01-01 ~ 2018-12-31 | 2018-12-31 ~ 2019-12-31 | 2.06 | 0.75 | 6.83% | -5.94% | 738 |
| W3 | 2017-01-01 ~ 2019-12-31 | 2019-12-31 ~ 2020-12-30 | 2.06 | 0.77 | 8.56% | -8.93% | 672 |
| W4 | 2018-01-01 ~ 2020-12-31 | 2020-12-31 ~ 2021-12-31 | 2.07 | 0.95 | 10.76% | -6.27% | 512 |
| W5 | 2019-01-01 ~ 2021-12-31 | 2021-12-31 ~ 2022-12-31 | 1.85 | 0.18 | 1.85% | -6.32% | 632 |
| W6 | 2020-01-01 ~ 2022-12-31 | 2022-12-31 ~ 2023-12-31 | 1.58 | 1.42 | 9.99% | -3.48% | 424 |
| W7 | 2021-01-01 ~ 2023-12-31 | 2023-12-31 ~ 2024-12-30 | 1.80 | -0.45 | -3.47% | -7.16% | 534 |
| W8 | 2022-01-01 ~ 2024-12-31 | 2024-12-31 ~ 2025-12-31 | 0.97 | 0.38 | 2.93% | -5.62% | 444 |

### 3.2 IC88.CFFEX

#### Expanding WFO

| 指标 | 数值 |
|------|------|
| 窗口数 | 8 |
| WFE | 0.05 |
| Consistency | 50.0% |
| Avg Test Sharpe | 0.35 |
| Avg Test Return | 5.39% |
| Avg Test Max DD | -9.49% |
| Concatenated OOS Sharpe | 0.50 |
| Concatenated OOS Return | 43.10% |
| 过拟合风险 | **HIGH** |
| 可实盘 | **False** |

| 窗口 | Train 期 | Test 期 | Train Sharpe | Test Sharpe | Test Return | Test Max DD | 交易数 |
|------|----------|---------|--------------|-------------|-------------|-------------|--------|
| W1 | 2015-01-01 ~ 2018-01-01 | 2018-01-01 ~ 2019-01-01 | 2.49 | -0.85 | -7.85% | -15.62% | 846 |
| W2 | 2015-01-01 ~ 2019-01-01 | 2019-01-01 ~ 2020-01-01 | 1.94 | 0.32 | 3.13% | -5.01% | 822 |
| W3 | 2015-01-01 ~ 2020-01-01 | 2020-01-01 ~ 2021-01-01 | 1.70 | 2.02 | 23.41% | -4.17% | 822 |
| W4 | 2015-01-01 ~ 2021-01-01 | 2021-01-01 ~ 2022-01-01 | 1.72 | -1.35 | -13.80% | -18.75% | 726 |
| W5 | 2015-01-01 ~ 2022-01-01 | 2022-01-01 ~ 2023-01-01 | 1.41 | -0.15 | -1.77% | -12.35% | 814 |
| W6 | 2015-01-01 ~ 2023-01-01 | 2023-01-01 ~ 2024-01-01 | 1.39 | -0.92 | -8.14% | -12.07% | 436 |
| W7 | 2015-01-01 ~ 2024-01-01 | 2024-01-01 ~ 2025-01-01 | 1.24 | 2.09 | 26.87% | -4.03% | 578 |
| W8 | 2015-01-01 ~ 2025-01-01 | 2025-01-01 ~ 2025-12-31 | 1.24 | 1.60 | 21.25% | -3.92% | 536 |

#### Rolling WFO

| 指标 | 数值 |
|------|------|
| 窗口数 | 8 |
| WFE | 0.41 |
| Consistency | 62.5% |
| Avg Test Sharpe | 0.65 |
| Avg Test Return | 6.73% |
| Avg Test Max DD | -7.67% |
| Concatenated OOS Sharpe | 0.72 |
| Concatenated OOS Return | 53.84% |
| 过拟合风险 | **MODERATE** |
| 可实盘 | **True** |

| 窗口 | Train 期 | Test 期 | Train Sharpe | Test Sharpe | Test Return | Test Max DD | 交易数 |
|------|----------|---------|--------------|-------------|-------------|-------------|--------|
| W1 | 2015-01-01 ~ 2017-12-31 | 2017-12-31 ~ 2018-12-31 | 2.53 | -0.81 | -7.83% | -15.08% | 874 |
| W2 | 2016-01-01 ~ 2018-12-31 | 2018-12-31 ~ 2019-12-31 | 1.86 | 0.47 | 3.47% | -4.50% | 520 |
| W3 | 2017-01-01 ~ 2019-12-31 | 2019-12-31 ~ 2020-12-30 | 1.62 | 2.09 | 20.10% | -2.85% | 404 |
| W4 | 2018-01-01 ~ 2020-12-31 | 2020-12-31 ~ 2021-12-31 | 1.41 | -0.63 | -5.82% | -14.12% | 376 |
| W5 | 2019-01-01 ~ 2021-12-31 | 2021-12-31 ~ 2022-12-31 | 1.03 | 0.73 | 8.21% | -7.71% | 456 |
| W6 | 2020-01-01 ~ 2022-12-31 | 2022-12-31 ~ 2023-12-31 | 1.32 | -0.70 | -5.38% | -7.84% | 360 |
| W7 | 2021-01-01 ~ 2023-12-31 | 2023-12-31 ~ 2024-12-30 | 0.50 | 2.18 | 22.51% | -4.73% | 414 |
| W8 | 2022-01-01 ~ 2024-12-31 | 2024-12-31 ~ 2025-12-31 | 1.52 | 1.86 | 18.59% | -4.48% | 376 |

![WFO Window Comparison](ldt_if_ic_2015_deep_dive/wfo_window_comparison.png)

![Concatenated OOS PnL](ldt_if_ic_2015_deep_dive/concatenated_oos_pnl.png)

---

## 4. Expanding vs Rolling 对比分析

| 品种 | WFO 类型 | WFE | Consistency | Avg Test Sharpe | Concatenated OOS Sharpe | 过拟合风险 | 可实盘 |
|------|----------|-----|-------------|-----------------|-------------------------|------------|--------|
| IF88.CFFEX | Expanding | 0.40 | 62.5% | 0.61 | 0.66 | moderate | True |
| IF88.CFFEX | Rolling | 0.42 | 87.5% | 0.75 | 0.83 | moderate | True |
| IC88.CFFEX | Expanding | 0.05 | 50.0% | 0.35 | 0.50 | high | False |
| IC88.CFFEX | Rolling | 0.41 | 62.5% | 0.65 | 0.72 | moderate | True |

---

## 5. 结论与风险提示

### 结论

1. **IF88.CFFEX 综合推荐实盘**
   - GA 全样本 Sharpe 1.20，总收益 108.44%，最大回撤 -7.98%，通过全部 IS 门槛。
   - Expanding WFO: deployable=True，WFE=0.40，Consistency=62.5%，Avg Test Sharpe=0.61，过拟合风险 moderate。
   - Rolling WFO: deployable=True，WFE=0.42，Consistency=87.5%，Avg Test Sharpe=0.75，过拟合风险 moderate。
   - Rolling 比 Expanding 更稳健（Consistency 87.5% vs 62.5%），说明使用最近 3 年数据重新优化参数，能更好适应市场环境变化。
   - **建议实盘参数**：采用 IF88 Rolling WFO 最后一个窗口（W8, 2022-01-01 ~ 2024-12-31 Train）的最优参数：
     - k1=0.52, k2=0.66, trailpercent=0.45, range_cap=3, exit_time_type=1, need_lock=3, fixed_size=1, trade_limit=2

2. **IC88.CFFEX 不推荐实盘**
   - GA 全样本 Sharpe 1.29，总收益 190.29%，最大回撤 -6.71%，IS 表现优秀。
   - Expanding WFO: deployable=False，WFE=0.05，Consistency=50%，过拟合风险 high。说明从 2015 年开始累积训练时，参数对远期市场适应性差。
   - Rolling WFO: deployable=True，WFE=0.41，Consistency=62.5%，Avg Test Sharpe=0.65，过拟合风险 moderate。Rolling 显著优于 Expanding，但 Expanding 失败意味着策略在 IC88 上的长期参数稳定性不足。
   - 鉴于同一策略在 IF88 上两种 WFO 均通过，而 IC88 仅 Rolling 通过，IC88 仅列为**观察对象**，不建议作为首批实盘候选。

3. **Expanding vs Rolling 对比洞察**
   - 对 LDT 这种日内突破策略，**Rolling WFO 明显更稳健**：IF88 Consistency 提升 25pct，IC88 从 high 风险降至 moderate 风险。
   - 原因可能在于股指期货市场结构、波动率和监管环境在 2015-2025 年间发生显著变化，固定 3 年滚动窗口更能捕捉近期市场特征，而累积全部历史数据的 Expanding 窗口会过度拟合早期 regimes。
   - **后续深度挖掘建议**：对日内/短线策略默认优先使用 Rolling WFO，或缩短 Train 窗口长度进行敏感性测试。

### 风险提示

1. **过拟合风险**：即使 Rolling WFO 通过，Train Sharpe 仍普遍高于 Test Sharpe，实盘表现可能低于样本外。
2. **市场环境变化**：2015 年股灾、2017 年低波动、2020 年疫情、2024 年政策变化等 regimes 均在样本内，未来新 regime 可能导致策略失效。
3. **杠杆与仓位**：名义仓位按 10% 资本金计算，股指期货保证金约 12-15%，实际杠杆可能接近 1 倍或更高，需严格控制仓位。
4. **品种差异**：IF88 与 IC88 波动率、保证金、流动性不同，即使同一策略参数也不宜直接套用。
5. **执行风险**：日内策略依赖分钟级数据和低延迟执行，滑点、网络延迟、交易时段限制均可能影响实盘绩效。

---

## 6. 输出文件

| 文件 | 路径 |
|------|------|
| 本报告 | `{REPORT_DIR}/ldt_if_ic_2015_deep_dive.md` |
| 报告图表 | `{ASSET_DIR}/` |
| IF88 GA 最优参数 | `data/pipeline/ldt_if88_2015_ga_v2/LimitedDualThrustStrategy_IF88_CFFEX/best_params_*.json` |
| IC88 GA 最优参数 | `data/pipeline/ldt_ic88_2015_ga_v2/LimitedDualThrustStrategy_IC88_CFFEX/best_params_*.json` |
| IF88 Expanding WFO | `data/pipeline/ldt_if88_2015_wfo_v3/wfo/LimitedDualThrustStrategy_IF88_CFFEX/wfo_summary.json` |
| IC88 Expanding WFO | `data/pipeline/ldt_ic88_2015_wfo_v3/wfo/LimitedDualThrustStrategy_IC88_CFFEX/wfo_summary.json` |
| IF88 Rolling WFO | `data/pipeline/ldt_if88_2015_wfo_rolling/wfo/LimitedDualThrustStrategy_IF88_CFFEX/wfo_summary.json` |
| IC88 Rolling WFO | `data/pipeline/ldt_ic88_2015_wfo_rolling/wfo/LimitedDualThrustStrategy_IC88_CFFEX/wfo_summary.json` |
