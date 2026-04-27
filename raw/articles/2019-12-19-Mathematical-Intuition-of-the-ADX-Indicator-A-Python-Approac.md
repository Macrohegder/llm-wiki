---
title: "Mathematical Intuition of the ADX Indicator: A Python Approach"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/adx-indicator-python/"
date: "2019-12-19"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Mathematical Intuition of the ADX Indicator: A Python Approach

**来源**: [QuantInsti](https://blog.quantinsti.com/adx-indicator-python/)  
**日期**: 2019-12-19  
**作者**: QuantInsti

---

## 原文

Mathematical Intuition of the ADX Indicator: A Python Approach

ByRekhit Pachanekar

You can use the Average Directional Index (ADX) indicator if you want to determine the intensity or strength of a trend. But why would you want to find the intensity of a trend? If you trade in a weaker trend then there is a high probability of reversal compared to a stronger trend. So combining your directional trades with a stronger trend will help you achieve higher hit ratio and higher average profitability per trade.

Here is an interesting fact, while the name is the Average Directional Index (ADX), it does not tell us the direction of the trend. While it may sound alarming, the reason for this is quite simple, The ADX indicator is always used in conjunction with the Positive directional indicator and the Negative directional indicator, which indicate the up and downtrend respectively. We will understand the ADX indicator and its use in this blog.

We will go through the following topics:

What is ADX Indicator?

Calculation of ADX Indicator

Using ADX indicator trading strategy using Python

What is ADX Indicator

Welles Wilder created the directional movement indicator and the ADX indicator to determine the direction as well as the strength of the trend. According to Welles Wilder, the directional movement indicator is said to consist of the following components: the True Range, Smoothed Plus Directional Indicator (+DI) and Smoothed Minus Directional Indicator (-DI).

The ADX indicator is calculated as the smoothed average of the difference between the +DI indicator and the -DI indicator, thus telling us the strength of the trend.

The ADX indicator has a value between 0 and 100. It is generally agreed that if the ADX is above 25, it is a sign of a strong trend.

Before we move ahead with the ADX indicator-based strategies, let’s take a small example and see how the ADX indicator is calculated.

Calculation of ADX Indicator

We have divided this section into the following steps:

The True range

Positive Directional Movement

Negative Directional Movement

Smoothed values

The Positive Index Indicator and Negative Index Indicator

ADX Indicator: Final Calculations

Let us say we have the following data.

11/29/2019

12/2/2019

12/3/2019

12/4/2019

12/5/2019

12/6/2019

12/9/2019

12/10/2019

12/11/2019

12/12/2019

12/13/2019

Before we actually get to the ADX indicator, we have to go through a few other variables too. We have divided this section of the blog into a number of small parts and we begin by finding the true range of the stock price. Let’s get moving!

The True range

The range for the first row is the difference between High and Low. That is 90 - 82, 8. Only truth shall set you free! While the previous statement is arbitrary, it is somewhat true too. If you look at the high and low data, you might miss the price action tradinghappening between the consecutive days. This is where the true range comes into the picture.

To gain a deeper understanding of such nuances and build strategies based on real market movements, explore ourPrice Action Trading Coursedesigned to help you read charts, spot key patterns, and make informed trading decisions.Simply put, we take the maximum value of the following three components:(Current High - Current Low)Absolute value of (Current High - Previous Close)Absolute value of (Current Low - Previous Close)In that respect, we find the actual range of the price action between the days.If we have to calculate the True range of the above values, then for 2 December, the three values would be:(Current High - Current Low) = 95 - 85 = 10Absolute value of (Current High - Previous Close) = 95 - 87 = 8Absolute value of (Current Low - Previous Close) = (85 - 87) = Absolute value of (-2) = 2Thus, since the true range is the maximum of the three values, it would be 10.Let’s fill the table now.DateHighLowClose(High - Low)[1](Today's High - Yesterday's Close)[2](Today's Low - Yesterday's Close)[3]True Range11/29/2019908287----12/2/201995858710821012/3/20191059397121861812/4/2019120106114142392312/5/20191401241331626102612/6/20191651471571832143212/9/20191951751862038183812/10/20192302082232244224412/11/20192702462642447234712/12/20193152893112651255112/13/201936533735028542654All right. Let's keep moving forward.Positive Directional MovementWe are going all the way up, my friend. As the name suggests, the Positive Directional Indicator is used to help us gauge the uptrend of the market. Of course, we pair it with the Negative Directional indicator to derive real meaning from the indicators.But how do I know which way is up?Intuitively, if everyday new high is made compared to previous day high then we can say that the prices are moving up.We have a simple formula for that, which uses the famous "if-else" statement found both in English as well as programming.If (Today's high - Yesterday's High) > (Yesterday's Low - Today's Low), then+DM = (Today's high - Yesterday's High)Otherwise, it's 0.But why do we do that? We are checking if the price difference of the two “highs” is more than the difference between the two lows. This would indicate that there is a demand for the stock and a willingness to buy at a higher price than the previous high.Let us move on to the next section.Negative Directional MovementJust like life, which has its ups and downs, there will always be times when a stock is going down. As we discussed in the previous section, we are checking the selling pressure, which could show up if the investors are ready to sell the stock at a price lower than the previous day.Thus, in the case of the Negative Directional indicator, the formula would be:If (Yesterday's Low - Today's Low) >(Today's high - Yesterday's High), then-DM = (Yesterday's Low - Today's Low)Otherwise, it's 0.We will use the formulae mentioned above and calculate the positive directional movement and the negative directional movement for the table.DateHighLowCloseTrue RangePositive DMNegative DM11/29/2019908287---12/2/2019958587105012/3/201910593971810012/4/20191201061142315012/5/20191401241332620012/6/20191651471573225012/9/20191951751863830012/10/20192302082234435012/11/20192702462644740012/12/20193152893115145012/13/201936533735054500Thus, in this manner, we have understood the directional movements.Before we move to the directional index indicators, we have to figure out what a smoothed version of a True range, Positive Directional movement and a Negative Directional movement is.Smoothed valuesWe should note that the smoothed version is sort of similar tomoving average, as it is used to smoothen out the fluctuations, if any, from the data.We will define a period as 5. This is arbitrarily chosen.We will do the smoothed values of the positive directional movement. The first value is calculated by taking the sum of the first 5 values, ie (5 + 10 +15 + 20 + 25) = 75.The next value is calculated by taking the previous smoothed value and subtract the average from it. Finally, add the current value of the positive directional movement.Confused? Don’t worry, we have the example below.First smoothed positive directional movement value = 75.Average of the smoothed positive directional movement value = 75/5 = 15.Current positive directional movement = 30 (Recall that it is the sixth value)Thus, the second smoothed true range value = 75 - (75/5) + 30 = 75 - 15 + 30 = 90.Let us create the table for the following:DateTrue RangePositive DMNegative DMSmoothed Positive DM11/29/2019----12/2/20191050-12/3/201918100-12/4/201923150-12/5/201926200-12/6/20193225075.012/9/20193830090.012/10/201944350107.012/11/201947400125.612/12/201951450145.512/13/201954500166.4We would like to note that since the Negative DM was 0, the smoothed negative DM is also 0.Similarly, the smoothed true range values are computed and filled in the following table:DateTrue RangePositive DMNegative DMSmoothed Positive DMSmoothed Negative DMSmoothed True range11/29/2019------12/2/20191050---12/3/201918100---12/4/201923150---12/5/201926200---12/6/20193225075.00.0109.012/9/20193830090.00.0125.212/10/201944350107.00.0144.212/11/201947400125.60.0162.312/12/201951450145.50.0180.912/13/201954500166.40.0198.7Great! We have calculated quite a few variables. We now move on to the trinity, the Positive Directional Index indicator, the Negative Directional Index Indicator and the final boss, ie the Averaged Directional Index (ADX) indicator. Let’s move on, shall we?The Positive Directional Index Indicator and Negative Directional Index IndicatorWe found out the Smoothed positive Directional movement as well as the Negative directional movement. On its own, either of the indicators has limited uses. But Wilder made use of both of them together so that their crossovers could be classified as a signal.Now since each can have different magnitudes, we normalise them by dividing with the true range and expressing them as a percentage.Thus, for the positive Directional Indicator, we take the value of Smoothed Positive DM ie 75 and divide it by the true range, 70 and get the value 75/70 = 1.07 and as a percentage, it will be 107.Here, we should note that the Smoothed negative DM was always 0, hence the Negative Directional Index Indicator will be 0.Great! We are just a few more steps away from the main point of this story, ie the ADX indicator.ADX Indicator: Final calculationsRemember that we said the ADX Indicator tells us the strength of the trend and not the direction. To give a brief recap of the situation, so far we found out the positive directional indicator and the negative directional indicator. These would tell us the direction of the trend.But let us step back and try to see if we can get more information from the indicators. What we have to check is how far are the two indicators from each other and this would give us a fair idea of how the market is behaving.If we have a situation where both the indicators are close to each other, then it means there could be a weak trend, if there is.But if there is a large difference between the two, it means we have a strong trend. Wilder quantified this by giving the formula for the directional index (DX) indicator. It is as follows:DX = (Difference of positive and negative directional index indicator) / (sum of positive and negative directional indicator)Thus, the DX value for 6 December would be:DX = (75 - 0) / (75 + 0) = 1.As we are expressing them in percentages, it will be multiplied by 100 to give us the value: 1 * 100 = 100.And now, since we have to remove any fluctuations, we take the moving average of DX to get the Average directional Index (ADX) indicator.Since we are taking the time period as 5, we take the average of the five values.Thus, the updated table would be as follows:DateTrue RangePositive DMNegative DMSmoothed Positive DMSmoothed Negative DMSmoothed True rangePositive Directional IndicatorNegative Directional IndicatorDXADX11/29/2019----------12/2/20191050-------12/3/201918100-------12/4/201923150-------12/5/201926200-------12/6/20193225075.00.0109.068.807339450100-12/9/20193830090.00.0125.271.884984030100-12/10/201944350107.00.0144.274.223085460100-12/11/201947400125.60.0162.377.374205310100-12/12/201951450145.50.0180.980.43684038010010012/13/201954500166.40.0198.783.740533990100100Since the value is 100, we will say that the ADX indicator is exhibiting a very strong trend. This can be also visually confirmed by thecandlestickplot of the data shown above.Considering that we took a simple example before, we have added another table below which gives the stock price of Apple and its corresponding ADX indicator.DateTrue RangePositive DMNegative DMSmoothed True rangeSmoothed Positive DMSmoothed Negative DMPositive Directional IndicatorNegative Directional IndicatorDXADX2017-04-281.030.140.006.101.000.3816.456.2544.9632.362017-05-013.552.900.008.433.700.3043.933.6284.7942.852017-05-021.510.001.888.252.962.1235.8925.7416.4837.572017-05-033.240.000.009.842.371.7024.0817.2616.4833.352017-05-041.330.001.549.201.902.9020.6031.5020.9330.872017-05-052.451.840.009.813.362.3234.2123.6418.2728.352017-05-084.744.720.0012.597.411.8658.8214.7459.9334.672017-05-091.870.004.4211.945.925.9049.6149.440.1727.772017-05-101.880.000.0011.434.744.7241.4541.310.1722.252017-05-111.760.000.0010.913.793.7834.7634.650.1717.832017-05-122.470.002.3611.203.035.3827.0948.0827.9219.852017-05-151.600.000.3810.562.434.6922.9944.3931.7722.232017-05-161.340.000.009.791.943.7519.8438.3131.7724.142017-05-175.760.000.0013.591.553.0011.4322.0731.7725.672017-05-183.090.000.0013.961.242.408.9017.1931.7726.892017-05-191.440.001.5012.610.993.427.8827.1254.9632.502017-05-221.670.600.0011.761.402.7411.8723.2732.4532.492017-05-231.590.000.4011.001.122.5910.1523.5439.7533.942017-05-241.500.000.0010.300.892.078.6720.1139.7535.102017-05-251.320.000.009.560.711.667.4717.3339.7536.03Here we can see a number of times the Positive Directional Indicator crossed over from under the Negative Directional Indicator. But, as we mentioned above, we check the ADX indicator level as well to ascertain the strength of the trend.Let us take a few cases where we could use the ADX indicator as part of a trading strategy.Using ADX indicator trading strategy using PythonEarlier, we saw the process of finding the ADX indicator using a simple table. Now, to work on real-world data, we would take the help of Python to make life easier.We will fetch the data from yahoo finance in the following manner.import yfinance as yf
aapl = yf.download('AAPL', '2017-1-1','2019-12-18')We have taken the stock of Apple and chose the period from 1 Jan 2017 to 18 Dec 2018 at random. We will use the adjusted values with the following code.aapl['Adj Open'] = aapl.Open * aapl['Adj Close']/aapl['Close']
aapl['Adj High'] = aapl.High * aapl['Adj Close']/aapl['Close']
aapl['Adj Low'] = aapl.Low * aapl['Adj Close']/aapl['Close']
aapl.dropna(inplace=True)You can easily compute the ADX indicator in Python with the following codefrom ta.trend import ADXIndicator
adxI = ADXIndicator(aapl['Adj High'],aapl['Adj Low'],aapl['Adj Close'],14,False)
aapl['pos_directional_indicator'] = adxI.adx_pos()
aapl['neg_directional_indicator'] = adxI.adx_neg()
aapl['adx'] = adxI.adx()
aapl.tail()The output will be as follows:DateOpenHighLowCloseAdj CloseVolumeAdj OpenAdj HighAdj Lowpos_directional_indicatorneg_directional_indicatoradx12/11/201926927126927127119,689,20026927126931212612/12/201926827326727127134,327,60026827326731192612/13/201927127527127527533,396,90027127527133182612/16/201927728127728028032,046,50027728127739162812/17/201928028227928028028,539,600280282279391529In Python, we use the “matplotlib” library to plot the graph in the following manner:import matplotlib.pyplot as plt
def plot_graph(data,ylabel,xlabel):
plt.figure(figsize=(10,7))
plt.grid()
plt.plot(data)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plot_graph(aapl['Adj Close'], 'Price', 'Date')
plot_graph(aapl['adx'], 'Price', 'Date')The output is as follows:In this manner, we can compare the ADX indicator with the price and create your trading strategy.But it looks confusing!Don’t worry, we have got you covered. In the following code, we will plot the price data and highlights the parts where the ADX indicator is above 25, indicating a strong trend.aapl['trend'] = np.where(aapl.adx>25,aapl['Adj Close'],np.nan)

aapl['trend_signal'] = np.where(aapl.adx>25,1,0)
plt.figure(figsize=(10,7))
plt.grid()
plt.plot(aapl['Adj Close'])
plt.plot(aapl['trend'])
plt.ylabel('Price')
plt.xlabel('Date')As we had mentioned earlier, The ADX indicator tells us the strength of the trend and not the direction. Thus, if we take the example of the data from Oct 2018 to Jan 1, 2019, the ADX indicator has highlighted the price data signifying that there is a strong trend present. Further, when we see the price chart, we can see it is a downtrend and can take a short position.But we see the data from Jan 2019 onwards, until May 2019, the price rose upwards with the ADX indicator above 25, signifying an uptrend and we can use this as a signal to go long.If we were to use the ADX indicator as to the trading strategy, the returns would be plotted in the following manner.aapl['direction'] = np.where(aapl.pos_directional_indicator>aapl.neg_directional_indicator,1,-1) * aapl['trend_signal']
aapl['daily_returns'] = aapl['Adj Close'].pct_change()
aapl['strategy_returns'] = aapl.daily_returns.shift(-1) * aapl.direction
plot_graph((aapl['strategy_returns']+1).cumprod(), 'Returns', 'Date')These are but a few ways we can use the directional indicators as well as the ADX indicator for your trading strategy. Of course, no indicator is perfect, and it is always recommended to use it along with otherindicatorsto confirm your actions.ConclusionWe have come a long way today, from understanding the calculation of the ADX indicator as well as the python code to implement it, to the use of the indicator in your trading strategy. We have also understood that the ADX indicator is relatively simple to execute and helps us in identifying strongtrendsin the market. Although it has its own limitations, coupling it with other indicators will lead to a strong trading strategy.If you want to learn various aspects of Algorithmic trading and automated trading systems, then check outthe Executive Programme in Algorithmic Trading (EPAT®). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT® equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

Simply put, we take the maximum value of the following three components:

(Current High - Current Low)

Absolute value of (Current High - Previous Close)

Absolute value of (Current Low - Previous Close)

In that respect, we find the actual range of the price action between the days.

If we have to calculate the True range of the above values, then for 2 December, the three values would be:

(Current High - Current Low) = 95 - 85 = 10

Absolute value of (Current High - Previous Close) = 95 - 87 = 8

Absolute value of (Current Low - Previous Close) = (85 - 87) = Absolute value of (-2) = 2

Thus, since the true range is the maximum of the three values, it would be 10.

Let’s fill the table now.

(High - Low)

(Today's High - Yesterday's Close)

(Today's Low - Yesterday's Close)

True Range

11/29/2019

12/2/2019

12/3/2019

12/4/2019

12/5/2019

12/6/2019

12/9/2019

12/10/2019

12/11/2019

12/12/2019

12/13/2019

All right. Let's keep moving forward.

Positive Directional Movement

We are going all the way up, my friend. As the name suggests, the Positive Directional Indicator is used to help us gauge the uptrend of the market. Of course, we pair it with the Negative Directional indicator to derive real meaning from the indicators.

But how do I know which way is up?

Intuitively, if everyday new high is made compared to previous day high then we can say that the prices are moving up.

We have a simple formula for that, which uses the famous "if-else" statement found both in English as well as programming.

If (Today's high - Yesterday's High) > (Yesterday's Low - Today's Low), then

+DM = (Today's high - Yesterday's High)

Otherwise, it's 0.

But why do we do that? We are checking if the price difference of the two “highs” is more than the difference between the two lows. This would indicate that there is a demand for the stock and a willingness to buy at a higher price than the previous high.

Let us move on to the next section.

Negative Directional Movement

Just like life, which has its ups and downs, there will always be times when a stock is going down. As we discussed in the previous section, we are checking the selling pressure, which could show up if the investors are ready to sell the stock at a price lower than the previous day.

Thus, in the case of the Negative Directional indicator, the formula would be:

If (Yesterday's Low - Today's Low) >(Today's high - Yesterday's High), then

-DM = (Yesterday's Low - Today's Low)

Otherwise, it's 0.

We will use the formulae mentioned above and calculate the positive directional movement and the negative directional movement for the table.

True Range

Positive DM

Negative DM

11/29/2019

12/2/2019

12/3/2019

12/4/2019

12/5/2019

12/6/2019

12/9/2019

12/10/2019

12/11/2019

12/12/2019

12/13/2019

Thus, in this manner, we have understood the directional movements.

Before we move to the directional index indicators, we have to figure out what a smoothed version of a True range, Positive Directional movement and a Negative Directional movement is.

Smoothed values

We should note that the smoothed version is sort of similar tomoving average, as it is used to smoothen out the fluctuations, if any, from the data.

We will define a period as 5. This is arbitrarily chosen.

We will do the smoothed values of the positive directional movement. The first value is calculated by taking the sum of the first 5 values, ie (5 + 10 +15 + 20 + 25) = 75.

The next value is calculated by taking the previous smoothed value and subtract the average from it. Finally, add the current value of the positive directional movement.

Confused? Don’t worry, we have the example below.

First smoothed positive directional movement value = 75.

Average of the smoothed positive directional movement value = 75/5 = 15.

Current positive directional movement = 30 (Recall that it is the sixth value)

Thus, the second smoothed true range value = 75 - (75/5) + 30 = 75 - 15 + 30 = 90.

Let us create the table for the following:

True Range

Positive DM

Negative DM

Smoothed Positive DM

11/29/2019

12/2/2019

12/3/2019

12/4/2019

12/5/2019

12/6/2019

12/9/2019

12/10/2019

12/11/2019

12/12/2019

12/13/2019

We would like to note that since the Negative DM was 0, the smoothed negative DM is also 0.

Similarly, the smoothed true range values are computed and filled in the following table:

True Range

Positive DM

Negative DM

Smoothed Positive DM

Smoothed Negative DM

Smoothed True range

11/29/2019

12/2/2019

12/3/2019

12/4/2019

12/5/2019

12/6/2019

12/9/2019

12/10/2019

12/11/2019

12/12/2019

12/13/2019

Great! We have calculated quite a few variables. We now move on to the trinity, the Positive Directional Index indicator, the Negative Directional Index Indicator and the final boss, ie the Averaged Directional Index (ADX) indicator. Let’s move on, shall we?

The Positive Directional Index Indicator and Negative Directional Index Indicator

We found out the Smoothed positive Directional movement as well as the Negative directional movement. On its own, either of the indicators has limited uses. But Wilder made use of both of them together so that their crossovers could be classified as a signal.

Now since each can have different magnitudes, we normalise them by dividing with the true range and expressing them as a percentage.

Thus, for the positive Directional Indicator, we take the value of Smoothed Positive DM ie 75 and divide it by the true range, 70 and get the value 75/70 = 1.07 and as a percentage, it will be 107.

Here, we should note that the Smoothed negative DM was always 0, hence the Negative Directional Index Indicator will be 0.

Great! We are just a few more steps away from the main point of this story, ie the ADX indicator.

ADX Indicator: Final calculations

Remember that we said the ADX Indicator tells us the strength of the trend and not the direction. To give a brief recap of the situation, so far we found out the positive directional indicator and the negative directional indicator. These would tell us the direction of the trend.

But let us step back and try to see if we can get more information from the indicators. What we have to check is how far are the two indicators from each other and this would give us a fair idea of how the market is behaving.

If we have a situation where both the indicators are close to each other, then it means there could be a weak trend, if there is.

But if there is a large difference between the two, it means we have a strong trend. Wilder quantified this by giving the formula for the directional index (DX) indicator. It is as follows:

DX = (Difference of positive and negative directional index indicator) / (sum of positive and negative directional indicator)

Thus, the DX value for 6 December would be:

DX = (75 - 0) / (75 + 0) = 1.

As we are expressing them in percentages, it will be multiplied by 100 to give us the value: 1 * 100 = 100.

And now, since we have to remove any fluctuations, we take the moving average of DX to get the Average directional Index (ADX) indicator.

Since we are taking the time period as 5, we take the average of the five values.

Thus, the updated table would be as follows:

True Range

Positive DM

Negative DM

Smoothed Positive DM

Smoothed Negative DM

Smoothed True range

Positive Directional Indicator

Negative Directional Indicator

11/29/2019

12/2/2019

12/3/2019

12/4/2019

12/5/2019

12/6/2019

68.80733945

12/9/2019

71.88498403

12/10/2019

74.22308546

12/11/2019

77.37420531

12/12/2019

80.43684038

12/13/2019

83.74053399

Since the value is 100, we will say that the ADX indicator is exhibiting a very strong trend. This can be also visually confirmed by thecandlestickplot of the data shown above.

Considering that we took a simple example before, we have added another table below which gives the stock price of Apple and its corresponding ADX indicator.

True Range

Positive DM

Negative DM

Smoothed True range

Smoothed Positive DM

Smoothed Negative DM

Positive Directional Indicator

Negative Directional Indicator

2017-04-28

2017-05-01

2017-05-02

2017-05-03

2017-05-04

2017-05-05

2017-05-08

2017-05-09

2017-05-10

2017-05-11

2017-05-12

2017-05-15

2017-05-16

2017-05-17

2017-05-18

2017-05-19

2017-05-22

2017-05-23

2017-05-24

2017-05-25

Here we can see a number of times the Positive Directional Indicator crossed over from under the Negative Directional Indicator. But, as we mentioned above, we check the ADX indicator level as well to ascertain the strength of the trend.

Let us take a few cases where we could use the ADX indicator as part of a trading strategy.

Using ADX indicator trading strategy using Python

Earlier, we saw the process of finding the ADX indicator using a simple table. Now, to work on real-world data, we would take the help of Python to make life easier.

We will fetch the data from yahoo finance in the following manner.

import yfinance as yf
aapl = yf.download('AAPL', '2017-1-1','2019-12-18')

We have taken the stock of Apple and chose the period from 1 Jan 2017 to 18 Dec 2018 at random. We will use the adjusted values with the following code.

aapl['Adj Open'] = aapl.Open * aapl['Adj Close']/aapl['Close']
aapl['Adj High'] = aapl.High * aapl['Adj Close']/aapl['Close']
aapl['Adj Low'] = aapl.Low * aapl['Adj Close']/aapl['Close']
aapl.dropna(inplace=True)

You can easily compute the ADX indicator in Python with the following code

from ta.trend import ADXIndicator
adxI = ADXIndicator(aapl['Adj High'],aapl['Adj Low'],aapl['Adj Close'],14,False)
aapl['pos_directional_indicator'] = adxI.adx_pos()
aapl['neg_directional_indicator'] = adxI.adx_neg()
aapl['adx'] = adxI.adx()
aapl.tail()

The output will be as follows:

Adj Close

Volume

Adj Open

Adj High

Adj Low

pos_directional_indicator

neg_directional_indicator

12/11/2019

19,689,200

12/12/2019

34,327,600

12/13/2019

33,396,900

12/16/2019

32,046,500

12/17/2019

28,539,600

In Python, we use the “matplotlib” library to plot the graph in the following manner:

import matplotlib.pyplot as plt
def plot_graph(data,ylabel,xlabel):
plt.figure(figsize=(10,7))
plt.grid()
plt.plot(data)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plot_graph(aapl['Adj Close'], 'Price', 'Date')
plot_graph(aapl['adx'], 'Price', 'Date')

The output is as follows:

In this manner, we can compare the ADX indicator with the price and create your trading strategy.

But it looks confusing!

Don’t worry, we have got you covered. In the following code, we will plot the price data and highlights the parts where the ADX indicator is above 25, indicating a strong trend.

aapl['trend'] = np.where(aapl.adx>25,aapl['Adj Close'],np.nan)

aapl['trend_signal'] = np.where(aapl.adx>25,1,0)
plt.figure(figsize=(10,7))
plt.grid()
plt.plot(aapl['Adj Close'])
plt.plot(aapl['trend'])
plt.ylabel('Price')
plt.xlabel('Date')

But we see the data from Jan 2019 onwards, until May 2019, the price rose upwards with the ADX indicator above 25, signifying an uptrend and we can use this as a signal to go long.

If we were to use the ADX indicator as to the trading strategy, the returns would be plotted in the following manner.

aapl['direction'] = np.where(aapl.pos_directional_indicator>aapl.neg_directional_indicator,1,-1) * aapl['trend_signal']
aapl['daily_returns'] = aapl['Adj Close'].pct_change()
aapl['strategy_returns'] = aapl.daily_returns.shift(-1) * aapl.direction
plot_graph((aapl['strategy_returns']+1).cumprod(), 'Returns', 'Date')

These are but a few ways we can use the directional indicators as well as the ADX indicator for your trading strategy. Of course, no indicator is perfect, and it is always recommended to use it along with otherindicatorsto confirm your actions.

Conclusion

We have come a long way today, from understanding the calculation of the ADX indicator as well as the python code to implement it, to the use of the indicator in your trading strategy. We have also understood that the ADX indicator is relatively simple to execute and helps us in identifying strongtrendsin the market. Although it has its own limitations, coupling it with other indicators will lead to a strong trading strategy.

If you want to learn various aspects of Algorithmic trading and automated trading systems, then check outthe Executive Programme in Algorithmic Trading (EPAT®). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT® equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
