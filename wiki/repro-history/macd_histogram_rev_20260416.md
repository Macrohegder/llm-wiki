---
id: repro-history-macd_histogram_rev_20260416
title: "Repro History: MACD Histogram Mean Reversion"
strategy_id: macd_histogram_rev_20260416
---

# MACD Histogram Mean Reversion — 复现历史总览

## 原文信息
- **来源**: [[strategy-repro-macd-histogram-rev-20260416]]
- **URL**: https://quantifiedstrategies.substack.com/p/macd-histogram-trading-strategy-rules
- **作者**: QuantifiedStrategies
- **发布日期**: 2024-03-07

## 复现时间线

| 日期 | 复现报告 | 状态 | 最佳品种 | 代码版本 | 关键事件 |
|------|----------|------|----------|----------|----------|
| 2026-04-16 | [[strategy-repro-macd_histogram_rev_20260416\|报告-20260416]] | 🟢 Green | QQQ (Sharpe=1.038) | 1bbb4ed | 首次复现，代码逻辑正确 |
| 2026-04-28 | [[strategy-repro-macd_histogram_rev_20260416\|报告-20260428]] | 🟢 Green | QQQ (Sharpe=1.397) | 1bbb4ed | 修复 `daily_end_hour` 被 OAT 优化问题 |

## 关键参数演进

| 日期 | decline_days | fast_period | slow_period | signal_period | 备注 |
|------|-------------|-------------|-------------|---------------|------|
| 2026-04-16 | 3 | — | 34 | 12 | OAT 优化结果 |
| 2026-04-28 | 2 | 11 | 41 | 9 | 修复代码后重新优化 |

## 代码变更记录

| 日期 | 变更 | 影响 |
|------|------|------|
| 2026-04-16 | 首次实现 | 基于原文规则：hist 连续下跌 4 天且低于零轴、收盘价 < 前日 |
| 2026-04-28 | 修复 `daily_end_hour` | 改为内部参数 `_daily_end_hour`，防止 OAT 优化导致 `time()` 错误 |
| 2026-04-28 | 恢复有效版本 | 从 git 恢复 4月16日版本，当前版本逻辑错误（cond_1 被覆盖） |

## 品种覆盖演进

| 日期 | Green | Yellow | Red | 探索率 |
|------|-------|--------|-----|--------|
| 2026-04-16 | 1 | 0 | 3 | 25% |
| 2026-04-28 | 1 | 0 | 3 | 25% |

> **扩展测试**: 2026-04-24 曾进行 14 品种扩展测试，13/14 达到 Yellow 以上，9 品种 Green（详见原文页）

## 结论

- **当前有效复现**: [[strategy-repro-macd_histogram_rev_20260416]]
- **策略有效性**: ✅ 在 QQQ 上表现稳健（Sharpe > 1.3）
- **主要风险**: 仅 QQQ 有效，其他品种无信号（参数可能过于特异化）
- **建议**: 考虑扩展品种测试或调整参数范围
