# Portfolio Development Series - Part 3

**原文链接**: https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-144

**发布时间**: Jul 21, 2025

**抓取时间**: 2026-04-25 09:04:11

---

## 摘要

Premium Content Vault
Portfolio Development Series - Part 3
US Long Side Mean Reversion System On Mega Cap Stocks
TradeQuantiX
Jul 21, 2025
∙ Paid
20
12
3
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is the first article in this portfolio development series where I will focus on developing a trading strategy for the portfolio. Up until this point, we have focused on portfolio design considerations and understanding portfolio level thinking. Now it’s tim...

---

## 全文

Premium Content Vault
Portfolio Development Series - Part 3
US Long Side Mean Reversion System On Mega Cap Stocks
TradeQuantiX
Jul 21, 2025
∙ Paid
20
12
3
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is the first article in this portfolio development series where I will focus on developing a trading strategy for the portfolio. Up until this point, we have focused on portfolio design considerations and understanding portfolio level thinking. Now it’s time to get to the fun stuff: the actual system development work.
This article will focus on a US mega-cap long-side mean reversion system. To be honest, I’m not much of a mean reversion guy, but I understand the importance of having mean reversion system types in the portfolio.
My preference is with momentum and trend systems, but for you guys, I will step outside my comfort zone and develop a mean reversion system. Heck, if I like what I develop, maybe I’ll implement it into my own personal portfolio as well as the portfolio we develop throughout this series.
I’ll note that in each of these system design articles, I’m going to focus on a different part of the system development process to keep these articles from becoming stale. In some articles, I may focus on robustness testing; in others, the actual development of the system or how to brainstorm system ideas, etc.
In this article, I want to focus on the
in-sample and out-of-sample testing.
I’ll give a brief background on the development and why I made certain design decisions, but that won’t be the focus.
The focus will be the comparison between in-sample and out-of-sample performance, including my thoughts on the results, what concerns me, what I like, and what my next steps would be after seeing the out-of-sample results.
I think one of the things you’ll pick up on is in-sample and out-of-sample testing is just as much of an art as it is a science. We can have metrics to hit for the out-of-sample, but there are a lot of caveats and other things to consider that are harder to quantify. This is where some of the discretion comes in with systematic trading.
As a sneak peek, the images below show the equity curve, drawdown, and stats for the US mega-cap long-side mean reversion system that is discussed in this article. Not too bad, if I do say so myself!
Let’s get into it!
Systematic Trading with TradeQuantiX is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Mean Reversion And Capital Efficiency:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
