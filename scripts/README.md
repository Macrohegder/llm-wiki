# Substack → llm-wiki 自动化工作流 - 完整文档

## 概述

本工作流实现了从 Substack 文章自动采集、入库、策略复现到知识库维护的全自动化流水线。

## 文件结构

```
llm-wiki/
├── scripts/
│   ├── auto_ingest.py              # P0: 自动入库脚本
│   ├── strategy_repro_template.py  # P1: 策略复现模板
│   ├── batch_deep_process.py       # P3: 批量深度处理
│   ├── telegram_commands.py        # P4: Telegram Bot 命令
│   └── output/                     # 回测输出目录
├── wiki/
│   ├── sources/                    # 771 篇 source 文件
│   ├── strategies/                 # 策略 YAML 配置
│   └── syntheses/                  # 主题汇编报告
└── raw/articles/                   # 840 篇原文备份

substack-strategy-tracker/
└── scripts/
    ├── multi_substack_tracker.py   # RSS 自动抓取
    └── auto_ingest.py              # 自动入库（软链接）
```

## 组件说明

### P0: auto_ingest.py - 自动入库

**功能**:
- 从 substack-tracker/articles/ 扫描文章
- URL + 标题双重去重
- Concrete 评分（0-15 分策略可复现性检测）
- Paywall stub 过滤
- 自动标签推断（策略类型/资产类别/主题）
- 生成标准 frontmatter 的 source 文件
- 同步复制到 raw/articles/
- 更新 index.md 和 log.md
- 智能 Telegram 通知（仅高价值文章）

**用法**:
```bash
# 模拟运行
python3 auto_ingest.py --dry-run --source-dir /path/to/articles

# 实际入库
python3 auto_ingest.py --source-dir /path/to/articles --min-concrete 3

# 关闭通知
python3 auto_ingest.py --no-notify
```

### P1: strategy_repro_template.py - 策略复现

**功能**:
- 统一数据源接口（vnpy SQLite → CCXT OKX → yfinance）
- 8 种内置信号（趋势突破、RSI 均值回归、均线交叉、布林带反弹等）
- 简化回测引擎（多空、止损止盈、仓位管理）
- 性能指标（年化收益、Sharpe、最大回撤、胜率）
- YAML 配置驱动
- 输出 CSV + Markdown 报告 + 图表

**用法**:
```bash
# 列出可用信号
python3 strategy_repro_template.py --list-signals

# 列出可用品种
python3 strategy_repro_template.py --list-symbols SMART

# 使用 YAML 配置回测
python3 strategy_repro_template.py --config strategy.yaml

# 交互式配置
python3 strategy_repro_template.py --interactive
```

**YAML 配置示例**:
```yaml
strategy:
  name: "SPY 20-Day Breakout"
  symbols: ["SPY"]
  exchange: "SMART"
  interval: "d"
  start_date: "2014-01-01"
  end_date: "2024-12-31"
  signal_type: "trend_breakout"
  params:
    lookback: 20
    entry_on_close: true
  stop_loss_pct: 0.05
  position_size: 1.0
```

### P3: batch_deep_process.py - 批量深度处理

**功能**:
- 基于标签的主题聚类
- 读取 raw/articles/ 完整内容
- 提取策略规则表格（入场/出场/止损/仓位）
- 提取回测数据对比
- 识别共同参数区间
- 生成主题汇编报告（wiki/syntheses/）
- 生成可复现策略 YAML 配置

**用法**:
```bash
# 列出主题分布
python3 batch_deep_process.py --list-themes

# 处理特定主题
python3 batch_deep_process.py --theme strategy/mean-reversion --max-articles 20

# 按关键词处理
python3 batch_deep_process.py --keyword "intraday" --output intraday-analysis.md
```

### P4: telegram_commands.py - Bot 命令扩展

**命令列表**:
| 命令 | 功能 |
|------|------|
| `/ingest <url>` | 抓取单篇文章并入库 |
| `/batch <theme>` | 批量处理某主题 |
| `/repro <name>` | 一键回测策略 |
| `/status` | 今日处理统计 |
| `/queue` | 查看待处理队列 |
| `/synth <theme>` | 生成/查看主题报告 |
| `/themes` | 列出主题分布 |
| `/data <symbol>` | 检查品种数据 |
| `/help` | 帮助信息 |

**集成方式**: 将 `process_telegram_message()` 函数集成到 Hermes Gateway 的消息处理器中。

## 定时任务

| 任务 | 时间 | 功能 |
|------|------|------|
| daily-substack-auto-ingest | 每天 9:00 | 自动入库新文章 |
| weekly-strategy-summary | 每周日 21:00 | 生成周度汇总 |
| monthly-theme-analysis | 每月 1 日 10:00 | 主题深度分析 |

## 使用流程

### 场景 1: 收到 Telegram 文章通知
```
1. Telegram 收到新文章通知
2. 如果感兴趣 → 回复 /ingest <url> 手动触发
3. 或直接等每天 9:00 自动入库
```

### 场景 2: 探索某类策略
```
1. /themes                    # 查看有哪些主题
2. /batch strategy/trend-following  # 批量处理
3. /synth strategy/trend-following  # 查看报告
4. /repro Strategy_Name       # 回测具体策略
```

### 场景 3: 手动复现策略
```
1. 从文章中提取参数
2. 创建 YAML 配置文件
3. python3 strategy_repro_template.py --config my_strategy.yaml
4. 查看 output/ 目录下的报告和图表
```

## 注意事项

1. **数据质量**: yfinance 在云服务器 IP 上易限流，优先使用 vnpy 本地数据
2. **回测简化**: 当前回测引擎未考虑滑点和佣金，结果仅供参考
3. **标签推断**: 自动标签基于关键词匹配，可能需要手动调整
4. **Concrete 评分**: 阈值可调，建议根据实际效果调整 min_concrete 参数

## 后续优化方向

- [ ] 集成到 Hermes Gateway 作为原生命令
- [ ] 添加更多信号类型（机器学习信号、统计套利等）
- [ ] 支持多时间框架回测
- [ ] 添加参数优化（walk-forward）
- [ ] 策略组合回测（多策略等权/风险平价）
