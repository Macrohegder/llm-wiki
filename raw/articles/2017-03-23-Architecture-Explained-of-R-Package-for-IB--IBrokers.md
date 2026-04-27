---
title: "Architecture Explained of R Package for IB - IBrokers"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/r-implementation-in-interactive-brokers-api/"
date: "2017-03-23"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Architecture Explained of R Package for IB - IBrokers

**来源**: [QuantInsti](https://blog.quantinsti.com/r-implementation-in-interactive-brokers-api/)  
**日期**: 2017-03-23  
**作者**: QuantInsti

---

## 原文

Architecture Explained of R Package for IB - IBrokers

ByMilind Paradkar

In the our last post onUsing IBrokers package, we introduced our readers to some of the basic functions from the IBrokers package which are used to retrieve market data, view account info, and execute/modify orders via R. This post will cover the structure of the IBrokers package which will enable the R users to build their customtrading strategiesand get them executed via Interactive Brokers Trader Workstation (TWS).

Overview of the Interactive Brokers API Architecture

Before we explain the underlying structure of the IBrokers package, let us take an overview of the Interactive Brokers API architecture. Interactive Brokers provides its API program which can be run on Windows, Linux, and MacOS. The API makes a connection to the IB TWS. The TWS, in turn, is connected to the IB data centers and thus, all the communication is routed via the TWS.

The IBrokers R package enables a user to write his strategy in R and helps it get executed via the IB TWS. Below is the flow structure diagram.

Getting data from the TWS

To retrieve data from the IB TWS, the IBrokers R package includes five important functions.

reqContractDetails: retrieves detailed product information.

reqMktData: retrieves real-time market data.

reqMktDepth: retrieves real-time order book data.

reqRealTimeBars: retrieves real-time OHLC data.

reqHistoricalData: retrieves historical data.

In addition to these functions, there are helper functions which enable a user to create the above-mentioned data functions easily. These helper functions include:

twsContract: create a general Contract object.

twsEquity/twsSTK: wrapper to create equity Contract objects

twsOption/twsOPT: wrapper to create option Contract objects.

twsFuture/twsFUT: wrapper to create futures Contract objects.

twsFuture/twsFOP: wrapper to create futures options Contract objects.

twsCurrency/twsCASH: wrapper to create currency Contract objects.

Example:

tws = twsConnect()
reqMktData(tws, twsSTK("AAPL"))

Real-time Data Model Structure

When a data function is used to access market data streams, the data streams received by the TWS API follow a certain path which enables to bucket these data streams into the relevant message type. Shown below is the list of arguments of the reqMktData function.

Example:Arguments of the reqMktData function

Source: Algorithmic Trading in R - Malcolm Sherrington

Real-time Data Model

In the following sections, we will see how this data model works and how the arguments of the real-time data functions (e.g. reqMktData) can be customized to create user-defined automated trading programs in R.

Using the CALLBACK Argument

The data functions like reqMktData, reqMktDepth, and reqRealTimeBars all have a special CALLBACK argument. By default, this argument calls the twsCALLBACK function from the IBrokers package.

The general logic of the twsCALLBACK function is to receive the header to each incoming message from the TWS. This is then passed to the processMsg function, along with the eWrapper object. The eWrapper object can maintain state data (prices) and has functions for managing all incoming message types from the TWS. Once the processMsg call returns, another cycle of the infinite loop occurs.

In the example of the incoming messages shown below, we have circled a single message in green (1 6 1 4 140.76 1 0). The first digit (i.e. 1) is the header and the remaining numbers (i.e. 6 1 4 140.76 1 0) constitute the body of the message.

Incoming messages from the reqMktData function call

Each message received will invoke the appropriately named eWrapper callback, depending on the message type. By default when nothing is specified, the code will call the default method for printing the results to the screen via cat.

Example with Default Method:

Result:

Setting CALLBACK = NULL will send raw message level data to cat, which in turn will use the file argument to that function to either return the data to the standard output, or redirected via an open connection, a file, or a pipe.

Example with CALLBACK argument set to NULL:

Result:

Callbacks, via CALLBACK and eventWrapper, are designed to allow for R level processing of the real-time data stream. Callback helps to customize the output (i.e. incoming results) which can be used to create automated trading programs in R based on the user-defined criteria.

Internal code of the twsCALLBACK function

Inside of the CALLBACK (i.e. twsCALLBACK function) is a loop that fetches the incoming message type and calls the processMsg function at each new message.

Internal code snippet of the twsCALLBACK function

The ProcessMsg Function

The processMsg function internally is a series of if-else statements that branch according to a known incoming message type. A snippet of the internal code structure of the processMsg function is shown below.

Internal code snippet of the processMsg function

The eWrapper Closure

Creating eWrapper closure in twsCALLBACK using the eWrapper function

The eWrapper function creates an eWrapper closure to allow for the custom incoming message management. The eWrapper closure contains a list of functions to manage all incoming message type. Each message has a corresponding function in the eWrapper designed to handle the particular details of each incoming message type.

List of functions contained in the eWrapper Closure

The data environment is .Data, with accessor methods get.Data, assign.Data, and remove.Data. These methods can be called from the closure object eWrapper$get.Data, eWrapper$assign.Data, etc. By creating an instance of eWrapper, accomplished by calling it as a function call, one can then modify any or all the particular methods embedded in the object.

Summarizingthe Internal Structure of the IBrokers Package

We have seen above how the internal structure of the IBrokers package works. To summarize the entire mechanism, it can be depicted as shown below:

Request to TWS for data -> twsCALLBACK -> processMsg -> eWrapper

Real-Time Data Model

We will use the snapShotTest code example published by Jeff Ryan. The code below modifies the twsCALLBACK function. This modified callback is used as an argument to the reqMktData function. The output using the modified callback is more convenient to read than the normal output when we use the reqMktData function.

Another change in the snapShotTest code is to record any error messages from IB API to a separate file. (Under the default method the eWrapper prints such error messages to the console).  To do this, we create a different wrapper using eWrapper(debug=NULL). Once we construct this, we can assign its errorMessage() function to the eWrapper we should use.

We then apply a simple trade logic which generates a buy signal if the last bid price is greater than a pre-specified threshold value. One can similarly tweak the logic of the twsCALLBACK to create custom callbacks based on one’s requirement of trading strategy.

Order getting filled in the IB Trader Workstation (TWS)

Conclusion

To conclude, the post gave a detailed overview of the architecture of the IBrokers package which is the R implementation of Interactive Brokers API. Interactive Brokers in collaboration with QuantInsti® hosted a webinar,“Trading using R on Interactive Brokers”which was held on 2nd March 2017 and conducted by Anil Yadav, Director at QuantInsti®. You can click on the link provided above to learn more about the IBrokers package. Click on the download button below for the related R files used in the webinar.

Disclaimer:

This software is in no way affiliated, endorsed, or approved by Interactive Brokers or any of its affiliates. It comes with absolutely no warranty and should not be used in actual trading unless the user can read and understand the source. IBrokers is a pure R implementation of the TWS API.

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.Enroll now!

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
