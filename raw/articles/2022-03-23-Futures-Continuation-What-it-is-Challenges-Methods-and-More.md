---
title: "Futures Continuation: What it is, Challenges, Methods and More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/continuous-futures-contract/"
date: "2022-03-23"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Futures Continuation: What it is, Challenges, Methods and More

**来源**: [QuantInsti](https://blog.quantinsti.com/continuous-futures-contract/)  
**日期**: 2022-03-23  
**作者**: QuantInsti

---

## 原文

Futures Continuation: What it is, Challenges, Methods and More

ByChainika ThakarandVarun Pothula

Usually, most of the trading activity is seen in a trading contract. Futures continuation contract is one of the trading contracts that helps continue a futures contract over to the succeeding month. If you are not familiar with futures continuation yet,You can begin by learning more about thefutures trading courseand it's fundamentals from our blog onfutures trading.

This blog will take you through everything from the basics to the ways of building a continuous futures. It covers:

What is futures continuation?

Challenge with futures continuation contract

Methods to build a continuous futures

Which method to choose?

Continuous futures vs non continuous futures contracts

What is futures continuation?

A contact that represents a sequence of successively expiring lead futures contracts with an associated interval during which a lead future ends before another takes over.

For example, let us take a look at a sequence of futures contracts for crude oil. The futures contract will look like this using the following contracts:

CO January’ 2022CO December’ 20211125CO November’ 2021020CO October’ 20210922

In the above list, each contract is mentioned with the date format in yy/mm/dd. For example, in the contract “CO October’ 20210922” the 2021 is the year, 09 is the month September and 22 is the date.

The above list is an example of sequential contracts and each contract shows the lead end date of the previous contract. On the end date, the previous contract stops being the lead contract and another contract takes over as the lead.

Hence, the contract expires on 22/09/2021 and the October contract becomes the lead contract. Then the next expiry date is 20/10/2021.

Next, the contract expires on 25/11/2021 and the last contract is in January 2022. That is the reason we have not taken the last expiry date in the 2022 contract.

Challenge with futures continuation contract

Futures contracts for an asset have different expiry dates (occurring within a short span of time), making their technical analysis and signal generation difficult.

For example, the lean hog futures will expire in October and December. An October lean hog futures contract will not exist after its expiry date. Hence the data will be available for a very short span of time.

By the short span of time here, we mean around three to six months. A straightforward task of calculating lean hog price crossover which is a cross of the 50-daymoving averageand the 200-day moving average is very difficult as we don't have that many data points.

But is there a way to increase the data points?

We need to stitch different expiry futures together and create a continuous futures contract to increase data points.

A continuation is a time series obtained by stitching together multiple individual series. A future continuation is a time series obtained by stitching together multiple individual futures contracts.

A very simple solution is to add the data from the next expiry when the current month futures expire.

For example, when the October lean hog futures expire on 27th October, we can append the data of the November lean hog futures contract. Unfortunately, this can lead to erroneous results as these two are different contracts.

The price on 27th October for Oct lean hog futures will be different from November lean hog futures. By simply appending the data, you will introduce artificial gaps in your time series.

Let us visualise how the artificial gap will look since the gap can make the price look as if it is going in a particular direction (down or up) while it actually is not.

For visualising, we will use Python. First of all, we will import the necessary libraries. Here we will read two futures contracts. These two contracts are the futures data for Lean Hogs of October 2020 and December 2020 expiry.

Output:

In the graph above, you can see the output that shows a sudden gap in the series. This gap is because of the difference in the price between two consecutive months. It doesn’t mean that the actual price has seen the fall.

Methods to build a continuous futures

To build a futures continuation, you need to adjust the contracts back in time. These adjustments are made as there can be a price difference between the first contract and the second contract on expiry.

One way to adjust it is by adding/subtracting a factor so that the last value of the first contract matches the first value of the second contract. This way, you can get a continuous time series.

A drawback of the adjustment by addition is that long term time series can sometimes go negative after many years of such adjustments. Another disadvantage is that percentage changes are not kept intact, which makes the calculation of returns difficult.

Let us find out a few adjustment methods to build the continuous futures. These methods are:

Proportional adjustment

Backward/Forward adjustment

Rollover/Perpetual series

Proportional adjustment

To avoid the problem of adjustment, you can use proportional adjustment. In proportional adjustment, when you are rolling from one month to the next, the first contract is shifted by a ratio instead of adding a fixed number. The main advantage is that percentage moves are kept intact, making ratio style calculations possible.

Let us take the same example as above and find out how the price rolls from one month to next. The time period of contracts goes as follows:

CO January’ 2022CO December’ 20211225CO November’ 20211120CO October’ 20211022

The two contracts will be made continuous by proportional adjustment. The ratio of the price of the second contract to the first contract (on the expiry date of the first contract) is the proportional adjustment factor.

You can get continuous futures data using the following steps:

Get the price of the first contract and the next contract on the rollover date.The rollover date is when you rolled your position from the first contract to the second contract.In this example, we have considered the rollover date as the expiry date. We will roll over from the first contract to next month’s contract on the first contract’s expiry date.

Calculate the adjustment factor as:$$ \text{Adjustment factor} = \frac{\text{Second contract's price}}{\text{First contract's price}} $$

Store the first contract's data in the variable named continuous_futures_proportional.

Multiply the adjustment factor to the continuous_futures_proportional till the expiry of the first contract.

Append the second contract to continuous_futures_proportional to get the continuous data.

Let us go step wise with Python codes now. First of all we will fetch the contract prices.

Output:

The price of the first contract on 2020-10-14 00:00:00 is $78.425.The price of the second contract on 2020-10-14 00:00:00 is $68.425.The adjustment factor to multiply to the first contract is 0.872.

The proportional adjustment you have done here is technically called the end-to-end roll with the backwards ratio method.

The end-to-end roll means rolling the contract on the expiry date of the first contract.

The backwards ratio method is another name for the proportional adjustment where the price of the current contract is preserved, and the previous contracts are adjusted.

Backward/Forward adjustment

This method of adjustment takes away the gaps the multiple future contracts may hold. Hence, the open/close of all the prior contracts on the expiry date will match.

Let us understand the backward adjustment with an example. For instance, we want the data series to be adjusted backward through the quarterly contracts of two months i.e., August and December.

Now, if the price of August contract is 718 and the price of December contract is 712, the backward adjustment method will lower all the prices for June contract by -6.00. Therefore, delta of -6.00 will be added to all the past data.

In case of forward adjustment, the method is same with the only difference being the adjustment taking place for the following contracts and not the previous ones.

Let us learn this adjustment with the help of Python:

Output:

The price of the first contract on 2020-10-14 00:00:00 is $78.425.The price of the second contract on 2020-10-14 00:00:00 is $68.425.The adjustment factor to add to the first contract is $-10.0.

You can see in the output above how futures contracts are adjusted by adding the adjustment factor.

Rollover/Perpetual series

In the continuous data series, it is not always clear when one contract needs to be predominant over the another one. This method basically solves that problem and uses a weighted average approach.

With the shift in the contract importance, the weights also shift in this method. As and when the contract expiration approaches, a considerably small percentage of the current contract and a large percentage of the new contract are used.

The weights are often used on open interest, volume or the time left until the contract expires. Hence, this method leads to a smooth transition from one contract to the other.

For example, consider five smoothing days. The price on day 1,  is equal to 80% of the far contract price (F1) which is the November price and 20% of the near contract price (N1) which will be the October price. Similarly, on day 2 the price is

P2=0.6×F2+0.4×N2

By day 5, we have P5=0.0×F5+1.0×N5=N5

The contract, afterwards, just becomes a continuation of the near price. Thus, after five days the contract is smoothly transitioned from far to near.

Let us find out how to perform this adjustment in Python. Here we will read two futures contracts. These two contracts are the futures data for lean hogs of October 2020 and December 2020 expiry.

Output:

Same way as in the backward/forward adjustment, the perpetual adjustment has adjusted the contracts to avoid any gaps in the data.

Summing the above three methods

To sum up the above three adjustment methods in the table format here is how the adjustments (mentioned in the columns) and the dates (mentioned on the extreme left column) with the rollover date(expiry of first contract) being 14/10/2021 will look:

In the above image, the “first” and “second” signify the contract columns. The addition(backward adjustment), proportional and perpetual are the three adjustment methods we just saw above.

Since the backward adjustment (addition) has happened after the rollover date (expiry of first contract) i.e., 14/10/2021, all the prices before this date are adjusted by subtracting “10” from the first contract’s prices as explained in the backward/forward adjustment section above.

Similarly, the proportional adjustment takes place by multiplying “0.8” to all the first contract prices before the rollover date. Likewise, for perpetual adjustment, the last five days (above the rollover date) including the rollover date are adjusted until 8/20/2020.

Which method to choose?

There is no standard or best method to create a continuous futures contract. The choice of the method depends on the main aim to opt for a continuous futures contract.

For example, if the aim is to be able to conduct technical analysis, by using the backward adjustment method, you can create a continuous contract and analyse the price movements in the short span.

However, as we move deeper into the historical contracts using the backward adjustment method, there is a chance of generating negative prices that can break the analysis.

So, to analyse long term trends or to perform backtesting, proportional method or roll over methods can be used and backward adjustment method should be avoided.

For doing statistical analysis, rollover/ perpetual series method would be the best choice since it smoothens the time series.

Continuous futures vs non continuous futures contracts

Continuous futures contracts

Continuous contracts are stitched contracts to build long term future charts. In a continuous contract several contracts are stitched together post expiry to form a long term chart.

You can see the above examples where the contracts’ data are appended and hence, stitched together to make one long term chart contract.

Non-continuous futures contracts

Non-continuous contracts are simply individual contracts. This contract holds the data from the inception of the contract until the expiry of the contract.

Conclusion

Futures continuation contracts exist to make it easier to solve the problem of insufficient historical data while dealing with an active futures contract. With an extremely short span of historical data available (of 3 to 6 months), it becomes difficult to conduct analysis.

We have discussed how to solve this problem with the right adjustment ways and information around the contract.

To learn more about futures continuation, find out detailed explanation in our course onFutures Trading: Concepts & Strategies. Enroll now!

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
