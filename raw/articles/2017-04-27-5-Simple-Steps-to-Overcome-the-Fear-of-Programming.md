---
title: "5 Simple Steps to Overcome the Fear of Programming"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/overcome-fear-programming/"
date: "2017-04-27"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# 5 Simple Steps to Overcome the Fear of Programming

**来源**: [QuantInsti](https://blog.quantinsti.com/overcome-fear-programming/)  
**日期**: 2017-04-27  
**作者**: QuantInsti

---

## 原文

Overcome the Fear of Programming

ByMilind Paradkar

You say you never programmed in life before? Never heard of words like Classes and Objects, Dataframe, Methods, Inheritance, Loops? Are you fearful of programming, huh?

Don’t be! Programming can be fun, stimulating, and once you start and learn to program many of you would love spending hours programming different strategies; you would love to see your own codes run in the blink of an eye and would see how powerful these codes can be.

TheExecutive Programme in Algorithmic Trading (EPAT™)course makes extensive use of Python and R programming language to teach strategies, backtesting, and their optimization. Let us take the help of R to demonstrate how you can overcome the fear of programming. Here are some suggestions for the newbie programmers.

1) Think and let the questions pop in your mind

As a newbie programmer when you have a task to code, even before you start on it, spend some time ideating on how you would like to solve it step-by-step. Simply let questions pop up in your mind, as many questions as your mind may throw up.

Here are a few questions:Is it possible to download stock price data in R from google finance?
How to delete a column in R? How to compute an exponential moving average (EMA)?
How do I draw a line chart in R? How to merge two data sets?
Is it possible to save the results in an excel workbook using R?

2) Google the questions for answers

Use google search to see whether solutions exist for the questions that you have raised. Let us take the second question, how to delete a column in R? We posted the question in the google search, and as we can see from the screenshot below we have the solution in the very first result shown by google.

R is an open-source project, and there are hundreds of articles, blogs, forums, tutorials, Youtube videos on the net and books which will help you overcome the fear of programming and transition you from a beginner to an intermediate level, and eventually to an expert if you aspire to.

The chart below shows the number of questions/threads posted by newbie and expert programmers on two popular websites. As you can see, R clearly tops the results with more than 10 thousand questions/threads.
(Source: www.r4stats.com )

Let us search in google whether QuantInsti® has put up any programming material on R.As you can see from the google results, QuantInsti® has posted quality content on its website to help newbie programmers design and modelquantitative trading strategiesin R. You can read all the rich content posted regularly by QuantInsti® here - http://blog.quantinsti.com

3) Use the print command in R

As a newbie programmer, don’t get intimidated when you come across complex looking codes on the internet. If you are unable to figure out what exactly the code does, just copy the code in R. You can use a simple “print” command to help understand the code’s working.

One can also use Ctrl+Enter to execute the code line-by-line and see the results in the console.

I am unsure of the working of commands at line 9 and line 11. So I simply inserted aprint(head(returns))command at line 10 and one more at line 12. Thereafter I ran the code. Below is the result as shown in the console window of R.

The returns = returns[‘2008-06-02/2015-09-22’] command simply trims the original NSEI.Close price returns series. The series was earlier starting from 2007-09-17. The series now starts from 2008-06-02 and ends at 2015-09-22.

4) Use help() and example() functions in R

One can also make use of the help() and example() functions in R to understand a code, and also learn new ways of coding. Continuing with the code above, I am unsure what the ROC function does at line 9 in the code.

I used the help(“ROC”) command, and R displays all the relevant information regarding the usage, arguments of the ROC function.

There are hundreds of add-on packages in R which makes programming easy and yet powerful.

Below is the link to view all the available packages in R:
https://cran.r-project.org/web/packages/availablepackagesby_name.html

5) Give time to programming

Programming can be a very rewarding experience, and we expect that you devote some time towards learning and honing your programming skills. Below is a word cloud of some essential characteristics a good programmer should possess. The best suggestion would be to just start programming!!

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.Enroll now!

Update

We have noticed that some users are facing challenges while downloading the market data from Yahoo and Google Finance platforms. In case you are looking for an alternative source for market data, you can use Quandl for the same.

As a newbie programmer, you have just made a start. The faculty at QuantInsti® will teach and guide you through different aspects of programming in R and Python. Over the course of the program, you will learn different data structures, classes and objects, functions, and many other aspects which will enable you to program algorithmic trading strategies in the most efficient and powerful way.

---

*Imported from QuantInsti Blog on 2026-04-27*
