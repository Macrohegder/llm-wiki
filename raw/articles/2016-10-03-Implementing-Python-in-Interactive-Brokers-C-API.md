---
title: "Implementing Python in Interactive Brokers C++ API"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/implement-python-in-interactive-brokers-api/"
date: "2016-10-03"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Implementing Python in Interactive Brokers C++ API

**来源**: [QuantInsti](https://blog.quantinsti.com/implement-python-in-interactive-brokers-api/)  
**日期**: 2016-10-03  
**作者**: QuantInsti

---

## 原文

Using IBridgePy to implement Python in Interactive Brokers API

ByHari Kumar Krishnamoorthy

In the previous article onIBPy Tutorial to implement Python in Interactive Brokers API, I talked about Interactive Brokers, its API and implementing Python codes using IBPy. In this article, I will be talking about implementing python in IB's C++ API using a wrapper, written byDr. Hui Liu.

About Dr. Hui Liu

Dr. Hui Liu is the founder of Running River Investment LLC, which is a private hedge fund specialized in development of automated trading strategies using Python. Hui is the author of IBridgePy, a famous Python trading platform that allows traders to implement their trading strategies quickly.

Dr. Hui Liu obtained his bachelor degree and master degree in materials science and engineering from Tsinghua University, China and Ph.D from University of Virginia, U.S.A. His MBA was from Indiana University, U.S.A and his study interest at Indiana was quantitative analysis.

Dr. Liu’sIBridgePyis the wrapper that will help you trade in Interactive Brokers API using Python. QuantInsti hosted a highly successful webinar on this subject and we had a record number of registrants (1000+) attending the webinar which was conducted by Dr. Liu himself. I will be sharing the link to the webinar at the end of this article.

IBridgePy

IBridgePyis one of the most flexible and friendliest Python packages which can be used to implement Python on Interactive Brokers API. It is quite different from IBPy.

Well, is a third-party implementation of theApplication Programming Interfacethat is used to access IB’s Trader Workstation. While IBridgePy works differently; it does not re-implement Interactive brokers’ API. Instead it helps Python to call IB’s C++ API directly as it acts as a wrapper. Since IBridgePy calls on IB’s C++ API directly, therefore, we can expect less number of errors and exceptions in the program.

For a simple reason: Interactive Brokers C++ API is officially maintained by Interactive Brokers. In fact, when Interactive Brokers will have a new release of its platform, then the API will also be updated.

What are the benefits of using IBridgePy?

IbridgePy has some key features which make it more beneficial for users and I am going to list these as:

Flexibility

Ease of Use

Privacy

Flexibility

The best thing about IBridgePy is the fact that you can use it to trade any kind of securities. You can tradestocks, futures, options, forexetc. One of Dr. Liu’s motivations to develop IBridgePy was to make the application flexible. On IBridgePy, you can use any python package and access data source from anywhere.

Easy-to-use

The complexities of Interactive Brokers API have been completely eclipsed by theuser friendly interface of IBridgePy. You will not have to put any extra efforts to manage your orders that are pending or writing codes to get historical data or quotes from the server, as the wrapper takes care of it.

Privacy

Privacy is very important and one of the overlooked factors at times when you give out your credentials to a third party program that is running on a different server. However, IBridgePy is running on your computer, so your privacy is totally under your control.

Who should use IBridgePy?

People who are into Automated trading

Those who want to use it as a market or stock screener

How to install IBridgePy?

You can simply visit the download section of theIBridgePy websiteand download the the setup file which matches your python version. Run the file and install the necessary files.

Prerequisites

You should have the following programs installed on your system:

Interactive Brokers TWS. We have discussed in detail how to install Interactive Brokers TWS in theprevious article.

Alternately, you can also use IB Gateway (which comes along with TWS)

You should also have a python package installed on your system. Anaconda Navigator is a good resource for running python files.

You should have IbridgePy (and the set of sample programs) which you can get by writing a request to IbridgePy's email mentioned above.

TWS or IB Gateway?

Both TWS and Gateway can be used to trade. If you are relatively new to the trade, then I would recommend TWS as it is more user friendly. However, if you want to save time and avoid IB system restarts then go for the IB Gateway.

We will follow the same steps as in theprevious article. When the login screen appears, check on IB Gateway and proceed. When the IB Gateway opens, we go to its configuration, just like we did with TWS.

This will be followed by the manual configuration of the IB Gateway. Next, click on Settings. Though there is nothing to change here, we can set the port as per your need, although it is not recommended.

We will also set TWS, like we did in theprevious article. Restart TWS after configuring it.

Preparing IDE

The next important step in this tutorial is to prepare the Python’s IDE. If you are using Python(XY), then you must start the executable and run spyder from there:

Once Spyder starts, and follow these steps:

Go toViewthenPanesand checkEditorandConsole

Add the folder to thePython Pathby clicking onToolsthen selectingPYTHONPATH manager. Here you will click onAdd pathand choose the folder where you had unzippedIBridgePy.

Click oncloseto accept it.

Restart Spyder.

Running Sample Program

Click on RUN_ME.py in Spyder IDE by clicking on File and then on Open.

*RUNME.py is the program you may run this as the entrance but examplemovingaveragecross.py is the file where the trading strategy is kept.

After this, ensure that you log in to IB TWS or IB gateway. Hit on the green triangle or press F5.

Decoding the Code Structure

Just like I had discussed about the structure of the program in my previous article, I am going to talk about the code structure here as well.

We defineinitialize()which is an built-in method to claim variables which will only be run once.

Next we definehandle_data(), which is also a built-in method where trading decision is made. Two inputs are given here(context, data).Contextcontains the variables claimed ininitialize(). Whiledatais the live feed received either daily or minutely.

Line 16~ line 19:You may choose one algorithm that you want to execute by commenting out others

Line 20:Your Interactive Brokers account code

Line 21:The frequency or how often the function of handle_data(context, data),  60 means to run it every minute and 1 means to run it every second.

Line 22:There are 4 levels to show results

ERROR:only show error messages

INFO:typical users will use it to know the results of your algo

DEBUG:you may know more info when you debug your algo

NOTSET:You will see tremendous info if you really want to know what is going on

The 3 Corner Stones of IBridgePy

Here are three of the most striking in-built functions which form the cornerstones of IbridgePy:

Show_real_time_price

Request_data

Placing Order

Real-time quotes

Whenever you need real-time quotes, then you can use the built-in functionshowrealtime_price

In the above line, you will see the parameters used are CASH, EUR, USD which will return with the forex rates in real-time for the currencies specified.

Similarly, you can useSTK,AAPL, USDinstead and the value of APPLE’s stock in US dollars. STK is the security type, which we have discussed in detail in the previous article onImplementing Python in Interactive Brokers API using IBPy.

Fetching Historical Data

request_datais the function that is used to get historical data from Interactive Brokers. You will also have to specify a parameterhistoryData.

Using the parameters we select the instrument for which the historical data needs to be obtained, in the above example it is SPY which is an ETF tracking on the S&P500 index

Next we specify the time gap, in our example it is‘1 day’

Go-back period is the next parameter where we specify the period of historical data that is required. In our example it is’50 D’means go back 50 days from today.

The retrieved historical data are saved in a pandas dataframe that are saved at hist, an attribute of the DataClass, saved in a dictionary called data.

Requesting Multiple Historical Data

Just like you requested historical data from Interactive Brokers for a specific period of time, you can also fetch multiple historical data at once. Look at the code below:

I have specified SPY and AAPL and the time gap specified is1 min(1 minute) and1 dayrespectively. The period specified is1 D&10 D(D = days) respectively. Similarly, we have specified the requirements in the output function as well.

Placing Order

Order placing is the important step in our entire process and here is how we place order on Interactive Brokers using IBridgePy:

Place market orders: order(symbol(‘security’), x)

Here security is the target security, eg SPY and x is the number of shares. –x meansSELLand x meansBUY.

Eg, order(symbol(‘SPY’), 100)

The target security is SPY

The action is to BUY 100 shares when n > 0

If it was -100, then the negative number means SELL, -100 = SELL 100 shares

order_target(symbol(‘SPY’), 100) will adjust positions based on your holding positions by either BUY or SELL until you hold 100 shares

Place Limit/Stop ordersorder(symbol(‘SPY’), 100, LimitOrder(213.42)) place a limit order to BUY 100 shares of SPY at price = $213.42 per shareorder(symbol(‘SPY’), -100, StopOrder(213.42)) place a stop order to SELL 100 shares of SPY at price = $213.42 per share

order(symbol(‘SPY’), 100, LimitOrder(213.42)) place a limit order to BUY 100 shares of SPY at price = $213.42 per share

order(symbol(‘SPY’), -100, StopOrder(213.42)) place a stop order to SELL 100 shares of SPY at price = $213.42 per share

It is highly recommended to follow up on the status of the order you placed by using order_status_monitor()

Just like in the previous tutorial, we had specified an orderId, here also we specify a function orderId which is the unique identity of your order requests. For market orders, you should expect ‘Filled’ as the ending point of your order request, which means the orders have been executed at Interactive Brokers.

For limit and stop orders, the expected status is ‘Submitted’, which means the orders have been accepted by IB and waiting for executions. For high liquidity securities, it won’t take too long (a few seconds) to complete the transactions.

TheIbridgePy.Tradersingleaccountis the name of the module and it is followed by aREQUESTto buy 100 shares. This is followed by theAccount Balance.

You can watch recording of Dr. Hui Liu's webinar here.

Frequently Asked Questions

Over the years, we have seen some common hurdles faced by users who were trying to install IBridgePy and we wrote this section with the belief that it will help smoothen the process and let the users focus more on what they want, ie to apply their trading strategies.

I am not able to download IBridgePy, the link is taking me to the 404 page. Can you please help me how to do this?

Please usethislink to download IBridgePy. You will also have to make an account to access the files.

When I want to run the RUN_ME.py on Spyder it gives me a different language, why so?Something like: strategies/PK×¯ ÐÙ#ÛiW üà4YjÌµ½Z~ØpÖÑòa§;íîTOýõ#OvÔCP`ØK RäÇäwTuc]

You need to unzip the zip file you downloaded fromDownload – Easiest Python Platform to Backtest and Live Tradefirst before you access it on Spyder.

I am getting the following error:"from IBridgePy import IBCpp""ImportError: DLL load failed: The specified module could not be found."

What should I do?

The error will show up if the downloaded IBridgePy version does not match the python in your system. The other reason for the error is that there are multiple python versions installed on your system. The solution is to uninstall unmatched Python from your system.

Solution steps:

Check if the correct IBridgePy version has been downloaded. (It solves most of the issues)

Make sure that Anaconda is used if you are using Windows.

Check if multiple Python versions have been installed. If yes, uninstall the unused python version. Or, execute RUN_ME.py using the correct Python.

You can execute RUN_ME.py on Spyder using a different version of python by going to:

Tools → Preferences → Python interpreter → Setting the path of the required python interpreter

You can also do this by creating a new environment on anaconda with the required python version and then run Spyder or Jupyter using this.

I am getting the following error message:

"errorMessage=Unable to connect as the client id is already in use. Retry with a unique client id."

This is a known issue in the recent release from IB API. Whenever you start the TWS the client id is assigned and on ending the code, the client id is still active. Thus, next time you run the code you will face the error message that the client id is already in use. When a fix is released by IB in IB API, this issue will be permanently solved.

Unfortunately, meanwhile, you can restart the kernel before running the code again. And when restarted a new client id will be used and thus solve the issue.

A video guide on this can be accessed from here:Trading with Interactive Broker using Python: Unable connect as the client id is already in use.

I am getting the following error:

ImportError: Module use of python37.dll conflicts with this version of Python

Make sure that that you downloaded the correct version of IBridgePy from the website. This version should be in line with the version of python your spyder environment us using. If not, there will be a conflict.

How do I know that client running Sypder is able to connect to the server on IB TWS/ Gateway?

When after running RUN_ME.py you get an account summary similar to the following:

IBridgePy version 9.1.4

fileName = example_show_positions.py

####    Starting to initialize trader    ####

##    ACCOUNT Balance  DU229341  ##

broker_service_factory.BrokerService_callback::_get_account_info_one_tag: EXIT, no value based on accountCode=DU229341 tag=TotalCashValue

active accountCode is ['DU229341', 'DU229347']

I am getting the following encoding error while running RUN_ME.py on spyder while using the demo account:

“UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1035: character maps to <undefined>”

You can add encoding="utf8", highlighted below in line number 83 of configuration.py file. This file is located at C:\Users\...\IBridgePy_Win_Anacondaxx_yy\configuration.py

with open(os.path.join(os.getcwd(), 'Strategies', fileName), encoding="utf8") as f:

script = f.read()

I am trying to download the pricing data for backtesting purposes from Interactive Brokers following the IBridgePy course, the Interactive brokers’ platform is throwing an error message:IBridgePy version 5.2.3fileName = example_get_historical_data.py####    Starting to initialize trader    ####..............................................####    Initialize trader COMPLETED    ####Historical Data of STK,SPY,USD

broker_client_factory.CallBacks:errorId=13 errorCode=162 errorMessage=Historical Market Data Service error message:No market data permissions for AMEX STKbroker_client_factory.CallBacks:EXIT IBridgePy version = 5.2.3An exception has occurred, use %tb to see the full traceback.

If you are using a demo account while fetching the data, then you will not have access at all the tickers. Your access will be limited to Forex pairs mostly. In such a case, try the below code to fetch the data.

How do you retrieve information regarding any IB contract and symbol?

To get the information regarding any IB contract or symbol, you can visithere. The syntax of the superSymbol function:

superSymbol(secType=None, symbol=None, currency=’USD’, exchange=”, primaryExchange=”, expiry=”, strike=0.0, right=”, multiplier=”, includeExpired=False, conId=0, localSymbol=”)

Example: For Australian futures SPI, the code can be as follows:

superSymbol(secType='FUT', symbol='SPI', currency='AUD', exchange='SNFE', primaryExchange='SNFE', multiplier='25', expiry='20200917')

When I run RUN_ME I have this error

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf3 in position 36: invalid continuation byte

You can check the following youtube link:https://youtu.be/xsxY0-hiWdMfor a detailed explanation.

I am getting the following error:

“errorCode=502 errorMessage=Couldn't connect to TWS.  Confirm that "Enable ActiveX and Socket Clients" is enabled on the TWS "Configure->API" menu."

Make sure to enable ActiveX and Socket Clients in the API Settings located in Global Configuration. And change the socket port (7496 for paper trade, 7497 for live trade).

If this error persists try re-installing the IB TWS application with the compatible versions of python and IBridgePy.

These were some of the most common questions which were asked by individuals who were starting their journey in IBridgePy. If you have any queries, feel free to add it in the comments below.

Next Step

This is a relatively simple tutorial and can be easily understood if you already gone throughour previous article. We would like you to try using IBridgePy to trade on Interactive Brokers and see which one you find is easier- IBPy or IBridgePy. We will wait for your feedback. In the meantime, we would also like to tell you that we will be discussing about another API called KiteConnect, which will also be used to trade using Python without being bound to some trading platform’s User interface.

You can read more about using Python for algorithmic tradinghereand it is preferred by programmers all over the world. If you want to know more about algorithmic trading and quantitative finance, then you should register for a free call from our EPAT specialist bysigning up here.

---

*Imported from QuantInsti Blog on 2026-04-27*
