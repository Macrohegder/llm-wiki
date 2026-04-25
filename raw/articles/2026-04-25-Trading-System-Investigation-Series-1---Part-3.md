# Trading System Investigation:               Series 1 - Part 3

**原文链接**: https://www.tradequantixnewsletter.com/p/trading-system-investigation-series-02d

**发布时间**: Oct 14, 2024

**抓取时间**: 2026-04-25 09:01:59

---

## 摘要

Premium Content Vault
Trading System Investigation:               Series 1 - Part 3
A deep dive into a short term trading system found online. Is it worth trading?
TradeQuantiX
Oct 14, 2024
∙ Paid
43
10
3
Share
In the previous parts of this series, we explored a system we found online. We were able to code the system, make the system our own, improve performance, then take the system through an in sample and out of sample approach. Now, for part 3 we are going to investigate the system further with some robustness tests. Just passing out of sample alone is not enough to consider the system worthy of our capital. It could have been dumb luck that the system passed out of sample. We have to take it one step further, to the most important step, this is the step were we try to break the system...

---

## 全文

Premium Content Vault
Trading System Investigation:               Series 1 - Part 3
A deep dive into a short term trading system found online. Is it worth trading?
TradeQuantiX
Oct 14, 2024
∙ Paid
43
10
3
Share
In the previous parts of this series, we explored a system we found online. We were able to code the system, make the system our own, improve performance, then take the system through an in sample and out of sample approach. Now, for part 3 we are going to investigate the system further with some robustness tests. Just passing out of sample alone is not enough to consider the system worthy of our capital. It could have been dumb luck that the system passed out of sample. We have to take it one step further, to the most important step, this is the step were we try to break the system.
Try to break the system? Why would we do that? Good question. When we develop a trading system, we have to look at it from the perspective of “can this system prove to me it is worthy of my hard earned capital?”. The best way we can prove to ourselves a trading system is worth our capital is by trying to break the system and seeing if it holds up to the tests. If we throw every adverse scenario we can think of at the system and it still holds up, then that’s a good sign the system is robust. It is no guarantee that just because a system passes out of sample and robustness testing that it can’t crash and burn during live trading, but it’s definitely a great filter in preventing us from trading bad systems. If a system fails robustness testing, then we can surely assume that live trading is going to suck, but if the system passes robustness testing then live trading could potentially be pretty good.
Thanks for reading Systematic Trading with TradetroniX! Subscribe for free to receive new posts and support my work.
Subscribe
So how do we robustness test the system? Well there are probably hundreds if not thousands of methods and variations of robustness tests, but I am just going to perform a few in this article and see what conclusions we can make about the trading system. Before we go too much further, let me remind you what the trading system looks like (with slippage and  commissions included):
The system looks pretty dang good if you ask me, even with slippage and commissions included. So let’s now try to break the system and make it look terrible so we can either prove or disprove that this system is worthy of our hard earned capital.
The four robustness techniques I want to test out on this trading system are listed below. We will walk through each one-by-one and I will explain how the robustness test works. I will also share my thoughts on how well the system holds up.
+-25% parameter sensitivity test
Monte Carlo (trade order re-shuffle)
Slippage sensitivity
Testing the system on other trading universes
Like I mentioned, this is not an exhaustive list, but is a good start to see how the system holds up.
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
