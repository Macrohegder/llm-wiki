---
title: "Paper Review: An Effective Intraday Momentum Strategy"
url: "https://open.substack.com/pub/quantmacro/p/paper-review-an-effective-intraday?r=1ppqsv&utm_medium=ios"
author: "quantmacro"
pub_date: "2025-03-14"
summary: "学术论文综述：基于日内波动率锥（VSO）的SPY动量突破策略"
---

# Paper Review: An Effective Intraday Momentum Strategy

**来源**: [https://open.substack.com/pub/quantmacro/p/paper-review-an-effective-intraday?r=1ppqsv&utm_medium=ios](https://open.substack.com/pub/quantmacro/p/paper-review-an-effective-intraday?r=1ppqsv&utm_medium=ios)
**作者**: quantmacro
**日期**: 2025-03-14

---

Link to paper: Beat the Market An Effective Intraday Momentum Strategy for S&P500 ETF (SPY) by Carlo Zarattini, Andrew Aziz, Andrea Barbon. Swiss Finance Institute Research Paper No. 24-97

I came across this paper recently and decided to give it a read. I had looked into Opening Range Breakout (ORB) type strategies in the past, which were classic breakouts that were developed by the likes of Crabel, decades ago. There is still a typewritten pdf file talking about that stuff somewhere on the internet. 

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribe

This paper is a fresh take on the ORB strategy, although the results are a bit too good to be true. I will first talk about what I like about the paper, then have a few constructive critiques about it. In no ways this is a summary of the paper, interested readers should read the paper itself. 

The breakout strategy they use can be described as a way to define a “noise band”, where the noise is related to the volatility of returns from Open until time T, on a given day:

Let me call this quantity VolSinceOpen or VSO. 

The novelty of this relatively simple way of calculating VSO using historical intraday returns is that it takes into account the intraday seasonality of volatility. One should expect higher volatility during open and going into the close, with a lower volatility during mid-day. This results in an intuitively meaningful noise cone, where the cone ramps up quickly near the open where there is high market volatility, then slows down, and into the close it ramps up again with increased volatility

A naive way to calculate this cone would have been to use the daily volatility σ and scale it as: 

\(\sigma \sqrt{T}\)

where T is the ratio of hours since open to hours in trading session, and σ is in daily units. By using the empirical volatility measure, the authors take into account the non-uniform distribution of volatility throughout the day. 

The strategy always goes flat at the end of the day, as shown in Figure 2. I did not see any discussion of why this is important in the paper. I am not sure if this adds anything to the strategy returns other than adding transaction costs. It definitely makes the implementation simpler, since trading starts from fresh every day. 

Authors add a few bells and whistles which are quite sensible. Those are: 

Close the position before the EOD if the position was opened and the price action went against us 

Use a second trailing stop which is the VWAP of the day. If the price crosses below VWAP (for a long position), close the position

Add a multiplier for the noise boundary, so the boundary becomes N x σ. Larger N values result in less frequent trading, and in the absence of volatility targeting, lower returns 

Vol targeting, such that position sizes (once a position is opened) are adjusted to deliver constant volatility units per day 

Finally, the authors check the robustness of their system under different volatility (VIX) regimes, and various daily patterns. It seems like the strategy performs better in high vol regimes (VIX>20) but the relationship is not exactly linear. Also, without the error bars it is hard to discern whether there is a statistically significant difference between the low and high vol regimes. 

As for testing whether the daily patterns have any conditioning power on this signal, there is one thing that I am not exactly sure about. Authors do not disclose whether they are testing contemporaneous or predictive relationships. In other words, when they look for the presence of a certain pattern such as NR4 (Narrow Range 4 Days), are they looking for the presence of the pattern as of yesterday’s close? If so, that would be a predictive relationship, and it would be tradable. Otherwise, it would be a contemporaneous relationship, and it would be useful to describe when the signal works but it would not be tradable. I have a sense that they are looking at predictive relationships, but some clarification from the authors would be useful here. 

Another thing that strikes me here is that the hit ratio is quite low, around 43% for a strategy with a relatively high sharpe. This indicates that the strategy is highly convex, in other words the average gain is significantly larger than the average loss. 

To summarize, here are my follow-up questions to the authors. Overall, a solid paper. 

What are the execution assumptions? Do you assume instant fill once a signal is generated? What if you wait for the next bar, do you bleed alpha?

Why close the position at EOD? Have you considered keeping the position open until the next day, and evaluating that position at or near the open, in order to realize any continuation from yesterday’s close to today’s open? 

If you were trading this strategy using futures, would you still anchor the noise boundary to the cash open? Note that CME Globex trading hours for the E-mini S&P contract is 6pm ET until 5pm the next day. 

Actually.. They answered this question partially on the Q&A section of the paper. but no details on how they choose the open and close times. 

Why anchor the noise boundary to the open? What if an important market shock 

comes in at a time that markets are not very active (say 11am), and the market was stagnant until then? Would you not react because significant time has passed since open, yet market had not moved until 11am? 

Have you tried this for a basket of markets? Are the results robust in other stock indices, in different geographies? What about other asset classes? 

Overall a solid paper, you can tell that authors are practitioners with good understanding of underlying math and market fundamentals. 

84

3

4

Share
