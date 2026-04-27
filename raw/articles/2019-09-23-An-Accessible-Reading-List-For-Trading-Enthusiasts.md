---
title: "An Accessible Reading List For Trading Enthusiasts"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/reading-list-trading-enthusiasts/"
date: "2019-09-23"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# An Accessible Reading List For Trading Enthusiasts

**来源**: [QuantInsti](https://blog.quantinsti.com/reading-list-trading-enthusiasts/)  
**日期**: 2019-09-23  
**作者**: QuantInsti

---

## 原文

An Accessible Reading List For Trading Enthusiasts

ByZach Oakes

The most frequent question I get about trading is how I got started. The onlyrealanswer is to begin gaining experience as soon as possible in any way you can. That doesn't mean trading 25 contract futures, but I think paper trading does very little to teach the psychology and mechanics of orders filling. I believe getting started with micro lot Currencies or slowly scaling to comfort in equities (or more recently Micro Futures may have a place) provides the best way to gain experience in capital markets — without losing all the capital you may later need.

The other true answer, at least for me, was to readeverything I could get my hands on. I'm a pretty avid reader—I try to read between 3 and 5 books a week—unfortunately for the girlfriend most of which end up in an enormous stack next to (or on) the bed. I've read pretty much every trading book I could find, and owe most of myfull-stack developeraccreditation to working through code books.

This will not be the first reading list you'll find, but rather than making this a list to intimidate readers, I thought making an accessible reading list would be more useful. I've included a beginner, intermediate, and a free book for all necessary components to quantitative trading. If options trading is part of your learning roadmap, complement this reading list with our guide onoptions trading basicsfor a strong foundational start. This is a reading list for people interested in gaining trading experience, rather than a PHD in applied mathematics. If you have a degree in applied mathematics, I would suggest Hull and other like titles — but this list probably isn’t for you.

The first key to automation is making sure you have all the right tools. If you're just looking for automating retail, EasyLanguage can be very versatile and has helpful courses/books on Tradestation.com. Alongside these books, theAutomated Trading for Beginnerslearning track offers a hands-on practical complement to your reading ideal for those who prefer learning by doing. For someone with goals of working at an institution, this should be at the least Python, and eventually maybe a lower level language like C + +. For now, the goal isaccessibleso we’ll start with Python, and it'sNECESSARYcomponentPandas. Once you're comfortable with Python and Pandas,python backtestingis the logical next step to validate your trading strategies on historical data. Don't make the mistake I made of not properly learning the Pandas library when I learned Python, it will makeeverythingin Python a struggle.

Best books on Python — An Algorithmic Trading Foundation

Beginner: QuantInsti Python Handbook (Free)

If you want to read a single book (Python and Pandas), this would be a good option as it has a lot of direct examples that you can apply. I wish I had this reference when I was learning Python.

Learn Python in One day & learn it well, Chan

This book could not be more clear, and if learning a new language is intimidating I would start here. This should provide a great foundation to later build more specific models upon with libraries like Pandas, Numpy, Scipy.

Pandas Cookbook

If you find yourself sighing every time you see a df, do yourself a favor and work through this book. Within a few chapters you’ll have endless tricks even for simple operations that once frustrated you. I greatly regret waiting until recently to work through this book — being comfortable in Pandas is a MUST for system trading, and it’s importance to ML cannot be understated.

Intermediate: Python for Finance (check PD content) / Data Science

An excellent more in depth read, with direct applications and useful functions (Like Monte Carlo’s, Backtesting, etc). Also has a good Pandas section, with coverage of query and filter functions. My favorite parts are the various MC models, and optimization functions/efficient frontier coverage.

Intermediate: Python Cookbook

Probably my favorite Python book, excellent recipes and helpful in understanding things like tuple unpacking, properties, etc. Working through these books is always such a joy, nothing makes me really appreciate a programming languages intricacies like Cookbooks — so you’ll see a few of them on my list.

Mentions

Elements of Programming Interviews in Python, Aziz

This book was my bible when I was interviewing for quant positions. It proved incredibly helpful for coding challenges — which many times are NOT like anything you would do in practice. It’s good to be as prepared as possible, and this will get you there (also reviewhttps://www.hackerrank.com, many funds use this as a screening tool; andcheckif the firm gives you PRACTICE QUESTIONS—I realized once the firm basically gave me the questions in advance, but I didn’t look)

The next piece in the puzzle is capital markets, and I'm going to include my favorites for each asset class, although to a technical trader they’re relatively interchangeable (aside from Options). Based on this theory, I decided to group them in together — it should be fairly obvious what most books cover with my notes.

Before I begin, I want to mention that from my experience you should ignore any books with ‘Warren Buffet’ in the title. Most people don't realize that their suitability is light-years away from his, and treat his actions as divine. I think there's little to be gained in the short term fromvalueinvesting.

Best books on Day Trading

Beginner: Understanding Stocks, Understanding Options; Sincere

Both great intro books to simple and complex concepts alike. Clearly written, brief coverage but enough to know if you would like to dive deeper. This will provide you with a comprehensive understanding of the basics, and a solid foundation to build upon.

High probability Trading, Link

My favorite book on Futures, so simple and so helpful. Great for beginners and pro’s to review basics. Includes psychology section which is often overlooked in new traders. I especially liked the breadth of markets used in examples — all corners of Futures markets, not just ES or CL.

Day and Swing Trading the Currency Market, Lien

Great intro book for forex, provides helpful understanding for what moves currencies and interest rates. Provides a strong foundation for getting into FX trading and Event Arbitrage.

Long Term Secrets to Short Term Trading, Williams

A wonderful old school Futures book, easy enough for beginners, great backtests included on some basic filters.

Intermediate: Options Volatility and Pricing, Natenburg

My favoritetradingbook — I used to read this every year when I traded only options. It’s the Options Bible. No book will leave you with a more complete understanding of Options Pricing.

Mentions: How To Day Trade for a Living, Aziz (Great overall trading book), Naked Forex, Nekritin & Peters (Simple, helpful, indicator free FX), Options as a Strategic Investment, McMillan (Extensive coverage of Options and some Futures markets).

A more recent trend in the technology aspect has been Machine Learning. I'll be honest, I haven't seen much success from applying machine learning to alpha models. I have maybe 3 filters that involve ML techniques, (out of approx 320 strategies) and they are just filters on top of existing strategies. Nonetheless, if padding the resume is the goal this can be important at many funds.

Machine Learning in Quantitative Trading

Beginner: The Hundred-Page Machine Learning Book (Free)

Great to get a basic understanding of confusing concepts. I’ve found this book helpful even after reading some of the more advanced names on this list — just to confirm ideas of what these ML concepts really are doing.

Hands on Machine Learning with SKLearn, TF Keras (get most recent edition: TF2.0, much more forgiving)

A good book to work through and gain a comfort level working with RFR’s and NN’s. Aurelien is very helpful if you have questions, and the exercises in the book — while challenging — leave you with a real confidence on the content.

Intermediate:Neural Networks & Deep Learning, Nielsen (FREE)

A helpful online walkthrough of advanced ML concepts. Very similar to Hands On ML. Should provide an excellent alternative to Hands On if you’re on a budget (also, ThriftBooks sometimes has great deals on common textbooks)

Advanced: Advances in Financial ML, Prado

A revolutionary book that turns most time series studies on their head. A definite must read once you have a basic ML understanding. Incredible development in the field, truly a must read even for people not interested in Machine Learning for it’s coverage of backtesting bias in depth.

I want to attempt to keep this list from being too biased, so I'll disclose again that I am a technical trader, and my preference leans towards technical analysis just from my own experience, but I wanted to include some good Fundamental books in here as well.

Best Day Trading Books for Beginners

Technical Analysis Masterclass

Should be free for Prime/Kindle members; it wasnota masterclass, but a great overview of TA.

Technical Analysis, The complete resource for technicians, Kirkpatrick

This book is significant (and the CMT text), but it has statistics for how often each pattern tends to work — a very helpful guide. My favorite book on Technical Analysis — there’s nothing that isn’t covered in this book in depth.

The Intelligent Investor, Graham

Value Investing Bible, and maybe breaks my Warren Buffet rule by transitive property. If you’re going to read a value investing book, this is the one to read — nothing more advanced is needed.

Intermediate: Finding Alpha, Falkenstein

This book reviews fundamental factors, and provides a backtest based on quartiles (top vs bottom, filtered by for ex. EPS Growth and EBITDA to book value). It provides a valuable guide in building fundamental filters for universe selection, or even filtering out existing strategy signals.

Mention

Pioneering Portfolio Management, Swensen

(He averaged 11.9% YoY from 99-09, and has provided $16.5B in value to the Yale Endowment—enough said)

To tie everything together, there are some fantastic books to bring light to the process of creating profitable trading strategies, and the routine involved. The first book is written by a personal friend whom I admire greatly, and a wonderful teacher to many aspiring new traders—not to mention World Series Futures 2x Winner.

Algorithmic Trading Books

Beginner: Building Winning Algorithmic Trading Systems, Kevin Davey

Fantastic coverage of every stage of strategy development; if you need to read one book, I would read this. Davey goes through everything from coming up with trading ideas to backtesting, and even monitoring implementation of new systems. Davey’s greatest contribution is his guidelines on Trading System production — it helped me to realize this is constant work, always improving and finding new Alphas.

Trading Systems, Jaekle & Tomasini

Simple book that provides an overview to all aspects of system trading. This book was particularly helpful in coming up with new system ideas, and also provides a great intro to Portfolio Optimization techniques.

Algorithmic Trading, Chan

A fundamental book in quant trading, excellent coverage of mean reversion techniques. I was a bit underwhelmed with the coverage of Momentum strategies in favor of mean reversion, but that’s likely because of my personal preference towards Momentum. For an introduction to the technical and statistical models needed for Quantitative/Algorithmic Trading — look no further.

Advanced: High-Frequency Trading, Aldridge

This probably doesn’t apply to most, but I found it to be one of the most interesting trading books I’ve read in years. Provides a loose recipe for creating a HF infrastructure. Provides a fantastic look into the world of low latency, and provides incredibly useful research tables on Max Sharpe per Interval.

Mentions

Algorithmic Trading & DMA

Great book, however likely not applicable.

I wanted to make another point about what I consider to be the ‘wrong’ reading material. I believe market microstructure to be important to understanding mechanics, however I think it's overrated. First of all, it's ever-changing and most of what you'll read is outdated. Second of all, it's most useful in minimizing latency, and latency is not a retail traders field. If you're not in sub microseconds of latency, I don't think it's worth spending significant time on. Algorithmic Trading & DMA is a great book, but I think it's application is not fit for this list unless the goal is to work in HF.

I also wanted to provide a mixed list of some of my favorite code books that AREN’T Python, so just in case you find yourself looking to expand your horizons as I once did, you don't accidentally buy a Bjarnes Strastroup book to learn C + + (as I once did).

Best Non-Python Books for Algorithmic Trading

Beginner: Practical C + +, Oualline

I learned C + + working through this text, it’s great.

Cython: A Guide for Py Programmers, Smith

If you’re looking for a challenge in Python, or need to speed up some code — look no further.

Matlab, A Practical Introduction to Programming & Problem Solving, Attaway

Great intro MATLAB book, I learned MATLAB with this text.

Learn C# in One Day and learn it well, Chan

I initially purchased C# In Depth, found it unreadable for my beginner level, and worked through this in a matter of hours with a new love for C#. Perfect C# opener.

Advanced: C+ + Cookbook

I love cookbooks, and this one is no different.

Essential C# 7.0 (or 8.0)

Comparable to Practical C + +, a nice hefty book clear enough for beginners.

High Performance C + +

Covers added features like BOOST library, and works much like a cookbook.

Mentions

https://www.learncpp.com

https://matlabacademy.mathworks.com

https://www.learncs.org

I hope this list proves as valuable to you as it has been to me; I can't even express how helpful these titles were and continue to be to my everyday work. I also hope this isn't a daunting task, as this isn't supposed to be an overnight process — it takes a lifetime to acquire the skills to be a profitable trader, and the best part is the learning phase never really ends. The best way to learn to code is to open an editor and start working through problems, and finding solutions. This applies to most aspects of trading, the only way to learn is by doing — but hopefully these books can help provide some context, and point you in the right direction.

Disclaimer: The views, opinions, and information provided within this guest post are those of the author alone and do not represent those of QuantInsti®. The accuracy, completeness, and validity of any statements made or the links shared within this article are not guaranteed. We accept no liability for any errors, omissions or representations. Any liability with regards to infringement of intellectual property rights remains with them.

---

*Imported from QuantInsti Blog on 2026-04-27*
