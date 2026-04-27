---
title: "Trading Strategy Example In C++"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/an-example-of-a-trading-strategy-coded-in-c/"
date: "2015-10-02"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Trading Strategy Example In C++

**来源**: [QuantInsti](https://blog.quantinsti.com/an-example-of-a-trading-strategy-coded-in-c/)  
**日期**: 2015-10-02  
**作者**: QuantInsti

---

## 原文

An Example Of A Trading Strategy Coded In C++

Anytrading strategycan be broken down into a set of events and the reaction to those events. The reactions can get infinitely complex and varying but essentially strategy writing is quite simply put exactly that.

The kind of events and their frequency would depend on the markets and the instruments on which this strategy would be working on, however, broadly speaking most markets would have different flavours of the following:

Kind Of Events

Market data changing- This could mean the prices changing or the sizes changing. It could also be the Last Traded price.

Reports from the exchange- Acknowledgements from exchanges, rejects, etc.

Execution of orders- Partial of full execution of orders that were placed earlier.

Orders being sent to the exchange- Some book-keeping that might need to be done just after sending an order to the exchange, perhaps for risk management.

Interval events- This is not a market-related event but more like some logic that needs to be run at regular intervals. For eg, candle formation.

New portfolio being loaded- A new portfolio being loaded might change the risk limits of other portfolios already running and hence the need to reduce the order sizes etc.

User parameters changing- Every strategy requires a certain set of user inputs or parameters which define the framework within which the strategy operates. This could range from quoting order size to the maximum exposure that the strategy can take, etc. Any of these parameters changing can and usually will warrant some amount of recalculation.

The Strategy

As an exercise, we can look at a very simplequantitative trading strategyand see how we break down a premise into the reaction to events. Let us consider a purearbitrage strategywhich essentially is based on the fact that the same instrument being quoted on different destinations should ideally have the same value. If there is any discrepancy in the value great enough to justify buying in one exchange and selling in the other we do so. So let's say we want to make a spread s out of every buy and sell. So the proposed strategy would be to quote on instr1 at a price

Buyprice = bid2-s

SellPrice = ask 2+s

Where buyprice and sell price are prices of the buy order and sell order respectively on instr1.

Bid1 and ask1 are prices of instr1.

Bid2 and ask2 are prices of instr2.

Basic logic would be to consistently keep the buy order at bid2 –s and sell order at ask2 + s. Whenever the buy order gets executed we send a sell order on instr2 at bid2. So in effect,

We bought at bid2 –s and sold at bid2 => made s out of this transaction.

OnMarketData(tick1, tick2)

{

buyPrice = tick2.bid- s

if buyorder present in instr1

replace it to buyPrice

else

send new order at buyPrice

sellPrice = tick2.ask + s

if sellorder present in instr2

replace it to sellPrice

else

send new order at sellPrice

}



onExecution{

if buy execution happened on instr1

send sell order on instr2

else if sell execution happened on instr1

send buy order on instr2

}

Clearly, as we can see, the onMarketData logic really depends only on the market data of instr2 and nothing else.

Similarly, the onExecution logic depends on the execution of orders on instr1.

Sounds good so far. This would be perfect in an ideal world where things happen instantaneously. But in the real world, we operate under certain constraints. Some such constraints are

It takes a finite amount of time for an order to reach the exchange

It takes a finite amount of time for the exchange to acknowledge an order

Replace request can't be sent on an order unless it's in an acknowledged state.

Clearly, this changes things. Consider the following timeline.

T0: buy order sent at price b1 (= bid2 –s)

T1: instr2 moves to tick~2 (bid2-1, ask2-1)

T2: Acknowledged for the order sent at T0

T10: new market data in instrument 2

At T1 our buy order on instr1 should have been replaced to bid2 – 1 –s . However, since the order is unacknowledged we could not replace it and hence the order still stands at bid2 –s and it stays there till the new market data comes at T10. Note that the acknowledgement arrived at T2. However, we did not replace our order (which was standing at the wrong price) because we decided that the quoting on instr1 depends only on market data of instr2. This means if this order gets executed at say T3, we would

Buy instr1 at bid2-s

Sell instr2 at bid2 -1 => we made s-1 (instead of s).

To avoid this one might want to react to acknowledgement reports as well.

So the new pseudocode would be

onAcknowledgement()

{

If acknowledgement is for instr1

onMarketData(tick1, tick2)

}

OnMarketData(tick1, tick2)

{

buyPrice = tick2.bid- s

if buyorder present in instr1

replace it to buyPrice

else

send new order at buyPrice

sellPrice = tick2.ask + s

if sellorder present in instr2

replace it to sellPrice

else

send new order at sellPrice

}

onExecution{

if buy execution happened on instr1

send sell order on instr2

else if sell execution happened on instr1

send buy order on instr2

}

Sounds good yet again. Until of course we dig a bit deeper. Consider the following timeline.

T0: buy order O1 sent at price b1 (= bid2 –s)

T1: Acknowledged for the order sent at T0

T2: execution of original order O1. Cover sell order sent on instr2 at bid2

T3: instr2 order execution. Nothing was done since execution is on instr2

T10: new market data in instrument 2. New buy order O2 sent on instr1

Note that from T2 and T10, there’s no buy order standing on instr1. Meaning we might be missing out on opportunities. We only step in with a buy order at T10 since the events we were listening to were market data on instr2, acknowledgement of instr1 and execution of instr1. To avoid missing out on the opportunity we will add another event to our list. Executions of instr2. As a result, well modify our pseudo code as

onAcknowledgement()

{

If acknowledgement is for instr1

onMarketData(tick1, tick2)

}

OnMarketData(tick1, tick2)

{

buyPrice = tick2.bid- s

if buyorder present in instr1

replace it to buyPrice

else

send new order at buyPrice

sellPrice = tick2.ask + s

if sellorder present in instr2

replace it to sellPrice

else

send new order at sellPrice

}

onExecution{

if buy execution happened on instr1

send sell order on instr2

else if sell execution happened on instr1

send buy order on instr2

else if execution is on instr2

onMarketData(tick1, tick2);

}

So far we are assuming that our executions happen fully or none at all. Partial executions introduce a can of worms into our neat logic. This is because this adds another constraint which we must respect:

When replacing, we have to tell the exchange what the last transaction time was. Last transaction time refers to the timestamp that every exchange assigns whenever an order is changed (acknowledged, replaced, traded, etc)

Now this leads to the following scenario

T0: buy order O1 sent at price b1 (= bid2 –s)

T1: Acknowledged for the order sent at T0. Last transaction time updated to T1

T2: MarketData for instr2 changes to bid2 – 1. Replace request (R1 with last transaction time as T1) sent to change the price to bid2-1-s

T3: partial execution of original order O1 before R1 reaches the exchange. Last transaction time updated at the exchange end to T3. Cover sell order sent on instr2 at bid2. No replace request sent on instr1 as an order is in the unacknowledged state.

T4: order rejected because exchange thinks the Last transaction time is T3 but the replace request is sent with T1.

T10: new market data in instrument 2. Replace request sent R2 sent on instr1

Between T4 and T10, the buy order on instr1 is still standing at bid2 –s (instead of bid2-1-s). This could lead to slippage if we see another execution. We have not replaced it to the right price because we are only reacting to market data on instr2, acknowledgement of instr1, executions.

Now we can add rejects to the algorithm as well.

onAcknowledgement()

{

If acknowledgement is for instr1

onMarketData(tick1, tick2)

}

OnMarketData(tick1, tick2)

{

buyPrice = tick2.bid- s

if buyorder present in instr1

replace it to buyPrice

else

send new order at buyPrice

sellPrice = tick2.ask + s

if sellorder present in instr2

replace it to sellPrice

else

send new order at sellPrice

}

onExecution{

if buy execution happened on instr1

send sell order on instr2

else if sell execution happened on instr1

send buy order on instr2

else if execution is on instr2

onMarketData(tick1, tick2);

}

onReject{

if reject on instr1

onMarketData(tick1, tick2)

}

So far we have made two very big assumptions. One, that events happen one by one and two, that our reaction to an event is instantaneous. In reality, however, events can happen simultaneously, for eg, market data and an execution of one of our orders could reach us at the same time. This means the strategy would be running two different threads in parallel. Similarly, an execution might arrive while we are processing our reaction to a market data event. If one does process events in parallel, we have to be careful with the implementation since variables like buyPosition and sellPosition might be in an inconsistent state. If you want to avoid the complexity of multi-threaded implementations, then one could always process events sequentially, then the cost would be latency. We will look into the edge cases that crop up with multi-threaded implementation and how they can be bypassed in another post.

Even in single-threaded implementations, we have not yet taken care of the user-generated events like parameter changes. For eg, what if the user decides to change the value of s. We should react to that as well instead of waiting for the next market event to replace our quotes with the right price. The essence of this post is to introduce the approach of breaking down an event and digging deeper into the flow of the logic before implementing a strategy for algorithmic trading.

Next Step

Learn how you can back-test your trading strategy in R. Our post on 'Trading Strategy Coded Using Quantmod Package In R' will take you through step-by-step process to pull historical data and code your trading strategy in R..

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download C++ Code

Trading Strategy Code In C++

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
