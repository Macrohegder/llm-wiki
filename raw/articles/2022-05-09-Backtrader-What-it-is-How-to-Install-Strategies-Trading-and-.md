---
title: "Backtrader: What it is, How to Install, Strategies, Trading and More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/backtrader/"
date: "2022-05-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Backtrader: What it is, How to Install, Strategies, Trading and More

**来源**: [QuantInsti](https://blog.quantinsti.com/backtrader/)  
**日期**: 2022-05-09  
**作者**: QuantInsti

---

## 原文

Backtrader: What it is, How to Install, Strategies, Trading and More

BySuleyman Emre Yesil

Python enables traders and investors to backtest their strategies so that they can assess whether the strategy is good or not by observing the past performance of the strategy. However, not everyone has a high level of coding skills that can implement their backtesting in the most accurate and efficient way. Thanks to the Backtrader library, everyone can backtest their strategies in an efficient and accurate way.

Find out how you can conduct a backtest with the Backtrader library in this blog that includes:

What is Backtrader?

How to install the Backtrader library?

Create your first code with Backtrader

How to backtest a strategy with Backtrader?

How to do live trading with Backtrader?

Advantages of Backtrader

Limitations of Backtrader

What is Backtrader?

Backtrader is an open-source Python library that you can use for backtesting, strategy visualisation, and live-trading.

Although it is quite possible to backtest your algorithmic trading strategy in Python without using any special library, Backtrader provides many features that facilitate this process. In general, every complex component of ordinary backtesting can be created with a single line of code by calling special functions.

For traders and coders exploring algorithmic trading, masteringbacktestingis essential for strategy evaluation and refinement. By using tools like Backtrader, you can simplify the process and focus on building robust trading strategies with confidence.

How to install the Backtrader library?

There is no special requirement for installing the Backtrader library. It also doesn’t have any dependencies. You can install this library by using the package manager “pip”.

To install the Backtrader library by using the “pip” package manager, open the command prompt (or terminal for Mac users) then type the below code:

pip install backtrader

You can check whether it is installed successfully by trying the following code:

Although there are no dependencies, to use plotting features of the Backtrader library, “matplotlib” is required. You can install this library by using the same way.

Please note that the latest version of the matplotlib library may cause some errors while using it with Backtrader. It is compatible with version 3.2.2 of the matplotlib library. Therefore, you need to specify this version while installing.

pip install matplotlib==3.2.2

Now you are ready to use Backtrader with its full functionality.

Create your first code with Backtrader

In this part, you will go through the core components for creating a backtesting framework with the Backtrader library. As with all external libraries, first, you need to import the Backtrader library.

import backtrader as bt

The first thing you need to know about this library is the Cerebro class. It is the core of the library in which most of the works are done. It is an engine that fetches data, simulates the strategy and presents the findings and alternatively plots the inputs and the outputs.

You can create the Cerebro engine and add data, strategy and other inputs such as starting investment amount and commission and run it by the following code:

Before going into another important component of Backtrader which is the strategy class, let’s check the ways for fetching the data. In the code above, “adddata()” must include your data as a parameter.

Therefore, before this line, you need to import data online or offline. Here are the two different options for reading data for Backtrader’s Cerebro:

Note:Recent updates to the yfinance library (v0.2.51 and above) return multi-indexed DataFrames and auto-adjusted prices by default. To use this with Backtrader, you must flatten the multi-index structure using .xs() and ensure consistency using auto_adjust=True.

How to backtest a strategy with Backtrader?

To backtest a strategy, you need to define a strategy class and add this strategy to the Cerebro instance by typing the name of the class inside the parenthesis in the above code.

In this part, you will go through the components of the strategy class. These components are the functions used for variable definition, trade actions logging and signal generations.

The first function is log():

This function is used for outputting the information which you would like to save and print. We will exemplify this function while explaining another function of this class, next():

This is a simple example that prints the closing prices. During the backtesting, this function is where you generate signals.

For example, let’s employ a strategy where it sells when the price drops below the 100-daymoving averageand buys when it crosses above the 100-day moving average.

However, before writing down this strategy, you should know another function of Backtrader, “__init__(self)”. This function is where you define the variables and indicators you use in your strategy. Thanks to Backtrader’s indicators feature, you can easily calculate technical indicators.

For this strategy, we need to calculate 100-day moving average. You can define this indicator by the following code:

Now you can create your custom strategy function to generate orders. Let’s say the entering rule is the one described above and the exit rule is keeping the position for 4 periods.

To summarise so far, we have created 3 functions for our strategy class. The first function is for logging which prints actions when we call it. The second one is the main function ("__init__") where we define variables and indicators for our strategy. Then, we created the “next()” function to define enter and exit rules.

The last function is for checking whether our order sent via “next()” function is executed or not. This function is called “notify_order()”. This function is called to notify of order status.

Now you are ready to backtest a strategy. Here is the complete code for backtesting this simple strategy.

How to do live trading with Backtrader?

Backtrader has three options for live trading. These are Interactive Brokers, Visual Charts and Oanda. The base logic is the same during live trading. It just needs a couple of adding to be able to send actual orders instead of opening simulated ones.

For example, to go live-trading on Oanda, first, you need to install “oandapy” by using package manager “pip”:

pip install git+https://github.com/oanda/oandapy.git

Now you can use your broker by the following code:

To instantiate a data feed from Oanda, you can use the following code:

data = oandastore.getdata(dataname='EUR_USD')

You can review Backtrader’sdocumentationfor live trading for details and the ways for connecting the other brokers.

Advantages of Backtrader

There are many advantages of Backtrader when it comes to backtesting. First of all, it is really powerful and fast. Despite having a lengthy dataset,event-driven trading strategyallow you to obtain the results of a backtest in mere seconds.

Secondly, you can employ your trading strategy for live trading. If you choose not to use Backtrader and instead manually learnhow to backtest a trading strategy, you will also need to create a trading bot from scratch to eventually employ that strategy in a live market. This customPython trading botapproach offers the most flexibility for complex strategies that require non-standard data handling. However, while Backtrader simplifies the process by requiring only a few lines of code for deployment, building your own system ensures you understand every gear in your execution engine.

Another important advantage of Backtrader is that you can get performance metrics of your strategy and plot the results with just one line of code. Plotting is important because it plots almost everything related to your strategy.

Here is the graph produced for our sample strategy.

In the graph, you can see your trading signals and the change in your investment at the top. Below that, you can see which trades were profitable and which are not. Also, you can observe the levels you buy and sell with green up and red down signs.

It has also this easy to understanddocumentation pagethat you can find code syntaxes and examples for all part of this library.

Limitations of Backtrader

Although there are many advantages of Backtrader, you may also encounter some disadvantages. First of all, since the library has a lot of features and it aims to make the event-driven backtesting process applicable to many strategies, some may find it complex. Therefore, sometimes the effort you have to put to implement your strategy into the Backtrader framework can be too much.

Secondly, data feed options are limited. You can either use public data feed options or data feed from the three brokers which Backtrader supports live trading.

Finally, it can be very difficult to backtest a strategy for options. Backtrader can backtest options as OHLC time series but for now, it doesn’t have any further features for handling multiple expirations dates and strike prices.

Conclusion

Backtrader is a very useful open-source Python library developed forbacktesting trading strategiesvery quickly and accurately. Although it seems complex, you will realise that you can start backtesting a lot of strategies by only changing the signal generation conditions.

To summarise the strategy class creation process, you can define the variables such as technical indicators used in the strategy under “__init__()” function. To print the actions such as order creation during the backtesting, you need to call the “log()” function by passing the text you would like to print.

There is also “notify_order()” function used to print whether the order sent after signal generation is completed or not. Finally, the “next()” function is where you define the signal conditions.

Please note that you do not necessarily have to make changes to the “log()” and “notify_order()” functions. You can use them without making any changes. To create a strategy class for your strategy, you need to make changes to “__init__()” and “next()” functions.

You can check out theswing trading strategies courseon Quantra and apply it in the real world when you are satisfied with the results.

File in the download:

Backtrader - Python Notebook

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
