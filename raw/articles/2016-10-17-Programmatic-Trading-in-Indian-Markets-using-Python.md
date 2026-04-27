---
title: "Programmatic Trading in Indian Markets using Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/trading-with-python-indian-markets/"
date: "2016-10-17"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Programmatic Trading in Indian Markets using Python

**来源**: [QuantInsti](https://blog.quantinsti.com/trading-with-python-indian-markets/)  
**日期**: 2016-10-17  
**作者**: QuantInsti

---

## 原文

Trading with Python in Indian Markets Using Zerodha Kite Connect API

We have told you why Python is one of the preferred languages to do algo trading inthis article. We have also told you about programmatictrading in India. We also had a successful webinar on Trading in Indian Markets using Python (Click hereto watch the webinar), we ought to give you a prelude to the trading platform which will enable you to implement your algorithmic trading strategies in python.

To enable trading in Indian Markets using Python, we will utilize Zerodha Kite Connect API, India’s first market API for retail clients. We will be covering this in detail in the webinar. We cover most of the trading platforms inEPAT™, our highly sought after course on algorithmic trading and quantitative finance. We have also covered variouslibraries available in Python for programmatic tradingin an earlier article, in this article we will also be talking about the official python client for communicating with Zerodha Kite Connect API.

What is Zerodha Kite Connect?

Kite Connect is a compilation of REST-like hypertext transfer protocol based APIs that ease numerous capabilities needed to build investment and trading platforms. It is built on top of Zerodha’s online trading platform. The users should be clients of Zerodha only and they will get programmatic access to all the information on the brokerage. You can also use Kite Connect API for:

Executing orders in real time

managing portfolios

streaming real time market data

offsite order execution

getting reliable updates on your orders

of course, getting historical data

Now, if you remember, in our article on trading with Interactive Brokers, we had mentioned some of theadvantages of using IB API for algorithmic trading. For Indian markets, Zerodha Kite Connect is a great choice for implementing algorithmic trading strategies using Python, which has been further explained in ourwebinar.

Objectives of Zerodha Kite Connect

Gone are the days when retail clients stayed away from capital markets because they did not have any option to access their trading accounts pragmatically. With aim to bring a revolutionary change in the way trading is done in India, Zerodha Kite Connect promises to:

Cutting down costs involved to perform trading in India

Going completely brokerage free in future

Making the process more transparent

Offer a better platform to do trading

Keeping a client-first attitude.

Supporting a wide array of programming languages including Python, Java, C#, Excel VBA, etc. You can also use the command line console on Kite Connect.

Besides placing and managing orders, Kite Connect promises to enable users to build:

Multi asset risk modelling systems

Stock screeners

Quant strategies

Equity stock selection models

Option greeks calculators

Backtesting, machine learning

Personal Kite or Pi.

One of the key advantages of Zerodha Kite Connect is that you will own and control your trading account and the data associated with it, and you will not be restricted to the platform offered by your broker.

Python for Programmatic Trading in Kite Connect

We have already told you why Python has sufficed as the best choice for programmatic trading in our article titled:Why Python Programmatic Trading is Preferred Choice Among Traders?

Zerodha's Kite Connect has client libraries in multiple programming languages including PHP, JS and of course, Python. The official library for Python is available here:

https://github.com/rainmattertech/pykiteconnect

Requirements

Zerodha is India’s first discount broker and all the trades in Kite Connect are executed through Zerodha.  So, first thing that you need to do is tocreate a trading account on Zerodhaso that you can access the APIs. Once you have that, next thing to do is toregister for a developer account. That’s it! You can get started immediately.  In our webinar, Nithin Kamat, Founder & CEO at Zerodha, & Satyajit Sarangi, Software Developer at Zerodha, will be explaining all this in a step-by-step manner.

Since Zerodha has already got all the necessary approvals for users of Kite Connect API, therefore you, as a Kite Connect user, do not have to acquire any other approvals.

Installation of Python client

After downloading the resources from the github repository you will have to install the files. To install the client, you will have to use the following command:

pip install kiteconnect

API Usage

You can find the following code on the github repository as well. However, for convenience' sake, we are giving it here:

fromkiteconnectimportKiteConnect

kite=KiteConnect(api_key="your_api_key")# Redirect the user to the login url obtained# from kite.login_url(), and receive the request_token# from the registered redirect url after the login flow.# Once you have the request_token, obtain the access_token# as follows.data=kite.request_access_token("request_token_here",secret="your_secret")
kite.set_access_token(data["access_token"])# Place an ordertry:
    order_id=kite.order_place(tradingsymbol="INFY",exchange="NSE",transaction_type="BUY",quantity=1,order_type="MARKET",product="NRML")print("Order placed. ID is", order_id)exceptExceptionase:print("Order placement failed", e.message)# Fetch all ordersprint(kite.orders())

WebSocket usage

fromkiteconnectimportWebSocket# Initialise.kws=WebSocket("your_api_key","your_public_token","logged_in_user_id")# Callback for tick reception.defon_tick(tick,ws):printtick# Callback for successful connection.defon_connect(ws):# Subscribe to a list of instrument_tokens (RELIANCE and ACC here).ws.subscribe([738561,5633])# Set RELIANCE to tick in `full` mode.ws.set_mode(ws.MODE_FULL, [738561])# Assign the callbacks.kws.on_tick=on_tick
kws.on_connect=on_connect# Infinite loop on the main thread. Nothing after this will run.# You have to use the pre-defined callbacks to manage subscriptions.kws.connect()

You can read further about all the list of supported methodshere. The top guns from Zerodha will be covering this in great detail in our webinar on Trading in Indian Markets using Python. If you didn't attend it then watch the recording byclicking here.

To Conclude

Algorithmic Trading in Indian Markets using Python has become all the more interesting and easier, thanks to Zerodha’s Kite Connect API. All you have to do now is:

Sign up with Zerodha for a trading account

Register for a Kite Connect account

Log in to your kite connect developer account

Start creating your strategies

That’s it! Enjoy the programmatic trading offered by Kite Connect

Next Step

Python algorithmic trading has gained traction in the quant finance community as it makes it easy to build intricate statistical models with ease due to the availability of sufficient scientific libraries like Pandas, NumPy, PyAlgoTrade, Pybacktest and more.

In case you are looking to master the art of using Python to generate trading strategies, learnhow to backtest a trading strategy, deal with time series, generate trading signals, predictive analysis and much more, you can enroll for our course onPython for Trading!

Disclaimer:All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Source:https://kite.trade

---

*Imported from QuantInsti Blog on 2026-04-27*
