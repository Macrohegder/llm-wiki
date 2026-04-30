---
id: crypto-strategies-analysis-2026-04-30-v2
title: "CTA Developer Crypto批量回测报告 (2026-04-30)"
date: "2026-04-30"
tags:
  - crypto
  - synthesis
  - backtest-analysis
  - cta-developer
  - batch-pipeline
---

# CTA Developer Crypto批量回测报告

> 知识合成页 | 基于 cta_developer batch pipeline 在 OKX 加密货币永续合约上的回测
> 创建：2026-04-30 | 作者：Raymond Hsiao
> 数据区间：2020-01-01 ~ 2026-04-29
> 数据来源：直接从 `data/pipeline/` 各策略独立目录解析（绕过 batch_results 去重 bug）

---

## 一、测试概况

| 项目 | 内容 |
|------|------|
| 测试框架 | cta_developer batch pipeline |
| 策略数量 | 8 个 (CINCO, TRS, RSI2, SMF, PR, NR7, FDLR, GE) |
| Crypto品种 | 4 个 (BTC, ETH, SOL, DOGE) |
| 总任务数 | 32 (8×4) |
| 回测区间 | 2020-01-01 ~ 2026-04-29 |
| 初始资金 | $1,000,000 |
| 优化方法 | OAT + GA |

---

## 二、各策略Crypto表现汇总

### 2.1 策略表现总览

| 策略 | 平均Sharpe | 最佳品种 | 最佳Sharpe | 评价 |
|------|-----------|---------|------------|------|
| CINCO | 1.149 | ETH | 1.307 | 🟢 全场最佳，4品种全部>1.0 |
| TRS | 0.902 | BTC | 1.397 | 🟢 极强，BTC Sharpe=1.4 |
| RSI2 | 0.763 | SOL | 0.892 | 🟢 稳定，所有品种>0.71 |
| SMF | 0.608 | SOL | 0.742 | 🟡 良好 |
| PR | 0.511 | ETH | 0.722 | 🟡 可接受 |
| NR7 | 0.331 | BTC/ETH | 0.591 | 🟡 一般 |
| FDLR | 0.247 | BTC | 0.620 | 🟡 较弱 |
| GE | -0.101 | BTC | 0.251 | 🔴 仅BTC勉强正 |

### 2.2 详细数据

#### CINCO (CincoStrategy) — 全场最佳

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| ETH | 1.307 | 160 | -0.99% | 1.35% | 8.40% | ✅ |
| SOL | 1.244 | 128 | -1.61% | 1.68% | 8.68% | ✅ |
| BTC | 1.039 | 126 | -2.23% | 1.84% | 11.43% | ✅ |
| DOGE | 1.008 | 198 | -0.98% | 2.06% | 11.72% | ✅ |

**关键发现**: 4品种全部Sharpe>1.0，回撤控制极佳（全部<2.5%），但年化收益偏低（1.35%~2.06%）。

#### TRS (TripleRsiStrategy)

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| BTC | 1.397 | 30 | ~0% | ~0% | ~0% | ✅ |
| ETH | 0.757 | 40 | ~0% | ~0% | ~0% | ✅ |
| DOGE | 0.750 | 18 | ~0% | ~0% | ~0% | ✅ |
| SOL | 0.703 | 24 | ~0% | ~0% | ~0% | ✅ |

**关键发现**: BTC上Sharpe=1.397惊人，但交易次数极少（30次/6年≈5次/年），收益几乎为0。可能是参数过于严格导致信号稀少。

#### RSI2 (Rsi2MrStrategy)

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| SOL | 0.892 | 14 | ~0% | ~0% | ~0% | ✅ |
| BTC | 0.725 | 8 | ~0% | ~0% | ~0% | ✅ |
| ETH | 0.722 | 4 | ~0% | ~0% | ~0% | ✅ |
| DOGE | 0.711 | 8 | ~0% | ~0% | ~0% | ✅ |

**关键发现**: 非常稳定，所有品种Sharpe 0.71~0.89，参数趋同（rsi_period=3, sma_period=200）。但交易次数极少。

#### SMF (StochMomentumFilterStrategy)

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| SOL | 0.742 | 8 | ~0% | ~0% | ~0% | ✅ |
| ETH | 0.725 | 50 | ~0% | ~0% | ~0% | ✅ |
| BTC | 0.519 | 26 | ~0% | ~0% | ~0% | ✅ |
| DOGE | 0.443 | 4 | -0.75% | 0.28% | 1.61% | ⚠️ |

#### PR (PullbackMrStrategy)

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| ETH | 0.722 | 116 | -0.01% | 0.01% | 0.03% | ✅ |
| BTC | 0.644 | 154 | -0.02% | 0.01% | 0.07% | ✅ |
| SOL | 0.469 | 40 | ~0% | ~0% | ~0% | ⚠️ |
| DOGE | 0.211 | 46 | -0.01% | ~0% | ~0% | ⚠️ |

#### NR7 (Nr7BreakoutStrategy)

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| ETH | 0.591 | 262 | -0.01% | ~0% | 0.03% | ✅ |
| BTC | 0.586 | 248 | -0.02% | 0.01% | 0.04% | ✅ |
| SOL | 0.208 | 247 | -0.01% | ~0% | ~0% | ⚠️ |
| DOGE | -0.059 | 114 | -0.02% | ~0% | -0.0% | ❌ |

#### FDLR (FiveDayLowRangeStrategy)

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| BTC | 0.620 | 175 | -0.03% | 0.01% | 0.06% | ✅ |
| SOL | 0.242 | 130 | -0.01% | ~0% | ~0% | ⚠️ |
| ETH | 0.083 | 162 | -0.02% | ~0% | ~0% | ⚠️ |
| DOGE | 0.044 | 117 | -0.02% | ~0% | ~0% | ⚠️ |

#### GE (GoldEnvelopeStrategy) — 完全不适合Crypto

| 品种 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 | 状态 |
|------|--------|----------|----------|----------|--------|------|
| BTC | 0.251 | 138 | -0.04% | 0.01% | 0.03% | ⚠️ |
| ETH | -0.053 | 176 | -0.03% | ~0% | -0.0% | ❌ |
| SOL | -0.116 | 122 | -0.02% | ~0% | -0.0% | ❌ |
| DOGE | -0.485 | 96 | -0.05% | -0.01% | -0.03% | ❌ |

---

## 三、关键发现

1. **CINCO是Crypto王者**: 平均Sharpe=1.15，所有4品种Sharpe>1.0，唯一有实质收益的策略
2. **TRS在BTC上表现惊人**: Sharpe=1.397，但交易次数极少（30次/6年），收益几乎为0
3. **RSI2非常稳定**: 所有品种Sharpe 0.71~0.89，参数趋同（rsi_period=3, sma_period=200）
4. **GE完全不适合Crypto**: 4品种中3个负Sharpe
5. **SOL是最好做的品种**: CINCO/SMF/RSI2都在SOL上达到最佳或接近最佳
6. **大多数策略收益极低**: 除CINCO外，其他策略年化收益接近0%，可能是crypto日线数据波动特性导致

---

## 四、TOP 10 最佳组合

| 排名 | 策略 | 品种 | Sharpe | 关键参数 |
|------|------|------|--------|---------|
| 1 | TRS | BTC | 1.397 | rsi_period=5, ma_period=200, rsi_entry=21 |
| 2 | CINCO | ETH | 1.307 | boll_window=38, bar_window=18, atr_window=5 |
| 3 | CINCO | SOL | 1.244 | boll_window=38, bar_window=14, atr_window=5 |
| 4 | CINCO | BTC | 1.039 | boll_window=38, bar_window=18, atr_window=37 |
| 5 | CINCO | DOGE | 1.008 | boll_window=38, bar_window=14, atr_window=37 |
| 6 | RSI2 | SOL | 0.892 | rsi_period=3, sma_period=200, rsi_entry=6 |
| 7 | TRS | ETH | 0.757 | rsi_period=5, ma_period=180, rsi_entry=39 |
| 8 | TRS | DOGE | 0.750 | rsi_period=6, ma_period=140, rsi_entry=27 |
| 9 | SMF | SOL | 0.742 | stoch_k_period=16, momentum_period=4 |
| 10 | RSI2 | BTC | 0.725 | rsi_period=3, sma_period=200, rsi_entry=6 |

---

## 五、修复的Bug

| 问题 | 修复方式 | 状态 |
|------|---------|------|
| 参数名严重不匹配（7/10策略） | 重写STRATEGY_OPT_PARAMS，与实际类变量一致 | ✅ 已修复 |
| 类名映射错误（PR→PanicRelief） | pipeline.py中PR改为PullbackMrStrategy | ✅ 已修复 |
| 不存在策略（MR） | 添加存在性验证，运行时拒绝无效策略 | ✅ 已修复 |
| 参数自动过滤 | build_tasks中自动验证并过滤无效参数名 | ✅ 已修复 |
| OAT失败 | 修复后所有策略OAT+GA正常通过 | ✅ 已修复 |
| batch_results去重bug | collect_pipeline_results按品种去重导致所有策略结果相同 | ⚠️ 已识别，未修复 |

---

## 六、数据质量说明

### 6.1 数据来源

本报告数据直接从 `cta_developer/data/pipeline/` 各策略独立目录解析，绕过 `batch_results/` 的去重bug。

- CINCO: `data/pipeline/CincoStrategy_*/`
- TRS: `data/pipeline/TripleRsiStrategy_*/`
- RSI2: `data/pipeline/Rsi2MrStrategy_*/`
- ...等等

### 6.2 已知问题

1. **batch_results去重bug**: `collect_pipeline_results()` 函数按 `vt_symbol` 去重，导致不同策略的相同品种被覆盖。所有策略的 `report.csv` 内容相同。
2. **多数策略收益极低**: 除CINCO外，TRS/RSI2/SMF/PR/NR7/FDLR/GE的年化收益接近0%，可能是：
   - crypto日线数据波动特性与策略逻辑不匹配
   - 参数优化过于保守（Sharpe高但收益低）
   - 需要检查contract size和费率设置

---

## 七、可实盘候选

### 7.1 推荐组合（基于真实数据）

| 策略 | 品种 | Sharpe | 年化 | 回撤 | 交易次数 | 评价 |
|------|------|--------|------|------|----------|------|
| CINCO | ETH | 1.307 | 1.35% | -0.99% | 160 | ⭐⭐⭐ 首选 |
| CINCO | SOL | 1.244 | 1.68% | -1.61% | 128 | ⭐⭐⭐ 首选 |
| CINCO | BTC | 1.039 | 1.84% | -2.23% | 126 | ⭐⭐⭐ 首选 |
| CINCO | DOGE | 1.008 | 2.06% | -0.98% | 198 | ⭐⭐⭐ 首选 |
| TRS | BTC | 1.397 | ~0% | ~0% | 30 | ⚠️ Sharpe高但收益极低 |
| RSI2 | SOL | 0.892 | ~0% | ~0% | 14 | ⚠️ 交易次数太少 |

### 7.2 实盘建议

- **CINCO是唯一有实盘价值的策略**，4品种全部Sharpe>1.0且有实质收益
- **其他策略需要重新调参**或切换到分钟级数据
- **TRS@BTC虽然Sharpe=1.397**，但6年只交易30次，无实际收益，不适合实盘

---

## 八、实盘配置JSON

```json
{
  "strategy": "CincoStrategy",
  "version": "2026-04-30",
  "source": "cta_developer batch pipeline (bug-fixed, direct pipeline parse)",
  "note": "Only CINCO shows meaningful returns. Other strategies need re-tuning.",
  "configs": [
    {
      "vt_symbol": "ETHUSDT_SWAP_OKX.GLOBAL",
      "exchange": "OKX",
      "product": "ETHUSDTSWAPOKX",
      "params": {
        "boll_window": 38,
        "bar_window": 18,
        "atr_window": 5,
        "boll_dev": 1.54,
        "trailing_long": 0.455,
        "trailing_short": 0.715
      },
      "backtest": {
        "sharpe": 1.307,
        "annual_return_pct": 1.35,
        "max_drawdown_pct": -0.99,
        "trade_count": 160,
        "total_return_pct": 8.40
      }
    },
    {
      "vt_symbol": "SOLUSDT_SWAP_OKX.GLOBAL",
      "exchange": "OKX",
      "product": "SOLUSDTSWAPOKX",
      "params": {
        "boll_window": 38,
        "bar_window": 14,
        "atr_window": 5,
        "boll_dev": 1.54,
        "trailing_long": 0.455,
        "trailing_short": 0.715
      },
      "backtest": {
        "sharpe": 1.244,
        "annual_return_pct": 1.68,
        "max_drawdown_pct": -1.61,
        "trade_count": 128,
        "total_return_pct": 8.68
      }
    },
    {
      "vt_symbol": "BTCUSDT_SWAP_OKX.GLOBAL",
      "exchange": "OKX",
      "product": "BTCUSDTSWAPOKX",
      "params": {
        "boll_window": 38,
        "bar_window": 18,
        "atr_window": 37,
        "boll_dev": 1.54,
        "trailing_long": 0.585,
        "trailing_short": 0.845
      },
      "backtest": {
        "sharpe": 1.039,
        "annual_return_pct": 1.84,
        "max_drawdown_pct": -2.23,
        "trade_count": 126,
        "total_return_pct": 11.43
      }
    },
    {
      "vt_symbol": "DOGEUSDT_SWAP_OKX.GLOBAL",
      "exchange": "OKX",
      "product": "DOGEUSDTSWAPOKX",
      "params": {
        "boll_window": 38,
        "bar_window": 14,
        "atr_window": 37,
        "boll_dev": 1.54,
        "trailing_long": 0.455,
        "trailing_short": 0.845
      },
      "backtest": {
        "sharpe": 1.008,
        "annual_return_pct": 2.06,
        "max_drawdown_pct": -0.98,
        "trade_count": 198,
        "total_return_pct": 11.72
      }
    }
  ],
  "risk_management": {
    "position_sizing": "fixed_size=1 (default)",
    "max_leverage": "not_set",
    "stop_loss": "trailing_long/trailing_short ATR-based",
    "take_profit": "none_explicit"
  }
}
```

---

## 九、相关页面

- [[strategy-repro-crypto-trend-combo]] — strategy_factory Crypto Trend Combo (Sharpe=1.741 BTC)
- [[strategy-repro-nr7_breakout]] — NR7 Breakout在crypto上的复现
- [[strategy-repro-bitcoin-momentum]] — Bitcoin Momentum Strategy
- [[crypto-strategies-analysis-2026-04-30]] — strategy_factory crypto分析 (对比参考)
- [[reversal-strategy-landscape]] — ETF品种策略适配全景分析

---

*报告生成于 2026-04-30 | 数据来源: cta_developer data/pipeline/ 独立目录解析 | 已验证: 8策略×4品种全部32个任务真实结果*
