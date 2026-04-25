# Luck By Design - Part 1

**原文链接**: https://www.tradequantixnewsletter.com/p/luck-by-design-part-1

**发布时间**: Mar 11, 2025

**抓取时间**: 2026-04-25 09:02:43

---

## 摘要

Premium Content Vault
Luck By Design - Part 1
Navigating the Randomness of Luck in Your Trading Systems
TradeQuantiX
Mar 11, 2025
30
4
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication aims to equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
Introduction:
Luck exists everywhere. Whether you narrowly avoid hitting the pothole in the road because you saw it and swerved at the last second, or you drop you...

---

## 全文

Premium Content Vault
Luck By Design - Part 1
Navigating the Randomness of Luck in Your Trading Systems
TradeQuantiX
Mar 11, 2025
30
4
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication aims to equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
Introduction:
Luck exists everywhere. Whether you narrowly avoid hitting the pothole in the road because you saw it and swerved at the last second, or you drop your phone over the toilet but happen to snag it out of mid-air, avoiding catastrophe. There is a massive component of luck in life. You can do everything wrong yet things can still work out because you got lucky, or you can do everything right and everything turns out terrible because you got unlucky. You're lucky when luck is on your side and unlucky when it's not. Luck is so random. How can we control it? How does it impact our trading?
The effect of luck on systematic trading is what I want to cover in today's article. I will point out and explain some common areas where luck plays a big role in our trading. I will go over ways luck can creep into systematic trading, and then explain how to ensure luck is on our side as often as possible. Then, in subsequent parts of this article series, we will walk through examples of how to implement this concept in practice.
Thanks for reading Systematic Trading with TradetroniX! Subscribe for free to receive new posts and support my work.
Subscribe
Common Areas Where Luck Exists In Systematic Trading:
It doesn’t matter how skilled you are when it comes to systematic trading; luck still finds its way into your results. Though the best systematic traders know how to control luck and keep it on their side as often as possible. Before we dive into how to control our luck in systematic trading, let’s first give some examples of where luck finds its way into systematic trading. There are too many regions of luck that exist to list them all, but there are some areas where systematic trading luck is common and addressable. Remember, when I refer to luck, that also means bad luck and vice versa; good luck and bad luck are the two paths of outcomes that can happen as a result of any event. The best way to illustrate luck in systematic trading is through examples:
Timing Luck:
Say you just developed a momentum trading system with a monthly rotation interval. On the first day of each month, you sell some lagging positions and buy some new positions that appear to be stronger performers. You hold the new positions for a month, then repeat the portfolio rebalance process at the beginning of the next month. Seems like a sensible approach; it’s a pretty common approach too. I personally trade systems that operate in this manner.
Here's where luck comes in: what happens when you get completely loaded up on new positions and then the markets drop 20% mid-month? You're stuck holding all the open positions until the next rotation cycle, two weeks from now. That's a massive open trade drawdown to have to sit through for two whole weeks. Could you endure this? Somehow, we need to remove this timing risk to reduce the pain dealt by scenarios like this. Sure, we could just add a stop loss to the system that allows an exit any time during the month, but this adds some complexity to the trading system (remember, 99% of the time, less complexity is better). There may not be many data points where this stop loss was triggered historically to understand if the stop loss rule is robust or not. It may be difficult to prove the stop loss actually adds value or if it was just curve fit to a small set of data points historically. Also, the more complexity within a trading system the more susceptible you are to lucks wrath.
Conversely, maybe the markets start dropping on the last day of the month, and you sell all your positions the next day based on the system rules, and your system goes flat. You end up with a small 2% drawdown as opposed to a 20% drawdown. You look at your trading system and say, “Phew, I got really lucky there!” But we don’t want to just get lucky sometimes; we want to control this luck to the best of our abilities. If you got lucky this time, sometime in the future, the opposite scenario will happen with 99% certainty. This timing luck is something we can better control with the proper techniques.
Parameter Selection Luck:
Assume you just spent a lot of time developing a long side trading system on the NASDAQ 100 and the system results look great historically. You launch the system live just to watch it trade sideways for a year. You scratch your head and ask yourself “Why is it doing that? The NASDAQ 100 is up this year, this system should have made money”. Most likely, you had a bad case of parameter selection luck (or un-luck!). This past year, the system was just out of tune with the markets, it’s likely still a profitable system it just wasn’t able to capture the big moves this year.
You take the system back to the drawing board and try to improve the system such that it produces positive results for the previous year. You discover that if you just tweak one of your parameters by 5% - 10% the system becomes profitable for the previous year. This is a case of parameter selection luck. The system may not have been overfit per say, but the parameters that worked the best this year were different than the parameters that worked the best the years before.
You start to play with the system parameters more. You notice some trends in the performance where if you tweak the parameters one way, the system performs better this year but the year before that the system performs a little worse. Then you tweak the parameters the other way and the opposite happens, this year looks flat in terms of performance but the year before looks good. The equity curve as a whole looks stable, but depending on the parameter selection, the years that perform the best shift around.
This phenomenon is completely normal. The performance going forward will have some impact of luck involved because we don’t know what the optimal parameters are next year or how they will then shift the year after that. We need to control the luck of parameter selection to ensure our system performance going forward is as stable as possible and not susceptible to subtle market shifts. This is another region of luck that we can potentially control with the proper techniques.
Universe Selection Luck:
Similar to the previous example in parameter selection luck, again assume we just developed a killer trading system on the NASDAQ 100. Again, you launch the system and the performance is lackluster over the next year. You look at the markets performance and realize the NASDAQ 100 actually didn’t perform that well this year. So, it makes sense the system did not perform that well either. Instead, it appears there was a performance shift from the tech industry to the health care industry over the past year. Due to this shift, the S&P 100 actually greatly outperformed the NASDAQ 100. It appears your system was potentially not trading the best performing market this year.
You then take your system you developed on the NASDAQ 100 and apply it to the S&P 100 and run a backtest. Looking at the results you are not impressed. The first 10 years of the S&P 100 backtest greatly underperform the system performance on the NASDAQ 100. But you then notice something interesting, in the past few years there was a shift and the system rules had started to perform very well on the S&P 100 after not performing well for the first 10 years of the backtest. You’re confused, you don’t know if you should transition the system from trading the NASDAQ 100 to the S&P 100 because the S&P 100 performance looks like its improving, or keep it on the NASDAQ 100 and hope next year the great performance comes back. The results of a decision like this would be nothing but pure luck. There is no knowing what universe will perform better during the coming year. This is another case of luck that we will attempt to control.
The graph above shows the rolling yearly performance of the NASDAQ 100 (Blue) and the S&P 100 (Orange). You can see how the performance of the universes shifts back and forth in terms of which universe is outperforming.
Entry/Exit Rule Selection Luck:
This example is again similar to the parameter selection luck example. Say you develop a trading system that trades the VXX ETF (an ETF that tracks the movement of the VIX volatility index). You want a hedging system so when the markets panic, you can potentially profit from the increased volatility. The trading system you develop uses a Bollinger Band breakout to enter the trade. You launch the system live and the next time the markets panic you buy the VXX to try to profit from the panic. You end up buying the top of the move in the VXX and the VXX falls back down and you exit at a loss. “What the heck?” you say to yourself. The system bought the panic but was too late to the party to profit from the panic.
After some tinkering with the system you discover that if you used a Donchian channel breakout instead of a Bollinger Band breakout you would have perfectly caught the move in the VXX. Nothing with your original entry logic was wrong, it just didn’t capture the move this time around. You check the historical trades in the backtest and see the Bollinger Band breakout does cause late entries from time to time. You also notice that the Donchian channel misses some good VXX moves from time to time as well (but happened to nail the most recent entry). Neither entry option is right or wrong and neither is necessarily better or worse over the long term. So, which entry rule do you go with? Another choice in the system development process purely down to luck.
Subscribe
Luck, Risk, and Opportunity:
You may have observed that these four instances of luck in trading bear a striking resemblance to one another, sharing a common origin. Each of these instances of luck can be traced back to decisions made during the design phase of the trading system. It is often claimed that systematic trading eliminates discretionary decisions; this claim holds true once the system is running live, but during the system development process, the process is entirely driven by discretionary decision-making. Systematic trading front-loads discretion, allowing live trading decision to be computer automated and non-discretionary. Each of the four examples of luck cited above, which led to unfortunate outcomes, were once within our control. This implies that we possess the capability to make strategic decisions which can align luck in our favor. There are multiple techniques we can utilize to move our results towards beneficial rather than detrimental luck.
The best way to position yourself to experience the most lucky outcome is to spread your risk across as many positive expectancy opportunities as possible. Manage your luck by managing your risk for each opportunity. What the heck does that mean? Let's break it down…
The most effective way to invite good luck into your trading system is to diversify risk across a broad spectrum of timing, parameters, entry/exit criteria, and universes; rather than concentrating on a single set simply because historical backtesting suggests it has been successful or the best. In essence, good luck in trading is often the byproduct of strategically positioning oneself to exploit each trading opportunity from as many different angles as possible and by spreading risk across them.
This fundamentally changes the luck outcomes from a binary 1 0, good luck or bad luck, to a continuous scale between good luck and bad luck. See the figure below showing how traders typically approach a trading opportunity.
They approach the trading opportunity from the lens of win or lose, good luck or bad luck. Good luck results in a score of +1 and bad luck a score of -1. Assume a trading opportunity resulted in a loss (bad luck), we score a -1 for that trade. If instead you spread your risk across many different ways of looking at the same trading opportunity, the sum of luck changes dramatically.
Here we looked at the same trading opportunity from four different angles and spread our risk evenly across them. Instead of resulting in a bad luck -1 outcome for a losing trade, the results begin to look a little different with this approach. The first risk bucket results in bad luck (-0.25), the second risk bucket results in good luck (+0.25), the third resulted in bad luck (-0.25), and the fourth risk bucket actually decided not to participate in this trading opportunity (+0). The sum of the scores is -0.25. This is a significantly better outcome than the first example where we only have 1 risk bucket and had a full -1 bad luck outcome. Rather than a full unlucky outcome of -1, we only had a small unlucky outcome of -0.25 for the same trading opportunity.
To draw an analogy, when applying to colleges, one does not apply to just one institution; instead, applications are spread across multiple schools to mitigate the risk of rejection. By distributing your risk across numerous potential outcomes, you enhance your chances of a favorable result—getting into college. This principle of risk distribution is what we will apply to our trading systems via various methods to ensure we always have as much luck as possible on our side.
Subscribe
How to Control Luck Conceptually:
For each trading opportunity, we control our luck by spreading our risk as much as possible. This is why financial advisors preach diversification. Diversification is just a way of spreading around risk, luck, and opportunity. So, we are going to control our luck via diversification, but not in the traditional way that people think, where diversification happens at the portfolio level, but rather intentional diversification at the system level.
Intentionally working in diversification at the system level is a very powerful technique that I don’t see discussed too often. Rather, what I tend to see is portfolio level diversification discussions. It takes a slight mental shift to look at your collection of systems and think about system level diversification rather than portfolio level diversification. Pretend like you only have one trading system and you want to diversify as fast as possible without developing a completely new trading system, how do you do it? The only rules are you can modify the current trading system and trade both the modified trading system(s) and the original.
Well, looking back up at the four examples of where luck creeps into trading, we can easily modify four things to create system-level diversification. We can modify the timing mechanism of the system, the parameters of the system, the entry/exit rules of the system, and the universe the system trades. We can do these things relatively fast, much quicker than if we were to completely restart system development with a new and different trading idea.
This may sound stupid, and maybe even obvious to some, though to others, this may be a completely new concept. Whatever boat you are in, let me tell you, this concept is one of the main techniques that turned my trading profitable. Rather than being reliant on one trading system having the perfect parameter selection, perfect timing, the best entry/exit rules, and on the best performing asset; I was able to rely on a robust portfolio of systems all with system level diversification. This ensured I was on the right side of luck. Rather than me getting lucky sometimes or unlucky other times, my results have become much more consistent. My equity curve has stabilized and is positively skewed towards the lucky side. I’ve spread my risk across timing mechanisms, parameter sets, entry/exit rules, and universes, thus positioning myself to experience the most lucky outcomes on average. See the example system below I actually trade live where I have implemented some of the techniques of luck control, thus smoothing out my equity curve overall.
Each colored line represents a different version of the same system concept. The gray filled region represents the return of these three system versions combined together. The equity curve ride becomes a lot smoother with system level diversification!
Subscribe
Conclusion:
This article has explored the often underestimated role of luck in systematic trading, illustrating how it can impact even the most meticulously designed strategies. We've examined four key areas where luck can influence trading outcomes: timing, parameter selection, universe selection, and entry/exit rule selection.
Each of these aspects highlights how discretionary decisions during the development phase of a trading system can lead to either beneficial or detrimental luck outcomes. However, the article emphasizes that we're not merely at the mercy of luck. Instead, we have the power to manage and potentially control it through strategic decision-making at the system design phase.
I've introduced the concept of controlling luck by spreading risk across multiple opportunities, suggesting that diversification at the system level can stabilize performance and skew outcomes towards good luck. This technique involves modifying existing systems in terms of timing, parameters, entry/exit rules, and trading universe, rather than developing entirely new systems.
While this article has been somewhat of a tease, discussing these concepts in theory without diving into specifics, the journey doesn't end here. In the next articles, we will walk through practical examples from start to finish, developing a system and implementing the four components of luck discussed. You'll see firsthand how these luck control techniques can increase the stability and robustness of a trading system, ultimately leading to improved out of sample system performance. So, be on the lookout for the coming articles where theory meets practice, and we put this technique to the test.
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
Do you have ideas/suggestions for future articles? Let me know what you want to read about by clicking the button below and submitting your suggestions. Your suggestions are greatly appreciated as they help tailor this newsletter to what you want to read about.
Start Survey
Disclaimer
The information and services provided by the Systematic Trading with TradeQuantiX newsletter are for educational and informational purposes only and do not constitute financial advice, investment recommendations, or guarantees of trading performance. Any information provided is general in nature and does not take into account your individual circumstances. Trading involves significant risks, including the potential for substantial financial losses, and past performance is not indicative of future results. The information is provided ‘as is’ without warranty of accuracy or completeness. All decisions and actions based on the information provided are the sole responsibility of the reader. You should seek independent professional advice before trading. The Systematic Trading with TradeQuantiX newsletter is not liable for any losses, damages, or outcomes resulting from the use of this information or our services.
30
4
4
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
