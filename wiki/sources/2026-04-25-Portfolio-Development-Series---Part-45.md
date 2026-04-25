# Portfolio Development Series - Part 4.5

**Source**: [[2026-04-25-Portfolio-Development-Series---Part-4.5]] | [TradeQuantiX](https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-28e)
**Date**: 2026-04-25
**Tags**: #article #substack

## One-Sentence Summary

> Premium Content Vault
Portfolio Development Series - Part 4.5
Survivorship Bias! We Need To Fix It!
TradeQuantiX
Aug 19, 2025
∙ Paid
9
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” new...

## Key Insights

1. **原文来源**: [TradeQuantiX](https://www.tradequantixnewsletter.com/p/portfolio-development-series-part-28e)

## Full Content

Premium Content Vault
Portfolio Development Series - Part 4.5
Survivorship Bias! We Need To Fix It!
TradeQuantiX
Aug 19, 2025
∙ Paid
9
4
Share
Welcome to the “Systematic Trading with TradeQuantiX” newsletter, your go-to resource for all things systematic trading. This publication will equip you with a complete toolkit to support your systematic trading journey, sent straight to your inbox. Remember, it’s more than just another newsletter; it’s everything you need to be a successful systematic trader.
Introduction:
This is an article I was not expecting to write as part of this series; hence it being called part 4.5. I made a mistake in the previous part 4 article of this Portfolio Development series.
After I posted the previous article about creating a US momentum trading system, a subscriber was kind enough to point out to me a very subtle survivorship bias within the system. Now, don’t freak out, I have fixed the system and it still works just fine, the updated code will be provided at the end of this article.
Since I am in this awkward position, I figured I should make the most of it and use it as an opportunity to discuss mistakes in system development. In this article, I want to:
Discuss the mistake in the system
Discuss why it matters
Discuss how it could have been avoided
It’s important not only as a learning opportunity but to also point out that even someone who has been doing this for years can still make mistakes!
If you missed the previous article, check it out here. There is still a lot of informative content aside from the mistake!
Premium Content Vault
Portfolio Development Series - Part 4
TradeQuantiX
·
August 4, 2025
In this fourth installment of the portfolio development series, I will create a long-side momentum system focused on US mega-cap stocks. In my opinion, this is the bread and butter, the meat and potatoes, of a well-rounded systematic trading portfolio.
Read full story
The Survivorship Bias Mistake:
The coding mistake within the momentum system was within the breadth filter. The current breadth filter logic is as shown below:
BreadthFilterThreshold: 0.5	
BreadthFilter1:	#Sum InOEX
BreadthFilter2:	#Sum C>MA(C, LongTermLookback)
BreadthFilter:	BreadthFilter2 / BreadthFilter1 > BreadthFilterThreshold
In English, this code was meant to:
Sum the number of stocks currently in the S&P 100 index
Sum the number of stocks in the S&P 100 currently above the 200 day moving average
Only take a trade if 50% of stocks in the S&P 100 are above the 200 day moving average
The survivorship bias issue occurs in step 2. I missed a conditional to only sum the number of stocks above the 200 day moving average if they are a constituent of the S&P 100 at that point in time in the backtest. Accurate historical constituency is key.
Instead, this rule was checking for 200 day MA uptrends in all stocks currently in the S&P 100, previously in the S&P 100, and to be added in the future to the S&P 100.
This issue is a mix between what's called survivorship bias and a future leak. The breadth rule was using data in the calculation that would not have been available at that point in time.
This is obviously no good, hence why I need to fix it. This can severely skew results, and survivorship biases and future leaks are generally some of the worst biases in backtesting. Luckily, the impact to the system is minor, but more on that in a bit.
It is why it is extremely important to have an accurate index constituency time series. This makes it so a strategy can know what stocks were in the S&P 100 every single day of the backtest. In this case that is what the
InOEX
function does in the RealTest code.
Survivorship bias and future leaks can wreak havoc on live trading results. A backtest with survivorship bias/future leak may look fantastic, but once you go live your results are slowly going to degrade over time.
This is because during live trading we don't know what the future holds, so the system is only going to be using the current data. But as time goes on, the system will be subtly adjusting it's historical performance as new future information is known. The history of the backtest will be “repainted” as some call it.
You’ll notice that some of your live trades inexplicably change. You may also notice that your live results look a lot worse than the backtested results over the same period. It’s a slow and subtle degradation in between live and backtested performance.
For example, let’s say a handful of new stocks were added to the index in 2021. With a future leak/survivorship bias, the breadth filter calculation is going to include the stocks that were added to the index in 2021 for all years prior to 2021 as well. But before 2021 we would not have known those stocks were going to be added to the index yet. The system was making decisions based on unknown future data.
The equity curve will essentially be constantly changing with every stock that is added to the index. The back test will not be static, it will be

---

*Imported from Substack on 2026-04-25*
