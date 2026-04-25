#!/usr/bin/env python3
"""
策略复现模板 - 标准化策略回测框架
功能：
  1. 统一数据源接口（vnpy SQLite / CCXT OKX / yfinance）
  2. 信号注册系统（多种策略类型）
  3. 简化回测引擎（多空、止损止盈、仓位管理）
  4. 性能指标计算（年化收益、Sharpe、最大回撤、胜率）
  5. YAML 配置文件驱动
  6. 输出 CSV + Markdown 报告

用法：
  python3 strategy_repro_template.py --config strategy_config.yaml
  python3 strategy_repro_template.py --interactive  # 交互式配置
"""

import os
import sys
import json
import yaml
import sqlite3
import argparse
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Callable, Tuple, Any
from pathlib import Path
from datetime import datetime
from collections import defaultdict

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # 无头服务器模式
import matplotlib.pyplot as plt

# ── 配置 ────────────────────────────────────────────────
VNPAY_DB = "/root/.vntrader/database.db"
OUTPUT_DIR = Path(os.path.expanduser("~/llm-wiki/scripts/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── 数据类 ──────────────────────────────────────────────

@dataclass
class StrategyConfig:
    """策略配置"""
    name: str
    description: str = ""
    symbols: List[str] = field(default_factory=list)
    exchange: str = "SMART"
    interval: str = "d"
    start_date: str = "2014-01-01"
    end_date: str = "2024-12-31"
    
    # 信号参数
    signal_type: str = "trend_breakout"
    params: Dict[str, Any] = field(default_factory=dict)
    
    # 风控
    stop_loss_pct: Optional[float] = None
    take_profit_pct: Optional[float] = None
    trailing_stop_pct: Optional[float] = None
    position_size: float = 1.0
    max_positions: int = 1
    
    # 输出
    output_prefix: str = ""
    plot: bool = True
    save_csv: bool = True
    save_report: bool = True


@dataclass
class Trade:
    """单笔交易记录"""
    entry_date: datetime
    exit_date: Optional[datetime] = None
    entry_price: float = 0.0
    exit_price: float = 0.0
    direction: str = "long"  # long / short
    pnl_pct: float = 0.0
    pnl_dollar: float = 0.0
    exit_reason: str = ""  # signal, stop_loss, take_profit, trailing_stop, end


# ── 数据源 ──────────────────────────────────────────────

class DataSource:
    """统一数据源接口"""
    
    def __init__(self):
        self.vnpy_path = VNPAY_DB
        self._vnpy_conn = None
    
    def _get_vnpy_conn(self):
        """获取 vnpy 数据库连接（懒加载）"""
        if self._vnpy_conn is None:
            self._vnpy_conn = sqlite3.connect(self.vnpy_path)
        return self._vnpy_conn
    
    def get_data(self, symbol: str, exchange: str, interval: str,
                 start: str, end: str) -> Optional[pd.DataFrame]:
        """
        获取数据，按优先级尝试多个数据源
        返回 DataFrame: index=datetime, columns=[open,high,low,close,volume]
        """
        # 1. 尝试 vnpy
        df = self._from_vnpy(symbol, exchange, interval, start, end)
        if df is not None and len(df) > 0:
            print(f"  [数据] vnpy: {symbol}@{exchange} {len(df)} 条")
            return df
        
        # 2. 尝试 OKX (Crypto)
        if exchange.upper() in ['OKX', 'BINANCE', 'BYBIT'] or 'USDT' in symbol.upper():
            df = self._from_ccxt(symbol, exchange, interval, start, end)
            if df is not None and len(df) > 0:
                print(f"  [数据] CCXT: {symbol}@{exchange} {len(df)} 条")
                return df
        
        # 3. 尝试 yfinance（最后手段）
        df = self._from_yfinance(symbol, start, end)
        if df is not None and len(df) > 0:
            print(f"  [数据] yfinance: {symbol} {len(df)} 条")
            return df
        
        print(f"  [数据] 无法获取: {symbol}@{exchange}")
        return None
    
    def _from_vnpy(self, symbol: str, exchange: str, interval: str,
                   start: str, end: str) -> Optional[pd.DataFrame]:
        """从 vnpy SQLite 读取"""
        try:
            conn = self._get_vnpy_conn()
            query = """
                SELECT datetime, open_price, high_price, low_price, close_price, volume
                FROM dbbardata
                WHERE symbol = ? AND exchange = ? AND interval = ?
                AND datetime >= ? AND datetime <= ?
                ORDER BY datetime
            """
            df = pd.read_sql(query, conn, params=(symbol, exchange, interval, start, end))
            
            if len(df) == 0:
                return None
            
            df['datetime'] = pd.to_datetime(df['datetime'])
            df.set_index('datetime', inplace=True)
            df.rename(columns={
                'open_price': 'open',
                'high_price': 'high',
                'low_price': 'low',
                'close_price': 'close',
                'volume': 'volume'
            }, inplace=True)
            
            return df
        except Exception as e:
            print(f"  [数据] vnpy 错误: {e}")
            return None
    
    def _from_ccxt(self, symbol: str, exchange: str, interval: str,
                   start: str, end: str) -> Optional[pd.DataFrame]:
        """从 CCXT OKX 读取"""
        try:
            import ccxt
            
            # 标准化 symbol
            okx_symbol = symbol.upper().replace('_SWAP', '-SWAP')
            if '-SWAP' not in okx_symbol and 'USDT' in okx_symbol:
                okx_symbol = okx_symbol.replace('USDT', '-USDT-SWAP')
            
            ex = ccxt.okx({'enableRateLimit': True})
            
            # 转换时间
            since = int(pd.Timestamp(start).timestamp() * 1000)
            
            # 获取 K 线
            timeframe_map = {'d': '1d', '1h': '1h', '1m': '1m'}
            tf = timeframe_map.get(interval, interval)
            
            ohlcv = ex.fetch_ohlcv(okx_symbol, tf, since=since, limit=1000)
            
            if not ohlcv or len(ohlcv) == 0:
                return None
            
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('datetime', inplace=True)
            df = df[['open', 'high', 'low', 'close', 'volume']]
            
            # 过滤结束日期
            df = df[df.index <= end]
            
            return df
        except Exception as e:
            print(f"  [数据] CCXT 错误: {e}")
            return None
    
    def _from_yfinance(self, symbol: str, start: str, end: str) -> Optional[pd.DataFrame]:
        """从 yfinance 读取（备用）"""
        try:
            import yfinance as yf
            import time
            
            # 标准化 symbol
            yf_symbol = symbol.upper()
            if '.' not in yf_symbol and yf_symbol not in ['SPY', 'QQQ', 'DIA', 'IWM']:
                # 尝试添加交易所后缀
                pass
            
            # 添加延迟避免限流
            time.sleep(1.0)
            
            ticker = yf.Ticker(yf_symbol)
            df = ticker.history(start=start, end=end)
            
            if len(df) == 0:
                return None
            
            df.rename(columns={
                'Open': 'open',
                'High': 'high',
                'Low': 'low',
                'Close': 'close',
                'Volume': 'volume'
            }, inplace=True)
            
            return df[['open', 'high', 'low', 'close', 'volume']]
        except Exception as e:
            print(f"  [数据] yfinance 错误: {e}")
            return None
    
    def list_available_symbols(self, exchange: str = None) -> pd.DataFrame:
        """列出 vnpy 数据库中可用的品种"""
        try:
            conn = self._get_vnpy_conn()
            if exchange:
                query = """
                    SELECT symbol, exchange, count, start, end
                    FROM dbbaroverview
                    WHERE exchange = ? AND interval = 'd'
                    ORDER BY count DESC
                """
                df = pd.read_sql(query, conn, params=(exchange,))
            else:
                query = """
                    SELECT symbol, exchange, count, start, end
                    FROM dbbaroverview
                    WHERE interval = 'd'
                    ORDER BY count DESC
                """
                df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            print(f"[数据] 查询可用品种失败: {e}")
            return pd.DataFrame()


# ── 信号系统 ────────────────────────────────────────────

class SignalRegistry:
    """信号注册中心"""
    
    def __init__(self):
        self._signals: Dict[str, Callable] = {}
        self._register_builtin()
    
    def _register_builtin(self):
        """注册内置信号"""
        self.register('trend_breakout', self._trend_breakout)
        self.register('mean_reversion_rsi', self._mean_reversion_rsi)
        self.register('momentum_crossover', self._momentum_crossover)
        self.register('bollinger_bounce', self._bollinger_bounce)
        self.register('session_high_retest', self._session_high_retest)
        self.register('donchian_channel', self._donchian_channel)
        self.register('adx_trend', self._adx_trend)
        self.register('rsi_divergence', self._rsi_divergence)
    
    def register(self, name: str, func: Callable):
        """注册信号"""
        self._signals[name] = func
    
    def get(self, name: str) -> Optional[Callable]:
        """获取信号函数"""
        return self._signals.get(name)
    
    def list_signals(self) -> List[str]:
        """列出所有可用信号"""
        return list(self._signals.keys())
    
    # ── 内置信号实现 ────────────────────────────────────
    
    def _trend_breakout(self, df: pd.DataFrame, **params) -> pd.Series:
        """趋势突破：N 日高点突破"""
        lookback = params.get('lookback', 20)
        entry_on_close = params.get('entry_on_close', True)
        
        df['high_n'] = df['high'].rolling(lookback).max().shift(1)
        
        if entry_on_close:
            signal = (df['close'] > df['high_n']).astype(int)
        else:
            signal = (df['high'] > df['high_n']).astype(int)
        
        return signal
    
    def _mean_reversion_rsi(self, df: pd.DataFrame, **params) -> pd.Series:
        """RSI 均值回归：超卖买入，超买卖出"""
        rsi_period = params.get('rsi_period', 14)
        oversold = params.get('oversold', 30)
        overbought = params.get('overbought', 70)
        
        # 计算 RSI
        delta = df['close'].diff()
        gain = delta.where(delta > 0, 0).rolling(rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(rsi_period).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        signal = pd.Series(0, index=df.index)
        signal[df['rsi'] < oversold] = 1   # 买入
        signal[df['rsi'] > overbought] = -1  # 卖出
        
        return signal
    
    def _momentum_crossover(self, df: pd.DataFrame, **params) -> pd.Series:
        """均线交叉动量：快线上穿慢线买入"""
        fast = params.get('fast_period', 20)
        slow = params.get('slow_period', 50)
        
        df['ma_fast'] = df['close'].rolling(fast).mean()
        df['ma_slow'] = df['close'].rolling(slow).mean()
        
        signal = pd.Series(0, index=df.index)
        signal[(df['ma_fast'] > df['ma_slow']) & 
               (df['ma_fast'].shift(1) <= df['ma_slow'].shift(1))] = 1
        signal[(df['ma_fast'] < df['ma_slow']) & 
               (df['ma_fast'].shift(1) >= df['ma_slow'].shift(1))] = -1
        
        return signal
    
    def _bollinger_bounce(self, df: pd.DataFrame, **params) -> pd.Series:
        """布林带反弹：触及下轨买入，触及上轨卖出"""
        period = params.get('period', 20)
        std_dev = params.get('std_dev', 2.0)
        
        df['ma'] = df['close'].rolling(period).mean()
        df['std'] = df['close'].rolling(period).std()
        df['upper'] = df['ma'] + std_dev * df['std']
        df['lower'] = df['ma'] - std_dev * df['std']
        
        signal = pd.Series(0, index=df.index)
        signal[df['close'] < df['lower']] = 1
        signal[df['close'] > df['upper']] = -1
        
        return signal
    
    def _session_high_retest(self, df: pd.DataFrame, **params) -> pd.Series:
        """Session High Retest：前日高点回撤买入"""
        # 简化为前日高点突破后回撤
        df['prev_high'] = df['high'].shift(1)
        df['prev_low'] = df['low'].shift(1)
        
        signal = pd.Series(0, index=df.index)
        # 前日创新高，今日回撤到前高附近买入
        signal[(df['high'] > df['prev_high'].rolling(5).max().shift(1)) &
               (df['low'] <= df['prev_high'])] = 1
        
        return signal
    
    def _donchian_channel(self, df: pd.DataFrame, **params) -> pd.Series:
        """唐奇安通道突破"""
        lookback = params.get('lookback', 20)
        
        df['upper'] = df['high'].rolling(lookback).max().shift(1)
        df['lower'] = df['low'].rolling(lookback).min().shift(1)
        
        signal = pd.Series(0, index=df.index)
        signal[df['close'] > df['upper']] = 1
        signal[df['close'] < df['lower']] = -1
        
        return signal
    
    def _adx_trend(self, df: pd.DataFrame, **params) -> pd.Series:
        """ADX 趋势强度过滤"""
        adx_period = params.get('adx_period', 14)
        adx_threshold = params.get('adx_threshold', 25)
        
        # 简化版 ADX
        df['tr'] = np.maximum(
            df['high'] - df['low'],
            np.maximum(
                abs(df['high'] - df['close'].shift(1)),
                abs(df['low'] - df['close'].shift(1))
            )
        )
        df['atr'] = df['tr'].rolling(adx_period).mean()
        
        # 简化为 ATR 过滤的趋势跟随
        df['ma'] = df['close'].rolling(adx_period).mean()
        signal = pd.Series(0, index=df.index)
        signal[(df['close'] > df['ma']) & (df['atr'] > df['atr'].rolling(adx_period*2).mean())] = 1
        signal[(df['close'] < df['ma']) & (df['atr'] > df['atr'].rolling(adx_period*2).mean())] = -1
        
        return signal
    
    def _rsi_divergence(self, df: pd.DataFrame, **params) -> pd.Series:
        """RSI 背离"""
        rsi_period = params.get('rsi_period', 14)
        lookback = params.get('lookback', 20)
        
        delta = df['close'].diff()
        gain = delta.where(delta > 0, 0).rolling(rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(rsi_period).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        # 检测价格创新低但 RSI 未创新低（底背离）
        df['price_low'] = df['close'].rolling(lookback).min()
        df['rsi_low'] = df['rsi'].rolling(lookback).min()
        
        signal = pd.Series(0, index=df.index)
        signal[(df['close'] == df['price_low']) & (df['rsi'] > df['rsi_low'].shift(1))] = 1
        
        return signal


# ── 回测引擎 ────────────────────────────────────────────

class BacktestEngine:
    """简化回测引擎"""
    
    def __init__(self, config: StrategyConfig):
        self.config = config
        self.datasource = DataSource()
        self.signals = SignalRegistry()
        self.trades: List[Trade] = []
    
    def run(self) -> Dict:
        """运行回测"""
        print(f"\n{'='*60}")
        print(f"策略回测: {self.config.name}")
        print(f"{'='*60}")
        
        results = {}
        all_equity = {}
        
        for symbol in self.config.symbols:
            print(f"\n[品种] {symbol}")
            
            # 获取数据
            df = self.datasource.get_data(
                symbol, self.config.exchange, self.config.interval,
                self.config.start_date, self.config.end_date
            )
            
            if df is None or len(df) < 100:
                print(f"  [跳过] 数据不足")
                continue
            
            # 计算信号
            signal_fn = self.signals.get(self.config.signal_type)
            if signal_fn is None:
                print(f"  [错误] 未知信号: {self.config.signal_type}")
                continue
            
            df['signal'] = signal_fn(df, **self.config.params)
            
            # 运行交易模拟
            symbol_trades, equity_curve = self._simulate(df, symbol)
            self.trades.extend(symbol_trades)
            
            # 计算指标
            metrics = self._calculate_metrics(symbol_trades, equity_curve)
            results[symbol] = metrics
            all_equity[symbol] = equity_curve
            
            print(f"  交易次数: {metrics['num_trades']}")
            print(f"  总收益: {metrics['total_return']:.2%}")
            print(f"  年化收益: {metrics['annualized_return']:.2%}")
            print(f"  Sharpe: {metrics['sharpe_ratio']:.2f}")
            print(f"  最大回撤: {metrics['max_drawdown']:.2%}")
            print(f"  胜率: {metrics['win_rate']:.1%}")
        
        # 汇总
        if len(results) > 1:
            combined = self._combine_results(results)
            results['_combined'] = combined
        
        # 输出
        if self.config.save_csv and all_equity:
            self._save_csv(all_equity)
        
        if self.config.save_report:
            self._save_report(results)
        
        if self.config.plot and all_equity:
            self._plot(all_equity, results)
        
        return results
    
    def _simulate(self, df: pd.DataFrame, symbol: str) -> Tuple[List[Trade], pd.Series]:
        """模拟交易"""
        trades = []
        position = None  # None, 'long', 'short'
        entry_price = 0
        entry_date = None
        
        equity = [1.0]  # 初始资金
        
        for i in range(1, len(df)):
            date = df.index[i]
            price = df['close'].iloc[i]
            prev_price = df['close'].iloc[i-1]
            signal = df['signal'].iloc[i]
            
            # 检查止损/止盈（简化：基于收盘价）
            if position is not None:
                pnl_pct = (price - entry_price) / entry_price
                if position == 'short':
                    pnl_pct = -pnl_pct
                
                exit_reason = None
                
                # 止损
                if self.config.stop_loss_pct and pnl_pct < -self.config.stop_loss_pct:
                    exit_reason = 'stop_loss'
                
                # 止盈
                elif self.config.take_profit_pct and pnl_pct > self.config.take_profit_pct:
                    exit_reason = 'take_profit'
                
                # 信号反转
                elif (position == 'long' and signal == -1) or (position == 'short' and signal == 1):
                    exit_reason = 'signal'
                
                # 出场
                if exit_reason:
                    trade = Trade(
                        entry_date=entry_date,
                        exit_date=date,
                        entry_price=entry_price,
                        exit_price=price,
                        direction=position,
                        pnl_pct=pnl_pct,
                        exit_reason=exit_reason
                    )
                    trades.append(trade)
                    equity.append(equity[-1] * (1 + pnl_pct * self.config.position_size))
                    position = None
            
            # 检查入场
            if position is None and signal == 1:
                position = 'long'
                entry_price = price
                entry_date = date
            elif position is None and signal == -1:
                position = 'short'
                entry_price = price
                entry_date = date
            else:
                # 无变化，延续上一期权益
                if len(equity) <= i:
                    equity.append(equity[-1])
        
        # 平仓剩余仓位
        if position is not None:
            last_price = df['close'].iloc[-1]
            pnl_pct = (last_price - entry_price) / entry_price
            if position == 'short':
                pnl_pct = -pnl_pct
            
            trade = Trade(
                entry_date=entry_date,
                exit_date=df.index[-1],
                entry_price=entry_price,
                exit_price=last_price,
                direction=position,
                pnl_pct=pnl_pct,
                exit_reason='end'
            )
            trades.append(trade)
            equity.append(equity[-1] * (1 + pnl_pct * self.config.position_size))
        
        equity_series = pd.Series(equity, index=df.index[:len(equity)])
        return trades, equity_series
    
    def _calculate_metrics(self, trades: List[Trade], equity: pd.Series) -> Dict:
        """计算性能指标"""
        if not trades:
            return {
                'num_trades': 0, 'total_return': 0, 'annualized_return': 0,
                'sharpe_ratio': 0, 'max_drawdown': 0, 'win_rate': 0,
                'avg_trade': 0, 'profit_factor': 0, 'equity': equity,
            }
        
        pnls = [t.pnl_pct for t in trades]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p <= 0]
        
        total_return = equity.iloc[-1] / equity.iloc[0] - 1
        
        # 年化收益（假设 252 交易日/年）
        years = len(equity) / 252
        annualized = (1 + total_return) ** (1 / max(years, 0.1)) - 1
        
        # Sharpe（简化，假设无风险利率 0）
        daily_returns = equity.pct_change().dropna()
        sharpe = daily_returns.mean() / daily_returns.std() * np.sqrt(252) if daily_returns.std() > 0 else 0
        
        # 最大回撤
        cummax = equity.cummax()
        drawdown = (equity - cummax) / cummax
        max_dd = drawdown.min()
        
        # 胜率
        win_rate = len(wins) / len(pnls) if pnls else 0
        
        # 盈亏比
        avg_win = np.mean(wins) if wins else 0
        avg_loss = abs(np.mean(losses)) if losses else 1e-6
        profit_factor = avg_win / avg_loss if avg_loss > 0 else float('inf')
        
        return {
            'num_trades': len(trades),
            'total_return': total_return,
            'annualized_return': annualized,
            'sharpe_ratio': sharpe,
            'max_drawdown': max_dd,
            'win_rate': win_rate,
            'avg_trade': np.mean(pnls),
            'profit_factor': profit_factor,
            'equity': equity,
            'trades': trades,
        }
    
    def _combine_results(self, results: Dict) -> Dict:
        """合并多品种结果"""
        all_trades = []
        for symbol, metrics in results.items():
            if symbol.startswith('_'):
                continue
            all_trades.extend(metrics.get('trades', []))
        
        # 简化：取平均指标
        metrics_list = [m for s, m in results.items() if not s.startswith('_')]
        if not metrics_list:
            return {}
        
        return {
            'num_trades': sum(m['num_trades'] for m in metrics_list),
            'total_return': np.mean([m['total_return'] for m in metrics_list]),
            'annualized_return': np.mean([m['annualized_return'] for m in metrics_list]),
            'sharpe_ratio': np.mean([m['sharpe_ratio'] for m in metrics_list]),
            'max_drawdown': np.mean([m['max_drawdown'] for m in metrics_list]),
            'win_rate': np.mean([m['win_rate'] for m in metrics_list]),
        }
    
    def _save_csv(self, all_equity: Dict[str, pd.Series]):
        """保存 CSV"""
        prefix = self.config.output_prefix or self.config.name.replace(' ', '_')
        
        # 保存权益曲线
        equity_df = pd.DataFrame(all_equity)
        csv_path = OUTPUT_DIR / f"{prefix}_equity.csv"
        equity_df.to_csv(csv_path)
        print(f"\n[输出] 权益曲线: {csv_path}")
        
        # 保存交易记录
        if self.trades:
            trades_data = []
            for t in self.trades:
                trades_data.append({
                    'entry_date': t.entry_date,
                    'exit_date': t.exit_date,
                    'entry_price': t.entry_price,
                    'exit_price': t.exit_price,
                    'direction': t.direction,
                    'pnl_pct': t.pnl_pct,
                    'exit_reason': t.exit_reason,
                })
            trades_df = pd.DataFrame(trades_data)
            trades_path = OUTPUT_DIR / f"{prefix}_trades.csv"
            trades_df.to_csv(trades_path, index=False)
            print(f"[输出] 交易记录: {trades_path}")
    
    def _save_report(self, results: Dict):
        """保存 Markdown 报告"""
        prefix = self.config.output_prefix or self.config.name.replace(' ', '_')
        report_path = OUTPUT_DIR / f"{prefix}_report.md"
        
        lines = [
            f"# 策略回测报告: {self.config.name}",
            f"",
            f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**信号类型**: {self.config.signal_type}",
            f"**品种**: {', '.join(self.config.symbols)}",
            f"**交易所**: {self.config.exchange}",
            f"**时间框架**: {self.config.interval}",
            f"**回测区间**: {self.config.start_date} ~ {self.config.end_date}",
            f"",
            f"## 参数配置",
            f"",
            f"```yaml",
            yaml.dump(self.config.params, default_flow_style=False),
            f"```",
            f"",
            f"## 回测结果",
            f"",
            f"| 品种 | 交易次数 | 总收益 | 年化收益 | Sharpe | 最大回撤 | 胜率 |",
            f"|------|---------|--------|---------|--------|---------|------|",
        ]
        
        for symbol, metrics in results.items():
            if symbol.startswith('_'):
                continue
            lines.append(
                f"| {symbol} | {metrics['num_trades']} | "
                f"{metrics['total_return']:.2%} | {metrics['annualized_return']:.2%} | "
                f"{metrics['sharpe_ratio']:.2f} | {metrics['max_drawdown']:.2%} | "
                f"{metrics['win_rate']:.1%} |"
            )
        
        # 汇总行
        if '_combined' in results:
            c = results['_combined']
            lines.append(
                f"| **平均** | {c['num_trades']} | "
                f"{c['total_return']:.2%} | {c['annualized_return']:.2%} | "
                f"{c['sharpe_ratio']:.2f} | {c['max_drawdown']:.2%} | "
                f"{c['win_rate']:.1%} |"
            )
        
        lines.extend([
            f"",
            f"## 详细说明",
            f"",
            f"- 止损: {self.config.stop_loss_pct or '无'}",
            f"- 止盈: {self.config.take_profit_pct or '无'}",
            f"- 仓位: {self.config.position_size}",
            f"",
            f"## 局限性",
            f"",
            f"- 简化回测，未考虑滑点和佣金",
            f"- 信号基于收盘价，可能与实际执行有偏差",
            f"- 多品种等权配置，未优化权重",
            f"",
        ])
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"[输出] 报告: {report_path}")
    
    def _plot(self, all_equity: Dict, results: Dict):
        """绘制图表"""
        prefix = self.config.output_prefix or self.config.name.replace(' ', '_')
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        # 权益曲线
        ax1 = axes[0]
        for symbol, equity in all_equity.items():
            if not symbol.startswith('_'):
                ax1.plot(equity.index, equity.values / equity.values[0], label=symbol, alpha=0.7)
        ax1.set_title(f'Equity Curve: {self.config.name}')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Normalized Equity')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 回撤
        ax2 = axes[1]
        for symbol, equity in all_equity.items():
            if not symbol.startswith('_'):
                cummax = equity.cummax()
                drawdown = (equity - cummax) / cummax
                ax2.fill_between(equity.index, drawdown.values, 0, alpha=0.3, label=symbol)
        ax2.set_title('Drawdown')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Drawdown')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plot_path = OUTPUT_DIR / f"{prefix}_chart.png"
        plt.savefig(plot_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"[输出] 图表: {plot_path}")


# ── 配置加载 ────────────────────────────────────────────

def load_config_from_yaml(path: str) -> StrategyConfig:
    """从 YAML 加载配置"""
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    strategy_data = data.get('strategy', data)
    
    return StrategyConfig(
        name=strategy_data.get('name', 'Unnamed'),
        description=strategy_data.get('description', ''),
        symbols=strategy_data.get('symbols', []),
        exchange=strategy_data.get('exchange', 'SMART'),
        interval=strategy_data.get('interval', 'd'),
        start_date=strategy_data.get('start_date', '2014-01-01'),
        end_date=strategy_data.get('end_date', '2024-12-31'),
        signal_type=strategy_data.get('signal_type', 'trend_breakout'),
        params=strategy_data.get('params', {}),
        stop_loss_pct=strategy_data.get('stop_loss_pct'),
        take_profit_pct=strategy_data.get('take_profit_pct'),
        trailing_stop_pct=strategy_data.get('trailing_stop_pct'),
        position_size=strategy_data.get('position_size', 1.0),
        max_positions=strategy_data.get('max_positions', 1),
        output_prefix=strategy_data.get('output_prefix', ''),
        plot=strategy_data.get('plot', True),
        save_csv=strategy_data.get('save_csv', True),
        save_report=strategy_data.get('save_report', True),
    )


def interactive_config() -> StrategyConfig:
    """交互式配置"""
    print("\n" + "="*60)
    print("策略复现 - 交互式配置")
    print("="*60)
    
    name = input("策略名称: ").strip()
    
    print("\n可用信号类型:")
    registry = SignalRegistry()
    for i, sig in enumerate(registry.list_signals(), 1):
        print(f"  {i}. {sig}")
    
    signal_idx = int(input("选择信号 (编号): ")) - 1
    signals = registry.list_signals()
    signal_type = signals[signal_idx] if 0 <= signal_idx < len(signals) else 'trend_breakout'
    
    symbols_str = input("品种 (逗号分隔, 如 SPY,QQQ): ").strip()
    symbols = [s.strip() for s in symbols_str.split(',')]
    
    exchange = input("交易所 (默认 SMART): ").strip() or "SMART"
    
    stop_loss = input("止损 % (如 0.05 表示 5%, 默认无): ").strip()
    stop_loss = float(stop_loss) if stop_loss else None
    
    print("\n配置完成，开始回测...")
    
    return StrategyConfig(
        name=name,
        symbols=symbols,
        exchange=exchange,
        signal_type=signal_type,
        stop_loss_pct=stop_loss,
    )


def main():
    parser = argparse.ArgumentParser(description='策略复现模板')
    parser.add_argument('--config', type=str, help='YAML 配置文件路径')
    parser.add_argument('--interactive', action='store_true', help='交互式配置')
    parser.add_argument('--list-signals', action='store_true', help='列出可用信号')
    parser.add_argument('--list-symbols', type=str, help='列出 vnpy 中某交易所的可用品种')
    
    args = parser.parse_args()
    
    if args.list_signals:
        registry = SignalRegistry()
        print("可用信号类型:")
        for sig in registry.list_signals():
            print(f"  - {sig}")
        return
    
    if args.list_symbols:
        ds = DataSource()
        df = ds.list_available_symbols(args.list_symbols)
        if len(df) > 0:
            print(df.to_string())
        else:
            print(f"未找到交易所 {args.list_symbols} 的数据")
        return
    
    # 加载配置
    if args.interactive:
        config = interactive_config()
    elif args.config:
        config = load_config_from_yaml(args.config)
    else:
        # 默认演示配置
        config = StrategyConfig(
            name="SPY 20-Day Breakout",
            symbols=["SPY"],
            exchange="SMART",
            signal_type="trend_breakout",
            params={"lookback": 20, "entry_on_close": True},
            stop_loss_pct=0.05,
            start_date="2014-01-01",
            end_date="2024-12-31",
        )
        print("使用默认演示配置，可通过 --config 指定 YAML 文件")
    
    # 运行回测
    engine = BacktestEngine(config)
    results = engine.run()
    
    print(f"\n{'='*60}")
    print("回测完成")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
