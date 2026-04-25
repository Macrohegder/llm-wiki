# Portfolio Development Series - Part 5

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-21e

**发布时间**: Aug 25, 2025

**抓取时间**: 2026-04-25 09:04:29

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 5
ASX Long Side Trend Following System On Small Cap Stocks
TradeQuantiX
Aug 25, 2025
∙ Paid
9
8
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is the first article in the Portfolio Development series focusing on a market outside the US market. While most traders and investors concentrate on the US markets due to its liquidity and maturity, the US market is not the only viable market to trade. The A...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 5
ASX Long Side Trend Following System On Small Cap Stocks
TradeQuantiX
Aug 25, 2025
∙ Paid
9
8
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is the first article in the Portfolio Development series focusing on a market outside the US market. While most traders and investors concentrate on the US markets due to its liquidity and maturity, the US market is not the only viable market to trade. The Australian stock market, known as the ASX, offers diversification opportunities for a systematic stock trading portfolio.
As I’ve mentioned in all my articles, each piece in this series focuses on a specific aspect of the system development process to keep things fresh and engaging. In this article, while I’ll briefly cover how the system works and its in-sample and out-of-sample results, the main focus will be on
robustness testing
.
In this article, I will develop a long term trend following strategy for the ASX market. This trend following strategy will use moving averages in a way that reduces the dependency on just one single parameter combination.
As I always preach, the more we can leverage and be exposed to the entire parameter space, the better. Hence, this strategy will use a technique similar (but a little different) to what was outlined in the article below, to determine the entry and exit signals.
Premium Content Vault
Conquering Curve Fitting: A Game-Changing Technique for Robust Systematic Trading
TradeQuantiX
·
June 23, 2025
One of the biggest and most annoying problems systematic traders face is developing robust trading systems. Have you ever developed a new trading system that looked good in the backtest but fell apart during robustness testing?
This is generally a sign of unintentional curve fitting. We don’t try to curve fit, but it’s a lot easier to do accidentally than I wish it was.
Read full story
As a sneak peak, this is the system I will develop and then robustness test in this article. Not too bad for a long term trend following system!
Why The ASX?
The ASX has distinct advantages over the US market. The US market is relatively efficient, with many large institutional players extracting alpha everyday, leaving little for retail traders, like us. The ASX, on the other hand, is less institutionalized, providing more opportunities for retail traders to find an edge.
This is a double-edged sword, however. A mature, institutionalized market tends to be highly liquid, whereas a less mature, less institutionalized market like the ASX is typically less liquid. While smaller markets like the ASX may offer greater edges to exploit, the reduced liquidity can be a challenge.
Depending on your trading style, this lower liquidity may or may not be an issue. If you trade systems with long-term time horizons (holding trades for weeks, to months, to even years) in a less liquid markets, you’ll likely be fine. This is because the increased expectancy due to holding positions for long periods of time can overcome the extra slippage caused by lower liquidity.
However, if you’re trading a fast mean-reversion system on the ASX, like the one we developed for US markets in Part 3 of this Portfolio Development series, your profits could be eroded by excessive slippage due to illiquidity. This isn’t to say there are not stocks in the ASX which are liquid, there are quite a few very liquid stocks on the ASX, there are just fewer than in a more mature market, like the US market.
In summary, smaller markets provide larger edges for retail traders to exploit, but these edges are generally best captured on longer timeframes to mitigate the impact of slippage due to lower liquidity. It’s also worth noting that commissions on the ASX are higher, likely because it’s a smaller market with fewer brokers, thus there is less competition to drive the commission prices down. Higher commissions and lesser liquidity leading to more slippage is a disaster for short term trading systems, hence we are looking longer term.
This is why I’m developing a long-term trend-following system for the ASX market. Being long-term, the system’s expectancy should be high enough to remain robust to significant slippage and commissions. The system will focus on small-cap stocks, as smaller stocks on smaller markets tend to offer larger edges for us retail traders to exploit.
Institutional investors often can’t easily trade smaller stocks due to liquidity constraints, making it easier for us retail traders to compete. Running a long-term trend-following system on ASX small-cap stocks is like playing poker against your drunk friends instead of a professional poker player.
The ASX Trend System Rules:
I personally run multiple trend-following systems in my systematic trading portfolio. Rather than leveraging an existing system I already have, for this article, I wanted to create something original. I went a completely different direction than I would normally go for trend following. While the indicators and filters I used are not original, I think the way I used them is original and also adds robustness.
I’m a big believer in always pushing yourself to coming up with new ideas, no matter how goofy they may seem. You never know, one of those ideas may work. This is exactly what I did here, I forced myself to go outside the normal way I define trend following, and the results were pretty interesting.
I built the system on an in-sample dataset from 2000 to 2018, with out-of-sample testing ranging from 2018 to mid-2025 (today). The rules I finalized for the system are as follows:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
