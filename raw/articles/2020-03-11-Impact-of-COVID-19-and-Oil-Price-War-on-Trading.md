---
title: "Impact of COVID-19 and Oil Price War on Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/impact-covid-19-oil-price-trading/"
date: "2020-03-11"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Impact of COVID-19 and Oil Price War on Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/impact-covid-19-oil-price-trading/)  
**日期**: 2020-03-11  
**作者**: QuantInsti

---

## 原文

Impact of COVID-19 and Oil Price War on Trading

ByChainika ThakarWith the well-known fact that novel Corona Virus struck China in the first place, it was the economy of China which slowed down and impacted the stock market consequently. Another major event that has hit the stock market considerably further is the Oil Price dispute between Russia and Saudi Arabia.

In this article, pertaining to the current declining market scenario and the simultaneous changes which are taking place with regard to trading, we will discuss various aspects. As far as the impact of Covid-19 and Oil Price War on Trading is concerned, we are taking a look at this situation from the following aspects:

Future Returns After the Drawdown

Trading Strategies in the Current Scenario

Global Impact of Corona Virus and Oil Price War on Trading

Historical Stock Market Crashes

Future Returns After the Drawdown

In this section, we are calculating average future returns based on the data from historical stock market crash scenario. For that, we have taken into consideration the data from a stock market crash in the past. With that data, we have taken out the aftermath of drawdowns in the situation of stock market crash. Let us take a look at what the possibilities are in the near future based on the analysis of historical data of a stock market crash.

Running the above code imports the historical data from yahoo for GSPC stock in January 1990, which gives us the following output:

The output above prints the first five trading days and gives us the values in the stock market in that specified time.

After importing the values, we will calculate the daily per cent change and cumulative returns. Now we will create a function to calculate the average future returns for 5 days, 22 days, 90 days and 252 days. After that, we calculate the running peaks for the cumulative returns and ensure that the value never drops below 1. In the next step we calculate the percentage drawdown of cumulative returns.

Running the above code gives us the following plot in the output:

Now, we will create a column with drawdown values and will be flagging all the peaks of the drawdown series. Following this, we will sequentially add each flag by 1 to get it indexed. And filling NaN values for drawdown with forward value. Ahead, you need to assign conditions that every next drawdown must fall to below -10% from above -10%.

Running the above code gives the following output:

In the above code, we calculate the future returns on the condition that previous drawdown is not equal to current drawdown and then plot the mean of future values. This will give us following results:

Below, we have combined all the codes to give you one code for calculating percentage fall. You can add the details you want the output for accordingly.

Running the above code gives us the future values for NSEI. In this code, you can replace NSEI with your preferred ticker and check the desired results.

The future values for NSEI show as follows:

Perfect! Now, let us move ahead to the Trading Strategies that you can adopt in the current difficult scenario.

Trading Strategies in the Current Scenario

In such a scenario, where the stock market has crashed considerably in the past some time, every trader is looking for the strategy which will get him/her the maximum profits. While there are many trading strategies, in such a tricky situation, there are always some industries that do well. This is so because these industries are helpful to the people in the current crisis.

As traders are facing the worst trading time, there is a good escape by opting for Options Trading Strategy with less volatile stocks (Disinfectants industry). Let us discuss some ways you can use the strategy:

Selling Put Options

We have seen that the market usually returns to its highest point in almost a year following the crash or drawdown. This shows that investors can sell their overpriced puts at this time. Also, it is profitable to accumulate long-term buy and hold positions.

Breakout Strategy

In order to use this strategy, there are two most important things that come under “the management”:

Using Stop losses

Profit-taking

Now,Stop lossescan help you be more on the profitable side, with fewer losses to bear when you are dealing with more than one trade. Since coming out with a small loss is better than bearing a big loss, this works!

And,Profit-takinghelps with the price-action so as to not lose out on profit opportunity in the market. With a breakout strategy, it will be possible to make an action as such.

For instance, you can put an exit order immediately following the entry. In this, you can put an order to sell half stock at a good price (with a profit of around 50%) and then sell some more or the entire remaining stock (at a profit of maybe 100% or 200%).

Straddles

Withstraddles,you can try to get an estimate as to how much the stock may move and decide appropriately then. Based on this analysis, you can make profits with ease. You can take a look at how much the straddle is priced at in the current moment and then see how much would the worth of the straddle be in case the stock makes a move. In case the profit shown is good enough then you may take it. There is an optional way out here of selling half of the position when the stock reaches the level and let the rest go on a bit more. This kind of analysis can prove profitable in a difficult scenario in the stock market.

We will now go ahead and see what has been the Global Impact of Corona Virus and Oil Price War on Trading.

Global Impact of Corona Virus and Oil Price War on Trading

With Covid-19 and Oil Price War making a huge impact on various sectors, we will discuss them all and much more.

The start of this week, i.e., Monday, 9th March 2020 saw a major decline in oil prices in almost 30 years. This led to a further crash in the stock market, which started due to Corona Virus-led decline in the stocks of various industries.

Also, five minutes into trading, on 9th March 2020, the trading in the U.S came to a 15-minute halt after the S&P 500 plunged by 7 per cent. This situation is known asa circuit breaker.

But this was not all, Clorox is one of the handful of companies in the S&P 500 of which the shares rose almost 1 per cent. Clorox is the maker of disinfecting cleaners and wipes.

Now, let us see which are the sectors that led to the negative impact on the stock market due to Corona Virus in the month of February:

A Decline in the Manufacturing Sector Globally

A Negative Hit on the Leisure Industries

A Decline in the Manufacturing Sector Globally

By the end of February (somewhere around 28th Feb), theDJIA remained downfor the entire last week of the month. The major factor behind this was the panic of the Corona Virus amongst people.

Between 2nd and 6th March, the news about the infection (related to its possible causes, mortality rate etc.) soared. Even though the news of infection and its awareness related topics increased, there were no new revelations or cases of Corona Virus. Hence, with the facts about the disease, the uncertainties went down. And,DJIA ended up being +455 points.

Although it was observed later in the document released byUNCTADthat China witnessed about 22 points of decline in output which is measured in Manufacturing Purchasing Manager’s Index (PMI). Since PMI suffered a fall, it was also noted that the exports from China fell by about 2 per cent. Hence, -2 per cent supply of goods made a huge impact on the trading sector consequently.

According to current news in theWorld Economic Forum,Apple’s manufacturing partner in China, Foxconn, is facing a production delay. Some carmakers includingNissan and Hyundaitemporarily closed factories outside China because they couldn’t get parts. The pharmaceutical industry is alsobracing for disruption to global production.

Hence, observing these, the uncertainties went up and the stock market began to crash.

Below is the image showing China’s Purchasing Managers Indices and it is very clearly visible that the entire February month saw a sharp decline in output, which was by 22 points.

Recently, on 9th of March 2020, a downfall in Wall Street was observed which was the worst since 2008 as per The New York Times. The same day S&P 500 was seen to have fallen by more than 7 per cent. Also, the Dow Jones industrial average was down by 2,000 points.

A Negative Hit on the Leisure Industries

Recently, it was mentioned by the International Air Transport Association (IATA) that the airlines globally can lose in passenger revenues by up to $113 billion if the disease spreads any further. Also, it was revealed that worldwide passenger revenue has gone down by 19%.

Coming to theAirline’s share prices,they have come down by almost 25% ever since the Corona Virus outbreak began. It is almost 21% higher than the loss that was reported in 2003 during the SARS crisis. According toEconomic Times, Airline shares have been among those badly affected by the deep sell-offs on financial markets at the end of February, as investors felt that the spread of Covid-19 could dent global growth.

Because of the travel plans having had gone down, even the hospitality sector has faced a hit. According toBusiness Standard, hotel stockshit yearly lows and shed about a quarter of their market capitalisation over the past month.

Moreover, coming to the rate hikes, in 2018, there were four USD rate hikes. On the contrary 2019 had three rate cuts. Stepping into 2020, there has already been an emergency rate cut of 50 bps following Corona outbreak. It is important to note that the last emergency rate cut was done during the financial global crisis of2008-09. As a result of this, major financial institutions' stock prices have started to trend lower this year.

Ahead, now we will see Historical Stock Market Crashes which will give you an insight into how the markets suffered in a similar way due to other reasons.

Historical Stock Market Crashes

It is a well-known fact that an unexpected crisis is a part of every sector and financial sector is one of them. In such huge businesses, crisis are unavoidable. And, there have been some instances in the past which made the Trading sector go through a downfall for some time, which we will discuss:

Great Depression 1929

Great Depression is another crisis that struck the stock market in 1929 after the stock prices fell considerably in the U.S. It was also popularly termed as Black Tuesday as it began on September 4, 1929 and became widespread. In between 1929 and 1932 the GDP fell by 15%, which consequently led to a crash in the stock market considerably leading to a major blow.

According toWikipedia, The Great Depression also came to be known as TheWall Street Crash of 1929 or theGreat Crash.It was a majorstock market crashthat occurred in 1929. It started in September and ended late in October when share prices on theNew York Stock Exchangecollapsed. It was the most devastating stock market crash in thehistory of the United States.

Stock Market Crash 1987

In 1987, the global stock markets had crashed considerably and the day came to be known as Black Monday. During the same time, the Dow Jones index came down crashing by 508 points (23% of its value). That time, Roger Ibbotson, who was a finance professor at Yale University had mentioned the crash elaborately. The scenario was so bad that the market was crashing every few minutes which made the whole week chaotic. In his words, “The futures market was a mess, but you could actually make good money if you were up for some risk. A lot of people tried to set up brokerage accounts to take advantage of some of the valuations.” But, by the end of the year, its impact faded and the market returned to normalcy.

Recession 2008

In 2008, the stock market crash that happened was the largest drop in the history till then. Stock market crash of 2008 happened due to a great collapse in the house prices which went to be a problem long after the market recovered. This scenario also led to Great Recession in the economy which came under control only after some time and not soon. Another reason behind the crash was believed to be the non-repayment of loans by many people.

According toWikipedia,The Timesof London reported that older traders were comparing it with Black Monday in 1987. The fall that week of 21% compared to a 28.3% fall 21 years earlier, but some traders were saying it was worse. "At least then it was a short, sharp, shock on one day."

We have discussed the major crisis in the past that took the stock market to their lowest levels.Hence, there have been some such scenarios where the stock market crashed to the worst level and recovered thereafter.

Conclusion

The aspects discussed in the article consisted of a global perception with regard to near-future estimation with regard to the movement of stocks, trading strategies to adopt and market crashes in the past. All in all, this article aimed at making the present and future scenario clearer with regard to the stock market.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
