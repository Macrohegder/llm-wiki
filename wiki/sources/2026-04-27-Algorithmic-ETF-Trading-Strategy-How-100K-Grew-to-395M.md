---
title: "Algorithmic ETF Trading Strategy: How $100K Grew to $3.95M"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/tqqq-gold-leveraged-etf-strategy-backtest"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# Algorithmic ETF Trading Strategy: How $100K Grew to $3.95M

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/tqqq-gold-leveraged-etf-strategy-backtest)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

Algorithmic ETF Trading Strategy: How $100K Grew to $3.95M
What happens when you replace Treasury bonds with gold in a leveraged TQQQ & GOLD ETF strategy? Full strategy rules step-by-step adn RealTest code.
SetupAlpha
Oct 12, 2025
∙ Paid
23
2
2
Share
Hey!
Do you remember the
strategy
we made last week? Today, we’re going to build a similar one. Is it better? Let’s find out!
After I published the TQQQ/TMF strategy article, I kept thinking about
Glenn’s paper
.
He mentioned that TQQQ should be paired with an uncorrelated asset. TMF worked because of the negative correlation. But what if there’s something better?
Gold came to mind.
TQQQ = Blue | GOLD = Green
It has low correlation with tech stocks, but for different reasons than bonds. It’s not about flight to safety. It’s about inflation hed...

---

## 原文

Algorithmic ETF Trading Strategy: How $100K Grew to $3.95M
What happens when you replace Treasury bonds with gold in a leveraged TQQQ & GOLD ETF strategy? Full strategy rules step-by-step adn RealTest code.
SetupAlpha
Oct 12, 2025
∙ Paid
23
2
2
Share
Hey!
Do you remember the
strategy
we made last week? Today, we’re going to build a similar one. Is it better? Let’s find out!
After I published the TQQQ/TMF strategy article, I kept thinking about
Glenn’s paper
.
He mentioned that TQQQ should be paired with an uncorrelated asset. TMF worked because of the negative correlation. But what if there’s something better?
Gold came to mind.
TQQQ = Blue | GOLD = Green
It has low correlation with tech stocks, but for different reasons than bonds. It’s not about flight to safety. It’s about inflation hedging and currency debasement.
So I tested it, almost same rules, same rebalancing. Just swap TMF for UGL (3x gold).
That’s better than the TQQQ/TMF version.
Let me walk through what changed, why it worked, and what broke differently. And what makes it even better?
Why Gold Instead of Bonds?
Problem with bonds as a hedge.
Bonds work when central banks cut rates or when there’s a deflationary panic. They fail when rates rise or inflation accelerates. That’s what happened in 2022.
TMF dropped over 70% from its peak as the Fed raised rates from 0% to 5.5%. If you were holding TQQQ/TMF during that period, your bond hedge wasn’t hedging.
Gold behaves differently. It doesn’t move based on interest rate expectations alone. It responds to:
Real rates (nominal rates minus inflation)
Currency debasement fears
Geopolitical risk
Central bank policy mistakes
Inflation expectations
Gold and tech stocks have low correlation, but it’s not negative correlation like bonds. Gold doesn’t spike every time tech crashes. Instead, it provides diversification through a different risk factor.
When I tested TQQQ with UGL instead of TMF, I wanted to see if this structural difference created a more stable portfolio.
The Setup: Same Strategy, Different Asset
The strategy is identical to the TQQQ/TMF version:
Position Sizing:
50% TQQQ (3x Nasdaq)
50% UGL (3x gold)
Rebalancing:
Every 2 months on the last trading day
Sell winners, buy losers, return to 50/50
Crash Filter:
If TQQQ drops 20% in a single day, exit to IEF (7-10 year Treasury ETF)
Stay in IEF until TQQQ recovers above its pre-crash price
Return to 50/50 TQQQ/UGL
The code structure is the same. The only change is replacing TMF with UGL. That’s it.
My Backtest Results
Are you using RealTest as well?
Take a look at these strategies
I tested this in RealTest using Norgate daily data from January 4, 2010 to October 3, 2025.
Test Parameters:
Starting capital: $100,000
Slippage: 0.25% per trade
Rebalancing: Every 2 months
Crash filter: 20% single-day drop in TQQQ
Benchmark: SPY buy-and-hold
Results:
$100k to $1.85 million.
But, later you can see how I made this up to
$3.95 million
, like the equity below.
Sharpe ratio 1.05…
Before we dive in, let’s talk about this strategy concept.
How It Performed in Different Regimes
COVID Crash (March 2020):
TQQQ dropped over 60%. UGL rallied as investors fled to safe havens. The crash filter kicked in and moved everything to IEF. The strategy avoided the worst of the crash, just like the TQQQ/TMF version.
2020-2021 Tech Rally:
TQQQ exploded higher. UGL consolidated but didn’t collapse. The rebalancing forced me to sell TQQQ and buy UGL every 2 months. This locked in tech gains and accumulated gold at stable prices.
2022 Rate Hikes:
This is where the strategies diverged. TMF got destroyed in 2022. UGL held up better. Gold dropped from $2,000 to $1,600, about 20%. Not bad compared to a 70% collapse like TMF.
The TQQQ/UGL strategy handled 2022 better than TQQQ/TMF. The drawdown was smaller. The recovery was faster.
2023-2025 AI Rally:
TQQQ went parabolic. UGL trended higher as central banks accumulated gold and inflation fears persisted. The rebalancing kept selling TQQQ into strength and buying UGL. This smoothed returns and reduced volatility.
What Makes This Version Better
A few things stood out:
1. Gold doesn’t break in rising rate environments
Bonds collapse when rates rise. Gold doesn’t. Gold can rally during rising rates if real rates stay low or inflation expectations are high. This creates a more stable hedge.
2. Smoother rebalancing
Gold trends gradually. Bonds spike violently. Gradual trends create better rebalancing opportunities. You’re not trying to catch violent spikes. You’re capturing slow divergences.
3. Lower maximum drawdown
TQQQ/UGL had a 25% max drawdown. TQQQ/TMF had 28.4%. Not a huge difference, but consistent across multiple drawdown periods. Gold cushioned losses better.
4. Higher profit factor
The 11.07 profit factor is exceptional for a rebalancing strategy. It means the mean reversion between TQQQ and UGL is stronger and more consistent than between TQQQ and TMF.
5. Better Sharpe and Sortino ratios
Sharpe of 0.96 vs 0.87. Sortino of 1.68 vs 1.49. Both indicate better risk-adjusted returns with gold.
Where This Strategy Still Struggles
Yes, it’s not perfect, I found some issues.
1. Gold can lag for years
Gold had a brutal decade from 2011 to 2020. It went nowhere. If you’re holding 50% UGL during a gold bear market, that portion drags on performance. TQQQ has to carry the entire strategy.
2. Leverage decay still exists
UGL suffers from beta slippage just like TMF. In choppy markets with no clear trend, 3x leverage eats returns. The rebalancing helps, but it can’t eliminate decay entirely.
3. Correlation isn’t negative
Gold and TQQQ have low correlation, not negative correlation. They can both fall together during liquidity crises (March 2020, early crash period). The crash filter helps, but there’s still tail risk.
4. Smaller accounts face friction
If you’re trading with $10k, the rebalancing costs add up. You need at least $50k-$100k for this to be efficient. Smaller accounts should consider using 1x or 2x leveraged versions (QQQ + GLD).
5. ETF structure risk
TQQQ and UGL are swap-based ETFs. If regulations change or the issuer faces issues, the ETFs could be restructured. This is low probability but worth knowing.
Why the Low Correlation Works
Gold and tech stocks are driven by different factors:
TQQQ (Tech Stocks) Driven By:
Earnings growth
Innovation cycles
Risk appetite
Growth expectations
Tech sector sentiment
UGL (Gold) Driven By:
Real interest rates
Inflation expectations
Currency debasement
Central bank policy
Geopolitical risk
These factors don’t move together. When tech crashes because growth expectations collapse, gold might rally because inflation fears spike. When tech rallies because of AI hype, gold might consolidate because real rates stabilize.
The low correlation creates diversification. The rebalancing forces you to sell what’s working and buy what’s lagging. This is mechanically sound.
I’m not saying gold is a perfect hedge. I’m saying it’s a different hedge. And in this test, it performed better than bonds.
RealTest code + Rules (Step-By-Step):
▼ Import:
	DataSource: 	Norgate
	IncludeList: 	TQQQ
	IncludeList: 	UGL
	IncludeList: 	IEF
	IncludeList: 	SPY
	StartDate: 	Earliest
	EndDate: 	Latest
	SaveAs: 	          tqqq_ugl_ief_daily.rtd

▼ Settings:
	DataFile: 	tqqq_ugl_ief_daily.rtd
	StartDate: 	1/1/2010
	EndDate: 	Latest
	BarSize: 	Daily
	AccountSize: 	100000

▼ Parameters:
	k_months: 	2

➤ Data:{...}

➤ Strategy:{...}
The full strategy implementation rules and RealTest code are available to paid subscribers below.
We put a ton of time, effort, and care into each article to bring you real strategies and alpha. Consider supporting our work by becoming a paid subscriber.
Subscribe
About us:
We help You to build strong trading strategies/portfolios. Our strategies are crafted from academic research, live-tested, and ready to run without wasting years coding and research.
Our trading startegies.
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
