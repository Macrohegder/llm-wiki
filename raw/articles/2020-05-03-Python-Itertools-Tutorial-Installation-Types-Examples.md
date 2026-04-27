---
title: "Python Itertools Tutorial: Installation, Types, Examples"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/itertools/"
date: "2020-05-03"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Itertools Tutorial: Installation, Types, Examples

**来源**: [QuantInsti](https://blog.quantinsti.com/itertools/)  
**日期**: 2020-05-03  
**作者**: QuantInsti

---

## 原文

Python Itertools Tutorial: Installation, Types, Examples

ByRekhit Pachanekar

Python itertools is quite simply, one of the best and elegant solutions to implement an iterator in Python. But what are Iterators?

An iterator is an object that can be iterated upon and which will return data, one element at a time. It allows us to traverse through all elements of a collection, regardless of its specific implementation.

While iterators are a great way to list the contents of a list, sometimes you wonder if we can just hide all the complexity into one single line of code. For example, we don’t want to worry about the number of elements when we are comparing two different dataframes. This is where the Python itertools module shines through.

Let us go through the outline of this blog and then dive right in:

Iterators and itertools in Python

Infinite iterators

Terminating iterators

Combinatoric iterators

All right! Let’s understand what are the prerequisites for using itertools.

Iterators and itertools in Python

Technically, in Python, an iterator is an object which implements the iterator protocol, which in turn consists of the methods __next__() and __iter__().

__iter__() method which returns the iterator object itself and is used while using the for and in keywords.

__next__() method returns the next value. It also returns StopIteration error once all the objects have been tracked.

Iterators are mostly used in for loops. You can read about them in detail in thePython Handbook.

You can import itertools in your Python code with the following commands

We have also imported the “operator” module as we will be using algebraic operators along with itertools.

But yes, it is that simple to import the module in Python. Let’s move forward to the first type of itertools.

Infinite iterators

As the name suggests, infinite iterators are created to go through the elements of a data object infinitely, unless we pass a break statement.

Let’s see an example of it.

The count() iterator

Here, we will append the count function with “itertool” to give us the function “itertool.count” iterator and pass the parameters start and step to begin counting.

In this code, 42 is the starting point and 8 is the step. Just so that the function doesn’t continue endlessly, we use the break statement to stop once it goes beyond 60.

Thus, the code is:

The output is as follows:

42
505866

I will just add here that since the "if" statement is invoked after the "print" statement, 66 is printed and then the iteration stops.

We will now move on to the next type of iterators, which are the opposite of infinite.

Terminating iterators

In contrast to the infinite iterators, this type of iterator does not keep going endlessly. Terminating iterators produce a short output and are used for fast processing of the elements in a collection. Let’s go through a few of them now.

The accumulate() iterator

This iterator can be used to perform algebraic operations on the elements of a collection. For example, let’s say we have the daily percentage returns of the closing price of Tesla, Inc. (TSLA) and we want to see how it adds up. Well we will use the accumulate function.

Since we need the data of a stock, we will import yahoo finance libraries and retrieve the data of Tesla Inc. for this example.

The code is as follows:

Now, we will use the accumulate function.

This will give us the following output

0.00254164043577076450.00789366815117254-0.025408562632891818-0.05447527833839694-0.1902005059491796-0.1288024515250945-0.14600300988614834-0.2621753684071464-0.2870259490496102-0.472803982601416-0.5062144458374956-0.6665584928598186-0.4826815945616202-0.48293885736531517-0.4671270785780336-0.30430962926118144-0.23648784708296355-0.2570534972553673-0.2831819213970286

Here, we have passed the function “operator.add” as a parameter. But you can also use “operator.mul” if you desire. If you don’t pass any parameter then it takes the addition operator by default and computes the result. Why don’t you try it out and let us know in the comments?

Let’s keep the momentum going and try another type of terminating iterator.

The chain() iterator

As you might have guessed, we can use the chain() itertool to combine two lists together. Here it is in action below:

The output will be as follows:

TSLAMSFTNVDAGOOGLAAPLINTCHDFCRELIANCEINFYICICIBANK

The compress() iterator

While the chain() iterator is used to combine more than one list (or rather any element), the compress() iterator can be used to select a few elements in the list. We will understand it by seeing the code.

The output is as follows:

TSLAGOOGLINTC

Thus, only those elements were printed which were associated with 1 in the selections list. You can also use ‘True’ and ‘False’ in place of 1 and 0.

The dropwhile() iterator

You can use this iterator to filter your list, but return only those elements after the condition has been false. For example, in our example below, we want to list only those closing prices after the stock price went below $700. Thus, we write the code as follows:

The output is as follows:

608.0645.3300170898438634.22998046875560.5499877929688546.6199951171875445.07000732421875430.20001220703125361.2200012207031427.6400146484375427.5299987792969434.2900085449219505.0539.25528.1599731445312514.3599853515625The takewhile() iteratorThis iterator is the opposite of the dropwhile() iterator. In this function, it will return the outputs till the conditions return false. As you have guessed it, you can use the two iterators according to your needs. The sample code for this iterator is as follows:The output is given as follows:743.6199951171875745.510009765625749.5724.5399780273438703.47998046875The filterfalse() iteratorMost of the iterators are self-explanatory, and filterfalse() is no exception. This iterator will only return the element if the condition is false.For example, if we want only those daily returns which are negative, we will put the condition that the daily returns should be more than 0 and the filterfalse() iterator will give us the required values. Let’s see how we use it in python.The output is as follows:-0.03330223078406436-0.02906671570550512-0.13572522761078265-0.01720055836105383-0.11617235852099805-0.024850580642463815-0.18577803355180578-0.03341046323607966-0.16034404702232297-0.0002572628036949798-0.02056565017240375-0.026128424141661277The islice() iteratorThis iterator has four parameters which can be passed, the element, starting element variable, ending variable and the number of elements to be skipped.Suppose, we wanted the Adj. Close price every third day, we would write the code as follows:The output would be as follows:743.6199951171875749.5703.47998046875645.3300170898438560.5499877929688445.07000732421875361.2200012207031427.5299987792969Well, these were some terminating iterators. Now, we will see the next type of iterators, which are more concerned with the selection and the arrangement of the values.Combinatoric iteratorsWe have all studied permutations and combinations before. These iterators make it really easy to list down all the possible values in a simple manner. Let’s start with the first one right away.The combinations() iteratorAs the name specifies, this iterator helps us illustrate all the possible combinations present in the list. The only parameters we have to pass are the elements and the number of values in a combination. Let’s see it in action right now:The output will be as follows:('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'INTC')The combinations_with_replacement() iteratorIf you had seen the output above, there were no stocks repeated in the combinations. This iterator takes care of that by listing the values repeated too.The Python code for this iterator is as follows:The output would is shown below:('TSLA', 'TSLA')('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'MSFT')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'NVDA')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'GOOGL')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'AAPL')('AAPL', 'INTC')('INTC', 'INTC')Well, these were the combinations, but what about the permutations? Let’s check it out right now.The permutations() iteratorRecall that in permutations, the order does matter. Hence ('TSLA', 'MSFT') and ('MSFT’, 'TSLA') are entirely different in permutations. Having said that, let us see the python code for this iterator.The output would be as follows:('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'TSLA')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'TSLA')('NVDA', 'MSFT')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'TSLA')('GOOGL', 'MSFT')('GOOGL', 'NVDA')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'TSLA')('AAPL', 'MSFT')('AAPL', 'NVDA')('AAPL', 'GOOGL')('AAPL', 'INTC')('INTC', 'TSLA')('INTC', 'MSFT')('INTC', 'NVDA')('INTC', 'GOOGL')('INTC', 'AAPL')Great! That is about it for the python itertools() tutorial. Do let us know in the comments how you can use these tools in your python codes.ConclusionPython itertools is a really convenient way to iterate the items in a list without the need to write so much  code and worry about the errors such as length mismatch etc. It also makes the Python code simple and readable as the names of the iterators are quite intuitive to understand and execute. In this blog we understood the concept of iterators and also the different types of iterators, ie the infinite, terminating and combinatoric iterators. We also learnt how to use these iterators with the help of simple codes and financial data taken from yahoo finance.Disclaimer:  All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

The takewhile() iterator

This iterator is the opposite of the dropwhile() iterator. In this function, it will return the outputs till the conditions return false. As you have guessed it, you can use the two iterators according to your needs. The sample code for this iterator is as follows:

The output is given as follows:

743.6199951171875745.510009765625749.5724.5399780273438703.47998046875

The filterfalse() iterator

Most of the iterators are self-explanatory, and filterfalse() is no exception. This iterator will only return the element if the condition is false.

For example, if we want only those daily returns which are negative, we will put the condition that the daily returns should be more than 0 and the filterfalse() iterator will give us the required values. Let’s see how we use it in python.

The output is as follows:

-0.03330223078406436-0.02906671570550512-0.13572522761078265-0.01720055836105383-0.11617235852099805-0.024850580642463815-0.18577803355180578-0.03341046323607966-0.16034404702232297-0.0002572628036949798-0.02056565017240375-0.026128424141661277The islice() iteratorThis iterator has four parameters which can be passed, the element, starting element variable, ending variable and the number of elements to be skipped.Suppose, we wanted the Adj. Close price every third day, we would write the code as follows:The output would be as follows:743.6199951171875749.5703.47998046875645.3300170898438560.5499877929688445.07000732421875361.2200012207031427.5299987792969Well, these were some terminating iterators. Now, we will see the next type of iterators, which are more concerned with the selection and the arrangement of the values.Combinatoric iteratorsWe have all studied permutations and combinations before. These iterators make it really easy to list down all the possible values in a simple manner. Let’s start with the first one right away.The combinations() iteratorAs the name specifies, this iterator helps us illustrate all the possible combinations present in the list. The only parameters we have to pass are the elements and the number of values in a combination. Let’s see it in action right now:The output will be as follows:('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'INTC')The combinations_with_replacement() iteratorIf you had seen the output above, there were no stocks repeated in the combinations. This iterator takes care of that by listing the values repeated too.The Python code for this iterator is as follows:The output would is shown below:('TSLA', 'TSLA')('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'MSFT')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'NVDA')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'GOOGL')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'AAPL')('AAPL', 'INTC')('INTC', 'INTC')Well, these were the combinations, but what about the permutations? Let’s check it out right now.The permutations() iteratorRecall that in permutations, the order does matter. Hence ('TSLA', 'MSFT') and ('MSFT’, 'TSLA') are entirely different in permutations. Having said that, let us see the python code for this iterator.The output would be as follows:('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'TSLA')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'TSLA')('NVDA', 'MSFT')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'TSLA')('GOOGL', 'MSFT')('GOOGL', 'NVDA')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'TSLA')('AAPL', 'MSFT')('AAPL', 'NVDA')('AAPL', 'GOOGL')('AAPL', 'INTC')('INTC', 'TSLA')('INTC', 'MSFT')('INTC', 'NVDA')('INTC', 'GOOGL')('INTC', 'AAPL')Great! That is about it for the python itertools() tutorial. Do let us know in the comments how you can use these tools in your python codes.ConclusionPython itertools is a really convenient way to iterate the items in a list without the need to write so much  code and worry about the errors such as length mismatch etc. It also makes the Python code simple and readable as the names of the iterators are quite intuitive to understand and execute. In this blog we understood the concept of iterators and also the different types of iterators, ie the infinite, terminating and combinatoric iterators. We also learnt how to use these iterators with the help of simple codes and financial data taken from yahoo finance.Disclaimer:  All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

The islice() iterator

This iterator has four parameters which can be passed, the element, starting element variable, ending variable and the number of elements to be skipped.

Suppose, we wanted the Adj. Close price every third day, we would write the code as follows:

The output would be as follows:

743.6199951171875749.5703.47998046875645.3300170898438560.5499877929688445.07000732421875361.2200012207031427.5299987792969

Well, these were some terminating iterators. Now, we will see the next type of iterators, which are more concerned with the selection and the arrangement of the values.

Combinatoric iterators

We have all studied permutations and combinations before. These iterators make it really easy to list down all the possible values in a simple manner. Let’s start with the first one right away.

The combinations() iterator

As the name specifies, this iterator helps us illustrate all the possible combinations present in the list. The only parameters we have to pass are the elements and the number of values in a combination. Let’s see it in action right now:

The output will be as follows:

('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'INTC')

The combinations_with_replacement() iterator

If you had seen the output above, there were no stocks repeated in the combinations. This iterator takes care of that by listing the values repeated too.The Python code for this iterator is as follows:

The output would is shown below:

('TSLA', 'TSLA')('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'MSFT')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'NVDA')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'GOOGL')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'AAPL')('AAPL', 'INTC')('INTC', 'INTC')

Well, these were the combinations, but what about the permutations? Let’s check it out right now.

The permutations() iterator

Recall that in permutations, the order does matter. Hence ('TSLA', 'MSFT') and ('MSFT’, 'TSLA') are entirely different in permutations. Having said that, let us see the python code for this iterator.

The output would be as follows:

('TSLA', 'MSFT')('TSLA', 'NVDA')('TSLA', 'GOOGL')('TSLA', 'AAPL')('TSLA', 'INTC')('MSFT', 'TSLA')('MSFT', 'NVDA')('MSFT', 'GOOGL')('MSFT', 'AAPL')('MSFT', 'INTC')('NVDA', 'TSLA')('NVDA', 'MSFT')('NVDA', 'GOOGL')('NVDA', 'AAPL')('NVDA', 'INTC')('GOOGL', 'TSLA')('GOOGL', 'MSFT')('GOOGL', 'NVDA')('GOOGL', 'AAPL')('GOOGL', 'INTC')('AAPL', 'TSLA')('AAPL', 'MSFT')('AAPL', 'NVDA')('AAPL', 'GOOGL')('AAPL', 'INTC')('INTC', 'TSLA')('INTC', 'MSFT')('INTC', 'NVDA')('INTC', 'GOOGL')('INTC', 'AAPL')

Great! That is about it for the python itertools() tutorial. Do let us know in the comments how you can use these tools in your python codes.

Conclusion

Python itertools is a really convenient way to iterate the items in a list without the need to write so much  code and worry about the errors such as length mismatch etc. It also makes the Python code simple and readable as the names of the iterators are quite intuitive to understand and execute. In this blog we understood the concept of iterators and also the different types of iterators, ie the infinite, terminating and combinatoric iterators. We also learnt how to use these iterators with the help of simple codes and financial data taken from yahoo finance.

Disclaimer:  All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
