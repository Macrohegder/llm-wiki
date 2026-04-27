---
title: "Bull Call Spread Strategy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/bull-call-spread-strategy/"
date: "2018-05-03"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Bull Call Spread Strategy

**来源**: [QuantInsti](https://blog.quantinsti.com/bull-call-spread-strategy/)  
**日期**: 2018-05-03  
**作者**: QuantInsti

---

## 原文

Bull Call Spread Strategy

ByNitin Thapar

Introduction

In my last blog, I explained how theStrangle Strategyworks. This time I will be taking you through the Bull Call Spread strategy. This strategy is quite popular amongst novice traders since it is simple to follow and has limited risk involved but if you click the right opportunity there is great potential to get good amount of returns on your investment.

This strategy is preferred by traders who want to minimize their risk and gain moderate returns on their investment.

What Is Bull Call Spread Strategy?

The bull call spread strategy involvesoptionson the same underlying security, with the same expiration date, but with different strike prices. Therefore, this strategy is also known as a"Vertical Spread".

Strategy Highlights

Moneyness Of The Options:

Buy 1 OTM Strike Call

Sell 1 OTM Strike Call

Maximum Profit:Strike Price of Short Call - Strike Price of Long Call-Net Premium Paid

Maximum Loss:Net Premium Paid

Breakeven:Strike Price of Long Call + Net Premium Paid

How To Implement This Strategy?

Let’s learn this strategy through an example. If the Infosys Ltd (INFY) stock is trading at INR 1130 and as a trader if I expect that INFY will do marginally well and move up to INR 1200 on the expiration date of 28th March 2018, then, to monetize on this view, I will buy an INR 1160 strike call for INR 20.

Source: nseindia.com

If my view is right and the stock moves to INR 1200 then the 1160 strike call will be in the money by 40 points and post deduction of the premium, the net profit will be around INR 20 but if my view is wrong then I will lose out on the premium of INR 20. A risk of INR 20 for a reward of mere INR 10 doesn’t look the right thing to do.

This is when the Bull Call Spread strategy comes into the picture. In order to improve my risk-reward ratio what I can do is in addition to buying a 1160 strike call for INR 20, I can sell an INR 1200 strike call and collect a premium of INR 11.

Buy 1160 strike call @ 20

Sell 1200 strike call @ 11

Source: nseindia.com

This makes the net payable premium INR 9, which is nothing but the difference in the premium paid for long strike call and the premium collected from the short strike call.

As per my view if the INFY stocks move to INR 1200 on the expiration date then the 1160 strike call is 40 points in the money, the 1200 strike call has no value and after deducting the net premium paid of INR 9, the net profit is INR 31.

Considering a different scenario, if INFY stays below long call strike price of 1160. We already know if the option is out of the money on expiration date then the option expires worthless. So both the call options with strike price of 1160 and 1200 are out of the money and expire worthless. I will lose INR 20 i.e. the premium paid for the long 1160 strike call but made INR 11 as the premium collected from the short 1200 strike call. So the net loss is INR 9.

Now, what if the INFY stock price at the expiration date ends between 1160, long call strike price and 1200, short call strike price. Then, the 1200 strike call is out of the money and has no value and 1160 strike call is in the money and is worth the difference between the INFY stock price and 1160.

Here is a simple representation of my payoff on a variation of stock prices for INFY:

LS – IV – Lower Strike – Intrinsic value (1160 CE)

PP – Premium Paid

LS Payoff – Lower Strike Payoff

HS-IV – Higher strike – Intrinsic Value (1200 CE)

PR – Premium Received

HS Payoff – Higher Strike Payoff

You can download the payoff sheet by clicking on the download button at the bottom of this blog. You just need to enter the values for your option in this sheet to get a representation of your payoff.

How To Calculate The Strategy Payoff In Python?

Now, let me take you through the Payoff chart using the Python programming code.

Import Libraries

import numpy as np
import matplotlib.pyplot as plt
import seaborn

Call Payoff

We define a function that calculates the payoff from buying a call option. The function takes sT which is a range of possible values of stock price at expiration, strike price of the call option and premium of the call option as input. It returns the call option payoff.

def call_payoff(sT, strike_price, premium):
return np.where(sT > strike_price, sT - strike_price, 0) – premium

# Infosys stock price
spot_price = 1130# Long call
strike_price_long_call = 1160
premium_long_call = 20# Short call
strike_price_short_call = 1200
premium_short_call = 11# Stock price range at expiration of the call
sT = np.arange(0.95*spot_price,1.1*spot_price,1)

Long 1160 Strike Call Payoff

payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,label='Long 1160 Strike Call',color='g')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

Short 1200 Strike Call Payoff

payoff_short_call = call_payoff(sT, strike_price_short_call, premium_short_call) * -1.0
# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_short_call,label='Short 1200 Strike Call',color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

Bull Call Spread Payoff

payoff_bull_call_spread = payoff_long_call + payoff_short_call

print "Max Profit:", max(payoff_bull_call_spread)
print "Max Loss:", min(payoff_bull_call_spread)# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,'--',label='Long 1160 Strike Call',color='g')
ax.plot(sT,payoff_short_call,'--',label='Short 1200 Strike Call ',color='r')
ax.plot(sT,payoff_bull_call_spread,label='Bull Call Spread')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.Enroll now!

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download Data File

Bull Call Spread - Python Code

Bull Call Spread - Payoff Excel Sheet

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
