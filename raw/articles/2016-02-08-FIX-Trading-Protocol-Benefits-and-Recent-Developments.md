---
title: "FIX Trading Protocol: Benefits and Recent Developments"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/fix-trading-protocol/"
date: "2016-02-08"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# FIX Trading Protocol: Benefits and Recent Developments

**来源**: [QuantInsti](https://blog.quantinsti.com/fix-trading-protocol/)  
**日期**: 2016-02-08  
**作者**: QuantInsti

---

## 原文

Financial Information eXchange (FIX) Trading Protocol

ByDhanjit Das

FIX (Financial Information eXchange) protocol is the defacto standard for message communication for almost two decades of electronic trading. In 1992, Salamon brothers and Fidelity Investments initiated FIX protocol to be used in equity trading. Today, it is used by a variety of market participants, firms, and vendors. With the advent of electronic trading, various exchanges and firms devised their own messaging formats, and so FIX was seen and developed as an intermediary messaging format, a common underlying means of standardized communications.

Benefits

Pre-trade, on trade and post-trade processes have over the decades changed distinguishably, and even more so for different market participants and firms. The automation of processes demanded an automation of communication in general, and a standardized format of messages.

Connectivity costs

Widespread use of a standard messaging protocol reduces cost and complexity of integrating various internal processes, hence beneficial to all stakeholders. There is a vast improvement in the ease of maintaining application working over FIX than one that uses a proprietary protocol. The use of FIX reduces the costs of establishing a trading platform, automated execution tool, etc. simply by allowing replication from existing implementations.

Reduced complexity for involving multiple partners

If three people are having a conversation, it makes sense for them to use the language common to all three, the same analogy can be applied to message interaction between different market participants and stakeholders. With FIX as a standard, it is easier to involve multiple partners as one avoids the added complexity of using proprietary protocols to deal with multiple firms/exchanges.

Source: Oxera

Source: Oxera

Reliable and Reduced Risk, and Continuous Development

FIX is a well tested, widely used protocol. The reliability of FIX is hence guaranteed. FIX Protocol Ltd, is the organization owning the rights and looking into the issuing of the FIX standard.

Increased Quality of Service

Investment management firms will be able to switch more easily between brokers due to the availability of a common standard protocol. Thereby, increasing competition among brokers for trading services; resulting in increased quality of service.

Needless to say, the benefits compound when more firms use the same messaging protocol.

Some numbers…

To put the impact of FIX support into perspective, the size of the markets that currently benefit from the protocol now include the USA, Europe and Asia- Pacific equity markets, which in 2008 had an annual turnover of $113 trillion, in addition to a significant number of emerging equity markets; the government and corporate debt securities markets, which had an outstanding value globally of $83.9 trillion in June 2009; the exchange traded derivatives markets, with notional amounts in the USA, Europe and Asia-Pacific in June 2009 of $63.4 trillion and the global over-the counter (OTC) derivatives markets, with notional amounts in December 2008 of $591 trillion.

Within six months of implementing FIX in 2000, GIM had upgraded its OMS to the FIX-compatible version, built a server and installed a FIX gateway, completed testing and was sending orders via FIX. Initially, FIX was used with only one broker, but within three years, GIM was communicating electronically with 50 or more brokers for FIX orders and executions, 13 of which also handled FIX allocations.

In the case of ACI, FIX was introduced in 1996. Within three years of introducing FIX capabilities for executions, more than 97% of US executions and 93% of international executions were carried out using FIX. At the same time, within three years of introducing FIX-compatible allocations, more than 88% of US allocations and 43% of international allocations were carried out using FIX.

NBIM adopted FIX in late 2002 and went from 100% manual execution to 80–90% via FIX within one year. Its current use of FIX is almost 100%.

Recent Developments

*** New Open Technical Resource (github.com)

On 23rd Nov, 2015 FIX Trading community opened its technical standards process to developers in the financial industry. The interface is hosted onGithub. Several FIX projects have already been published to Github and more are on the way.

*** Transport Independence Framework (FIXT)

With the advent of 'Transport Independence' multiple application messages can be carried over via one signal. This allows FIX messages to be used over any suitable transport technology from a message queue, buses etc.

*** FAST (FIX Adapted for STreaming) protocol

Developed as a low latency solution, the FAST framework provides optimized data representation on the network resulting in higher throughput and more efficient communication between financial institutions.

*** FIX Simple Binary Encoding (FIX SBE)

FIX SBE again strives for faster communication, with a message design that strives for direct data access without complex transformations and conditional logic. It uses native binary data types and prefers fixed position, fixed width fields that support direct access.

Message Structure

FIX is layered over a TCP connection. A FIX message has tag value pairs; each pair being separated with a ASCII character code SOH (0x001), a tag separated from a value with an equality character (=). Every message has a header, a body and a tail. The tail is the checksum with the tag 10. The fix version and body length of the message are in the header part (8 and 9 tags respectively). The message type is denoted by the value of tag 35.

Examples

8=FIX.4.19=11235=049=BRKR56=INVMGR34=23552=19980604-07:58:28112=19980604-07:58:2810=157

8=FIX.4.19=15435=649=BRKR56=INVMGR34=23652=19980604-07:58:4823=11568528=N55=SPMI.MI54=227=20000044=10100.00000025=H10=159

Next Step

If you’re a retail trader or a tech professional looking to start your own automated trading desk, startlearning Algo tradingtoday! Begin with basic concepts likeautomated trading architecture,market microstructure,strategy backtesting systemandorder management system.

---

*Imported from QuantInsti Blog on 2026-04-27*
