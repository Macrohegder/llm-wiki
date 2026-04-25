# Volatility Targeting 101: Enforcing Equal Risk

**原文链接**: https://www.tradequantixnewsletter.com/p/volatility-targeting-101-enforcing

**发布时间**: Apr 28, 2025

**抓取时间**: 2026-04-25 09:03:04

---

## 摘要

Premium Content Vault
Volatility Targeting 101: Enforcing Equal Risk
Improving Trading Systems With Volatility Targeting
TradeQuantiX
Apr 28, 2025
∙ Paid
12
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Subscribe
Introduction:
I live by the mantra “keep it simple, stupid.” I apply this not only to my personal life and day job, but also to my systematic trading. At every step of my trading processes, I strive to eliminate unnecessary complexity. Overcomplicating things is...

---

## 全文

Premium Content Vault
Volatility Targeting 101: Enforcing Equal Risk
Improving Trading Systems With Volatility Targeting
TradeQuantiX
Apr 28, 2025
∙ Paid
12
1
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Subscribe
Introduction:
I live by the mantra “keep it simple, stupid.” I apply this not only to my personal life and day job, but also to my systematic trading. At every step of my trading processes, I strive to eliminate unnecessary complexity. Overcomplicating things is the enemy of system stability and robustness, it also opens the door to mistakes.
That said, I once confused complexity with proper modeling in one aspect of systematic trading. Since then, I have changed my mind and in this article I will show you why. In my eyes, complexity exists on a three-point scale, ranging from naïve to simple to complex:
The goal is to balance simplicity and complexity without drifting too far toward naïveté. However, with one specific trading topic, I leaned too heavily into naïveté, not even realizing it, mistaking it for simplicity.
That topic is volatility targeting.
Subscribe
📈
If you’re passionate about systematic trading and seeking guidance toward success, I can help!
🥇
I’ve worked as a systematic trading consultant for a private trading community for over 2.5 years, successfully helping more than 100 clients achieve their trading goals.
🚀 Now, I’m launching TradeQuantiX Consulting Services, offering personalized one-on-one coaching to help you master the intricacies of systematic trading.
📚
To learn more, click the image below to visit my website. There, you can book a free 30-minute introductory session to discuss how I can help you succeed as a systematic trader.
My Old Thinking vs. My Current Thinking:
For a long time, I opposed volatility targeting. Every trading system I built used simple equal-weight position sizing. If a system held 10 positions, each received a 10% allocation. It was simple, straightforward, and it worked. But I was naïve about what volatility targeting truly is and what it achieves. Here’s my old thought process:
“Any stock I buy that meets my entry criteria has an equal opportunity of outcome, meaning all stocks I hold have the same probability of being a winner or loser. Thus, using anything other than equal position sizing introduces a non-linear impact on those odds that’s difficult to measure.”
Part of that is true, but I was missing one crucial component. I was assuming the size of the winner or loser was consistent, which is not the case because every stock moves in a different range i.e volatility. The varying magnitude of price movements (in percentage terms) must be normalized to make stock A comparable to stock B. Here’s my revised thinking after learning over the years:
“Any stock I buy that meets my entry criteria has an equal opportunity of outcome, meaning all stocks I hold have the same probability of being a winner or loser. While the probability of outcomes is the same, the magnitude of price swings differs for each stock. Thus, these price swings must be accounted for to normalize stock behavior, making them comparable. Only then are the odds of being a winner or loser truly comparable.”
Consider this analogy: You study blackjack enough to gain a slight edge and visit a casino to make money. You start at a low-stakes table with a $10 buy-in. You win 7 out of 10 hands, earning $70 in profits and losing $30, for a net gain of $40. Then, you move to a $50 buy-in table, play one hand, and lose, resulting in an overall net loss of $10. You played 11 hands, won 7, and lost 4—a great win percentage—but still ended up losing. Why? The magnitude of the game changed; the volatility changed. If you had stayed at the $10 table, you’d be net positive. Even playing all night at the $50 table would have yielded a profit because the volatility per hand was consistent. When volatility changes between hands, outcomes become non-linear. The thinking for my original position-sizing approach was backward: equal-weight sizing creates non-linear outcomes, while volatility targeting normalizes them.
Admittedly, my original thinking about position sizing was embarrassing. It’s all part of the learning journey, though. I’ve had to figure this out myself over the years (with help from a mentor or two). This newsletter aims to accelerate your progress by sharing my mistakes! My old thinking sat between simple and naïve—illustrated by the red dot. But…at least I wasn’t in the middle of complex and naïve!
Applying My Old Thinking vs. My Current Thinking To A Stock Portfolio:
Continue reading this post for free, courtesy of TradeQuantiX.
Claim my free post
Or purchase a paid subscription.
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
