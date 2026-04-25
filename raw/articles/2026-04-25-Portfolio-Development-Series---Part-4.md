# Portfolio Development Series - Part 4

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-bfd

**发布时间**: Aug 04, 2025

**抓取时间**: 2026-04-25 09:04:21

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 4
US Long-Side Momentum System on Mega-Cap Stocks
TradeQuantiX
Aug 04, 2025
∙ Paid
17
2
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In this fourth installment of the portfolio development series, I will create a long-side momentum system focused on US mega-cap stocks. In my opinion, this is the bread and butter, the meat and potatoes, of a well-rounded systematic trading portfolio.
Momentum is my f...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 4
US Long-Side Momentum System on Mega-Cap Stocks
TradeQuantiX
Aug 04, 2025
∙ Paid
17
2
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
In this fourth installment of the portfolio development series, I will create a long-side momentum system focused on US mega-cap stocks. In my opinion, this is the bread and butter, the meat and potatoes, of a well-rounded systematic trading portfolio.
Momentum is my favorite system type. You jump into the strongest stocks and sell the weakest ones—a simple yet robust concept. Momentum systems allow you to gain exposure to the market's upward bias, creating a solid return stream for your portfolio.
Momentum systems maintain exposure to the markets when they are hot and avoid them when they are cold. This allows our portfolios to experience the best of the good times while avoiding the bad times.
As mentioned in the previous article, each article in this portfolio development series focuses on a different part of the system development process. This keeps the articles engaging and allows me to take deep dives into specific aspects of trading system design and validation. In this article, I will focus on:
The initial planning phase of the system.
Thinking through why and how the system will operate fundamentally.
Building the system from the ground up, one piece at a time.
Here is a sneak peak of where we will end up in this article: a momentum system across three different US market universes.
Let’s get started!
Why Momentum Systems Are Great:
As I mentioned, momentum systems are my favorite.
But why is that?
First, they make fundamental sense, at least to me. If I were a discretionary stock trader, I would buy the strongest stocks during their peak performance periods and sell into strength, capitalizing on the upward move while avoiding the downturn. This is exactly what momentum systems do: they buy the strongest stocks during their strongest periods and then sell them as the momentum starts to cool off.
This trading method aligns with my personality and how I think about the markets, making momentum systems effortless for me to trade. I rarely hesitate to place orders for my momentum systems because I know they seek to get my portfolio involved in the best performing stocks in the market at any given time.
With mean reversion systems, however, I sometimes feel nervous placing trades because mean reversion buys the losers. Mean reversion systems go against how my brain operates. There’s definitely a trader personality type, and my personality type is momentum.
Second, momentum systems, at least the way I develop them, are fairly straightforward to trade.
Identify a small basket of the strongest performing stocks
Buy that basket of stocks
Wait for a week to a couple of months
Re-evaluate the basket of stocks currently held
Sell the laggards
Replace the laggards with the most current strongest performing stocks
It’s a simple yet effective concept.
This means that, day-to-day, there isn’t much work to do with this type of system. Once you establish the portfolio of potential outperformers, there’s generally a quiet period where you let these outperformers do their thing.
After a week to a few months, you re-evaluate and adjust the momentum portfolio as needed; ensuring you’re holding only the best and strongest stocks again.
Check out the example momentum trade in the image above. That trade just feels good. It entered during a moment of low volatility and then followed the explosive trend until it started to settle down. These are my favorite types of trades.
A Tangent On Periodicity and Trading Frequency:
All the momentum systems in my personal systematic trading portfolio use a monthly periodicity. This means I re-evaluate the momentum portfolio at the beginning of every month, buying the winners and selling the laggards, then do nothing for the rest of the month. My momentum systems place trades only 12 times a year.
The relatively slow trading pace of momentum systems makes them ideal for someone with a busy lifestyle; or someone who prefers less action in their systematic trading portfolio. Some people may not want to place trades every day, which I understand, as it can be a lot of work especially if you manage multiple trading systems.
A person with this preference might opt for a portfolio of systems operating on weekly or monthly periodicities; where trading activity occurs only on weekends or at the end of the month.
You don’t need a highly active systematic trading portfolio that places trades daily. You can adjust the trading frequency by developing systems that operate on higher periodicities.
Don’t want to trade every day?
Develop systems that trade weekly, monthly, quarterly, or even yearly.
Additionally, higher timeframes often have less noise in the data, which can lead to stronger signals.
That said, if you have order management software, as I do, periodicity becomes less relevant. Hypothetically, I could place hundreds of orders daily and it would be no different in terms of workload than placing one order a day.
This is because my systematic trading portfolio is 80% automated, and I use order management software to place and track all my orders. The computer does all the annoying management and tracking work, I just do a quick review to ensure everything looks reasonable. This makes my portfolio theoretically infinitely scalable and allows me to trade various periodicities without issues.
I’ll digress from this tangent about periodicity, trade frequency, and my portfolio. I just wanted to highlight that a trading portfolio doesn’t have to be highly active. You can use different system types on various periodicities to make the portfolio slower and less frequent in its day-to-day activity.
Don’t throw a system away because it trades too infrequently, sometimes infrequent trading has a real edge.
Defining Momentum And Other Market Effects:
Momentum is a well-documented market effect that has been studied extensively. The momentum effect has persisted in markets for centuries and continues to do so today. Because momentum is a real market effect, retail traders like us can capture it.
But what does momentum mean?
Sure, buy stocks when they’re rising and strong, and sell them when they’re no longer strong; but how do you convert that description into quantifiable rules or equations?
Saying "momentum" is vague and can have many interpretations. We need to quantify it, and that’s the tricky part. Thus, the first step in developing this system is figuring out how to measure and quantify momentum.
So, we need to define momentum.
But what else other than momentum do we want to incorporate into this system that also needs defined?
Can we get a two-for-one?
Yes, I think we can. I also want to incorporate the low volatility effect into this system. If you’re unfamiliar, the low volatility effect is another well-studied market phenomenon that persists over time.
Research shows that stocks with lower volatility outperform those with higher volatility on a risk-adjusted basis, meaning low volatility stocks offer more return for a given amount of risk. You can read more about the low volatility effect in the article below where I developed a system exploiting this effect:
Premium Content Vault
Trading System Investigation Series 3
TradeQuantiX
·
June 3, 2025
I don’t know about you, but I’d like to outperform the S&P 500 over the long term. Outperformance can be on the absolute returns or the risk adjusted returns (or both). In this article, we are going to explore a trading system that has delivered slightly better than S&P500 returns with less than half the drawdown.
Read full story
Thus, trading momentum with a bias toward a basket of lower-volatility stocks should improve risk-adjusted returns. Stacking multiple market effects is powerful because it builds proven, profitable methodologies into the trading system.
But, as with momentum, we must ask:
How do we define low volatility?
Qualitatively, low volatility means stock A fluctuates less than stock B. We need to quantify the magnitude of this fluctuation. Once we do, we can leverage the low volatility effect by biasing the system toward stocks that offer better risk-adjusted returns.
Universe Selection And Regime Filtering:
Two other major components of this system that need to be defined before we begin development:
The universe the system will trade
The regime filtering, if any, to avoid unfavorable market periods.
Universe Selection:
Starting with the universe, large and mega-cap stocks tend to exhibit momentum with more stability and reliably than smaller-cap stocks. This isn’t to say smaller-cap stocks lack momentum, but their momentum is often more erratic, noisy, and less predictable, at least in my experience. I’m sure there are systematic traders out there with killer momentum systems on small cap stocks, but I personally have struggled here.
Mega-cap stocks exhibit momentum for several reasons. First, they represent businesses which are considered the best of the best, consistently growing with strong fundamentals. Stocks with strong fundamentals are the ones that large funds focus on. These stocks also have high liquidity, allowing large billion-dollar funds to scale into positions over time. This scaling in of large positions gradually increases the stock price over time, and creates an upward trend.
There’s also a herding effect, where stocks performing well continue to do so. As people learn about a stock’s performance, they want to buy in to join the action. Mega-cap stocks, often household names covered by the mainstream media, are familiar and comfortable for everyday investors. Investors see these big name stocks they’re familiar with exhibiting a lot of momentum, so they jump on the train. Like with large funds, this herd-like behavior drives more money into the stock, boosting its price and momentum over time.
Mega-cap stocks are also included in major indices like the S&P 500, NASDAQ 100, or Russell 1000. ETFs and mutual funds representing these indices make up a significant portion of investors’ retirement and buy-and-hold portfolios. These accounts often deposit regular sums of money into these ETFs and mutual funds, which flow into the mega-cap stocks, fueling further their consistent growth.
Due to these fundamental effects, momentum persists consistently and cleanly in mega-cap stocks. Thus, this momentum system will be designed to trade a mega-cap stock universe.
The universes I’m considering are the NASDAQ 100, S&P 100, and Russell 1000. But, rather than picking one universe, I’m considering letting the system trade all three universes to diversify risk across sectors.
Many systematic traders focus on developing trading systems only on the NASDAQ 100. The NASDAQ 100 consists of the top 100 technology-oriented stocks, resulting in significant tech exposure. The tech sector has historically shown strong growth, and I don’t foresee it slowing down. That said, I want exposure to other sectors too, in case tech underperforms in the future.
The reason why many systematic traders focus on developing trading systems only on the NASDAQ 100 is because of the very good historical performance. Only trading the best universe is a selection bias. To get around this bias, we will force the system to trade multiple universes.
The S&P 100 overlaps some with the NASDAQ 100 but is much less tech-heavy, with a more even distribution across US sectors. This allows exposure to momentum in other areas of the market. Momentum shifts; sometimes it’s strong in tech, sometimes in healthcare or energy etc. Trading the S&P 100 ensures access to the top 100 US stocks across many sectors, positioning the system to capture the hottest sector at any given time.
The Russell 1000 provides exposure to other large stocks just outside the top 100. It includes the top 1000 stocks by market capitalization, expanding our breadth even further than the S&P 100.
In short, we will focus on momentum within mega-cap stocks across multiple US index universes, providing access to various market sectors. This ensures the system has a diversified basket to choose from, allowing it to dynamically capture momentum in the hottest sector.
This also helps prevent selection bias, avoiding only trading the system on what has historically been the strongest universe; because we don’t know which universe will be the best performing in the future.
Regime Filtering:
The other component that needs to be defined for the system is regime filtering, a much debated topic. Some systematic traders oppose regime filtering; others don’t. I personally use regime filtering, but am cautious about implementation.
It’s easy to overfit regime filters. Many traders apply indicators to a market index and brute force optimize for the best result, which I strongly oppose. Using a regime filter on a market index representative of your trading universe is fine, but excessive optimization is risky due to limited data points.
Optimizing an indicator on one time series can yield great results quickly, but they are likely not robust. The limited data points in a single index time series don’t justify such precise fitting. A simple, blunt, unoptimized regime filter is much better than a complex, precise one; at least from a robustness point of view.
From the point of view of having the most beautiful looking backtest, a very optimized regime filter will look much better, but these results will certainly not hold up in future live out-of-sample.
I’m a big fan of intentionally diversifying regime filters. If one system uses a specific regime filter, I’ll purposely use a different regime filter in another system. Or I’ll use the same regime filter but with an intentional selection of different parameters.
This spreads my risk across regime filters, allowing gradual scaling in and out as markets shift from risk-on to risk-off environments. This is better than being fully in or out of the markets at once, just because your one regime filter in all your systems triggered.
To me, being risk on or risk off is a gradient, therefore I treat it as such. This ensures some systems turn off quicker and at different times than other systems.
For this momentum system, I’ll need to determine what regime filter to use. I’m considering two types of regime filters:
A pure price action-based regime filter → An indicator on the index timeseries
Or a market breadth regime filter → A cross sectional measurement of all stocks within the index
I’m unsure which will be sufficiently robust and give good results, so I’ll investigate both during system design. I may even end up using both regime filter types, who knows.
I really like breadth filters because they tend to be more robust as they use more data points, analyzing the timeseries of all stocks within the universe. This allows the filter to have many more data points in the regime identification.
System Design and Implementation:
There are many other important aspects  within a trading system, but the components above-market effects (momentum and low volatility), trading universe, and regime filtering-make up about 80% of the system operation. These components allow the system to pick and choose what stocks to buy and sell.
Another super important aspect of system development that has not been addressed yet is position sizing. Position sizing I see almost as a second layer. We need a way to quantify and measure a trading signal first so we know what to buy and sell, but from there it’s all position sizing.
For many years I was in the “position sizing is overrated” camp. After many many hours of research, I have since proved myself wrong. Position sizing is the most important part of system design after the definition of the entry signal.
You need a signal to warrant a position, but as soon as the system says be risk on, the next question is: By how much? How aggressive should we be risk on? Are we scaling in or out? Are we using leverage? So many questions to answer on position sizing.
Rather than trying to dive super deep into position sizing theory here, I’ll let the results show for themselves a little bit later in the article. I’ll show how I built up the system, piece by piece, and you’ll see how position size layering really enhances the systems risk adjusted performance.
If you want to learn more about position sizing, you can check out this article linked below. I also plan to explore position sizing more in future articles.
Premium Content Vault
Volatility Targeting 101: Enforcing Equal Risk
TradeQuantiX
·
April 28, 2025
I live by the mantra “keep it simple, stupid.” I apply this not only to my personal life and day job, but also to my systematic trading. At every step of my trading processes, I strive to eliminate unnecessary complexity. Overcomplicating things is the enemy of system stability and robustness, it also opens the door to mistakes.
Read full story
After spending about five hours on system design, I developed a system I was satisfied with. I worked hard to incorporate original ideas, as I’ve built many momentum systems before, and they can become redundant. The rules I finalized can be read from the code at the end of the article. But we will also walk through, rule by rule, and see the impact on the system performance in just a bit.
I built this system from the ground up, starting with the most basic concept and iterating from there. The foundation and starting point for the system was a momentum ranking factor that incorporates volatility. The system ranks all stocks in the universe, and the top 10 are selected for investment. The ranking factor used is shown below:
0.4 * ROC(C, 63)/HVOL(63) + 0.2 * ROC(C, 126)/HVOL(126) + 0.2 * ROC(C, 189)/HVOL(189) + 0.2 * ROC(C, 252)/HVOL(252)
Where ROC is the rate of change over x days and HVOL is the volatility of the stock averaged over x days.
This ranking factor considers both momentum and volatility, using different quarterly lookbacks. This approach, inspired by Investor’s Business Daily, is a stable way to measure historical momentum. My only twist is I normalized momentum by volatility. This ensures both the momentum and volatility effects are being built into the ranking factor.
I decided to use the S&P 100 universe as my in-sample data, using the date range from 1991 to 2018. 2018 to mid 2025 (today) was used for out-of-sample.
Below I’ll show a series of plots. Each plot will show the results of a new addition incorporated into the system, showing how I built the system from the ground up.
The first plot will show the S&P 100 in-sample dataset with only the volatility normalized momentum ranking factor applied, equal position sizing, and a monthly rotation (all plots will use a monthly rotation).
From there, I add in one new component to the system until the system is finished. The new component will be specified as we go.
See the first plot below for the starting point with only the volatility normalized momentum ranking factor, equal position sizing, and a monthly rotation. We are only looking at the in-sample data for now.
Current Momentum System Rules:
Volatility Normalized Momentum Ranking Factor
Equal Weighted Position Size
Monthly Rotation
The starting returns are 13.5%, better than market average, but drawdowns are massive, on par with the market at 52%. The volatility normalized momentum ranking captures the momentum effect, but there’s nothing controlling downside risk yet. It’s worth noting, the drawdown is actually even worse when the momentum ranking factor is not normalized by volatility.
To make this system more tradable we need to focus on reducing the downside risk. One way to manage downside risk is through position sizing. Remember I mentioned position sizing can have a sizable impact on system performance?
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
