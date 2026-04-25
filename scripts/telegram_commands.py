#!/usr/bin/env python3
"""
Telegram Bot 命令扩展模块
为 Hermes Gateway 添加自定义命令，支持策略工作流快捷操作

用法：
  将此模块集成到 Hermes Gateway 或作为独立 webhook 服务运行

支持的命令：
  /ingest <url>     - 抓取单篇文章并入库
  /batch <theme>    - 批量处理某主题文章
  /repro <name>     - 一键复现策略
  /status           - 查看今日处理统计
  /queue            - 查看待处理队列
  /synth <theme>    - 生成主题汇编报告
  /themes           - 列出所有主题分布
  /data <symbol>    - 检查品种数据可用性
"""

import os
import sys
import re
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, List

# ── 路径配置 ──────────────────────────────────────────
VAULT_DIR = Path(os.path.expanduser("~/llm-wiki"))
SCRIPTS_DIR = VAULT_DIR / "scripts"
TRACKER_DIR = Path("/root/.openclaw/workspace/skills/substack-strategy-tracker")

# ── 命令处理器 ────────────────────────────────────────

class CommandHandler:
    """Telegram 命令处理器"""
    
    def __init__(self):
        self.commands = {
            'ingest': self.cmd_ingest,
            'batch': self.cmd_batch,
            'repro': self.cmd_repro,
            'status': self.cmd_status,
            'queue': self.cmd_queue,
            'synth': self.cmd_synth,
            'themes': self.cmd_themes,
            'data': self.cmd_data,
            'help': self.cmd_help,
        }
    
    def handle(self, command: str, args: List[str]) -> str:
        """处理命令"""
        cmd = command.lower().lstrip('/')
        handler = self.commands.get(cmd)
        
        if not handler:
            return f"未知命令: /{cmd}\n使用 /help 查看可用命令"
        
        try:
            return handler(args)
        except Exception as e:
            return f"命令执行错误: {e}"
    
    def cmd_ingest(self, args: List[str]) -> str:
        """/ingest <url> - 抓取单篇文章并入库"""
        if not args:
            return "用法: /ingest <substack_url>\n示例: /ingest https://quantifiedstrategies.substack.com/p/article"
        
        url = args[0]
        
        if 'substack.com' not in url:
            return "错误: 目前仅支持 Substack 文章"
        
        # 调用 auto_ingest 处理单个 URL
        # 实际实现：curl 获取 + Python 解析 + 入库
        return f"🔄 正在处理: {url}\n\n（实际实现需要调用 auto_ingest.py 的单 URL 模式）"
    
    def cmd_batch(self, args: List[str]) -> str:
        """/batch <theme> - 批量处理某主题文章"""
        if not args:
            return "用法: /batch <theme_tag>\n示例: /batch strategy/mean-reversion\n\n可用主题: /themes"
        
        theme = args[0]
        
        # 调用 batch_deep_process.py
        script = SCRIPTS_DIR / "batch_deep_process.py"
        if not script.exists():
            return "错误: batch_deep_process.py 未安装"
        
        try:
            result = subprocess.run(
                [sys.executable, str(script), '--theme', theme, '--max-articles', '20'],
                capture_output=True, text=True, timeout=300
            )
            
            if result.returncode == 0:
                # 提取关键信息
                output = result.stdout
                # 查找报告路径
                report_match = re.search(r'报告:\s*(\S+)', output)
                report_path = report_match.group(1) if report_match else "未知"
                
                return f"✅ 批量处理完成\n\n主题: {theme}\n报告: `{report_path}`\n\n使用 /synth {theme} 查看详细报告"
            else:
                return f"❌ 处理失败:\n```\n{result.stderr[:500]}\n```"
        except Exception as e:
            return f"❌ 执行错误: {e}"
    
    def cmd_repro(self, args: List[str]) -> str:
        """/repro <name> - 一键复现策略"""
        if not args:
            return "用法: /repro <strategy_name_or_yaml_file>\n示例: /repro SPY_20-Day_Breakout\n\n查看可用策略: ls ~/llm-wiki/wiki/strategies/"
        
        name = args[0]
        
        # 查找 YAML 配置
        yaml_path = STRATEGIES_DIR / f"{name}.yaml"
        if not yaml_path.exists():
            # 尝试模糊匹配
            available = list(STRATEGIES_DIR.glob("*.yaml"))
            matches = [f.stem for f in available if name.lower() in f.stem.lower()]
            
            if matches:
                return f"未找到精确匹配 '{name}'\n\n相似策略:\n" + '\n'.join(f"  - {m}" for m in matches[:5])
            else:
                return f"未找到策略 '{name}'\n\n使用 /batch 处理主题后生成策略配置"
        
        # 调用回测
        script = SCRIPTS_DIR / "strategy_repro_template.py"
        try:
            result = subprocess.run(
                [sys.executable, str(script), '--config', str(yaml_path)],
                capture_output=True, text=True, timeout=300
            )
            
            if result.returncode == 0:
                # 提取结果
                output = result.stdout
                
                # 查找关键指标
                metrics = {}
                for line in output.split('\n'):
                    if '总收益:' in line:
                        metrics['total_return'] = line.split(':')[1].strip()
                    elif '年化收益:' in line:
                        metrics['annualized'] = line.split(':')[1].strip()
                    elif 'Sharpe:' in line:
                        metrics['sharpe'] = line.split(':')[1].strip()
                    elif '最大回撤:' in line:
                        metrics['max_dd'] = line.split(':')[1].strip()
                    elif '胜率:' in line:
                        metrics['win_rate'] = line.split(':')[1].strip()
                
                report = f"✅ 策略回测完成: {name}\n\n"
                if metrics:
                    report += "| 指标 | 数值 |\n|------|------|\n"
                    for k, v in metrics.items():
                        report += f"| {k} | {v} |\n"
                
                report += f"\n详细报告: `~/llm-wiki/scripts/output/{name}_report.md`"
                return report
            else:
                return f"❌ 回测失败:\n```\n{result.stderr[:500]}\n```"
        except Exception as e:
            return f"❌ 执行错误: {e}"
    
    def cmd_status(self, args: List[str]) -> str:
        """/status - 查看今日处理统计"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        # 统计今日入库
        sources_dir = VAULT_DIR / "wiki" / "sources"
        raw_dir = VAULT_DIR / "raw" / "articles"
        
        today_sources = 0
        today_raw = 0
        
        if sources_dir.exists():
            for f in sources_dir.iterdir():
                if f.is_file() and datetime.fromtimestamp(f.stat().st_mtime).strftime('%Y-%m-%d') == today:
                    today_sources += 1
        
        if raw_dir.exists():
            for f in raw_dir.iterdir():
                if f.is_file() and datetime.fromtimestamp(f.stat().st_mtime).strftime('%Y-%m-%d') == today:
                    today_raw += 1
        
        # 统计策略配置
        strategies_dir = VAULT_DIR / "wiki" / "strategies"
        strategy_count = len(list(strategies_dir.glob("*.yaml"))) if strategies_dir.exists() else 0
        
        # 统计合成报告
        synth_dir = VAULT_DIR / "wiki" / "syntheses"
        synth_count = len(list(synth_dir.glob("*.md"))) if synth_dir.exists() else 0
        
        return f"""📊 今日处理统计 ({today})

**入库**: {today_sources} 篇 sources, {today_raw} 篇 raw
**累计**: {len(list(sources_dir.glob('*.md'))) if sources_dir.exists() else 0} sources, {len(list(raw_dir.glob('*.md'))) if raw_dir.exists() else 0} raw
**策略配置**: {strategy_count} 个
**主题报告**: {synth_count} 份

常用命令:
  /batch <theme> - 批量处理
  /synth <theme> - 查看报告
  /themes - 主题分布
"""
    
    def cmd_queue(self, args: List[str]) -> str:
        """/queue - 查看待处理队列"""
        # 检查策略工厂队列
        queue_file = Path("/root/.openclaw/workspace/strategy_factory/.pipeline_queue.json")
        
        if not queue_file.exists():
            return "📭 队列为空"
        
        try:
            with open(queue_file, 'r') as f:
                queue = json.load(f)
            
            pending = [q for q in queue if q.get('status') == 'pending']
            completed = [q for q in queue if q.get('status') == 'completed']
            
            if not pending:
                return f"📭 无待处理任务\n\n已完成: {len(completed)} 篇"
            
            report = f"📋 待处理队列 ({len(pending)} 篇)\n\n"
            for i, item in enumerate(pending[:10], 1):
                report += f"{i}. {item.get('title', 'Unknown')[:50]}...\n"
                report += f"   来源: {item.get('source_id', 'Unknown')}\n"
            
            if len(pending) > 10:
                report += f"\n... 还有 {len(pending) - 10} 篇"
            
            return report
        except Exception as e:
            return f"❌ 读取队列失败: {e}"
    
    def cmd_synth(self, args: List[str]) -> str:
        """/synth <theme> - 生成/查看主题汇编报告"""
        if not args:
            return "用法: /synth <theme>\n示例: /synth strategy/mean-reversion\n\n可用主题: /themes"
        
        theme = args[0]
        
        # 检查是否已有报告
        safe_theme = theme.replace('/', '-')
        report_path = VAULT_DIR / "wiki" / "syntheses" / f"{safe_theme}-analysis.md"
        
        if report_path.exists():
            # 读取报告摘要
            try:
                with open(report_path, 'r') as f:
                    content = f.read()
                
                # 提取文章清单行数
                article_count = content.count('| ') - content.count('|------')
                
                return f"📑 主题报告已存在: {theme}\n\n文章数: ~{max(article_count, 0)} 篇\n路径: `{report_path}`\n\n使用 /batch {theme} 重新生成"
            except:
                return f"📑 主题报告: {report_path}"
        
        # 生成新报告
        return self.cmd_batch([theme])
    
    def cmd_themes(self, args: List[str]) -> str:
        """/themes - 列出所有主题分布"""
        script = SCRIPTS_DIR / "batch_deep_process.py"
        if not script.exists():
            return "错误: batch_deep_process.py 未安装"
        
        try:
            result = subprocess.run(
                [sys.executable, str(script), '--list-themes'],
                capture_output=True, text=True, timeout=60
            )
            
            if result.returncode == 0:
                output = result.stdout
                # 格式化输出
                lines = output.split('\n')
                themes = []
                for line in lines:
                    if ':' in line and not line.startswith('['):
                        themes.append(line.strip())
                
                if themes:
                    report = "📚 主题分布\n\n"
                    for t in themes[:20]:
                        report += f"  {t}\n"
                    
                    if len(themes) > 20:
                        report += f"\n... 还有 {len(themes) - 20} 个主题"
                    
                    report += "\n使用 /batch <theme> 处理特定主题"
                    return report
            
            return "暂无主题数据，请先入库文章"
        except Exception as e:
            return f"❌ 查询失败: {e}"
    
    def cmd_data(self, args: List[str]) -> str:
        """/data <symbol> - 检查品种数据可用性"""
        if not args:
            return "用法: /data <symbol>\n示例: /data SPY\n\n查看所有: /data --list"
        
        symbol = args[0].upper()
        
        if symbol == '--list':
            # 列出 vnpy 中的品种
            script = SCRIPTS_DIR / "strategy_repro_template.py"
            try:
                result = subprocess.run(
                    [sys.executable, str(script), '--list-symbols', 'SMART'],
                    capture_output=True, text=True, timeout=60
                )
                return f"📊 可用品种 (SMART):\n```\n{result.stdout[:2000]}\n```"
            except Exception as e:
                return f"❌ 查询失败: {e}"
        
        # 检查特定品种
        import sqlite3
        try:
            conn = sqlite3.connect("/root/.vntrader/database.db")
            query = """
                SELECT symbol, exchange, count, start, end
                FROM dbbaroverview
                WHERE symbol = ? AND interval = 'd'
            """
            df = pd.read_sql(query, conn, params=(symbol,))
            conn.close()
            
            if len(df) > 0:
                row = df.iloc[0]
                return f"""✅ 数据可用: {symbol}

| 字段 | 值 |
|------|-----|
| 品种 | {row['symbol']} |
| 交易所 | {row['exchange']} |
| 数据条数 | {row['count']} |
| 起始 | {row['start']} |
| 结束 | {row['end']} |

使用 /repro 运行策略回测
"""
            else:
                return f"❌ 未找到品种: {symbol}\n\n使用 /data --list 查看可用品种"
        except Exception as e:
            return f"❌ 查询失败: {e}"
    
    def cmd_help(self, args: List[str]) -> str:
        """/help - 帮助信息"""
        return """🤖 Substack 策略工作流 Bot

**文章处理**:
  /ingest <url>    - 抓取单篇文章并入库
  /batch <theme>   - 批量处理某主题文章
  /status          - 今日处理统计

**策略复现**:
  /repro <name>    - 一键回测策略
  /data <symbol>   - 检查品种数据
  /queue           - 查看待处理队列

**分析汇总**:
  /synth <theme>   - 生成/查看主题报告
  /themes          - 列出所有主题分布

**示例流程**:
  1. /themes                    # 查看有哪些主题
  2. /batch strategy/trend-following  # 批量处理趋势策略
  3. /synth strategy/trend-following  # 查看汇总报告
  4. /repro SPY_20-Day_Breakout      # 回测具体策略
"""


# ── 集成接口 ────────────────────────────────────────────

def process_telegram_message(text: str) -> str:
    """
    处理 Telegram 消息文本
    返回回复文本
    
    集成到 Hermes Gateway:
    - 在 gateway 的 message handler 中调用此函数
    - 如果消息以 / 开头，传递给 CommandHandler
    """
    if not text.startswith('/'):
        return None  # 不是命令，让 gateway 正常处理
    
    # 解析命令和参数
    parts = text.split()
    command = parts[0]
    args = parts[1:]
    
    handler = CommandHandler()
    return handler.handle(command, args)


# ── 测试 ──────────────────────────────────────────────

def test():
    """测试命令"""
    handler = CommandHandler()
    
    print("=" * 60)
    print("测试 Telegram 命令")
    print("=" * 60)
    
    # 测试 help
    print("\n/help:")
    print(handler.handle('/help', []))
    
    # 测试 status
    print("\n/status:")
    print(handler.handle('/status', []))
    
    # 测试 themes
    print("\n/themes:")
    print(handler.handle('/themes', []))
    
    # 测试 batch
    print("\n/batch strategy/mean-reversion:")
    print(handler.handle('/batch', ['strategy/mean-reversion']))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test()
    else:
        print("Telegram Bot 命令扩展模块")
        print("集成到 Hermes Gateway 使用")
        print("\n测试: python3 telegram_commands.py --test")
