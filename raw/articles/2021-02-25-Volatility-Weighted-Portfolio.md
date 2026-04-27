---
title: "Volatility Weighted Portfolio"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/volatility-weighted-portfolio/"
date: "2021-02-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Volatility Weighted Portfolio

**来源**: [QuantInsti](https://blog.quantinsti.com/volatility-weighted-portfolio/)  
**日期**: 2021-02-25  
**作者**: QuantInsti

---

## 原文

Volatility Weighted Portfolio

ByMario Pisa

One can determine the position size using multiple methods. In this blog, we focus on and explain the Volatility Weighted Portfolio. The Volatility Weighted Portfolio ensures that all the components of the portfolio contribute equally to the risk/reward ratio.

Topics covered:

Notional exposure

Leverage portfolio allocation

Stock portfolio allocation

Conclusion

The position size matters while trading. An educated and efficient trader should be concerned about the position size in her/his portfolio because it is the way she/he can control the estimated risk she/he is taking.

Regardless of the strategy we are using to enter or exit the market and the financial instruments we are using, it is necessary to control the notional exposure to which we are exposed in the market as this is what determines the risk we are assuming.

There are multiple methods to determine theposition sizeand here we will focus on a Volatility Weighted Portfolio to try to ensure that all components of the portfolio contribute in the same proportion to the risk/reward ratio.

Basically the method consists of scaling the exposure according to the volatility required in the portfolio and the volatility offered by the instrument and/or strategy.

Notional exposure

The notional exposure is very easy to understand for stocks in a cash type broker account.

If the price of a stock is 100 USD and we want to buy 100 shares, we need to have 10,000 USD in the broker's account.

Let's assume a margin account where we are allowed to leverage 4:1.

This means that to buy 100 shares of a stock priced at 100 USD, we will need only 2,500 USD assuming a risk four times greater than in the cash account if we are fully exposed. Or, with a 10,000 USD account we could buy 100 shares with 1:1 leverage, 200 shares with 2:1 leverage and so on up to 4:1.

In the case of margin products the leverage can be much higher and consequently multiply the portfolio risk.

Taking as an example the March Mini S&P 500 futures contract ESH21 has a price of 3,935.00 USD and a multiplier of 50, which means that one contract has a notional exposure in the market of 196,750 USD which means that we should have an account with at least 200,000 USD to be able to manage a reasonable leverage.

For forex, brokers in general offer insane leverage, although this does not mean that we should take on as much risk exposure as possible just because the broker allows it.

In any of the above cases the key is how to manage the notional exposure to the market.

Therefore, the idea is to know a method to distribute the capital among the different instruments that constitute the portfolio.

Leverage portfolio allocation

Leveraged financial products allow taking positions in the market that substantially exceed the actual capital available in the broker's account. This is because only a small margin is required with respect to the notional exposure.

The usual margin ranges from 5% to 20%, although this is variable depending on the volatility of the market and/or the volatility of the instrument itself.

Let's create a portfolio of futures and look at the notional exposure for a single contract in each instrument. Explore ourFutures Trading Courseto dive deeper into the concept and gain knowledge on how to trade systematically in the futures market.

ESH21: Emini S&P 500 March’2021HGH21: Copper March’2021GGH21: Euro Bund March’2021GCJ21: Gold April’2021

Notional exposure = Price x Multiplier x Currency

Price 2021-02-21

3,922.25

3,8105

174.79

1,784.7

Multiplier

Currency USD

1,206430

1 contract not. exp.

196,112.50

95,262.50

210,871.90

178,470.00

Note:I’m including the currency of the instrument, since in this case the German bund is quoted in euros and our portfolio is denominated in USD. So, we have to convert the notional exposure to the currency of our portfolio.

Total notional exposure: 680,716.90

Adding the total notional exposure, we obtain $680,716.90 by buying a single contract of each instrument and the gain or loss will go against the notional exposure.

To obtain a leverage of 1:1 we need to capitalize the account with $700,000 to buy one contract of each of these instruments, the problem is that the contribution to the risk/reward of the portfolio is very skewed, leaving the portfolio very exposed to the more volatile instruments and a very small impact for the less volatile instruments.

To balance the contribution of each instrument to the volatility of the whole portfolio we will take the volatility measured by the ATR of each instrument to obtain the number of contracts we need.

The following formula proposed by Perry Kauffman in the book Trading Systems and Methods simply divides the capital by the ATR to obtain the number of contracts, the higher the volatility the lower the position and vice versa.

Position size = (Allocation / currency) / (ATR * multiplier)

700,000

175,000

3,922.25

3.8105

174,79

1,784.7

ATR(20)

0.0665

Multiplier

Currency

1,206430

1 contract not. exp.

196,112.5

95,262.5

210.871,8997

178,470

Contracts

Notional exposure

13,139,537.50

10,002,562.50

40.900.860,00

11,243,610.00

Total notional exposure: 75,286,570.00

The result of the formula proposes to buy/sell a very high number of contracts which would give us a notional exposure of $75,286,570.00 and would give us a deadly leverage of $75,286,570.00:$700,000.00 or 107:1 to burn your account and put you out of the game in one strike.

Therefore, we will scale the positions to find reasonable leverages of 2:1, 3:1 or 4:1.

The main key is to find the ratio to scale the notional exposure, which is obtained by dividing the total capital by the sum of the total notional exposure.

700000

175.000

3,922.25

3.8105

174.79

1,784.7

ATR(20)

0.0665

Multiplier

Currency

1.206430

1 contract not. exp.

196,112.5

95,262.5

210,871.8997

178,470

Contracts

Notional exposure

13,139,537.50

10,002,562.50

40,900,860.00

11,243,610.00

Ratio to scale

0.009298

Exposure scaled

122,168.88

93,001.90

380,288.30

104,540.92

Leverage 1:1

Leverage 2:1

Leverage 3:1

Leverage 4:1

Note how for the more volatile instruments they obtain a lower number of contracts with respect to the less volatile instruments that have a higher number of contracts.

It is interesting to note that for 1:1 leverage we could only buy German bonds without leverage. I have left the decimals only to see that we could only buy a portion of the contract. Which is not really possible.

Another key aspect is that we need a leverage of at least 2:1 to have open positions in all instruments. In this case 1 contract for the S&P 500 and Gold, 2 contracts for Copper and 4 contracts for German Bunds.

Stock portfolio allocation

For a cash account where leverage is not possible we can balance the portfolio by volatility in the same way.

Assume the following ETFs:

SPY: S&P 500 SPDR ETFGLTR: Physical Precious Metals Basket ETFTLT: 20+ Year Treas Bond Ishares ETFGSG: S&P GSCI Commodity-Indexed Ishares ETF (GSG)

Position size = (Allocation / currency) / (ATR * multiplier)

In the case of stocks the multiplier is 1.

400.000

100.000

144.87

ATR(20)

Multiplier

Currency

Shares

526316

Notional exposure

9,340,663.00

6,146,189.01

11,778,075.87

7,405,266.12

Ratio to scale

0.0115

Exposure scaled

107,765.92

70,910.35

135,887.05

85,436.69

Shares

274.70

730.21

937,99

6,072.26

In this way we can determine the number of shares for each instrument taking into account the current volatility of each instrument. If we add up the total exposure we obtain the maximum available capital.

Total allocation: 400,000.00

Explore options trading volatility in a brief video after learning about Volatility Weighted Portfolio—gain insights on gaining an edge, risk management, volatility estimation, and practical application.

Conclusion

Here we have only seen one of the many methods that exist to balance the portfolio based on volatility. It is a useful tool so that the risk/reward ratio of the portfolio is not out of balance for the more volatile instruments.One can learn about constructing portfolios and managing risks using various quantitative techniques in this course onQuantitative Portfolio Management.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
