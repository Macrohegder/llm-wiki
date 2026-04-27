---
title: "How to Build a Flag Pattern Scanner in RealTest"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/how-to-build-a-flag-pattern-scanner"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# How to Build a Flag Pattern Scanner in RealTest

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/how-to-build-a-flag-pattern-scanner)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

How to Build a Flag Pattern Scanner in RealTest
A step-by-step guide to detecting tight flag pattern and low-volatility setups inspired by Minervini and Qullamaggie.
SetupAlpha
Apr 23, 2025
2
1
Share
Hey! In this guide, I’ll walk through how to build a tight
flag pattern scanner
using
RealTest
. This pattern rising swing lows, falling swing highs, and compressing volatility is one that discretionary traders like Mark Minervini and Kristjan Kullamägi often reference.
The goal here is simple: outline the technical steps to detect this structure systematically. This isn’t about replicating their full trading approach since they incorporate fundamentals and discretion but it’s a useful starting point for anyone interested in screening for similar setups.
We’ll go section by section, covering s...

---

## 原文

How to Build a Flag Pattern Scanner in RealTest
A step-by-step guide to detecting tight flag pattern and low-volatility setups inspired by Minervini and Qullamaggie.
SetupAlpha
Apr 23, 2025
2
1
Share
Hey! In this guide, I’ll walk through how to build a tight
flag pattern scanner
using
RealTest
. This pattern rising swing lows, falling swing highs, and compressing volatility is one that discretionary traders like Mark Minervini and Kristjan Kullamägi often reference.
The goal here is simple: outline the technical steps to detect this structure systematically. This isn’t about replicating their full trading approach since they incorporate fundamentals and discretion but it’s a useful starting point for anyone interested in screening for similar setups.
We’ll go section by section, covering settings, swing logic, volatility, and the final scan.
1.
Detecting Swing Lows
SwingLow:	l > l[5] and l[1] > l[5] and l[2]>l[5] and l[3]>l[5] and l[4]>l[5] and l[5]<l[6] and l[5]<l[7] and l[5]<l[8] and l[5]<l[9] and l[5]<l[10]
This logic defines a
swing low
:
The
low 5 days ago
(
l[5]
) must be
lower
than the
five days before
it (
l[6]
to
l[10]
)
and
the
five days after
it (
l
to
l[4]
).
This confirms that
five days ago
was a
pivot low
lower than its surrounding bars.
Finding the Most Recent Swing Lows
BarAgo1L:	SinceTrue(SwingLow) + 5
SwingLow1:	l[BarAgo1L]
SinceTrue(SwingLow)
counts
how many bars ago
the
last swing low
occurred.
We add
+5
because the swing low is always
five bars back
(from our earlier calculation).
SwingLow1
captures the
low price
at that most recent swing low.
Finding the Previous Swing Lows
BarAgo2Lraw:	SinceTrue(SwingLow)[BarAgo1L]
BarAgo2L:	BarAgo1L + BarAgo2Lraw + 5
SwingLow2:	l[BarAgo2L]
BarAgo2Lraw
: From the
previous swing low's position
, it looks
further back
to find the next occurrence of a swing low.
BarAgo2L
: Adds everything up:
The number of bars to the
first swing low
.
Plus the
gap to the second swing low
.
Plus
5
for the bar position logic.
The same logic repeats once more for the
third swing low
:
BarAgo3Lraw:	SinceTrue(SwingLow)[BarAgo2L]
BarAgo3L:	BarAgo2L + BarAgo3Lraw + 5
SwingLow3:	l[BarAgo3L]
2.
Detecting Swing Highs (Same Logic, Inverted)
Swing highs follow the same structure but detect
peaks
:
SwingHigh:	h<h[5] and h[1] < h[5] and h[2]<h[5] and h[3]<h[5] and h[4]<h[5] and h[5]>h[6] and h[5]>h[7] and h[5]>h[8] and h[5]>h[9] and h[5]>h[10]
A
swing high
occurs when the
high 5 days ago
is higher than both the
five days before
and the
five days after
.
Finding the Swing Highs
BarAgo1H:	SinceTrue(SwingHigh) + 5
SwingHigh1:	h[BarAgo1H]
This finds the
most recent swing high
and its
price
.
And again, for
previous swing highs
:
// Previous confirmed swing high
BarAgo2Hraw:	SinceTrue(SwingHigh)[BarAgo1H]
BarAgo2H:	BarAgo1H + BarAgo2Hraw + 5
SwingHigh2:	h[BarAgo2H]

// One more back
BarAgo3Hraw:	SinceTrue(SwingHigh)[BarAgo2H]
BarAgo3H:	BarAgo2H + BarAgo3Hraw + 5
SwingHigh3:	h[BarAgo3H]
If you enjoy then subsribe now!
Subscribe
3.
Calculating Bollinger Band Width (Volatility Measure)
bbw:	(BBTop(20,2) - BBBot(20,2)) / avg(c,20) * 100 
LowVolatility:	Lowest(bbw,100)==bbw
BBW (Bollinger Band Width)
=
Difference between the
upper
and
lower
Bollinger Bands (20-period, 2 standard deviations).
Divided by the
20-day average close
.
Multiplied by
100
to express as a
percentage
.
LowVolatility
checks if the
current BBW
is the
lowest
in the past
100 days
.
This confirms
volatility compression
, a key feature of the
flag pattern
.
4.
Defining the Flag Pattern
Pattern:	SwingLow1 > SwingLow2 and SwingLow2 > SwingLow3 and SwingHigh1 < SwingHigh2 and SwingHigh2 < SwingHigh3 and Lowest(l,5)[1]>Lowest(l, BarAgo3Lraw)[1] and highest(l,5)[1]<highest(l, BarAgo3Hraw)[1] and LowVolatility
Rising swing lows
:
Most recent swing low
>
second swing low
>
third swing low
.
Falling swing highs
:
Most recent swing high
<
second swing high
<
third swing high
.
Extra condition on recent lows and highs
:
The
lowest low of the last 5 bars
is
higher
than the
lowest low
from the
third swing low
period.
The
highest high of the last 5 bars
is
lower
than the
highest high
from the
third swing high
period.
Low volatility
:
The
current Bollinger Band Width
is at its
lowest in 100 days
.
Together, these confirm a
flag pattern
: price compressing between
rising lows
,
falling highs
, and
low volatility
.
5.
Final Scan: Apply Filters
Filter:	Pattern and c>Avg(c,200) and InRUI
Pattern
: Requires all flag conditions.
c > Avg(c,200)
: Price must be
above its 200-day moving average
to favor
uptrend
candidates.
InRUI
: Stock is in the
Russell 1000 index
. (It can be any universe)
Summary
This scanner looks for
compression patterns
rising lows, falling highs, and squeezing volatility on
Russell 1000 stocks
above their
200-day moving average
.
It’s inspired by
Minervini
and
Qullamaggie
setups but
only captures the technical side
(no fundamentals).
But keep in mind this isn’t exactly the pattern Minervini or Qullamaggie use on every trade. It captures one flavor of setups they like, but their edge comes from discretion, fundamentals, and timing, not rigid patterns alone.
You can adjust
swing sensitivity
(the number of bars before/after) or the
volatility window
to fit different styles.
If you found this useful, we offer a lot
of ready-to-run RealTest strategies and backtests 👇
just download and run. Check them out
HERE
.
Every equity-curve/strategy includes trading cost.
Feel free to reach out with questions or feedback!
2
1
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
