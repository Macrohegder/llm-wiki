# NR7 Breakout 期货批量挖掘 Pipeline 扩展

**来源**: cta_developer 基础设施扩展
**日期**: 2026-04-25
**标签**: #infrastructure #pipeline #nr7 #futures #IB

## 一句话摘要

将 NR7 Breakout 策略的批量优化 Pipeline 从纯 ETF 扩展到 24 个 IB 期货品种（ES、NQ、CL、GC、NG 等），同时在 asset_registry 中新增完整的 IB 期货合约规格支持。

## 修改文件

### 1. `cta/pipeline/asset_registry.py`
- 新增 `IB_FUTURES` 模板（asset_class=FUTURES, currency=USD）
- 新增 `_ib_futures_specs` 字典（24 个品种的精准 size/pricetick/commission）
- 在 `lookup()` 方法中添加 `_apply_ib_futures_specs()` 自动覆盖
- 支持 `@ES.CME`、`@CL.NYMEX`、`@GC.COMEX`、`@ZB.CBOT`、`@CC.ICE` 等格式

### 2. `pipeline_batch_nr7_etf.py`
- `build_pipeline_config(symbol)` → `build_pipeline_config(vt_symbol)`：接受完整 vt_symbol
- `run_batch(symbols)` → `run_batch(vt_symbols)`：传入完整 vt_symbol
- 新增 `FUTURES_SYMBOLS` 列表
- 新增 `--futures` / `--futures-only` 参数

### 3. `scripts/run_nr7_etf_batch.py`
- 新增 `FUTURES_SYMBOLS` 列表 + `FUTURES_EXCHANGE_MAP` 映射
- `build_universe()` 新增 `futures_mode` 参数（ETF 查 SMART，期货查对应交易所）
- 支持 `--futures [品种列表]` / `--futures-only`
- 输出目录自动区分：`nr7_etf_` / `nr7_futures_` / `nr7_futures_etf_`
- 报告 CSV 自动命名：`summary_nr7_etf.csv` / `summary_nr7_futures_etf.csv`

## 期货品种列表（24 个）

| 分类 | 品种 | 交易所 | 乘数 | Tick | 数据起始 |
|------|------|--------|------|------|----------|
| 指数 | ES | CME | 50 | 0.25 | 2021-06 |
| 指数 | NQ | CME | 20 | 0.25 | 2023-03 |
| 指数 | RTY | CME | 50 | 0.10 | — |
| 指数 | YM | CBOT | 5 | 1.0 | — |
| 能源 | CL | NYMEX | 1000 | 0.01 | 2015-11 |
| 能源 | NG | NYMEX | 5000 | 0.001 | 2014-11 |
| 贵金属 | GC | COMEX | 100 | 0.10 | 2018-12 |
| 贵金属 | SI | COMEX | 5000 | 0.005 | — |
| 贵金属 | HG | COMEX | 25000 | 0.0005 | — |
| 贵金属 | MGC | COMEX | 100 | 0.10 | — |
| 利率 | ZB | CBOT | 1000 | 0.03125 | 2023-09 |
| 利率 | ZN | CBOT | 1000 | 0.015625 | — |
| 利率 | ZF | CBOT | 1000 | 0.0078125 | — |
| 利率 | ZT | CBOT | 2000 | 0.0078125 | — |
| 农产品 | ZC | CBOT | 5000 | 0.25 | 2021-12 |
| 农产品 | ZS | CBOT | 5000 | 0.25 | — |
| 农产品 | ZW | CBOT | 5000 | 0.25 | — |
| 农产品 | ZL | CBOT | 60000 | 0.01 | — |
| 农产品 | ZM | CBOT | 100 | 0.10 | — |
| 农产品 | HE | CME | 40000 | 0.00025 | — |
| 农产品 | LE | CME | 40000 | 0.00025 | — |
| 软商品 | CC | ICE | 10 | 1.0 | 2022-06 |
| 软商品 | KC | ICE | 10 | 0.05 | — |
| 软商品 | CT | ICE | 50 | 0.01 | — |

## 期货 vs ETF 配置差异

| 维度 | ETF | 期货 |
|------|-----|------|
| vt_symbol 格式 | `SPY.SMART` | `@ES.CME` |
| 数据源 | SQLite (`db_load_bar`) | SQLite (`db_load_bar`) |
| 合约乘数 | 1 (常规) | 按品种配置 |
| 佣金 | fixed $0.005/share | fixed $2.2 + rate 0.0004% |
| 滑点 | pricetick × 0.5 | pricetick × 2 |
| 资产类别 | EQUITY | FUTURES |

## 用法

```bash
# ETF（原有逻辑不变）
python scripts/run_nr7_etf_batch.py

# 期货
python scripts/run_nr7_etf_batch.py --futures-only

# 指定期货品种
python scripts/run_nr7_etf_batch.py --futures ES NQ CL GC

# 期货 + ETF 混合
python scripts/run_nr7_etf_batch.py --futures --whitelist SPY,QQQ

# dry-run 测试
python scripts/run_nr7_etf_batch.py --futures --dry-run
```

## 相关概念
- [[asset_registry]]
- [[pipeline_batch_nr7_etf]]
- [[IB期货数据集成]]
- [[NR7 Breakout Strategy]]
