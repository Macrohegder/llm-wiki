# Strategy #15: A Simple Short System That Profits From Bear Market Rallies

**原文链接**: https://algomatictrading.substack.com/p/strategy-15-a-simple-short-system

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:22:24

---

## 摘要

Strategy #15: A Simple Short System That Profits From Bear Market Rallies
When markets bounce inside a downtrend, most traders buy hope. This strategy sells it.
Algomatic Trading
Feb 22, 2026
∙ Paid
9
5
Share
Ever watched a market rally for a few days right in the middle of a downtrend?
Does that bounce actually mean something? Or is it just noise that’s about to get faded back down?
And can you systematically profit from fading it across completely different asset classes?
That’s what this post is about.
Today we’re looking at a short-only swing system built on a single idea: when price is below the long-term MA and RSI spikes to extreme overbought levels, the bounce is more likely exhaustion than reversal.
We tested this on three very different markets: TLT (US 20+ Year Treasury ETF), th...

---

## 全文

Strategy #15: A Simple Short System That Profits From Bear Market Rallies
When markets bounce inside a downtrend, most traders buy hope. This strategy sells it.
Algomatic Trading
Feb 22, 2026
∙ Paid
9
5
Share
Ever watched a market rally for a few days right in the middle of a downtrend?
Does that bounce actually mean something? Or is it just noise that’s about to get faded back down?
And can you systematically profit from fading it across completely different asset classes?
That’s what this post is about.
Today we’re looking at a short-only swing system built on a single idea: when price is below the long-term MA and RSI spikes to extreme overbought levels, the bounce is more likely exhaustion than reversal.
We tested this on three very different markets: TLT (US 20+ Year Treasury ETF), the DAX 40, and the Euro Stoxx 50. Same logic. Three markets. The results across all three are worth talking about.
Subscribe for free
below if you want this kind of research landing in your inbox regularly.
Subscribe
The Hypothesis
Markets trend. But even in downtrends prices don’t fall in a straight line, they bounce, sometimes sharply. These short-term countertrend moves are driven by short covering, macro noise, or just raw mean-reversion mechanics. They feel like reversals. They rarely are.
The hypothesis is this: when a market is in a confirmed bear regime (price below the long-term MA), a sudden strength spike signals temporary exhaustion, not genuine buying conviction. The market has gotten ahead of itself in the short term. When it snaps back and strength crashes toward oversold levels, the short trade pays off.
It’s a mean-reversion entry inside a trend-following framework. The regime filter is where the edge lives. Without it, you’re just randomly fading rallies. With it, you’re working with the trend, not against it.
Strategy Overview
This is a short-only mean-reversion system that activates exclusively in bear regimes price below the long-term simple moving average. When RSI spikes into extreme overbought territory, the system enters short at market. It exits when strength mean-reverts to oversold levels, or after a maximum hold period if that reversion hasn’t come.
Position size is dynamically adjusted, scaling down when markets are moving fast, scaling up when they’re quieter.
The same core logic was applied to three markets: TLT, DAX 40, and Euro Stoxx 50.
No curve-fitting per market. One system, three instruments.
Why It Works
The trend filter is doing most of the heavy lifting.
A short-term RSI spike in a bull trend can sustain for a long time, the market is strong, buyers keep coming. But once the broader regime turns bearish, that dynamic flips. The path of least resistance is down, and short-term rallies tend to run out of steam quickly.
The RSI component is deliberately set to be hypersensitive, it’s designed to catch moments of short-term exhaustion, not sustained momentum shifts. In a bear regime, those moments are fading opportunities. The time stop keeps capital efficient, and the position sizing adapts to market conditions automatically. It’s a system that knows when to pull back.
I Also Tested This On…
The strategy was built and validated across three instruments simultaneously.
TLT
(US 20+ Year Treasury Bond ETF) gives you exposure to rate-driven bear regimes, typically associated with rising rate environments or macro risk-off periods where bonds sell off hard.
DAX 40
brings you into European equity territory, a market known for sharp, emotionally-driven intraday moves and strong trend behaviour. Bear regimes here can be prolonged and volatile.
Euro Stoxx 50
is the broader European blue-chip benchmark, slightly less volatile than the DAX but with its own distinct bear regime characteristics, often tied to European macro and political cycles.
Running the same system across these three gives a much stronger signal than a single-market backtest. If the edge only shows up on one instrument, it’s probably noise. When it shows up across bonds and two European equity indices with different volatility profiles, that’s something more interesting.
Equity curves and per-market stats for all three instruments are below.
Backtest Setup 1 (DAX40)
Instrument:
DAX40 5€ (Futures).
Timeframe:
Daily bars.
Period Tested:
Jan 2000 – Feb 2026.
Starting Capital:
$20,000.
Position Sizing:
ATR-based.
Stops:
Time based stop-loss.
Spread:
12 p
Backtest Setup 2 (Euro Stoxx 50)
Instrument:
Euro Stocks50 2€ (Futures).
Timeframe:
Daily bars.
Period Tested:
Jan 2000 – Feb 2026.
Starting Capital:
$20,000.
Position Sizing:
ATR-based.
Stops:
Time based stop-loss.
Spread:
4 p
Backtest Setup 3 (TLT)
Instrument:
TLT (ETF).
Timeframe:
Dailybars.
Period Tested:
Aug 2007 – Feb 2026 (Earliest available data on ProRealTime).
Starting Capital:
$20,000.
Position Sizing:
ATR-based.
Stops:
Time based stop-loss.
Spread:
2 p
Results & Metrics
The CAGR figures here look modest, and in isolation, they are.
But that’s not the right way to read them.
This is not a standalone growth strategy. It’s a
hedging tool
. It’s designed to make money during the same periods that are destroying your long portfolio: bear markets, risk-off selloffs, prolonged downtrends. The years this strategy profits are the years everything else bleeds.
The bulk of the profits come from periods like 2001–2002, 2008 and 2022. During the bull market years in between, the system is largely idle. That’s intentional.
The real value isn’t the CAGR in isolation. It’s what this strategy does to your
overall portfolio drawdown
when you run it alongside long strategies.
Judge this one by how it behaves in the bad years, not the good ones.
Instrument:
DAX40 (Futures)
CAGR:
+1.18% (
2001:
+8.8%,
2008:
+13.25%,
2022:
+17.18%)
Max Drawdown:
-16.68%
Win Rate:
60%
Profit Factor:
1.32
Avg Gain Per Trade:
76.50€
Instrument:
Euro Stoxx 50 (Futures)
CAGR:
+1.41% (
2001:
+17.20%,
2008:
+7.04%,
2011:
+11.73%,
2022:
+11.77%)
Max Drawdown:
-12.56%
Win Rate:
59%
Profit Factor:
1.48
Avg Gain Per Trade:
85.94€
Instrument:
TLT (iShares 20+ Year Treasury Bond ETF)
CAGR:
+0.76% (
2009:
+5.43% while TLT was down ~23%, TLT fell roughly ~36% between 2021 and 2023. The strategy was short. It returned +14.69%.
Max Drawdown:
-12.83%
Win Rate:
60%
Profit Factor:
1.21
Avg Gain Per Trade:
42.89$
Now, you can try to reverse-engineer this system on your own… or you can fast-track your learning, support my work, and access the full code + detailed walkthrough by becoming a paid member.
Full Code & Detailed Walk-Through
Below is the complete PRT code but also a description of all the parameters for easy translation to any chosen platform (Easylanguage, MT5, Python or Ninjatrader).
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
