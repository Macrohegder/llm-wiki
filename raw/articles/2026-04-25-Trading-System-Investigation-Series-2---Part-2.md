# Trading System Investigation Series 2 - Part 2

**原文链接**: https://www.tradequantixnewsletter.com/p/trading-system-investigation-series-7d2

**发布时间**: May 29, 2025

**抓取时间**: 2026-04-25 09:03:36

---

## 摘要

Premium Content Vault
Trading System Investigation Series 2 - Part 2
Tearing A Short Side Day Trade System Apart, Then Rebuilding It Back Together
TradeQuantiX
May 29, 2025
∙ Paid
12
6
2
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In Part 1 of this series, I explored a short-side day trading system I found online, aiming to understand its concept and replicate its results. I coded it in my backtester and dug into its pros and cons.
Now, in Part 2, I’ll simp...

---

## 全文

Premium Content Vault
Trading System Investigation Series 2 - Part 2
Tearing A Short Side Day Trade System Apart, Then Rebuilding It Back Together
TradeQuantiX
May 29, 2025
∙ Paid
12
6
2
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In Part 1 of this series, I explored a short-side day trading system I found online, aiming to understand its concept and replicate its results. I coded it in my backtester and dug into its pros and cons.
Now, in Part 2, I’ll simplify, improve, and validate the baseline system. The final code and rules will be provided as well.
There’s no guarantee I’ll end up with an exciting or robust trading system—that’s just part of the game. Let’s dive in and see if we can create a system that adds value to our systematic trading portfolios.
If you missed the Part 1 article in the series, check it out below!
Simplifying The System:
From the discussion in Part 1 of this article series, it was pointed out that the system appears to be more complex than what I would consider ideal. There are a lot of trading rules and parameters within the trading system.
Complexity in systematic trading is a real concern. To truly trust a trading system and ensure it is properly fitted and captures the underlying phenomena, we have to understand how each component of the trading system contributes.
When a system has a bunch of rules, the relationship between any one rule and the outcome of each trade becomes difficult to understand. Thus, simplification is key and how I start every trading system evaluation.
Subscribe
Determine In and Out of Sample:
Before diving in, let’s define our in and out of sample date ranges:
In-sample: 2000–2018, used for simplification and improvements.
Out-of-sample: 2018–2025, used for validation.
The in-sample baseline results are below:
If you remember from the previous article, the system had the rules as listed below. I went through and studied each rule, one-by-one, to understand if the rule was significant to the performance outcome or not. Under each rule I have an italicized summary of if the rule was significant and will be kept, insignificant and will be removed, or required for the system to operate.
Entry Rules:
Stock is within the Russell 1000
I have left the universe alone for now, will continue this investigation on the Russell 1000.
Stock has an average volume of 1,000,000 shares or higher over the last 50 days
I have left this rule alone for now, 1,000,000 shares traded is sufficiently high volume for this system. Lower volume stocks may make it harder to get short shares to borrow. We can always go back and lower this number later, if desired.
The stock is $10 or higher
I have left this rule alone for now, $10 stock price is relatively low for US markets. Cheaper stocks may make it harder to get short shares to borrow. We can always go back and lower this number later, if desired.
The 39 day percent normalized ATR is within 1% to 8%
This rule appeared to be somewhat significant, the drawdown and volatility of the system increased without it, the rule stayed in the system… for now.
The 2 day percent normalized ATR is within 1% to 20%
This rule was very insignificant and the results of the system were essentially unimpacted without this rule. The rule was removed from the system.
The 5 day ADX is higher than 35
This rule appeared to be significant and the drawdown and volatility of the system increased without it, the rule stayed in the system.
The day before entry had an up move (measured from open to close) of more than 5%
This rule was make or break for the trading system, without this rule the system was unprofitable. Rule is very significant.
Place a limit order 5% above yesterday’s close
This rule appeared to be significant and the drawdown and volatility of the system increased without it, the rule stayed in the system.
Position Size Rules:
The system holds a maximum of 10 positions
I have left this position count alone for now, 10 stocks is a fine starting point, not too many and not too few trades.
The system holds equal weight positions (10% each)
I have left the position sizing lone for now, I tend to focus on position sizing last. Sometimes it is easier to understand relationships when position sizing is equal weight.
If there are more than 10 setups, rank by 10 day percent normalized ATR
Having a way to rank setups when there is more than 10 is important. We need some sort of rule here to start. I will begin with the current rule, but see if a better option exists later.
Exit Rules:
Cover the position market-on-close on the same day as the entry (no holding positions overnight)
Since this is a day trading system, this rule is required for proper operation. I am not looking to add complexities like a profit target at the moment. This rule will stay.
I removed the insignificant 2-day percent-normalized ATR rule and consolidated parameters where possible. When I say parameter consolidation, this means if two parameters were similar in value, I combined them into one to reduce a degree of freedom. The system went from 8 entry rules to 7 and from 10 indicator parameters (excluding maximum positions and liquidity) to 6 after consolidation. This reduced complexity, paving the way towards a potentially robust system.
Now that the system has been simplified to the min viable solution, we have a great base to start from. That base is a system with the core components required to operate and perform its intended purpose of being a short side day trade system. The backtested results reflecting this simplification can be observed below:
As you’ll notice, the results of the simplified system are very similar to the baseline system. I’ve removed one rule and 4 parameters, reducing complexity by multiple orders of magnitude, and the results are essentially unchanged. This shows how the baseline system had a bunch of needless complexity, simplicity is almost always better.
Now let’s move on to improving the system with this simpler version of the system as a starting point. As I go, I will continuously try to remove complexity and further reduce degrees of freedom as I potentially find better ways to filter and model the rules.
Subscribe
For deeper learning opportunities in systematic trading, consider signing up for the Systematic Trader School.
📈
This will consist of 10, 1-on-1 consulting sessions with me! By the end of the 10 consulting sessions, you’ll have a robust portfolio of 3–5 designed, developed, and implemented systematic trading strategies.
🥇
These aren’t theoretical trading strategies—you’ll develop real, tradable strategies for use with your trading account.
🚀 I’ll guide you step-by-step, from planning your portfolio and developing your own trading strategies, to conducting robustness testing and implementing the portfolio live.
📚
To learn more, check out the Systematic Trader School page. Also, you can book a free 30 minute consultation. During the call, I’ll explain exactly how it works and the transformation you can expect:
👉
[Click here to learn more about the
Systematic Trader School
!]
👈
👉
[Click here to book a free 30 minute consultation!]
👈
Improving The Trading System:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
