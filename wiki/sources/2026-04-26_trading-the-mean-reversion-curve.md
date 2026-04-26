# Trading the Mean Reversion Curve — 深度处理

**来源**: [Substack](https://open.substack.com/pub/quantitativo/p/trading-the-mean-reversion-curve)
**作者**: Quantitativo (Quant Trading Rules)
**日期**: 2026-04-26
**标签**: #mean-reversion #RSI2 #portfolio-diversification #parameter-ensemble #Nasdaq-100

## 一句话摘要

PJ Sutherland 的"交易均值回归曲线"思想——用一个多参数均值回归策略组合（不同 RSI2 入场阈值）配合月度再平衡的 Sharpe 优化分配算法，解决单一参数策略近年衰减问题，实现 2010 年以来年化 25.7% 收益。

## 完整规则（最终 Diversified System）

### 入场规则

```
每个交易开盘：
1. 对 Nasdaq-100 成分股
2. 筛选价格 > 200-day SMA 的股票
3. 计算 2-period RSI，根据 6 个阈值(5,10,15,20,25,30)生成 6 个子组合
4. 每个子组合：选 RSI2 < 对应阈值 的股票，按 NATR 排序取优先高波动
5. 总组合：根据月再平衡算法分配 6 个子组合的权重
6. 资金分为 4 个槽位
```

### 出场规则

```
股票收盘价 > 昨日高点 → 下一开盘出场
```

### 仓位管理

- 最大 10 个持仓（最终用 4-slot 效果更好）
- 月再平衡：每月初重新优化权重
- 回望期：504 天（约 2 年）
- 优化目标：最大化 Sharpe 比率

### 组合权重算法

```
1. 回望过去 504 天每个子组合的表现
2. 用线性优化(或搜索)找到 6 个权重使组合 Sharpe 最大
3. 43% 时间仅选最优单一策略
4. 40% 时间分配给 2 个策略
5. 几乎不分配给 4+ 策略
```

## 回测数据

| 指标 | Base (RSI2<5) | 宽松 (RSI2<10) | 4-slot | **Diversified (2010+)** |
|------|-------------|-------------|---------|------------------------|
| 年化收益 | 18% | 25% | 34% | **25.7%** |
| 基准收益 | 12% | - | - | **17.6%** |
| 最大回撤 | 21% | 25% | 35% | **28%** |
| Sharpe | 1.14 | 1.23 | 1.23 | **1.14** |
| 基准 Sharpe | - | - | - | **0.89** |
| 胜率 | 58% | - | - | **64.8%** |
| 每笔收益 | +0.88% | +0.79% | - | **+0.40%** |
| 每笔收益比 | 0.87 | 0.78 | - | **0.72** |
| 年交易次数 | 170 | 239 | - | - |
| 暴露时间 | 83% | 93% | - | - |

### 月度统计 (Diversified, 2010+)
- 正向月：66%
- 最佳月：+20.1% (Jul'23)
- 最差月：-15.2% (May'19)
- 最长连胜：9 个月 (Dec'16-Aug'17)
- 最长连败：4 个月 (Jun'15-Sep'15)
- 亏损年：2 年（含当前年份）

## 伪代码框架

```python
# 配置
THRESHOLDS = [5, 10, 15, 20, 25, 30]
MAX_POSITIONS = 10  # 或 4
LOOKBACK = 504      # 交易日
REBALANCE_FREQ = 21 # 月频（交易日）

class MeanReversionCurve:
    def __init__(self):
        self.portfolio_weights = [1/6] * 6
        self.last_rebalance = 0
        self.positions = []

    def on_bar(self, date, universe):
        # Step 1: 月再平衡检查
        if days_since(self.last_rebalance) >= REBALANCE_FREQ:
            self.portfolio_weights = self.optimize_weights(date)

        # Step 2: 对每个阈值生成信号
        signals_by_threshold = []
        for t in THRESHOLDS:
            candidates = [
                s for s in universe
                if rsi2(s) < t and close(s) > sma(s, 200)
            ]
            sorted_by_vol = sorted(candidates, key=natr, reverse=True)
            signals_by_threshold.append(sorted_by_vol[:MAX_POSITIONS])

        # Step 3: 按权重分配资金
        final_signals = weighted_merge(signals_by_threshold, self.portfolio_weights)

        # Step 4: 出场管理（收盘>昨日高点 → 下次出场）
        for pos in self.positions:
            if close(pos.stock) > high(pos.stock, -1):
                schedule_exit(pos, datetime.now())

        # Step 5: 入场
        for stock in final_signals:
            if len(self.positions) < MAX_POSITIONS:
                enter_long(stock, position_sizing)

    def optimize_weights(self, current_date):
        # 回望 LOOKBACK 天
        start_date = current_date - LOOKBACK
        best_sharpe = -inf
        best_weights = None
        for weights in search_combinations():
            port_returns = combine_portfolios(weights, THRESHOLDS, start_date)
            sharpe = calculate_sharpe(port_returns)
            if sharpe > best_sharpe:
                best_sharpe = sharpe
                best_weights = weights
        return best_weights
```

## 局限性与风险

1. **近年衰减**：2021 年以来仅 7.1% 年化 vs Nasdaq-100 13.4%，暴露均值回归策略长期衰减
2. **交易成本敏感**：高换手率（每笔交易 +0.40% 预期收益，需要控制滑点）
3. **月度间隙风险**：周末跳空标准差 1.4%，限制了再平衡频率
4. **仅 Nasdaq-100**：回测仅基于 Nasdaq-100 成分股，外推性有限
5. **数据时间范围**：核心策略从 1998 年开始测试，但近年衰减需要持续监控
6. **过拟合风险**：504 天回望 + 月度再平衡是经过参数搜索选择的结果
7. **生产级补充**：作者明确表示有未公开的改进（更高单笔收益、调整分散算法、更优下跌表现）

## 五维度评价

| 维度 | 评分 | 说明 |
|------|------|------|
| 数据质量 | ⭐⭐⭐⭐ | RealTest 双重认证，Nasdaq-100 成分股，Norgate Data |
| 规则完整性 | ⭐⭐⭐⭐ | 完整入场/出场/仓位规则，阈值可调 |
| 可操作性 | ⭐⭐⭐ | 需要组合优化算法 + 40+ 股票监控 + 换手成本 |
| 风险透明度 | ⭐⭐⭐⭐ | 完整回撤、月度盈亏、近期衰减讨论 |
| 新颖性 | ⭐⭐⭐⭐⭐ | PJ Sutherland 的"均值回归曲线"参数分散思想独特 |

**总评**: 🟡 **Yellow**（有生产价值的框架，但近期衰减未完全解决，+ 作者保留关键改进）

## 与现有知识的关系

- 与 [[RSI2 均值回归策略]] 系列高度相关 —— 同一作者的改进版
- 与 [[Larry Connors RSI2 策略]] 有相似逻辑但加入了参数分散组合
- 参数分散思想与 [[Dual Momentum]] 的组合思路类似，但应用于同一策略的不同参数化而非不同资产
- 策略近年衰减印证[[均值回归策略长期衰减]]现象
- 与 [[PJ Sutherland All-Weather 组合]] 概念相通

## 回测验证 (2026-04-26, QQQ 单品种替代)

用 QQQ 日线数据（2016-2026）对基础 RSI2 策略做初步验证：

| RSI2阈值 | 总收益% | 交易次数 | Sharpe | 最终资金 |
|---------|--------|---------|--------|---------|
| 5 | 11.32% | 32 | 2.78 | $1,113,238 |
| 10 | 6.26% | 66 | 1.50 | $1,062,562 |
| 15 | 17.88% | 92 | 2.24 | $1,178,752 |
| 20 | 18.58% | 113 | 1.86 | $1,185,771 |
| 25 | 41.84% | 126 | 2.65 | $1,418,390 |
| **30** | **66.33%** | **155** | **3.04** | **$1,663,308** |

**发现**：
1. 放宽阈值提高交易频率的同时总收益也提升（与文章一致）
2. 单品种（QQQ）信号远少于文章用的 100 只 Nasdaq-100 个股
3. 2025-02-21 到 03-14 最大单笔亏损 -9.15%
4. 2017-12 到 2019-01 持仓 374 天才触发退出条件（close > 前日 high）
5. 基础逻辑验证通过，但多品种组合效果需要完整 Nasdaq-100 数据才能复现

## 思考链

1. Base strategy: RSI2<5, 200d SMA filter → 18%年化, 但2008年后衰减
2. 放宽阈值到10 → 25%年化, 但10年后still lagging to benchmark
3. 减少持仓到4个 → 34%年化, 但回撤35%
4. 核心问题: 单一参数组合近年衰减
5. 解决方案: 多阈值参数分散(5,10,15,20,25,30) + Sharpe优化分配
6. 关键发现: 43%时间只选最优1个, 40%时间选2个, 策略自动切换
7. 限制: 周末跳空风险使周再平衡不可行 → 月再平衡
8. 最终: 25.7%年化(2010+), Sharpe 1.14 vs 0.89 benchmark, 但2021年后仍显弱
