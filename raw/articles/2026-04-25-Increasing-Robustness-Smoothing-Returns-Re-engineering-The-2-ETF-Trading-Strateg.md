# Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy

**原文链接**: https://www.tradequantixnewsletter.com/p/this-strategy-is-stable-during-adverse

**发布时间**: Jun 17, 2025

**抓取时间**: 2026-04-25 09:03:50

---

## 摘要

Premium Content Vault
Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy
Developing My Own Version Of The Simple 2-ETF Strategy Shared By The Algomatic Trading Database
TradeQuantiX
Jun 17, 2025
∙ Paid
16
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Recently, the newsletter
The Algomatic Trading Database
shared a 2 ETF strategy that beat the Nasdaq 100. The Algomatic Trading Database found the system concept on X and decid...

---

## 全文

Premium Content Vault
Increasing Robustness & Smoothing Returns: Re-engineering The 2-ETF Trading Strategy
Developing My Own Version Of The Simple 2-ETF Strategy Shared By The Algomatic Trading Database
TradeQuantiX
Jun 17, 2025
∙ Paid
16
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Recently, the newsletter
The Algomatic Trading Database
shared a 2 ETF strategy that beat the Nasdaq 100. The Algomatic Trading Database found the system concept on X and decided to test the idea himself, sharing his results in his newsletter.
This strategy consisted of an allocation of 33% to the TQQQ ETF (3x leveraged Nasdaq 100) and a 67% allocation to the BTAL ETF (market neutral, short-beta exposure).
What interested me about this strategy was that it outperformed the Nasdaq 100 on both an absolute and a risk-adjusted basis, meaning it had lesser drawdowns while also achieving higher compound annual growth. Hence, I was inclined to do my own research on the concept. You can check out the original article here:
Algomatic Trading Database
Strategy #2: This Simple 2-ETF Strategy Has Outperformed the Nasdaq for 13 Years
A once‑a‑year rebalance between an anti‑beta ETF and a 3× Nasdaq fund has compounded at 19.6 % since 2012 with a –15.7 % max drawdown…
Read more
a year ago · 36 likes · 11 comments · Algomatic Trading
In this article, I would like to take the original strategy concept and decompose it. I will discuss what I think is great about it, as well as some of the drawbacks and risks associated with the strategy. Then, I will create my own version of this strategy which addresses some of the risks I will outline.
The Algomatic Trading Database Original Strategy:
Let’s first start by sharing what the original strategy results looked like:
Looks like a pretty good starting point! Outperformance to the Nasdaq 100 over the long term with lesser drawdowns? Sign me up!
Well, not so fast. We have to do our own research on the idea first. Never blindly trust a trading system found online or even in a book. Do your own research!
That’s exactly what we will do in this article.
Before I start working on the strategy, let me first discuss some aspects of this strategy that I think are great.
Original Strategy Benefits:
One of the key features that makes this strategy interesting is its simplicity, holding only two ETFs. It doesn’t get much simpler than that.
Additionally, the fact that it only rebalances yearly makes it extremely easy to execute and more tax-efficient.
It also utilizes a technique, often referred to as return stacking, which makes this strategy capital-efficient. Rather than buying the QQQ ETF, it buys a 3x leveraged version of that ETF called the TQQQ, but with one-third the position size; this results in exposure equivalent to 100% allocation to QQQ. This allows us to have equivalent exposure to the Nasdaq 100 while also freeing up a bunch of capital to be used for other diversifying assets. It’s the equivalent of using margin without having to pay any margin loans. This is a technique which emphasizes capital efficiency and diversification.
Another aspect I like is the strategic use of the BTAL ETF. This is a market-neutral, short-beta ETF, and thus will be inherently uncorrelated to the TQQQ ETF. The BTAL ETF aims to perform well when the broader market declines by employing a strategy that goes long on low-beta U.S. equities (stocks with lower volatility relative to the market) and short high-beta U.S. equities (stocks with higher volatility).
BTAL can therefore be used as a hedging tool or diversifier within portfolios, as its market-neutral approach can help reduce volatility and provide returns uncorrelated with traditional stock markets.
This BTAL ETF exposure is the main driver of the original strategy’s improved risk-adjusted performance compared to the Nasdaq 100. When the Nasdaq 100 is experiencing a drawdown, the BTAL ETF is likely performing in a completely different, uncorrelated manner, leading to a smoother equity curve.
Using the capital efficiency of return stacking with the TQQQ ETF and using the spare capital to allocate to the BTAL ETF, a diversifying asset with a non-correlated return stream, is why the system results in improved risk-adjusted metrics when compared to the Nasdaq 100.
Original Strategy Drawbacks and Risks:
While there are many aspects of this strategy that I like, there are some risks and drawbacks inherent to the original strategy that I would like to address as well.
The first is the risk inherently baked into using leveraged ETFs. It is likely obvious, but the risk of a leveraged ETF is the fact that it uses leverage. In this case, the strategy uses a triple-leveraged ETF. So, when the Nasdaq 100 drops 10%, the TQQQ will drop around 30%. When the Nasdaq 100 drops 20%, the TQQQ drops 60%.
You may be able to see where I’m going with this.
When the Nasdaq 100 drops 33%, the TQQQ has basically lost nearly all of its notional value. It doesn’t always work exactly like that, but that’s generally what will occur.
Luckily, since the TQQQ's inception around 2010, the worst drawdown experienced has not wiped out the fund. The worst drawdown so far occurred during the 2022 and 2023 bear market. During this time, the Nasdaq 100 dropped 34%, and the TQQQ dropped 81%. See a drawdown comparison between QQQ (red) and TQQQ (green).
Yikes!
You could imagine how holding the TQQQ ETF may have caused a lot of pain to investors during this time. Ironically, I just used the term "investor." I do not think the TQQQ should be used as an investment-type asset where you buy and hold for years at a time.
Rather, I view leveraged ETFs like TQQQ as more of a tradable instrument. Now, when I say tradable, I don’t necessarily mean day trading, but holding periods of a few weeks to a few months at a time are reasonable, with solid risk procedures in place.
How I might go about this is to only hold the TQQQ ETF when it’s above a simple moving average, then go flat when it’s below the moving average. This allows me to be risk-on when the markets are favorable and risk-off when the probabilities of a large market sell-off are higher. Then I’ll have a higher probability of avoiding the massive drawdowns inherent to these leveraged ETFs.
Another risk is the limitation of the backtest. The TQQQ ETF's inception was around the beginning of 2010. While 15 years of backtest history is decent, it is not enough for me to have 100% confidence in such a strategy. The only truly difficult market conditions that the TQQQ ETF has endured are COVID and the 2022 and 2023 bear market. While these market periods were difficult, there have been worse market corrections in the past, such as 2000 or 2008.
The TQQQ ETF would have likely been obliterated during 2000 or 2008 market crashes. There's a very interesting Reddit post where somebody simulated the TQQQ back in time with different inception dates. You can see how the performance differs vastly if the TQQQ ETF was incepted just before the 2000 market crash vs. just after the crash.
TQQQ Inception in 2002, Just After 2000 Market Crash:
Red Line: TQQQ
Blue Line: QQQ
TQQQ Inception Just Before the 2000 Market Crash:
Red Line: TQQQ
Blue Line: QQQ
You can check out the original Reddit post by clicking the above images.
Obviously, there is a massive timing component and market regime risk to holding highly leveraged instruments. This is what I see as the biggest risk within this system that the backtest doesn’t necessarily reveal.
Finally, the last risk I’d like to discuss is the inherent selection bias using the TQQQ ETF. The Nasdaq 100 has performed exceptionally well the past 15 years. So, applying 3x leverage to that performance is going to result in even more phenomenal performance.
When creating a strategy that holds a few ETFs, you aren’t going to select the ETFs with the worst track record; you’re going to select the ETFs with the best track record. This leads to a selection bias where we pick things that have performed the best in the past, assuming that this will continue into the future.
While this assumption can cause backtested results to overstate performance compared to the results we may see in the future, I don’t believe it is the worst bias in the world.
Why do I not think this bias is the worst?
Well, it’s not great, but it’s not the worst.
I’ll illustrate with an example:
Strategies which trade momentum use this exact assumption to extract profits. These strategies assume that past performance will continue into the future, thus momentum systems buy assets that have been performing well, expecting that performance to continue.
That’s basically what we are doing with the TQQQ, looking at the historical performance and assuming that will continue into the future, just like how a momentum system would work.
The difference comes when these momentum strategies end up selling. When the assets the momentum system buys do not continue their performance into the future, the system will sell the position for a relatively small loss.
Whereas with the original two-ETF strategy, the allocation is static. If the TQQQ begins to degrade in performance in the future, there’s no exit rule to not own the TQQQ ETF—you’re simply holding it to zero.
Hence, the assumption that momentum persists into the future is a reasonable one that’s backed by research, but if the Nasdaq 100 starts to underperform in the future, there is no exit rule in the original system to sell and move on to better opportunities.
Another potential issue is the volatility decay from using leveraged ETFs. Volatility decay is a function of rebalancing within the ETF, where rebalancing causes a slight decay in price from day to day. When a leveraged ETF experiences sideways or down markets, the decay can be greatly exacerbated.
Notice how the QQQ ETF has made new highs in 2025 after the 2022 and 2023 bear market, but the TQQQ ETF is yet to break to new highs. This is the volatility decay in action.
QQQ Performance:
TQQQ Performance:
How I Think About Utilizing Others System Ideas::
What I want to do now is try to take the system originally shared by The Algomatic Trading Database to the next level. I will attempt to reduce some of the risks from the system, as discussed above, while also keeping a similar or better performance profile.
I also want to attempt to find a way to increase the backtest period such that it starts pre-2008. This makes it so I can include some more adverse market environments in the testing.
I was pretty excited to write this article because I loved the premise of the original system that The Algomatic Trading Database shared. I was eager to dig in, tear the system apart, then rebuild it with my own twist on it.
I never blindly take trading systems I find online and implement them into my portfolio.
I always do my own research to validate ideas for myself. Then I add my own twists and creativity to every system idea. If I don’t validate an idea for myself, I have no way to trust that the system is actually real, and I won’t follow the system because it doesn’t have my ideas and preferences baked into it. I encourage everyone to do the same.
I will outline what was going through my mind as I was deconstructing then reconstructing the original system, along with the rationale for each change I made to the original system so that you can learn my thought processes.
Let’s start breaking things…
Constructing The TradeQuantiX Version Of The System:
Now let’s tear the original system apart and build a new version of the system. I will leverage many of the good qualities and remove some of the bad qualities from the original system. In the end, I will have a system unique to me with my preferences. Below, I discuss my thought process and what I changed from the original system.
While I appreciate that the original version of this system was extremely tax-efficient, only rebalancing once a year, and it was extremely easy to operate, only holding two ETFs, and it was generally simple, I’m going to add a little bit more complexity.
Now, anyone who knows me or has read any of my articles knows that I am against complexity. While that’s generally a true statement, in reality, I think complexity is a trade-off.
If the increase in complexity leads to an increase in robustness and decrease in risk, then the extra complexity may be warranted. If the added complexity hardly moves these metrics, then the added complexity is not warranted and should be removed.
The complexity that I will add will both decrease the risk while also increasing the robustness of the system, and thus I believe the complexity is warranted in this case. You don’t have to agree with me here, but that is just my reasoning.
First, I’d like to add a little bit more diversification to this system. The original system held two ETFs; I would like to increase that to five ETFs. The ETFs that I would like to include are:
QLD (2x leveraged Nasdaq 100)
GLD (gold)
TLT (bonds)
DBC (commodities)
BTAL (market neutral, short-beta)
Preferably, I would add a commodity trend-following ETF, like KMLM instead of DBC, but the price history on trend-following commodity ETFs is not as long, with most having just a few years of price history. This is not long enough to have a meaningful backtest, so DBC will have to serve as a proxy.
Also, I would add a Bitcoin ETF, but again, the price history on these ETFs is not very long. While I can get a synthetic price history pretty easily to test how Bitcoin would have performed, I don’t believe the future of Bitcoin will have as violent growth as the past, leading to an inflated backtest result.
That said, I do think having some sort of Bitcoin exposure in the future could be a good hedge against inflation; so if I traded this system, I would probably add BTC, but for this article, I will leave it out of the system. I’ll digress on Bitcoin because I know sometimes it is a controversial topic.
You’ll notice that instead of TQQQ, I am changing to use QLD, which is a 2x leveraged Nasdaq 100 ETF as opposed to a 3x leveraged Nasdaq 100 ETF. What this does is reduce some of the inherent risks of using leverage while also still allowing me to get some of the return stacking effect. This change will also reduce some of the volatility decay that is experienced with leveraged ETFs. The lesser the leverage, the less the volatility decay.
Also, the QLD ETF had an inception date earlier than TQQQ, around 2006. This allows us to test through the Global Financial Crisis in 2008, which is an added bonus.
Adding some of the other sectors like bonds, commodities, and hard assets, like gold, expands our diversification and helps the portfolio be more prepared for different macro market environments in the future. Hence why I added the extra diversification.
I also ended up using a volatility-based position sizing method. I cannot expect different asset classes to have the same magnitude of price moves. Thus, adjusting for volatility normalizes the risk contribution of each asset class to the portfolio. You can read more about volatility targeting in this article here:
Premium Content Vault
Volatility Targeting 101: Enforcing Equal Risk
TradeQuantiX
·
April 28, 2025
or a long time, I opposed volatility targeting. Every trading system I built used simple equal-weight position sizing. If a system held 10 positions, each received a 10% allocation. It was simple, straightforward, and it worked. But I was naïve about what volatility targeting truly is and what it achieves. Here’s my old thought process:
Read full story
And lastly, while the original system was a simple buy-and-hold with a yearly rebalance, I’m going to add a market risk timing filter to the system. This makes it more of an actively traded, tactical asset allocation type of system.
All I’m going to add is a rule specifying the asset’s close has to be above the 200-day moving average for entry, and below the 200-day moving average for an exit. That’s it, nice and simple.
I did not apply this 200-day moving average trend timing rule to the BTAL ETF, but it is applied to all other assets. I did not apply the trend timing rule to the BTAL ETF because I see this ETF as pure diversification and non-correlation that I want to be exposed to at all times. The purpose of this ETF is not to make money but to reduce volatility of the whole portfolio. Thus, we will use all other assets to make the portfolio gains, and use the BTAL ETF to diversify the risk and lower the volatility of the portfolio.
I’ll still have a yearly rebalance built into the system, just in case an asset has been held for a long time and the position sizing has gotten unbalanced.
Finally, to reduce noise, I will make it so that the system only trades weekly. Every Monday, signals for new entries or exits are evaluated, rather than intra-week. This makes the system a little easier to trade and less prone to whipsaws where an asset pops above the 200-day moving average then falls back below a couple days later.
The results based on all of the updates and modifications that I made to the original system can be seen below:
Red Line: SPY Benchmark
Blue Line: TradeQuantiX System
One thing I really like about this portfolio is the outperformance during the 2008 market crash as well as during the 2022 and 2023 bear market. While the system outperforms during bear markets, there was some underperformance during some of the bull markets.
You can’t always win them all. The idea here is to get as much diversification as we can in a robust way, not have a system that makes money every single week.
I also have a plot showing the individual contributions of each ETF to the overall portfolio. You’ll notice a lot of ETFs have pretty bad performance at times, while at other times the performance really skyrockets. You never know which asset class will start to perform well, hence why I wanted exposure to multiple asset classes.
You can see how the QLD 2x leveraged Nasdaq 100 ETF is making up the majority of the returns. Then, the other asset classes kick in when equities underperform.
One way to take this system to the next level would be to have a way to choose between different equity ETFs over time. Maybe in the future the Nasdaq 100 will underperform and another non-technology sector will outperform. Or maybe another global stock market in general will outperform the US.
Either way, the next step I would implement would be a way for the system to dynamically choose what equities to be exposed to, in order to reduce the risk of US equities or the Nasdaq 100 underperforming in the future.
For those purely against leverage, we can also test the same portfolio but with the QQQ ETF (1x Nasdaq 100). The returns of this portfolio won’t be as good, but for the very risk-averse, it may be a better option.
While returns suffer a bit, you still get some good diversification during adverse market environments. Due to the uniqueness of the performance profile during bear markets, this system could almost serve as a good hedge within a broader portfolio of multiple trading systems.
If you like the premise of this trading system, then check out my 3-part research series on All Weather Portfolios, where I test multiple different ETF-based portfolios:
All Weather Portfolio Research: Part 1
TradeQuantiX
·
November 19, 2024
I’m not really sure why but I’ve had an on and off fascination with ETF trading systems in the past year. To most people, ETF trading systems probably seem boring, but boring can still be a good impl…
Read full story
Pros And Cons With The TradeQuantiX Version:
Now let’s discuss some of the pros and cons associated with all the changes I made to the original system. We’ll first start with the pros.
The first pro is the addition of the market timing filter, which allows us to better avoid adverse market downturns. While not perfect, it does help us avoid events like 2008 and potentially similar adverse events in the future.
There’s no guarantee that the 200-day moving average timing filter will always work, but I feel more comfortable using it than not.
Another pro, the increased diversification helps the portfolio during different market environments, such as inflationary or deflationary markets. The diversification also reduces some of the risk of ETF selection bias. Adding more diversifying assets for the sake of diversification and non-correlation reduces the likelihood of cherry-picking the best-performing ETFs historically.
Finally, the last pro is the mitigation of some of the risks inherent to holding leveraged instruments. Reducing the leverage from 3x to 2x Nasdaq 100 will reduce the risk of blowups due to market sell-offs, as well as reduce the impact of volatility decay. Though any use of leverage is risky, I am much more comfortable with a 2x leveraged ETF than a 3x.
Now, we’ll move on to some of the cons.
This system is significantly less tax-efficient than the original system. While not every country is the same tax-wise, in the US, the original system would have fallen into the long-term capital gains tax bracket, which is the lowest tax bracket. This new version of the system would likely fall into the short-term capital gains tax bracket for most trades, which adds a little bit more to your tax bill every year.
It’s your risk; it’s the government’s reward.
This higher tax bill is due to the implementation of the market timing switch, where the system jumps in and out of the markets more frequently. It’s all a tradeoff though. The system buys and sells more quickly, but in return, the system has less inherent risk to downside volatility events. It’s a trade-off of taxes versus downside risk. You can’t always optimize for both.
Another con is the increase in complexity and the week-to-week management of the system. While the original system only required you to log into your broker and update the allocations to the two ETFs once a year, this new version requires you to sit down in front of your computer and potentially update trades every single week—a potential 52x increase in week-to-week system maintenance.
This increase in complexity can also lead to errors. The more active a system is, the more opportunity you have to make an error, like missing an exit signal or entering the wrong position size; such as adding an extra zero and taking on 10x more exposure than you planned.
The TradeQuantiX version of the system has a lot of improvements, but still has some drawbacks. I don’t believe any system will ever be perfect, but we can try!
I invite you to see what you can improve further with this system; the code is at the end of the article!
Commenter Concerns With The Original System:
While reading the original post from The Algomatic Trading Database, I noticed there were many positive comments, but there were also some comments expressing concerns with the strategy.
I would like to directly address these concerns. I mean all of my responses with the utmost respect and gained a lot of insight from reading about people’s concerns with the original strategy.
Now, I’m sure The Algomatic Trading Database is fully aware of all of the risks I have listed in this article and made by other commenters. All The Algomatic Trading Database was trying to do was show the power of simplicity, where simple ideas can generate outsized results. He recognizes that this strategy has its limitations and risks and should not necessarily be traded as is. No idea found online should be traded as is; you always need to do your own homework and research to validate a system for yourself, then apply your own methodologies to how the system operates.
The first concern made by some commenters I would like to address is the concern about the use of the 3x leveraged ETF, explaining that this is likely to have a blow-up-type event in the future during the next market crisis. There was also concern about the volatility decay with the 3x leveraged ETF, where the performance would suffer during sideways market periods.
While these are valid concerns, and I agree with them, The Algomatic Trading Database was not saying to trade this system as is, but rather was showing how you can implement simple ideas and get interesting results. I have also considered this concern in the implementation of the TradeQuantiX version of the system by removing some of the inherent leverage from the system by using only a 2x leveraged ETF, rather than a 3x leveraged ETF.
Another concern was that the system was overly simple. I think this is somewhat of an interesting concern; in my eyes, generally, simplicity is better. I really like the simplicity in the original system; I thought it was very elegant. That said, I think where this concern of simplicity was coming from was that the original model maybe didn’t account for left-tail-like events or major economic regime shifts—a too simplistic view of the world, per se. Again, this is a valid concern, but I have attempted to address this concern by implementing more diversification into other assets that perform during different market regimes. I have also implemented a market timing filter in attempts to avoid left-tail-like events in the future.
Another concern is the short backtest period, only going back to 2011 and hardly experiencing many negative market events. I did my best here to increase the backtest period to 2007 so that I could include the 2008 Global Financial Crisis bear market. While I would prefer to go even further back in time, I can’t reliably test further back than 2007 because most ETFs used did not exist yet.
The last concern was tax implications. Where rebalancing yearly would trigger a taxable event. While this tax event would be at a long-term capital gains rate, you would still have to pay taxes on any profits realized from the system rebalance every year. I did the exact opposite of addressing this concern, where I made the tax implications much worse in the TradeQuantiX version of the system. Though I made the tax situation worse, I made the system much more robust and with much less inherent risk.
You can’t always win them all. A lot of times, implementing a solution in one aspect makes another aspect worse. In this case, removing risk from the system and adding diversification benefits caused us to end up in a worse position tax-wise.
All of these KPIs exist on a sliding scale, and you can never satisfy all KPIs but rather optimize for the best solution for each KPI. I would much rather have a more robust, less risky, and more diversified system but pay a little bit more in taxes than optimize my tax status while trading a much riskier system.
Conclusions:
All in all, I think the system shared by The Algomatic Trading Database was a really interesting idea and worthy of this exploration. While the original system had its limitations, The Algomatic Trading Database was not publishing this system as a finished idea, ready to trade, but rather to show the power of simplicity. The system shared is a great starting point for you to implement your own ideas, like a foundation to build off of, and that’s exactly what we did here.
In this article, I showed you how to take an interesting idea, tear it apart, add your own critical thinking, then put it back together; resulting in a new and unique trading system.
I invite you to take any trading system shared online (mine included), tear them apart, assess based on your own vision of risk and robustness, account for said risks and add more robustness, and then build the system back together, implementing your own assumptions and improvements, making the system entirely your own. This is how I do things, and it’s the best way to become a qualified system developer.
Oh, and if you haven’t already, check out
The Algomatic Trading Database
for more fantastic trading system ideas!
Algomatic Trading Database
A library of simple algorithmic strategies and guides complete with code and backtests—delivered monthly by Algomatic Trading.
Do you have ideas/suggestions for future articles? Let me know what you want to read about by clicking the button below and submitting your suggestions. Your suggestions are greatly appreciated as they help tailor this newsletter to what you want to read about.
Start Survey
Disclaimer
The information and services provided by the Systematic Trading with TradeQuantiX newsletter are for educational and informational purposes only and do not constitute financial advice, investment recommendations, or guarantees of trading performance. Any information provided is general in nature and does not take into account your individual circumstances. Trading involves significant risks, including the potential for substantial financial losses, and past performance is not indicative of future results. The information is provided ‘as is’ without warranty of accuracy or completeness. All decisions and actions based on the information provided are the sole responsibility of the reader. You should seek independent professional advice before trading. The Systematic Trading with TradeQuantiX newsletter is not liable for any losses, damages, or outcomes resulting from the use of this information or our services.
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
