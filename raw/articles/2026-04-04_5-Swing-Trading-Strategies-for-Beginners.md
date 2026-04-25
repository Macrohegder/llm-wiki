# 5 Swing Trading Strategies for Beginners

**原文链接**: https://quantifiedstrategies.substack.com/p/5-swing-trading-strategies-for-beginners

**发布时间**: Mar 19, 2026

**抓取时间**: 2026-04-04 22:08:55

---

## 摘要

5 Swing Trading Strategies for Beginners
Rules, Backtest, and Results
QuantifiedStrategies.com
Mar 19, 2026
20
3
2
Share
Today, we provide you
5 swing trading strategies for beginners
.
Swing trading is holding a tradable asset for one or more days to catch price changes or swings.
It is different from day trading because you aren’t closing everything by the end of the bell, but it isn’t buy-and-hold either because you aren’t waiting years for a return. You are looking for short-term price movements.
All of the data here comes from backtesting the SPY, which is the ETF that tracks the S&P 500, though you can use futures like the ES contract too (but we have not backtested the strategies on that contract).
The core idea is simple but people mess it up by being too aggressive or not having p...

---

## 全文

5 Swing Trading Strategies for Beginners
Rules, Backtest, and Results
QuantifiedStrategies.com
Mar 19, 2026
20
3
2
Share
Today, we provide you
5 swing trading strategies for beginners
.
Swing trading is holding a tradable asset for one or more days to catch price changes or swings.
It is different from day trading because you aren’t closing everything by the end of the bell, but it isn’t buy-and-hold either because you aren’t waiting years for a return. You are looking for short-term price movements.
All of the data here comes from backtesting the SPY, which is the ETF that tracks the S&P 500, though you can use futures like the ES contract too (but we have not backtested the strategies on that contract).
The core idea is simple but people mess it up by being too aggressive or not having proper trading rules. You want to exploit the long-term rising trend of the stock market by buying when there is short-term weakness or panic. You buy the weakness and you sell when the market shows strength. This is called mean reversion.
Let’s go to our first swing trading strategy for beginners:
Strategy 1: The Mean Reversion Band and IBS
This first strategy is about identifying when the price has dropped significantly from a recent high. You need to do some math for this one:
5 swing trading strategies for beginners trading rules
First, calculate the average of the High minus the Low over the last 25 days. This gives you the average daily range. Then you calculate a band that is 2.5 times lower than the high of the last 10 days using that 25-day average range.
It sounds complicated but it’s just measuring how far the price has stretched away from its recent peak.
You also need the
IBS indicator
: IBS is (Close - Low) / (High - Low). It tells you where the close is relative to the day’s range. If SPY closes under that band you calculated and the IBS is lower than 0.3, you go long at the close.
The exit is simple. You sell when the close is higher than yesterday’s high. You are selling into strength.
The green and red arrows show you where you buy and sell:
Looking at the numbers from 1993 to 2025, a $100,000 starting capital grew to 1.2 million dollars:
5 swing trading strategies for beginners backtest
That’s an 8% annual return. Now, that is slightly lower than just buying and holding the S&P 500, but here is why it matters: you are only in the market 18% of the time. If you aren’t in the market, you aren’t exposed to the big crashes.
The max drawdown for this strategy was 23%, while buy-and-hold investors had to sit through a 55% drop. When you divide that 8% return by the 18% time spent in the market, the risk-adjusted return is 44%. You get most of the gains with a fraction of the ulcer-inducing drops.
Strategy 2: Turnaround Tuesday
This one is a classic. It’s often called
Turnaround Tuesday
because the market has a habit of rallying on Tuesdays after a crappy Monday.
The rules are very specific. You buy at the close on Monday, but only if two things are true: today’s close is lower than Friday’s close, and Friday’s close was lower than Thursday’s close. Basically, the market has to be down two days in a row ending on a Monday. If that happens, you go long at the Monday close.
You exit when the close is higher than yesterday’s high.
It’s a pure play on short-term panic. People get scared over the weekend, they sell on Monday, and then the professional buyers step back in on Tuesday.
It doesn’t work every single time because losing trades are part of the process, but the equity curve since 1993 shows it’s a consistent way to grab small gains.
5 swing trading strategies for beginners results
A 100,000 investment would have compounded annually at 7.2% from 1993 until today. The equity curve rises steadily, and the equity would have grown to one million by today. Not too bad for such a simple strategy. There are 271 trades that, on average, are invested just 4 days, thus making you invested just 11% of the time and hence avoiding the worst drawdowns. Max drawdown is at only 16%. Again, the risk adjusted return is very high at 65%.
Strategy 3: The 5-Day Low Entry
If you want something even simpler, look at Strategy 3.
You buy when the close is lower than the low of the previous five trading days. That’s it for the entry. You are looking for a week’s worth of downward pressure. When the market breaks below a five-day low, it’s often overextended to the downside.
The exit rule stays the same as the others: exit when the close is higher than yesterday’s high. This is the theme of these strategies. You buy when people are selling and you sell the second the market shows a sign of life. You don’t wait for a huge rally. You just want that one “swing” back to the mean.
5 swing trading strategies for beginners performance
If we look at the equity curve of the strategy, it’s hard not to be impressed of such a simple strategy. You started with 100,000 in 1993 and end up with 1.25 million today, despite being invested just 21% of the time. The annual returns are 8%, while the risk-adjusted return is 37%. Again, it shows that simplicity works in the stock market. As a matter of fact, simplicity trumps complexity.
Strategy 4: Volatility Contraction
This strategy uses the ADX indicator and the daily range. ADX measures the strength of a trend.
For this strategy, you want the 5-day ADX to be above 40. That means there is a very strong trend happening. At the same time, you want today’s range, the High minus the Low, to be the lowest range of the last 6 days. This is a “volatility squeeze.”
The market is in a strong trend but the price movement has suddenly tightened up. It’s like a spring being coiled. You buy that tight range and, again, you sell when the close ends higher than yesterday’s high. You are betting that the trend will resume or snap back after that brief period of quiet.
Let’s look at how your equity would have grown if you traded all signals from 1993 until today.
Swing strategies for beginners
We start with 100,000 USD in 1993 and let it compound until today. As you can see, the equity shows an upward slope. There are a few setbacks along the way, but overall, the strategy performs reasonably well. The statistics are not as good as the previous three strategies, but the strategy complements the other strategies well.
Strategy 5: New Highs with Low IBS
This last strategy is a bit counter-intuitive. Usually, people see a new high and they want to buy because they think the market is “breaking out.”
This strategy does the opposite. You look for a day where today’s high is higher than the previous high of the last ten days. So, it’s making a 10-day high.
But, you only buy if the IBS indicator is below 0.15. Remember, IBS is (Close - Low) / (High - Low). An IBS of 0.15 means that even though the market hit a new 10-day high at some point during the day, it closed in the bottom 15% of its daily range. It’s a “failed” breakout. The market tried to go higher and got rejected.
Why buy that? Because in a long-term bull market, these intraday rejections are often just temporary noise.
Swing strategies for beginners, mean reversion
From 1993 to today, a $100,000 investment in this would have grown to about $300,000. The annual return is 7.2%, but you are only invested 11% of the time.
You only took 271 trades over those decades. The average trade only lasts 4 days. Because you are out of the market 89% of the time, your max drawdown is only 16%. Your risk-adjusted return here is 65%. This is how you stay in the game for thirty years without blowing up your account.
5 Swing Trading Strategies for Beginners Combined
We’ve now presented five free swing trading strategies for beginners. To wrap things up, let’s run a final combined backtest.
In this test, we trade all strategies simultaneously, but allocate 100% of the equity to a single position at any given time. That means we ignore new buy signals if a position is already open. Since all five strategies use the same exit rule, there are no conflicts when it comes to selling.
When we combine all five strategies, the result is a significantly higher number of trades.
5 Swing trading strategies for beginners
An initial investment of 100,000 in 1993 would have grown to 3.2 million, with a maximum drawdown of just 23%. That’s the power of compounding - it snowballs over time. Keep in mind that the scale on the right is logarithmic, not linear, so what you’re seeing reflects relative changes.
Let’s summarize the combined results. Across 975 trades, the average return per trade was 0.38%, leading to a compounded annual return of 11.1%. That’s better than buy-and-hold, despite being invested only 41% of the time.
When combining all five strategies, there were only two losing years: 2008 and 2018, down 1% and 13% respectively.
And yes, it feels great to make money when the market is falling. Even though all these strategies trade only from the long side, bear markets can still be favorable. Increased volatility often improves short-term long setups, not just short strategies.
Practical Realities and Mistakes
One major thing people ignore is slippage and commissions. In these backtests, we include 0.03% per trade for those costs. If you use a broker with high fees or you trade stocks with no liquidity, those small costs will eat your 7% or 8% annual return for breakfast.
You also have to follow the exit rules. Beginners often see a trade go in their favor and they get greedy. They think, “Maybe it’ll go higher tomorrow.” No. The rule is you exit when the close is higher than yesterday’s high. If you don’t sell on that strength, you are no longer swing trading; you are just gambling on hope.
Common mistakes include:
Over-leveraging:
Thinking that because the drawdown is low (like 16% in Strategy 5), you can trade five times your account size. Don’t.
Ignoring the Trend:
These strategies work because we are exploiting the long-term rising trend of the S&P 500. If the entire global economy is in a structural collapse, these mean reversion plays will be much riskier.
Failing to Backtest:
Don’t just take a strategy from a PDF and throw your life savings at it. You need to understand that the “Turnaround Tuesday” logic works on the SPY, but might not work on a random volatile penny stock.
The reason these strategies matter is that they give you a mathematical edge. You aren’t guessing. You are looking for specific conditions, like a Monday close being lower than a Friday close, and acting on them.
It is boring. It is repetitive. But that is what professional trading looks like. You spend most of your time waiting for the market to panic, you jump in for 4 days, and you get out when things look good again. It keeps your stress low and your drawdowns manageable compared to the 55% drops that regular investors have to endure. Stay grounded in the numbers and don’t try to be a hero. Just follow the rules.
However, this is not investment advice. Please do your own backtesting and due diligence!
That was all for today, and we hope the
5 swing trading strategies for beginners
give you some food for thought.
20
3
2
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
