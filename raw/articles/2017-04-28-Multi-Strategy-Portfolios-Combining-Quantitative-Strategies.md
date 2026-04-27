---
title: "Multi-Strategy Portfolios: Combining Quantitative Strategies"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/multi-strategy-portfolios-combining-quantitative-strategies-effectively/"
date: "2017-04-28"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Multi-Strategy Portfolios: Combining Quantitative Strategies

**来源**: [QuantInsti](https://blog.quantinsti.com/multi-strategy-portfolios-combining-quantitative-strategies-effectively/)  
**日期**: 2017-04-28  
**作者**: QuantInsti

---

## 原文

Multi-Strategy Portfolios: Combining Quantitative Strategies Effectively

ByDerek Wong

Development of a successful algorithmic strategy is already a difficult endeavor. However trading a single strategy can pose its own set of risks, even if the strategy itself is robust and profitable.Understanding how to combine strategies effectively is an advanced skill typically built on a solid foundation, one that a structuredquant trading coursecan provide before you progress to multi-strategy portfolio construction.

So how do we as algorithmic traders understand exactly what our systems are delivering, change our mindset from development to implementation, and increase our risk adjusted returns?

Distribution Analysis of Trading Strategies

Most traders are familiar with looking at standard performance reports which have statistics like CAGR,Sharpe Ratio, and max drawdown. But these single numbers only provide a small glimpse into what the system is actually delivering. By addingreturn distribution analysisto your tool kit, you will be able tohave a better grasp about what the system may produce on a more granular level. Before combining strategies into a portfolio, each one must be individually validated, the course onbacktesting trading strategies pythonprovides the complete evaluation framework, including return distribution analysis, that every strategy needs to pass first.

The most common method for classifying a trading system is based on the entry type, either amomentum tradingormean reversion trading.This in the end is subjective and constraining, as many strategies will incorporate elements from both regimes. For example, a mean reversion strategy may employ the use of a filter that may have momentum characteristics. After this addition of the filter is it still a mean reversion system?

This problem can be solved by using statistical methods in orderto classify strategies by their distribution’s descriptive statistics, rather than by subjective type or style. By analyzing the skew, and looking at the tails of our return distribution we can get a much better indication of what the strategy is actually delivering. Thus allowing us to make a quantitative judgement as to which regime it belongs to.

Strategies as investable securities, changing your mindset.

Most novice traders think of their strategies as standalone systems, maintaining the same concept from ideation to implementation.  However, there are two distinct environments, the vacuum of the quantitative research laboratory, and the investment portfolio in which you will execute your strategy. We need to consider the implications of this implementation, and its effect on our current portfolio and the fit into our investment mandate. The best way to do that is to consider a strategy for allocation as an investable security.

At its most fundamental level any strategy has a singular purpose. Which is to deliver a return series with particular characteristics, usually outsized risk adjusted returns. If this is the case, then we can considera strategy that has been funded as making a long bet on that particular return series.This is the same as investing in any stock, commodity, or other asset.

Now there is basically no difference in motivation between investing in your strategy and investing in any other asset or security. You will allocate the most funds to those who exhibit the most desirable characteristics, and less to those who do not.

Applying portfolio optimization and diversification.

If we can accept this logic that investing in completed strategies, and investing in any other asset is the same.Naturally, the next logical step would be to create a portfolio.No one would recommend their friend to buy only a single stock. So why would you as a systematic trader only want to have one strategy?

We can now rely on two areas that have been heavily researched in academia and practiced in the field for many decades, portfolio optimization and diversification. By applying these very key principles that go into creating a portfolio of traditional assets, we can create a portfolio of multiple strategy systems.The same benefits that you get from creating a portfolio of traditional assets, such as decreased equity curve volatility and increase risk adjusted returns, can be then transferred to your set of systematic trading strategies.

Conclusion

QuantInsti® hosted a webinar, “Multi-Strategy Portfolios: Combining Quantitative Strategies Effectively”which was held on 16thMay 2017 and conducted by Derek Wong , Director of Systematic Trading at Foretrade Investment Management Co. LTD. You can click on the link provided above to access the recorded session of the webinar.

Next Step

If you want to learn various aspects ofAlgorithmic tradingthen check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.Enroll now!

---

*Imported from QuantInsti Blog on 2026-04-27*
