---
title: "Dealing With Errors And Exceptions In Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/dealing-python-error-exceptions/"
date: "2018-09-19"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Dealing With Errors And Exceptions In Python

**来源**: [QuantInsti](https://blog.quantinsti.com/dealing-python-error-exceptions/)  
**日期**: 2018-09-19  
**作者**: QuantInsti

---

## 原文

Dealing With Error And Exceptions In Python

ByMario Pisa Peña

All programmers, sooner rather than later, will find themselves spending a significant amount of time dealing with errors in their code. Therefore, it is necessary to understand the types of errors we find and how to handle them. To know more about Python for trading, you can also check outthis article

This post will attempt in plain language to review aspects of Python Errors interpretation and Python Errors resolution.

Understanding Errors and Exceptions in Python

There are two kinds of errors: Python Syntax Errors and Python Exceptions.

Python Syntax Errorsare usually easy to detect and fix. Unless we write code in a text editor that doesn’t include a Python parser, the editor usually tells us when we have asyntax errori.e. when we have written something that Python is not able to understand.

Python Exceptions, on the contrary, are errors that can only be detected when the code is executed. Here, the code is syntactically correct, but when executing it, it encounters some problem at a certain line that prevents the code from continuing to be executed.

Python Syntax Errors must be corrected immediately, otherwise, we can’t do anything with the code. Python Exceptions are unusual situations that can occur at runtime and the best thing we can do is to control them to prevent an abnormally ending execution.

Let’s see how we can deal with these kinds of errors.

Python Syntax Errors

With a very simple example, let’s check how Python Syntax Errors behave.

The first thing we are going to see is a syntactically correct code, we want to print a message on the screen in Python 3:

Since there is no Python Syntax Error, Python gives us the output we are looking for.

Now let’s try to do the same thing but in the style of Python 2 (remember, here we are using Python 3):

Although for Python 2 this statement is not a problem, the Python 3 interpreter expects to find parentheses surrounding the message to be printed. Therefore, this is how it lets us know, telling us clearly that there is a Python Syntax Error and also offers us a possible solution.

Let’s now make some silly mistakes to observe Python’s output:

Here we have forgotten to close the quotes and parentheses, the Python interpreter tells us that we have a problem at the end of line (EOL), i.e. the end of the line is not as expected.

We’re going to try to correct it by making another Python Syntax Error:

Here we close the print statement but leave the string open. The Python interpreter again gives us an error message indicating that the end of the line is still incorrect.

Okay, we’re going to close the string literal now, but this time we’re going to leave the print without closing.

What happened here?Python doesn’t offer us the expected output, but neither does it throw up an error. Instead, it shows a line with the secondary prompt (the three dots …), i.e. the interpreter is waiting for more information. In this case, we could close the parentheses, or even add more information to the print statement.

Well, here Python gives us the opportunity to add more information to the print statement because the interpreter is still open and waiting for an input. Until we close the sentence, the Python interpreter does not know that we have finished writing the print and therefore expects us to enter more information.

In the examples so far, we have introduced the statements directly in the interpreter, butwhat would happen if the code was in a file?

Here, it is indicating a Python Error at the end of file (EOF). However this time, it does not allow us to enter any information, and this is because we are launching Python to run a file. If this file contains errors, Python returns to the operating system terminal, indicating the file and the line where the error was found.

PythonExceptions

Python Exceptions are a type of error that is only triggered if an anomaly is found at runtime.

For example:

z = x + y

Syntactically it is correct, but whether the instruction ends well or badly depends on the values it gets from x and y, if they have any.

Suppose that:

x = 1 & y = 4:

The instruction will be executed without problems and will give us a result of:

5 for z.

What happens if x and/or y are not declared/initialized?

We get an exception, in this case, calledNameErrorthat stops the execution. This is because it does not find the variables we want to add (they do not exist, they have not been declared or initialized)

What happens if x and/or y were characters?

We get a Python Exception, in this case, calledTypeErrorthat stops the execution. This has happened because we are trying to add a number with a few letters and since it is not possible to do that operation, the interpreter throws us an exception.

So far we have only seen two exceptions:NameErrorandTypeError, but there are many more Python Exceptions embedded in Python. In addition, and this is a fundamental advantage, we can declare, catch and handle our own Python Exceptions.

Another of the most important aspects in handling Python Exceptions is that we can control them. That is, once an anomalous situation has occurred, instead of allowing the execution to be stopped, we can control that exception and treat it properly to allow, generally, the execution of the code to continue.

In thenext post, we will see how to deal with exceptions and how to make our programs more robust.

Next Steps

For those aspiring to learn more about Python, it's use and applications in the field of Algorithmic and Quantitative Trading or simply want to start trading in Python, they can opt for thePython For Tradingcourse byQuantra.  It covers important concepts from scratch and also helps to develop and improve Python skills specific to trading.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
