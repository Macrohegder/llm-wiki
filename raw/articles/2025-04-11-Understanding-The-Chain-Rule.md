---
title: "Understanding The Chain Rule"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/understanding-chain-rule/"
date: "2025-04-11"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Understanding The Chain Rule

**来源**: [QuantInsti](https://blog.quantinsti.com/understanding-chain-rule/)  
**日期**: 2025-04-11  
**作者**: QuantInsti

---

## 原文

Exploring the Chain Rule with Step-by-Step Examples

ByVarun Divakar

In this blog on “Understanding the chain rule,” we will learn the math behind the application of chain rule with the help of an example.

Table of Contents

What is a derivative?

What is the Chain Rule?

Understanding the Chain Rule

Example of Chain Rule

For those of you who are interested inNeural Networks and Deep Learning, the process ofbackpropagationis a very important concept which is extensively used while creating these advanced models. While performing backpropagation, we use the concept of chain rule to backpropagate the error values in prediction to adjust the weights.

To be able to understand this unit, you should know what a derivative is.

What is a derivative?

Don’t sweat it, in case you don’t know or don’t remember the same, you can learn about it on theglossary section of Quantra website.

What is the Chain Rule?

The chain rule is basically a formula for computing the derivative of a composition of two or more functions.

Understanding the Chain Rule

Let us say that f and g are functions, then the chain rule expresses the derivative of their composition asf ∘ g(the function which mapsxtof(g(x))). The derivative of this composition is calculated as mentioned below.

Herefis the function ofgandgis a function of variablex.

Another way of writing the above rule:

Where the functionFrepresents the composite functionf(g(x))

Let us say that we have three variablesx, yandzsuch that, the variablezdepends on the variabley, which in turn depends on the variablex. Soyandzare dependent variables, andz, via the intermediate variable ofy, depends onx. Then the chain rule for differentiating the variablezmay be written in the following manner.

This is the final formula that we use in backpropagation.

Herezis the function ofy,

z = f(y)

andyis a function ofx,

y= g(x)

Using the previous formula, we can rewrite the differential equation as follows:

Let us understand this better with the help of an example.

Example of Chain Rule

Let us understand the chain rule with the help of a well-known example from Wikipedia. Assume that you are falling from the sky, the atmospheric pressure keeps changing during the fall. Check out the graph below to understand this change.

At the time of your fall, 4000 meters above sea level, the initial velocity was zero, and the gravity is 9.8 meters per second squared. Now compare this situation to the previous chain rule equation. Let us say that the variablexin the equation is variablet, or time.

Then the variableyorg(t), which is the distance travelled by you since the beginning of the fall is given by

g(t) = 0.5*9.8t2

So, the height from the mean sea level can be given by the variableh, which is

h = 4000 - g(t)

Let us say that we also know, based on a model, the atmospheric pressure at a heighthas:

f(h) = 101325 e−0.0001h

These two equations can be differentiated by their respective variable to get the following information:

g′(t) = −9.8t,

where,g′(t)is the velocity of you at timet

f′(h) = −10.1325e−0.0001h

where,f′(h)is the rate of change in atmospheric pressure with respect to heighth

Now let us understand how we can combine these two equations to derive the

the rate of change in the atmospheric pressure with respect to time attseconds after the skydiver's jump, using the chain rule:

This equation gives us the rate of change of atmospheric pressure with respect to time since fall. In neural networks, we will need to calculate the change in weights at each neuron with respect to the errors in prediction. As you might have imagined by now, the chain rule helps adjusts these weights accordingly.

Conclusion

If we want to apply the chain rule to backpropagate the error in neural networks, then we will be using an equation such as this.

In the Quantra’s course onDeep Learning in Trading with Dr. E. P. Chan, we will help you not only understand advanced concepts such as deep learning, but also apply them in the context of trading.

Disclaimer:All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Suggested Reads:

Forward Propagation In Neural Networks

Understanding Backpropagation

---

*Imported from QuantInsti Blog on 2026-04-27*
