# Portfolio 5# The Five Pillar Portfolio

**原文链接**: https://algomatictrading.substack.com/p/portfolio-5-the-five-pillar-portfolio

**发布时间**: 2026-04-05

**抓取时间**: 2026-04-05 16:22:09

---

## 摘要

Portfolio 5# The Five Pillar Portfolio
Building a Robust Multi-Strategy Portfolio: A Collaboration with The Rogue Quant
Algomatic Trading
Jan 18, 2026
∙ Paid
20
4
Share
By now you know that I strongly advocate trading with strategy portfolios. A bundle of truly uncorrelated strategies is, in my view, one of the simplest and most robust ways to become a consistently profitable systematic trader.
This portfolio series, which I’ve been building over the past months, is meant to inspire you to take the first steps toward creating your own personal strategy portfolio. The portfolios I share are not “the” solution, but examples of how different ideas from my library can be combined into something more powerful than any single system on its own.
The number of possible combinations is enormous, an...

---

## 全文

Portfolio 5# The Five Pillar Portfolio
Building a Robust Multi-Strategy Portfolio: A Collaboration with The Rogue Quant
Algomatic Trading
Jan 18, 2026
∙ Paid
20
4
Share
By now you know that I strongly advocate trading with strategy portfolios. A bundle of truly uncorrelated strategies is, in my view, one of the simplest and most robust ways to become a consistently profitable systematic trader.
This portfolio series, which I’ve been building over the past months, is meant to inspire you to take the first steps toward creating your own personal strategy portfolio. The portfolios I share are not “the” solution, but examples of how different ideas from my library can be combined into something more powerful than any single system on its own.
The number of possible combinations is enormous, and there is no universally “best” portfolio. The optimal mix depends on your capital, risk tolerance, time horizon, and psychological comfort.
What I want to show you is not
the
perfect portfolio but
how to think
in terms of portfolios. This portfolio represents a collaboration between me
(Algomatic Trading)
and
The Rogue Quant
, bringing together complementary strategies that work in different market conditions.
Portfolio Philosophy
The core principle behind this portfolio is diversification, not just across markets, but across strategy types and timeframes. By combining mean reversion strategies that profit from overextended moves with trend-following systems that capture momentum, we create a portfolio that can perform across varying market regimes.
Each strategy included here has been backtested and demonstrates robust performance characteristics. More importantly, they have low correlation with each other, which is the key to portfolio construction that actually reduces drawdowns.
The Five Strategies
Strategy 1: Mean Reversion Using Linear Regression (FREE)
Market:
US500 (ES), Nasdaq100 (NQ)
Type:
Mean Reversion
Timeframe:
Daily
This is the free mean reversion strategy available to all my readers. It identifies overextended moves in major equity indices and enters when conditions suggest a snap-back is likely. The strategy uses Linear Regression and RSI-based signals combined with volatility filters to time entries when markets are oversold.
Key characteristics:
Win rate around 65-70%
Average holding period of 2-4 days
Works best in trending bull markets with periodic pullbacks
Full strategy details available here
Strategy 2: Larry Connors Refined (Coming Soon for Premium)
Market:
SPY, QQQ (can be adapted to futures and other indices)
Type:
Mean Reversion
Timeframe:
Daily
My enhanced take on Larry Connors’ legendary mean reversion approach. While Connors’ original strategies are well-known, this version incorporates modern filters, improved exit logic, and position sizing techniques that significantly improve the risk-adjusted returns, it’s also extremely simple which I like.
The improvements focus on:
Better entry timing
Dynamic position sizing based on volatility
Smarter exit rules that capture more of the bounce
This strategy will be released to premium Substack members in the coming weeks.
Preview post available here
Strategy 3: The Easiest Trend System (Premium)
Market:
Multiple futures markets
Type:
Trend Following
Timeframe:
Daily
Sometimes the simplest systems are the most robust. This trend-following strategy uses straightforward logic that any trader can understand and implement, yet it’s proven effective across decades of data. The beauty of this system is in its simplicity, no complex indicators, no curve-fitting, just clean trend identification and execution.
Key characteristics:
Low win rate (~40-50%) but strong risk-reward
Captures the big moves while managing whipsaws
Works across commodities, indices, and currencies
Full strategy in the premium database
Strategy 4: Turnaround Tuesday System (Premium)
Market:
Stock indices
Type:
Tactical/Swing
Timeframe:
1 Hour (Also uses multi-timeframe daily data)
This strategy takes advantage of weekly market patterns and structural tendencies that have persisted for years. It’s “boring” in the sense that it doesn’t generate frequent signals, but when it does signal, the edge is real and measurable.
The timeframe also means less monitoring and fewer execution headaches, perfect for traders who want systematic exposure without constant surveillance.
Key characteristics:
Low frequency
Strong risk-reward ratio
Minimal correlation with daily strategies
Full strategy in the premium database
Strategy 5: CL Composite RSI with Dynamic Sizing (The Rogue Quant × Algomatic Trading)
Market:
CL, US Crude Oil (CFDs & Futures)
Type:
Mean Reversion
Timeframe:
Daily
This is a collaboration strategy, originally developed by The Rogue Quant in one of his recent strategy posts, I simply translated it to
ProRealTime
and added dynamic position sizing. It’s a simple but very strong mean reversion approach specifically designed for crude oil which is quite hard to find good strategies on in my opinion.
Performance Characteristics:
Solid win rate with controlled drawdowns
Performs well in choppy, range-bound oil markets
The ProRealTime Code:
The full ProRealTime implementation is included at the end of this post.
Key features include:
Clean, readable PRT code structure
Dynamic position sizing integrated directly
Proper order management (no pyramiding)
This strategy represents the power of collaboration in the trading space, The Rogue Quant’s original idea but slightly customized for me. This also shows that simple strategies easily can be translated with LLMs (Like ChatGPT or Claude) which is exactly what I used to translate this strategy.
If you want to read more about this strategy check out this post for details about the backtest and full code (easylanguage & plain english)⬇️
The Rogue Quant
The Simple Crude Oil Strategy That Doesn’t Care About Venezuela
Yesterday (and all week), the timeline was doing what the timeline does…
Read more
3 months ago · 22 likes · 2 comments · The Rogue Quant
Backtested Portfolio Metrics
While individual strategy performance varies, the portfolio as a whole has this historical performance:
Annual Return:
11.7%
Maximum Drawdown:
-15.59%
MAR Ratio:
0.75
Win Rate:
~65%
These are realistic expectations for a systematic portfolio. We’re not promising 100% annual returns with 5% drawdowns, this is about consistent, reliable performance that overperforms the benchmark/comparable index and compounds over time.
Risk Management Across the Portfolio
Each strategy includes its own risk parameters, but portfolio-level risk management is equally important:
Position Sizing:
Each strategy uses dynamic sizing based on volatility
MAX Drawdown Risk Parity:
Each strategy gets sized so its maximum historical drawdown equals a set amount of money.
Example:
Portfolio Max DD:
-€6,074
Sum of Individual Max DDs:
-€23,685
Diversification Factor:
6074 / 23685 = 0.26
This means you’re getting
74% drawdown reduction
from diversification in this portolio, pretty damn good.
Getting Started
If you’re interested in implementing this portfolio:
For Free Strategy Access:
Strategy 1 is completely free and available to all readers
For Premium Access:
Strategies 3 and 4 are available now in the premium strategy database
Strategy 2 will be released to premium Substack members soon
Premium membership includes the full strategy library, code, and ongoing updates
For Strategy 5:
The ProRealTime code is available below for premium subscribers
Credit goes to The Rogue Quant for the original concept
Dynamic sizing and PRT translation by Algomatic Trading
Collaboration and Community
This portfolio post represents the power of the systematic trading community. The Rogue Quant’s CL strategy is a perfect example of how sharing ideas and building on each other’s work creates better trading systems. I’m grateful for the collaboration and excited to see how traders implement and adapt these strategies.
If you’re running any of these strategies or have questions about implementation, drop a comment below or reach out directly. I’m always interested in hearing how these strategies perform in real-world trading and what adaptations traders make for their own situations.
Final Thoughts
Building a portfolio is different from finding a single “best” strategy. It’s about combining complementary approaches that work together to smooth returns and reduce drawdowns. These five strategies represent different market conditions, different timeframes, and different risk profiles but together, they create something more robust than any single approach.
Systematic trading isn’t about perfection. It’s about having a plan, following it consistently, and letting probability work in your favor over time.
Special thanks to The Rogue Quant for the collaboration on the CL strategy. Follow his work for more sophisticated systematic approaches.
For questions about strategy implementation, position sizing, or portfolio construction, feel free to reach out through the comments or subscribe for premium access to the full strategy database.
Strategy 5: CL Composite translated to ProRealTime Code
The complete ProRealTime code of The Rogue Quant’s CL strategy with dynamic position sizing is available for paid subscribers below.
This post is for paid subscribers
Subscribe
Already a paid subscriber?
Sign in

---

*由 Substack Strategy Tracker 自动抓取*
