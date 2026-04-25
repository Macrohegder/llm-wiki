# Case Study: Dividend Investing - Part 2

**原文链接**: https://www.tradequantixnewsletter.com/p/case-study-dividend-investing-part-f11

**发布时间**: Jan 21, 2025

**抓取时间**: 2026-04-25 09:02:32

---

## 摘要

Case Study: Dividend Investing - Part 2
Creating a trend trading system around dividend stocks
TradeQuantiX
Jan 21, 2025
16
2
1
Share
Introduction:
In the previous article about dividend stocks, we looked at what dividend stocks are and their pros and cons. In this article, we are going to continue this exploration further, but with a systematic approach. I am a systematic trader, I do not take many discretionary trades; so I want to take the dividend investing approach and turn it into a rule based fully quantified system. Imagine the simplicity of having a completely rules based system you can simply run everyday and the system will tell you exactly what high dividend yielding stocks to allocate to. Then you sit back and collect a dividend payment every quarter. That sounds like a pretty...

---

## 全文

Case Study: Dividend Investing - Part 2
Creating a trend trading system around dividend stocks
TradeQuantiX
Jan 21, 2025
16
2
1
Share
Introduction:
In the previous article about dividend stocks, we looked at what dividend stocks are and their pros and cons. In this article, we are going to continue this exploration further, but with a systematic approach. I am a systematic trader, I do not take many discretionary trades; so I want to take the dividend investing approach and turn it into a rule based fully quantified system. Imagine the simplicity of having a completely rules based system you can simply run everyday and the system will tell you exactly what high dividend yielding stocks to allocate to. Then you sit back and collect a dividend payment every quarter. That sounds like a pretty sweet deal, especially for someone who is retired. So lets get to it!
Subscribe
The Dividend Trend Trading System:
Let me propose a few scenarios. Say you own a dividend paying stock and the stock reduces or even completely stops the dividend payment, what do you do? Or what if the dividend stock you own crashes 50%, what do you do? What if another opportunity arises but you already own a bunch of dividend stocks already and don’t have any more capital to allocate, what do you do? These are all scenarios that you need predefined rules to account for so when these situations inevitably do arise in the future, you can rationally make the correct decision and not make a silly decision out of fear or greed. This is why we are going to make a rules based trading system specifically focused on owning high dividend paying stocks.
I like the idea of having a trading system on high dividend paying stocks for a few reasons. The first is it can provide a good income stream of dividend payments for those who live off their trading and investments. Second, high dividend paying stocks can be thought of as a different sub universe within the US market. This could potentially serve as a good diversifier for my own personal trading portfolio where I own everything from no name small caps, to tech based large caps, and now potentially high dividend paying stocks as well.
Let’s break down how I think this system should work on a very high level:
Entry Criteria 1:
Buy high dividend paying stocks in an uptrend which have stable dividend payments
Entry Criteria 2:
Only buy new dividend paying stocks when the broader market is in a bull market
Exit Criteria 1:
Sell the high dividend paying stock when it stops trending
Exit Criteria 2:
Sell the high dividend paying stock when it stops paying dividends or if the payments reduce in value
Simple idea, but we need to be more specific. What we have outlined is very broad, so let’s define a couple of the terms used above a bit further. I want to break it down and make it more specific so you fully understand the direction I am going. This should hopefully be enough for you to replicate the system for yourself, if you want.
Entry Criteria 1:
“
High
” dividend paying stock:
This could be defined as the dividend is above x dollars per share or the dividend yield is above x%. Either should work.
Stock is in an “
uptrend
”:
Stock uptrend can be defined many ways. I generally use a simple trend filter, like the stock is above its own 200 day moving average. You could also say the stock breaks out to make a new high in the last 200 days.
“
Stable
” stable dividend payments:
Stable would mean the dividend is payed consistently and is non-erratic. The dividend payment value should be the same or increasing over time, not decreasing. I also would like consistent dividend income, so quarterly dividend payments that have not been missed in years would be preferred.
Entry Criteria
2:
Market is a “
bull market
”
This can be as simple or complex as you want it to be. I prefer simple regime filters like the S&P 500 above its 200 day moving average, that should suffice.
Exit Criteria 1:
Sell when the stock “
stops trending
”:
A simple trailing stop should work for this idea, from my own system development experience trailing stops tend to work fairly well.
Exit Criteria 2:
Sell when the stock “
stops paying dividends
”:
We picked dividend paying stocks based on consistent quarterly payments, so if the stock we own misses a dividend payment we assume it’s stopping its dividend payments. Maybe the company is in trouble or maybe they are restructuring, either way we want dividends so if the stocks stops paying them then we are out.
Sell when the stock when dividend payments “
reduce in value
”:
We are selecting stocks based on high dividend payments. If the dividend payments start to decrease then we are better off putting our money into another dividend paying stock that pays more.
Above, I have defined the structure of how the system will work. It should be enough to have a decent idea of what I am doing. You’ll notice I did not give exact calculations how I defined those rules, just words describing what the system is doing. I did that intentionally, I want you to exercise your systematic trading brain and think through how you may translate those criteria into code.  If you have any troubles you can reach out to me for some hints!
Alright that’s enough words, let’s show the system! Here is a backtest of this simple dividend trend system performance from 2000 to 2025 (today) on the entire US stock market.
Dividend Trading System Backtest (2000 - 2025):
Green line: Dividend Trading System
Red line: SPY Benchmark
Drawdown Plot:
Dividends Paid Per Month Plot:
As you can see, this simple theory of owning high dividend paying stocks in an uptrend has some merit. The equity curve is sable and growing and the dividend payments are doing the same. The compounded growth is good, but it’s not extraordinarily high. Stocks that pay high dividends consistently tend to be more stable companies. This system isn’t going to be buying high momentum companies like NVIDIA, which had returned over 100% in the last year or so. This system is more for income generation (or diversification, that’s how I plan to use it), buying cool, calm, and collected blue chip stocks that pay nice dividends.
One thing you’ll notice is that the system sells off it’s positions during bear markets and doesn’t take any new positions until the bear market turns back to a bull market. The system also sells positions when they are no longer trending up. Some may argue that you are better off not selling, and instead you should be holding the position through the tough times. We can actually test this to see if that is the case. Here are the results of the tests where there is not an index filter nor is there a sell rule for loss of stock trend. The only sell rule will be the reduction in dividend payments or missed dividend payments (we want dividends so if the stock stops paying we sell). Here are the results of this test:
No Trailing Stop:
No Index Filter:
No Index Filter OR Trailing Stop:
As you can see, selling the position when the stock trend ends is actually helpful to the system. You will actually make more in dividends over time by selling when the stock stops trending and then reallocating to a new opportunity rather than holding through the downtrend. You’ll also notice the index filter actually doesn’t do too much. I would consider this a good thing, it can be dangerous to trade a system that is very reliant on an index filter, it’s prone to overfitting (but that doesn’t seem to be a concern here). The trailing stop is really what makes all the difference. The old saying of cut your losers and let your profits run actually has some merit. Get rid of the non-trending junk in the portfolio and focus on the winners. Here’s why this works this way.
Dividends are paid on a per share basis, the more shares you own the more dividends you receive
To own more shares you need a larger account
To get a larger account you need to focus on having an asymmetrical risk profile (greater reward than risk, this system uses classical trend following principles)
By selling the positions that are underperforming and reallocating to stocks that are performing well, we can compound the account much better
The higher the account value the more shares we buy
The more shares we own the more dividends we are paid
You get the point…
So we need to focus on growing the account so we can own more shares and collect more dividends. We will do this by avoiding large downtrends and focus on the dividend stocks performing well right now.
A side note, I tend to hear something like the following a lot: “
If you used an index filter in your system, then you need to use the same filter on your benchmark
”. I’m not going to go into if I agree with that sentiment or not, but for anyone wondering I have the system comparison to the benchmark with the index filter applied. The system still outperforms the benchmark (the benchmark is SPY).
Now let’s give a simple example of how collecting dividends from this system might look. All of the backtests shown so far have dividends reinvested back into the system, but if we want to collect these dividends into our pockets we have to account for that in the backtest. Here is a simulation where a someone traded this system with a starting account balance of 100k in 2000. In 2018 they decided to retire and live off dividends so they start taking dividends out of the account to pay bills instead of reinvesting them. The blue line is the result of always reinvesting dividends. The green line is what our retired trader will see, when they start pulling dividends out of the account the compounding slows down a little bit (compared to the blue line). The red line is the cumulative dividends put into the retired traders pocket. The gap between the blue and green line is “filled” by the red line in a sense (it’s not perfectly like that due to compounding, but you can simplistically think of it this way).
The retired trader is collecting a solid 30k a year in dividends on a sub 1 million dollar account. If the trader had a larger account, then they would collect even more dividends. You can see how this is a powerful concept and could really pay off one day. Don’t discount a middle of the range CAGR system with stable growth, the dividends it may pay can really add up over time.
Subscribe
Conclusions:
The dividend trading system discussed in this article has many unique properties. It can serve as a portfolio diversifier because it potentially invests in different stocks than the rest of your portfolio. It can also serve as a good retirement system to use for collecting and living off dividends. The returns are not extraordinary, but the losses are limited and the growth is stable. For extraordinary growth look at momentum trading systems in the tech sector. Remember, I look at trading systems as just one piece of my portfolio. This system is just another diversifier for me (and potentially a cash flow source in the future). I already have the high growth trading systems in the tech sector, I want something different, which is why I am excited for this system. If you are interested in this system, give the coding a shot and let me know if you need any hints. Have a good one!
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
16
2
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
