# CL 跨市场套利深度分析报告

**Date**: 2026-04-20
**Analyst**: AI Research Agent
**Data Sources**: Hyperliquid API, OKX API, Trading Research Hub (pedma, 2026-04-09)
**Tags**: #arbitrage #cross-exchange #funding-rate #crude-oil #hyperliquid #okx #cme

---

## 执行摘要

| 套利路径 | 可行性 | 核心原因 |
|-----------|--------|---------|
| HL ↔ OKX 跨市场 | ❌ **不可行** | HL 的 CL 合约已下架 |
| OKX 内部 Funding 套利 | ❌ **不可行** | 无 CL 现货对冲，funding 收益低于波动风险 |
| CME ↔ OKX 跨市场 | ⚠️ **边际可行** | 收益极低，结构成本高，不适合个人交易者 |

**关键发现: OKX 存在严重结构性风险——其 CL-USDT 指数 50% 权重引用了已下架的 HL CL/USDC 合约。**

---

## 1. 市场现状

### 1.1 Hyperliquid (HL)

**WTIOIL 已下架**
- API 返回 HTTP 500（Internal Server Error）
- `allMids` 中不存在 WTIOIL 或 CL
- `universe` 中 229 个资产均为加密货币，无任何原油相关合约
- 文章（2026-04-09）提到 deployer 为 tradexyz，该合约可能是通过 HL 的部署功能上市的，但现已下架

### 1.2 OKX

**CL-USDT-SWAP 永续合约规格**

| 参数 | 值 |
|------|-----|
| 合约类型 | 线性永续 (Linear Perp) |
| 合约价值 (ctVal) | 0.1 桶/ 张 |
| 最小下单 (minSz) | 1 张 |
| 最大杠杆 | 50x |
| 价格精度 (tickSz) | $0.01 |
| 结算货币 | USDT |
| 开仓方式 | fix_price |
| 状态 | live |

**流动性**

| 指标 | 数值 |
|------|------|
| 24h 成交量 | 7,841,909 张 ≈ 784,191 桶 ≈ $69.2M |
| 持仓量 (OI) | 2,259,154 张 ≈ 225,915 桶 ≈ $19.9M |
| 买卖价差 | $0.01 = 1.13 bps |
| Bid 深度 | 1,482 张 ≈ $130K |
| Ask 深度 | 445 张 ≈ $39K |

**当前价格**
- Last: $88.22
- Mark: $88.24
- Index: $88.118
- Premium: (88.24 - 88.118) / 88.118 = 0.138%

---

## 2. 指数成分分析

### 2.1 OKX CL-USDT Index 构成

```
CL-USDT Index = 0.5 × HL_CL/USDC + 0.5 × OKX_CL-USDT-SWAP
```

实际数据（2026-04-20）：
- HL CL/USDC: $88.06 ← **但 HL 上已无此合约**！
- OKX CL-USDT-SWAP: $88.28
- Index Last: $88.147

### 2.2 结构性风险

**这是一个严重问题**：

1. OKX 的指数 50% 权重引用了已下架的 HL 合约
2. 如果 HL 价格是 stale 的，则 index 不反映真实市场价格
3. Funding rate = (Mark - Index) / Index，index 失真会导致 funding rate 被扭曲
4. 任何依赖于 funding rate 的套利策略都面临指数风险

---

## 3. Funding Rate 深度分析

### 3.1 基本统计（169 个周期，约 46 天）

| 指标 | 每 8h | 每日 | 年化 |
|------|--------|-------|-------|
| 平均 | +0.0030% | +0.0089% | +3.25% |
| 标准差 | 0.0959% | 0.2878% | 105.0% |
| 最大 | +0.391% | +1.173% | +428% |
| 最小 | -0.394% | -1.181% | -431% |

### 3.2 分布特征

| 类别 | 次数 | 占比 | 平均强度 |
|------|------|------|----------|
| 正 funding | 78 | 46.2% | +0.0617% |
| 负 funding | 43 | 25.4% | -0.1003% |
| 零 funding | 48 | 28.4% | 0% |

### 3.3 连续性分析

| 方向 | 最长连续 | 平均连续 |
|------|----------|----------|
| 正 streak | 42 周期 (14 天) | 9.8 周期 (3.3 天) |
| 负 streak | 19 周期 (6.3 天) | 7.2 周期 (2.4 天) |

### 3.4 累计收益

- 46 天总计：多头支付 0.50%，空头收取 0.50%
- 年化等效：空头约 +3.96%/年

### 3.5 价格滚动效应

OKX CL 永续合约也在经历 roll：
- 4月12日: ~$97.52
- 4月20日: ~$88.22
- 幅度: -9.5% (约 8 天内)

这正是 backwardation + 合约滚动的结果，与文章描述的 HL WTIOIL 机制完全一致。

---

## 4. 套利路径评估

### 4.1 路径一：HL ↔ OKX 跨市场

**状态: ❌ 不可行**

- HL 的 CL 合约已不存在
- 无法建立对冲仓位
- OKX 的 index 仍然引用 HL 价格，这本身就是一个红旗

### 4.2 路径二：OKX 内部 Funding 套利

**策略**: Short CL perp → 收取 funding
**问题**: 需要 delta 对冲

**对冲选项**
| 对冲方式 | 可行性 | 说明 |
|---------|--------|------|
| OKX CL 现货 | ❌ 不存在 | OKX 无 CL 现货交易对 |
| OKX 相关资产 | ❌ 无 | 无直接相关的可对冲资产 |
| CME 期货 | 可行但复杂 | 见路径三 |

**无对冲情况下的风险**

| 项目 | 数值 |
|------|------|
| Funding 收益 (46天) | +0.50% |
| 年化 funding 收益 | +3.96% |
| 年化波动率 | 106% |
| 46天价格变动 | -9.5% |
| 风险/收益比 | 空头短期暴跌 9.5% 的风险 vs 0.50% 的 funding 收益 |

**结论**: 无对冲的 funding 套利等于赌博方向。价格波动远大于 funding 收益，不值得。

### 4.3 路径三：CME ↔ OKX 跨市场

**策略**: Long CME CL 期货 + Short OKX CL perp

**收益来源**

| 来源 | 年化收益 | 说明 |
|------|----------|------|
| OKX funding | +3.96% | 46天平均，波动极大 |
| Basis 收益 | 不确定 | CME 与 OKX 价格差异 |
| Roll yield | 负 | Backwardation 时每次 roll 亏损 |

**成本分析**

| 项目 | 计算 | 结果 |
|------|------|------|
| OKX 开仓费 | 0.05% × 2 | 0.10% |
| OKX 平仓费 | 0.05% × 2 | 0.10% |
| CME 手续费 | ~$5 / $88K | 0.006% |
| CME roll cost | ~$1-2/桶/月 | 年化约 13-27% |
| 资金效率损失 | CME 8% vs OKX 2% | 约 6% 资金闲置 |
| 时间缺口风险 | CME 休市期间 | 无法对冲 |

**关键问题**

1. **Roll cost 吞噬收益**: CME CL 每月 roll，backwardation 时近月 > 远月。每次 roll 亏损 $1-2/桶，年化约 13-27%，远超 funding 收益。

2. **OKX index 不稳定**: 指数 50% 权重引用下架合约，mark/index 关系可能失真。

3. **波动率吞噬**: 106% 年化波动率意味着任何小的 basis 偏离都可能造成巨大亏损。

4. **资金效率**: CME 需要 8% 保证金，OKX 仅需 2%。对于 $100K 的对冲仓位，需要 $8K CME + $2K OKX = $10K 保证金。如果 funding 收益仅 3.96%，$100K 名义价值仅赚 $3,960/年。考虑到 $10K 保证金，实际 ROI 约 39.6%。但减去 roll cost (13-27%)、费用 (0.2%)、风险准备金，净收益可能接近零或为负。

---

## 5. 为什么会持续存在价差？

### 5.1 机制性原因

1. **合约滚动**: OKX 的 CL perp 跟踪的是包含 CME 期货的指数，每月需要 roll，backwardation 时产生粘性折价
2. **指数构成差异**: OKX index = 50% HL + 50% OKX，但 HL 已下架，导致 index 失真
3. **持仓不平衡**: 加密货币市场对 CL 的需求不对称，多头/空头比例持续偏离
4. **流动性分散**: 虽然 OKX CL 有 $69M 日成交，但相对于 CME 仍然很小，大单影响显著

### 5.2 为什么套利者不能平活

| 障碍 | 说明 |
|------|------|
| Roll cost | CME 每月 roll 亏损吞噬整体收益 |
| 结构性风险 | OKX index 失真、USDT 脱钩风险 |
| 资金效率 | CME 保证金要求高，拉低实际 ROI |
| 时间缺口 | CME 休市期间无法对冲 |
| 流动性 | 小规模套利者资金不足以影响市场 |

---

## 6. 结论

### 6.1 核心发现

1. **HL 的 CL 合约已下架**，跨市场套利在技术上已不可行
2. **OKX 的 CL index 存在结构性缺陷**，50% 权重引用下架合约
3. **OKX CL perp 也在经历同样的 roll/backwardation 机制**，价格从 $97 跌至 $88
4. **Funding rate 平均仅 +3.25% 年化**，但波动极大（-431% 到 +428%）
5. **CME roll cost 约 13-27% 年化**，远超 funding 收益

### 6.2 套利可行性评级

| 路径 | 评级 | 理由 |
|------|------|------|
| HL ↔ OKX | ❌ 不可行 | 合约已下架 |
| OKX 内部 | ❌ 不可行 | 无对冲工具，波动吞噬收益 |
| CME ↔ OKX | ⚠️ 边际 | 结构成本高，适合机构而非个人 |

### 6.3 建议

对于个人量化交易者：
- **不建议参与** CL 跨市场套利
- 结构性成本远超可见收益
- OKX index 的不稳定性增加了额外风险
- 如果必须参与，建议仅用极小仓位测试，并密切监控 OKX index 成分变化

---

## 附录: 数据来源与约定

- Hyperliquid API: https://api.hyperliquid.xyz/info
- OKX API: https://www.okx.com/api/v5/
- Trading Research Hub: https://www.tradingresearchub.com/p/why-is-the-wtioil-contract-on-hyperliquid
- 数据采集时间: 2026-04-20 UTC
- OKX 费率: VIP 0 Maker 0.02%, Taker 0.05% (参考值)
- CME 费率: 参考行业标准

## Related
- [[2026-04-09-wtioil-hyperliquid-funding]]
- [[Cross-Exchange Arbitrage]]
- [[Funding Rate Mechanics]]
- [[Contract Roll]]
