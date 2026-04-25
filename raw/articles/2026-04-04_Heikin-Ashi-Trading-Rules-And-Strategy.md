# Heikin Ashi Trading Rules And Strategy

**原文链接**: https://quantifiedstrategies.substack.com/p/heikin-ashi-trading-rules-and-strategy

**发布时间**: Mar 25, 2026

**抓取时间**: 2026-04-04 22:09:16

---

## 摘要

Heikin Ashi Trading Rules And Strategy
QuantifiedStrategies.com
Mar 25, 2026
7
3
1
Share
Today, we present Heikin Ashi trading rules and strategy. It was first publsihed on our website years ago.
What Is Heikin Ashi?
Heikin Ashi is a Japanese candlestick charting technique designed to filter out market noise and highlight trend direction more clearly than traditional Japanese candlesticks.
The name itself translates to “average bar,” which reflects how it functions: rather than showing raw price data, it uses a mathematical formula to create “artificial” values for the open, high, low, and close of each candle.
Because Heikin Ashi candles are calculated based on averages (for example, the open of a candle is the midpoint of the previous candle’s body), the resulting chart appears much smoo...

---

## 全文

Heikin Ashi Trading Rules And Strategy
QuantifiedStrategies.com
Mar 25, 2026
7
3
1
Share
Today, we present Heikin Ashi trading rules and strategy. It was first publsihed on our website years ago.
What Is Heikin Ashi?
Heikin Ashi is a Japanese candlestick charting technique designed to filter out market noise and highlight trend direction more clearly than traditional Japanese candlesticks.
The name itself translates to “average bar,” which reflects how it functions: rather than showing raw price data, it uses a mathematical formula to create “artificial” values for the open, high, low, and close of each candle.
Because Heikin Ashi candles are calculated based on averages (for example, the open of a candle is the midpoint of the previous candle’s body), the resulting chart appears much smoother.
How Heikin Ashi is Calculated (formula)
Heikin Ashi is calculated using this formula:
heikin ashi close = (O+H+L+C)/4;
heikin ashi open = (previous bar’s heikin ashi open + previous bar’s heikin ashi close) / 2;
heikin ashi high = highest value among the current bar’s high, heikin ashi open, and heikin ashi close;
heikin ashi low = lowest value among the current bar’s low, heikin ashi open, and heikin ashi close;
Heikin Ashi chart for the S&P 500
This helps traders identify sustained trends and consolidation phases with greater precision, as the candles tend to remain the same color for longer periods than on standard charts.
However, it is important to note that Heikin Ashi does not show real prices, meaning you cannot execute trades directly at the prices shown on the indicator.
Backtest: Heikin Ashi Trend-Following Strategy
To evaluate the effectiveness of this indicator, a rules-based trend-following strategy was backtested on the S&P 500 index from 1960 to the present, using a monthly time frame.
The Trading Rules:
Buy:
When the Heikin Ashi candle turns from red to green (specifically, when the
haClose
crosses above the
haOpen
).
Sell:
When the Heikin Ashi candle turns from green to red (the
haOpen
crosses below the
haClose
).
The code for Amibroker looks like this:
HAC = (O + H + L + C)/4;
HAO = AMA( Ref( HAC, -1 ), 0.5 );

Buy = HAC>HAO;
BuyPrice=Close;
Sell = HAC<HAO;
SellPrice = Close;
The Results
The backtest revealed that the strategy functions as a classic trend-following system with the following performance metrics:
Heikin Ashi Trading Rules And Strategy
Annual Return:
5.2% (compared to 7.5% for a buy-and-hold strategy).
Risk-Adjusted Return:
7.3%.
Maximum Drawdown:
29%, significantly lower than the 52.56% drawdown experienced by buy-and-hold investors.
Win Ratio:
52%
, which is typical for trend-following systems that rely on capturing large moves rather than frequent small wins.
Time in Market:
The strategy kept investors in the market 67% of the time.
Key Takeaways
The sources suggest that while Heikin Ashi is a lagging indicator, it is highly effective at visualizing price trends for analysts and discretionary traders.
The backtest demonstrates that while it may offer a lower absolute return than simply holding the index, it provides a much smoother ride with significantly reduced drawdowns.
We conclude that Heikin Ashi trading rules and strategy work best on longer time frames and might be a valuable supplement to other technical indicators.
7
3
1
Share
Previous
Next

---

*由 Substack Strategy Tracker 自动抓取*
