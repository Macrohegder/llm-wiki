---
title: "Python Exception: Raising And Catching Exceptions In Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-exception/"
date: "2018-09-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Exception: Raising And Catching Exceptions In Python

**来源**: [QuantInsti](https://blog.quantinsti.com/python-exception/)  
**日期**: 2018-09-25  
**作者**: QuantInsti

---

## 原文

Python Exception: Raising And Catching Exceptions In Python

ByMario Pisa Peña

In thelast post, we dealt with Python Errors and got a basic understanding of Python Exception: NameError and TypeError. In this post, we’ll get a deep Python Exception understanding, how to raise and how to catch Python Exception.

Resuming briefly, Python Errors are detected in the Python parser, i.e. when the Python code interpreter discovers some syntactically incorrect or an incomplete statement.

These python errors are easy to detect and fix because if we don’t correct them, we won’t be able to do anything with the code. These Python Errors are known asSyntaxError.

Python Exception

On one hand, there is Error in Python, while on the other hand, there is the Exception in Python (a python exception). These types of python error cannot be detected by the parser since the sentences are syntactically correct and complete, let’s say that the code logically makes sense, but at runtime, it finds an unexpected situation that forces the execution to stop.

This is what we callExceptions, ie. in this case, Python Exception. And fortunately for us, we can treat this python exception properly to prevent our code from ending its execution abruptly.

Understanding Python Exception

To better understand Python Exception, let’s see an example and going to play with it.

Example 1

In this example here, we have a very simple Python function to divide one number by another (we don’t really need the function to divide, but this serves as a structure on which to build the example).

This code is syntactically correct, is complete and doesn’t have errors. But the reality is that the correct execution of the code will depend on the valuesxandywe pass to the function. Let’s test some values.

Example 2

In this example, we call simple_div(2, 2) function with two numbers and the function works as expected, dividing the numbers.

Example 3

In this example, we call simple_div(0, 2) function with two numbers and the function works as expected, dividing the numbers.

Example 4

In this example, we call simple_div(2, 0) function with two numbers and the function doesn’t work as expected, because when we divide any number by 0 gives infinity, and infinity is not a number, because infinity is unknown and is not quantifiable, therefore, Python raises an exception, a python exception, called in this caseZeroDivisionError, the execution ends abruptly and does not let us continue (for example, we could be waiting for the result to do other operations).

Example 5

In this example, we call simple_div(2, 'a') function with one number and a character, hence the function doesn’t work because when we divide any number by characters, therefore, Python raises an exception (a python exception) called in this caseTypeError, the execution ends abruptly and does not let us continue.

Example 6

In this example, we call simple_div(2, a) function with one number and a variable named a, hence the function doesn’t work because the variable is not initialized, therefore, Python raises an exception (a python exception) called in this caseNameError, the execution ends abruptly and does not let us continue.

In any of these cases, if we were waiting for the result of the function to continue doing calculations, our code would end abruptly.

There are several ways to control these unexpected situations, for example, including control code that prevents calling the function with something that is not numbered and controlling that the denominator is not zero.

Another way to manage it would be by controlling python exception by capturing them when they occur, if they do. We call thiscatching exceptions.

Catching Exceptions

What we are going to try to do now is to control those anomalous situations (catch the exception) that can occur in the code execution, we are going to try to capture the first of the exceptions that we have seenZeroDivisionError.

It’s interesting to notice this verb, to try, because that’s precisely what we have to tell Python to try to do something and, if it finds an exception, do something with it.

In the function below, we are trying to perform a division, but if a ZeroDivisionError Python Exception is raised, we want to catch the exception and treat it properly, in this case, printing a message on the screen and offering the user a clean output.

We could also offer a value of type -1, 9999, or -9999 which would allow us to deal properly later in the code.

Let’s now try to catch exception TypeError, which, as you can imagine, follows the same structure.

In the case of exception NameError, the variable a does not exist, and therefore, does not allow to progress the execution of the code from the own call to the function, that is to say, the function never gets to be executed, because the function call cannot be made because the variable, that we are trying to pass to the function, does not exist.

On the other hand, we can follow the same structure to make the call to the function, that is to say, we try to call the function and if the python exception NameError occurs we treat it properly.

Let’s put it all together!

In block number 12, we have the function that accepts two input parameters and tries to make a division with them.

We also keep in mind that if some predictable situations occur, we can have them properly dealt with.

In blocks 13, 14 and 15 we simply try to call the function, taking into account also the possible python exception.

These python exceptions are probably the most typical, but there are many other python exceptions built into the python language that we can use.

Built-in Python Exception

Here's a very useful and important link that contains all theBuilt-in Python Exception

Conclusion

Python offers us the possibility of working with the so-called python exception to achieve a clean execution and allows us to make a treatment of certain anomalies that may occur in the python code executions.

In the next blog, we will see how we can build our own python exception and we will see in detail the python exception of python libraries like Pandas or Numpy.

For those aspiring to learn more about Python, it’s use and applications in the field of Algorithmic and Quantitative Trading or simply want to start trading in Python, they can opt for thePython For Tradingcourse byQuantra. It covers important concepts from scratch and also helps to develop and improve Python skills specific to trading.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
