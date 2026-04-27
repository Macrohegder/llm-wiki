---
title: "The Hidden FX Trade Every Non-U.S. Stock Investor Is Making"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/the-hidden-fx-trade-every-non-us"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# The Hidden FX Trade Every Non-U.S. Stock Investor Is Making

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/the-hidden-fx-trade-every-non-us)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

The Hidden FX Trade Every Non-U.S. Stock Investor Is Making
Hedging Currency Risk When You Trade Only U.S. Stocks
SetupAlpha
Sep 07, 2025
3
1
Share
If you’re based outside the U.S. (EUR, GBP, AUD, etc.) and trade only U.S. stocks, you have an invisible second trade running all the time.
Even if your broker shows PnL in dollars, the moment you convert back to your home currency (or just measure your returns in it), FX shifts can change your real return. For example:
Your stock is up 12% in USD.
USD drops 5% vs. your currency.
Your actual return in local money ≈ 6.9%, not 12%.
Quick intro
SetupAlpha develops algorithmic trading strategies based on academic and proprietary research. We provide fully coded RealTest strategies, tested, transparent, and ready for real-world results (with code th...

---

## 原文

The Hidden FX Trade Every Non-U.S. Stock Investor Is Making
Hedging Currency Risk When You Trade Only U.S. Stocks
SetupAlpha
Sep 07, 2025
3
1
Share
If you’re based outside the U.S. (EUR, GBP, AUD, etc.) and trade only U.S. stocks, you have an invisible second trade running all the time.
Even if your broker shows PnL in dollars, the moment you convert back to your home currency (or just measure your returns in it), FX shifts can change your real return. For example:
Your stock is up 12% in USD.
USD drops 5% vs. your currency.
Your actual return in local money ≈ 6.9%, not 12%.
Quick intro
SetupAlpha develops algorithmic trading strategies based on academic and proprietary research. We provide fully coded RealTest strategies, tested, transparent, and ready for real-world results (with code that Python etc users can adapt). Explore our full library here:
https://setupalpha.com/
1. Hold a Parallel Currency Hedge (50/50 USD & EUR with Margin)
One efficient way to hedge USD exposure, without constant FX conversions is to
keep 50% of your capital in USD and 50% in EUR
, and use
margin
to bridge the gap when trading U.S. stocks.
How it works in practice:
Keep half your cash in EUR (your home currency) and half in USD.
Trade your U.S. stocks using
margin
from your broker.
If you need more USD buying power, the broker effectively
lends
you USD against your EUR collateral.
Margin interest rates are often lower than the hidden costs of frequent FX conversions.
Because you still hold a large EUR balance, you avoid most “margin call” issues, your EUR is collateral, and your account stays healthy.
If the dollar drops, the EUR side of your account gains value in USD terms,
offsetting the currency loss
on your U.S. stock positions.
Advantages:
No constant FX conversions (avoids repeated FX fees).
Maintains a built-in currency hedge, part of your net worth is always in EUR.
Smooths out account swings caused by USD weakness.
Disadvantages:
You’re hedged, but you might miss upside if USD rises sharply.
Complexity in accounting.
Let’s backtest this:
Green line = Dollar 50% allocation
Red line = EUR 50% allocation
Blue = portfolio value (looks stable)
Yellow = hold only in dollar
Now let’s test and hold money only in EUR if dollar is closing below it’s 200 day sma.
Share
But now let’s test this: if the DXY is above the 200-day SMA, then we use 100% USD. If the DXY is below the 200-day SMA, then we use 50% USD and 50% EUR.
But what if we make same test like the last one but instead of using eur we now use bitcoin.
That’s amazing, in 2017–2018 it made 360%, which is insane. And if you stack that strategy with others, the compounding effect is massive. But that happened during the period when Bitcoin made its best moves. As time goes on, Bitcoin moves less, so we’ll probably never see gains like that again.
This is How An Algorithmic Crypto Strategy Made +3,332% With RealTest
SetupAlpha
·
September 3, 2025
Read full story
Here are some ChatGPT ideas on this hedging style too:
Extra diversification idea:
Instead of only hedging, consider allocating a portion of your portfolio to
non-U.S. stocks
directly, e.g., Australia (ASX) or Europe (STOXX, DAX, CAC).
Pros
: Direct exposure to local currency + local market cycles.
Cons
: Different market hours, liquidity variations, and sometimes higher trading costs.
Use Currency-Hedged ETFs for U.S. Equity Exposure
Instead of buying U.S. stocks directly, you could hold a
currency-hedged ETF
listed in your local market.
Example: In Europe,
IE00B3XXRP09
(iShares MSCI USA Hedged) gives U.S. equity exposure while neutralizing USD swings.
Pro
: Simple “set and forget” approach.
Con
: Less control over specific stocks; usually only available for broad index exposure.
Futures, Forwards, and Options
These offer precise control:
Futures
: Standardized, exchange-based contracts.
Forwards
: Customizable OTC trades tailored to your hedging timeline.
Options
: Provide asymmetric protection, useful if you want downside buffer while allowing upside.
Share
Few ideas from the outside too
What Institutions Do When the Dollar Drops
Lessons from Bank for International Research
Link -
https://www.bis.org/publ/bisbull105.pdf
The Bank for International Settlements recently dug into April–May 2025, when the dollar slid sharply. The surprising takeaway?
It wasn’t a mass exodus from U.S. assets, it was
hedging
.
Non-U.S. investors, sitting on trillions in dollar-denominated stocks and bonds, saw the greenback falling and rushed to protect their local-currency returns.
They didn’t sell the assets. Instead, they:
Added FX swaps and forwards
, selling USD forward to lock in local-currency value.
Increased hedge ratios “ex-post”
, boosting the portion of their portfolio protected against further dollar declines.
Concentrated activity in Asia
, BIS data showed the biggest USD moves happened during Asian trading hours, likely from Japanese, Taiwanese, and other regional institutions.
Two practical takeaways for smaller traders:
You can keep your U.S. positions
and still hedge the currency, ETFs, futures, or even your 50/50 margin method mimic what big players do.
Timing matters
, institutional hedges often come after a USD move has started, which can add momentum to the trend.
In short: big money doesn’t just ride the dollar up and down, they manage the FX side actively, and that’s a tool we can borrow.
This is exactly the type of work we do every day at
SetupAlpha
. Our mission is simple: give RealTest users robust strategies they can trust, without wasted time or curve-fit illusions. If you’re ready to add proven systems to your portfolio, you’ll find them here:
https://setupalpha.com/collections/realtest-strategies-and-backtests
Subscribe for more Alpha!
Subscribe
Read more:
This is How An Algorithmic Crypto Strategy Made +3,332% With RealTest
SetupAlpha
·
September 3, 2025
Read full story
We Tried Mean Reversion on Gold — And Didn’t Expect This (+32.7% this year)
SetupAlpha
·
August 13, 2025
Read full story
3
1
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
