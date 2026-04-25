# quant-wiki 合并：量化交易知识库

**来源**: quant-wiki (本地，无 Git 远程)
**日期**: 2026-04-25
**标签**: #migration #quant-wiki #merge

## 摘要

将独立的 quant-wiki 知识库（早期实验版本）全部合并至 llm-wiki 主库。quant-wiki 为纯本地仓库，未与任何 Git 远程关联。

## 迁移内容

| 目录 | 文件数 | 目标路径 |
|------|--------|----------|
| raw/articles/ | 391 篇 | llm-wiki/raw/articles/ |
| wiki/sources/ | 391 篇 | llm-wiki/wiki/sources/ |
| wiki/entities/ | 5 篇 | llm-wiki/wiki/entities/ |
| wiki/concepts/ | 6 篇 | llm-wiki/wiki/concepts/ |
| wiki/strategies/ | 5 篇 | llm-wiki/wiki/strategies/ |
| wiki/syntheses/ | 1 篇 | llm-wiki/wiki/syntheses/ |
| dashboard/ | (未迁移) | — |
| templates/ | (未迁移) | — |

### 新增实体

- [[Larry Connors]]
- [[QQQ]]
- [[SPY]]
- [[XLP]]
- [[QuantifiedStrategies-com]]

### 新增概念

- [[IBS (Internal Bar Strength)]]
- [[Mean-Reversion]]
- [[Overnight-Edge]]
- [[Position-Sizing]]
- [[RSI (Relative Strength Index)]]
- [[Williams %R]]

### 新增策略页面 (wiki/strategies/)

- 5 篇来自 quant-wiki 的策略卡片

## 说明

- quant-wiki 的文章全部来自 QuantifiedStrategies Substack
- 390 篇文章日期为 2026-04-04（批量导入），1 篇日期 2026-04-05，1 篇 2026-04-19
- 与 llm-wiki 原有内容无文件名冲突（0 重复）
