---
title: "Trading with Interactive Brokers using Python: An IBPy Tutorial"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/ibpy-tutorial-implement-python-interactive-brokers-api/"
date: "2016-09-19"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Trading with Interactive Brokers using Python: An IBPy Tutorial

**来源**: [QuantInsti](https://blog.quantinsti.com/ibpy-tutorial-implement-python-interactive-brokers-api/)  
**日期**: 2016-09-19  
**作者**: QuantInsti

---

## 原文

IBPy Tutorial To Implement Python In Interactive Brokers API

I hope you had a great time attending our webinar onTrading with Interactive Brokers using Python. I thought it would be a very good idea to give you a brief insight onInteractive Brokers APIand usingIBPyto implement Python in IB's TWS.

As we proceed, you will need an Interactive Brokers demo account and IBPy. Towards the end of this article, you will be running a simple order routing program usingInteractive Brokers API.

What we cover:

Why Interactive Brokers?

What is IBPy?

Implementation of IB in Python

The Configuration of Interactive Brokers Panel

Running the first program

Running the Code

Output

Complete Python Code

Next step

For those of you who are already aware of Interactive Brokers (IB) and its interface, you can very well understand why I prefer IB over other available online brokerages. However, for those who have not used IB, this would be the first question that comes to mind:

Why Interactive Brokers?

Interactive Brokers is my first choice because of 5 simple reasons:

International Investing in more than 100 markets

Commission rates that are highly competitive

Low margin rates

Very friendly user interface

Vast selection of order types

Among the five points mentioned above, the most important and impressive one for any beginner is point no. 2 and point no. 4, isn't it?

TheInteractive Brokers APIcan be used in a professional context even for those who are completely alien to it. Interactive Broker API’s connectivity with Java, C++ and Python is very impressive as well.

Enough said it is time to move to the next step. I can understand that most of you must already be eager to test their hand at the Interactive Brokers API panel. After all, nobody could say no to something very friendly that is lucrative as well.

You can easily set up your account on Interactive Brokers by going to their website. There is an option wherein you can opt for a free trial package.

Algorithmic traders prefer Interactive Brokers due to itsrelatively straightforward API.In this article, I will be telling youhow to automate trades by implementing Python in the Interactive Brokers APIusing a bridge calledIBPy.

As Interactive Brokers offers a platform to an incredibly wide spectrum of traders, therefore, its GUI consists of a myriad of features. This standalone application is called Trader Workstation orTWSon Interactive Brokers.

Apart from the Trader Workstation, Interactive Brokers also has anIB Gateway.This particular application allows IB servers to access it using a Command Line Interface. Algo traders usually prefer using this over GUI.

What is IBPy?

IBPy is a third-party implementation of the API used for accessing the Interactive Brokers on-line trading system.IBPy implements functionality that the Python programmer can use to connect to IB, request stock ticker data, submit orders for stocks and futures, and more.

The purpose of IBPy is to conceive the native API, that is written in Java, in such a way that it can be called from Python. Two of the most significant libraries in IBPy are ib.ext and ib.opt. ib.opt derives from the functionality of ib.ext.

Through IBPy, the API executes orders and fetches real-time market data feeds. The architecture essentially utilizes a client-server model.

Implementation of IB in Python

First of all, you must have an Interactive Brokers account and a Python workspace to install IBPy, and thereafter, you can use it for your coding purposes.

Installing IBPy

As I had mentioned earlier,IBPyis aPython emulatorwritten for theJava-basedInteractive Brokers API. IBPy helps in turning the development ofalgo trading systemsin Python into a less cumbersome process.

For this reason, I will be using it as a base for all kinds of interaction with the Interactive Brokers TWS. HereI am presuming that you have Python 2.7 installed on your system, else you may refer the installation guide mentionedhere.

Installing IBPy on Ubuntu

IBPy can be acquired from GitHub repository.

The following code will be needed on an Ubuntu system:

sudo apt-get install git-core

mkdir ~/ibapi

cd ~/ibapi

git clone https://github.com/blampe/IbPy

cd ~/ibapi/IbPypython setup.py.in install

Great! You have installed Python on your Ubuntu system.

Installing IBPy on Windows

Go to the github repository and download the file from:https://goo.gl/e6Idr6

Unzip the downloaded file. Move this folder to the directory where you have installed Python so that it can recognize this package:

\\Anaconda2\Lib\site-packages

Now, open the setup with windows command prompt and type the following command:

python setup.py install

After this, you will have to get your Trader Workstation (TWS) in operation.

Installing Trader Workstation

Interactive Brokers Trader Workstation or TWS is the GUI that lets all registered users of Interactive Brokers to trade on their systems. Don't worry, even if you do not have prior knowledge of programming or coding, TWS will let you do the trading work.

You can download the TWS installer from interactive Brokers’ website and run it on your system.

You can download the TWS Demo from here:https://www.interactivebrokers.com/en/index.php?f=19903&invd=T

In the older versions of TWS, the user would get to choose two different programs. The first one was theTWSof Interactive Brokers and the second was theIB Gateway, about which I have already talked earlier. Although they are different applications, however, they can only be installed together.

The IB Gateway runs on lower processing power since it does not have an evolved graphical user interface as the Trade Workstation. However, the results and other data are displayed in the form of primitive codes on the IB Gateway, making it less friendly for certain set of users who do not possess enough knowledge in coding.

You may use either of the two interfaces for your work on Interactive Brokers. The functionalities of both remain the same, i.e. to relay info between your system and the Interactive Brokers server. Needless to say, the Python app will get the exact same messages from the server end of Interactive Brokers.

Installation Walk-through

Once you download the application, you will find the executable file at the bottom of your browser. Click on Run when prompted with a security warning.

Now, click on Next.

Click on finish to complete your installation.

Click on the desktop icon and start the TWS application.

Since I am going to use a demo account, therefore, click onNo User name?

Enter your email address and click on Login:

The Configuration of Interactive Brokers Panel

The journey so far has been pretty easy, hasn’t it? It is great if you agreed with me on that one. After installing the TWS and/or IB Gateway, we have to make some changes in the configurations before implementing our strategies on Interactive Brokers’ servers. The software will connect to the server properly only once these settings are changed.

Procedure

Go to API settings in TWS

Check theEnable ActiveX and Socket Clients

SetSocket portto unused port.

Set theMaster API client IDto 100

Create aTrusted IP Addressand set to 127.0.0.1

Running the first program

So, all done with the configuration?

Great! We are now ready to run our first program.

Before you start typing in those codes, make sure that you have started TWS (or IB Gateway). Many times, I get questions as to why we get an error message when the code is run.

Like I had mentioned in the previous section,your system is connected to the Interactive Brokers’ server through the TWS or IB Gateway. So, if you haven’t turned it on, then you are bound to get an exception message, no matter how smartly you have developed your code.

Let’s start working on the coding step-by-step.

Open Spyder (Start - All Programs - Anaconda2 - Spyder)

On the Spyder console, I will be entering my codes.

Connectionis a module that connects the API with IB whilemessageperforms the task of a courier between the server and the system, it basically retrieves messages from the Interactive Brokers server.

Just like every transaction in the real-world involves some kind of a contract or agreement, we haveContracthere as well. Allorderson Interactive Brokers are made usingcontract.

The contract function has the following parameters:

Symbol

Security Type

Exchange

Primary Exchange

Currency

The values of these parameters must be set accordingly.

Orderfunction allows us to make orders of different types. The order function has the following parameters:

Order Type

Total Quantity

Market Action (Buy or sell)

Considering that our order does have a set price, we code it in the following way:

The conditional statement will now set up the order as a simple market order without any set price.

The client id & port should be the same as you had set in the Global preferences

Establish the connection to TWS.

Assign error handling function.

Assign server messages handling function.

Create AAPL contract and send order

In the above line, AAPL is Apple Inc. and STK is the name of the security type. The exchange and primary exchange has been set to SMART.

When we set these two parameters to SMART, then we are actually using Interactive Brokers smart routing system which enables the algo to find the best route to carry out the trade. And of course, the currency has been set to USD.

We wish to sell 100 shares of AAPL

Our order is to sell 1 stocks and our price is $100.

We have placed an order on IB TWS with the following parameters:

Order id

Contract

“Always remember that the order id should be unique.”

And finally you need to disconnect:

Yes, you are done with your first order on Interactive brokers’ API using basic Python coding. Keep in mind that the demo account that you are using might not give you all the privileges of a paid account.

Running the Code

Click on the Green coloured ‘Play’ button or simply press F5 in Spyder. On your TWS Demo system, you will get a popup regarding your order. Click on OK.

Output

You can see the final output on the bottom right side of Interactive Brokers TWS panel.

Complete Python Code

Just in case you want to have a look at the complete code at one go, here it is.

If you wish to download it for free, scroll down to the bottom of the article.

Python code:

Next Step

Our post on 'Architecture Explained of R Package for IB – IBrokers' explains the architecture of IBrokers R implementation in Interactive Brokers API which allows executing orders in the IB Trader Workstation (TWS).

For those who want to learn to use Python in trading, here's a bundle of courses that teach different trading strategies including Day Trading, Machine Learning, ARIMA, GARCH, and Options Pricing and how to use their models in your trading.

Perfect for traders and quants! Check it out here:Algorithmic Trading for Everyone

Sources & References: quantstart.com, pythonprogramming.net, interactivebrokers.com

You can also check out our article on 'How to Get Historical Market Data Through Python Stock API' if you want to explore how to extract historical data using the Python stock API from various data providers.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

File in the download:A Simple Order Routing Mechanism - The complete python code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
