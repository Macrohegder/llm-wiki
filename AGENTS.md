# LLM Wiki - 量化策略知识库

## 项目定位
基于 Karpathy LLM Wiki 模式构建的持久化 Markdown 知识资产。承接 cta_developer 的回测输出，为 tracker 和实盘决策提供策略验证历史与知识储备。

## 目录结构

```
llm-wiki/
├── index.md                  # 主索引：实体、概念、来源、已验证策略总览
├── log.md                    # 活动日志：录入、复现、批量回测时间线
├── raw/
│   ├── articles/             # 原始策略文章（Substack/博客）
│   ├── papers/               # 学术论文
│   ├── notes/                # 手动笔记
│   └── batch_reports/        # cta_developer 批量回测报告（自动生成）
└── wiki/
    ├── entities/             # 实体卡片：人物、品种、作者、ETF
    ├── concepts/             # 概念卡片：均值回归、趋势跟踪、RSI 等
    ├── sources/              # 来源引用：文章、博客的引用页
    └── syntheses/            # 综合报告：批量回测汇总、策略汇编
```

## 命名规范

| 目录 | 命名格式 | 示例 |
|------|----------|------|
| `raw/articles/` | `YYYY-MM-DD-标题.md` | `2026-04-18-consecutive-down-days-strategy.md` |
| `wiki/entities/` | `实体名.md` | `Larry-Connors.md` |
| `wiki/concepts/` | `概念名.md` | `mean-reversion.md` |
| `wiki/syntheses/` | `主题-日期.md` | `rsi-etf-batch-2026-05-03.md` |

## 与 cta_developer 的协作

### 批量回测报告同步（自动）
- 由 `cta_developer/scripts/publish_to_wiki.py` 自动同步
- 输出到 `wiki/syntheses/` 和 `raw/batch_reports/`
- 自动更新 `index.md` 和 `log.md`

### 策略复现记录（手动维护）
复现完成后，手动更新 `index.md` 的"已验证策略"表：
```markdown
| 策略 | 原文 | 复现报告 | 最佳品种 | Sharpe | 评级 | 日期 |
```

### 评级标准
- 🟢 **Green**: Sharpe ≥ 0.8 且 交易数 ≥ 50
- 🟡 **Yellow**: Sharpe ≥ 0.5 且 交易数 ≥ 30
- 🔴 **Red**: 不满足以上

## 与 tracker 的协作
tracker 在构建实盘组合前，应查阅本 wiki：
- `index.md` → "已验证策略"表确认策略回测表现
- `wiki/syntheses/` → 查看批量回测综合报告
- 只有 Green/Yellow 评级的策略建议纳入实盘组合

## 安全红线
- **禁止**保存 API Key、账户密码、Telegram Token
- **禁止**保存实盘持仓明细、交易记录
- 策略参数、回测结果、文章摘要可以保存

## 常用操作

```bash
# 查看知识库状态
cd /root/llm-wiki && git status

# 手动添加文章后提交
git add raw/articles/ index.md log.md
git commit -m "wiki: 录入 XXX 策略文章"
git push

# 查看已验证策略列表
grep -A 50 "已验证策略" index.md
```
