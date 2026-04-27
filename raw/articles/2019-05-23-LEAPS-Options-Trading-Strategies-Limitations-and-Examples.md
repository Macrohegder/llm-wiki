---
title: "LEAPS Options: Trading Strategies, Limitations and Examples"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/leap-options/"
date: "2019-05-23"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# LEAPS Options: Trading Strategies, Limitations and Examples

**来源**: [QuantInsti](https://blog.quantinsti.com/leap-options/)  
**日期**: 2019-05-23  
**作者**: QuantInsti

---

## 原文

LEAPS Options: Trading Strategies, Limitations and Examples

LEAPS (Long-Term Equity AnticiPation Securities) are a special type of options which were born out of demand for investors who were looking for a long term investment but did not want to lock in their investment for that amount of time.

In this article, we cover the following topics:

What are LEAPS?

Example of LEAPS

LEAPS options strategies

Limitation of LEAPS

Before we move on to the main topic, make sure you understand thebasics of options trading. After that, you can refer to the followingoptions trading courseto refresh your knowledge.

What are LEAPS?

Long-Term Equity Anticipation Securities (or LEAPS for short) are a type of options contract whose expiry is always more than a year, some even going as far as three years. Typically, options were inherently short-term and were offered in the range of 3, 6 and 9-month ranges.

Eventually, there were individuals who were looking at the long term horizon for a certain asset but did not want to own it outright. Keeping this in mind, LEAPS were introduced, wherein an individual could participate in the long term market movements without significant capital at hand.

A point to note is that LEAP options are generally priced higher than other short term contracts and thus, you might have to consider a higher delta ie a deep ITM option (usually more than 80 or 0.8) to make sure that you end on the profitable side of the trade when the time comes for its expiry. Of course, just like options, you can use the greeks to evaluate a LEAPS option.

LEAPS aren’t designated as LEAPS on broker platforms and thus, you have to look at the expiry date to know that it is a LEAP option.

Remember, LEAPS last for more than a year.

Example of LEAPS

Let’s take into account the data for Apple options (as of May 02, 2019)

Stock price: 210.52 The options call prices for a strike price of 185 for different expiry dates are as follows:

In the table above, the option with the expiry date as June 18, 2021, is a LEAPS option. We can interpret it in the following manner.

We expect the stock price of Apple to stay upwards of $185 by June 2021.But why would someone sell a call option for a strike price which is less than the current stock price?

This is due to the fact that different investors can interpret the stock in a different manner and thus, the LEAPS call option seller would think that this is a good strike price where they would find a buyer at the option premium they want. There is also the fact that the option buyer has to take into account the option premium which will be added to the strike price when he calculates the potential profit.

Thus, we will buy a LEAPS option call for a price of $45.61 which will expire on June 18, 2021. In this scenario, the breakeven price for the buyer would be $230 (Strike price of $185 plus Option premium of $45.61).

LEAPS options strategies

While it seems that there is not much difference between LEAPS and normal options, investors look at it differently and have found various applications depending on their own risk profile.

We can see that in this case, the option premium is comparatively more expensive than the other options too. Let us now see some strategies when buying a LEAPS option which will make more sense than buying the stock itself,

Looking forward to a bull run of a specific stock in a year from now

Let’s assume that you have executed a fundamental analysis of a company and feel the stock price, while in the short term is all right, is not sustainable in the long term and can decline later.

Since going short will lock your investment for a considerable amount of time, you can buy a LEAP put option at a specific price so that you can exercise the option of selling the stock which should be greater than the (then) current stock price, thus making a profit.

Another advantage of a LEAPS put option over shorting a stock is the fact that you won’t be forced to close your trade if the price closes below the stop loss limit and you receive a margin call.

Let’s understand this with the help of an example. You have gone through the history of Tesla and feel that its main product, ie electric vehicles cannot be mass adopted in the next two years.

Right now, the share price of Tesla is $234.1. Let’s suppose we expect the stock price to decline as low as $150. Here, the investor looks at the option chain and buys a LEAPS put option for a strike price of $230 at a premium of $61.29.

To breakeven for the investor, the stock price should be ($230 - $61.29) = $168.71.

Using LEAPS to contain the losses in case the owned stock price declines

In this scenario, the long term investor has invested in a stock which they are sure to reap a profit from. However, the investor feels that they shouldn't be caught with their pants down in case the stock price goes the other way.

Hence, in this case, the investor will buy a LEAPS put so that even if the profit is reduced due to buying the option premium, they have put a cap on the maximum loss they will have to bear in case the stock price goes below the strike price.

Let’s say you have bought 1000 shares of Intel on Sep 13, 2018, at the price of $45.57. The stock price on 1 May is $50.76. Thus, the total investment is $45,570.

Now, while you do feel pretty confident about the long term, you feel that if you can reduce your potential profit by a minuscule amount but put a definite limit on the potential losses when you exit the market in 2 years, you look at the LEAPS option chain and try to find a suitable LEAPS put option.

One LEAPS put option which expires on Jan 15, 2021, has the strike price of $45 and a premium of $3.9. Thus if we were to buy the LEAPS put options for 1000 shares, the effective price is ($3.9 * 1000) = $3900.

Now, this means that the stock price will have to go beyond ($45.57 + $3.9) = $49.47 to book a profit. But if you look at the other end, we can see that if the stock price goes below ($45 - $3.9) = $41.1, we can contain our losses which wouldn’t have been possible if we had just bought the stocks. The gist is as follows,

Without LEAPS put option, we would have to sell the stocks at the market price which would have magnified our losses.

If the stock went as low as $35, we can exercise our LEAPS put option and sell the stock at the strike price of $45, ie ($45*1000) - ($3900) = $41,100. And without the LEAPS options, we would have to sell it for the stock price ie ($35* $1000) = $35,000. Another way is that we can sell the put option before the expiry date because as the price declines, the value of the put option will increase and thus, we can potentially cut our losses in this manner too.

The price trend of Intel for the past 5 years is just given as a reference.

A point to mention is that we can apply this strategy to the entire portfolio instead of just one stock.

The Bull Call Spread LEAPS options strategy

Yes, the relatively well-known bull call spread can be applied to the LEAPS as well. In a nutshell, it involves buying and selling LEAPS options on the same underlying security with the same expiration date, but with different strike prices. This strategy helps us improve our risk-reward ratio. To understand the strategy and how to code it in python, you can refer to the followingarticle.

The strategies mentioned above can be applied on the index too. Just like a single stock, one can buy LEAPS options for an index such as the S&P 500 as well. However, it is only advisable for the hardened investors as we have to understand the entire market structure to carefully assess its direction a year or two from now.

Bear in mind that we have not taken into account the transaction costs, brokerage etc. which would have an impact on the profitability of a certain strategy.

Thus, so far we learnt how LEAPS work and a few strategies where we would prefer LEAPS over the underlying stocks as well as other near term options. However, there are two sides of a coin and in the next section, we will understand the limitations of owning a LEAPS option.

Limitation of LEAPS

While a LEAPS option can be advantageous over a stock when it comes to the investment amount, a major disadvantage is that LEAPS have an expiry date. As we know, stocks can increase substantially in a short period. It will be of no use to the LEAPS call option holder if the stock increases after the option has expired without being exercised.

Due to the high premium paid to buy a LEAPS Option, it takes a longer time for the LEAPS Option holder to break even when compared to a person who owns the underlying stock.

The fact that a LEAPS option is made so far off in the future (some can be bought for even 3 years from the current date), it becomes difficult to predict the correct price which gives both, a decent return on the investment as well as an option premium which is not too expensive.

Unlike stocks, LEAPS do not provide any dividends and will not benefit from a stock repurchase.

Suggested reads

Calendar Spread Options Trading Strategy In Python

Bear Call Ladder Options Trading Strategy In Python

Options Pricing Models – Black Scholes, Derman Kani & Heston Model

Conclusion

LEAPS are a type of options whose expiry date is more than a year. The main benefit of a LEAPS option is that a long term investor can dabble in options without worrying about the short term volatility of the market. It also helps investors invest less capital when compared to owning the actual stock. We have also seen the limitations of LEAPS which arises due to its long term nature.

You can learn more about options trading and how to create your own strategy in python by going through the courses in the "Quantitative Approach in Options Trading" learning track.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
