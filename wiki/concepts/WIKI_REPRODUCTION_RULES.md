# LLM-Wiki 策略复现管理规则

**版本**: 1.0
**生效日期**: 2026-04-28
**适用范围**: 所有通过 strategy_factory 复现的策略，以及手动复现的策略

---

## 一、核心原则

1. **一篇原文 → 一个 source 页 → 可链接到多个复现报告**
2. **复现完成后，原文 source 页的复现状态必须同步更新**
3. **复现报告必须反向链接到原文 source 页**
4. **所有回测图表必须被 source 页或复现页引用，禁止散落**
5. **index.md 必须维护"已验证策略"索引表**

---

## 二、文件命名规范

### 2.1 原文 Source 页

```
wiki/sources/YYYY-MM-DD-文章标题.md
```

- 日期使用文章**发布日期**，非抓取日期
- 标题使用 kebab-case（短横线连接）
- 示例: `2024-03-07-MACD-Histogram-Trading-Strategy.md`

### 2.2 复现报告页

```
wiki/sources/strategy-repro-<策略ID>.md
```

- 策略 ID 使用 strategy_factory 生成的唯一标识
- 示例: `strategy-repro-macd-histogram-rev-20260416.md`

### 2.3 图表文件

```
raw/assets/<策略ID>_<描述>_<YYYYMMDD>.png
```

- 必须包含策略 ID 和日期，便于追溯
- 示例: `macd_histogram_rev_20260416_equity_curve.png`

---

## 三、页面结构规范

### 3.1 原文 Source 页（复现后更新版）

```markdown
---
id: <source-id>
title: "文章标题"
source: "来源网站"
url: "原文URL"
date: YYYY-MM-DD
tags: #strategy #trading
rating: green|yellow|red
status: reproduced|pending|failed
reproduction_id: strategy-repro-<id>  # 复现完成后填写
---

# 文章标题

## 一句话摘要
...

## 关键要点
- ...

## 相关实体
- [[实体名]]

## 相关概念
- [[概念名]]

## 复现状态
- **状态**: ✅ 已复现 / ⏳ 待复现 / ❌ 复现失败
- **复现日期**: YYYY-MM-DD
- **复现报告**: [[strategy-repro-<id>]]
- **最佳品种**: XXX (Sharpe=X.XX)
- **评级**: Green|Yellow|Red

## 评价
| 指标 | 评分 | 备注 |
|------|------|------|
| 数据质量 | ⭐⭐⭐⭐☆ | ... |
| 可操作性 | ⭐⭐⭐⭐☆ | ... |
| 新颖性 | ⭐⭐⭐☆☆ | ... |
| 风险透明度 | ⭐⭐⭐⭐☆ | ... |

**总体**: 🟢 Green / 🟡 Yellow / 🔴 Red
```

### 3.2 复现报告页

```markdown
---
id: strategy-repro-<id>
title: "Strategy Repro: 策略名"
source: "来源"
url: "原文URL"
reproduced_at: YYYY-MM-DD
status: completed|failed
rating: green|yellow|red
source_note: [[YYYY-MM-DD-文章标题]]  # 反向链接到原文
---

# 策略名 — 策略复现报告

## 原文信息
- **来源**: [[YYYY-MM-DD-文章标题]]
- **URL**: https://...
- **作者**: ...

## 原文摘要
> 一句话概括原文策略规则

## 复现方法
| 项目 | 设置 |
|------|------|
| 标的 | ... |
| 回测区间 | ... |
| 资金 | ... |
| 优化方法 | OAT / GA |
| 优化目标 | Sharpe Ratio |

## 最优参数
| 参数 | 最优值 |
|------|--------|
| ... | ... |

## 回测结果
| 指标 | 数值 |
|------|------|
| Sharpe Ratio | X.XXX |
| 交易次数 | N |
| 最大回撤 | -X.XX% |
| 年化收益 | X.XX% |
| 总收益 | X.XX% |

## 结论
- 评级：**GREEN** ✅ / **YELLOW** ⚠️ / **RED** ❌
- ...

## 复现产物
- YAML: `strategies/inbox/xxx.yaml`
- 代码: `generated/xxx.py`
- 评估报告: `reports/xxx.json`
- 图表: ![描述](MEDIA:raw/assets/xxx.png)

## 各品种回测结果
| 品种 | 评级 | Sharpe | 交易次数 | 最大回撤 | 年化收益 | 总收益 |
|------|------|--------|----------|----------|----------|----------|
| ... | ... | ... | ... | ... | ... | ... |

## 历史记录
- YYYY-MM-DD: 首次复现
- YYYY-MM-DD: 扩展测试 / 参数优化
```

---

## 四、状态同步规则

### 4.1 复现完成时（strategy_factory pipeline 最后一步）

必须执行以下同步操作：

1. **更新原文 source 页**
   - 修改 `status: reproduced`
   - 添加 `reproduction_id: strategy-repro-<id>`
   - 更新 `## 复现状态` 节为 ✅ 已复现
   - 添加复现报告链接 `[[strategy-repro-<id>]]`

2. **确认复现报告有反向链接**
   - 确保 `## 原文信息` 节包含 `[[YYYY-MM-DD-文章标题]]`

3. **引用图表**
   - 在复现报告的 `## 复现产物` 节用 `![描述](MEDIA:raw/assets/xxx.png)` 引用
   - 或在 `## 回测结果` 节直接嵌入图表

4. **更新 index.md**
   - 在 `## 📄 资料来源` 或 `## 🧠 综合结论` 中添加/更新条目
   - 确保链接到原文 source 页（而非复现报告）

5. **git push**
   - `cd /root/llm-wiki && git add -A && git commit -m "..." && git push origin master`

### 4.2 复现失败时

1. 原文 source 页更新：
   ```markdown
   ## 复现状态
   - **状态**: ❌ 复现失败
   - **失败日期**: YYYY-MM-DD
   - **失败原因**: <简要说明>
   - **相关日志**: `reports/failed_xxx.json`
   ```

2. 可选：创建 `wiki/sources/strategy-repro-<id>-FAILED.md` 记录失败详情

### 4.3 多版本复现时

同一策略可能有多次复现（参数优化、扩展品种等）：

```markdown
## 复现状态
- **状态**: ✅ 已复现
- **主复现报告**: [[strategy-repro-macd-histogram-rev-20260416]]
- **扩展测试**: [[strategy-repro-macd-histogram-ext-20260424]]
- **最佳品种**: QQQ (Sharpe=1.038)
- **评级**: Green
```

---

## 五、index.md 维护规范

### 5.1 已验证策略索引表

在 `index.md` 中维护以下表格：

```markdown
## ✅ 已验证策略 (Verified Strategies)

| 策略 | 原文 | 复现报告 | 最佳品种 | Sharpe | 评级 | 日期 |
|------|------|----------|----------|--------|------|------|
| [[2024-03-07-MACD-Histogram-...]] | [[strategy-repro-macd-histogram-...]] | QQQ | 1.038 | 🟢 Green | 2026-04-16 |
```

**规则**：
- 策略列链接到**原文 source 页**
- 复现报告列链接到**复现报告页**
- 按复现日期倒序排列
- 仅收录 `rating: green` 或 `rating: yellow` 的策略
- `rating: red` 的策略放入单独的"复现失败/无效策略"表

### 5.2 待复现策略清单

```markdown
## ⏳ 待复现策略 (Pending Reproduction)

| 策略 | 日期 | 来源 | 规则明确度 | 优先级 |
|------|------|------|-----------|--------|
| [[2026-04-04-RSI-Based-Range-...]] | 2026-04-04 | QuantifiedStrategies | ✅ 明确 | 高 |
```

---

## 六、图表管理规则

### 6.1 命名

```
raw/assets/<策略ID>_<品种>_<类型>_<YYYYMMDD>.png
```

- 策略ID: 如 `macd_histogram_rev_20260416`
- 品种: 如 `QQQ`, `SPY`, `ALL`（多品种汇总）
- 类型: 如 `equity`, `performance`, `params`, `chart`
- 日期: 复测日期

示例: `macd_histogram_rev_20260416_QQQ_equity_20260424.png`

### 6.2 引用

在复现报告中引用图表：

```markdown
### 净值曲线
![QQQ 净值曲线](MEDIA:raw/assets/macd_histogram_rev_20260416_QQQ_equity_20260424.png)

### 多品种汇总
![多品种表现](MEDIA:raw/assets/macd_histogram_rev_20260416_ALL_performance_20260424.png)
```

**规则**：
- 图表必须在复现报告中被引用，否则视为"散落图表"
- 禁止在 raw/assets/ 中存放未被引用的图表
- 旧版/废弃图表应删除或归档到 `raw/assets/archive/`

---

## 七、自动化同步脚本（待实现）

未来可添加脚本 `scripts/sync_wiki_reproduction.py`，功能：

1. 读取 `reports/eval_*.json`
2. 自动更新对应 source 页的 `## 复现状态`
3. 自动更新 `index.md` 的已验证策略表
4. 检查复现报告是否有反向链接
5. 输出待修复问题清单

---

## 八、违规检查清单

每次 wiki 更新后，自检以下项目：

- [ ] 原文 source 页的 `status` 与实际情况一致
- [ ] 原文 source 页有 `reproduction_id` 指向复现报告
- [ ] 复现报告有 `source_note` 指向原文 source 页
- [ ] index.md 的已验证策略表包含该策略
- [ ] 所有图表在复现报告中被引用
- [ ] git push 已完成

---

*本规则由 Hermes Agent 制定，经 Raymond Hsiao 确认后生效*
