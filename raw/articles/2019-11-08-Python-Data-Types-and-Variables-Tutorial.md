---
title: "Python Data Types and Variables Tutorial"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-data-types-variables-tutorial/"
date: "2019-11-08"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Data Types and Variables Tutorial

**来源**: [QuantInsti](https://blog.quantinsti.com/python-data-types-variables-tutorial/)  
**日期**: 2019-11-08  
**作者**: QuantInsti

---

## 原文

Python Data Types and Variables Tutorial

ByJay Parmar

In simple terms, variables can be thought of as a container with a name that is used to hold the value. A variable can take data in various formats such as a string, an integer, a number with fractional parts (float), etc. These formats mentioned earlier are called data types.

It is now time to look at each of these concepts in greater detail. We will go through python variables and python data types in more detail further in this blog. This blog article is an excerpt from thePython Basics Handbookcreated for the simple purpose of making the reader understand the beauty and simplicity of thePython language.

We will cover the following topics in this blog.

Python Variables

Python Data Types

Python Data Type Conversion

Python Variables

In programming parlance, a python variable is a reserved memory location to store values. In other words, a variable in a Python program gives necessary data to a computer for processing.

In this section, we will learn about python variables and their types. Let start by creating a variable.

Variable Declaration and Assignment

In Python, variables need NOT be declared or defined in advance, as is the case in many other programming languages. In fact, Python has no command for declaring a variable. To create a python variable, we assign a value to it and start using it. An assignment is performed using a single equal sign=a.k.a. Assignment operator. A python variable is created the moment we assign the first value to it.

# Creating a variable
In [1]: price = 226

The above statement can be interpreted as a python variablepriceis assigned a value226. It is also known asinitializingthe variable. Once this statement is executed, we can start using thepricein other statements or expressions, and its value will be substituted. For example,

In [2]: print(price)
226 # Output

Later, if we change the value ofpriceand run theprintstatement again, the new value will appear as output. This is known asre-declarationof the python variable.

In [3]: price = 230 # Assigning new value
In [4]: print(price) # Printing price
230 # Output

We can also chain assignment operation to python variables, which makes it possible to assign the same value to multiple variables simultaneously.

In [5]: x = y = z = 200 # Chaining assignment operation
In [6]: print(x, y, z) # Printing all variables
200 200 200 # Output

The chained assignment shown in the above example assigns the value200to python variablesx,y, andzsimultaneously.

Python Variable Naming Conventions

We use python variables everywhere in Python. A python variable can have a short name or more descriptive name. The following list of rules should be followed for naming a variable.

A python variable name must start with a letter or the underscore character.stock = 'AAPL' # Valid name
_name = 'AAPL' # Valid name

A python variable name must start with a letter or the underscore character.

stock = 'AAPL' # Valid name
_name = 'AAPL' # Valid name

A python variable name cannot start with a number.1stock = 'AAPL' # Invalid name
1_stock = 'AAPL' # Invalid name

A python variable name cannot start with a number.

1stock = 'AAPL' # Invalid name
1_stock = 'AAPL' # Invalid name

A python variable name can only contain alpha-numeric characters (A-Z, a-z, 0-9) and underscores ( _ ).Stock = 'AAPL' # Valid name. It starts with a capital letter.
stock_price = 226.41 # Valid name. It is a combination of alphabets and the underscore.
stock_1 = 'AAPL' # Valid name. It is a combination of alphabets and a number.
Stock_name_2 = 'MSFT' # Valid name. It is a combination of a capital letter, alphabets and a number.

A python variable name can only contain alpha-numeric characters (A-Z, a-z, 0-9) and underscores ( _ ).

Stock = 'AAPL' # Valid name. It starts with a capital letter.
stock_price = 226.41 # Valid name. It is a combination of alphabets and the underscore.
stock_1 = 'AAPL' # Valid name. It is a combination of alphabets and a number.
Stock_name_2 = 'MSFT' # Valid name. It is a combination of a capital letter, alphabets and a number.

A python variable name cannot contain whitespace and signs such as +, -, etc.stock name = 'AAPL' # Invalid name. It cannot contain the whitespace.
stock-name = 'AAPL' # Invalid name. It cannot contain characters other than the underscore ( _ ).

A python variable name cannot contain whitespace and signs such as +, -, etc.

stock name = 'AAPL' # Invalid name. It cannot contain the whitespace.
stock-name = 'AAPL' # Invalid name. It cannot contain characters other than the underscore ( _ ).

Python Variable names are case-sensitive.STOCK = 'AAPL'
stock = 'MSFT'
Stock = 'GOOG'
# STOCK, stock and Stock all three are different variable names.Remember thatvariable names are case-sensitivein Python.

Python Variable names are case-sensitive.

STOCK = 'AAPL'
stock = 'MSFT'
Stock = 'GOOG'
# STOCK, stock and Stock all three are different variable names.

Remember thatvariable names are case-sensitivein Python.

Remember thatvariable names are case-sensitivein Python.

Python keywords cannot be used as a variable name.str = 'AAPL' # Invalid name.
is = 'A Variable' # Invalid name.
for = 'Dummy Variable' # Invalid name.
# 'str', 'is', and 'for' cannot be used as the variable name as they are reserved keywords in Python.

Python keywords cannot be used as a variable name.

str = 'AAPL' # Invalid name.
is = 'A Variable' # Invalid name.
for = 'Dummy Variable' # Invalid name.
# 'str', 'is', and 'for' cannot be used as the variable name as they are reserved keywords in Python.

The following points arede factopractices followed by professional programmers.

Use a name that describes the purpose, instead of using dummy names. In other words, it should be meaningful.a = 18 # Valid name but the variable does not describe the purpose.
age = 18 # Valid name which describes it suitably

Use a name that describes the purpose, instead of using dummy names. In other words, it should be meaningful.

a = 18 # Valid name but the variable does not describe the purpose.
age = 18 # Valid name which describes it suitably

Use an underscore character_to separate two words.stockname = 'AAPL' # Valid name.
stock_name = 'AAPL' # Valid name. And it also provides concise readability.

Use an underscore character_to separate two words.

stockname = 'AAPL' # Valid name.
stock_name = 'AAPL' # Valid name. And it also provides concise readability.

Start a variable name with a small alphabet letter.Stock_name = 'AAPL' # Valid name.
stock_name = 'AAPL' # Valid name. Additionally, it refers to uniformity with other statements.

Start a variable name with a small alphabet letter.

Stock_name = 'AAPL' # Valid name.
stock_name = 'AAPL' # Valid name. Additionally, it refers to uniformity with other statements.

Adhering to these rules increases readability of code. Remember these are good coding practices (and recommended but by no means necessary to follow) which you can carry with you to any programming language, not just Python.

Adhering to these rules increases readability of code. Remember these are good coding practices (and recommended but by no means necessary to follow) which you can carry with you to any programming language, not just Python.

Python Data Types

Having understood what variables are and how they are used to store values, it is time to learn data types of values that python variables hold. We will learn about primitive python data types such as numeric, string and boolean that are built into Python. Python has four basic data types:

Integer

String

Boolean

We will cover these python data types in greater detail below:

Integer

In python data types, an integer can be thought of as a numeric value without any decimal. In fact, it is used to describe anywhole numberin Python such as7,256,1024, etc. We use an integer value to represent a numeric data from negative infinity to infinity. Such numeric numbers are assigned to python variables using an assignment operator.

total_output_of_dice_roll = 6
days_elapsed = 30
total_months = 12
year = 2019

We assign a whole number6to a variabletotal_output_of_dice_rollas there can be no fractional output for a dice roll. Similarly, we have a variabledays_elapsedwith value30,total_monthshaving a value12, andyearas2019.

In python data types, a float stands forfloating point numberwhich essentially means a number with fractional parts. It can also be used for rational numbers, usually ending with a decimal such as6.5,100.1,123.45, etc. Below are some python data types examples where a float value is more appropriate rather than an integer.

stock_price = 224.61
height = 6.2
weight = 60.4

From the statistics perspective, a float value can be thought of as a continuous value, whereas an integer value can correspondingly be a discrete value.

From the statistics perspective, a float value can be thought of as a continuous value, whereas an integer value can correspondingly be a discrete value.

By doing so, we get a fairly good idea how python data types and python variable names go hand in hand. This, in turn, can be used in expressions to perform any mathematical calculation.

Let's tryPython as a Calculatorvery briefly using variables.

# Assign an integer value
In [7]: x = 2
# Assign a float value
In [8]: y = 10.0
# Addition
In [9]: print(x + y)
Out[9]: 12.0
# Subtraction
In [10]: print(x - y)
Out[10]: -8.0
# Multiplication
In [11]: print(x * y)
Out[11]: 20.0
# Division
In [12]: print(x / y)
Out[12]: 0.2
# Modulo
In [13]: print(x % y)
Out[13]: 2.0
# Exponential / Power
In [14]: print(x ** y)
Out[14]: 1024.0

Please note the precise use ofcommentsused in the code snippet to describe the functionality. Also, note thatoutputof all expressions to befloatnumber as one of the literals used in the input is a float value.

Please note the precise use ofcommentsused in the code snippet to describe the functionality. Also, note thatoutputof all expressions to befloatnumber as one of the literals used in the input is a float value.

Look at the above-mentioned examples of python data types and try to understand the code snippet. If you are able to get a sense of what's happening, that's great. You are well on track on this python data types journey. Nevertheless, let's try to understand the code just to get more clarity. Here, we assign an integer value of2toxand a float value of10.0toy. Then, we try to attempt various mathematical operations on these defined variables instead of using direct values. The obvious benefit is the flexibility that we get by using these python variables. For example, think of a situation where we want to perform the said operation on different values such as3and15.0, we just need to re-declare variablesxandywith new values respectively, and the rest of the code remains as it is.

Boolean

This built-in python data type can have one of two values,TrueorFalse. We use an assignment operator=to assign a boolean value to variables in a manner similar to what we have seen for integer and float values. For example:

In [15]: buy = True
In [16]: print(buy)
Out[16]: True
In [17]: sell = False
In [18]: print(sell)
Out[18]: False

Expressions in Python are often evaluated in the boolean context, meaning they are interpreted to represent their truth value. Boolean expressions are extensively used in logical conditions and control flow statements. Consider the following examples

# Checking for equality between 1 and itself using comparison operator '=='
In [19]: 1 == 1
Out[19]: True
# Checking for equality between values 1 and -1
In [20]: 1 == -1
Out[20]: False
# Comparing value 1 with -1
In [21]: 1 > -1
Out[21]: True

The above python data types examples are some of the simplest boolean expressions that evaluate to eitherTrueorFalse.

We do NOT writeTrueandFalsewithin quotes. It needs to be written without quotes. Also, the first letter needs to be upper case followed by lower case letters. The following list will not be evaluated to a boolean value'TRUE'TRUEtrue'FALSE'FALSEfalse

We do NOT writeTrueandFalsewithin quotes. It needs to be written without quotes. Also, the first letter needs to be upper case followed by lower case letters. The following list will not be evaluated to a boolean value

'TRUE'

'FALSE'

String

In python data types, a string is a collection of alphabets, numbers, and other characters written within a single quote'or double quotes". In other words, it is a sequence of characters within quotes. Let us understand how a string works with the help of some examples.

# Variable assignment with a string
In [22]: sample_string = '1% can also be expressed as 0.01'
# Print the variable sample_string
In [23]: sample_string
Out[23]: '1% can also be expressed as 0.01'

In the above python data types examples we have defined a string variable with namesample_stringassigned a value'1% can also be expressed as 0.01'. It is interesting to note here that we have used a combination of alphabets, numbers and special characters for defining the variable. In Python, anything that goes within quotes is a string. Consider the following example,

In [24]: stock_price = '224.61'
In [25]: stock_price
Out[25]: '224.61'

We define the variablestock_priceassigning the string value'224.61'. The interesting thing to notice is the output of the variable is also a string. Python will not convert the python data types implicitly whenever numeric values are given as a string.

We can concatenate two or more string using the+operator.

In [26]: 'Price of AAPL is ' + stock_price
Out[26]: 'Price of AAPL is 224.61'

Concatenation operation using the+operator works only on a string. It does not work with different python data types. If we try to perform the operation, we will be presented with an error.

In [27]: stock_price = 224.61 # Re-declaring the variable with an integer value
In [28]: 'Price of AAPL is ' + stock_price # Error line
Traceback (most recent call last):
 File "<ipython-input-28-1c5964ef305c>", line 1, in <module>
 'Price of AAPL is ' + stock_price
TypeError: must be str, not float

As expected, Python spat out aTypeErrorwhen we tried concatenating a string and float literal. Similar to the+operator, we can use the*operator with a string literal to produce the same string multiple times.

In [29]: string = 'Python! '
In [30]: string * 3
Out[30]: 'Python! Python! Python! '

In python data types, we can select a substring or part of a string using the slice operation. Slicing is performed using the square brackets[]. The syntax for slicing a single element from the string is[index]which will return an element atindex. The index refers to the position of each element in a string and it begins with 0, which keeps on increasing in chronological order for every next element.

In [29]: string = 'EPAT Handbook!'
In [30]: string[0] # 0 refers to an element E
Out[30]: 'E'
In [31]: string[1] # 1 refers to an element P
Out[31]: 'P'

In the above python data types example, an elementEbeing the first character belongs to an index0,Pbeing next toEbelongs to an index1, and so on. Similarly, the index for elementbwill be9. Can you guess the index for elementkin the above example?

To slice a substring from a string, the syntax used is[start index:end index]which will return the substring starting from an element atstart indexup to but not including an element atend index. Consider the following python data types example, where we substring the string from an index0up to4which yields the output'EPAT'. Notice how the element' 'at an index4is not included in the output. Similarly, we slice a substring as seen in the below python data types example.

In [32]: string[0:4]
Out[32]: 'EPAT'
In [33]: string[4]
Out[33]: ' '
In [34]: string[5:13]
Out[34]: 'Handbook'
In [35]: string[13]
Out[35]: '!'

In Python, we cannot perform the slicing operation with an index not present in the string. Python will throwIndexErrorwhenever it encounters slicing operation with incorrect index.

In [36]: string[14]
Traceback (most recent call last):
 File "<ipython-input-36-6a6fe155a0da>", line 1, in <module>
 string[14]
IndexError: string index out of range

In the above python data types example, the last index is13. The slicing operation performed with an index14will result in an errorIndexErrorstating that index we are looking for is not present.

We list out some of the important points for string literals below:In Python 3.x all strings areUnicodeby default.A string can be written within either''or"". Both work fine.Strings are immutable. (although you can modify the variable)An escape sequence is used within a string to mark a new line, provide tab space, writing\character, etc.

We list out some of the important points for string literals below:

In Python 3.x all strings areUnicodeby default.

A string can be written within either''or"". Both work fine.

Strings are immutable. (although you can modify the variable)

An escape sequence is used within a string to mark a new line, provide tab space, writing\character, etc.

Operations on String

In this section of python data types, we discuss some of the most common string methods. A method is like a function, but it runsonan object. If the variablesample_stringis a string, then the codesample_string.upper()runs theupper()method on that string object and returns the result(this idea of running a method on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Some methods also take an argument as a parameter. We provide a parameter to a method as an argument within parentheses.

upper()method: This method returns the upper case version of the string. The python data types example is as follows:In [37]: sample_string.upper()
Out[37]: 'EPAT HANDBOOK!'

upper()method: This method returns the upper case version of the string. The python data types example is as follows:

In [37]: sample_string.upper()
Out[37]: 'EPAT HANDBOOK!'

lower()method: This method returns the lower case version of the string. The python data types example is as follows:In [38]: sample_string.lower()
Out[38]: 'epat handbook!'

lower()method: This method returns the lower case version of the string. The python data types example is as follows:

In [38]: sample_string.lower()
Out[38]: 'epat handbook!'

strip()method: This method returns a string with whitespace removed from the start and end. The python data types example is as follows:In [39]: ' A string with whitespace at both the ends. '.strip()
Out[39]: 'A string with whitespace at both the ends.'

strip()method: This method returns a string with whitespace removed from the start and end. The python data types example is as follows:

In [39]: ' A string with whitespace at both the ends. '.strip()
Out[39]: 'A string with whitespace at both the ends.'

isalpha()method: This method returns the boolean valueTrueif all characters in a string are letters,Falseotherwise. The python data types example is as follows:

isalpha()method: This method returns the boolean valueTrueif all characters in a string are letters,Falseotherwise. The python data types example is as follows:

In [40]: 'Alphabets'.isalpha()
Out[40]: True
In [41]: 'This string contains only alphabets'.isalpha()
Out[41]: False # The string under evaluation contains whitespace.

isdigit()method: This method returns the boolean valueTrueif all characters in a string are digits,Falseotherwise. The python data types example is as follows:In [42]: '12345'.isdigit()
Out[42]: True

isdigit()method: This method returns the boolean valueTrueif all characters in a string are digits,Falseotherwise. The python data types example is as follows:

In [42]: '12345'.isdigit()
Out[42]: True

startswith(argument)method: This method returns the boolean valueTrueif the first character of a string starts with the character provided as an argument,Falseotherwise. The python data types example is as follows:In [43]: 'EPAT Handbook!'.startswith('E')
Out[43]: True

startswith(argument)method: This method returns the boolean valueTrueif the first character of a string starts with the character provided as an argument,Falseotherwise. The python data types example is as follows:

In [43]: 'EPAT Handbook!'.startswith('E')
Out[43]: True

endswith(argument)method: This method returns the boolean valueTrueif the last character of a string ends with the character provided as an argument,Falseotherwise. The python data types example is as follows:In [44]: 'EPAT Handbook!'.startswith('k')
Out[44]: False # String ends with the '!' character.

endswith(argument)method: This method returns the boolean valueTrueif the last character of a string ends with the character provided as an argument,Falseotherwise. The python data types example is as follows:

In [44]: 'EPAT Handbook!'.startswith('k')
Out[44]: False # String ends with the '!' character.

find(sub, start, end)method: This method returns the lowest index in a string where substringsubis found within the slice[start:end]. Here, argumentsstartandendare optional. It returns-1ifsubis not found. The python data types example is as follows:

find(sub, start, end)method: This method returns the lowest index in a string where substringsubis found within the slice[start:end]. Here, argumentsstartandendare optional. It returns-1ifsubis not found. The python data types example is as follows:

In [45]: 'EPAT Handbook!'.find('EPAT')
Out[45]: 0
In [46]: 'EPAT Handbook!'.find('A')
Out[46]: 2 # First occurrence of 'A' is at index 2.
In [47]: 'EPAT Handbook!'.find('Z')
Out[47]: -1 # We do not have 'Z' in the string.

replace(old, new)method: This method returns a copy of the string with all occurrences ofoldreplace bynew. The python data types example is as follows:

Out[48]: '00 01 10 11'.replace('0', '1')
Out[48]: '11 11 11 11' # Replace 0 with 1
In [49]: '00 01 10 11'.replace('1', '0')
Out[49]: '00 00 00 00' # Replace 1 with 0

split(delim)method: This method is used to split a string into multiple strings based on thedelimargument. The python data types example is as follows:

In [50]: 'AAPL MSFT GOOG'.split(' ')
Out[50]: ['AAPL', 'MSFT', 'GOOG']

Here, the Python outputs three strings in a single data structure calledList. The python data types example is as follows:

index(character)method: This method returns the index of the first occurrence of thecharacter. The python data types example is as follows:

In [51]: 'EPAT Handbook!'.index('P')
Out[51]: 1

Python will provide an error if the character provided as an argument is not found within the string.

In [52]: 'EPAT Handbook!'.index('Z')
Traceback (most recent call last):
 File "<ipython-input-52-d1b3e87f78be>", line 1, in <module>
 'EPAT Handbook!'.index('Z')
ValueError: substring not found

capitalize()method: This method returns a capitalized version of the string. The python data types example is as follows:

In [53]: 'python is amazing!'.capitalize()
Out[53]: 'Python is amazing!'

count(character)method: This method returns a count of an argument provided bycharacter. The python data types example is as follows:

In [54]: 'EPAT Handbook'.count('o')
Out[54]: 2
In [55]: 'EPAT Handbook'.count('a')
Out[55]: 1

type() function

The inbuilttype(argument)function is used to evaluate the python data types and returns the class type of theargumentpassed as a parameter. This function is mainly used for debugging.

In [56]: type('EPAT Handbook')
Out[56]: str # A string is represented by the class 'str'.
In [57]: type(224.61)
Out[57]: float # A float literal is represented by the class 'float'.
In [58]: type(224)
Out[58]: int # An integer literal is represented by the class 'int'.
In [59]: type('0')
Out[59]: str # An argument provided is within quotation marks. Hence, it is considered as a string object represented by the class 'str'.
In [60]: type(True)
Out[60]: bool # A boolean value is represented by the class 'bool'.
In [61]: type(False)
Out[61]: bool
In [62]: type('False')
Out[62]: str # An argument is provided within a quotation mark.
In [63]: type([1, 2, 3])
Out[63]: list # An object passed as an argument belongs to the class 'list'.
In [64]: type({'key':'value'})
Out[64]: dict # An object passed as an argument belongs to the class 'dict'.
In [65]: type((1, 2, 3))
Out[65]: tuple # An object passed as an argument belongs to the class 'tuple'.
In [66]: type({1, 2, 3})
Out[66]: set # An object passed as an argument belongs to the class 'set'.

Alist,dict,tuple,setare native data structures within Python.

Python Data Type Conversion

We often encounter situations where it becomes necessary to change the python data types of the underlying data. Or maybe we find out that we have been using an integer when what we really need is a float. In such cases, we can convert the python data types of variables. We can check the data type of a variable usingtype()function as seen above.

There can be two types of conversion possible:implicittermed as coercion, andexplicitoften referred to as casting. When we change the type of a variable from one to another, this is calledtypecasting.

Implicit Conversion: This is an automatic type conversion and the Python interpreter handles this on the fly for us. We need not to specify any command or function for same. Take a look at the following python data types example:

In [67]: 8 / 2
Out[67]: 4.0

The division operation performed between two integers8being a dividend and2being a divisor. Mathematically, we expect the output to be4- an integer value, but instead, Python returned the output as4.0- a float value. That is, Python internally converted an integer4to float4.0.

Explicit Conversion: This type of conversion is user-defined. We need to explicitly change the python data types for certain literals to make it compatible for data operations. Let us try to concatenate a string and an integer using the+operator.

In [68]: 'This is the year ' + 2019
Traceback (most recent call last):
 File "<ipython-input-68-2bccd8d1d6de>", line 1, in <module>
 'This is the year ' + 2019
TypeError: must be str, not int

Here we attempted to join a string'This is the year 'and an integer2019. Doing so, Python threw an errorTypeErrorstating incompatible python data types. One way to perform the concatenation between the two is to convert the python data type of2019to string explicitly and then perform the operation. We usestr()to convert an integer to string.

In [68]: 'This is the year ' + str(2019)
Out[68]: 'This is the year 2019'

Similarly, we can explicitly change the python data type of literals in the following manner.

# Integer to Float conversion
In [69]: float(4)
Out[69]: 4.0
# String to Float conversion
In [70]: float('4.2')
Out[70]: 4.2
In [71]: float('4.0')
Out[71]: 4.0
# Float to Integer conversion
In [72]: int(4.0)
Out[72]: 4 # Python will drop the fractional part.
In [73]: int(4.2)
Out[73]: 4
# String to Integer conversion
In [74]: int('4')
Out[74]: 4
# Python does not convert a string literal with a fractional part, and instead, it will throw an error.
In [75]: int('4.0')
Traceback (most recent call last):
 File "<ipython-input-75-a6536d9312a9>", line 1, in <module>
 int('4.0')
ValueError: invalid literal for int() with base 10: '4.0'
# Float to String conversion
In [76]: str(4.2)
Out[76]: '4.2'
# Integer to String conversion
In [77]: str(4)
Out[77]: '4'

In the above example, we have seen how we can change the python data type of literals from one to another. Similarly, the boolean python data type represented byboolis no different. We can typecastbooltointas we do for the rest. In fact, Python internally treats the boolean valueFalseas0andTrueas1.

# Boolean to Integer conversion
In [64]: int(False)
Out[64]: 0
In [65]: int(True)
Out[65]: 1

It is also possible to convert an integer value to boolean value. Python converts0toFalseand rest all integers gets converted toTrue.

# Integer to Boolean conversion
In [78]: bool(0)
Out[78]: False
In [79]: bool(1)
Out[79]: True
In [80]: bool(-1)
Out[80]: True
In [81]: bool(125)
Out[81]: True

Conclusion

Thus, we have familiarized ourselves with python variables, and then went on to define them, understanding python data types, their internal workings, and type conversions.

To reiterate, the Python data types and variables tutorial is an excerpt from thePython Basics Handbook, which was created for both; beginners who are starting out inPythonas well as accomplished traders who can use it as a handy reference while coding their strategy.

Do let us know if you loved the article and any other feedback in the comments below.

Disclaimer:All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
