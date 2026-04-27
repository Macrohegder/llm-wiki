---
title: "Real Effective Exchange Rate (REER): Formula, Calculation, and More"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/real-effective-exchange-rate/"
date: "2022-10-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Real Effective Exchange Rate (REER): Formula, Calculation, and More

**来源**: [QuantInsti](https://blog.quantinsti.com/real-effective-exchange-rate/)  
**日期**: 2022-10-13  
**作者**: QuantInsti

---

## 原文

Real Effective Exchange Rate (REER): Formula, Calculation, and More

ByChainika Thakar

Real effective exchange rate is a useful tool for calculating the strength of your nation’s currency against the currencies of other countries. When REER increases, it indicates a loss in trade competitiveness.

Hence, this calculation of the real effective exchange rate helps you decide which currency to trade by considering the factors in favour of the trade including trade competitiveness.

REER is an important measure that is considered during policy-making and when scrutinising the economic growth of a country. Institutions like the IMF, World Bank, BIS and others provide REER analysis of 133 countries.

Let us find out some more interesting facts and uses of Real Effective Exchange Rate (REER) with this blog that covers:

A brief introduction to real effective exchange rate

Formula for REER

Calculation of REER with example

REER vs Real exchange rate

REER vs Spot exchange rate

Types of exchange rates

Working of REER

FAQsWhat does REER below 100 mean?What does a higher REER mean?Is REER adjusted to inflation?

What does REER below 100 mean?

What does a higher REER mean?

Is REER adjusted to inflation?

A brief introduction to real effective exchange rate

Real effective exchange rate (REER)  is the weighted average of a country's currency in relation to a basket of other currencies. This exchange rate is mostly used to determine an individual country's currency value relative to other major currencies.

REER is adjusted for the effects of inflation for every currency in the basket, enabling it to be a measure of what can actually be purchased by a currency.

REER is used to understand how well a currency is doing with respect to other currencies and also with respect to itself in the past. It is an importantquantitative toolthat a trader should be cognizant of.

Real effective exchange rates are useful in measuring whether a currency has appreciated relative to its trading partners. The real effective exchange rate is volatile over the short term and is not a goodindicatorfor intraday trading, but it can be used in anFX trading strategywith a longer-term perspective.

Formula for REER

Coming back to REER calculation, a country's REER can be calculated by taking the average of the bilateral real exchange rates (RER) between itself and its trading partners and then weighing it by using the trade allocation of each partner and then adjusting it for the inflation.

This might sound a bit complicated for a beginner, but it will be simplified further as we will discuss the calculation of REER with an example.

So first, let us see the formula for calculating the real effective exchange rate (REER), which is given by the RBI as:

where,

n = the number of countries in the basket

i = the ‘i’th currency in the basket

e is the exchange rate of the Indian rupee against the IMF’s Special Drawing Rights (SDRs) in indexed form

ei is the exchange rate of foreign currency ‘i’ against the IMF’s Special Drawing Rights (SDRs) in indexed form

wi is the weight attached to the foreign currency ‘i’

Pi is the consumer price index of the country associated with the foreign currency ‘i’

P is India’s consumer price index (CPI) (India uses the CPI to adjust REER)

Calculation of REER with example

For calculating the REER of each of the 6 countries, we need to find the following:

Weights of each of the 6 countries

Exchange rate of each country

Inflation rate of all 6 countries

Weights of each of the 6 countries

We will calculate the “weights” by getting the trade volume data for the six basket countries.

India's largest trade partners with their total trade (sum of imports and exports) in billions of US dollars for the financial year 2021–22 are as follows:

Country

Exports

Imports

Total trade

United States

119.42

115.41

United Arab Emirates

Saudi Arabia

Switzerland

Germany

The total trade with the six countries = (119.42)+(115.41)+(72.90)+(42.00)+(18.11)+(21.9) = $389.74bn. Trade weights for the six countries using the total trade parameter are calculated as follows:

Country

Weight

Weight percentage (%)

United States

119.42/389.74

115.41/389.74

United Arab Emirates

72.90/389.74

Saudi Arabia

42/389.74

Switzerland

18.11/389.74

Germany

21.9/389.74

Exchange Rate of each country

Now let us look at the exchange rates of the six basket currencies with respect to the Indian Rupee. For simplifying the calculation, I have taken the exchange rate of each foreign currency in 10 units per Indian Rupee. For instance, 10 Chinese Yuan = 113.90 INR.

Country

Exchange rate with INR

United States

815.09

113.90

United Arab Emirates

222.05

Saudi Arabia

216.70

Switzerland

823.66

Germany

787.59

We have considered the EURO/INR as the exchange rate for Germany in this case. While calculating the exchange rate value, the agencies consider an average rate for a predefined period of time. This is done to account for the daily volatile fluctuations in the forex markets.

Also, the real effective exchange rate (REER) value is usually released by the IMF, central banks and other international agencies with a lag of approximately 3 months.

Inflation

Let us now look at the inflation data of the 6 basket currencies and India.

Country

Consumer Price Inflation (CPI)

United States

296.171

United Arab Emirates

108.62

Saudi Arabia

107.61

Switzerland

104.77

Germany

Now, we will calculate the REER for China by following these steps:

The exchange rate component= e/e1 = 1/113.90 = 0.00877

The inflation component = P/P1 = 174.3/103.1 (India/China’s CPI) = 1.690

The product of exchange rate component and inflation component = 0.00877*1.690 ([(e/e1)* (P/P1)]^w1) = 0.0148

The final REER component = [(e/e1) *(P/P1)]^w1= (0.0148)^0.296= 0.31875

Similarly, we can perform this calculation for the rest of the basket countries and for India. Also, you can calculate the REER with respect to the other countries.

For instance, by taking the product of the real effective exchange rate (REER) components of all the other countries, we get the total REER for India with respect to the basket of six countries.

Also, if you find the REER of India/your own country has increased in comparison with another country, it implies that the exports to the particular country have become expensive while the imports have become cheaper. Hence, it implies that the trade competitiveness is not much now.

Similarly, when REER of a India/your own country has decreased in comparison with another country, it implies that the exports from that country have become cheaper and the imports have become expensive which also implies that the trade competitiveness has increased with that country.

REER vs Real exchange rate

Let us now see the difference between REER and Real exchange rate.

Real exchange rate

REER is the measure or tool that compares the nation’s currency value against the weighted average of the currencies of its major trading partners.

The real exchange rate measures the value of a country’s goods against goods of another country, a group of countries, or the rest of the world at the prevailing nominal exchange rate.

The formula of the real effective exchange rate is:

REER = i=1n [(e/ei) (P/Pi)]wi

Where,

n is the number of countries in the basket

i is the ‘i’th currency in the basket

e is the exchange rate of the Indian rupee against the IMF’s Special Drawing Rights (SDRs) in indexed form

ei is the exchange rate of foreign currency ‘i’ against the IMF’s Special Drawing Rights (SDRs) in indexed form

wi is the weight attached to the foreign currency ‘i’

Pi is the consumer price index of the country associated with the foreign currency ‘i’

P is India’s consumer price index (CPI), India use the CPI to adjust REER

The formula of the real exchange rate is:

e x P / P*

Where,

e = foreign currency per unit of domestic currency i.e., nominal exchange rate

P/P* = Domestic price / Foreign price (in terms of foreign currency)

REER vs spot exchange rate

A spot exchange rate is the current price to exchange one currency for another for delivery on the earliest possible value date (Date for a financial transaction involving an asset with price fluctuations).

Although the spot exchange rate is for delivery on the earliest date, the standard settlement date for most spot transactions is two business days after the transaction date.

The spot exchange rate is a current market price, whereas REER is an indicator of the value of a currency in relation to its trading partners.

Types of exchange rates

There are four main types of exchange rates that one can use. These four exchange rates are:

Fixed exchange rate

Floating exchange rate

Pegged float

Dollarization

Let us see the relevance of each one by one.

Fixed exchange Rate

The rates that are directly convertible towards other currencies are called fixed rates. In case of fixed exchange rate, the central bank of a particular country makes the country’s official exchange rate pegged (tied) to another country’s currency or gold.

This way, the fixed exchange rate system keeps the currency’s value within a narrowcurrency band. For example, the Danish krone (DKK) is pegged to the euro at a central rate of 746.038 kroner per 100 euro.

Floating exchange Rate

The most common regime today that is adopted in most countries is floating exchange rates. The most common examples are the yen, dollar, Euro, and British pound which fall under this category.

With the floating exchange rate, the central banks of the respective countries intervene frequently in order to avoid depreciation or appreciation.

Pegged float

These currencies under a pegged float are pegged against a particular value or currency bands. The pegged floats are adjusted either periodically or are fixed.

Pegged floats are also considered crawling bands. The crawling band is the rate at which it is allowable to fluctuate around a central value in a band. Also, pegged floats are adjusted periodically. The adjustment is done in either a controlled way or at a preannounced rate.

For example, Hong Kong allows the free flow of capital and pegs the exchange rate to the U.S. dollar.

Dollarization

Dollarization is a term generally used when a particular non-U.S country uses U.S dollars as their national currency. For example, Zimbabwe introduceddollarization in 2009for reducing hyperinflation. However, the central bank of Zimbabwe hasruled out a return to dollarizationrecently.

Working of REER

In the working of a real effective exchange rate, the relative trade balance of a country's currency is compared against each of the existing countries in the index for calculating the weights.

The exchange rate determines the specific currency's value compared to other major currencies in the index.

The REER indicates the equilibrium value of the currency. It measures the country’s trade capabilities and export-import condition.

Since REER indicates the price a consumer pays for buying a product that is not national, or in other words, is imported, it includes the tariffs and other transaction costs involved in importing the product.

The REER of a country’s currency can be calculated by weighing the average of the bilateral exchange rates between the country and its trade partners using the trade allocation of each.

Calculating REER based on the consumer price index or on unit labour cost is the most common practice. The IMF computes the REER based on consumer price index for almost all the countries and unit labour cost based REER is used for most of the industrial nations.

It detects the underlying factors of the trade flow and takes into consideration the changes in the international price.

There are some frequently asked questions around real effective exchange rate and here we answer some of them.

What does REER below 100 mean?

A REER reading below 100 keeps exports competitive and imports expensive.

What does a higher REER mean?

A higher REER means imports are cheaper and exports are expensive.

Is REER adjusted to inflation?

Yes. REER is adjusted to inflation while calculating the REER.

Conclusion

Real effective exchange rate is mostly used to determine an individual country's currency value relative to other major currencies. Hence, REER is used to understand how well a currency is doing with respect to other currencies and also with respect to itself in the past.

This is the reason quantitative analysts use REER to determine the strength of the currency before trading or investing in one.

If you wish to explore more about the exchange rates and how to gain an edge in the markets, you may enroll in this learning track forautomated trading in forex.

You will gain knowledge about forex valuation methods such as purchasing power parity, nominal effective exchange rate and real effective exchange rate and learn to automate forex trading on Interactive Brokers and FXCM using Python. Moreover, you can create your own set up for trading or use cloud-based trading solutions after completing this learning track. Do check it out.

Note: The original post has been revamped on 13th October 2023 for accuracy, and recentness.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
