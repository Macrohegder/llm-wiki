---
title: "Building a Machine Learning model for a Long-only strategy to be used as a Retail Trader"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/machine-learning-model-long-only-strategy-retail-trader-project-pranav-lal/"
date: "2022-04-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Building a Machine Learning model for a Long-only strategy to be used as a Retail Trader

**来源**: [QuantInsti](https://blog.quantinsti.com/machine-learning-model-long-only-strategy-retail-trader-project-pranav-lal/)  
**日期**: 2022-04-13  
**作者**: QuantInsti

---

## 原文

Building a Machine Learning model for a Long-only strategy to be used as a Retail Trader

This project helps you learn how you can implement a long-only strategy to buy and sell stocks via machine learning.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT) at QuantInsti. Do check ourProjects pageand have a look at what our students are building.

About the Author

Pranav Lalis an action-oriented manager specializing in information security from India. Pranav is a commerce graduate and holds a post-graduate MBA. He has professional experience of more than 20 years and is an EPAT alumnus.

Project Abstract

A long-only strategy has been encoded into a machine learning model. The model generates two sets of signals namely one and zero. If the signal is one, then we go long and if the signal is 0, we go short. There is no hold state.

The buy triggers of a number of indicators have been used to determine when a single stock should be bought. Their sell indicators have not been encoded. This has been done to keep the model simple.

Moreover, a decision tree has been used to ensure that the model is easy to explain and to minimize hidden variables. We do not want a black box that will spit out trading decisions. We want a model whose decisions can be seen, understood and debugged.

Project Motivation

I am new to trading, but not new to programming. I do not know the markets therefore wanted a mechanism to be able to trade with as little human input as possible.

I could have used indicators such as themoving averageconvergence divergence but did not know what values to plugin to optimize the strategy returns. This is why my mentor suggested that I use a machine learning model and let it decide when to buy.

All I had to do was to encode the buy-side triggers in the model. These returns became the variable that I predicted. However, I have converted the return to a binary label to better meet the binary nature of the signal from the model.

Data Mining

I had a significant challenge in sourcing high-quality data. As a retail trader, I have a limited budget. As of the writing of the project, I settled on yahoo finance. It was the only provider that was giving me adjusted closing prices.

I could have studied individual corporate actions and have factored them into the model but given my inexperience, I did not see the value in that course of action. Moreover, I would not gain anything and would introduce more complications in my code.

I am also in the process of signing up with a broker that supports algorithmic trading. My existing broker did not have the data I needed.

I did consider downloading directly from the National Stock Exchange (NSE). The initial results were promising but the python wrapper to do this efficiently failed to work consistently hence I have elected to use yahoo finance.

I was using machine learning therefore I needed data. In the interest of simplicity and a reduction of errors, I have elected to use the adjusted closing prices at the end of each day to train my model.

I am going back 10 years. I could go back further but given the changes in India, I did not see the value in training a model on really old data.

Data Analysis

I had initially started by focusing on model scores such as accuracy. However, my mentor suggested that I  emphasize the business-related matrix such as the strategy return, the sharp ratio and maximum drawdown.

I am using the nifty 50 stocks and have achieved an annual return of 28%. Having said that, the maximum drawdown in some cases has been -22%.

The model works with a single stock for now. It is possible to build a model for a portfolio but that requires a significant amount of research.

I have started with a capital of Rs. 10000. See the below output for some nifty 50 companies.

HDFCLIFE.NS
mcc=0.2323
{'0': {'precision': 0.5766423357664233, 'recall': 0.7117117117117117, 'f1-score': 0.6370967741935484, 'support': 111}, '
1': {'precision': 0.6595744680851063, 'recall': 0.5166666666666667, 'f1-score': 0.5794392523364487, 'support': 120}, 'ac
curacy': 0.6103896103896104, 'macro avg': {'precision': 0.6181084019257648, 'recall': 0.6141891891891892, 'f1-score': 0.
6082680132649985, 'support': 231}, 'weighted avg': {'precision': 0.6197239629449599, 'recall': 0.6103896103896104, 'f1-s
core': 0.6071448147872628, 'support': 231}}
all done, model saved
HDFCLIFE.NS
end capital=13025.661671336782
cumulative returns=0.01
annualized returns=11.946754317747708
sharp ratio=2.430894954720865
maximum draw down=-5.335562897550606
event based back testing
inventory=0
total trades62
Worst drawdown periods Net drawdown in %  Peak date Valley date Recovery date Duration
0                               	5.34 2021-07-19  2021-07-30	2021-08-26   	29
1                               	4.61 2021-09-30  2021-10-14	2021-12-03   	47
2                               	1.48 2021-09-17  2021-09-28    2021-09-30   	10
3                               	1.40 2021-07-05  2021-07-06	2021-07-14    	8
4                               	0.28 2021-06-22  2021-06-23	2021-06-25    	4
(
AXISBANK.NS
mcc=0.1157
{'0': {'precision': 0.5460251046025104, 'recall': 0.6444444444444445, 'f1-score': 0.5911664779161948, 'support': 405}, '
1': {'precision': 0.5714285714285714, 'recall': 0.46943765281173594, 'f1-score': 0.5154362416107382, 'support': 409}, 'a
accuracy': 0.5565110565110565, 'macro avg': {'precision': 0.5587268380155409, 'recall': 0.5569410486280902, 'f1-score': 0
.5533013597634665, 'support': 814}, 'weighted avg': {'precision': 0.558789254395949, 'recall': 0.5565110565110565, 'f1-s
core': 0.5531152903867946, 'support': 814}}
all done, model saved
AXISBANK.NS
end capital=11912.529405911413
cumulative returns=0.01
annualized returns=14.396557602433907
sharp ratio=1.2692911988723536
maximum draw down=-11.401175197958969
event based back testing
inventory=0
total trades270
Worst drawdown periods Net drawdown in %  Peak date Valley date Recovery date Duration
0                              	11.40 2021-10-27  2021-12-27       	NaT  	NaN
1                               	2.58 2021-05-25  2021-06-03	2021-06-28   	25
2                               	2.30 2021-05-03  2021-05-11	2021-05-18   	12
3                               	1.85 2021-06-30  2021-07-09	2021-08-05   	27
4                               	1.74 2021-09-24  2021-09-27	2021-10-12   	13
(
CIPLA.NS
end capital=10108.381471799057
cumulative returns=0.01
annualized returns=12.97248677553947
sharp ratio=-0.17873433713762618
maximum draw down=-8.419739036394535
event based back testing
inventory=1
total trades253
Worst drawdown periods Net drawdown in %  Peak date Valley date Recovery date Duration
0                               	8.42 2021-09-03  2021-12-22       	NaT  	NaN
1                               	8.10 2021-03-08  2021-03-19	2021-06-11   	70
2	                               1.91 2021-06-11  2021-06-18	2021-07-15   	25
3                               	0.36 2021-07-15  2021-07-16	2021-08-02   	13
4                               	0.00 2021-03-08  2021-03-08	2021-03-08    	1
(
HINDALCO.NS
mcc=0.2139
{'0': {'precision': 0.6022727272727273, 'recall': 0.6463414634146342, 'f1-score': 0.6235294117647059, 'support': 410}, '
1': {'precision': 0.6122994652406417, 'recall': 0.5668316831683168, 'f1-score': 0.5886889460154242, 'support': 404}, 'ac
curacy': 0.6068796068796068, 'macro avg': {'precision': 0.6072860962566845, 'recall': 0.6065865732914755, 'f1-score': 0.
606109178890065, 'support': 814}, 'weighted avg': {'precision': 0.6072491426769502, 'recall': 0.6068796068796068, 'f1-sc
ore': 0.6062375835549887, 'support': 814}}
all done, model saved
2021-03-07
2022-01-04
HINDALCO.NS
end capital=24400.365307225453
cumulative returns=0.02
annualized returns=25.342755013632857
sharp ratio=4.32476549991755
maximum draw down=-7.444258699940887
event based back testing
inventory=0
total trades270
Worst drawdown periods Net drawdown in %  Peak date Valley date Recovery date Duration
0                               	7.44 2021-10-27  2021-12-07	2022-01-03   	49
1                               	3.73 2021-07-06  2021-07-09	2021-07-19   	10
2                               	2.18 2021-09-01  2021-09-02	2021-09-14   	10
3                               	2.11 2021-07-19  2021-07-20	2021-07-28 	   8
4                               	2.06 2021-10-05  2021-10-06	2021-10-13    	7
(

Key Findings

More data does not always lead to the logical output

I had initially tried combining several stocks into a giant portfolio in the belief that more data is good for my machine learning model. I did get good results but the business matrix such as annual returns was off the charts. The results were not valid.

There must be some logic to the predictors you enter

I had tried combining multiple strategies into a super-intelligent model. That did not work. The accuracy was low and the model’s results could not be relied upon during backtesting.

Start small

The project moved forward when I followed my mentor’s advice and focused on a single stock. The returns and other matrices such as maximum drawdown were rational which is within expected parameters.

Your model should have a single goal

I had initially tried making a supermodel which would tell me when to buy, sell and hold. After a review with my project mentor, I decided to focus only on the long conditions of each indicator. The model then began yielding usable results.

Sourcing data is hard and very expensive

I was trying to get an authentic source of data but eventually held on to yahoo finance. Data vendors are expensive and many of them do not have data that has the adjusted close price. Costs for about 7 years of data were about Rs. 40000. This data was not adjusted. I returned to yahoo finance but propose to source the data from my broker.

Challenges/Limitations

The sourcing of high-quality data is hard and potentially expensive.

Paper trading using the model remains a work in progress.

This project supports a long-only strategy.

The project is not written in the structure of iBridgePy or similar frameworks therefore work has to be done to adapt it.

Implementation Methodology

The project has been tested with the nifty 50 stocks. It was not possible to test the project with broker supplied data.

The system runs upon the opening of the market and runs the model. The generated signal is used to decide to buy or sell.

Conclusion

It is possible for a retail trader to build an effective strategy that uses machine learning. Careful feature selection and feature engineering are needed to begin to use the strategy in a production environment.

One advantage with financial data is that it is less as compared to what is available in other areas of machine learning like image processing. This allows for users who may not have the latest and greatest machine learning hardware to get started. Regular business-class machines are sufficient if one is doing medium to low-frequency trading.

With the integration ofartificial intelligence in trading, even retail traders are empowered to leverage advanced data analysis without extensive resources. AI enables efficient processing and modeling, giving traders the tools to create strategies that adapt dynamically to market patterns, maximizing potential within accessible setups.

Annexure/Codes

The project is divided into 3 main modules.

The FetchData class.

The MomentumStrategy class.

The stockbot script.

The FetchData class pulls the data from yahoo finance and brings it into a  dictionary. The data is downloaded into a frame first and that frame is placed in a dictionary with the ticker symbol as the key.

The MomentumStrategy class takes this data and computes a series of indicators and other variables like percentage and log returns. The class returns a large pandas data frame containing the calculated variables and the original stock data. The NA values are also removed.

The stockbot.py script trains the model with the specified data and also runs the prediction.

This is where the order generation logic will be incorporated. There is also reporting code in place.

As of this writing, if the system gets a buy signal, it will check the inventory and if there is more than one stock,  it will ignore the signal. If there is no inventory, a market order will be placed to buy the stock. The quantity will be defined based on the available capital.

If the system gets a 0 signal, and the inventory is greater than zero, then all the available quantity will be sold.

Appropriate reports will be generated by the system and transaction logging will be introduced later.

If you want to learn various aspects of Algorithmic trading then check out thisalgo trading coursewhich covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
