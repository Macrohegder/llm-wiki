# Portfolio Development Series - Part 7

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-278

**发布时间**: Sep 15, 2025

**抓取时间**: 2026-04-25 09:04:36

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 7
Assembling The Systematic Trading Portfolio
TradeQuantiX
Sep 15, 2025
∙ Paid
7
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
At this point in the portfolio development series, we have created four unique trading systems across three global equity markets. In this Part 7 article, I will start assembling a portfolio of systems so we can see the portfolio effect in action. What we will find when we build the portfo...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 7
Assembling The Systematic Trading Portfolio
TradeQuantiX
Sep 15, 2025
∙ Paid
7
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
At this point in the portfolio development series, we have created four unique trading systems across three global equity markets. In this Part 7 article, I will start assembling a portfolio of systems so we can see the portfolio effect in action. What we will find when we build the portfolio is that, even with just four trading systems, phenomenal performance can be achieved at the portfolio level.
In this article, I will cover a handful of topics, including:
Recap the performances of the four original trading systems.
Review the portfolio level goals laid out in the first article in this series.
Combine the 4 trading systems into a portfolio.
Understand the portfolio's strengths and weaknesses.
Outline next steps.
Ideally, this article will show you why having multiple systems working together within a systematic trading portfolio is the only true Holy Grail. There is no such thing as the Holy Grail at the trading system level.
The only Holy Grail that exists is the result of combining multiple different and uncorrelated trading systems into one unified systematic trading portfolio. This article will show you how to do just that.
As a sneak peek, here is where we end up: a portfolio of four trading systems, with allocations set such that each system contributes similarly to the overall equity curve. This shows the power of developing a systematic trading portfolio. Just four uncorrelated trading systems can create a magical result.
A Quick Recap:
First, let's start by recapping where we stand up to this point. We have developed four unique trading systems across three different equity markets. Each trading system has its own unique performance profile.
No individual system is amazing on its own. The good news is that no system has to be amazing on its own; what matters is the effect on the portfolio as a whole.
Below are the backtested equity curves and performance metrics for each of the four systems we have developed thus far:
System 1 - US Mega Cap Mean Reversion:
System 2 - US Mega Cap Momentum:
System 3 - ASX Small Cap Trend Following:
System 4 - TSX Momentum:
Next, let’s quickly outline the performance goals of the systematic trading portfolio. These goals were laid out in the second article in this series. We will see if the four-system portfolio is sufficient to meet these goals. If it does, great! If not, we will discuss methods to meet these goals in the Next Steps section.
If you missed the article that outlined these performance goals, you can check it out here:
Premium Content Vault
Portfolio Development Series - Part 2
TradeQuantiX
·
July 14, 2025
In the first article in this portfolio development series, we discussed the concept of portfolio-level thinking. I took a simple momentum system and applied portfolio-level thinking to show how the performance of one individual trading system does not matter as much as many believe. What really matters is how that one trading system contributes to a portfolio of many trading systems.
Read full story
Portfolio Performance Goals:
Portfolio CAGR Goal:
>20%
Portfolio Max Drawdown Goal:
<25%
Portfolio Max Drawdown Length Goal:
<1 year
Portfolio Average Drawdown Goal:
<10%
Portfolio Volatility Goal:
<10%
Portfolio Sharpe Goal:
>2.0
If the portfolio falls short of these goals, we will simply have to keep working toward them over time. We don’t have to be perfect from the beginning. A systematic trading portfolio is a never-ending improvement project anyway. You should always be striving to make the portfolio better.
These performance metrics were chosen loosely based on my own personal situation. I'm in my late 20s, looking for strong absolute portfolio performance to quickly compound my capital. I do not want to work in the corporate world my entire life, so I need a high CAGR to compound my capital quickly.
While I am willing to take on some risk to achieve a high CAGR, I do not want to take on so much risk that I am constantly stressed and can’t sleep at night. Hence, the drawdown tolerance at the portfolio level is moderate, at 25%, but not absurdly high.
Risk and reward are proportional. If I want more returns, I generally have to take on more risk. Therefore, I’ll accept downside risk up to 25% to achieve a CAGR of 20%.
Equal Weight Portfolio Allocation:
Now, let's start digging into the assembly of the systematic trading portfolio. But, before we start, let’s discuss some of the assumptions surrounding how this portfolio will work:
All systems will share capital from one account.
The systems do not operate in silos; they all work together and share the same capital from one account. If System 1 makes money, that capital is equally distributed across Systems 2, 3, and 4.
System allocation and position sizing are based on the net liquidation value of the account. This value is updated every day.
Every day, the allocations to each system are recalculated based on the net liquidation value of the account. These allocations are then used to position-size new trades within the system, but existing trades are not updated based on the day-to-day allocation fluctuations.
Open trades are not rebalanced based on changes in the account's net liquidation value; unless there is a specific rule in the system to rebalance periodically (some of the systems have a rule to rebalance monthly or if the trade size is significantly different from the current ideal size).
The starting account balance of the portfolio backtest will be $100,000.
There will be no deposits or withdrawals from the account over the entire portfolio backtest period. Only compounding of the original $100,000 will be shown.
Think of this portfolio as a team. If one member of the team is performing well, the entire team benefits. The dollar allocation to each system builds or reduces based on the performance of every other system, but the percentage allocation remains static.
There are many unique ways we can allocate capital to each trading system. I want to pick a few allocation methods and experiment to see which capital allocation method is the best to achieve our portfolio goals. The capital allocation methods I want to test are:
Equal weight allocation
Equal volatility weighted allocation (risk parity allocation)
Equal return weighted allocation (return parity allocation)
Each allocation technique has its own pros and cons. For example, equal weight allocation may be naively simple, but it ensures equal exposure to each system and/or market, which may be desired.
Let’s dive into each of these allocation methods, see how they behave, and decide which is best for this portfolio. We may even decide we don’t like any of these allocation techniques and instead go a hybrid route. There’s no correct answer; it’s all about experimentation and picking something that suits your goals.
One of the most important things is to pick an allocation style you can stick to without constantly changing allocations or quitting trading the portfolio altogether.
You may find that one of the allocation methods has better results on paper (however you define “better”), but it may not be something you would actually be comfortable trading live. For example, maybe the allocation method has amazing returns but too much risk for your liking. Thus, you modify the allocations to allocate less to some of the more volatile systems to create more of a hybrid allocation approach.
Portfolio allocation is more of an art than a science. You’re going to be the one who has to ride the equity curve of this portfolio every day, so allocate in a way that makes it a ride you want to take.
Equal Weight Portfolio Allocation:
We will first start with the simplest allocation method: an equal allocation percentage given to each system. Since the portfolio has four systems, each system receives 25% of the total portfolio capital.
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
