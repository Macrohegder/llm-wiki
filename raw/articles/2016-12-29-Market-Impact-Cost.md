---
title: "Market Impact Cost"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/market-impact-cost/"
date: "2016-12-29"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Market Impact Cost

**来源**: [QuantInsti](https://blog.quantinsti.com/market-impact-cost/)  
**日期**: 2016-12-29  
**作者**: QuantInsti

---

## 原文

Market Impact Cost

ByMilind Paradkar

Market impact cost, a very important component of trading costs get closely tracked by portfolio managers as it can make or break a fund’s performance. In this post, we will throw some light on market impact cost, and identify its sources and the different means adopted by portfolio managers to mitigate it.

Trading costs breakup- Before we dive in, let us first view the break-up of trading costs for a portfolio manager. These get bucketed into:

Explicit trading costsBrokerageTaxes

Brokerage

Implicit trading costsMarket impact costOpportunity cost

Market impact cost

Opportunity cost

Explicit trading costs include brokerage and taxes and are easy to quantify. These costs are listed by the brokers as a part of the agreement with the portfolio managers. The second category i.e. implicit costs are not easy to quantify and various studies have been undertaken by academic researchers and practitioners to quantify, predict, and mitigate impact costs and thereby improve the portfolio performance and net returns.

Market Impact Cost defined

Market impact cost or simply “impact cost” is caused by the difference between the price before the trade is initiated and the actual price at which the trade gets executed.

Market impact cost is of two types: temporary and permanent. The temporary component is transitory in nature and reflects the price concession needed to attract counterparties at the time of order execution. The permanent component reflects the information that is transmitted to the market by the buy/sell imbalance. Thus, we can summarize impact cost as:

Market impact cost = Temporary component + Permanent component

Example:

Consider the order book shown above. The ideal price for executing a trade can be defined as the average of the best bid and offer price, in the above example, it is (22.50+22.75)/2, i.e. 22.625. In an infinitely liquid market, it would be possible to execute large transactions at a price close to this price of  22.625. In reality, more than  22.625 per share may be paid while buying and less than  22.625 per share may be received while selling the stock.

In the example above, a sell order for 4000 shares will be executed at a price of 22.3875 which is 1.05% worse than our ideal price of  22.625. Thus, the impact cost of the trade stands at 1.05%.

Empirical estimation of impact cost

A research report published by David Gallagher and Adrian Looi which examined the market impact cost of 26 Australian institutions found that the active managers of these institutions incurred an impact cost of 0.27% (on a principal-weighted basis) for a round-trip package, while the mean abnormal returns gained through a rough trip transaction stood at 0.92%.

From this research, it becomes apparent that impact costs can significantly affect the performance of a portfolio and thereby the net returns generated. Hence, it becomes imperative for a portfolio manager to identify the factors driving impact costs and devise strategies to mitigate these and contain them within acceptable standards.

Factors driving impact cost

Following are the important factors that drive impact cost -

Trade size –Impact cost is proportional to the trade size executed. When the trade size is large and accounts for a high proportion of the total trading volume in the stock, impact cost can be expected to be on the higher side. This is because large trades can cause a significant adverse movement in the stock price.

Manager’s Style –Apart from the trade size and complexity, a portfolio manager’s style also contribute in determining the impact cost. Factors like manager’s investment objective, the amount of funds under management, assets traded etc. have a bearing on impact cost. For example, a manager who wants to trade immediately faces the risk of higher impact cost compared to a manager who can spread his trades over a number of days.

Manager’s Skill –The research work by David Gallagher and Adrian Looi found that some managers incurred a cost in excess of 1%, while some managers gained a benefit of over 2%. Thus, the skill of individual managers also assumes importance in controlling impact cost.

Different ways to mitigate the impact cost

One common strategy involves slicing large market orders into small quantities and trade over a period of time to mask the intention of the portfolio manager.

Another strategy involves dividing trades among several brokers and thus preventing all the information flow to a single broker.

A research paper on identifying expensive trades found that only 10% of the trades determined 75% of the total market impact cost. This indicates that portfolio managers can substantially reduce impact cost by focusing on such expensive trades.

Advent of Machine Learning Models in Predicting Impact costs

Machine learning has found wide application in the algorithmic trading world today. Researchers have developed & deployed parametric and non-parametric machine learning models in an effort to predict market impact cost. Some of these models have been found to be successful towards this objective. For example, a research paper on using nonparametric machine learning models for predicting impact cost used a state-of-the-art nonparametric machine learning model which usedneural networks, Bayesian neural network, Gaussian process, and support vector regression, to predict market impact cost accurately. The non-parametric model was able to outperform a state-of-the-art benchmark parametric model in four error measures.

These machine learning models add to the repository of the existing traditional measures that are being used to control and mitigate portfolio impact cost.

To Conclude

In this post we defined market impact cost, factors driving it, and learned why the cost assume significance for portfolio managers. Quant researchers worldwide continue to conduct research and develop newer models in their quest towards unraveling impact cost.

Next Step

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to be a successful trader. If you also want to learn more, you can explore ourAutomated Trading Coursehere!

References:

David Gallagher and Adrian Looi,An Examination of the Market Impact Costs of Active Australian Equity Managers

---

*Imported from QuantInsti Blog on 2026-04-27*
