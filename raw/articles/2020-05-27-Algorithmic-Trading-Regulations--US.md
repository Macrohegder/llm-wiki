---
title: "Algorithmic Trading Regulations - US"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/algo-trading-regulations-us/"
date: "2020-05-27"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Algorithmic Trading Regulations - US

**来源**: [QuantInsti](https://blog.quantinsti.com/algo-trading-regulations-us/)  
**日期**: 2020-05-27  
**作者**: QuantInsti

---

## 原文

Algorithmic Trading Regulations - US

ByZach Oakes

Ask any experienced entrepreneur what the most difficult part of starting a business is, and 8/10 will likely say ‘scaling effectively’; building an automated trading business is no different!

I’m going to take you through the checklist that I wish I had gone through prior to starting out as an individual, and eventually a CTA/CPO and RIA (and I’ll explain what these are in a bit).

I’ll be covering:

My experience

Going Live with Trading

Capital requirements

Which markets would you like to trade?

Which platform/language are you comfortable with?

How many trades should you go for per year?

High-Frequency Trading

Trading your own Capital

Trading outside Capital

Trading Capacity

Registration

Brokerage & Platform Opinions

My Favourite Platforms

My Favourite Automated Brokerages

My experience

When I first got into automation, I focused entirely on the strategies — all I did for almost two years was write and test signals, strategies, systems, and various filters to compile a sort of database of potential Alpha models.

I didn’t exactly plan my path like that, but it ended up being a good use of my time for the most part. Something I wish I had considered was more of the organizational aspects ofAlgorithmic Trading, and how exactly I hoped to scale.

Trading as an individual is quite simple - it really doesn’t require anything in terms of regulation aside from a brokerage account and capital. Trading outside capital is a different story - but it’s far simpler in the US than in other regions of the world.

Going Live with Trading

Let’s begin with the simplest method of going live — this involves simply opening a brokerage account at whichever firm you feel suits your needs best. There are a few considerations here, and it’s important, to behonestwith yourself about these.

For the remainder of the article, I’m going to operate under the assumption that you have developed and tested your automated strategies extensively. To me, that means you have a group of strategies, with low correlation to each other, that have been throughbacktests, Walk Forwards (WF’s), and a good period of simulation/paper trading to ensure real-time performance isn’t worlds away from your tested metrics.

If you haven’t done this, start by simulating them (ACTUALLY simulating - with execution, slippage and everything; Not just watching the code run real-time.)

Capital requirements

How much capital do you have to trade? It’s important to invest money wisely. Also, consider your drawdown levels, and realize that live drawdowns will likely exceed your backtest/ WF levels. I’ll be frank and give what I would consider being comfortable starting capital levels for these markets, keep in mind that these levels are my opinions and bootstrapping for less may be possible.

A good way to determine capital requirements is to multiply your drawdown by 1.5 or 2.0, then add the capital requirements for the instruments, and go by that amount PER SHARE / CONTRACT. For example; ES @12.9k Initial margin + 3.5k Drawdown x 1.5 = $18.15k per contract.

Which markets would you like to trade?

This also circles back to the first point, as Futures is likely the most liquid — but also has a higher capital requirement if you need a large universe. Equities seem cheaper, and it can be cheaper to start out — but I find that it’s actuallymoreexpensive to trade any sort of scale in the equities.

There’s a 25K PDT minimum in Equities (Pattern Day Trader designation — cannot have more than 2 round trip trades per day if < 25k level) that can be prohibitive, but equities allow margin at this level at most brokerages (4x1).

Forex also allows 50:1 margin in the US and is probably the cheapest market to get your feet wet in. Please be mindful of the use of margin, as it can greatly increase modelled drawdowns (for example, your FX drawdown of 10K can now be 500K).

Which platform/language are you comfortable with?

In my opinion, the easiest ones are TradeStation’s Easylanguage, or TradingView’s Pine Script — though these are retail-focused languages. NinjaTrader’s NT8 is also good for any developers with C# / .Net experience (and is quite robust in general).

If you need a more robust full programming language, I suggest Python as long as latency isn’t a large factor (More on that next).Ease of Use is key here, you want something you’re COMFORTABLE in, not something that will take you a month to program a strategy in.

How many trades should you go for per year?

Getting an idea of your systems scale should not only help you negotiate commissions with any brokerage, but will also determine if you need to be concerned with latency - which is an expensive goal.

This should also give you an idea if you need to worry about things like PDT ($25K) minimums, and how important your trading costs are. If you’re trading intervals of >1M bars, I think any of these languages/platforms should suit you just fine.

If you’re going to be trading on tick level intervals, or 10-second intervals, using a lower-level language like C++ or C# may be needed — thus you’ll need a brokerage that integrates with C++, C#, or Java (Interactive Brokers’ IB API does). Keep in mind there are firms that spend 9-10 figures monthly to ensure optimal latency; unless you’re trading 9 or 10 figures I find it best to stay out of the arms race ( even if you are trading huge figures).

High-Frequency Trading

If you decide to go with latency, you’ll need to consider costs like server colocation (Equities: Equinix NY, 2.6K/mo; Futures: CME Aurora, 5K+/mo). ~5k is the partial rack lease People on the retail end should, at the max, go for tools like Rithmic API, CQG, etc in terms of DMA.

On top of that you’ll need to be quite the C++, C#, or Java developer — and may also want to consider investing in a FIX engine for execution.

I really think for the purposes of this article it’s best to avoid this nearly endless expense — I’ve considered doing this many times and always end up being overcome by expenses when I get close to pulling the trigger.

Trading your own Capital

If you have the means to trade your own capital, that will definitely keep things simpler. Really all you need to do is open a brokerage account at a firm of your choice, fund it, and begin trading.

You may want to find an accountant that specializes in prop trading, or possibly create an entity to protect yourself (an LLC or S-Corp are most popular, and have tax advantages over a C Corporation).

If it’s your own money it’s likely personal preference as to whether you need to incorporate at all. I didnotincorporate when trading my own account, but it may have made it easier on my accountant. If you’re trading your own capital, your setup ends here; wasn’t that easy?!

Trading outside Capital

So you’ve had some success on your own, and you decide it’s time to open up your strategies to the public. If you determine it’s time to begin trading outside capital (ideally when you have 3+ years of a successful track record), there are some considerations and requirements in order to get registered.

Trading outside capital can bring many regulatory topics into the question, but it also puts a strain on your anxiety level, capital, and strategies. It’s important to ensure that you have the resources in all aspects to continue.

Trading Capacity

Many strategies that work wonderfully at say $1M simply fall off after $5M, and are nonexistent at $20M, and it’s important to know where your lands. Determining where exactly your model’s threshold volume is more of an art than a science.

There are a few different models that can be used, from the rudimentary to the rather complex. I’ve used a model as simple as 2.5% of ADV (Average Daily Volume) as a max Share Count.

Registration

My initial question — what markets are you trading — determines what registration you need. If you’re comfortable with your strategy's capacity, it’s most likely time to begin studying.

There are some exemptions for both Futures and Equities, but they have pretty low limits. I’ll mention these exemptions just in case:

Equities

You can have as many as five clients, and $50M state of $150M Federal and still be exempt under the private advisor exemption. Thereareother exemptions for things like Venture Capital, but really it’s five clients.

If you’re trading equities, you’ll need to either open an RIA or become a RIAR at an existing RIA (Regifted Investment Advisor (Representative)). The simplest route is to look up an RIA, and speak with them about becoming a RIAR — many places are open to these types of agreements, like Edward Jones and similar firms.

If you’d like to start your own RIA, you’ll need to file a Form ADV either with each state in which you have > 5 clients, or a Federal Registration if you meet the Federal Requirements (>$110M, for starters). You will also need to pass either a Series 7 or a Series 65. I’ll include a link for specifics of registering an RIA — from someone who has registered a federal RIA it is not an easy task.Info here.

Futures

You can manage up to 400k of outside money (400K of initial investments), and up to fifteen clients without registering as a CTA or CPO.

If you’re going with Futures, you have a few routes to go here. If you decide Futures, you’ll need to register as either a CPO / CTA (Commodity Pool Advisor, or Commodity Trade Advisor) — I suggest the latter for simplicity and cost. CPO is essentially ahedge fund, whereas CTA you simply control other peoples accounts.

This lack of custody (you never have possession of client money — simply a Limited Power of Attorney / Trade Agreement to trade the account the client owns.) for a CTA makes it much more lax in terms of regulation. There are no longer regular audits, you don’t have strict requirements on capital base, etc.

A CTA will cost you at least 5K to open, you’ll need a track record/performance capsule and various details of your accounts and strategies performance to date. You’ll also need to pass a Series 3 Exam with the NFA.Info here.

The easy route

For simplicity sake, I think the easiest route here is to simply start out under the Futures exemption, or speak with an existing RIA. If you have success, you can then register as a CTA, or even begin your own RIA.

Keep in mind you will now have to monitor every new client account as a CTA (or register as a CPO, which is more difficult/complex) — it’s not an easy undertaking in general. I did it with many wonderful partners, and it still is not easy to manage. The absolute simplest method is to simply trade your own account, and let that number grow naturally!

Brokerage & Platform Opinions

First off, let me explain the difference between Brokerage and Platform. A Brokerage is any Broker / Dealer that you can open an account and execute trades with. A platform is any front-end or programming language that can be used to automate trading — but this can also be a Broker / Brokers API.

A telling example is Multicharts, which is a Platform that uses Easylanguage (TradeStation’s Language/Platform) and can be used with a handful of different brokerages for execution (for example, Interactive Brokers, or GAIN Futures).

Free platforms are also available that make things easy and worthwhile.Blueshift, a recently launched backtesting platform with minute-level data covering multiple asset classes and markets, is one such example.

It is a free platform to bring institutional class infrastructure for investment research, backtesting and algorithmic trading to everyone. The best part is that it is now available for Live Trading as well, including for US Equities.

In the interest of full disclosure, I use Multicharts x Interactive Brokers for Equities, and TradeStation or Multicharts x GAIN for Futures (as well as Native Python x Interactive Brokers x IB Insync). In my personal opinion, Easylanguage (ELD) is really fast to get strategies to production — and I’ve used it effectively even at scale. If you don’t prefer Tradestation, you can use Multicharts to trade your ELD strategies with different brokerages — which is what I do.

My Favourite Platforms

Multicharts/Tradestation’s ELD:This is my favourite, as it utilizes ELD. It’s not cheap though, so if you’re just starting out I would skip this for now. I have used this for Futures, Equities, Spot FX, and Crypto even. ELD is as I’ve said the fastest way to get ideas into production that I’ve come across, but Multicharts isn’t cheap, I would use Tradestation to start, and if you like it go with MC for production when you canswingit.-TradingView Pine Script: They are always adding new features and integrations, I think it will be big in years to come as more than simply an analysis platform.

Ninjatrader/NT8:This is similar to TradeStation. The language NT8 is pretty impressive though, so if you’re coming from .NET I would definitely take a look at this. Multicharts also offers a .NET version that uses NT8 with other brokerages.

Python x IB-Insync:This is not Interactive Brokers API, but a third party framework to work with their API. I also have a modular strategy build using this that may prove helpful if you’d like to use Python and Interactive Brokers.

Alpaca: It seems to be growing rapidly. This is actually a Python API but can use TradingView Scripts as well

QuantConnect: A Python / C# API. This offers integration with IB, and some other Brokerages (GAIN for Futures, a Crypto and FX brokerage)

Blueshift: I like Blueshift better than most other Python based platforms. It is also free to use

My Favourite Automated Brokerages

Interactive Brokers: it is pretty good overall. The API works and has many language integrations; their commissions are competitive; they offer most instruments. (Futures, Equities, FX)

TradeStation: Most data is free - including popular Futures instruments - and the data is very good quality. The language (ELD) is excellent, and everything else is worth dealing with for the free use of the language. Commissions are VERY high, but for testing, this is by far, my favourite platform. (Futures, Equities, Options, FX, Crypto)

GAIN: It doesn’t really have a platform, but they’re very large, consistent, and offer very good service and flexibility in terms of instruments (Futures, FX)

NT8: Many of my friends swear by them. A robust platform, with exceptional error handling — just not really my style. (Equities, Futures, Options, FX)

Alpaca: They offer the ability to execute Tradingview and their own simple API via Python and more. I think in the future I will likely use Alpaca for native Python builds. They also offer free data once you have a minimum account size, and the API could not be cleaner. (Equities, Futures, FX)

TD Ameritrade:I feel that TD Ameritrade is good for Systematic Traders who want to do discretionary trading. They offer all asset classes, a great (barely automated) platform, TOS, and wonderful service — and free commissions in many instruments.

Conclusion

A consistent level of success is completely viable for those who are willing to put in the work.

As you can see there are many questions you must answer if you’re going the route of managing money for others, but for the most part, it’s quite simple if you’re only trading your own or are below the exemption levels — I suggest you stay below them for as long as you can! Let the scale come naturally, and don’t worry so much about how much money you’re managing — focus on your returns.

Note from editor: QuantInsti respects the author’s choices and preferences but we in no way endorse, support or suggest any brands in this article. The views are of the author’s completely. We prefer and promote usage of Python for Quantitative Trading.

Disclosure: Blueshift platform is a cloud-based platform offered by QuantInsti

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
