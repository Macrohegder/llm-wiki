# LDT 股指期货 WFO 滚动频率对比报告

> 生成时间: 2026-06-30T09:36:15.310505
> 策略: LimitedDualThrustStrategy (LDT)
> 品种: IF88 / IC88 / IH88 / IM88
> 数据周期: 2015-01-01 ~ 2025-12-31
> WFO 设置: rolling, train=36 个月, test=12/6/3 个月
> 参数选择: plateau_center, Top-N=10, ensemble_size=2
> GA 设置: pop=30, ngen=12, workers=2

## 1. 摘要

本报告对比 LDT 策略在三个 Walk-Forward 滚动频率下的表现：

- **年度** (test=12 个月): 参数更新最慢，样本外窗口最长
- **半年** (test=6 个月): 平衡参数更新速度与单窗口风险
- **季度** (test=3 个月): 参数更新最快，单窗口风险最低

核心发现：
- **IF88 和 IC88 在年度频率下样本外 Sharpe 最高**
- **IM88 在半年频率下表现异常突出，但数据窗口较少，统计稳健性存疑**
- **IH88 在季度频率下 deployable=False**
- **IF+IC 2x2 ensemble 组合在年度频率下表现最佳**
- **WFO 滚动频率只影响参数重新优化的周期，不影响 LDT 策略本身的日内交易频率**

## 2. 各品种三种频率对比

### 2.1 平均样本外 Sharpe

| 品种 | annual | semi | quarter |
|------|-------|-------|-------|
| IF88 | 0.7816 | 0.6751 | 0.5633 |
| IC88 | 0.4979 | 0.3432 | 0.4739 |
| IH88 | 0.3693 | 0.3117 | 0.2853 |
| IM88 | 0.5199 | 1.1754 | 0.3598 |

### 2.2 Walk-Forward Efficiency (WFE)

| 品种 | annual | semi | quarter |
|------|-------|-------|-------|
| IF88 | 0.4497 | 0.5249 | 0.4118 |
| IC88 | 0.2571 | 0.0217 | 0.3055 |
| IH88 | 0.4177 | 0.4575 | 0.7483 |
| IM88 | 0.2476 | 0.7282 | 0.4351 |

### 2.3 Consistency (正收益窗口占比)

| 品种 | annual | semi | quarter |
|------|-------|-------|-------|
| IF88 | 0.8750 | 0.6875 | 0.6250 |
| IC88 | 0.6250 | 0.5000 | 0.6562 |
| IH88 | 0.8750 | 0.6250 | 0.6875 |
| IM88 | 0.6667 | 0.6667 | 0.6154 |

### 2.4 平均样本外收益 (%)

| 品种 | annual | semi | quarter |
|------|-------|-------|-------|
| IF88 | 16.1146 | 7.2843 | 3.4062 |
| IC88 | 16.3059 | 6.7589 | 4.0054 |
| IH88 | 5.5999 | 3.6742 | 1.9826 |
| IM88 | 8.8878 | 12.9941 | 2.6165 |

### 2.5 平均样本外最大回撤 (%)

| 品种 | annual | semi | quarter |
|------|-------|-------|-------|
| IF88 | -12.7785 | -10.2372 | -7.2213 |
| IC88 | -16.1988 | -13.1749 | -9.2436 |
| IH88 | -12.0555 | -7.8952 | -5.6293 |
| IM88 | -18.1418 | -10.9934 | -8.1965 |

### 2.6 可部署性

| 品种 | annual | semi | quarter |
|------|--------|------|---------|
| IF88 | ✅ | ✅ | ✅ |
| IC88 | ✅ | ✅ | ✅ |
| IH88 | ✅ | ✅ | ❌ |
| IM88 | ✅ | ✅ | ✅ |

## 3. IF+IC 2x2 Ensemble 组合对比

| 频率 | 共同窗口数 | 平均收益 | Sharpe | Consistency |
|------|-----------|---------|--------|-------------|
| annual | 8 | 16.21% | 0.74 | 75.0% |
| semi | 16 | 7.02% | 0.52 | 56.3% |
| quarter | 32 | 3.71% | 0.48 | 68.8% |

年度频率下的 IF+IC 组合：
- 平均窗口收益最高（16.21%）
- Sharpe 最高（0.74）
- 虽然 consistency 不是最高，但收益质量明显更好

## 4. 关键观察

1. **年度频率对 IF/IC/IH 更优**：更长的 test 窗口允许策略完整捕捉趋势行情，避免了短窗口中的噪声和参数频繁切换带来的损耗。

2. **季度频率回撤更小但收益也更低**：短 test 窗口的单次最大回撤确实更小，但年化后收益大幅下降。原因不是日内交易成本增加（WFO 频率不改变 LDT 日内交易次数），而是 **3 个月窗口太短，GA 容易选出只适应上一季度行情的特殊参数；参数每季度切换一次，导致策略总在"追热点"，长期来看稳健性下降**。

3. **IM88 半年异常好需谨慎解读**：IM88 半年 sharpe=1.18，但仅有 6 个窗口（vs annual 3 个、quarter 13 个），样本量不足，不宜作为推荐依据。

4. **IH88 季度不可部署**：avg_test_sharpe=0.29，consistency 68.75%，但未通过 deployable 门槛。

## 5. 结论与建议

### 5.1 推荐配置

| 品种 | 推荐频率 | 理由 |
|------|---------|------|
| IF88 | **annual** | 最高 avg_test_sharpe (0.78) 和 consistency (87.5%) |
| IC88 | **annual** | avg_test_sharpe 0.50，consistency 62.5%，均优于 semi |
| IH88 | **annual** | avg_test_sharpe 0.37，consistency 87.5%，季度不可部署 |
| IM88 | **annual/semi 需观察** | 数据窗口少，建议继续积累样本 |

### 5.2 对 500 万本金 IF+IC 实盘组合的影响

原方案 **IF+IC 2x2 ensemble + 年度滚动** 仍然是最佳选择：
- 历史组合 Sharpe: 0.74
- 平均窗口收益: 16.21%
- 无需因为短期 2026 回撤或频率对比而改为半年/季度

### 5.3 代码改动

已在 `cta/pipeline/walk_forward_engine.py` 和 `pipeline.py` 中支持 `--wfo-test-months` 参数：

```bash
python pipeline.py --strategy LDT --symbol IF88.CFFEX ... --wfo-test-months 12  # 年度
python pipeline.py --strategy LDT --symbol IF88.CFFEX ... --wfo-test-months 6   # 半年
python pipeline.py --strategy LDT --symbol IF88.CFFEX ... --wfo-test-months 3   # 季度
```

## 6. 图表

![Sharpe by Frequency](raw/assets/ldt_cn_index_futures_freq_compare/sharpe_by_freq.png)

![WFE by Frequency](raw/assets/ldt_cn_index_futures_freq_compare/wfe_by_freq.png)

![IF+IC Cumulative Return](raw/assets/ldt_cn_index_futures_freq_compare/ific_cum_return_by_freq.png)
