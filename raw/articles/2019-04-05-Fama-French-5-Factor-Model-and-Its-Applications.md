---
title: "Fama French 5 Factor Model and Its Applications"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/fama-french-five-factor-asset-pricing-model/"
date: "2019-04-05"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Fama French 5 Factor Model and Its Applications

**来源**: [QuantInsti](https://blog.quantinsti.com/fama-french-five-factor-asset-pricing-model/)  
**日期**: 2019-04-05  
**作者**: QuantInsti

---

## 原文

Fama French 5 Factor Model and Its Applications

This article was originally posted on Quants Portal.

ByRujeko Musarurwa

The relationship between risk and return has long been a topic for discussion and research. Investors and investment managers seek financial models that quantify risk and translate that risk into estimates of expected return on equity (Mullins, 1982). This post will look at and discuss the Fama French 5 factor model and its applications.

This article will begin by discussing the theory and where the model originated from. A discussion of when and how the model is implemented and applied will then follow.

Ultimately it will be seen that the Fama-French five-factor model is an improvement from previous models but that it still has some drawbacks and areas that can be improved on.

Background and History

Different methods and models of pricing securities and thereby determining expected returns on capital investments has been improved and developed over the years.

In the beginning, 1964, the single-factor model also known as the capital asset pricing model was developed. This single factor was beta and it was said that beta illustrated how much a stock moved compared to the market. Stocks that moved more than the market had a higher beta and thus higher risk and return (DeMuth, 2014).

In 1993, Fama and French came up with the three-factor model with its two additional factors being size and value (e.g. book to market value). The three-factor model was a significant improvement over the CAPM because it adjusted for outperformance tendency.

Use Python to automate portfolio management

Self-paced online course

But, it did not explain some anomalies nor the cross-sectional variation in expected returns particularly related to profitability and investment (ValueWalk, 2015).

The Fama-French five-factor model which added two factors, profitability and investment, came about after evidence showed that the three-factor model was an inadequate model for expected returns because it’s three factors overlook a lot of the variation in average returns related to profitability and investment (Fama and French, 2015).

Application of theFama French 5factor model

The theoretical starting point for the Fama-French five-factor model is the dividend discount model as the model states that the value of a stock today is dependent upon future dividends. Fama and French use the dividend discount model to get two new factors from it, investment and profitability (Fama and French, 2014).

The empirical tests of the Fama French models aim to explain average returns on portfolios formed to produce large spreads in Size, B/M, profitability and investment.

Firstly, the model is applied to portfolios formed on size, B/M, profitability and investment. The portfolio returns to be explained are from improved versions of the sorts that produce the factor.

Secondly, the five-factor model’s performance is compared to the three-factor model’s performance with regards to explaining average returns associated with major anomalies not targeted by the model (Fama and French, 2014).

With the addition of profitability and investment factors, the five-factor model time series regression has the equation below:

Rit— RFt= ai+ bi(RMt— RFt) + siSMBt+ hiHMLt+ riRMWt+ ciCMAt+ eit

Where:

Rftis the return in month t of one of the portfolios

RFtis the riskfree rate

Rm - Rf is the return spread between the capitalization-weighted stock market and cash

SMB is the return spread of small minus large stocks (i.e. the size effect)

HML is the return spread of cheap minus expensive stocks (i.e. the value effect)

RMW is the return spread of the most profitable firms minus the least profitable

CMA is the return spread of firms that invest conservatively minus aggressively (AQR, 2014)

List of open Quant Jobs

Placement Opportunities available

The purpose of the regression test is to observe whether the five-factor model captures average returns on the variables and to see which variables are positively or negatively correlated to each other and additionally identifying the size of the regression slopes and how all these factors are related to and affect average returns of stocks values.

The tests done by Fama and French (2014) show that the value factor HML is redundant for describing average returns when profitability and investment factors have been added into the equation and that for applications were sole interest is abnormal returns, a four or five-factor model can be used but if portfolio tilts are also of interest in addition to abnormal returns then the five-factor model is best to use.

The results also show that the Fama-French five-factor model explains between 71% and 94% of the cross-section variance of expected returns for the size, value, profitability and investment portfolios.

It has been proven that a five-factor model directed at capturing the size, value, profitability, and investment patterns in average stock returns performs better than the three-factor model in that it lessens the anomaly average returns left unexplained.

The new model shows that the highest expected returns are attained by companies that are small, profitable and value companies with no major growth prospects (Fama and French, 2014).

The Fama-French five-factor model’s main setback, however, is its failure to capture the low average returns on small stocks whose returns perform like those of firms that invest a lot in spite of low profitability as well as the model’s performance being indifferent to the way its factors are defined (Fama and French, 2015).

List of open Quant Jobs

Placement Opportunities available

Conclusion

The Fama French 5 factor model has yet to be proven as an improvement compared to previous models however it has left room for better models to be further developed from it in the future.

Most investors still use the famous three-factor model but as methods seem to take some years before people start using, as industry personnel always have doubts.

Looking at the practical work done and shown by Fama and French it seems it would be in the best interests for investors to use the other factor models until this method proves its self in the empirical evidence.

In case you are also interested in developing lifelong skills that will always assist you in improving your trading strategies. In thisautomated trading course, you will be trained in statistics & econometrics, programming, machine learning and quantitative trading methods, so you are proficient in every skill necessary to excel in quantitative & algorithmic trading. Know more about the EPAT course now!

References

AQR, 2014. Our Model Goes to Six and Saves Value From Redundancy Along the Way. [online] Available at:https://www.aqr.com/cliffs-perspective/our-model-goes-to-six-and-saves-value-from-redundancy-along-the-way[Accessed 5 June 2015]

DeMuth, P., 2014. What’s up with Fama & French’s new 5-factor model? The Mysterious new factor V. Forbes, [online] Available at:http://www.forbes.com/sites/phildemuth/2014/01/20/whats-up-with-fama-frenchs-new-5-factor-model-the-mysterious-new-factor-v/[Accessed 6 June 2015]

Fama, E and French, K., 2015. Dissecting anomalies with a five-factor model. Social Science Research Network. [online] Available at:http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2503174[Accessed 5 June 2015]

Fama, E and French, K., 2014. A five-factor asset pricing model. Social Science research Network. [online] Available at:http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2287202[Accessed 5 June 2015]

Mullins, D., 1982. Does the capital asset pricing model work? Harvard Business Review. [online] Available at:https://hbr.org/1982/01/does-the-capital-asset-pricing-model-work[Accessed 6 June 2015]

ValueWalk, 2015. The five-factor Fama-French Model: International evidence. [online] Available at:http://www.valuewalk.com/2015/05/the-five-factor-fama-french-model-international-evidence/[Accessed 7 June 2015]

Disclaimer: The views, opinions, and information provided within this guest post are those of the author alone and do not represent those of QuantInsti®. The accuracy, completeness, and validity of any statements made or the links shared within this article are not guaranteed. We accept no liability for any errors, omissions or representations. Any liability with regards to infringement of intellectual property rights remains with them.

---

*Imported from QuantInsti Blog on 2026-04-27*
