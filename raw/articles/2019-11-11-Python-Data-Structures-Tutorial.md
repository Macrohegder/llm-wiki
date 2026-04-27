---
title: "Python Data Structures Tutorial"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-data-structures/"
date: "2019-11-11"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Data Structures Tutorial

**来源**: [QuantInsti](https://blog.quantinsti.com/python-data-structures/)  
**日期**: 2019-11-11  
**作者**: QuantInsti

---

## 原文

Python Data Structures Tutorial

ByJay Parmar

Python has various built-in data structures such as tuples, lists, dictionaries, and sets. Like a variable, python data structures are also used to store a value. Unlike a variable, they don't just store a value, rather a collection of values in various formats. Broadly speaking, python data structures are divided intoarray,listandfile. Arrays can be considered a basic form of python data structures while files are more advanced to store complex data.

This blog article is an excerpt from thePython Basics Handbookcreated for the simple purpose of making the reader understand the beauty and simplicity of thePython language.

We will cover the following topics in this python data structures tutorial:

Indexing and Slicing

Tuples

Stacks and Queues

Dictionaries

Before we dive into the world of python data structures, let us have a look at the concept ofindexingandslicingwhich is applicable to all data structures in Python.

Indexing and Slicing

A string can be thought of as a sequence of characters. Similarly, python data structures store sequences of objects (floats, integers, strings, etc.).

Consider a sequence of 10 characters ranging from A to J where we assign a unique position to each literal in a sequence. The position assigned to each character is a sequence of integers beginning with 0 up to the last character. These increase successively by 1 as can be seen below.

In the above sequence, the characterAis at index0,Bat1,Cat2, and so on. Notice how the index increases in chronological order by one unit at each step. Whenever a new character is appended to this sequence, it will be appended at the end and will be assigned the next index value (in the above example, the new index will be10for the new character). Almost all python data structures have an index to position and locate the element.

Elements within the sequence can be accessed using the square brackets[]. It takesindexof an element and returns the element itself. The syntax for accessing a single element is as follows:

sequence[i]

The above statement will return the element from sequence at indexi. We can access multiple elements from the sequence using the syntax[start index : end index]in the following manner:

sequence[si : ei]

The above statement will return values starting at indexsiup to but NOT including the element at indexei. This operation is referred to asslicing. For example:

sequence[0:4] will return elements from 'A' to 'D' and not up to 'E'. Element at the last index in the provided range will not be returned.

Python also supports negative indexing to access elements from the sequence end and it starts with -1 as follows:

A sequence can also be sliced using the negative indexing. In order to access the last element, we write

sequence[-1]

and it will return the elementJ. Similarly, a range can be provided to access multiple elements.

sequence[-5:-1] will return elements from 'F' to 'I'

An array can be thought of as a container that can hold a fixed number of data values of the same type. Though the use of array is less popular in Python as compared to other languages such as C and Java, most other python data structures internally make use of arrays to implement their algorithms. An array consists of two components, vizElementandIndex.

Element: These are the actual data values to be stored in an array.

Index: Each element in an array is positioned at the particular location depicted by an index. Python followszero-based indexingwhich means an index will always start with 0.

We can create an array by using the built-inarraymodule. It can be created as follows:

In [1]: from array import *
In [2]: arr = array('i', [2, 4, 6, 8])
In [3]: arr
Out[3]: array('i', [2, 4, 6, 8])
In [4]: type(arr)
Out[4]: array.array

In the above python data structures example, we import thearraymethod from thearraymodule and then initialize the variablearrwith values2,4,6, and8within the square brackets. Theirepresents the data type of values. In this case, it represents an integer.Python array documentationprovides more information about the various type codes available in Python.

Visualizing an Array

An array declared above can be represented in the following manner:

From the above illustration, the following are the points to be considered.

Index starts with 0.

Array length is 4 which means it can store 4 values.

An array can hold values with a single data type only.

Each element can be accessed via its index.

Accessing Array Element

We use slicing operation to access array elements. Slicing operation is performed using the square brackets[]. It takes an index of an element we are interested in. It can be noticed that the index of the first element in the above array is 0. So, in order to access an element at the position 3, we use the notationarr[2]to access it.

# Here, 2 represents the index of element 6
In [5]: arr[2]
Out[5]: 6
In [6]: arr[0]
Out[6]: 2

Manipulating Arrays

Let us now understand different array operations in this python data structures tutorial. Thearraymodule provides a wide variety of operations that can be performed based on the requirement. We will learn some of the most frequently used operations.

We use insertion operation to insert one or more data elements into an array. Based on the requirement, an element can be inserted at the beginning, end or any given index using theinsert()method.

# Inserting an element at the beginning
In [7]: arr.insert(0, 20)
In [8]: arr
Out[8]: array('i', [20, 2, 4, 6, 8])
# Inserting an element at the index 3
In [9]: arr.insert(3, 60)
In [10]: arr
Out[10]: array('i', [20, 2, 4, 60, 6, 8])

An element can be deleted from an array using the built-inremove()method.

In [11]: arr.remove(20)
In [12]: arr
Out[12]: array('i', [2, 4, 60, 6, 8])
In [13]: arr.remove(60)
In [14]: arr
Out[14]: array('i', [2, 4, 6, 8])

We can update an element at the specific index using the assignment operator=in the following manner:

# Update an element at index 1
In [15]: arr[0] = 1
In [16]: arr
Out[16]: array('i', [1, 4, 6, 8])
# Update an element at index 3
In [17]: arr[3] = 7
In [18]: arr
Out[18]: array('i', [1, 4, 6, 7])

In addition to the above-mentioned operation, thearraymodule provides a bunch of other operations that can be carried out on an array such as reverse, pop, append, search, conversion to other types, etc. More details can be foundhere

Though Python allows us to perform a wide variety of operations on arrays, the built-in array module is rarely used. Instead, in real world programming most programmers prefers to use NumPy arrays provided by the NumPy library.

Though Python allows us to perform a wide variety of operations on arrays, the built-in array module is rarely used. Instead, in real world programming most programmers prefers to use NumPy arrays provided by the NumPy library.

Tuples

In Python data structures, tuples are part of the standard library. Like arrays, tuples also hold multiple values within them separated by commas. In addition, it also allows storing values of different types together. Tuples are immutable, and usually, contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.

To create a tuple, we place all elements within brackets(). Unlike arrays, we need not import any module for using tuples. Let us look at some operations on the tuples python data structure now.

# Creating a tuple 'tup' with elements of the same data type
In [19]: tup = (1, 2, 3)
In [20]: tup
Out[20]: (1, 2, 3)
# Verifying the type
In [21]: type(tup)
Out[21]: tuple
# Creating a tuple 'tupl' with elements of different data types
In [22]: tupl = (1, 'a', 2.5)
In [23]: type(tupl)
Out[23]: tuple

The tupletuplcreated above can be visualized in the following manner:

A tuple python data structure can also be created without using the brackets.

# Creating a tuple without brackets
In [24]: tup = 1, 2, 3
In [25]: type(tup)
Out[25]: tuple

We can repeat a value multiple times within a tuple as follows:

In [26]: tupl = (1,) * 5 # Note trailing comma
In [27]: tupl
Out[27]: (1, 1, 1, 1, 1)

Accessing tuple elements

A slice operation performed using the square brackets[]is used to access tuple elements. We pass the index value within the square brackets to get an element of our interest. Like arrays, tuples python data structures also have an index and all elements are associated with the particular index number. Again, the index starts with '0'.

# Access an element at index 0
In [28]: tup[0]
Out[28]: 1
# Access an element at index 2
In [29]: tup[2]
Out[29]: 1

Python throws an error if we try to access an element that does not exist. In other words, if we use the slice operation with a non-existent index, we will get an error.

In [30]: tup[3]
Traceback (most recent call last):
 File "<ipython-input-30-c965c442ca22>", line 1, in <module>
 tup[3]
IndexError: tuple index out of range

In the above example, we try to access an element with index3which does not exist. Hence, Python threw an error statingindex out of range.

The built-inlen()function is used to check the length of a tuple.

In [31]: len(tup)
Out[31]: 3
In [32]: len(tupl)
Out[32]: 5

Immutability

In Python data structures, tuple objects are immutable. That is, once they are created, it cannot be modified. If we try to modify a tuple, Python will throw an error.

In [33]: tup[1] = 10
Traceback (most recent call last):
 File "<ipython-input-33-991819cff38c>", line 1, in <module>
 tup[1] = 10
TypeError: 'tuple' object does not support item assignment

As expected, the interpreter threw an error depicting the tuple object to be immutable.

Concatenating Tuples

Python allows us to combine two or more tuples or directly concatenate new values to an existing tuple. Let us see how to concatenate tuples python data structures now:

In [34]: t1 = (1, 2, 3)
In [35]: t2 = (4, 5)
In [36]: t1 + t2
Out[36]: (1, 2, 3, 4, 5)

Tuples can be concatenated using operators*=and+=.

In [37]: t1 = (1, 2, 3)
In [38]: t1 += 4, 5
In [39]: t1
Out[39]: (1, 2, 3, 4, 5)

Unpacking Tuples

In one of the above example, we encountered the statementtup = 1, 2, 3which is, in turn, an example oftuple packing. That is, we pack various values together into a single variabletup. The reverse operation is also possible:

In [40]: tup
Out[40]: (1, 2, 3)
In [41]: x, y, z = tup

The above statement performs theunpackingoperation. It will assign the value1to the variablex,2toy, and3toz. This operation requires that there are as many variables on the left-hand side of the equal sign as there are elements in the tuples python data structures.

Tuple method

Tuple being one of the simple objects in Python data structures, is easier to maintain. There are only two methods available for tuple objects:

index() : This method returns the index of the element.

In [42]: tup
Out[42]: (1, 2, 3)
In [43]: tup.index(3) # Returns the index of value '3'.
Out[43]: 2

count() : This method counts the number of occurrences of a value.

In [44]: tup = (1, 1, 1, 1, 1)
In [45]: tup.count(1)
Out[45]: 5

Some of the reasons why tuples python data structures are useful are given below:

They are faster than lists.

They protect the data as they are immutable.

They can be used as keys on dictionaries.

Alistis one of the python data structures that holds an ordered collection of items i.e. we can store asequenceof items in a list. In Python data structures, lists are created by placing all items within square brackets[]separated by a comma.

It can have any number of items and they may be of different data types and can be created in the following manner:

# Empty list
In [46]: list_a = []
In [47]: list_a
Out[47]: []
# List with integers
In [48]: list_b = [1, 2, 3]
In [49]: list_b
Out[49]: [1, 2, 3]
# List with mixed data types
In [50]: list_c =[1, 2.5, 'hello']
In [51]: list_c
Out[51]: [1, 2.5, 'hello']

A list can also have another list as an item. This is called anested list.

In [52]: a_list = [1, 2, 3, ['hello', 'stock'], 4.5]

Accessing List Items

Like with any other python data structures, slice operator is used to access list items or a range of list items. It can be used in the following manner.

In [53]: stock_list = ['HP', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AMZN', 'NLFX']
# Accessing an element at index 2
In [54]: stock_list[2]
Out[54]: 'TSLA'
# Accessing multiple elements using slicing
In [55]: stock_list[1:4]
Out[55]: ['GOOG', 'TSLA', 'MSFT']
# Accessing last element using negative index
In [56]: stock_list[-1]
Out[56]: 'NLFX'

Updating Lists

Unlike tuples, lists python data structures are mutable. That is, we can change the content even after it is created. Again, the slicing operation helps us here

In [57]: stock_list
Out[57]: ['HP', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AMZN', 'NLFX']
# Updating the first element
In [58]: stock_list[0] = 'NVDA'
# Updating the last 3 elements
In [59]: stock_list[-3:] = ['AMD', 'GE', 'BAC']
In [60]: stock_list
Out[60]: ['NVDA', 'GOOG', 'TSLA', 'AMD', 'GE', 'BAC']

It is also possible to add new elements to an existing list. Essentially a list is an object in Python. Hence, the list class provides various methods to be used upon the list object. There are two methodsappend()andextend()which are used to update an existing list.

append(element)method adds a single element to the end of the list. It does not return the new list, just modifies the original list.

extend(list2)method adds the elements in list2 to the end of the list.

In [61]: stock_list
Out[61]: ['HP', 'GOOG', 'MSFT']
In [62]: stock_list.append('AMZN')
In [63]: stock_list
Out[63]: ['HP', 'GOOG', 'MSFT', 'AMZN']

In the above example, we add a new element using theappend()method. Let's add multiple elements to the list. In Python data structures, whenever we are to add multiple literal to any object, we enclose it within list i.e. using[]the square brackets. The output that we expect is the appended list with all the new elements.

In [64]: stock_list.append(['TSLA', 'GE', 'NLFX'])
In [65]: stock_list
Out[65]: ['HP', 'GOOG', 'MSFT', 'AMZN', ['TSLA', 'GE', 'NLFX']]

The output we got is not as per our expectation. Python amended the new element as a single element to thestock_listinstead of appending three different elements. Theextend()method is provided to achieve this in lists python data structures.

In [66]: stock_list
Out[66]: ['HP', 'GOOG', 'MSFT', 'AMZN']
In [67]: stock_list.extend(['TSLA', 'GE', 'NLFX'])
In [68]: stock_list
Out[68]: ['HP', 'GOOG', 'MSFT', 'AMZN', 'TSLA', 'GE', 'NLFX']

To simplify, theappend()method is used to add a single element to the existing list and it takes a single element as an argument, whereas theextend()method is used to add multiple elements to the existing list and it takes a list as an argument.

List Manipulation

Lists are one of the most versatile and used python data structures. In addition to the above-discussed methods, we also have other useful methods at our disposal. Some of them are listed below:

insert(index, element): Inserts an item at a given position. The first argument is the index of the element before which to insert, solist.insert(0, element)inserts at the beginning of the list.

# Inserting an element at index position 1.
In [69]: stock_list.insert(1, 'AAPL')
In [70]: stock_list
Out[70]: ['HP', 'AAPL', 'GOOG', 'MSFT', 'AMZN', 'TSLA', 'GE', 'NLFX']

remove(element): Removes the first item whose value iselementprovided in an argument. Python will throw an error if there is no such item.

# Removing the element 'AAPL'
In [71]: stock_list.remove('AAPL')
In [72]: stock_list
Out[72]: ['HP', 'GOOG', 'MSFT', 'AMZN', 'TSLA', 'GE', 'NLFX']
# Again removing the element 'AAPL'.
In [73]: stock_list.remove('AAPL') # This line will throw an error as there is no element 'AAPL' the list.
Traceback (most recent call last):
 File "<ipython-input-73-8af176c2bd12>", line 1, in <module>
 stock_list.remove('AAPL')
ValueError: list.remove(x): x not in list

pop(): This function removes and returns the last item in the list. If we provide theindexas an argument, it removes the item at the given position in the list and returns it. Note: It is optional to provide an argument here.

# Without providing index position as an argument. Returns and removes the last element in the list.
In [74]: stock_list.pop()
Out[74]: 'NLFX'
In [75]: stock_list
Out[75]: ['HP', 'GOOG', 'MSFT', 'AMZN', 'TSLA', 'GE']

# Providing an index position as an argument. Returns and removes the element from the specific location. In [76]: stock_list.pop(2) Out[76]: 'MSFT' In [77]: stock_list Out[77]: ['HP', 'GOOG', 'AMZN', 'TSLA', 'GE']

index(element): Returns the index of the first item whose value iselementprovided in an argument. Python will throw an error if there is no such item.

In [78]: stock_list.index('GOOG')
Out[78]: 1
In [79]: stock_list.index('GE')
Out[79]: 4

count(element): Returns the number of timeselementappears in the list.

# Count the element 'GOOG'
In [80]: stock_list.count('GOOG')
Out[80]: 1
# Appending the same list with 'GOOG'
In [81]: stock_list.append('GOOG')
In [82]: stock_list
Out[82]: ['HP', 'GOOG', 'AMZN', 'TSLA', 'GE', 'GOOG']
# Again, counting the element 'GOOG'
In [83]: stock_list.count('GOOG')
Out[83]: 2

sort(): When called, this method returns the sorted list. The sort operation will be in place.

# Sorting the list. The same list will be updated.
In [84]: stock_list.sort()
In [85]: stock_list
Out[85]: ['AMZN', 'GE', 'GOOG', 'GOOG', 'HP', 'TSLA']

reverse(): This method reverses the elements of the list and the operation performed will be in place.

# Reversing the elements within the list.
In [86]: stock_list.reverse()
In [87]: stock_list
Out[87]: ['TSLA', 'HP', 'GOOG', 'GOOG', 'GE', 'AMZN']

Stacks and Queues

The list methods make it very easy to use a list as a stack or queue. Astackis one of the python data structures (though not available directly in Python) where the last element added is the first element retrieved, also known asLast In, First Out (LIFO). A list can be used as a stack using theappend()andpop()method. To add an item to the top of the stack, we use theappend()and to retrieve an item from the top of the stack, we use thepop()without an explicit index. We will see some examples in this python data structures tutorial now:

# (Bottom) 1 -> 5 -> 6 (Top)
In [88]: stack = [1, 5, 6]
In [89]: stack.append(4) # 4 is added on top of 6 (Top)
In [90]: stack.append(5) # 5 is added on top of 4 (Top)
In [91]: stack
Out[91]: [1, 5, 6, 4, 5]
In [92]: stack.pop() # 5 is removed from the top
Out[92]: 5
In [93]: stack.pop() # 4 is removed from the top
Out[93]: 4
In [94]: stack.pop() # 6 is removed from the top
Out[94]: 6
In [95]: stack # Remaining elements in the stack
Out[95]: [1, 5]

Another one of the python data structures that can be built using list methods isqueue, where the first element added is the first element retrieved, also known asFirst In, First Out (FIFO). Consider a queue at a ticket counter where people are catered according to their arrival sequence and hence the first person to arrive is also the first to leave.

In order to implement a queue, we need to use thecollections.dequemodule; however, lists python data structures are not efficient for this purpose as it involves heavy memory usage to change the position of every element with each insertion and deletion operation.

It can be created using theappend()andpopleft()methods. For example,

# Import 'deque' module from the 'collections' package
In [96]: from collections import deque
# Define initial queue
In [97]: queue = deque(['Perl', 'PHP', 'Go'])
In [98]: queue.append('R') # 'R' arrives and joins the queue
In [99]: queue.append('Python') # 'Python' arrives and joins the queue
In [100]: queue.popleft() # The first to arrive leaves the queue
Out[100]: 'Perl'
In [101]: queue.popleft() # The second to arrive leaves the queue
Out[101]: 'PHP'
In [102]: queue # The remaining queue in order of arrival
Out[102]: deque(['Go', 'R', 'Python'])

Dictionaries

In python data structures, a dictionary is an unordered collection of items. It stores data inkey-valuepairs. A dictionary is like a phone-book where we can find the phone numbers or contact details of a person by knowing only his/her name i.e. we associate names(keys)with corresponding details(values). Note that the keys must be unique just like the way it is in a phone book i.e. we cannot have two persons with the exact same name.

In dictionary python data structures, pairs of keys and values are specified within curly brackets{}using the following notation:

dictionary = {key1 : value1, key2 : value2, key3 : value3}

Notice that the key-value pairs are separated by the colon:and pairs themselves are separated by,. Also, we can use only immutable objects like strings and tuples for the keys of a dictionary. Values of a dictionary can be either mutable or immutable objects. Dictionaries python data structures that we create are instances of thedictclass and they are unordered, so the order that keys are added doesn't necessarily reflect the same order when they are retrieved back.

Creating and accessing dictionaries

A dictionary can be created either using the curly brackets{}or the methoddict(). For example:

# Creating an empty dictionary using {}
In [103]: tickers = {}
In [104]: type(tickers)
Out[104]: dict
# Creating an empty dictionary using the dict() method
In [105]: tickers = dict()
In [106]: type(tickers)
Out[106]: dict

Let us create a dictionary with values of the same data type.

In [107]: tickers = {'GOOG' : 'Alphabet Inc.',
 ...: 'AAPL' : 'Apple Inc.',
 ...: 'MSFT' : 'Microsoft Corporation'}
In [108]: tickers
Out[108]:
{'GOOG': 'Alphabet Inc.',
 'AAPL': 'Apple Inc.',
 'MSFT': 'Microsoft Corporation'}

Next, we will create a dictionary with multiple data types.

In [109]: ticker = {'symbol' : 'AAPL',
 ...: 'price' : 224.95,
 ...: 'company' : 'Apple Inc',
 ...: 'founded' : 1976,
 ...: 'products' : ['Machintosh', 'iPod', 'iPhone', 'iPad']}

We can also provide a dictionary as a value to another dictionary key. Such a dictionary is called anested dictionary. Take a look at below example:

In [110]: tickers = {'AAPL' : {'name' : 'Apple Inc.',
 ...: 'price' : 224.95
 ...: },
 ...: 'GOOG' : {'name' : 'Alphabet Inc.',
 ...: 'price' : 1194.64
 ...: }
 ...: }

Keys in a dictionary should be unique. If we supply the same key for multiple pairs, Python will ignore the previous value associated with the key and only the recent value will be stored. Consider the following example:

In [111]: same_keys = {'symbol' : 'AAPL',
 ...: 'symbol' : 'GOOG'}
In [112]: same_keys
Out[112]: {'symbol': 'GOOG'}

In the above example, Python discarded the valueAAPLand retained the latest value assigned to the same key. Once we have created dictionaries python data structures, we can access them with the help of the respective keys. We use the slice operator[]to access the values; however, we supply akeyto obtain its value. With the dictionaries created above, we can access values in the following manner:

In [113]: ticker
Out[113]:
{'symbol': 'AAPL',
 'price': 224.95,
 'company': 'Apple Inc',
 'founded': 1976,
 'products': ['Machintosh', 'iPod', 'iPhone', 'iPad']}
In [114]: tickers
Out[114]:
{'AAPL': {'name': 'Apple Inc.', 'price': 224.95},
 'GOOG': {'name': 'Alphabet Inc.', 'price': 1194.64}}
# Accessing the symbol name
In [115]: ticker['symbol']
Out[115]: 'AAPL'
# Accessing the ticker price
In [116]: ticker['price']
Out[116]: 224.95
# Accessing the product list
In [117]: ticker['products']
Out[117]: ['Machintosh', 'iPod', 'iPhone', 'iPad']
# Accessing the item at position 2 in the product list.
In [118]: ticker['products'][2]
Out[118]: 'iPhone'
# Accessing the first nested dictionary from the 'tickers' dictionary
In [119]: tickers['AAPL']
Out[119]: {'name': 'Apple Inc.', 'price': 224.95}
# Accessing the price of 'GOOG' ticker using chaining operation
In [120]: tickers['GOOG']['price']
Out[120]: 1194.64

Altering dictionaries

A value in a dictionary python data structures can be updated by assigning a new value to its corresponding key using the assignment operator=.

In [121]: ticker['price']
Out[121]: 224.95
In [122]: ticker['price'] = 226
In [123]: ticker['price']
Out[123]: 226

A new key-value pair can also be added in a similar fashion. To add a new element, we write the newkeyinside the square brackets[]and assign a new value. For example:

In [124]: ticker['founders'] = ['Steve Jobs', 'Steve Wozniak', 'Ronald Wayne']
In [125]: ticker
Out[125]:
{'symbol': 'AAPL',
 'price': 226,
 'company': 'Apple Inc',
 'founded': 1976,
 'products': ['Machintosh', 'iPod', 'iPhone', 'iPad'],
 'founders': ['Steve Jobs', 'Steve Wozniak', 'Ronald Wayne']}

In the above example, we add the keyfoundersand assign the list['Steve Jobs', 'Steve Wozniak', 'Ronald Wayne']as value. If we are to delete any key-value pair in the dictionary python data structures, we use the built-indel()function as follows:

In [126]: del(ticker['founders'])
In [127]: ticker
Out[127]:
{'symbol': 'AAPL',
 'price': 226,
 'company': 'Apple Inc',
 'founded': 1976,
 'products': ['Machintosh', 'iPod', 'iPhone', 'iPad']}

Dictionary Methods

Thedictclass provides various methods using which we can perform a variety of operations. In addition to these methods, we can use built-inlen()functions to get the length of a dictionary.

In [128]: len(ticker)
Out[128]: 5
In [129]: len(tickers)
Out[129]: 2

Now we discuss some of the popular methods provided by thedictclass in python data structures.

items(): This method returns an object containing all times in the calling object.

In [130]: ticker.items()
Out[130]: dict_items([('symbol', 'AAPL'), ('price', 226), ('company', 'Apple Inc'), ('founded', 1976), ('products', ['Machintosh', 'iPod', 'iPhone', 'iPad'])])

keys(): This method returns all keys in the calling dictionary.

In [131]: ticker.keys()
Out[131]: dict_keys(['symbol', 'price', 'company', 'founded', 'products'])

values(): This method returns all values in the calling object.

In [132]: ticker.values()
Out[132]: dict_values(['AAPL', 224.95, 'Apple Inc', 1976, ['Machintosh', 'iPod', 'iPhone', 'iPad']])

pop(): This python data structures method pops the item whose key is given as an argument.

In [133]: tickers
Out[133]:
{'GOOG': 'Alphabet Inc.',
 'AAPL': 'Apple Inc.',
 'MSFT': 'Microsoft Corporation'}
In [134]: tickers.pop('GOOG')
Out[134]: 'Alphabet Inc.'
In [135]: tickers
Out[135]: {'AAPL': 'Apple Inc.', 'MSFT': 'Microsoft Corporation'}

copy(): As the name suggests, this python data structures method copies the calling dictionary to another dictionary.

In [136]: aapl = ticker.copy()
In [137]: aapl
Out[137]:
{'symbol': 'AAPL',
 'price': 224.95,
 'company': 'Apple Inc',
 'founded': 1976,
 'products': ['Machintosh', 'iPod', 'iPhone', 'iPad']}

clear(): This method empties the calling dictionary.

In [138]: ticker.clear()
In [139]: ticker
Out[139]: {}

update(): This method allows adding new key-pair value from another dictionary.

In [140]: ticker1 = {'NLFX' : 'Netflix'}
In [141]: ticker2 = {'AMZN' : 'Amazon'}
In [142]: new_tickers = {}
In [143]: new_tickers.update(ticker1)
In [144]: new_tickers.update(ticker2)
In [145]: new_tickers
Out[145]: {'NLFX': 'Netflix', 'AMZN': 'Amazon'}

In python data structures, a set is an unordered and unindexed collection of items. It is a collection data type which is mutable, iterable and contains no duplicate values. A set in Python represents the mathematical notion of a set.

In Python data structures, sets are written using the curly brackets in the following way:

In [146]: universe ={'GOOG', 'AAPL', 'NLFX', 'GE'}
In [147]: universe
Out[147]: {'AAPL', 'GE', 'GOOG', 'NLFX'}

We cannot access items in a set by referring to an index (slicing operation), since sets are unordered the item has no index. But we can loop through all items using theforloop.

Once a set is created, we cannot change its items, but we can add new items using theadd()method.

In [148]: universe.add('AMZN')
In [149]: universe
Out[149]: {'AAPL', 'AMZN', 'GE', 'GOOG', 'NLFX'}

Python won't add the same item again nor will it throw any error.

In [150]: universe.add('AMZN')
In [151]: universe.add('GOOG')
In [152]: universe
Out[152]: {'AAPL', 'AMZN', 'GE', 'GOOG', 'NLFX'}

In order to add multiple items in sets python data structures, we use theupdate()method with new items to be added within a list.

In [153]: universe.update(['FB', 'TSLA'])
In [154]: universe
Out[154]: {'AAPL', 'AMZN', 'FB', 'GE', 'GOOG', 'NLFX', 'TSLA'}

We can use the inbuiltlen()function to determine the length of a set.

In [155]: len(universe)
Out[155]: 7

To remove or delete an item, we can use theremove()ordiscard()sets python data structures methods. For example,

In [156]: universe.remove('FB')
In [157]: universe.discard('TSLA')
In [158]: universe
Out[158]: {'AAPL', 'AMZN', 'GE', 'GOOG', 'NLFX'}

If we try to remove an item using theremove()which is not present in the set, Python will throw an error.

In [159]: universe.remove('FB')
Traceback (most recent call last):
 File "<ipython-input-159-3a137a1e6cce>", line 1, in <module>
 universe.remove('FB')
KeyError: 'FB'

Thediscard()method will not throw any error if we try to discard an item which is not present in the set.

In [160]: universe
Out[160]: {'AAPL', 'AMZN', 'GE', 'GOOG', 'NLFX'}
In [161]: universe.discard('FB')

We use theclear()method to empty the set.

In [162]: universe.clear()
In [163]: universe
Out[163]: set()

Following the mathematical notation, we can perform set operations such as union, intersection, difference, etc. in Python using the set. Let us look at some examples in the python data structures tutorial:

We define two setstech_stocksandfin_stocksas follows:

In [164]: tech_stocks = {'AMD', 'GOOG', 'AAPL', 'WDC'}
In [165]: fin_stocks = {'BAC', 'BMO', 'JPLS'}

union()method: Thissetspython data structures method allows performing a union between sets. This operation returns all elements within both sets.

# Performs the 'union` operation
In [166]: universe = tech_stocks.union(fin_stocks)
In [167]: universe
Out[167]: {'AAPL', 'AMD', 'BAC', 'BMO', 'GOOG', 'JPLS', 'WDC'} # 'universe' contains all elements of both sets

intersection()method: Thissetspython data structures method performs the intersection between sets. It returns only elements which are available in both sets.

In [168]: universe.intersection(fin_stocks)
Out[168]: {'BAC', 'BMO', 'JPLS'} # Only elements present in the 'universe' set and 'fin_stocks` are returned

difference()method: This sets python data structures method performs the difference operation and returns a set containing all elements of the calling object but not including elements of the second set.

In [169]: universe.difference(fin_stocks)
Out[169]: {'AAPL', 'AMD', 'GOOG', 'WDC'} # All elements of the 'universe' set is returned except elements of the 'fin_stock'

issubset()method: This sets python data structures method checks whether all elements of the calling set is present within a second set or not. It returns true if the calling set is a subset of the second set, false otherwise.

In [170]: fin_stocks.issubset(universe) # True, as the 'universe' contains all elements of the 'fin_stocks'
Out[170]: True
In [171]: universe.issubset(tech_stocks) # Can you guess why it resulted in to False?
Out[171]: False

isdisjoint()method: This sets python data structures method checks for the intersection between two sets. It returns true if the calling set is disjoint and not intersected with the second set, false otherwise.

In [172]: fin_stocks.isdisjoint(tech_stocks) # True, none of the set contains any element of each other
Out[172]: True
In [173]: fin_stocks.isdisjoint(universe) # False, the 'universe' set contains elements of the 'fin_stocks' set
Out[173]: False

issuperset()method: This sets python data structures method checks whether the calling set contains all elements of the second set. It returns true if the calling set contains all elements of the second set, false otherwise.

In [174]: universe.issuperset(fin_stocks) # True, the 'universe' set contains all elements of the 'fin_stocks'
Out[174]: True
In [175]: universe.issuperset(tech_stocks) # True, the 'universe' set contains all elements of the 'tech_stocks'
Out[175]: True
In [176]: fin_stocks.issuperset(universe) # False, the 'fin_stocks' set does not contains all elements of the 'universe' set
Out[176]: False

Conclusion

In this python data structures tutorial, we understood that they are the fundamental building blocks for writing programs. We also learned about arrays, lists, tuples, dictionaries and sets. Apart from their uses, we have looked at the different operations that can be performed on these python data structures.

To reiterate, the Python data structures tutorial is an excerpt from thePython Basics Handbook, which was created for both; beginners who are starting out inPythonas well as accomplished traders who can use it as a handy reference while coding their strategy.

Do let us know if you loved the article and any other feedback in the comments below.

Disclaimer:All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
