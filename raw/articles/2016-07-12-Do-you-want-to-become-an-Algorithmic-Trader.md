---
title: "Do you want to become an Algorithmic Trader"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/candid-conversations-algorithmic-trader-2/"
date: "2016-07-12"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Do you want to become an Algorithmic Trader

**来源**: [QuantInsti](https://blog.quantinsti.com/candid-conversations-algorithmic-trader-2/)  
**日期**: 2016-07-12  
**作者**: QuantInsti

---

## 原文

Candid Conversations with an Algo Trader (Part 2)

If you don’t know who you are, the stock market is an expensive place to find out -George Goodman

In theprevious post, I had a conversation with a few experts in the field of Algorithmic Trading to gain some insights into this seemingly “black-box”. That conversation not only helped me dispel some of my doubts regarding Algo Trading, but it also strengthened my desire to jump headfirst into a world dominated by complex mathematical models, managing positions instock market, and coding woes.

So, here I stand, ready to take the plunge. I am told that I don’t need a university degree in finance or computer science to become an Automated Trader. Of course, to succeed in the field, I do understand that a formalized education will be highly beneficial, but right now, I am just scratching the surface here. Although, my engineering background does give me certain leeway into the understanding of financial mathematical models and programming.

Yet, the road seems bumpy. I still have a truck load of questions going through my head. How much knowledge of the markets is good enough to start trading using algos? Where can I verify my trading strategies? How can I make my strategies profitable? What are the“Must Dos”and“Rule-of-the-thumbs”of the field that I need to follow?

I guess I need to sit down with an expert all over again, over a cup of steaming hot latte, to clear the air.

So, I have read some literature on Algorithmic Trading and eventually want to set up my own trading desk. What path do you recommend?

So, I have read some literature on Algorithmic Trading and eventually want to set up my own trading desk. What path do you recommend?

If your idea is eventually to have your own setup, you would need to build expertise in quant and/or programming. To start with, I would recommend you to master at least one of the programming language commonly used by Quants and Algo traders (Matlab/Python/R), because that is an essential ingredient. Of course, the skills that you will develop in any one of the languages will be useful for others as well. The best way is to get your hands dirty as soon as possible. Start learning about the markets. Build your knowledge on charting. Read about different kind of strategies used by traders in the market. Perhaps, the important thing is to understand the basics of market inefficiency and to capitalise on it by building a strategy around it. Once the strategy is in place, backtest it on historical data to remove the inaccurate assumptions you might have had. If all goes well, you should be able to trade with this strategy in live markets.

What do you mean by Market inefficiency?

What do you mean by Market inefficiency?

A situation where live prices of stocks or securities do not accurately reflect their true value. In an inefficient market, some securities are overpriced while the others underpriced. This gives a certain risk or in some cases, opportunity to make money for the traders.  Ever heard of the term “Statistical Arbitrage”?

Yes. Isn’t it a fancy word for pair trading? I would like to know more about it.

Yes. Isn’t it a fancy word for pair trading? I would like to know more about it.

That is only partially true. Pair trading is one of the many kinds of statistical arbitrage.It is also a type of market inefficiency. Being quite popular amongst Algo and High-Frequency Traders, It is actually an evolved version ofpair-trading strategies, in which stocks are put into pairs by fundamental or market-based similarities. When one stock in a pair outperforms the other, the poorer performing stock is bought along with the expectation that it climbs its outperforming partner, and the other is sold short. This hedges risk from whole-market movements.

That does seem logical. So what do you opine as the most important things to keep in mind while designing a trading strategy?

That does seem logical. So what do you opine as the most important things to keep in mind while designing a trading strategy?

There is no direct answer to this question, as it’s a mix and match of several things. You need to understand how the market operates and determine the entry and exit points accordingly. As far as my experience goes,recognising when to exit the market and identifying stop loss is more difficult than the entry position. Every strategy is unique, and therefore in need of its own customised positions.

Once your strategy is ready, it is good idea tobacktestit against historical data. However, there is an element of caution to be exercised when backtesting. E.g. a trader wants to test a strategy based on the notion that Internet IPOs outperform the overall market. If you were to test this strategy during the dotcom boom years in the late 90s, the strategy would outperform the market significantly. However, trying the same strategy after the bubble burst would result in dismal returns.

Therefore it is important to prepare a contingency plan, as no strategy will work in all prevailing market conditions. Drawdown is unavoidable, and it should be incorporated in the trading strategy. Remember, a good strategy is not a slave of technology. You can hire a programmer to implement your trading strategy, but not vice versa.

NinjaTrader is a free to use platform in case you want to put your algorithms to test. There are a lot of otherfree backtesting toolsthat can be looked into, if you want more information.

I like your point about the exits, as I understand that any trading strategy is not devoid of risk. How are the risks handled in an Algo Trading system?

I like your point about the exits, as I understand that any trading strategy is not devoid of risk. How are the risks handled in an Algo Trading system?

You should understand thatrisk managementand its reduction is one of the most critical areas of Algorithmic Trading. The market is full of oddities and once you realise that you are on the verge of losing money, your algorithm should check out of the deal. That is the reason that exit points of an Algorithm are more important than the entry points.

Algorithmic risk can be categorised into several things: Consistency, Quality, Scalability being a few of them. Consistency means that the data which is being fed to the system is not old or outdated.Market data packets have time-stamp embedded in them. The advanced exchanges in the world are adopting concepts like time-syncs to atomic clocks. Your algorithmic trading system should be able to track these time-stamps to ensure the data you are getting is indeed fresh.

For any normal trading activity, you have to take care of market risk, financial risk, regulatory risk, liquidity risk and credit/counter-party risk. In addition, algorithmic traders also need to prepare for the statutory risks.There are two places in an Algorithmic Trading system where the risk has to be handled: within the application and before generating the order in the Order Management System.India, having one of the most stringent regulatory environment, a lot of these algorithmic trading related risks have to be mandatorily checked in the system before an order flows out. This makes risk controls and system-level checks especially critical for anyone building analgorithmic trading setup in India.

Wow! That’s a whole lot of risk managements that we are talking about here. But I would want to take a step back and ask you about the Order Management System

Wow! That’s a whole lot of risk managements that we are talking about here. But I would want to take a step back and ask you about the Order Management System

Order Management Systemor OMS as it is called, is the pathway through which the orders are routed to their correct destinations. Orders need to contain the security identifier, order size, price limits, order type and conditions, type of algorithms used, to name a few.This information is usually entered via a winform by the end user but for fully automated systems no winform is required, however in both cases it is recommended to have each order object stored in a relational database for record keeping.

Once the order is captured by the system, it needs to be routed to the required destination. As most systems receiving the order have their own proprietary protocol, order routing requires each order to be encoded in the correct format.

There are several checks in place to make sure that order information is correctly sent and received. The venue will run various checksums and order length so that the FIX engine can confirm that the order received matches the expected order transmitted. The order manager also performs risk checks before sending out the order.

Well, well. I guess I will stop my queries for now. I have got some really great insights from your talks. Probably I should just start with some programming tutorials to get me started.

Well, well. I guess I will stop my queries for now. I have got some really great insights from your talks. Probably I should just start with some programming tutorials to get me started.

That’s a good idea. Here are a few resources where you can look for. AggregatedReading listfor Algorithmic Trading

Step Ahead

If you had any such conversations with an Algorithmic Trader or Market Expert, do share with us in the comments section below.

If you are a coder or a tech professional looking to start your own automated trading desk.Learn algorithmic tradingfrom live Interactive lectures by daily-practitioners. OurAlgo trading course, Executive Programme in Algorithmic Trading covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading.

---

*Imported from QuantInsti Blog on 2026-04-27*
