---
title: "3x Leveraged ETF Strategy: 1,481% Return With 28% Drawdown (Trading Strategy Rules)"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/leveraged-etf-strategy-tqqq-tmf-rebalancing-backtest"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# 3x Leveraged ETF Strategy: 1,481% Return With 28% Drawdown (Trading Strategy Rules)

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/leveraged-etf-strategy-tqqq-tmf-rebalancing-backtest)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

3x Leveraged ETF Strategy: 1,481% Return With 28% Drawdown (Trading Strategy Rules)
How a simple 50/50 rebalancing system turned leveraged ETF risk into steady performance, tested across 15+ years. Rules Step-by-Step. (SSRN Paper)
SetupAlpha
Oct 05, 2025
∙ Paid
24
5
Share
Hey Followers & Subscribers!
A friendly substack user asked me to test a strategy from an academic paper
(SSRN Paper link below)
about holding 3x leveraged ETFs long-term. I was a little bit skeptical because everyone knows you don’t hold leveraged ETFs overnight, let alone for years.
But the idea was interesting. Take TQQQ (3x Nasdaq) and TMF (3x Treasury bonds), split them 50/50, and rebalance every two months. Add a simple crash filter. That’s it.
So I backtested and ran it from 2010 through October 2025.
The results: ...

---

## 原文

3x Leveraged ETF Strategy: 1,481% Return With 28% Drawdown (Trading Strategy Rules)
How a simple 50/50 rebalancing system turned leveraged ETF risk into steady performance, tested across 15+ years. Rules Step-by-Step. (SSRN Paper)
SetupAlpha
Oct 05, 2025
∙ Paid
24
5
Share
Hey Followers & Subscribers!
A friendly substack user asked me to test a strategy from an academic paper
(SSRN Paper link below)
about holding 3x leveraged ETFs long-term. I was a little bit skeptical because everyone knows you don’t hold leveraged ETFs overnight, let alone for years.
But the idea was interesting. Take TQQQ (3x Nasdaq) and TMF (3x Treasury bonds), split them 50/50, and rebalance every two months. Add a simple crash filter. That’s it.
So I backtested and ran it from 2010 through October 2025.
The results: $100,000 turned into $1.5 million. CAGR of 20%. Maximum drawdown of 28.4%.
Let me walk through what I found, how it works, and where it breaks.
But first…
Why Leveraged ETFs Usually Fail
Here’s the problem with holding leveraged ETFs long-term.
Say an asset goes up 25% one day, then down 20% the next. The underlying ends at breakeven: (1 + 0.25) × (1 - 0.20) = 1.0.
But a 3x leveraged ETF goes up 75% the first day, then down 60% the second: (1 + 0.75) × (1 - 0.60) = 0.70. You lose 30% while the underlying is flat.
This is called beta slippage. It happens because the fund rebalances daily to maintain 3x exposure. In choppy markets with no clear trend, this eats returns.
https://seekingalpha.com/article/4134608-do-investors-need-to-worry-about-beta-slippage-in-leveraged-funds
But what if you pair it with something that moves in the opposite direction? When tech crashes, bonds rally. When tech rallies, bonds fall. Maybe the negative correlation could offset some of the decay.
That’s the idea behind this strategy.
The Academic Foundation
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3722318
This comes from a 2020 research paper by Dr. Lewis A. Glenn: “Long-Term Investing in Triple Leveraged Exchange Traded Funds” (SSRN).
Glenn tested a simple idea: combine TQQQ (3x Nasdaq) with TMF (3x 20+ year Treasury bonds) in equal weight and rebalance regularly.
His results were striking. The 50/50 portfolio delivered strong returns with much lower drawdowns than holding TQQQ alone. The negative correlation between tech and bonds created a natural hedge.
Glenn also added a “black swan filter” a rule to exit to cash when TQQQ drops more than 20% in a single day. This reduced extreme drawdowns during crashes.
I wanted to see if this held up through 2025, including the 2022 rate spike that crushed long-duration bonds. So I built it in RealTest and tested it.
How the Strategy Works
The strategy has three parts. Start with 50% TQQQ, 50% TMF. Equal dollar allocation to each. Rebalance every 2 months.
On the last trading day of every second month, check your allocation. If TQQQ has grown to 60%, sell some and buy TMF to get back to 50/50. If TMF is 55%, sell some and buy TQQQ.
This forces you to sell winners and buy losers. It’s mechanical and removes emotion.
Crash filter. If TQQQ drops 20% or more in a single day, exit both TQQQ and TMF. Move 100% into IEF (a 7-10 year Treasury ETF). Stay there until TQQQ recovers and exceeds its pre-crash price. Then return to the 50/50 split.
My Backtest Results
I tested this in RealTest using Norgate daily data from January 4, 2010 to October 3, 2025.
Test parameters:
Starting capital: $100,000
Slippage: 0.25% per trade
Rebalancing: Every 2 months
Crash filter: 20% single-day drop in TQQQ
Benchmark: SPY buy-and-hold
Results:
Net Profit:
$1,481,916
ROR:
19.58%
Maximum Drawdown:
-28.48%
MAR Ratio:
0.69
Total Trades:
167
Win Rate:
76.05%
Profit Factor:
2.71
Sharpe Ratio:
0.87
Sortino Ratio:
1.42
Volatility:
23.75%
These are my actual backtest numbers. Not Glenn’s original results.
Turning $100k into $1.4 million in 15 years is solid. The 20% CAGR is more than double SPY. The 28.4% max drawdown is manageable compared to TQQQ’s 69+% drawdown.
The 76% win rate on rebalancing trades tells me the negative correlation works. You’re systematically buying low and selling high between two assets that move in opposite directions.
The profit factor of 2.71 means for every dollar lost, you make $2.71 on winners.
A few things stood out:
Please take 1 minute to answer this quick
SURVEY
(3 questions) it’ll help me produce exactly the kind of strategies and research that move you closer to your trading goals.
Start Survey
During COVID (March 2020):
TQQQ dropped. TMF spiked as investors fled to bonds. The crash filter kicked in and moved everything to IEF. The strategy avoided the worst of the crash.
During 2022 rate hikes:
TMF crash. Long bonds collapsed as rates rose. But TQQQ held up better. The rebalancing forced me to sell TQQQ (winner) and buy TMF (loser). When bonds stabilized, that positioning paid off.
The strategy isn’t my favourite, but the rebalancing mechanic does what it’s supposed to: exploit mean reversion between negatively correlated assets.
What Makes It Work
A few things make this strategy different from typical backtests:
It’s simple.
Two ETFs. One rule. No curve fitting. Simple strategies tend to be more robust.
It’s based on a structural relationship.
Tech stocks and long-term bonds are negatively correlated because of how capital flows. When investors panic, they sell stocks and buy bonds. When they’re optimistic, they sell bonds and buy stocks. This isn’t a statistical accident it’s a behavioral pattern.
It covers multiple market regimes.
The test period includes the 2010-2011 recovery, 2015-2016 volatility, 2018 correction, COVID crash, 2022 rate hikes, and the recent AI rally. Different conditions, different outcomes, but the strategy adapted.
It forces discipline.
Rebalancing makes you buy what’s down and sell what’s up. It’s emotionally hard but mathematically sound.
Academic validation.
Glenn’s research showed similar results. That gives me confidence this isn’t just an artifact of my data.
Where It Struggles
It doesnt work in all conditions. I found some issues…
1. Rising rate environments
TMF has been weak since 2022. When rates rise, long-duration bonds get crashed. If rates keep rising while tech crashes, both TQQQ and TMF could fall together. The negative correlation breaks down in stagflation (high inflation + slow growth).
2. Leverage decay in choppy markets
If we get a multi-year sideways market with high volatility, both TQQQ and TMF will suffer from beta slippage. The rebalancing helps, but it can’t fully offset the decay.
3. Gap risk
The crash filter only triggers on daily closes. If TQQQ drops 30% intraday but recovers to close down 18%, the filter won’t kick in. You’re exposed to intraday moves.
4. Smaller accounts
If you’re trading with $10k, the slippage and rebalancing costs add up. You need at least $50k-$100k for this to be efficient.
5. ETF structure risk
TQQQ and TMF are swap-based ETFs. If the issuer faces issues or regulations change, the ETFs could be restructured or liquidated.
RealTest code + Rules (Step-By-Step):
▼ Import:
	DataSource: 	Norgate
	IncludeList: 	TQQQ
	IncludeList: 	TMF
	IncludeList: 	IEF
	IncludeList: 	SPY
	StartDate: 	Earliest
	EndDate: 	Latest
	SaveAs: 	          tqqq_tmf_ief_daily.rtd

▼ Settings:
	DataFile: 	tqqq_tmf_ief_daily.rtd
	StartDate: 	1/1/2010
	EndDate: 	Latest
	BarSize: 	Daily
	AccountSize: 	100000

▼ Parameters:
	k_months: 	2

➤ Data:{...}
The full strategy implementation rules (step-by-step) and RealTest code are available to paid subscribers below.
Subscribe
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
