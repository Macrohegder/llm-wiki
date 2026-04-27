---
title: "Quantitative Trading - Building Entry Ideas and Idea flow"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/quantitative-trading-building-entry-ideas/"
date: "2020-06-18"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Quantitative Trading - Building Entry Ideas and Idea flow

**来源**: [QuantInsti](https://blog.quantinsti.com/quantitative-trading-building-entry-ideas/)  
**日期**: 2020-06-18  
**作者**: QuantInsti

---

## 原文

Quantitative Trading - Building Entry Ideas and Idea flow

ByZach Oakes

One of my favourite Authors, Kevin Davey, preaches an idea that he calls the ‘Strategy Factory’ — and while all parts of the process are vital to the development of profitable strategies, without raw inputs (or new trading ideas), you will drastically limit your output. So how do you keep the ideas flowing, even after you’ve seemingly tested and optimized every combination of entry that you think viable? Let’s see.

In this article, we cover:

The flow of an Idea in Trading

Entry and exit

Generating Entry ideas

Inspiring new heights

Importance of generating new ideas

The flow of an Idea in Trading

A key part of automated trading is idea generation, and by keeping things simple you can greatly improve your output by improving the inputs. An easy way to do this is to make some of the variable aspects of a strategy constant – like using a fixed exit package – and focusing solely on new entries initially.

By optimizing the process of strategy development, you can create a constant output of fresh, unique signals that can be combined to drastically improve your performance.

So, how do we keep the ideas flowing? For me, I set a weekly threshold level of new ideas that I must test - in order to keep the inflow of signals constant. These aren’t always initial great ideas, but sometimes they inspire great ideas or an improvement on something existing. I try to create 5 organic entry signals each week.

Entry and exit

Let me speak to theentriesa bit more - initially, I have a generic Exit package (TrailStop, Fixed Stop, Boolean Target), and something I call asignalexit; basically just an extension of the entry logic that would exit the position.

It’s easier explained in an example - if I’m entering long when the 5 days MA crosses the 20 day MA, maybe my long signal exit is when the 5 day MA has a negative slope, or when they’re both negative sloped, or when 5 days is below the 20 days if it’s long-only.

Combined with my generic exit package - Pct Trailstop, Fixed stop, and Boolean Profit Target - I can basically copy and paste in my exit package, tweak the entry logic and I’m good to begin testing the strategy.

I do this for a few reasons:

Efficiency - it allows me to keep my idea flow up. Sometimes I do add a new exit signal idea, and consider that one of my 5 unique ideas that week. But most of the time I stick with my generic exit package.

Consistency - By keeping the standard exit package, I’m able to get an apples to apples comparison of how effective the entry signals are in a quick (Multicharts performance report) way.

Exits are taken care of, so I can focus on the entries - my idea flow now dependssolelyon an entry signal. So where do I generate these entry ideas, after I’ve tested all reasonable technical, fundamentals, and combinations of these signals?

Generating Entry ideas

I’m a technical guy, so I’ll admit that I have a preference towardsprice action tradinghere - but for me, I always like looking at charts to find new entry ideas. I engulf myself in a symbol, and will change the timeframe, or pair up a few timeframes on the same chart, maybe add an indicator or two, see if it’s showing me anything new.

Once I get something that looks like it could be a repeatable pattern,

I look for somementalentries on the chart.

I try to find examples thatdisprovemy signal i.e. Entry signals that would have performed very poorly.

Then, I see if maybe a different interval, an added indicator, or some OHLC pattern possibly would have removed this bad entry from the mix.

I look for filters, to make the pattern I found that much more reliable.

Keep in mind, to have an effective strategyyou don’t want to limit your trades too much; you need asolid amount of entriesnot only to add the potential for larger excess returns but also to increase your sample size and statistical significance.

If you have one entry a month, you could easily have a 6Mo drawdown with 5 bad trades in a row. If you have an entry every hour or so, if you’re still trading in a 6mo drawdown then you’re a bolder man than I.

So where do I turn when I’m just not seeing anything new in my charts? I have a few favourites for signal ideas, and if you give them a chance, I promise you’ll drastically improve your idea flow.

Inspiring new heights

TradingView:I browse popular chart markups, new indicator ideas, look for symbols I haven’t traded as often as others, and browse for general sentiment or biases I notice on a Macro level. Maybe every other chart is a Bitcoin to 50k chart, and maybe I disagree and can exploit this.To enhance your analysis, consider utilizingautomated trading with TradingView, which can help you implement strategies based on your insights and market observations.

Technical Analysis of Stocks and Commodities:(Magazine, or Website - Traders.com) This is one of my absolute favourites. Not only do you get fresh charts and perspectives, but they always have a new indicator (or a new take on an old indicator).They have diverse markets and symbols that are always helpful in developing a new idea. Most issues literally have a strategy in them translated to any platform you’re comfortable in.Start here, and see if it gives you any ideas for something a bit different.

Books:I find a lot of new ideas fromreallyold trading books; I particularly like the works of Larry Williams or Bill Williams. They have some timeless patterns in here, and while it’s far from a fresh perspective in terms of technology, they often provide a different perspective. Many of these older books are complete gems, and new books can be really helpful as well (Bean, Chan, Davey, Prado, Pruitt are some of my favourite authors).

Archive:When I’m developing a new strategy, if it doesn’t quite meet my expectations yet it’s still profitable, I archive it. I save it in a big database with its performance metrics, so that maybe later I can come back to it with something fresh.If I’m looking for a new idea, I sometimes start with strategies that didn’t quite pan out with fresh eyes and see if maybe I missed something. I’ve honestly been able to improvemostof my archived strategies simply by coming back to them later with new insights.Not all of them met my requirements once they were improved upon, but many of them did! Nothing feels better than salvaging an improved recycled entry idea that was very nearly in the trash.I also encourage you to go back through your ‘robust’ existing strategies list and see if maybe you can improve the ones that already meet your specs.

Importance of generating new ideas

The important part isn’t where you’re finding new ideas, it’s that you’re continuing to generate them at a consistent rate. These sources are what inspire me to find new methods of entry, but yours could be completely different!

I also want to be clear, this isn’t an Indiana Jones movie, and we’re not in search of the Holy Grail here — the goal isnewstrategies that generateexcess returns, with anegative correlationto existing Alpha models.

If you combine enough of these signals, it very wellcouldbe an ingredient to a revolutionary system. One thing is for certain though, without trying new (or recycled) ideas — your repertoire of Alpha’s will never grow. Put yourself out there; create something new and bold, you never know — it could be an ingredient inyourholy grailsystem.

Conclusion

While fresh ideas are the raw materials in your continued development, there are many ways to improve the bottom line - i.e. add new, robusttrading strategies. I’ve found that even thebeststrategies are often quite simple.

And while nobody knows what RenTec’s signals look like, I imagine they allstartedquite simple at the very least. They all must start somewhere, and I encourage you to do the same with these goals in mind.

Note from the editor: QuantInsti respects the author’s choices and preferences but we in no way endorse, support or suggest any brands in this article. The views are of the author’s completely. We prefer and promote usage of Python for Quantitative Trading.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to the accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
