# Portfolio Development Series - Part 6

**Source**: [[2026-04-25-Portfolio-Development-Series---Part-6]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-5fd)
**Date**: 2026-04-25
**Tags**: #article #substack

## One-Sentence Summary

> Premium Content Vault
Portfolio Development Series - Part 6
Developing a TSX Long-Side Momentum System
TradeQuantiX
Sep 01, 2025
∙ Paid
8
6
Share
Welcome to the “Systematic Trading with TradeQuantiX” ...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-5fd)

## Full Content

Premium Content Vault
Portfolio Development Series - Part 6
Developing a TSX Long-Side Momentum System
TradeQuantiX
Sep 01, 2025
∙ Paid
8
6
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
Welcome to the part 6 article of the Portfolio Development series. In this article we are going to head up north to the Canadian market. Thus far, we've developed a couple of systems on the US market, a system on the ASX market, and now we are going to add the TSX market.
Having diversification across multiple world equity markets can provide massive benefits to a systematic trading portfolio. Think about it, different economies perform better during different times. The US market may be going sideways, the Australian market may be in decline, and the Canadian market may be growing. You never know what the economic situation will be, and so having exposure to multiple different economic environments can be extremely powerful.
On the Canadian market, I'm going to develop a momentum trading system. To be honest, I'm pretty nervous about developing this system. I have attempted to develop momentum systems on the Canadian markets a couple of times in the past, and every attempt has failed out-of-sample or robustness testing.
I'm actually starting to write this article before I even develop the system. That way I fall into the sunk cost fallacy and work really hard to develop a system that actually passes out-of-sample testing and is robust. So wish me luck.
In this article, I'm going to focus on parameter optimization during the in-sample development phase. I'll share the final system results, but the majority of the article will focus on robust optimization practices and setting yourself up for success in out-of-sample.
The worst feeling is when you spend hours developing using in-sample data just to check out-of-sample and the system completely falls apart. It's demoralizing and feels like you've wasted an entire day, and then the rest of your day you just feel defeated.
This is why I want to focus on robust parameter optimization techniques so that you set yourself up for success for the out-of-sample test. There's no guarantee, obviously, that the out-of-sample will pass, but it will give you a better probability of passing when you implement these techniques, as opposed to not.
Systematic Trading with TradeQuantiX is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe
Common Optimization Pitfalls:
It's very common for systematic traders to throw a bunch of indicators on a chart, they then say:
“That looks good, all it needs is some optimization!”
Then they run a brute force exhaustive optimization on a million parameter combinations and pick the very best result. This is a faulty practice and is nearly guaranteed to fail in out-of-sample.
A better practice than picking the best parameter is to pick the most stable parameter. This is why I think optimization confuses people. The word "optimizing" is the wrong word. It should be called stability searching, or something of that nature.
Generally we need to find a parameter with a stable performance surface, meaning all parameters surrounding the chosen parameter have similar performance. This allows for the markets to shift a little bit and the system still work into the future.
Now, it’s not always this easy. Sometimes parameter optimization surfaces are bumpy, sloped, and noisy. There is a lot of nuance that goes into how I pick parameters during these scenarios. Those examples will be outlined in this article.
Picking the best parameter (the performance peak) allows no wiggle room for future market shifts, and thus is more likely to fall apart in the future. Performance peaks generally are not real, instead, they are noise within the data.
The reason why systematic traders are prone to pick performance peaks and overfit rather than create robust systems is because robust systems aren't as pretty. Overfitting results in beautiful backtests. It's very easy to fall in love with how your backtest looks. But a backtest is just that, there's no guarantee of future performance, and the more fragile and overfit your backtest is, the less likely you are to have any positive performance in the future.
Instead, this is why we need to focus on robust backtests, which are uglier backtests, but they're real. These backtests are much more likely to have continued positive performance into the future. Ask yourself, would you rather:
Trade a system with a lumpy and bumpy equity curve with drawdowns and periods of underperformance that is robust and continues to make money over the lon

---

*Imported from Substack on 2026-04-25*
