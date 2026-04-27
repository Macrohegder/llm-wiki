---
title: "Bear Spread Options Trading Strategy In Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/bear-spread-options-trading-strategy-in-python/"
date: "2018-06-27"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Bear Spread Options Trading Strategy In Python

**来源**: [QuantInsti](https://blog.quantinsti.com/bear-spread-options-trading-strategy-in-python/)  
**日期**: 2018-06-27  
**作者**: QuantInsti

---

## 原文

Bear Spread Options Trading Strategy In Python

ByViraj Bhagat

What Is Spread Trading?

Buying and selling options of the same type for the same stocks is called asSpread Trading. It limits your risk since you know the spread between the two options, but at the same time shrinks the reward, thus the Profits are limited. On creating a spread, the sale of an option offsets the purchase of an option. It offers visibility on risk Requires moderate to high level of trading, and thus for Advanced users

What Is Bear Spread?

Abear spreadis an option spread strategy opposite to that of a Bull Spread when the price of the underlying security is expected to fall. These strategies cost less to apply and are capped for Maximum Profit. Here, oneBuys option and then sells an optionof a lower strike price. If you are moderately bearish or want to reduce the cost of hedging your long positions, the bear call spread or bear put spread may be the answer.

What Are Vertical Bear Spreads?

Vertical Spreads can be best explained as the following:

Options with a: - lower striking price is sold - higher striking price is purchased

Entering with a net credit or a net debit: Depends on whether calls or puts are used

Gain and Loss has to be defined: Maximum loss and maximum gain for the trade is done by selecting strike prices of the options

Objective: To profit when the stock price is expected to be steady or to go down (not significantly)

Qualities Of A Bear Spread Trading Strategy

The qualities of a Bear Spread Strategy can be listed as follows:

Used for excellent trades for when a stock is expected to go down but is likely to not go lower than a strong support level

Profit or Max. Loss can be identified in advance

Both spreads have a similar Payoff Structure

Select strikes based on the time to expiry

Profits and losses are capped

When To Select A Bear Spread Strategy?

The spread is best invoked when you are moderately bearish on the markets

Implement the strategy only when you expect the volatility to increase (especially in the 2nd half of the series)

If call option premiums are more attractive than put options - Choose bear call spread over a bear put spread

If the stock collapses in the short term: Bear Put Spread is a better bet as the payout on long puts is immediate

Most Common Approach:If the trade goes opposite to the Trade, compare the maximum loss of each spread, identify which would generate the smallest loss and practise the CALL or the PUT spread accordingly

What Do You Need ForA Bear Spread Strategy?

The following criteria have to be met with if one wants to trade for Bear Spread Options:

Underlying stock likely to fall in price

Expiration date matching that of the stock price to fall

Strike price

Consider:Price of  underlying asset/Stock that is believed to decrease in PriceRisk:Simultaneously buying a higher striking ITM Put option and selling an OTM Put option at a lower strike price that reduces the cost, and thus the risk of the trade.Expiry of Options:Both options have the same expiry date

Construction Of A Bear Spread Options Trading Strategy

Buy 1 ITM Put

Sell 1 OTM Put

The only difference is the Strike Price

The strategy would ideally look something like this:Often, people seem to question the differences between Vertical Spreads for Put and Vertical Spreads for Call and different types of Bear Spreads by asking questions like:

What Is The Difference Between A Vertical Bear Credit Spread and A Vertical Bear Debit Spread?

Vertical Bear Credit Spread versusVertical Bear Debit Spread - Which One Is Better?

What Are The Different Types Of Bear Spreads?

What Are The Different Types Of Vertical Spreads?

Well, here is a brief comparison of both to help you understand the difference.

Now, to explain it in a simpler manner, utilising these concepts, I would take you through an example to gain a better understanding of the subject.

Example Of Bear Spread Trading Strategy

For this, we would take the example of Bear Put Options Trading StrategyMaximum Profit:Max Profit = Strike Price of Long Put - Strike Price of Short Put - Net Premium Paid Maximum Profit Potential = (Width of Put Strikes - Net Debit Paid) x 100 Price of Underlying </= Strike Price of Short Put Estimated Probability of Profit: Less than 50% for out-of-the-money spreads, approximately 50% for at-the-money spreads, and greater than 50% for in-the-money spreads.Maximum Loss:Max Loss = Net Premium Paid Maximum Loss Potential = Net Debit Paid x 100 Price of Underlying >/= Strike Price of Long PutBreakeven Point= Strike Price of Long Put - Net Premium Paid Expiration Breakeven Price = Long Put Strike Price - Net Debit PaidResulting Position After Expiration:If the entire put spread is in-the-money at expiration, the long put expires to -100 shares and the short put expires to +100 shares, netting out to no stock position. However, if only the long put is in-the-money at expiration, the resulting position will be -100 shares per contract.

Implementing The Bear Spread Options Strategy

I will use Adani Enterprises Ltd. (Ticker – NSE: ADANIENT) option for this example.

Spot Price: 160

Long Put Strike Price: 165 (Premium: 9.7)

Short Put Strike Price: 155 (Premium: 5.4)

How To Calculate The Bear Spread Options Trading Strategy Payoff In Python?

Now, let me take you through the Payoff chart using the Python programming code.

import numpy as np
 import matplotlib.pyplot as plt
 import seaborn 
 seaborn.set(style="darkgrid")

def put_payoff(sT, strike_price, premium):
     return np.where(sT < strike_price, strike_price - sT, 0) - premium# Adani Enterprises Ltd Spot Prices0 = 160# Long Putstrike_price_long_put =165
 premium_long_put = 9.7# Short Putstrike_price_short_put = 155
 premium_short_put = 5.4# Range of put option at expirysT = np.arange(100,220,1)


long_put_payoff = put_payoff(sT, strike_price_long_put, premium_long_put)

 fig, ax = plt.subplots()

 ax.spines['bottom'].set_position('zero')
 ax.plot(sT, long_put_payoff, color ='g')
 ax.set_title('Long 165 Strike Put')
 plt.xlabel('Stock Price (sT)')
 plt.ylabel('Profit & Loss')
 plt.show()

short_put_payoff = put_payoff(sT, strike_price_short_put, premium_short_put) * -1.0

 fig, ax = plt.subplots()
 ax.spines['bottom'].set_position('zero')
 ax.plot(sT, short_put_payoff, color ='r')
 ax.set_title('Short 155 Strike Put')
 plt.xlabel('Stock Price (sT)')
 plt.ylabel('Profit & Loss')
 plt.show()

The Payoff should ideally be as calculated in the tabular format here. You candownload the excel sheetfor calculating the Payoff of Bear Spread Strategy in the downloadable format at the end of the article.

fig, ax = plt.subplots(figsize=(10,5))
 ax.spines['bottom'].set_position('zero')
 ax.plot(sT, Bear_Put_payoff, color ='b', label = 'Bear Put Spread')
 ax.plot(sT, long_put_payoff,'--', color ='g', label ='Long Put')
 ax.plot(sT, short_put_payoff,'--', color ='r', label ='Short Put')
 plt.legend()
 plt.xlabel('Stock Price (sT)')
 plt.ylabel('Profit & Loss')
 plt.show()

The final output would look like this:

Bear_Put_payoff = long_put_payoff + short_put_payoff 

 fig, ax = plt.subplots()
 ax.spines['bottom'].set_position('zero')
 ax.plot(sT, Bear_Put_payoff, color ='b')
 ax.set_title('Bear Put Spread Payoff')
 plt.xlabel('Stock Price (sT)')
 plt.ylabel('Profit & Loss')
 plt.show()

profit = max (Bear_Put_payoff)
 loss = min (Bear_Put_payoff)

 print ("Max Profit %.2f" %profit)
 print ("Max Loss %.2f" %loss)

  5.70
 -4.30

Max. Profit: 5.70 INR Max. Loss: -4.30 INR

Conclusion

If you are modestly bearish, think volatility is rising and prefer to limit your risk, the best strategy would be a bear put spread.

Modern trading demands a systematic approach and the need to steer yourself away from trading from the gut. Learn how you too can trade options in a systematic manner with our course onSystematic Options Trading. Plus, you get to explorebasics of options tradingstrategies like a butterfly, iron condor, and spread strategies. Enroll now!

Download Data File

Bear Spread Trading Strategy - Python Code.ipynb

Bear Spread Payoff Strategy Calculation.xlsx

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
