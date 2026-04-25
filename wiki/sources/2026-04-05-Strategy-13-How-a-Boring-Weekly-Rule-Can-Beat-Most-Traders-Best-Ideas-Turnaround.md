# Strategy #13: How a “Boring” Weekly Rule Can Beat Most Traders’ Best Ideas (Turnaround Tuesday)

**Source**: [[2026-04-05-Strategy-#13:-How-a-“Boring”-Weekly-Rule-Can-Beat-Most-Traders’-Best-Ideas-(Turnaround-Tuesday)]] | [Algomatic Trading](https://algomatictrading.substack.com/p/strategy-13-how-a-boring-weekly-rule)
**Date**: 2026-04-05
**Tags**: #article #substack #strategy #seasonality

## One-Sentence Summary

> Strategy #13: How a “Boring” Weekly Rule Can Beat Most Traders’ Best Ideas (Turnaround Tuesday)
A minimalist, rules-based system that targets a repeatable midweek rebound while keeping risk controlled...

## Key Insights

1. **原文来源**: [Algomatic Trading](https://algomatictrading.substack.com/p/strategy-13-how-a-boring-weekly-rule)

## Full Content

Strategy #13: How a “Boring” Weekly Rule Can Beat Most Traders’ Best Ideas (Turnaround Tuesday)
A minimalist, rules-based system that targets a repeatable midweek rebound while keeping risk controlled.
Algomatic Trading
Jan 11, 2026
∙ Paid
28
5
Share
Many successful systematic traders didn’t get there by trading more.
They got there by trading better, at the right time, with the right structure.
This strategy is built around a simple observation: markets love to create sharp early-week narratives, then quietly mean-revert once the emotional fuel burns out.
This strategy shows up at the same time on Mondays, takes the same measured position, and lets the snap-back do its thing.
The core idea here is that after some Monday sell-offs the buying pressure usually creates a rebound from those oversold levels after the weekend.
The Problem
Your real opponent isn’t volatility, it’s your reaction to volatility.
Late Monday, the market has already done its damage.
The news has landed.
Overreactions have played out.
And most discretionary traders are either:
Revenge trading their losses
Paralyzed waiting for “confirmation”.
Where traders fail:
Overtrading
after big moves, confusing motion with opportunity
Chasing confirmation
, entering late when edge decays
Sizing wrong
, taking the same position on calm days and chaos days
Holding too long
, turning a short-term edge into a long-term prayer
Without structure, you’re grinding. Overtrading. Paying spread. Absorbing drawdowns that have nothing to do with bad analysis, just bad timing and inconsistent risk.
This system removes all of it in a very simple way, it is actually one of my simplest strategies and probably one of the most robust ones as well.
Join 6,800+ traders learning systematic trading and get new strategies & research every month.
Subscribe
Strategy Overview
Here’s the basic settings for my backtests (Full Code is in the end of the post):
Market:
Nasdaq100, DAX40 and FTSE100 (CFD).
Timeframe:
1-hour bars.
Test Period:
From April 26th 2006, to January 9th, 2026 (20 years of market data, covering diverse market cycles including bull runs, bear markets, and periods of volatility). April 2006 was the earliest I could backtest with 1-hour bars on PRT.
Starting Capital:
Illustratively, a nominal starting capital of $20,000 for calculation purposes.
Position Sizing:
ATR-based.
Spread:
2p on all indices (2p spread in early 2000s is a lot more than 2p today but this is included anyway)
Backtest Setup 1 (Nasdaq)
Instrument:
Nasdaq100 1€ (CFD).
Timeframe:
1-hour bars.
Period Tested:
April 2006 – Jan 2026 (with out-of-sample 2021-now).
Starting Capital:
$20,000.
Position Sizing:
ATR-based.
Stops:
Fixed % stop-loss.
Spread:
2 p
Backtest Setup 2 (DAX)
Instrument:
DAX40 1€ (CFD).
Timeframe:
1-hour bars.
Period Tested:
April 2006 – Jan 2026 (with out-of-sample 2021-now).
Starting Capital:
$20,000.
Position Sizing:
ATR-based.
Stops:
Fixed % stop-loss.
Spread:
2 p
Backtest Setup 3 (FTSE)
Instrument:
FTSE100 1€ (CFD).
Timeframe:
1-hour bars.
Period Tested:
April 2006 – Jan 2026 (with out-of-sample 2021-now).
Starting Capital:
$20,000.
Position Sizing:
ATR-based.
Stops:
Fixed % stop-loss.
Spread:
2 p
Results & Metrics
Average backtesting results on three different stock indices:
CAGR:
+4.68%-5.76%
Max Drawdown:
-5.61%-17.42%
Win Rate:
58%-60%
MAR Ratio:
0.26-0.90
Profit Factor:
1.43-1.63
Avg Gain Per Trade:
99€-119€
Why the low time-in-market matters:
This strategy is active less than 12% of the time, making it
extremely compatible with other systems
. You can stack this with momentum strategies, volatility plays, or trend-following approaches without capital conflicts.
Stack 5-8 systems like this with different market conditions and timeframes, and you're building a 20-30% CAGR portfolio with manageable drawdowns.
Compare this to buy-and-hold, which keeps you exposed 100% of the time with drawdowns often exceeding 30-40% during bear markets. This system delivers decent annual returns while your capital sits idle 88% of the time, available for other opportunities and great portfolio combinations.
Track This Strategy’s Real Performance
Want to see how this strategy (and all my others) are actually performing?
I’ve built a public tracker that shows the real returns of every strategy I’ve published.
👉
View the strategy tracker here
What you’ll see:
Year-to-date returns for all 10+ strategies
Total returns since published
Maximum drawdown per strategy
Win rates & MAR ratios
Live vs. paper trading status
Real numbers with correct spreads and commissions
No cherry-picking. No hiding the strategies that didn’t work. Updated monthly.
Why This Works
Market mechanics:
Early-week moves carry positioning pressure from weekend headlines, macro repricing and portfolio rebalancing.
When price gets pushed into uncomfortable zones early in the week:
Late sellers appear (scared, not strategic)
Reversion buyers surface once the worst-case narrative stops accelerating
The psychology:
The entry f

---

*Imported from Substack on 2026-04-25*
