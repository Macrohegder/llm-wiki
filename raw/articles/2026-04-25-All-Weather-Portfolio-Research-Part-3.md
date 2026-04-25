# All Weather Portfolio Research: Part 3

**原文链接**: https://www.tradequantixnewsletter.com/p/all-weather-portfolio-research-part-f13

**发布时间**: Dec 20, 2024

**抓取时间**: 2026-04-25 09:02:21

---

## 摘要

All Weather Portfolio Research: Part 3
Implementing Improvements to the TradeQuantiX All Weather Portfolio
TradeQuantiX
Dec 20, 2024
18
14
Share
Welcome to part 3 of this All Weather Portfolio series! Before we dive into it, let’s just do a quick recap of the previous two articles in the series. The first part of the All Weather Portfolios research focused on coding up and testing already existing All Weather Portfolios found online. We learned a lot doing this but ultimately, traditional All Weather Portfolios were pretty boring in terms of performance and severely underperformed the past few years. From there, I made my own TradeQuantiX All Weather Portfolios where I attempted to take the traditional All Weather Portfolio and make it interesting again. The TradeQuantiX All Weather Portfo...

---

## 全文

All Weather Portfolio Research: Part 3
Implementing Improvements to the TradeQuantiX All Weather Portfolio
TradeQuantiX
Dec 20, 2024
18
14
Share
Welcome to part 3 of this All Weather Portfolio series! Before we dive into it, let’s just do a quick recap of the previous two articles in the series. The first part of the All Weather Portfolios research focused on coding up and testing already existing All Weather Portfolios found online. We learned a lot doing this but ultimately, traditional All Weather Portfolios were pretty boring in terms of performance and severely underperformed the past few years. From there, I made my own TradeQuantiX All Weather Portfolios where I attempted to take the traditional All Weather Portfolio and make it interesting again. The TradeQuantiX All Weather Portfolios increased diversification, reduced drawdown, and increased returns. I explored three variations of TradeQuantiX All Weather Portfolios, one with a static allocation and is always invested, a second with static allocation and a market timing switch, and a third with dynamic allocation and a market timing switch. Those three portfolios looked great and were much more interesting than the traditional All Weather Portfolios. If you missed the previous two articles check them out here:
Originally, I had planned for this to be a two part series, but after some more research and some reader suggestions, I have decided to write a third part to this series. In this article I will start with the tactical asset allocation with dynamically adjusting position sizing (the third all weather portfolio in part 2) and take it another step further. A reminder of what that portfolio looks like:
This portfolio has access to 13 ETFs and rebalances monthly. It also only holds ETFs that are above the 200 day moving average and sells ETFs below the 200 day moving average. The 13 ETFs it can hold are:
QLD (2x QQQ Nasdaq 100)
GLD (Gold)
TLT (20+ Year Treasury Bonds)
SHY (1-3 Year Treasury Bonds)
XLE (Energy Sector)
DBC (Commodity Index)
DBA (Agriculture Commodity Index)
VEU (Global Equity Excluding USA)
XLP (Consumer Staples Sector)
IYH (Healthcare Sector)
VNQ (Real Estate Index Fund (REIT))
BITO (Bitcoin ETF → GBTC used in backtests due to longer price history)
UUP (US Dollar Index)
Subscribe
All Weather Portfolio Improvements To Explore:
What I want to do next is explore more ideas to attempt to create the ultimate All Weather Portfolio. The ideas I will explore in this article are:
Continuous Rebalancing:
Currently the rebalance interval is monthly. But what about weekly? Or rebalance only when volatility changes?
Exposure to Country Specific ETFs:
This was a reader suggestion to allow the portfolio to hold ETFs for individual countries (Japan, India, China, etc.) rather than VEU, which is all countries except the US.
Annualize the Weighting for the Ranking Calculation:
This was a suggestion by a reader
Original ranking metric:
Ranking = ROC(C, 120) + ROC(C, 60) + ROC(C, 30)
Proposed ranking metric to give more weight to ETFs performing well recently
Ranking = 2*ROC(C, 120) + 4*ROC(C, 60) + 8*ROC(C, 30)
Add some Managed Futures ETFs:
A reader suggested to add managed futures ETFs like DBMF or KMLM
A few of these ideas are reader suggested, which I think is fantastic. I am ecstatic that my readers are engaged enough to send me suggestions. So thank you, I will always welcome suggestions, constrictive criticism, and improvement ideas.
To explore these ideas, we will look into each one at a time. We will start with the tactical asset allocation with dynamically adjusting position sizing All Weather Portfolio (the third all weather portfolio in part 2) and try each idea one at a time to understand the impact. One thing to be aware of, I plan to use the entire data series to assess these new ideas. I have considered an In Sample and Out of Sample approach, but given we only have a handful of ETFs and 16 years of history where most ETFs exist (which really isn’t that much to see how the portfolio behaves in different market conditions), it’s very difficult to assess this system with In Sample Out of Sample. I would argue I am better off with a very careful development approach of no optimizing, no tinkering, and focusing diligently on robustness tests. Remember, always do your own validation of an idea. Hopefully after this article, you too can conquer any “weather” event in your trading and always keep your trading portfolio bright and sunny.
Subscribe
All Weather Portfolio Improvement #1 - Continuous Rebalancing:
The current version of the TradeQuantiX All Weather Portfolio only rebalances once per month. If volatility expands or contracts severely during the month, the portfolio has to wait until the end of the month to account for the changes. If we can make the portfolio more dynamic to volatility changes, theoretically this should smoothen the equity curve. One thing we need to be careful of, if we are rebalancing every day we could get destroyed by commissions. Changes to the portfolio are not free, if we want to make a change to the portfolio for any reason we have to pay. So, there has to be a cost benefit to the change we propose, is the change more beneficial and likely to outperform more than the drag of commissions will pull performance down? Well, let’s set a baseline first and compare the original TradeQuantiX All Weather Portfolio to a version where we rebalance every day but NOT account for commissions.
The drawdown is improved when we continuously rebalance. Likely because when an adverse event happens volatility tends to increase. Continuous rebalancing can quickly react to the volatility changes and reduce position sizing fast during high volatility events. Remember, this is assuming no commissions though.
Now, here is the same portfolio that rebalances every day but with the commission structure of Interactive Brokers applied (this is the broker I use).
As you can see, commissions really put a drag on performance if we rebalance every day as opposed to rebalancing monthly. Theoretically, continuous rebalancing is a great idea, but after applying market frictions it actually hurts performance. So maybe daily rebalancing is too frequent, maybe weekly is a better option? Here is rebalancing weekly with and without commissions:
Without Commissions:
With Commissions:
The equity curves are closer but the commission drag is still a little more than I would prefer. Also, we could be needlessly rebalancing, after a week there could be positions that are still relatively balanced in their allocation but we are rebalancing anyway. To avoid this, instead of forcing a time based rebalance interval, let’s have a percentage based rebalance interval. Instead of rebalancing everyday or every week, let’s just rebalance if positions get too far out of wack. So, below I am showing an example were we only rebalance if the position size drifts more than 10% out of balance with the ideal position size.
Without Commissions and 10% Rebalance Threshold:
With Commissions and 10% Rebalance Threshold:
Okay it seems like 10% rebalance threshold is a little too sensitive and we are rebalancing a little too often as we are still getting commission drag. So, let’s make it much less sensitive and move to a 50% rebalance threshold. This should only rebalance positions that have drifted very far from the ideal position size (remember position sizing is based on a target volatility).
Without Commissions and 50% Rebalance Threshold:
With Commissions and 50% Rebalance Threshold:
We are gradually approaching a state of minimal commission drag. A 50% threshold is very large though. It’s almost starting to get to the point where we might as well just stick with our monthly rebalance in the original system. It seems that adding this rebalancing complexity, while seeming like a good idea, is not adding much benefit after accounting for real market frictions. This method may work very well in other systems or on other markets, but for this system I would argue the added complexity is not worth it.
I plan to keep this technique handy because I think I will find a use for it one day. Theoretically, the idea of continuous rebalancing really reduces volatility before adding commissions. With this particular system, the commission drag is just too much, but I will continue to look for a practical use case for this technique.
Subscribe
All Weather Portfolio Improvement #2 - Country Specific ETFs:
This improvement idea I really like because it gives us exposure to specific country equities. Right now, the only non-US equity exposure we have is through the VEU ETF which is global equities except the US. This will give us an average return based on the performance of global equities, but if we could target specific countries that are performing very well, that could help the portfolio a lot, theoretically.
We have to be careful with implementation of adding other countries ETFs though. This is an All Weather Portfolio so we want to be exposed to multiple different asset classes at once. If we add the ability to trade a bunch of country specific equities, you could probably imagine a situation where the system only owned equities and not any of the other commodities the system has access to. This may work out for us from time to time, but if a global crisis like 2008 or 2020 happens again and we are only invested in equities, that could be painful and defeats the purpose of an All Weather Portfolio. So, we likely need to limit the number of equity specific ETFs we can own at once so the portfolio is forced to own a few non-equity ETFs as well.
My initial thought how to do this would be to rank all global ETFs based on performance using the same ranking equation the system already uses:
Ranking = ROC(C, 120) + ROC(C, 60) + ROC(C, 30)
Then take the top few performing equities and tell the system these are the current equity ETFs you are allowed to trade right now. I am not forcing the system to trade these top few equity ETFs, the system could choose to not trade any equities at that point in time. This will prevent the system from buying only equity ETFs and ensure we maintain some level of diversification at all times within the All Weather Portfolio.
Doing a quick internet search, there are are many country specific equity ETFs available. You may choose to add all those ETFs to the system to trade or you may do some sort of down selecting based on geopolitical risks, volume traded, or how far along the country is developed. I asked Grok (the AI on the X platform) to make me a list of country specific ETFs and this is what it gave me:
Argentina
: Global X MSCI Argentina ETF - $ARGT
Brazil
: iShares MSCI Brazil ETF - $EWZ
Canada
: iShares MSCI Canada ETF - $EWC
Chile
: iShares MSCI Chile Capped ETF - $ECH
China
: iShares MSCI China ETF - $MCHI
France
: iShares MSCI France ETF - $EWQ
Germany
: iShares MSCI Germany ETF - $EWG
India
: iShares MSCI India ETF - $INDA
Israel
: iShares MSCI Israel ETF - $EIS
Italy
: iShares MSCI Italy ETF - $EWI
Japan
: iShares MSCI Japan ETF - $EWJ
Malaysia
: iShares MSCI Malaysia ETF - $EWM
Mexico
: iShares MSCI Mexico ETF - $EWW
Netherlands
: iShares MSCI Netherlands ETF - $EWN
Norway
: Global X MSCI Norway ETF - $NORW
Peru
: iShares MSCI Peru ETF - $EPU
Poland
: iShares MSCI Poland ETF - $EPOL
Qatar
: iShares MSCI Qatar ETF - $QAT
Singapore
: iShares MSCI Singapore ETF - $EWS
South Africa
: iShares MSCI South Africa ETF - $EZA
South Korea
: iShares MSCI South Korea ETF - $EWY
Spain
: iShares MSCI Spain ETF - $EWP
Sweden
: iShares MSCI Sweden ETF - $EWD
Switzerland
: iShares MSCI Switzerland ETF - $EWL
Taiwan
: iShares MSCI Taiwan ETF - $EWT
Thailand
: iShares MSCI Thailand ETF - $THD
Turkey
: iShares MSCI Turkey ETF - $TUR
United Kingdom
: iShares MSCI United Kingdom ETF - $EWU
United States
: SPDR S&P 500 ETF Trust - $SPY
That’s a heck of a list to start with! I wanted to understand the liquidity of these ETFs to ensure they were all tradable so I ran a scan to show the ETF liquidity. Below is this same list of ETFs but shows the average turnover and volume over the past 20 days.
Looks like a few of these ETFs have some low liquidity, such as NORW or EPU. I’m thinking we put a liquidity filter in the portfolio that applies to these country ETFs so if liquidity grows or shrinks over time the system can automatically adjust without us updating the ETF list.
From this list, I will remove one ETF based on personal preference. We already have QLD (2x QQQ) in the system so we don’t have a need for any more US based ETFs, so I removed SPY. Other than that all other ETFs remained available for trading.
Then, I ranked the country ETFs based on the performance metric and traded the top three ETFs. That equity curve alone looks like the following:
Very ugly, I’m not sure why momentum does not work anymore on a country ETF universe but it obviously does not. Anyway, I can plug this into the All Weather Portfolio and let the portfolio choose to trade these top three country ETFs if it wants (it is not forced to). The resulting equity curve is shown below.
Yikes, not great. Very volatile and drawdown skyrockets. I have experimented with momentum and trend following on country specific ETFs in the past and I have always ended up with an ugly result. The only way I can think of to improve this is to cherry pick specific countries, which is not ideal. You need a systematic approach to picking which country ETFs to trade, cherry picking you favorites or guessing what you think will do well in the future is a fools game and will likely cause your portfolio performance to crash and burn. So I am not going to explore this avenue further. Some ideas seem good, but end up not working, that’s just part of the game.
Subscribe
All Weather Portfolio Improvement #3 - Annualized Weighting Ranking Calculation:
This one should be pretty quick to test. We just need to update the ranking function the system uses. If there are more ETFs that fit our entry criteria than we have money to invest, the ranking function is used to determine which ETFs to buy. The ranking function function will get updated from:
Ranking = ROC(C, 120) + ROC(C, 60) + ROC(C, 30)
To:
Ranking = 2*ROC(C, 120) + 4*ROC(C, 60) + 8*ROC(C, 30)
What this does is multiply each lookback by a weighting that annualizes the lookback. If there are 252 trading days a year, then the 120 day lookback needs multiplied by approximately 2 to get to 240, which is close enough to 252. The 60 day lookback needs multiplied by 4 to get to 240, and the 30 day lookback needs multiplied by 8. I picked the default parameters not with optimization but rather I just wanted the system to check multiple lookbacks when ranking what ETFs to trade.
The results of the updated ranking function are below:
The results really are not that different. If you think about it, that is a sign of robustness with the strategy. The system is not sensitive to this ranking function, even significant changes to the calculation lead to very similar results. This gives me more confidence that there has not been unintentional overfitting or a lucky parameter choice with the ranking function. I will keep the original ranking function since the annualized ranking function is slightly more complex and doesn't add any benefit to this particular system.
Subscribe
All Weather Portfolio Improvement #4 - Add Managed Futures ETFs:
Another suggestion to improve the All Weather portfolio was to add managed futures ETFs to the list of ETFs the system can trade. I like this idea as Managed Futures are intuitively an uncorrelated return to the rest of the ETFs. The suggested ETFs were DBMF and KMLM, looking at both of these ETFs, they have very similar price patterns but DBMF has a longer price history, so I will go with DBMF to better see the effect on the All Weather Portfolio.
We have to be careful because for the first couple years the ETF has very little volume and the price was erratic. So we will take results during that time with a grain of salt, but it looks like today the volume and price behavior has matured so its likely okay to trade going forward.
Adding the DBMF ETF did not change performance much (remember the ETF is only available 2019 onwards). Though I do like the diversification aspect, so I think I will keep it. The purpose of this All Weather portfolio is to be diversified and uncorrelated to the market, so having a managed futures ETF meets that goal. Also, 4 years of price history is not a significant enough period of time to see the impact on the portfolio, especially since the rest of the portfolio is tested back for 24 years.
As you can see from the correlations of returns for DBMF (far right column), it is almost a zero correlation for all other ETFs. This is exactly what we want for an All Weather Portfolio. Hence, why I am inclined to keep this ETF. If anyone else has ETF suggestions that may be uncorrelated, please let me know.
Subscribe
Final All Weather Portfolio:
Out of all the four changes I tested, I chose to keep one to finalize the TradeQuantiX All Weather Portfolio. The update I have chose to make is:
Add DBMF Managed Futures ETF to the portfolio
Just one update, all the other ideas did not seem to add any value for the increase in complexity. The addition of the Managed Future ETF does not add much complexity and helps us work towards the purpose of this All Weather Portfolio, get as much diversification as possible.
Conclusions:
Not all ideas are as good as they seem. Some ideas feel like they should work, but they just don’t or add more complexity than benefit. That’s okay and it’s part of the system development game. We still were able to slightly improve the system by adding another uncorrelated Managed Futures ETF DBMF. Sometimes if feels like we wasted time going through all these ideas just for most to fail. In reality, it’s not a waste of time, now that you have checked these ideas off the list you are one step closer to an idea that will actually work. Never stop generating and testing ideas, 95% of ideas will fail but that 5% that end up being great ideas are what will make you a profitable trader.
Thanks for reading Systematic Trading with TradeQuantiX! Subscribe for free to receive new posts and support my work.
Subscribe
18
14
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
