#!/usr/bin/env python3
"""
批量深度处理脚本 - 主题级策略分析流水线
功能：
  1. 基于标签和标题的主题聚类
  2. 读取 raw/articles/ 获取完整内容（跳过 paywall stub）
  3. 提取策略规则表格
  4. 提取回测数据对比表
  5. 识别共同参数区间和矛盾观点
  6. 生成主题汇编报告
  7. 生成可复现策略的 YAML 配置

用法：
  python3 batch_deep_process.py --theme "strategy/mean-reversion" [--max-articles 20]
  python3 batch_deep_process.py --keyword "intraday" [--output mean-reversion-analysis.md]
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Optional, Tuple
from collections import defaultdict, Counter

import pandas as pd

# ── 路径配置 ──────────────────────────────────────────
VAULT_DIR = Path(os.path.expanduser("~/llm-wiki"))
RAW_DIR = VAULT_DIR / "raw" / "articles"
SOURCES_DIR = VAULT_DIR / "wiki" / "sources"
SYNTHESIS_DIR = VAULT_DIR / "wiki" / "syntheses"
STRATEGIES_DIR = VAULT_DIR / "wiki" / "strategies"

SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
STRATEGIES_DIR.mkdir(parents=True, exist_ok=True)

# ── 策略关键词（用于 concrete 检测）───────────────────────
_STRATEGY_KEYWORDS = [
    r"trading rules", r"entry signal", r"exit signal", r"stop loss",
    r"backtest result", r"annualized return", r"sharpe", r"win rate",
    r"profit factor", r"drawdown", r"position size", r"long position",
    r"short position", r"buy signal", r"sell signal",
]

_PAYWALL_SIGNALS = [
    "Continue reading this post for free",
    "This post is for subscribers",
    "Claim my free post",
    "purchase a paid subscription",
    "Upgrade to",
    "Subscribe to read more",
]

# ── 辅助函数 ────────────────────────────────────────────

def extract_url(content: str) -> Optional[str]:
    """提取 URL"""
    m = re.search(r'^url:\s*(https?://\S+)', content, re.MULTILINE | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'\*\*原文链接\*\*[:\uff1a]\s*(https?://\S+)', content)
    if m:
        return m.group(1).strip()
    return None


def extract_title(content: str, filename: str) -> str:
    """提取标题"""
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.match(r'\d{4}-\d{2}-\d{2}-(.+)\.md$', filename)
    if m:
        return m.group(1).replace('-', ' ')
    return "Untitled"


def extract_tags(content: str) -> List[str]:
    """从 frontmatter 提取标签"""
    tags = []
    in_tags = False
    for line in content.split('\n'):
        if line.strip() == 'tags:':
            in_tags = True
            continue
        if in_tags:
            if not line.startswith('  - '):
                break
            tag = line.replace('  - ', '').strip()
            if tag:
                tags.append(tag)
    return tags


def extract_date_from_filename(filename: str) -> str:
    """从文件名提取日期"""
    m = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    if m:
        return m.group(1)
    return ""


def has_concrete_logic(content: str) -> Tuple[int, bool]:
    """检测文章是否有可复现的策略逻辑"""
    text_lower = content.lower()
    
    is_paywall = any(signal in content for signal in _PAYWALL_SIGNALS)
    if is_paywall and len(content) < 1500:
        return (0, True)
    
    score = 0
    for kw in _STRATEGY_KEYWORDS:
        if re.search(kw, text_lower):
            score += 1
    
    if len(content) > 3000:
        score += 1
    if len(content) > 5000:
        score += 1
    
    return (score, is_paywall)


def normalize(text: str) -> str:
    """标准化文本"""
    return re.sub(r'[^a-z0-9]', '', text.lower())


# ── 主题聚类 ────────────────────────────────────────────

class ThemeClusterer:
    """主题聚类器"""
    
    def __init__(self):
        self.articles: List[Dict] = []
    
    def scan_sources(self):
        """扫描所有 source 文件"""
        if not SOURCES_DIR.exists():
            print("[错误] sources 目录不存在")
            return
        
        for fname in sorted(os.listdir(SOURCES_DIR)):
            if not fname.endswith('.md'):
                continue
            
            fpath = SOURCES_DIR / fname
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                continue
            
            title = extract_title(content, fname)
            url = extract_url(content)
            tags = extract_tags(content)
            date = extract_date_from_filename(fname)
            
            # 检查 raw 备份是否存在
            raw_exists = False
            raw_content = ""
            for raw_fname in os.listdir(RAW_DIR) if RAW_DIR.exists() else []:
                if normalize(raw_fname) == normalize(fname) or \
                   (date and raw_fname.startswith(date)):
                    raw_path = RAW_DIR / raw_fname
                    try:
                        with open(raw_path, 'r', encoding='utf-8') as f:
                            raw_content = f.read()
                        raw_exists = True
                        break
                    except:
                        pass
            
            self.articles.append({
                'filename': fname,
                'title': title,
                'url': url,
                'tags': tags,
                'date': date,
                'source_content': content,
                'raw_exists': raw_exists,
                'raw_content': raw_content,
            })
        
        print(f"[扫描] 共 {len(self.articles)} 篇 source 文件")
    
    def filter_by_theme(self, theme_tag: str = None, keyword: str = None) -> List[Dict]:
        """按主题过滤"""
        filtered = []
        
        for article in self.articles:
            match = False
            
            if theme_tag:
                if theme_tag in article['tags']:
                    match = True
            
            if keyword:
                text = (article['title'] + ' ' + ' '.join(article['tags'])).lower()
                if keyword.lower() in text:
                    match = True
            
            if match:
                filtered.append(article)
        
        return filtered
    
    def get_themes_distribution(self) -> Dict[str, int]:
        """获取主题分布统计"""
        counter = Counter()
        for article in self.articles:
            for tag in article['tags']:
                if tag.startswith('strategy/') or tag.startswith('asset/') or tag.startswith('topic/'):
                    counter[tag] += 1
        return dict(counter.most_common())


# ── 深度处理 ────────────────────────────────────────────

class DeepProcessor:
    """深度处理器"""
    
    def __init__(self, articles: List[Dict]):
        self.articles = articles
        self.processed: List[Dict] = []
    
    def process_all(self) -> List[Dict]:
        """处理所有文章"""
        print(f"\n[处理] 深度分析 {len(self.articles)} 篇文章")
        
        for i, article in enumerate(self.articles, 1):
            print(f"\n[{i}/{len(self.articles)}] {article['title'][:60]}...")
            
            # 获取完整内容
            content = article['raw_content'] if article['raw_exists'] else article['source_content']
            
            if not content:
                print("  [跳过] 无内容")
                continue
            
            # 检测 concrete
            score, is_paywall = has_concrete_logic(content)
            print(f"  Concrete: {score}, Paywall: {is_paywall}")
            
            if is_paywall:
                print("  [跳过] Paywall")
                continue
            
            # 提取结构化信息
            extracted = self._extract_structure(content, article['title'])
            
            self.processed.append({
                **article,
                'concrete_score': score,
                'extracted': extracted,
            })
        
        print(f"\n[完成] 成功处理 {len(self.processed)} 篇")
        return self.processed
    
    def _extract_structure(self, content: str, title: str) -> Dict:
        """从文章内容提取结构化信息"""
        text_lower = content.lower()
        
        extracted = {
            'entry_rules': [],
            'exit_rules': [],
            'stop_loss': None,
            'position_sizing': None,
            'timeframe': None,
            'assets': [],
            'indicators': [],
            'backtest_metrics': {},
            'key_params': {},
        }
        
        # 提取入场规则
        entry_patterns = [
            r'(?:entry|buy|long).*?(?:when|if|on|at)\s+(.+?)(?:\.|\n)',
            r'(?:go long|enter long).*?(?:when|if)\s+(.+?)(?:\.|\n)',
            r'(?:buy signal|entry signal).*?[:\s]+(.+?)(?:\.|\n)',
        ]
        for pattern in entry_patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            extracted['entry_rules'].extend(matches[:3])
        
        # 提取出场规则
        exit_patterns = [
            r'(?:exit|sell|close|cover).*?(?:when|if|on|at)\s+(.+?)(?:\.|\n)',
            r'(?:go short|exit long).*?(?:when|if)\s+(.+?)(?:\.|\n)',
            r'(?:sell signal|exit signal).*?[:\s]+(.+?)(?:\.|\n)',
        ]
        for pattern in exit_patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            extracted['exit_rules'].extend(matches[:3])
        
        # 提取止损
        sl_match = re.search(r'(?:stop loss|stop-loss).*?(\d+\.?\d*)\s*%?', text_lower)
        if sl_match:
            extracted['stop_loss'] = sl_match.group(1) + '%'
        
        # 提取仓位管理
        ps_match = re.search(r'(?:position size|sizing|risk per trade).*?(\d+\.?\d*)\s*%?', text_lower)
        if ps_match:
            extracted['position_sizing'] = ps_match.group(1) + '%'
        
        # 提取时间框架
        tf_patterns = [
            r'(\d+\s*-?\s*(?:minute|min|hour|hr|day|daily|week|month))',
            r'(intraday|daily|swing|position)',
        ]
        for pattern in tf_patterns:
            match = re.search(pattern, text_lower)
            if match:
                extracted['timeframe'] = match.group(1)
                break
        
        # 提取技术指标
        indicators = [
            'rsi', 'macd', 'bollinger', 'moving average', 'ema', 'sma',
            'atr', 'adx', 'stochastic', 'fibonacci', 'pivot',
            'volume', 'obv', 'mfi', 'cci', 'williams %r',
        ]
        for ind in indicators:
            if ind in text_lower:
                extracted['indicators'].append(ind)
        
        # 提取回测数据
        metric_patterns = {
            'cagr': r'(?:cagr|annualized return|annual return).*?(\d+\.?\d*)\s*%?',
            'sharpe': r'(?:sharpe ratio|sharpe).*?(\d+\.?\d*)',
            'max_drawdown': r'(?:max drawdown|maximum drawdown|mdd).*?(\d+\.?\d*)\s*%?',
            'win_rate': r'(?:win rate|winning rate|success rate).*?(\d+\.?\d*)\s*%?',
            'profit_factor': r'(?:profit factor|pf).*?(\d+\.?\d*)',
            'total_trades': r'(?:total trades|number of trades|trades).*?(\d+)',
        }
        for metric, pattern in metric_patterns.items():
            match = re.search(pattern, text_lower)
            if match:
                extracted['backtest_metrics'][metric] = match.group(1)
        
        # 提取关键参数
        param_patterns = {
            'lookback': r'(?:lookback|period|window|length).*?(\d+)\s*(?:day|bar|period)?',
            'rsi_period': r'rsi\s*(?:period|length)?\s*(\d+)',
            'ma_fast': r'(?:fast|short)\s*(?:ma|ema|sma).*?(\d+)',
            'ma_slow': r'(?:slow|long)\s*(?:ma|ema|sma).*?(\d+)',
            'std_dev': r'(?:std dev|standard deviation|band).*?(\d+\.?\d*)',
        }
        for param, pattern in param_patterns.items():
            match = re.search(pattern, text_lower)
            if match:
                extracted['key_params'][param] = match.group(1)
        
        return extracted
    
    def generate_synthesis(self, theme: str, output_path: Path):
        """生成主题汇编报告"""
        if not self.processed:
            print("[错误] 无处理结果")
            return
        
        print(f"\n[生成] 主题汇编报告: {theme}")
        
        # 统计
        concrete_articles = [a for a in self.processed if a['concrete_score'] >= 3]
        
        lines = [
            f"# 主题深度分析: {theme}",
            f"",
            f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**分析文章数**: {len(self.processed)} 篇",
            f"**可复现策略**: {len(concrete_articles)} 篇",
            f"",
            f"## 文章清单",
            f"",
            f"| # | 标题 | 日期 | Concrete | 状态 |",
            f"|---|------|------|----------|------|",
        ]
        
        for i, article in enumerate(self.processed, 1):
            status = "✅ 可复现" if article['concrete_score'] >= 5 else ("🟡 部分" if article['concrete_score'] >= 3 else "🔴 概念")
            url = article.get('url', '')
            url_link = f"[{article['title'][:40]}...]({url})" if url else article['title'][:40]
            lines.append(
                f"| {i} | {url_link} | {article['date']} | {article['concrete_score']} | {status} |"
            )
        
        # 策略对比表
        lines.extend([
            f"",
            f"## 策略规则对比",
            f"",
            f"| 文章 | 入场规则 | 出场规则 | 止损 | 时间框架 | 指标 |",
            f"|------|---------|---------|------|---------|------|",
        ])
        
        for article in concrete_articles[:10]:  # 最多 10 篇
            ex = article['extracted']
            entry = '; '.join(ex['entry_rules'][:2]) if ex['entry_rules'] else '-'
            exit_r = '; '.join(ex['exit_rules'][:2]) if ex['exit_rules'] else '-'
            sl = ex['stop_loss'] or '-'
            tf = ex['timeframe'] or '-'
            inds = ', '.join(ex['indicators'][:3]) if ex['indicators'] else '-'
            
            lines.append(
                f"| {article['title'][:30]}... | {entry[:40]} | {exit_r[:40]} | {sl} | {tf} | {inds} |"
            )
        
        # 回测数据对比
        lines.extend([
            f"",
            f"## 回测数据对比",
            f"",
            f"| 文章 | CAGR | Sharpe | 最大回撤 | 胜率 | 交易次数 |",
            f"|------|------|--------|---------|------|---------|",
        ])
        
        for article in concrete_articles[:10]:
            m = article['extracted']['backtest_metrics']
            lines.append(
                f"| {article['title'][:30]}... | {m.get('cagr', '-')} | "
                f"{m.get('sharpe', '-')} | {m.get('max_drawdown', '-')} | "
                f"{m.get('win_rate', '-')} | {m.get('total_trades', '-')} |"
            )
        
        # 共同参数区间
        lines.extend([
            f"",
            f"## 共同参数区间",
            f"",
        ])
        
        all_params = defaultdict(list)
        for article in concrete_articles:
            for param, value in article['extracted']['key_params'].items():
                try:
                    all_params[param].append(float(value))
                except:
                    pass
        
        if all_params:
            lines.append("| 参数 | 最小值 | 最大值 | 中位数 | 出现次数 |")
            lines.append("|------|--------|--------|--------|---------|")
            for param, values in sorted(all_params.items()):
                lines.append(
                    f"| {param} | {min(values):.0f} | {max(values):.0f} | "
                    f"{sorted(values)[len(values)//2]:.0f} | {len(values)} |"
                )
        else:
            lines.append("（未提取到足够参数数据）")
        
        # 可复现策略配置
        lines.extend([
            f"",
            f"## 可复现策略配置",
            f"",
            f"以下策略已生成 YAML 配置文件，可直接用于回测：",
            f"",
        ])
        
        for i, article in enumerate(concrete_articles[:5], 1):
            safe_name = re.sub(r'[^\w]', '_', article['title'][:30])
            yaml_file = f"strategies/{safe_name}.yaml"
            lines.append(f"{i}. [{article['title']}]({yaml_file})")
        
        # 设计检查清单
        lines.extend([
            f"",
            f"## {theme} 策略设计 Checklist",
            f"",
            f"### 数据",
            f"- [ ] 确认品种历史数据覆盖回测期",
            f"- [ ] 检查数据质量（缺失值、异常值）",
            f"- [ ] 确认交易成本（佣金、滑点）",
            f"",
            f"### 信号",
            f"- [ ] 入场条件是否明确、可量化",
            f"- [ ] 出场条件是否完整（止盈/止损/时间）",
            f"- [ ] 信号是否存在 lookahead bias",
            f"",
            f"### 风险管理",
            f"- [ ] 单笔风险是否控制在 1-2%",
            f"- [ ] 是否有最大回撤限制",
            f"- [ ] 是否有仓位上限",
            f"",
            f"### 回测验证",
            f"- [ ] 样本外测试（walk-forward）",
            f"- [ ] 参数敏感性分析",
            f"- [ ] 不同市场环境表现",
            f"",
            f"### 实盘准备",
            f"- [ ] 执行延迟评估",
            f"- [ ] 流动性检查",
            f"- [ ] 极端行情应对预案",
            f"",
        ])
        
        # 矛盾与局限
        lines.extend([
            f"",
            f"## 矛盾观点与局限",
            f"",
            f"（需手动补充：不同文章对同一参数的建议是否矛盾）",
            f"",
        ])
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"[完成] 报告已保存: {output_path}")
    
    def generate_strategy_configs(self):
        """生成策略 YAML 配置文件"""
        concrete_articles = [a for a in self.processed if a['concrete_score'] >= 5]
        
        print(f"\n[生成] {len(concrete_articles)} 个策略配置")
        
        generated = []
        for article in concrete_articles:
            safe_name = re.sub(r'[^\w]', '_', article['title'][:40])
            yaml_path = STRATEGIES_DIR / f"{safe_name}.yaml"
            
            ex = article['extracted']
            
            # 推断信号类型
            signal_type = 'trend_breakout'
            if any('rsi' in r for r in ex['entry_rules']):
                signal_type = 'mean_reversion_rsi'
            elif any('bollinger' in i for i in ex['indicators']):
                signal_type = 'bollinger_bounce'
            elif any('crossover' in r for r in ex['entry_rules']):
                signal_type = 'momentum_crossover'
            elif any('session' in r for r in ex['entry_rules']):
                signal_type = 'session_high_retest'
            
            # 构建参数
            params = {}
            if 'lookback' in ex['key_params']:
                params['lookback'] = int(float(ex['key_params']['lookback']))
            if 'rsi_period' in ex['key_params']:
                params['rsi_period'] = int(float(ex['key_params']['rsi_period']))
            if 'ma_fast' in ex['key_params']:
                params['fast_period'] = int(float(ex['key_params']['ma_fast']))
            if 'ma_slow' in ex['key_params']:
                params['slow_period'] = int(float(ex['key_params']['ma_slow']))
            if 'std_dev' in ex['key_params']:
                params['std_dev'] = float(ex['key_params']['std_dev'])
            
            config = {
                'strategy': {
                    'name': article['title'][:60],
                    'description': f"From: {article.get('url', 'N/A')}",
                    'symbols': ['SPY'],  # 默认，需手动调整
                    'exchange': 'SMART',
                    'interval': 'd',
                    'start_date': '2014-01-01',
                    'end_date': '2024-12-31',
                    'signal_type': signal_type,
                    'params': params,
                    'stop_loss_pct': 0.05 if not ex['stop_loss'] else float(ex['stop_loss'].rstrip('%')) / 100,
                    'position_size': 1.0,
                }
            }
            
            with open(yaml_path, 'w', encoding='utf-8') as f:
                f.write(f"# 策略配置: {article['title']}\n")
                f.write(f"# 来源: {article.get('url', 'N/A')}\n")
                f.write(f"# 生成时间: {datetime.now().strftime('%Y-%m-%d')}\n")
                f.write(f"# 注意: 参数来自文章提取，可能需要手动校准\n\n")
                import yaml
                yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
            
            generated.append(yaml_path.name)
            print(f"  [生成] {yaml_path.name}")
        
        return generated


# ── 主流程 ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='批量深度处理主题文章')
    parser.add_argument('--theme', type=str, help='按标签过滤（如 strategy/mean-reversion）')
    parser.add_argument('--keyword', type=str, help='按关键词过滤')
    parser.add_argument('--max-articles', type=int, default=20, help='最大处理文章数')
    parser.add_argument('--output', type=str, help='输出文件名')
    parser.add_argument('--list-themes', action='store_true', help='列出所有主题分布')
    parser.add_argument('--skip-yaml', action='store_true', help='不生成 YAML 配置')
    
    args = parser.parse_args()
    
    # 扫描
    clusterer = ThemeClusterer()
    clusterer.scan_sources()
    
    if args.list_themes:
        themes = clusterer.get_themes_distribution()
        print("\n主题分布:")
        for theme, count in themes.items():
            print(f"  {theme}: {count}")
        return
    
    if not args.theme and not args.keyword:
        print("[错误] 请指定 --theme 或 --keyword")
        print("可用主题（前 20）:")
        themes = clusterer.get_themes_distribution()
        for theme, count in list(themes.items())[:20]:
            print(f"  {theme}: {count}")
        return
    
    # 过滤
    filtered = clusterer.filter_by_theme(args.theme, args.keyword)
    print(f"\n[过滤] 找到 {len(filtered)} 篇相关文章")
    
    if len(filtered) == 0:
        print("[错误] 无匹配文章")
        return
    
    # 限制数量
    filtered = filtered[:args.max_articles]
    
    # 深度处理
    processor = DeepProcessor(filtered)
    processor.process_all()
    
    # 生成报告
    theme_name = args.theme or args.keyword
    output_name = args.output or f"{theme_name.replace('/', '-')}-analysis.md"
    output_path = SYNTHESIS_DIR / output_name
    
    processor.generate_synthesis(theme_name, output_path)
    
    # 生成 YAML
    if not args.skip_yaml:
        configs = processor.generate_strategy_configs()
        print(f"\n[完成] 生成 {len(configs)} 个策略配置")
    
    print(f"\n{'='*60}")
    print("批量深度处理完成")
    print(f"报告: {output_path}")
    print(f"策略配置: {STRATEGIES_DIR}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
