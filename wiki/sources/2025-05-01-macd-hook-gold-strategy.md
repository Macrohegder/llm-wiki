---
id: 2025-05-01-macd-hook-gold-strategy
title: "MACD Hook 黄金多头策略——远离主观交易"
source: "Algomatic Trading"
url: https://algomatictrading.substack.com/p/escape-discretionary-trading-automate
date: 2025-05-01
tags: #gold #macd #momentum #algorithmic-trading #prorealtime
status: reproduced
reproduction_id: strategy-repro-macd-hook-gold
rating: green
---

# MACD Hook 黄金多头策略

## 一句话摘要

利用 MACD 线上穿零轴 + histogram hook（回调后转向）+ Hull MA 趋势确认的三重过滤黄金多头策略，出场采用 "3连阳或10日市场" 简单规则，适合算法新手入门。

## 策略细节

### 入场条件（全部必须同时满足）

| 条件 | 说明 | 指标参数 |
|------|------|--------|
| MACD Line > 0 | 多头趋势偏置 | MACD(12,26,9) |
| Histogram Hook | histogram 在回调后转向上行 | m > m[1] and m[1] < m[2] |
| Hull MA 确认 | 短期价格动能向上 | average[15,7] |

### 出场条件（任意一条触发）

| 条件 | 说明 |
|------|------|
| 3 连阳 | 连续 3 个交易日 close > open |
| 10 日市场 | 持仓满 10 个交易日 |

### 风险管理

| 项目 | 设置 |
|------|------|
| 止损 | 5% 固定比例 |
| 仓位管理 | ATR(39) 动态定量，riskPercent=1% |
| 资金规模 | $20,000 默认 |
| 方向 | 多头专用 |
| 周期 | 日线 |

## 回测结果

- 回测区间：2005–2025
- OOS 开始：2022-04-01
- 平台：ProRealTime

原文展示了回测图表但未提供具体数值指标。
