---
title: "Pivot Point Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/pivot-point-strategy/"
date: "2019-11-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Pivot Point Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/pivot-point-strategy/)  
**日期**: 2019-11-22  
**作者**: QuantInsti

---

## 原文

Pivot Point Strategy

In this project, we analyze different intraday trading strategies with Pivot Points. After defining different ways of calculating the Pivot Point, we do aBacktestwith the most classic strategies and a different variant to those normally taught in textbooks.

To learn about Pivot Point and how to use it to predict movement in trade markets,read this blog.

This article is the final project submitted by the authors as a part of their coursework in the Executive Programme in Algorithmic Trading (EPAT®) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

A Multi-asset Portfolio Manager at Morabanc Asset Management,Tomás García-Purriñoshas over 10 years of experience in the financial sector. Among his strengths are economic analysis, asset allocation and alternative strategies with a global macro approach. Tomás is a Chartered Financial Analyst (CFA), Chartered Alternative Investment Analyst (CAIA) and holds a Master´s degree in Financial Markets from the IEB. He also teaches in several universities and business schools.

Introduction

Born probably in Chicago, Pivot Point is a popular technique among traders to calculate supports and resistances. It appears in most of the textbooks and curriculums dedicated to the study of technical analysis (i.e. CMT or CFTe), and is on the list of most common indicators in technical analysis software.

However, as with most technical indicators, public academic studies are scarce and the majority of backtests are either private (i.e proprietary research) or in blogs, etc.

There are different methods of calculating Pivot Point levels. We have tested strategies calculating the central pivot point in two different ways:

As the average between close, maximum and minimum of the previous day;

Including the opening of the current day;

Adding the opening twice and without closing price (Woodie's method).

The close price has been taken at 15:59. The remaining levels have been calculated as follows:

Classic / Woodie

Camarilla

Fibonacci

Support 1 (S1)

2 * Pivot Point - H

Pivot Point - (0.0916 * Range)

Pivot Point - (0.382 * Range)

Resistance 1

2 * Pivot Point - L

Pivot Point + (0.0916 * Range)

Pivot Point + (0.382 * Range)

Support 2 (S2)

Pivot Point - H - L

Pivot Point - (0.183 * Range)

Pivot Point - (0.618 * Range)

Resistance 2 (R2)

Pivot Point+ H - L

Pivot Point + (0.183 * Range)

Pivot Point + (0.618 * Range)

Support 3 (S3)

S1 - H - L

Pivot Point - (0.275 * Range)

Pivot Point - (1 * Range)

Resistance 3 (R3)

R1+ H - L

Pivot Point + (0.275 * Range)

Pivot Point + (1 * Range)

H = Last Period HighL = Last Period LowRange = Last Period High - Last Period Low

Figure 1: Pivot Point Levels

In this EPAT Final Project, we analyze different Pivot Point strategies on futures listed in CME (Mini S&P 500, Treasury, EURUSD and Gold).

Methodology

For Backtesting the strategies, we have used Python with Pandas, Numpy, Matplot and QuantStats libraries.

It is important to take into account different aspects of the analysis that could have taken their toll on the results:

The study was conducted with intraday data of one minute. There may be differences between the closing price of each minute and the price at which strategy would actually have been executed (slippage) and nothing ensures that there was enough volume. Also, commissions, fees and taxes have not been taken into account. Despite the above, the products chosen have remarkable liquidity and low commissions cost, so we estimate a low impact (subtracting around -0,25%/-0,75% to the cumulate returns of the sample backtest).

We´ve used the first contract of the future, so rollover hasn´t been taken into account. In the study sample, there has been at least one roll, which will impact on the calculation of the Pivot Points of the next day and therefore on the results of the day.

Due to difficulties in calculations, it has been preferred not to trade on Sundays (and eliminate this day for the Monday´s Pivot Points, which are calculated with Friday´s levels).

To explore these backtesting techniques in-depth and improve your trading strategies, our course offers practical training on handling real market data, slippage, and transaction costs. Enroll now to gain expertise inbacktesting tradingand strategy optimization.

Backtest

A 250-day sample and a 30-day Out Of Sample analysis have been used to analyze the results.

Initially, the idea was to test the most classic strategies, as explained in the textbooks (i.e. buy in supports and sell resistances, or buy when Price open above the pivot point, sell when Price open below Pivot Point, etc). However, the poor results obtained made us think they don´t work anymore.

We analyzed two alternative strategies:

Strategy 1:Buy when price breaks resistance. Add +1 contract in the breakdown of each resistance. Sell ​​when price breaks support. Add -1 contract in each break. The position must be between -3 and +3 contracts. Close all positions at the end of the day. This strategy does the opposite of what the textbook says.

Strategy 2:A slightly more elaborated version of Strategy 1. If the price opens above the Pivot Point, and if crosses below the Pivot Point, sell -2 contracts and add -1 on support 1 with a target on supports 2 and 3 (+2 on support 1 and +1 on support 2) and stop at the resistances. If the price opens below the Pivot Point, buy +2 when the price crosses up the centre pivot and add in resistance 1 +1, with targets in resistance 2 and 3 (-2 in resistance 2 and -1 in resistance 3) and stop on supports. Close all positions at the end of the day.

BT Strategy 1

In general, the results are mediocre, although somewhat better than the textbook version. The difference between methods of calculating pivot points is minimal, given that levels are relatively similar. In any case, the one that seems to give the best results, or at least the most stable, is the Classic method including the opening.

The only remarkable results using this strategy are on EURUSD, but they are not supported outside the sample and seem more a coincidence than a cause of the strategy.

You can find a summary of the results in Appendix 1.

BT Strategy 2

More interesting has been the results of the second strategy.

The results obtained with the MiniSP stand out especially.

The strategy shows consistent performance throughout the analyzed period and strongly trends in August:

Graph 1: Strategy 2. Cumulative Returns vs Benchmark MiniSP

Although drawdowns are higher than a Buy & Hold strategy, potential returns are higher too and compensate that risk as to the high Calmar Ratio shows.

This consistency remains out of the sample:

Graph 2: Strategy 2. Cumulative Returns vs Benchmark MiniSP Out Of Sample

In the case of Gold, we found positive results, although less colourful:

Graph 3: Strategy 2. Cumulative Returns vs Benchmark Gold

They don't stay out of the sample. Perhaps because of the strong trend that started in August:

Graph 4: Strategy 2. Cumulative Returns vs Benchmark Gold Out of Sample

Similarly, EURUSD repeats this pattern, but of less magnitude, while the Treasury shows good results, although out of the sample it behaves similarly to Gold at the end of the backtested period: it seems this system behaves worse in very trendy markets.

Graph 5: Strategy 2. Cumulative Returns vs Benchmark EURUSD

Graph 6: Strategy 2. Cumulative Returns vs Benchmark EURUSD Out of Sample

Graph 7: Strategy 2. Cumulative Returns vs Benchmark Treasury Futures

Graph 8: Strategy 2. Cumulative Returns vs Benchmark Treasury Futures Out of Sample

A summary of the main statistics is attached in Appendix 2.

Conclusion

We can highlight these main conclusions:

Pivot Points calculation differences do not offer significant changes in the results of simple systems.

Traditional trading strategies, as taught in the textbook, do not seem to work anymore. Also, the simplest or most obvious strategies do not work either way (neither for purchases nor to do the opposite). But small modifications in traditional strategies do seem to work and give some hope to continue researching.

It seems that mean regression strategies work worse than momentum. All in all, in very trendy markets, no one beats a simple Buy & Hold.

It would be interesting to continue researching and trying to find indicators to add to the strategy, especially those that made it rotate frommomentumto average regression depending on the type of market.

Bibliography

Books:

Candlestickand Pivot Point Trading, John L. Person, Wiley 2007.

Computer Analysis of the Futures Market, Charles LeBeau y David W. Lucas, 1992.

Magazines:

Stocks & Commodities V. 18:2 (16-22): Pivot Points by Jayanthi Gopalakrishnan.

Stocks & Commodities V. 24:3 (72-73):Predicting Reversals With Pivot Points by John Devcic.

Workpapers:

Wilinski, Antoni & Nyczaj, Tomasz & Bera, Aneta & Błaszyński, Piotr. (2013). A study on the effectiveness of investment strategy based on the concept of pivot points levels using Matthews criterion. Journal of Theoretical and Applied Computer Science. 7. 42-55.

StockCharts, ChartSchool » Technical Indicators and Overlays » Pivot Points:https://school.stockcharts.com/doku.php?id=technical_indicators:pivot_points

X-Trader.net »Especial Pivot Points:https://www.x-trader.net/foro/viewtopic.php?t=20210

APPENDIX 1: STRATEGY 1 BACKTEST

Table 1: Summary of Strategy 1 Backtest

Treasury Futures

Mini SP

EURUSD

EURUSD Out of Sample

Strategy 1

Buy & Hold

Strategy 1

Buy & Hold

Strategy 1

Buy & Hold

Strategy 1

Buy & Hold

Strategy 1

Buy & Hold

Start Period

05/02/2019

05/02/2019

05/02/2019

05/02/2019

05/02/2019

05/02/2019

05/02/2019

05/02/2019

21/08/2019

21/08/2019

End Period

21/08/2019

21/08/2019

21/08/2019

21/08/2019

21/08/2019

21/08/2019

21/08/2019

21/08/2019

20/09/2019

20/09/2019

Time in Market

Number of Trades

Cumulative Return

14.25%

10.12%

-7.28%

-2.77%

-2.02%

-0.25%

13.54%

10.43%

27.99%

19.56%

-13.08%

-5.07%

-22.03%

-3.02%

Sharpe

Sortino

Max Drawdown

-2.42%

-1.59%

-8.06%

-5.54%

-7.08%

-6.98%

-12.26%

-3.63%

-3.16%

-1.87%

Longest DD Days

Volatility (ann.)

13.24%

11.13%

10.99%

10.93%

Calmar

Kurtosis

Expected Daily %

-0.04%

-0.01%

-0.07%

-0.01%

Expected Monthly %

-1.07%

-1.02%

-0.13%

Expected Yearly %

14.25%

10.12%

-7.28%

-2.77%

-2.02%

-0.25%

Daily Value-at-Risk

-0.38%

-0.33%

-1.34%

-1.08%

-1.09%

-0.91%

-0.46%

-0.73%

-0.47%

Expected Shortfall (cVaR)

-0.55%

-0.55%

-1.83%

-1.83%

-1.63%

-1.63%

-1.06%

-1.06%

-1.31%

-1.31%

Payoff Ratio

Profit Factor

Common Sense Ratio

CPC Index

Tail Ratio

Outlier Win Ratio

Outlier Loss Ratio

-3.03%

-1.98%

-3.92%

17.57%

12.26%

-0.54%

-2.02%

-0.25%

13.22%

-1.76%

-2.02%

-0.25%

14.25%

10.12%

-7.28%

-2.77%

-2.02%

-0.25%

14.25%

10.12%

-7.28%

-2.77%

-2.02%

-0.25%

Best Day

Worst Day

-0.77%

-0.57%

-2.53%

-1.69%

-3.51%

-1.18%

-0.94%

-1.78%

Best Month

Worst Month

-0.79%

-0.47%

-3.03%

-1.68%

-1.94%

-6.94%

-6.81%

-3.03%

-0.99%

Avg. Drawdown

-0.47%

-0.39%

-1.94%

-1.48%

-1.69%

-1.44%

-1.75%

Avg. Drawdown Days

Recovery Factor

APPENDIX 2:SUMMARY OF STRATEGY 2 BACKTEST

Table 2: Summary of Strategy 2 Mini S&P Backtest

Mini S&P 500

Mini S&P 500 Out of Sample

Start Period

05/02/2019

05/02/2019

21/08/2019

21/08/2019

End Period

21/08/2019

21/08/2019

20/09/2019

20/09/2019

Time in Market

Number of Trades

Cumulative Return

45.03%

99.15%

12.39%

83.65%

56.27%

Sharpe

Sortino

Max Drawdown

-6.31%

-7.11%

-2.98%

-2.78%

Longest DD Days

Volatility (ann.)

18.77%

10.95%

15.14%

11.87%

Calmar

Kurtosis

Expected Daily %

Expected Monthly %

Expected Yearly %

45.03%

Daily Value-at-Risk

-1.75%

-1.11%

Expected Shortfall (cVaR)

-2.95%

-2.95%

-1.52%

-1.52%

Payoff Ratio

Profit Factor

Common Sense Ratio

CPC Index

Tail Ratio

Outlier Win Ratio

Outlier Loss Ratio

20.69%

-2.11%

24.15%

45.03%

45.03%

Best Day

Worst Day

-4.31%

-3.54%

-1.52%

-2.78%

Best Month

20.69%

Worst Month

-2.42%

-7.07%

Best Year

45.03%

Worst Year

45.03%

Avg. Drawdown

-1.45%

-1.16%

-1.24%

Avg. Drawdown Days

Recovery Factor

Table 3: Summary of Strategy 3 Treasury Futures Backtest

Treasury Futures

Treasury Futures Out of Sample

Start Period

05/02/2019

05/02/2019

21/08/2019

21/08/2019

End Period

21/08/2019

21/08/2019

20/09/2019

20/09/2019

Time in Market

Number of Trades

Cumulative Return

-0.52%

13.14%

13.54%

25.13%

-6.17%

Sharpe

Sortino

Max Drawdown

-3.85%

-1.59%

-3.27%

-2.57%

Longest DD Days

Volatility (ann.)

Calmar

Kurtosis

Expected Daily %

-0.02%

Expected Monthly %

-0.26%

Expected Yearly %

-0.52%

Daily Value-at-Risk

-0.55%

-0.33%

-0.52%

Expected Shortfall (cVaR)

-0.75%

-0.75%

-1.12%

-1.12%

Payoff Ratio

Profit Factor

Common Sense Ratio

CPC Index

Tail Ratio

Outlier Win Ratio

Outlier Loss Ratio

-0.89%

-0.52%

-0.52%

-0.52%

-0.52%

Best Day

Worst Day

-1.05%

-0.57%

-1.12%

-0.63%

Best Month

Worst Month

-0.47%

-0.89%

Best Year

-0.52%

Worst Year

-0.52%

Avg. Drawdown

-0.72%

-0.39%

-1.11%

Avg. Drawdown Days

Recovery Factor

Table 4: Summary of Strategy 2 EURUSD Backtest

EURUSD

EURUSD Out of Sample

Start Period

05/02/2019

05/02/2019

21/08/2019

21/08/2019

End Period

21/08/2019

21/08/2019

20/09/2019

20/09/2019

Time in Market

Cumulative Return

-2.28%

-2.77%

-0.25%

-4.18%

-5.07%

19.77%

-3.02%

Sharpe

Sortino

Max Drawdown

-10.87%

-3.63%

-1.29%

-1.87%

Longest DD Days

Volatility (ann.)

Calmar

Kurtosis

Expected Daily %

-0.01%

-0.01%

-0.01%

Expected Monthly %

-0.33%

-0.13%

Expected Yearly %

-2.28%

-2.77%

-0.25%

Daily Value-at-Risk

-0.72%

-0.46%

-0.72%

-0.47%

Expected Shortfall (cVaR)

-0.87%

-0.87%

-0.98%

-0.98%

Payoff Ratio

Profit Factor

Common Sense Ratio

CPC Index

Tail Ratio

Outlier Win Ratio

Outlier Loss Ratio

-1.78%

-0.54%

-0.25%

-4.71%

-1.76%

-0.25%

-2.28%

-2.77%

-0.25%

-2.28%

-2.77%

-0.25%

Best Day

Worst Day

-1.08%

-0.94%

-0.98%

Best Month

Worst Month

-4.13%

-3.03%

-0.99%

Best Year

-2.28%

-2.77%

-0.25%

Worst Year

-2.28%

-2.77%

-0.25%

Avg. Drawdown

-5.65%

-0.99%

Avg. Drawdown Days

Recovery Factor

Table 5: Summary of Strategy 2 Gold Backtest

Gold out of Sample

Start Period

05/02/2019

05/02/2019

21/08/2019

21/08/2019

End Period

21/08/2019

21/08/2019

20/09/2019

20/09/2019

Time in Market

Cumulative Return

36.32%

14.25%

-8.83%

77.55%

27.99%

-67.52%

13.95%

Sharpe

Sortino

Max Drawdown

-8.58%

-5.54%

-11.91%

-3.68%

Longest DD Days

Volatility (ann.)

17.97%

11.13%

18.94%

11.72%

Calmar

Kurtosis

Expected Daily %

Expected Monthly %

-4.52%

Expected Yearly %

36.32%

14.25%

-8.83%

Daily Value-at-Risk

-1.08%

-2.25%

-1.18%

Expected Shortfall (cVaR)

-2.53%

-2.53%

-2.52%

-2.52%

Payoff Ratio

Profit Factor

Common Sense Ratio

CPC Index

Tail Ratio

Outlier Win Ratio

Outlier Loss Ratio

-10.28%

-0.37%

35.57%

17.57%

-8.83%

34.04%

13.22%

-8.83%

36.32%

14.25%

-8.83%

36.32%

14.25%

-8.83%

Best Day

Worst Day

-3.79%

-1.69%

-2.53%

-1.75%

Best Month

11.62%

Worst Month

-3.38%

-1.68%

-10.28%

-0.37%

Best Year

36.32%

14.25%

-8.83%

Worst Year

36.32%

14.25%

-8.83%

Avg. Drawdown

-2.53%

-1.48%

-4.57%

-1.45%

Avg. Drawdown Days

Recovery Factor

If you want to learn various aspects of Algorithmic trading then check out the Executive Programme in Algorithmic Trading (EPAT®). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit./overseas

---

*Imported from QuantInsti Blog on 2026-04-27*
