---
title: "Momentum-based Live Trading Using IBridgePy"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/momentum-live-trading-ibridgepy/"
date: "2019-08-05"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Momentum-based Live Trading Using IBridgePy

**来源**: [QuantInsti](https://blog.quantinsti.com/momentum-live-trading-ibridgepy/)  
**日期**: 2019-08-05  
**作者**: QuantInsti

---

## 原文

Momentum-based Live Trading Using IBridgePy

This project uses Ibridgepy and is written in Python to access and use both historical and real-time data of securities provided byInteractive BrokersthroughIB Gateway.This article is the final project submitted by the authors as a part of their coursework in theExecutive Programme in Algorithmic Trading (EPAT®)at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Kent Yewis the Company Director at Glowill Enterprise Sdn. Bhd., based in Kuala Lumpur, Malaysia. Kent is an EPAT alumnus and holds a Masters Degree in Information Technology.

Project Abstract

AnAutomated trading computer programme(ATCP) is used to help traders to solve the limitations such as slow, low efficiency and emotional that lead to loss of opportunity and lower return, faced by human traders.This project would trade multiple securities and multiple asset classes listed below:

Forex: EURUSD (Euro US Dollar) and USDCHF (US Dollar Swiss Franc)

Stocks: XOM (Exxonmobil Corporation)

In this project, EURUSD real-time data would be used for trading signals generations according to the trading strategy to place trade orders of multiple securities of different asset classes that are having strong positive or negative correlation relationships with this currency/forex pair.If the current EURUSD price is higher than the highest closing prices of the previous 5 days, the ATCP would place market orders to buy EURUSD, sell USDCHF and XOM.If the current EURUSD price is lower than the lowest closing prices of the previous 5 days, the ATCP would place market orders to sell EURUSD, buy USDCHF and XOM.Otherwise, the ATCP would close all open positions.

Steps in the selection of asset classes

Step 1 -Correlation calculation based on data using MS Excel, python or R code that are being taught in the EPAT modules, free data could be downloaded from yahoo finance or other sources.Step 2 -Select assets based on the nature that are highly correlated and can be verified by Visual inspection of charts.

Challenges / Limitations

Potential challenges and limitations that are being noticed for this project are listed below:

Automated trading risks -All trading activities carry risks.Auto tradingby executing buy and sell orders without our consent would carry even higher risk.

Change of market dynamic -A previously profitable strategy could become a losing one when the market conditions deviate from the past. The parameters of trading strategy do not guarantee profits in trading.

Technical and software glitches -The technical glitches could come from the broker and even trading exchanges that might cause issues or even losses.

Unexpected events -Unexpected or ‘Black-swan’ events such as erupting wars, unexpected decisions by central banks or governments, etc. that are beyond control by the traders or any automated trading systems could cause a sudden spike of price movements resulting in a huge unrecoverable loss.

ibridgepy limitations -Most of the features, functions, services, access and trading capabilities are only available to Ibridgepy Premium paid account users and are not available for free Ibridgepy account users.

Conclusion

Developing and deploying an ATCP usingIBridgePyfor a simple trading strategy is relatively simple and easy compared to developing everything from scratch.If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT®). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti® disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit./overseasFile in the download:Python Notebook of the Project

---

*Imported from QuantInsti Blog on 2026-04-27*
