---
title: "Latency War - Why is Low Latency Important?"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/latency-war-why-is-low-latency-important/"
date: "2015-08-21"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Latency War - Why is Low Latency Important?

**来源**: [QuantInsti](https://blog.quantinsti.com/latency-war-why-is-low-latency-important/)  
**日期**: 2015-08-21  
**作者**: QuantInsti

---

## 原文

Latency War - Why is Low Latency Important?

It’s the latency stupid! David Cheriton once said that if you have a network link with low bandwidth then it's an easy matter of putting several in parallel to make a combined link with higher bandwidth, but if you have a network link with bad latency then no amount of money can turn any number of them into a link with good latency.

Let us have a look at an example to break down the technical jargon of latency. Boeing 747 carries 500 passengers whereas Boeing 737 carries 150. Would you say 747 is 3 times faster than 737? The Boeing 747 is 3 times bigger than the 737, not faster since both travel at 500 miles per hour. Latency plays a vital role in algorithmic trading where speed is the key entity in executing a trade. A brief comparison between traditional system architecture andautomated system architecture.

A traditional trading system would consist of a system to read data, a storehouse of historical data, a tool to analyze historical data, a system to submit trading inputs and a system to route orders to the exchange. Exchange sends the tick by tick data. The server is mostly used for data storage, a synonym to an individual’s desktop.

The market data is retrieved from server to the trader’s tool where actionable intelligence (buy, sell, no trade) takes place. The actions are then passed via order manager to the exchange. These actions are sequential. The trader’s tool can only process and generate orders once it receives market data.

The advent of Direct Market Access known as DMA has brought drastic changes in the architecture of a trading system.

In a traditional system the data flow would occur from the broker to the trader’s tool. This is bettered in the automated trading system via DMA. This significantly reduces the time needed for data flow from the exchange to the trading tool. Even in theautomated trading systemthese actions of data flow and trade generation remain sequential.

Latency can be reduced between the trading tool (event occurrence) and order generation can be reduced to achieve better efficiency. This can be done by reducing the latency to the order of milliseconds and lower. Risk management has to be implemented in real-time without human intervention.

Why is low latency that important in the first place? To answer this question, think of trading as a running race. Faster the speed than your competitors, better your chances of winning. The objective in trading is trade execution at a competitive price.

It is desirable to improve latency to stop getting picked by competitors. Correct technology has to be implemented to reduce latency as low latency systems cost a lot. Hence a right balance between low latency investment and ROI on low latency has to be achieved.

A snapshot below provides latencies for different strategies.

Latency can be represented in an equation form.

L=P+N+S+I+AP

Here P is propagation time sending the bits along the wire, N is network packet processing- routing, switching and protection, S is serialization time- pulling the bits on/off the wire, I interrupt handling time- receiving the packet on the server, API is application Processing Time.

As discussed before, decisive actions have to be taken to balance sophistication levels to reduce latency and optimizing investment decisions for the same.

To summarize low latency is an important factor in algorithmic trading. Low latency leads to competitive prices for trade execution.

Check out the complete recording of the webinar here:

The Presentation Slides of the webinar can be accessed here:

About the Session

The webinar aimed to cover the following concepts:

Latency - Metrics and Limits

Tick to Trade Latencies

Present Landscape and Foreseeable Future

About the Speaker

The webinar was taken by Gaurav Raizada, he is a Director at iRageCapital Advisory Private Ltd., leads the firm's advisory practice in India on the Systems, Performance and Strategies. He has consulted extensively with core focus on strategy development and execution including trading systems development, latency reduction, optimization and transaction cost analysis. Gaurav is IIT and IIM Alumnus.

The webinar was conducted on 18th February, 2014.

---

*Imported from QuantInsti Blog on 2026-04-27*
