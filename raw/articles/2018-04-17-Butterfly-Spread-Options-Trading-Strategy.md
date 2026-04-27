---
title: "Butterfly Spread Options Trading Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/butterfly-spread-options-trading-strategy-python/"
date: "2018-04-17"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Butterfly Spread Options Trading Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/butterfly-spread-options-trading-strategy-python/)  
**日期**: 2018-04-17  
**作者**: QuantInsti

---

## 原文

Butterfly Spread Options Trading Strategy In Python

ByViraj Bhagat

Traders and investors consider the movement in the markets as an opportunity to earn profits.

If the stock, Goes Up => Buy the stock + Buy call option Doesn’t Move Up Much => Apply Bull Spread Goes Down => Short Sell the stock + Apply Bear Spread Remains Steady => Apply Butterfly Options Strategy

About Butterfly Options Trading Strategy

For those unfamiliar withoptions trading basics, this is a neutral strategy with limited risk. Butterfly Options Strategy is a combination of Bull Spread and Bear Spread, a Neutral Trading Strategy, since it has limited risk options and a limited profit potential. It is practised on the stocks whose underlying Price is expected to change very little over its lifetime.

It is beneficial for directional trades and can be traded either upside or downside, and also works best in a non-directional market. It has a comparatively lesser risk for trading larger value stocks, thus using less margin. When the future volatility of the underlying asset is expected to go high/low than long/short IV Butterfly Spread has a high probability of earning a limited profit.

Components Of Butterfly Strategy

The ButterflyOptions Strategyis made of a Body (the middle double option position) and Wings (2 opposite end positions). Its properties are listed as follows:

It is a three-leg strategy

Involves Buying or selling of Call/Put options (unlikeCovered Call Strategywhere a stock is bought and an OTM call option is sold)

Can be constructed using Calls or Puts

4 options contracts at the same expiry date

Have the same underlying asset

3 different Strike Prices are involved (2 have the same strike price)

Create 2 Trades with these calls

Buy 1 ITM Call

Buy at lower Strike Price

Closes at expiry

Provides the Maximum Profit

Sell 2 ATM Calls

Sold at middle Strike Price

Generates the revenue

Expires worthless

Buy 1 OTM Call

Buy at higher Strike Price

Expires worthless

The strategy would ideally look something like this:

Condition

The difference between the Middle, Upper and Lower Strike Price must be the same.

The middle strike price should be halfway between the higher strike price and the lower strike price.

Calculation Of Butterfly Spread Strategy

A resulting net debit is taken to enter the trade.

Limited Profit

Maximum profit is earned when:

Underlying stock price remains unchanged at expiration

Only the lower striking call expires in the money

Cash price is equal to the middle strike price on the expiry day

Max Profit

Max Profit = Strike Price of Short Call - Strike Price of Lower Strike Long Call - Net Premium Paid

Price of Underlying = Strike Price of Short Calls

Limited Risk

The initial debit which is taken for entering the trade limits the Max. Loss for the Long Butterfly Spread.

Max Loss

Max Loss = Net Premium Paid + Commissions Paid

Price of Underlying </= Strike Price of Lower Strike Long Call Price of Underlying >/= Strike Price of Higher Strike Long Call

Breakeven Point(s)

There are 2 break-even points for the butterfly spread position:

Upper Breakeven Point = Highest Strike Price - Net Premium Paid (ie. Debit)

Lower Breakeven Point = Lowest Strike Price + Net Premium Paid (ie. Debit)

At expiry, if the price of the underlying Stock is equal to either of the two values the butterfly will breakeven.

Implementing The Strategy

I will use Adani Power Ltd (Ticker – NSE: ADANIPOWER) option for this example.

The stock price of Adani Power Ltd. is moving steadily in the second half of this month.The highest being 38.20 and lowest being 31.05 in last 1 month which is the current value as per Google Finance.

For the purpose of this example; I will buy 1 In-the-money Call, 2 At-the-money Call and 1 Out-of-the-money Call Options.

Here is the option chain of Adani Power Ltd. for the expiry date of 28th March 2018.

Source: nseindia.com

Source: nseindia.com

I will pay INR 3.60 for 2 calls ATM with a strike price of 32.50, INR 3.15 for the Call ITM with a strike price of 30.00 and INR 0.85 for the Call OTM with a strike price of 35. The options will expire on 28th March 2018. To make a profit, the market should move upwards before the expiry. The net premium paid to initiate this trade will be INR 10.10.

If the Butterfly Spread is properly implemented, the gains would be potentially higher than the potential loss, and both will be limited.

Calculating TheButterfly Spread Options Trading StrategyPayoff In Python

Now, let me take you through the Payoff chart using the Python programming code and by using Calls.

import numpy as np
import matplotlib.pyplot as plt
import seaborn

Call Payoff

def call_payoff (sT, strike_price, premium):
return np.where(sT> strike_price, sT-strike_price, 0)-premium
# Spot Price
s0 = 40
​
# Long Call
higher_strike_price_long_call = 35
lower_strike_price_long_call=30
​
premium_higher_strike_long_call = 0.85
premium_lower_strike_long_call = 3.15
​
# Short Call
​
strike_price_short_call = 32.5
premium_short_call = 1.80
​
# Range of call option at expiration
sT = np.arange(10,60,1)

Long Call Payoff

# OTM Strike Long Call Payoff
lower_strike_long_call_payoff = call_payoff(sT, lower_strike_price_long_call, premium_lower_strike_long_call)
​
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,lower_strike_long_call_payoff, color='g')
ax.set_title('LONG 30 Strike Call')
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
​
plt.show()

Higher Strike Long Call Payoff

# Higher Strike Long Call Payoff
​
higher_strike_long_call_payoff = call_payoff(sT, higher_strike_price_long_call, premium_higher_strike_long_call)
​
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,higher_strike_long_call_payoff, color='g')
ax.set_title('LONG 35 Strike Call')
plt.xlabel('Stock Price (sT)')
plt.ylabel('Profit & Loss')
​
plt.show()

Short Call Payoff

# Short Call Payoff
​
Short_call_payoff = call_payoff(sT, strike_price_short_call, premium_short_call)*-1.0
​
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT, Short_call_payoff, color='r')
ax.set_title('Short 32.5 Strike Call')
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
​
plt.show()

Butterfly Spread Payoff

Butterfly_spread_payoff = lower_strike_long_call_payoff + higher_strike_long_call_payoff + 2 *Short_call_payoff
​
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,Butterfly_spread_payoff ,color='b', label= 'Butterfly Spread')
ax.plot(sT, lower_strike_long_call_payoff,'--', color='g',label='Lower Strike Long Call')
ax.plot(sT, higher_strike_long_call_payoff,'--', color='g', label='Higher Strike Long Call')
ax.plot(sT, Short_call_payoff, '--', color='r', label='Short call')
plt.legend()
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
plt.show()

Butterfly_spread_payoff = lower_strike_long_call_payoff + higher_strike_long_call_payoff + 2 *Short_call_payoff
​
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,Butterfly_spread_payoff ,color='b', label= 'Butterfly Spread')
plt.legend()
plt.xlabel('Stock Price')
plt.ylabel('Profit & Loss')
plt.show()

profit = max(Butterfly_spread_payoff)
loss = min(Butterfly_spread_payoff)
​
print ("%.2f" %profit)
print ("%.2f" %loss)Max. Profit: 1.60Max. Loss: 0.40

Some Related Terms

Short Butterfly:Inverse to the Long Butterfly, practised when Stock Price could go in either direction

Long Call Butterfly:In this strategy, all Call options have the same expiration date, and the distance between each strike price of the constituent legs is the same

Long Put Butterfly:Practicing Long Butterfly Spread using Puts options

Broken Wings Butterfly:Distance between the Strike Prices is unequal

Condor:The body has different Strike Prices

Wingspreads:Family of spreads where the members are named after various flying creatures

Conclusion

The Butterfly Spread is a strategy that takes advantage of the time premium erosion of an option contract, but still allows the investor to have a limited and known risk. It is used by the investors who predict a narrow trading range for the underlying security (as they are comfortable), and by those who are not comfortable with the unlimited risk involved with a short straddle.You can enroll for theoptions trading courseon Quantra to create successful strategies and implement knowledge in your trading. It covers both retail andinstitutional tradingstrategies. If you're looking to combine options knowledge with systematic strategy building, analgo trading coursethat covers both quantitative methods and execution frameworks will be a natural next step.

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out the Executive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download Data File

Butterfly Options Trading Strategy - Python Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
