---
title: "Fundamental Analysis With Algorithmic Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/fundamental-analysis-performed-algorithmic-trading/"
date: "2017-12-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Fundamental Analysis With Algorithmic Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/fundamental-analysis-performed-algorithmic-trading/)  
**日期**: 2017-12-07  
**作者**: QuantInsti

---

## 原文

Fundamental Analysis With Algorithmic Trading

Investors who base their strategy on fundamentals operate in a very different manner than quantitative analysis based traders. Quantitative traders who base their strategy on technical analysis are able to scan thousands of charts per minute equipped with a bevy of indicators, ratios and data points finding the right instrument to suit theiralgorithmic trading strategy.

Fundamental analysis, on the other hand, is different. Fundamentals don’t change per minute the way prices change. Balance sheets, P&L statements, inventory, cash flow these things are made available at max once in a quarter.

Considering that, is there a way to analyze fundamentals the way quants analyze price-volume movements? Can you automate this process and maybe create an algorithmic trading strategy out of it? Once a fundamental signal is expressed as a rule, the logical next step isbacktesting trading strategies python, the Quantra course teaches you exactly how to test such rule-based fundamental strategies systematically before deploying them live. Well, this blog will help you do exactly that.

The blocks!

What goes into an algorithmic trading strategy? It’s simple, there is, of course, the data, the strategy (algorithm) and the broker’s API which will allow you to execute trades as per the strategy. Now let’s dig deep into each of these sections. Understand market mechanics with these essentialAlgorithmic Trading books.

The Data

This is the most crucial part of the equation. Where do you get fundamentals data of a company that is uniform, structured, accurate and most importantly in a format that a machine (algorithm) can understand?

Here is a list of reputable fundamentals data sources that are known for their data accuracy, variety and availability of a large number of trading instruments.

Additionally, you can also look at below data sources, just in case:

Benzinga

Airex markets

S&P Global NetAdvantage

EventVestor

Factset

Precautions to be taken:

Since the nature of the fundamentals data is different than your usual price data. There are many possibilities where your algorithmic trading strategy can end up taking wrong decisions based on not so correct data.

For example, some companies may lie in their reports, and there are multiple reasons as to why they would do this, but the most prominent is just to make them look good. Here are some such examples,

If the company includes receivables in the earnings reported. The money hasn’t come into their accounts yet but the company thinks the money will surely come at some point. But this could be a huge blunder for a fundamentals trader

Sometimes companies showcase sales numbers that are obtained by selling the product to their own related companies

Reports may not show any tax component for first three quarters but have a big one in the last quarter

Things like these come out in audits and the auditors make companies fix these issues, but the problem is important audits are conducted on yearly basis and you may have already taken a trade decision based on the pre-audited data. So how do we avoid these things? You can by sticking to some ground rules:

Only consider companies that have a history of disclosing data accurately

Include qualitative filters for small or unreliable stocks

Make sure the back-testing period is long enough

Be aware of forward-risks while conductingbacktesting, meaning things that might happen in future which could affect a stock’s performance are not usually present in balance sheet.

Trading strategy example based on fundamentals

Now let’s dive into an actual algorithmic trading strategy that is based on fundamental data. We have taken Quantopian’s help in this. Quantopian has tied up with Morningstar for fundamentals data, there are more than 600 metrics you can make use of in your algorithmic trading strategy.

Peter Poon, a dedicated quant on Quantopian has developed a strategy algorithm on fundamentals, he calls it “A quantitative value investing strategy using fundamental data”. Here’s what the strategy is all about.

Select no more than 15 stocks that satisfy the following rules: P/E < 12, P/B < 2, ROE > 15%, market cap > $100M

Hold the selections for one year, and re-do the selection next year

You can sign up for our ‘Python for Trading’ course that will teach (actually hand-hold you) to code your own algorithmic trading strategy. Here’s how the strategy performed during the backtest:

Performance in numbers:

Peter thinks the strategy results are in good agreement with the traditional value investing. The selected stocks in this algorithmic trading strategy outperformed the market by almost twice.

However, backtesting results are on paper, there are multiple factors (more in number than quantitative trading) that affect fundamentals of a company and its performance.Developing a strategythat includes all of them is a mammoth task.

Having said that, the markets are already moving towards algorithmic trading and slowly all sorts of data are being made available in machine-readable format. For example, news, social media and economic events based feeds are prevalent today.

You can read more about5 Things to know before starting Algorithmic Trading.

Conclusion

Incorporating fundamentals into an algorithmic trading strategy and letting it do the heavy lifting is the way forward. This approach presents a new dimension of possibilities that were not accessible to tradition fundamentals trader.

Take your first step towards learningalgo trading coursevia our self-learning portal Quantra and our comprehensive virtual classroom-based course Executive Programme in Algorithmic Trading (EPAT).

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
