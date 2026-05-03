---
id: rsi-etf-batch-2026-05-03
title: "RSI 批量回测报告 — ETF (2026-05-03)"
date: "2026-05-03"
tags:
  - rsi
  - backtest-analysis
  - cta-developer
  - batch-pipeline
  - synthesis
---

# RSI 批量回测报告 — ETF

> 知识合成页 | 基于 cta_developer batch pipeline 自动生成
> 创建：2026-05-03 | 策略：RSI
> 批次目录：`rsi_etf_20260503_175559`

---

## 一、测试概况

| 项目 | 内容 |
|------|------|
| 策略 | RSI |
| 资产类别 | ETF |
| 品种总数 | 5 |
| 生成时间 | 2026-05-03 |
| Green 评级 | 0 |
| Yellow 评级 | 4 |

- **最佳品种**: SPY.SMART (Sharpe=0.87)

---

## 二、全品种表现汇总

### 排名总览（按夏普降序）

| 排名 | 品种 | 夏普 | 年化收益% | 最大回撤% | 交易笔数 | 评级 |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | SPY.SMART | 0.8681544741685608 | 0.012616878191938675 | -0.01690064542459302 | 82 | 🟡 yellow |
| 2 | GLD.SMART | 0.7381982528086406 | 0.01788419565843566 | -0.036774562031048355 | 56 | 🟡 yellow |
| 3 | TLT.SMART | 0.6378460851864598 | 0.010082987558435105 | -0.01951240717752179 | 56 | 🟡 yellow |
| 4 | QQQ.SMART | 0.515225176189841 | 0.009162214228125784 | -0.024888751914541464 | 52 | 🟡 yellow |
| 5 | IWM.SMART | 0.47075249403342445 | 0.011736303733165306 | -0.037140133939748216 | 87 | 🔴 red |

---

## 三、原始报告

详细报告（含参数、图表、验证结果）位于：
- **CSV**: `data/batch_results/rsi_etf_20260503_175559/report.csv`
- **MD**: `data/batch_results/rsi_etf_20260503_175559/report.md`

---

## 四、相关页面

- [[cta-developer-crypto-batch-2026-04-30]] — CTA Developer Crypto 批量回测报告
- [[mean-reversion-strategies-comparison]] — 均值回归策略对比分析

---

*本页面由 cta_developer batch pipeline 自动生成并同步至 llm-wiki | 时间: 2026-05-03*
