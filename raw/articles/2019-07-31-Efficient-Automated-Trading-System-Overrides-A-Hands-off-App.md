---
title: "Efficient Automated Trading System Overrides: A Hands-off Approach"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/automated-trading-system-overrides/"
date: "2019-07-31"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Efficient Automated Trading System Overrides: A Hands-off Approach

**来源**: [QuantInsti](https://blog.quantinsti.com/automated-trading-system-overrides/)  
**日期**: 2019-07-31  
**作者**: QuantInsti

---

## 原文

Efficient Automated Trading System Overrides: A Hands-off Approach

ByZach OakesTrading has evolved greatly in the past decade that I’ve been active in the markets. With it there have been incredible advancements in how markets are traded, entries are found, and systems are implemented. Butwith great power comes great responsibility, and there are some tech hiccups one has to overcome/avoid in the process.To provide a little context - I say this with hesitancy - I’m a full-stack developer but prior to my focus in programming I was a discretionary futures trader, and before that, I was a market maker on the floor of what’s now the ICE.I have both high and low tech backgrounds, but roughly 95% of my trading is automated.

Going Live

I’ll begin with a story… recently I was launching a new portfolio, which for me means monitoring the system particularly closely for a few weeks and being ready to fix any errors. I noticed that unlike in the past, I found this task to be particularly difficult to manage in a hands-off type of way.I suppose I had expectations for this portfolio and had researched and tested it pretty heavily, so I knew what to expect and what I wanted to see from it, which naturally leads to agreed/fear hybrid of trading emotions.On the first day, I noticed a few mistakes in entries, but they were quickly resolved - all was working as it should have been, except I thought I knew better.With all the headline risk and the fed minutes coming out in the prior weeksI thought I should ‘confirm’ that my system wasn’t walking into any sentiment buzzsaws.Typically, I would consider this to be a more justified and responsible method of overriding a system, like tweaking or halting a system prior to an earnings announcement. I now havenew rulesfor what constitutes a ‘good’ override, and it’s not quite that simple.

Maybe I could do better?

I saw a trade that looked to be just a typical computer logic mistake; it was in Gold (GCQ19), and it was about to enter a solid short position after a large gap down had seemed to hit support. My days of discretionary were screaming at me to avoid this trade, but I decided:

If anything, I’ll simply exit it quickly if it moves against me.

In general, I don’t like to change trades, but I will occasionally exit earlier/cut losers if systems have a long holding period. This system has a holding period of <1hr, so I was completely lying to myself, either way, I looked at it here.The trade filled, and I was quickly down about $100/contract. I was looking for my exit, convinced I needed to override systems regularly as this couldn’t have been more clear. I waited for the system to (hopefully) find its way back to near even... a statement to generally be avoided in trading.The position clawed it's way back to -30, much closer to even than it had been (by now it had bounced around the stop at -350) and I closed it without a second thought. Within 10 minutes it had hit my trail stop floor of +250; it went on to close (in sim) around 370, I was kicking myself for my impatience.

… I can’t

We build these systems to trade better than ourselves, to avoid these heuristic mistakes and biases. However, if we’re overriding our work at every turn we negate the primary benefit ofauto trading- the elimination of human error.It’s essential to trust the systems you create. By allowing automation to handle decision-making, beginners can reduce emotional biases and focus on refining strategies for improved performance inautomated trading for beginners.I decidedthere really hasn’t been much research on the topic, and without opening the floodgates to a massive amount of data snooping or hindsight bias the only way to do this was Live, with money and opportunity on the line. I decided to dedicate (butcher) 10 trades over the course of a week for a small but fair miniature sample in how overriding systems effects my performance.I had one example, and I had 9 more to go - I’m aware the standard of statistically significant is >30 observation periods or >100 observations, but if I did this 100 times with the current aggregate the expected value of -34,000, I would have no business trading.

Results

Attached are my trades reported for the week, with my actual performance compared to the overridden results. It's no equity curve, simply a visualization of my results with and without my limited interference.As you can see, the interference was for the most part harmful to the account performance. When I think I know better, it seems in most cases I simply don’t; I am better off letting the systems I worked hard to develop run without interference or intervention.

Improve monitoring habits

If you need more convincing, here’s a few things I noticed in the process:First off -when you override your system you pretty much ruin your performance data. My week's performance doesn’t reflect my system performance, more so it reflects my weird hybrid trading systems performance.In terms of validating a new portfolio,this weeks datais useful to me for reference, but useless in terms of performance measurement.I also had afew interventionswhere I ended up causing way more problems than I fixed - for example, on RB & NG trades, I closed a position out in profit, and then the systems hit the trailing stop floor and executed the trailing stop - entering me in the reverse position, both times for a frustrating 1 tick loss.I also noticed that interfering tends to lead tomore interferenceas you look for more opportunities, try to optimize every single trade, or try to make up for a dumb past mistake.It also seemed to create more stress, as I no longer viewed it as out of my hands, but rather felt I needed to find the mistakes of my system before it was too late.Most importantly,interfering with my systems cost me money! There’s no reason to look further for justification, for me it was a less efficient and more costly method of trading.After a rather frustrating week, I had come up with a few tips that helped me monitor properly and separating potential good intervention vs bad intervention.Let’s begin with defining what I consider apractical override. I think if there is a rare and unusual excess headline risk or intangible risk that it is okay to intervene by modifying parameters prior to the trading day or to simply turn the system off temporarily.I don’t think this should be done often; an example is an earnings release in an equity your trading or a fed meeting when an interest rate decision is imminent.To give you an idea of what I believe constitutes an excess risk, I don’t think this should be done more than 4-6 times a year.

Don’t halt your system every time there is a presidential tweet - you’ll never fill any trades.

Don’t halt your system every time there is a presidential tweet - you’ll never fill any trades.

Some tips to help with monitoring

Monitor on mobile, or other limited platforms (where changes can’t be made if you wanted to without causing problems).

Step away from it; Come back every 2-6x intervals (if trading 15M, come back every 1.5 hours to review trades; 60M, every 2-3 hours).

Stay busyworking on new systems, researching new entries or alpha models.

Platform Mutewent a long way for me, whenever I hear a trade entered it’s almost impossible to not look at it.

Multiple targets& / or trailing stops / Alternate Exits - they can help ensure you have some discretion over closing trades that for eg. are +250 within the first bar or trades that cross back under a moving average for an MA entry signal. Also using unrelated but alternate stops can be helpful - like a LL/HH stop, etc.

Build systems that fityour style- This is very important if it doesn’t fit your trading style it will never be easy to monitor.

I once traded a swing trading system withmassive MFE’s(large winning trades that would turn into losers). It was unbearable for me (a scalper) to monitor. I shortened interval, added trailing stops and targets to eliminate large MFE.

Build-in failsafe, and automate good overrides - and stick to them!

Failsafe

Failsafe:I use an int based boolean, with levels 0 1 or 2 for the level of alert (0 is off, 1 is printed Alert, 2 is Halt (qty = 0)).

Max Drawdown:I leave 1 - 2 Stdev’s beyond largest to date or max DD from Monte Carlo simulations.

Win Pct:I set this 2.5 - 5% below my actual win rate (<70% if 73% Win-Rate). (Be careful with this early on, until the sample size is large—otherwise, 1 or 2 losing trades will trigger this)

Largest Loss:I price in an extra 1 - 2 Stdev’s of largest loss (or fixed stop loss) for slippage/gaps.

Consecutive Losing Trades:I add in 1 or 2 trades longer than longest to date.

Average Trade:$5 - $10 < tested average trade; (Again, be careful until sample size large enough)

These failsafe mechanisms are particularly important in regulatory environments likeautomated trading India, where SEBI mandates specific risk controls including position limits, order-to-trade ratios, and kill switches. Building these compliance requirements into your override logic ensures your system meets both your risk management and regulatory obligations.

Summary of Results

The cumulative performance difference for my overrides (vs. system exits) came out to a difference of -$850/contract, so I averaged $85Lessper trade than my system did.I was negative overall for every instrument I attempted to improve aside from the Euro (I’m convincednobodyis good at trading the Euro, this was sheer luck in small sample size).I further categorized the overrides, and in the event of override byhaltingor omitting a trade, the total performance difference was -$34/contract.So if you feel youmustoverride, according to this small sample it is best to simply omit a trade, rather than get involved after the trade is entered.In summary, if the system opens a trade, you’re better off letting the system close it - at least I was. The mindset that helps me is having confidence in my code, and trusting the ability and hard work that went into making thisexactlyhow it is - I put my faith in my own due diligence.

I know how tempting it is to close out trades on your own, but let your system earn the wins!

Happy Trading!Disclaimer: The views, opinions, and information provided within this guest post are those of the author alone and do not represent those of QuantInsti®. The accuracy, completeness, and validity of any statements made or the links shared within this article are not guaranteed. We accept no liability for any errors, omissions or representations. Any liability with regards to infringement of intellectual property rights remains with them.

---

*Imported from QuantInsti Blog on 2026-04-27*
