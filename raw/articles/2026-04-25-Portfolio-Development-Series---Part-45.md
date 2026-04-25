# Portfolio Development Series - Part 4.5

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-28e

**发布时间**: Aug 19, 2025

**抓取时间**: 2026-04-25 09:04:25

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 4.5
Survivorship Bias! We Need To Fix It!
TradeQuantiX
Aug 19, 2025
∙ Paid
9
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is an article I was not expecting to write as part of this series; hence it being called part 4.5. I made a mistake in the previous part 4 article of this Portfolio Development series.
After I posted the previous article about creating a US momentum trading system, a subscri...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 4.5
Survivorship Bias! We Need To Fix It!
TradeQuantiX
Aug 19, 2025
∙ Paid
9
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is an article I was not expecting to write as part of this series; hence it being called part 4.5. I made a mistake in the previous part 4 article of this Portfolio Development series.
After I posted the previous article about creating a US momentum trading system, a subscriber was kind enough to point out to me a very subtle survivorship bias within the system. Now, don’t freak out, I have fixed the system and it still works just fine, the updated code will be provided at the end of this article.
Since I am in this awkward position, I figured I should make the most of it and use it as an opportunity to discuss mistakes in system development. In this article, I want to:
Discuss the mistake in the system
Discuss why it matters
Discuss how it could have been avoided
It’s important not only as a learning opportunity but to also point out that even someone who has been doing this for years can still make mistakes!
If you missed the previous article, check it out here. There is still a lot of informative content aside from the mistake!
Premium Content Vault
Portfolio Development Series - Part 4
TradeQuantiX
·
August 4, 2025
In this fourth installment of the portfolio development series, I will create a long-side momentum system focused on US mega-cap stocks. In my opinion, this is the bread and butter, the meat and potatoes, of a well-rounded systematic trading portfolio.
Read full story
The Survivorship Bias Mistake:
The coding mistake within the momentum system was within the breadth filter. The current breadth filter logic is as shown below:
BreadthFilterThreshold: 0.5	
BreadthFilter1:	#Sum InOEX
BreadthFilter2:	#Sum C>MA(C, LongTermLookback)
BreadthFilter:	BreadthFilter2 / BreadthFilter1 > BreadthFilterThreshold
In English, this code was meant to:
Sum the number of stocks currently in the S&P 100 index
Sum the number of stocks in the S&P 100 currently above the 200 day moving average
Only take a trade if 50% of stocks in the S&P 100 are above the 200 day moving average
The survivorship bias issue occurs in step 2. I missed a conditional to only sum the number of stocks above the 200 day moving average if they are a constituent of the S&P 100 at that point in time in the backtest. Accurate historical constituency is key.
Instead, this rule was checking for 200 day MA uptrends in all stocks currently in the S&P 100, previously in the S&P 100, and to be added in the future to the S&P 100.
This issue is a mix between what's called survivorship bias and a future leak. The breadth rule was using data in the calculation that would not have been available at that point in time.
This is obviously no good, hence why I need to fix it. This can severely skew results, and survivorship biases and future leaks are generally some of the worst biases in backtesting. Luckily, the impact to the system is minor, but more on that in a bit.
It is why it is extremely important to have an accurate index constituency time series. This makes it so a strategy can know what stocks were in the S&P 100 every single day of the backtest. In this case that is what the
InOEX
function does in the RealTest code.
Survivorship bias and future leaks can wreak havoc on live trading results. A backtest with survivorship bias/future leak may look fantastic, but once you go live your results are slowly going to degrade over time.
This is because during live trading we don't know what the future holds, so the system is only going to be using the current data. But as time goes on, the system will be subtly adjusting it's historical performance as new future information is known. The history of the backtest will be “repainted” as some call it.
You’ll notice that some of your live trades inexplicably change. You may also notice that your live results look a lot worse than the backtested results over the same period. It’s a slow and subtle degradation in between live and backtested performance.
For example, let’s say a handful of new stocks were added to the index in 2021. With a future leak/survivorship bias, the breadth filter calculation is going to include the stocks that were added to the index in 2021 for all years prior to 2021 as well. But before 2021 we would not have known those stocks were going to be added to the index yet. The system was making decisions based on unknown future data.
The equity curve will essentially be constantly changing with every stock that is added to the index. The back test will not be static, it will be a constantly moving target that is impossible to hit because you don't know the future; but the backtest does.
Luckily The fix is relatively straightforward. All I need to do is add the conditional to check index constituency in the rule that calculates if the close is above the moving average.
BreadthFilterThreshold: 0.5	
BreadthFilter1:	#Sum InOEX
BreadthFilter2:	#Sum If(InOEX, C>MA(C, LongTermLookback), 0)
BreadthFilter:	BreadthFilter2 / BreadthFilter1 > BreadthFilterThreshold
These are the subtleties in back testing that are really easy to mess up. I've been doing this for over 5.5 years now and I still sometimes make subtle mistakes like this, everyone does.
Luckily the mistakes have reduced over time but obviously from time to time they still creep in. This is why it is extremely important to double check your work and if you have a second pair of eyes to look over your system code, that never hurts as well. Especially when the mistakes are not obvious, such as this one.
Removed Survivorship Bias Results:
After implementing the fix to remove the survivorship bias/future leak and ensure a proper historical index constituency, I re-ran the backtest. Shown below are two backtests comparing the original results with the survivorship bias free results.
Original US Momentum System - Survivorship Bias In Breadth Filter:
US Momentum System - Fixed Breadth Filter, Survivorship Bias Free:
Luckily, the results actually got better after removing survivorship bias. This is not common, I’ll reiterate that we got lucky. Returns increased by 1% and drawdown decreased by 5%.
The results got better likely because he breadth filter was being flooded with the price action of irrelevant stocks. A stock that joined the index in 2015 was being used to calculate breadth in 2000. Basically there was a lot of non-useful information being fed into the breadth filter, making its result more noisy.
Yes, future data was being used, but in this case that future data wasn’t actually that helpful to the system. It’s like cheating on a test by getting a hold of the answer key, but the answer key was for an outdated version of the test.
I decided to check and see if the breadth filter was even needed. I ran a quick optimization on the breadth filter threshold. Breadth threshold being defined as the percentage of stocks above the long term moving average within that index. The results are shown below:
Sharpe vs. Breadth Threshold Value:
ROR vs. Breadth Threshold Value:
Max Drawdown vs. Breadth Threshold Value:
Number of Trades vs. Breadth Threshold Value:
The Sharpe and rate of return are basically unchanged until the breadth threshold becomes 0.5 or so. Then the Sharpe and ROR drop off in terms of performance. Max Drawdown also follows a similar trend. Also, if you look at the number of trades, that drops off a cliff at the same rate.
This tells me the breadth filter is essentially just choking the system. It doesn’t do anything until after a threshold of about 0.5. Then for values higher than 0.5, it’s just reducing the number of trades, decreasing ROR and Max Drawdown proportionally. Thus, I am inclined to remove the breadth filter all together, it doesn’t appear to be adding to the system.
Avoiding This Issue In The Future:
There's actually another step that could have been taken that would have prevented this mistake from happening in the first place. In my system development process, I have a step where I ensure the significance of each rule in the system.
After I’ve finished developing the system, I go rule by rule and ensure that its contribution to the system performance actually matters and that the rule deserves a place in the system. For whatever reason, with this particular system, I forgot to do this step. I apologize for that.
What I’ve realized is that this breadth filter rule actually doesn't contribute that much to the system performance. The index filter and the breadth filter more or less perform the exact same function, and really I only need one within the system.
So, I could completely remove the breadth filter and the system would still work fine. In my eyes, this would be a great solution because it would remove needless complexity from the system.
As I always say, a system should be the simplest viable solution to capture the market effect you're aiming for. In this case I can get more or less the same results without the breadth filter. Removing it makes the system simpler and less complexity leads to less chance of error; and this whole article has outlined how error has already snuck into the system.
So, removing the breadth filter from the system results in the equity curve performance as shown below.
US Momentum System - No Breadth Filter, Survivorship Bias Free:
As you can see the system still performs just fine without this filter. I personally would just trade this version of the system without the breadth filter.
But, in case you want to explore the breadth filters impact more, I have both versions of the code below, with and without the fixed breadth filter. Maybe you’ll be able to find a better way to model it such that it has a more significantly positive impact on the system.
Conclusion:
This article is a great lesson in not only double checking your work but having a second pair of eyes to examine your systems. Luckily, in this case the survivorship bias/future leak in the system actually didn't have too much of an impact, but generally we don't get this lucky.
After fixing the survivorship bias/future leak and then examining the results with and without the breadth filter, it was determined that the breadth filter is needless complexity that doesn't add too much to the overall system performance.
Now that the system is fixed we can move on to the next article in the series which will focus on an ASX trend following system. Special thanks to the subscriber that pointed out this survivorship bias issue and working with me to resolve it.
Do you have ideas/suggestions for future articles? Let me know what you want to read about by clicking the button below and submitting your suggestions. Your suggestions are greatly appreciated as they help tailor this newsletter to what you want to read about.
Start Survey
Disclaimer
The information and services provided by the Systematic Trading with TradeQuantiX newsletter are for educational and informational purposes only and do not constitute financial advice, investment recommendations, or guarantees of trading performance. Any information provided is general in nature and does not take into account your individual circumstances. Trading involves significant risks, including the potential for substantial financial losses, and past performance is not indicative of future results. The information is provided ‘as is’ without warranty of accuracy or completeness. All decisions and actions based on the information provided are the sole responsibility of the reader. You should seek independent professional advice before trading. The Systematic Trading with TradeQuantiX newsletter is not liable for any losses, damages, or outcomes resulting from the use of this information or our services.
Corrected Real Test Code With Breadth Filter:
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
