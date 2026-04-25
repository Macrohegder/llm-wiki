# Investigating a Simple Trend Idea - Part 2

**原文链接**: https://www.tradequantixnewsletter.com/p/investigating-a-simple-trend-idea-ab1

**发布时间**: Jan 19, 2026

**抓取时间**: 2026-04-25 09:05:16

---

## 摘要

Premium Content Vault
Investigating a Simple Trend Idea - Part 2
Simplicity > Complexity: Always Be Simplifying, The Simplest Viable Solution Always Wins
TradeQuantiX
Jan 19, 2026
∙ Paid
6
6
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In the previous article, we took a very simple trend-following system idea and dissected it down to its core components. We learned what causes the system to make money and what rules are the key drivers of performance. We a...

---

## 全文

Premium Content Vault
Investigating a Simple Trend Idea - Part 2
Simplicity > Complexity: Always Be Simplifying, The Simplest Viable Solution Always Wins
TradeQuantiX
Jan 19, 2026
∙ Paid
6
6
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In the previous article, we took a very simple trend-following system idea and dissected it down to its core components. We learned what causes the system to make money and what rules are the key drivers of performance. We also uncovered some concerning features about the system that need to be addressed as well.
At the end of the part 1 article, I listed some ideas to test in an attempt to improve the system or increase its robustness. In this article, we are going to try implementing those ideas and see what we come up with.
Mindset In System Development:
My goals are to make a system with as few rules and parameters as possible. Simplicity is key; a rule really has to show a significant effect on the system in order to convince me to keep it. Also, a simple rule with slightly worse performance almost always trumps a complex rule with slightly better performance. It’s almost guaranteed the more complex rule is overfit.
Remember, a singular system doesn’t matter that much; it’s just one piece of the portfolio. Hence why we want robustness over performance. Robustness keeps the portfolio from failing; the performance comes from many non-correlated robust systems working together, each mediocre on their own, but extremely powerful when combined.
That is the mindset I am approaching this system with: simple system concepts and a portfolio-level view. If you don’t have a portfolio-level view, it’s very easy to throw away perfectly good systems. Of all the systems I personally trade, I wouldn’t trade a single one in isolation. I would only trade them together within a whole portfolio.
When you think about systems in this way, it’s much easier to look at system performance and design more objectively. The ideal portfolio-level thought process should be:
“That drawdown in 2008? I could curve-fit it out by tweaking the index filter, but wait, I just remembered I have a hedging system that makes money during 2008-like events! Okay, fine, I’ll leave it alone. The next market crash will likely behave differently anyway, so curve-fitting to remove one bad event won’t change the impact a future bad event would have on the system.”
Going into system development work with a portfolio mindset is crucial as it helps remove the urge to curve-fit. See this article for more details on the portfolio-level mindset.
Premium Content Vault
Portfolio Development Series - Part 1
TradeQuantiX
·
July 7, 2025
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your system…
Read full story
That’s enough of me blabbering about mindset. Let’s get to the good stuff. Let’s see what we can do with this system. As always, no promises it gets better; I write these articles as I do the investigation, so it’s true real-time learning for both you and me.
System Improvement Investigation:
As I mentioned in the part 1 article, there were a few ideas I listed to test for potential improvement of the system. To recap, those ideas were:
Add an entry rule to require a minimum amount of momentum prior to entry.
Ensure the stock has recently crossed the 200-day MA + two standard deviations for the entry signal.
Ensure volatility (standard deviations) is expanding to prove the stock is currently breaking out. Right now, a stock could calmly drift past the 2 standard deviations mark, which may mean that stock does not exhibit much momentum.
Remove the -2 standard deviations band from the exit rule. Just use the 200-day MA as the exit, or potentially add a trailing stop loss as well.
Allow the system to take more positions than 5.
Dynamically adjust volatility-based position sizing to help with those massive drawdowns.
If you remember, these ideas were not randomly pulled out of a hat. Instead, we tore the system apart to understand exactly what every component was doing, we looked at some example trades, and we ran some robustness sensitivities. Only from those observations were we able to come up with sensible ideas to test, rather than just random guesses based on a hunch.
To refresh what the in-sample results of the system looked like, below I have the system equity curve in green (benchmarked to the S&P 500 in red), followed by the performance stats of the system, and then the drawdown plot.
Baseline System Results (In-Sample):
This will be what we compare back to for many of the tests we will perform throughout the rest of the article. So burn those results into your memory… or just scroll back up in the article from time to time; that works too.
Let’s jump into the first system improvement idea (and remember, improvement doesn’t always mean better performance; it can also mean more robust!).
Change Number of Positions Held:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
