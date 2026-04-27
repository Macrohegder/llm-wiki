---
title: "Quantamental Trading Strategy: Fundamental Analysis and Quantitative Analysis"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/quantamental-trading-strategy/"
date: "2021-04-26"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Quantamental Trading Strategy: Fundamental Analysis and Quantitative Analysis

**来源**: [QuantInsti](https://blog.quantinsti.com/quantamental-trading-strategy/)  
**日期**: 2021-04-26  
**作者**: QuantInsti

---

## 原文

Quantamental Trading Strategy: Fundamental Analysis and Quantitative Analysis

ByAnkit Ahuja

In this blog, we are going to make a trading strategy, in which we will perform Quantitative analysis on fundamental data of the companies, and create a portfolio of fundamentally strong companies and analyse the performance of the portfolio.

Topics covered in this blog:

What is fundamental analysis?

What is quantitative analysis?

Why make a trading strategy using fundamental data?

How to make quantamental strategy?

Backtest the results

Compare the strategy performance against NASDAQ

What is fundamental analysis?

In accounting and finance, fundamental analysis is defined as the analysis of a company's financial statements i.e. its balance sheet, income statement and cash flow statements.

The motive behind this analysis is to point out the debt and other red flags which could lead to the downfall of the company. This kind of analysis helps one to judge the overall performance and health of the company in trailing years/quarters.

This analysis uses various financial ratios such as:

Price to Earnings Ratio (P/E Ratio)

Price to earnings ratio is calculated by dividing the stock price by earnings per share. This ratio is used to get an idea of the valuation of the company against its peers or the market.

Price to Book Ratio (P/B Ratio)

This ratio is calculated by dividing the stock price by the book value of equity or in other words the stock price is divided by its book value. This ratio is particularly helpful to judge the value of the company, whether it is undervalued or overvalued.

Enterprise Value to Sales Ratio (EV/Sales Ratio)

This ratio is calculated by dividing the enterprise value by sales or revenue of the company. This particular ratio is helpful to value a company against its sales considering both debt and equity.

Debt to Equity Ratio (D/E Ratio)

Debt to equity ratio or leveraging is a ratio particularly useful to analyse the debt level of a company. Whether the company is over leveraged or not. In other words how much of the company is financed by creditors and banks.

Net Debt to EBITDA Ratio

This ratio is also the leverage ratio, used to calculate the leveraging of the company. It depicts the company’s ability to pay off its debt or we can say for how long a company has to manage its current operations to pay off its current debt. Lower values are generally demanded as it shows companies ability to generate cash and pay their liabilities.

Debt to Assets Ratio (D/A Ratio)

The debt to assets ratio is calculated by dividing the debt by the total assets of the company, this ratio is used to get an idea of how much of the assets of the company are financed by the creditors. A lower ratio indicates that the company is able to self finance the new opportunities that can arise in future.

Fundamental analysis is also used to calculate the intrinsic value of the company. This helps the investors and traders to identify the companies that undervalued or overvalued. So, they can make decisions in accordingly.

What is quantitative analysis?

When various statistical techniques and other mathematical models are used to perform certain analysis or filtering, that kind of analysis is called Quantitative analysis. It can be used to identify stocks which satisfy certain conditions. These conditions can be some mathematical equations or filters.

To apply these concepts effectively in trading, explorequantitative trading strategiesthat leverage these techniques to build data-driven, systematic approaches to the market. This blend of statistical filtering and data-driven decision-making is at the heart of quant trading, where every trade is grounded in measurable evidence rather than intuition. Aquantitative trading coursecovering both fundamental and quantitative analysis can help you build and backtest such strategies in a systematic way.

The ultimate objective is to quantify the available piece of information into numeric value to facilitate decision making. In this kind of analysis, one uses various financial ratios and feeds them into a model, which has predefined steps, which make use of statistical techniques or mathematical formula and gives the desired output.

Why make a trading strategy using fundamental data?

NASDAQ tracks more than 3300 stocks across the sectors. But the question here is:

Where to invest and how to select the top-performing stocks and good companies?

According to a paper written by Fama and French professors onFactor Investing, we know that in the long term, the value companies perform more consistently as compared to other companies. But along with this, one question also arises on the fundamental strength of the company.

Is the company fundamentally strong and relatively undervalued or is it undervalued because its fundamentals are weak?

So the question is,

Can’t we consider both the above statements and make a strategy?

A strategy that is able to give us a set of companies that have performed better as compared to their previous quarters, and are also relatively undervalued as compared to their peers.

As we know after the Covid-19 pandemic, some companies have ceased to function overnight without any further notice. So, we need to select companies that have a good amount of fundamental backing such as cash reserves, and strong margins to face these kinds of ups and downs in the market.

How to make Quantamental strategy?

The Formulation has been divided into 2 Parts:

Evaluating a company against its peers.

Evaluating the past performance of the company with itself.

Evaluation of a company against its peers

Top 14 NASDAQ tech stocks have been chosen by market capitalisation.

Ratios listed below are used for evaluating the company against other companies.

Price to Earnings Ratio (P/E Ratio).

Price to Book Ratio (P/B Ratio).

Enterprise Value to Sales Ratio (EV/Sales Ratio).

Debt to Equity Ratio (D/E Ratio).

Net debt to EBITDA Ratio.

Debt to Assets Ratio (D/A Ratio).

To derive the value factor out of the companies, we are taking the inverse of these ratios.

After taking the inverse of these ratios, we will be taking the Z-score of these ratios. The rationale behind the Z-score is to normalise the ratios and remove any bias, and then the scoring algorithm will be used to calculate the final score of the companies.

The greater the score, the more undervalued it is, with respect to its peers.

Scoring Algorithm: A penalty algorithm is coded, whose reference has been taken from the “S&P Value bse Factor indices Paper”, where if the Z-score is greater than 0. Then 1 is added to the score, where it is 0 then it is replaced with 1. And the places where it is less than 1, there a penalty has been given with the formula 1/(1-z).

We have used the function “key_metrics” of thefundamentalanalysis package, as it returns previous year ratios as well. The listed snippet shows the retrieval of the ratios.

Note: You have to get your own free api key by visiting theFinancial Modeling Prepwebsite.

Evaluation of a company against its own previous performance

We have compared the companies among its peers. Now, we will compare these companies with their past quarter-to-quarter performances. We will refer to the academic paper written by “Hong-Yi Chen, National Chengchi University, Taiwan and Cheng-Few Lee, Rutgers University, USA”, where we calculate the F-score (Max, Min) and G-Score

(Max) to do an intra-company analysis. Using the same package of fundamental analysis, we extract the previous year’s ratios also.

F-score(max) uses the ratios which must increase from Quarter to Quarter as R&D to Revenue must increase to showcase the innovative power of the company. Current Ratio (Current Assets to Current Liabilities) must increase so that the company can clear off its Current Liabilities with Cash, Inventory & Receivables.

F-score(min) uses the ratios which must decrease from Quarter to Quarter.

G-score(max) uses the ratios which must again increase, but these ratios are more concerned with Cash Levels and Net Income.

Any addition of the ratio can be done to make the analysis more comprehensive and strong, but would have to take care of the correlations of the ratios to avoid unnecessary addition to the model.

Now, conditions which used to rank and score the companies are:

If the quarter-to-quarter change of F-score (max) and G-score (max) is more than 0, then +1 has been given at that place. And where it is less than 0, then -1 has been given as a penalty.

With the F-score(min) where the change has been less than 0, then +1 has been given at that place. And where the change has been more than 0, then -1 has been given as a penalty. This method is used because the F-score(min) needs to be reduced quarter to quarter.

This score contains the company’s performance with respect to its peers and also its own previous quarters. The Companies with the high score are better-performing companies in the previous 5 quarters, and are relatively undervalued as compared to their peers.

So, we can select the top 5 companies, more or less, according to the need and invest in them. As we are assured that those top 5 companies are fundamentally sound as compared to their peers and their past years as well. This method can be extended across the sector to get top-performing companies of the respective sectors.

Backtest the results

We have now made the strategy to select the companies, which are fundamentally sound and have shown good performance over the last financial year. Now we apply the same strategy, but year-wise, over the group of companies and then take positions in them over the year-long, and then reselect the companies at the start of each year. For convenience, we will take the weighing method to be equally weighted.

The course covers the key aspects ofbacktestingsuch strategies, ensuring you understand how to validate your approach using historical data. By learninghow to backtest a trading strategyeffectively, you can refine your strategy and adjust your positions for optimal performance across different market conditions.

The listed snippet shows the retrieval of the data from the repository of the package and ranking it according to the Z-score year-wise. The next step would be to calculate the F and G score and rank the companies, then take the positions in them.

The following snippet shows the cumulative score of the company year-wise.

The above snippet shows the calculation of the return of the strategy along with the rebalancing of the companies according to their score. The top 6 companies have been selected to take long positions, and the return series has been calculated. 6 are selected to avoid the over-concentration in any one company and keep allocation to a maximum of 16.66%, but it can be changed accordingly.

You can see the lists of the companies in which we have invested according to their scores, and while the score changed year-wise. So according to that, we changed the companies.

Compare the strategy performance against NASDAQ

Let us now review the performance of the strategy against the benchmark ‘NASDAQ’.

The above graph shows the monthly returns of the strategy we just formulated, with the start period from January 2017 to December 2020. Colour coding has been used.

A colour index has been added just beside the graph, which is used to give the colours to the months. Months with returns of less than 10% have been given the red colour, and then the intensity of the colour is gradually increased as the returns approach the 15% figure.

Conclusion

As we can see, portfolio is performing better than the benchmark and has outperformed it, as well as in terms of cumulative wealth. So, we can say that this strategy is working well.

More additions can be done to this strategy like using technical analysis, and after choosing the fundamentally good companies to filter companies, which are also havingmomentumin them.

We can also use the GMV optimiser or MSR optimiser to weigh the companies to get better performance, and make the portfolio well optimised.

Bibliography

Technical, fundamental, and combined information for separating winners from losers

S&P BSE value factor indices paper

File in the Download

Code for Quantamental Strategy

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
