# Do Stop-Loss Rules Add Value in Tactical Asset Allocation?

**原文链接**: https://www.quantseeker.com/p/do-stop-loss-rules-add-value-in-tactical

**发布时间**: Oct 26, 2025

**抓取时间**: 2026-04-19 22:26:41

---

## 摘要

Do Stop-Loss Rules Add Value in Tactical Asset Allocation?
Testing Whether Stop-Loss Overlays Improve Performance in a Systematic TAA Framework
QuantSeeker
Oct 26, 2025
∙ Paid
3
2
Share
Hello
,
Stop-loss rules are among the most debated tools in systematic investing. While many investors associate them with retail trading or emotion-driven decisions, academic research and institutional experience suggest a more nuanced picture. Studies by
Kaminski and Lo (2014)
and
Lo and Remorov (2017)
show that stop-losses can enhance performance when assets exhibit strong momentum and positive serial correlation but tend to hurt performance in mean-reverting environments.
My earlier article,
The Value of Stop-Loss Strategies
, summarizes and discusses the academic evidence on stop losses, emphasizing th...

---

## 全文

Do Stop-Loss Rules Add Value in Tactical Asset Allocation?
Testing Whether Stop-Loss Overlays Improve Performance in a Systematic TAA Framework
QuantSeeker
Oct 26, 2025
∙ Paid
3
2
Share
Hello
,
Stop-loss rules are among the most debated tools in systematic investing. While many investors associate them with retail trading or emotion-driven decisions, academic research and institutional experience suggest a more nuanced picture. Studies by
Kaminski and Lo (2014)
and
Lo and Remorov (2017)
show that stop-losses can enhance performance when assets exhibit strong momentum and positive serial correlation but tend to hurt performance in mean-reverting environments.
My earlier article,
The Value of Stop-Loss Strategies
, summarizes and discusses the academic evidence on stop losses, emphasizing that while stops can add alpha in specific contexts, their broader value lies in reducing drawdowns, improving return skewness, and mitigating the behavioral biases that often lead investors to abandon strategies during deep losses.
Research Affiliates recently revisited the
topic
, noting that even well-designed quantitative strategies can experience sharp interim losses that test investor discipline. They argue that stop-loss rules can serve as a straightforward way to manage risk and improve the return path, particularly useful for systematic and factor-based portfolios.
Building on these insights, today’s analysis examines whether integrating stop-loss rules can enhance performance in a Tactical Asset Allocation (TAA) framework, using the previously discussed model as a case study. Specifically, I test how different stop thresholds, defined as multiples of an asset’s past volatility, affect performance and drawdowns.
As a straightforward illustration, I apply stop-loss rules to SPXL, the leveraged equity component of the strategy, using stop levels ranging from 0.1× to 1× annualized volatility.
The baseline model achieves a 27% CAGR, a Sharpe ratio of about 1.3, a 20% maximum drawdown, and positive skewness. Introducing stop-loss rules of 0.2× and 0.3× reduces drawdowns to approximately 15% and further improves skewness, while maintaining a similar Sharpe ratio and only modestly reducing the CAGR, as overall portfolio volatility declines.
Detailed discussion and full results follow below.
Continue reading this post for free, courtesy of QuantSeeker.
Claim my free post
Or purchase a paid subscription.

---

*由 Substack Strategy Tracker 自动抓取*
