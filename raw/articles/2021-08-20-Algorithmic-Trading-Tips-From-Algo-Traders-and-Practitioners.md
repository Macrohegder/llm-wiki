---
title: "Algorithmic Trading Tips | From Algo Traders and Practitioners"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/algorithmic-trading-practitioners-tips/"
date: "2021-08-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Algorithmic Trading Tips | From Algo Traders and Practitioners

**来源**: [QuantInsti](https://blog.quantinsti.com/algorithmic-trading-practitioners-tips/)  
**日期**: 2021-08-20  
**作者**: QuantInsti

---

## 原文

7 Useful Tips From Experienced Algorithmic Trading Practitioners

ByChainika Thakar

Having an experience inalgorithmic tradingcomes from possessing the knowledge required for it, years of perseverance along with some trial and error. And when you embrace the useful tips from experienced individuals in the domain, you can build upon the practical knowledge much faster.

As abeginner in the algorithmic tradingdomain, the practical approach to execute favourable trades is yet another turning point right after you gain theoretical know-how. In this article, let us find out what the experienced practitioners at QuantInsti suggest when it comes to trading with the help of algorithms. Enhance your strategies with these insightfulAlgorithmic Trading books.

7 useful algorithmic trading tips from experiencedtop algorithmic tradersand practitioners:

Strategy paradigms are integral

Get a reliable financial data vendor

Be cautious when trading leveraged products

Learn to backtest systematically and backtest any trading idea rigorously

Paper trade before trading live

Risk management is the key

Read as many trading books as you can and be updated with new technology

Be sure to check out this video which briefly explains algorithmic trading.

Strategy paradigms are integral

First and foremost, you need to have the knowledge of thestrategy paradigmsand why these are important. Thestrategy development in live tradingis the most crucial part, and thus, should be done in a sequenced manner.

You start with the hypothesis of trading strategy, then do the coding, thenbacktestingand then walk-forward testing. This process ends with trading live in the market.

Get a reliable financial data vendor

Getting a reliable data vendor is another important thing when it comes toalgo trading. A financial data vendor provides data from the financial markets.

Used by traders and investors, the financial data vendor provides you themarket dataafter formatting and making it error free. For instance, data for SPY(live as well as historical) can have duplicates in the data, missing data values, etc. is erroneous and may lead to  imprecise results if used for creatingtrading strategies.

Firms such as Bloomberg, Thomson Reuters and Moody’s analytics are common examples of market data vendors.

Be cautious when trading leveraged products

While trading theleveragedproducts in the financial markets can help you gain on the borrowed or leveraged part of the total trade, it also poses a risk of losing more than you possess.

Let us assume that you hold a position of $100,000 with the leveraged funds in the market but yours is only $500. If the financial market goes up, you will be in a position to settle for a gain. Let us say the market goes up and your position in the market becomes $102,000. In this scenario, you will be gaining $1500 over and above the investment of $500 of your own.

On the contrary, let us suppose you find that the market falls, and your position in the market is sitting at $98,000. In this case, your loss will be $2000 on your initial exposure of $100,000. This makes it clear that you not only had to bear the loss of your own $500 but also will be additionally coughing up $1500 since the brokers usually make amargin call.

Margin call is initiated by the broker. In case the value of your account falls below the set threshold, your broker asks you to deposit more funds in the account. This happens because the broker tries to secure himself in case the account loses value and you are not able to repay the debt.

If the market value goes down, the best an algorithm can do is put a stop limit order or stop loss order on your leveraged product (exit the market) and save you from incurring huge losses when the market price starts falling. But, the initial loss still exists as and when the market value of the broker account goes down.

Using leverage in some securities such asETFs have more risk than others. ETFs have some costs associated with them such as expense ratio, taxes and turnover costs. Besides the additional loss, the trader is also needed to incur the expense of these costs.

However, you can manageleverage with hedge fundssince hedge fund managers know exactly when to use the leverage and when not, in order to save themselves from incurring huge losses. Hedge fund managers are usually private entities and require a minimum investment of the capital which they maintain or trade with in the financial market.

Learn to backtest systematically and backtest any trading idea rigorously

Traders usually lose funds because of not making the trading decisions on the basis of sound research and backtesting. It is extremely important to remove emotions from your trading decisions andbacktestthe strategy or the trading idea. Backtesting is the process of testing a trading hypothesis/strategy on the historical data. The Quantra course onbacktesting trading strategies pythonteaches you exactly how to do this systematically, covering overfitting, look-ahead bias, and proper performance evaluation.

Let us try to understand this better. Assume you have a trading hypothesis that states positive returns of the particular securities over the next two months. This hypothesis is on the basis of positive returns having occurred in the past two years.

Now, testing this hypothesis and knowing whether the strategy will work or not are the two main things here. This hypothesis can be validated with the help of backtest which implies finding out the performance of a trading strategy on the historical market data.

For instance, inmomentum trading strategy, the investors buy financial securities when they are rising and sell them when the peak is assumed. Here, the hypothesis can be a positive rise of the equity for a time period of two months. After two months the equity will reach its peak because this has happened in the last one year.

Let us say the return on all stocks of NIFTY 50 is expected to be 3%. This expectation states the hypothesis that the return will be 3% but to test the hypothesis we usehypothesis testing.

A good backtester makes sure that the following drawbacks or biases do not occur which have the potential to change your backtesting results:

Overfitting- When overfitting occurs, the backtest result of the trading strategy shows good performance of the strategy on the historical data but is likely to underperform on any new data.

Look ahead bias- Using the information in the backtesting before it actually appears in the public view is look ahead bias. It can lead to skewed results during backtesting. For instance, if you are assessing the impact on the stock market due to the quarterly earnings report of your organisation, you will be assuming the report which is yet to come at the end of the quarter.

Survivorship bias- A bias that occurs when only the winners are considered while analysing the historical data, whereas the losers are not taken into account. Hence including the whole universe of data while backtesting is extremely important. For instance, some mutual funds may have performed better in recession but other mutual funds may not have. But investing in mutual funds in the next recession taking into account only those which performed well in the last recession will be a survivorship bias.

Ignoringtransaction costs- The trading/transaction costs such as commissions, taxes and slippages are extremely significant while backtesting the strategy. Including these costs gives a true picture of the strategy's returns.

Moreover, there is no fixed number of times you should backtest your strategy. You can tweak the strategy a number of times. But, constant tweaking can lead to overfitting, so make sure you do not overdo it.

Once you are done backtesting, you can consider your trading strategy for paper trading first and then live trading.

Paper trade before trading live

If you are satisfied with the backtesting strategy performance, then you can start paper trading. And once the paper trading results are satisfactory, you can start live trading. This way, you ensure the accuracy of your strategy.

Process of Paper trading and Live trading

Some of the benefits of paper trading are:

There isno risk and no stressof losing money in paper trading since it is not an actual trading practice. Paper trading only helps you with an idea of the results an actual trading will provide.

The trader gets topractice tradingin the actual financial market scenario. Hence, a good experience can be gained in every element of the trading process from pre-market preparation to final profit or loss taking.

Now, the real question is “for how long should you stick to paper trade before going live?”

And the answer to this is not more than a month or so should you be paper trading because the experience you will get from live trading will be very different from the experience gained from paper trading.

Hence, the lessons learnt in live trading will be really useful for understanding the real market scenario where your actual money will be at stake. Nevertheless, you must manage the risks in the live market which we will discuss in the next section.

Recommended viewing:How Paper trading can make you a better trader

Risk management is the key

Risk managementin trading is essential for managing the risk of bearing the losses arising from the downward trend in the financial markets. This is possible in events like Covid-19, tsunami, etc.

Let us take a look at this table which is an example of how crucial it is to keep a check on your losses, because with every 5% extra loss, your percentage of gain needed to recover the losses increases. This simply implies greater the loss, harder it is to recover:

Percent loss

Percent gain needed to recover and get back to even

Source:Medium. Credits: Rishabh Mittal

Risk management involves identification, evaluation and mitigation of risks which usually arise when the market moves in the opposite direction from the expectations.

So, it is really important to set your expectations on the basis of a thorough analysis of the market after anticipating all the known risks and being prepared for anyblack swan events.

Trendsare the most important factor here. A trend implies the general direction or momentum of the market, asset price or other such measures. And a trend gets formed by the investors’ risk appetite which implies the risk anticipated in case of certain events such as elections (political events), interest rate decisions (economic events) and new advancements in technology (business events).

This was about the risks in the financial markets. Another isoperational risk(OR) which is the risk that a trader faces due to a failed internal process or system/network flaw.

OR involves a wide range of “non- financial problems” such as:

Technology risk where a computer system or network architecture is not updated, or there is incompetence in the personnel using them.

Lack of structured risk policies.

Process-related risks such as possibility of error in information processing, data transmission, data retrieval and inaccuracy of result or output.

Other risks include lack of proper monitoring of risk, employee’s or management’s involuntary errors, employee or management frauds or criminal activities.

Finally, it could include losses due to natural disasters, terrorism and so on.

Hence, after anticipating the risks, you can invest in the stock market weighing your anticipated risks with your anticipated gains.

Suggested read:Portfolio & Risk Management

Read as many trading books as you can and be updated with new technology

Reading trading books is the best way to increase your knowledge regarding algorithmic trading and become a professional trader. If you're new to the domain of algorithmic trading and quantitative trading, check out thesefree resources to learn algorithmic trading.

Dig into various concepts like market microstructure, statistics & econometrics, technical analysis,options trading, advanced statistics, machine-learning and Python via theseessential books on algorithmic trading.

For additional learning, you can check out thesefree resources to learn machine learning for tradingreplete with the latest information and informative resources.

These resources are particularly valuable for those exploringalgo trading for beginners, offering a well-rounded understanding of core topics and practical tools to kickstart their journey in this field.

Conclusion

In this article we aimed to cover the essential tips straight from the experienced algorithmic traders. These 7 tips are concise yet the most effective ones while beginning algorithmic trading practice.

You found out that any strategy making requires a step-by-step process which is the most crucial for strategy building. Then, getting a reliable data vendor and being cautious with regard to investments are the key to success in algorithmic trading.

Right before you take the execution step in the live market, you must backtest and paper trade. Last but not the least, reading as many trading books as possible will keep you up to date with the advancing scenarios.

Also, reading can help you with a lot of different perspectives coming from experienced individuals in the algorithmic trading domain. With increasing participation from retail traders and professionals,algorithmic trading in Indiais also evolving rapidly as more traders adopt systematic, rule-based approaches.

You too can gain essential skills required for different Quant trading desk roles such as trader, analyst, developer in about 40 hours withLearning Track: Algorithmic Trading for Everyone. Perfect for traders and quants who want to learn and usePython for tradingto learn different trading strategies includingDay Trading, Machine Learning, ARIMA, GARCH, and use Options Pricing models. Enroll now!

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
