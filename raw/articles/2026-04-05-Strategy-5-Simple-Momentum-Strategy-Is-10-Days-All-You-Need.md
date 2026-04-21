# Strategy #5: Simple Momentum Strategy (Is 10 Days All You Need?)

**原文链接**: https://algomatictrading.substack.com/p/strategy-5-simple-momentum-strategy

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:20:55

---

## 摘要

Strategy #5: Simple Momentum Strategy (Is 10 Days All You Need?)
Discover how a shockingly simple 10-day momentum performs on the Nasdaq 100
Algomatic Trading
Jun 19, 2025
24
5
2
Share
Is the market’s complexity holding you back?
Are you searching for a way to capture Nasdaq upside without living through its worst crashes?
What if the answer were as simple as looking back just ten trading days?
In this post, I will share a momentum-based strategy that uses a single 10-day look-back to decide when to hop in and an equally simple rule for hopping out.
I’ll explain exactly how the 10-day momentum signal works and share a full, ready-to-run strategy code so you can test it yourself.
Subscribe for free and get a new, backtested strategy in your inbox every month!
Subscribe
The Problem…
Most tra...

---

## 全文

Strategy #5: Simple Momentum Strategy (Is 10 Days All You Need?)
Discover how a shockingly simple 10-day momentum performs on the Nasdaq 100
Algomatic Trading
Jun 19, 2025
24
5
2
Share
Is the market’s complexity holding you back?
Are you searching for a way to capture Nasdaq upside without living through its worst crashes?
What if the answer were as simple as looking back just ten trading days?
In this post, I will share a momentum-based strategy that uses a single 10-day look-back to decide when to hop in and an equally simple rule for hopping out.
I’ll explain exactly how the 10-day momentum signal works and share a full, ready-to-run strategy code so you can test it yourself.
Subscribe for free and get a new, backtested strategy in your inbox every month!
Subscribe
The Problem…
Most traders assume “sophisticated market” means “sophisticated system.”
That often leads to:
Over-fitting
– strategies that memorize past noise and implode live.
Analysis paralysis
– dozens of indicators, zero clarity.
Ignoring drawdowns
– focusing on shiny CAGR while forgetting a 50 % loss needs a 100 % gain just to break even.
The Nasdaq 100 (or its ETF proxy, QQQ) illustrates the dilemma: spectacular upside but with deep crashes.
Strategy Overview
This approach lives on two lines of code:
Entry:
Go long when
10-day Momentum
crosses
above 0
.
Exit:
Close the position when
today’s close exceeds the high X days ago
.
What is the momentum indicator?
It’s very simple, it’s already integrated in ProRealTime but this is how it works:
Momentum[N] = Close − Close[N]
That’s it, no moving averages, no filters, no overfitting.
There are a lot of room for improvements here so feel free to build on this strategy.
Why It Works
Capturing Momentum
Short-term strength in Nasdaq often persists; a 10-day window is long enough to dodge noise, short enough to respond quickly.
Low Parameter Count = Low Curve-Fit Risk
One look-back period and one exit rule leave little room for accidental overfitting.
Backtest Setup
Instrument:
Nasdaq 100 CFD (IG)
Time Frame:
Daily
Data Window:
3 Jan 2005 – 19 Jun 2025
Capital:
$20 000
Spread:
2 pts
Platform:
ProRealTime 12 (CET)
Size:
Dynamic Position Sizing (Volatility Based)
Here are the results:
CAGR:
6.67 %
Max Drawdown:
–21.7 %
MAR Ratio:
≈ 0.3
Total Trades:
240
(Exact figures vary slightly with data source, but the edge is consistent.)
ProRealTime Code
Here's the ProRealTime code with added ATR based dynamic sizing:
//----------------------------------------------------------------------
// Concept:   Momentum
// Market:    US Tech 100 / Nasdaq
// Direction: Long only
// Timeframe: Daily
// Timezone:  CET
// Versions:  v.1 | By: Algomatictrading.com | 2024-05-20 | OOS since: 2022-05-01
//----------------------------------------------------------------------

defparam preloadbars = 5000
defparam cumulateorders = false


// POSITION MANAGEMENT
//---------------------------------------------------------------------
// ATR calculation period


atr = Averagetruerange[5]

//Dynamic Position Sizing
// User Inputs
riskPercent = 4        // Risk percentage for position sizing
portfolioSize = 20000     // Default portfolio size

contractsToTrade = 1       // Number of contracts to trade

// Position Sizing Calculation
portfolioEquity = Max(PortfolioEquity, portfolioSize) // Use real equity or default portfolio size
contractsToTrade = (riskPercent / 100) * portfolioEquity / (atr * PointValue)

// INDICATORS
//---------------------------------------------------------------------
m = momentum[10]
r = rsi[2]


// TRADING CONDITIONS
//---------------------------------------------------------------------
// Long - Enter
// ------------------
cl = m crosses over 0
cl = cl and  r < 90


// Long - Exit
// ------------------
clx = close > high[5] //5-7 is the most robust parameter


// TRADING ACTION
//---------------------------------------------------------------------
// Enter
// ------------------
if cl then
buy contractsToTrade contract at market
endif


// Exit
// ------------------
if longonmarket and clx then
sell at market
endif
Disclaimer:
I am not a financial advisor. This article is for informational and educational purposes only. Trading involves risk, and you can lose money. Always do your own research.
24
5
2
Share

---

*由 Substack Strategy Tracker 自动抓取*
