# Quant Workspace Agent 架构与运维入口

> 本文档记录 `/root/quant/` 下的 Agent 角色划分、协作关系和数据运维入口。
> 最后更新：2026-06-19

## Agent 角色总览

| Agent 角色 | 工作目录 | 核心职责 | 典型 Skill |
|-----------|---------|---------|-----------|
| **data_operator** | `data_operator/` | 数据采集、质量监控、修复、回填、跨源整合 | `quant-data-engineer`、`quant-data-guardian`、`okx-data` |
| **strategy_factory** | `strategy_factory/` | 文章/Idea → 策略 YAML/代码 | `cta-strategy-factory`、`cs-strategy-factory` |
| **cta_developer** | `cta_developer/` | CTA 策略回测、优化、报告 | `cta-pipeline`、`cta-strategy-factory`、`vnpy-coding-standard` |
| **cs_developer** | `cs_developer/` | 截面策略研发 | `cs-pipeline`、`cs-strategy-factory`、`vnpy-coding-standard` |
| **spread_trader** | `spread_trading/` | 跨所套利执行、风控、监控 | `okx-hl-arbitrage` 系列、`cross-exchange-hedge-execution` |
| **portfolio_optimizer** | `portfolio_optimizer/` | 组合优化、风险平价权重 | `risk-parity-strategy`、`quant-workflow` |
| **cta_live_deploy** | `cta_live_deploy/` | 实盘部署包构建、配置校验 | `quant-workflow`、`github` |
| **tracker** | `tracker/` | 实盘 vs 模拟绩效跟踪、样本外回测 | `quant-workflow` |

## 数据运维入口（data_operator）

### 统一采集

```bash
cd /root/quant/data_operator
python3 scripts/run_collection.py --all
```

### 健康检查

```bash
python3 scripts/run_health_check.py
python3 scripts/run_health_check.py --alert-only
```

### 手动修复

```bash
python3 scripts/run_repair.py --source okx
python3 scripts/run_repair.py --source okx,hyperliquid
```

### 历史回填

```bash
python3 scripts/run_backfill.py --source okx --symbol BTC --start 2020-01-01 --end 2024-01-01
```

### 跨源同步

```bash
python3 scripts/run_sync.py --task funding_history
```

### 状态看板

```bash
python3 scripts/dashboard.py
```

## 跨 Agent 协作契约

```
strategy_factory      cta_developer / cs_developer
       ↓                       ↓
   生成策略代码           批量回测/优化
       ↓                       ↓
   cta_developer ←  最优参数 cta_strategy_setting_*.json
       ↓
portfolio_optimizer 组合优化（风险平价权重）
       ↓
   cta_live_deploy 构建部署包
       ↓
   交易服务器 git pull
       ↓
   tracker 每日绩效跟踪
       ↓
   llm-wiki 知识沉淀

spread_trader ↔ data_operator （获取资金费率/K线数据）
```

## 数据问题上报路径

- CTA/CS/套利 Agent 发现数据异常 → 转交 `data_operator`
- 数据修复完成 → 通知相关策略/套利 Agent
- 数据问题导致实盘异常 → 立即通知 `spread_trader` / `cta_live_deploy`
