---
title: "Python Function Tutorial: Definition, Types, Namespace and Scope"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-function-tutorial/"
date: "2019-12-05"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Function Tutorial: Definition, Types, Namespace and Scope

**来源**: [QuantInsti](https://blog.quantinsti.com/python-function-tutorial/)  
**日期**: 2019-12-05  
**作者**: QuantInsti

---

## 原文

Python Function Tutorial: Definition, Types, Namespace and Scope

ByJay Parmar

Today, we will explore a remarkably handy feature seen in almost all programming languages: functions. There are lots of fantastic in-built functions in Python and its ecosystem. However, often, we as a Python programmer need to write custom functions to solve problems that are unique to our needs. Here is the definition of a function.

A function is a block of code(that performs a specific task) which runs only when it is called.

From the definition, it can be inferred that writing such block of codes, i.e. functions, provides benefits such as

Reusability: Code written within a python function can be called as and when needed. Hence, the same code can be reused thereby reducing the overall number of lines of code.

Modular Approach: Writing a python function implicitly follows a modular approach. We can break down the entire problem that we are trying to solve into smaller chunks, and each chunk, in turn, is implemented via a function.

We will go through the following points in this python functions tutorial:

Built-in python functions

User defined python functions

Variable Namespace and Scope

Lambda python functions

Python functions can be thought of as building blocks while writing a program, and as our program keeps growing larger and more intricate, functions help make it organized and more manageable. They allow us to give a name to a block of code, allowing us to run that block using the given name anywhere in a program any number of times. This is referred to ascallinga python function. For example, if we want to compute the length of a list, we call a built-inlenfunction. Using any python function means we are calling it to perform the task for which it is designed.

We need to provide an input to thelenfunction while calling it. The input we provide to the python function is called anargument. It can be a data structure, string, value or a variable referring to them. Depending upon the functionality, a function can take single or multiple arguments.

There are three types of python functions:

Built-in python functions such asprintto print on the standard output device,typeto check data type of an object, etc. These are the functions that Python provides to accomplish common tasks.

User-Defined python functions: As the name suggests these are custom functions to help/resolve/achieve a particular task.

Anonymous python functions, also known as lambda functions are custom-made without having any name identifier.

Built-in python functions

Built-in functions are the ones provided by Python. We will go through a few of them now:

type(object)is used to check the data type of anobject.

type(object)is used to check the data type of anobject.

float([value])returns a floating point number constructed from a number or stringvalue.

float([value])returns a floating point number constructed from a number or stringvalue.

int([value])returns an integer object constructed from a float or stringvalue, or return 0 if no arguments are given.

int([value])returns an integer object constructed from a float or stringvalue, or return 0 if no arguments are given.

round(number[, ndigits])is used to round a floatnumberup to digits specified byndigits.

round(number[, ndigits])is used to round a floatnumberup to digits specified byndigits.

abs(value)returns the absolute value of avalueprovided as an argument.

abs(value)returns the absolute value of avalueprovided as an argument.

format(value[, format_spec])converts avalueto a 'formatted' representation, as controlled byformat_spec.

format(value[, format_spec])converts avalueto a 'formatted' representation, as controlled byformat_spec.

str([object])returns a string version ofobject. If the object is not provided, returns the empty string.

str([object])returns a string version ofobject. If the object is not provided, returns the empty string.

bool([value])return a Boolean value, i.e. one ofTrueorFalse.valueis converted using the standard truth testing procedure[1]. If thevalueis false or omitted, this returnsFalse; otherwise, it returnsTrue.

bool([value])return a Boolean value, i.e. one ofTrueorFalse.valueis converted using the standard truth testing procedure[1]. If thevalueis false or omitted, this returnsFalse; otherwise, it returnsTrue.

dir([object])returns the list of names in the current local scope when an argument is not provided. With an argument, it attempts to return a list of valid attributes for that object.

dir([object])returns the list of names in the current local scope when an argument is not provided. With an argument, it attempts to return a list of valid attributes for that object.

len(object)returns the length (the number of items) of anobject. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

len(object)returns the length (the number of items) of anobject. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

It is worth noting that almost all built-in python functions take one or more arguments, perform the specific operation on it and return the output. We will keep learning about many more built-in python functions as we progress through our Python learning journey. More information about various built-in functions can be obtained from Python official documentation

User defined python functions

Although Python provides a wide array of built-in python functions, it does not suffice in tackling issues we would face while we develop programs and applications. As Python programmers, we might need to break down the programming challenge into smaller chunks and implement them in the form of custom oruser definedfunctions. The concept of writing functions is probably an essential feature of any programming language.

Functions are defined using thedefkeyword, followed by anidentifiername along with the parentheses, and by the final colon that ends the line. The block of statements which forms thebodyof the function follows thefunction definition. Here's a simple example.

def greet():
 """Block of statement.
 or Body of function."""
 print(' Hello from inside the function!')

The above definedgreetfunction can be called using its name as shown here.

# Calling the function
greet()

And the output will be

Hello from inside the function.

Python functions with a single argument

A function can be called as many times as we want, and Python will execute the statements within its body. The python function we mentioned above, neither takes any input nor does it return any output. It just prints the statement written within it. If the function has to take any input, it goes within the parentheses as aparameterduring the function definition. Parameters are the values we supply to the function so that the function can do something utilizing those values.

Note the terminology used here:

Parameters: They are specified within parentheses in the function definition, separated by commas.

Arguments: When we call a python function, values that parameters take are to be given as arguments in a comma separated format.

The modified version of the above simple python function explains these two terms:

# Here 'person_name' is a parameter.
def greet(person_name):
 """Prints greetings along with the value received via the parameter."""
 print('Hello ' + person_name + '!')

The above function definition definesperson_nameas a parameter to the functiongreet, and it can be called as shown below:

# Calling the function
greet('Amigo')

The above call to the functiongreettakes a stringAmigoas an argument and the output will be as follows:

Hello Amigo!

Python functions with multiple arguments and areturnstatement

Both versions of thegreetpython functions defined above were actually straightforward in terms of functionality that they perform. One more functionality that functions are capable of performing is to return a value to the calling statement using the keywordreturn. Consider a function that takes several parameters, performs some mathematical calculation on it and returns the output. For example:

# Function with two parameters 'a' and 'b'
def add(a, b):
 """Computes the addition and returns the result.
 It does not implement the print statement."""
 result = a + b # Computes addition
 return result # Returns the result variable

This user defined functionaddtakes two parametersaandb, sums them together and assigns its output to a variableresultand ultimately returns the variable to calling statement as shown below:

# Calling the add function
x = 5
y = 6
print(f'The addition of {x} and {y} is {add(x, y)}.')

We call the functionaddwith two argumentsxandy(as the function definition has two parameters) initialized with5and6respectively, and the addition returned by the function gets printed via theprintstatement as shown below:

The addition of 5 and 6 is 11.

Similarly, python functions can also return multiple values based on the implementation. The following function demonstrates the same.

# Function definition
def upper_lower(x):
 """Returns the upper and lower version of the string.
 The value must be a string, else it will result in an error.
 This function does not implement any error handling mechanism."""
 upper = x.upper() # Convert x to upper string
 lower = x.lower() # Convert x to lower string
 return upper, lower # Return both variables upper and lower

The aboveupper_lowerfunction takes one argumentx(a string) and converts it to their upper and lower versions. Let us call it and see the output.

Note: The function upper_lower implicitly assumes to have a string as a parameter. Providing an integer or float value as an argument while calling will result in an error.

Note: The function upper_lower implicitly assumes to have a string as a parameter. Providing an integer or float value as an argument while calling will result in an error.

# Calling the function
upper, lower = upper_lower('Python')
# Printing output
print(upper)
PYTHON
print(lower)
python

Here, the call toupper_lowerfunction has been assigned to two variablesupperandloweras the function returns two values which will be unpacked to each variable respectively and the same can be verified in the output shown above.

Python functions with default arguments

Let us say, we are writing a function that takes multiple parameters. Often, there are common values for some of these parameters. In such cases, we would like to be able to call the function without explicitly specifying every parameter. In other words, we would like some parameters to have default values that will be used when they are not specified in the function call.

To define a python function with a default argument value, we need to assign a value to the parameter of interest while defining a function.

def power(number, pow=2):
 """Returns the value of number to the power of pow."""
 return number**pow

Notice that the above python function computes the first argument to the power of the second argument. The default value of the latter is 2. So now when we call the python functionpoweronly with a single argument, it will be assigned to thenumberparameter and the return value will be obtained by squaringnumber.

# Calling the power function only with required argument
print(power(2))
# Output
4

In other words, the argument value to the second parameterpowbecame optional. If we want to calculate the number for a different power, we can obviously provide a value for it and the python function will return the corresponding value.

# Calling the power function with both arguments
print(power(2, 5)
# Output
32

We can have any number of default value parameters in a python function. Note however that they must follow non-default value parameters in the definition. Otherwise, Python will throw an error as shown below:

# Calling the power function that will throw an error
def power(pow=2, number):
 """Returns the raised number to the power of pow."""
 return number**pow
 File "<ipython-input-57-9d342db32aba>", line 1
 def power(pow=2, number):
 ^
SyntaxError: non-default argument follows default argument

Python functions with variable length arguments

Let's consider a scenario where we as developers aren't sure about how many arguments a user will want to pass while calling a python function. For example, a function that takes floats or integers (irrespective of how many they are) as arguments and returns the sum of all of them. We can implement this scenario as shown below:

def sum_all(*args):
 """Sum all values in the *args."""
 # Initialize result to 0
 result = 0
 # Sum all values
 for i in args:
 result += i
 # Return the result
 return result

The flexible argument is written as*followed by the parameter name in the python function definition. The parameterargspreceded by*denotes that this parameter is of variable length. Python than unpacks it to atupleof the same nameargswhich will be available to use within the function. In the above example, we initialize the variableresultto 0 which will hold the sum of all arguments. We then loop over theargsto compute a sum and update theresultwith each iteration. Finally, we return the sum to the calling statement. Thesum_allpython function can be called with any number of arguments and it will add them all up as follows:

# Calling the sum_all function with arbitrary number of arguments.
print(sum_all(1, 2, 3, 4, 5))
# Output
15
# Calling with different numbers of arguments.
print(sum_all(15, 20, 6))
# Output
41

Here,*argsis used as the parameter name (the shorthand forarguments), but we can use any valid identifier as the parameter name. It justs needs to be preceded by*to make it flexible in length. On the same lines, Python provides another flavor of flexible arguments which are preceded by double asterisk marks. When used ,they are unpacked todictionaries(with the same name) by the interpreter and are available to use within the function. For example:

def info(**kwargs):
 """Print out key-value pairs in **kwargs."""
 # Run for loop to prints dictionary items
 for key, value in kwargs.items():
 print(key + ': ' + value)

Here, the parameter**kwargsare known askeywords argumentswhich will be converted into a dictionary of the same name. We then loop over it and print all keys and values. Again, it is totally valid to use an identifier other thankwargsas the parameter name. Theinfopython function can be called as follows:

# Calling the function
print(info(ticker='AAPL', price='146.83', name='Apple Inc.', country='US'))
# Output
ticker: AAPL
price: 146.83
name: Apple Inc.
country: US

That is all about the default and flexible arguments. We now attempt to head towards the documentation part of python functions.

DocStrings

Python has a nifty feature calleddocumentation string, usually referred to by its shorter namedocstrings. This is an important but not required tool that should be used every time we write a program since it helps to document the program better and makes it easier to understand.

Docstrings are written within triple single/double quotes just after definition header. They are written on the first logical line of a python function. Docstrings are not limited to functions only; they also apply to modules and classes. The convention followed for a docstring is a multi-line string where the first line starts with a capital letter and ends with a dot. The second line is blank followed by any detailed explanation starting from the third line. It is strongly advised to follow this convention for all docstrings. Let's see this in practice with the help of an example:

def power(x, y):
 """Equivalent to x**y or built-in pow() with two arguments.
 x and y should be numerical values else an appropriate error will be thrown for incompatible types.
 Parameters:
 x (int or float): Base value for the power operation.
 y (int or float): Power to which base value should be raised.
 Returns:
 int or float: It returns x raised to the power of y.
 """
 try:
 return x ** y
 except Exception as e:
 print(e)

The python functionpowerdefined above returns the raised value of the argumentxpowered toy. The thing of our interest is the docstring written within'''which documents the function. We can access a docstring of any function using the__doc__attribute (notice thedouble underscores) of that function. The docstring for thepowerfunction can be accessed with the following code:

print(power.__doc__)

And the output is shown below:

Equivalent to x**y or built-in pow() with two arguments.
x and y should be numerical values else an appropriate error will be thrown for incompatible types.
Parameters:
x (int or float): Base value for the power operation.
y (int or float): Power to which base value should be raised.
Returns:
int or float: It returns x raised to the power of y.

We have already seen the indirect usage of docstrings in previous sections. When we use a python functionhelpin Python, it will show up the docstring. What it does is fetch the__doc__attribute of that function and displays it in a neat manner. If we ask for the help on the user definedpowerusing theprint(help(power)), Python will return the same output as shown above that we got using theprint(power.__doc__).

Nested python functions and non-local variable

A nested python function is a function that is defined inside another function. The syntax for the nested function is the same as that of any other python function. Though the applications of nested functions are complex in nature and limited at times, even in the quant domain, it is worth mentioning, as we might encounter this out there in the wild. Below is an example which demonstrates the nested python functions.

# Defining nested function
def outer():
 """ This is an enclosing function """
 def inner():
 """ This is a nested function """
 print('Got printed from the nested function.')
 print('Got printed from the outer function.')
 inner()

We define the python functionouterwhich nests another python functioninnerwithin it. Theouterfunction is referred to as anenclosingfunction andinneris known asnestedfunction. They are also referred to asinnerfunctions sometimes. Upon calling theouterfunction, Python will, in turn, call theinnerfunction nested inside it and execute it. The output for the same is shown below:

# Calling the 'outer' function
outer()
# Output
Got printed from the outer function.
Got printed from the nested function.

The output we got here is intuitive. First, theprintstatement within theouterfunction got executed, followed by theprintstatement in theinnerfunction. Additionally, nested functions can access variables of the enclosing functions. i.e. variables defined in the outer function can be accessed by the inner function. However, the inner or the nested python function cannot modify the variables defined in the outer or enclosing python function.

def outer(n):
 number = n
 def inner():
 print('Number =', number)
 inner()

A call toouterfunction will print the following

outer(5)
# Output
Number = 5

Though the variablenumberis not defined withininnerfunction, it is able to access and print thenumber. This is possible because of scope mechanism that Python provided. We discuss more on this in the following section. Now consider, what if we want the nested python function to modify the variable that is declared in the enclosing python function. The default behavior of Python does not allow this. If we try to modify it, we will be presented with an error. To handle such a situation, the keywordnonlocalcomes to the rescue.

In the nested python function, we use the keywordnonlocalto create and change the variables defined in the enclosing python function. In the example that follows, we alter the value of the variablenumber.

def outer(n):
 number = n
 def inner():
 nonlocal number
 number = number ** 2
 print('Square of number =', number)
 print('Number =', number)
 inner()
 print('Number =', number)

A call to theouterpython function will now print the number passed as an argument to it, the square of it and the newly updated number (which is nothing but the squared number only).

outer(3)
# Output
Number = 3
Square of number = 9
Number = 9

Remember, assigning a value to a variable will only create or change the variable within a particular python function (or a scope) unless they are declared using the nonlocal statement.

Variable Namespace and Scope

If we read theThe Zen of Python(tryimport thisin Python console), the last line statesNamespaces are one honking great idea -- let's do more of those!Let's try to understand what these mysterious namespaces are. However, before that, it will be worth spending some time understandingnamesin the context of Python.

Names in the Python world

Aname(also known as an identifier) is simply a name given to an object. From Python basics, we know that everything in Python are objects. And a name is a way to access the underlying object. Let us create a new variable with a namepricehaving a value 144, and check thememory location identifieraccessible by the python functionid.

# Creating new variable
price = 144
# Case 1: Print memory id of the variable price
print(id(price))
# Case 1: Output
1948155424
# Case 2: Print memory id of the absolute value 144
print(id(144))
# Case 2: Output
1948155424

Interestingly we see that the memory location of both cases (the variable and its assigned value) is the same. In other words, both refer to the same integer object. If you would execute the above code on your workstation, memory location would almost certainly be different, but it would be the same for both the variable and value. Let's add more fun to it. Consider the following code:

# Assign price to old_price
old_price = price
# Assign new value to price
price = price + 1
# Print price
print(price)
# Output
145
# Print memory location of price and 145
print('Memory location of price:', id(price))
print('Memory location of 145:', id(145))
# Output
Memory location of price: 1948155456
Memory location of 145: 1948155456
# Print memory location of old_price and 144
print('Memory location of old_price:', id(old_price))
print('Memory location of 144:', id(144))
# Output
Memory location of old_price: 1948155424
Memory location of 144: 1948155424

We increased the value of a variablepriceby 1 unit and see that the memory location of it got changed. As you may have guessed, the memory location of an integer object145would also be the same as that ofprice. However, if we check the memory location of a variableold_price, it would point to the memory location of integer object144. This is efficient as Python does not need to create duplicate objects. This also makes Python powerful in a sense that a name could refer to any object, even functions. Note that python functions are also objects in Python. Now that we are aware of the nitty-gritty of names in Python, we are ready to examine namespaces closely.

Namespace

Name conflicts happen all the time in real life. For example, we often see that there are multiple students with the same name X in a classroom. If someone has to call the student X, there would be a conflicting situation for determining which student X is actually being called. While calling, one might use the last name along with the student's first name to ensure that the call is made to the correct student X.

Similarly, such conflicts also arise in programming. It is easy and manageable to have unique names when programs are small without any external dependencies. Things start becoming complex when programs become larger and external modules are incorporated. It becomes difficult and wearisome to have unique names for all objects in the program when it spans hundreds of lines.

A namespace can be thought of a naming system to avoid ambiguity between names and ensures that all the names in a program are unique and can be used without any conflict. Most namespaces are implemented as a dictionary in Python. There is a name to object mapping, with names as keys and objects as values. Multiple namespaces can use the same name and map it to a different object. Namespaces are created at different moments and have different lifetimes. Examples of namespaces are:

The set of built-in names: It includes built-in functions and built-in exception names.

The global names in a module: It includes names from various modules imported in a program.

The local names in a function: It includes names inside a function. It is created when a python function is called and lasts until the function returns.

The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; that is, two different modules can contain a functionsumwithout any conflict or confusion. However, they must be prefixed with the module name when used.

Scopes

Until now we've been using objects anywhere in a program. However, an important thing to note is not all objects are always accessible everywhere in a program. This is where the concept of scope comes into the picture. Ascopeis a region of a Python program where a namespace is directly accessible. That is when a reference to a name (lists, tuples, variables, etc.) is made, Python attempts to find the name in the namespace. The different types of scopes are:

Local scope: Names that are defined within a local scope means they are defined inside a python function. They are accessible only within a function. Names defined within a function cannot be accessed outside of it. Once the execution of a function is over, names within the local scope cease to exist. This is illustrated below:

# Defining a function
def print_number():
 # This is local scope
 n = 10
 # Printing number
 print('Within function: Number is', n)
print_number()
# This statement will cause error when executed
print('Outside function: Number is', n)
# Output
Within function: Number is 10
Traceback (most recent call last):
 File "<ipython-input-2-f44bdaae6d53>", line 8, in <module>
 print('Outside function: Number is', n)
NameError: name 'n' is not defined

Enclosing scope: Names in the enclosing scope refer to the names defined within enclosing functions. When there is a reference to a name that is not available within the local scope, it will be searched within the enclosing scope. This is known as scope resolution. The following example helps us understand this better:

# This is enclosing / outer function
def outer():
 number = 10
 # This is nested / inner function
 def inner():
 print('Number is', number)
 inner()
outer()
# Output
Number is 10

We try to print the variablenumberfrom within theinnerfunction where it is not defined. Hence, Python tries to find the variable in theouterfunction which works as an enclosing python function. What if the variable is not found within the enclosing scope as well? Python will try to find it in theglobalscope which we discuss next.

Global scope: Names in the global scope means they are defined within the main script of a program. They are accessible almost everywhere within the program. Consider the following example where we define a variablenbefore a function definition (that is, within global scope) and define another variable with the same namenwithin the python function.

# Global variable
n = 3
def relu(val):
 # Local variable
 n = max(0, val)
 return n
print('First statement: ', relu(-3))
print('Second statement:', n)
# Output
First statement: 0
Second statement: 3

Here, the first print statement calls therelufunction with a value of-3which evaluates the maximum number to 0 and assigns the maximum number to the variablenwhich in turn gets returned thereby printing 0. Next, we attempt to print thenand Python prints3. This is because Python now refers to the variablendefined outside the function (within the global scope). Hence, we got two different values ofnas they reside in different scopes. This brings us to one obvious question, what if the variable is not defined within the local scope, but available in the globals scope and we try to access that global variable? The answer is intuitive, we will be able to access it within the python function. However, it would be a read-only variable and hence we won't be able to modify it. An attempt to modify a global variable result in the error as shown below:

# Global variable
number = 5
# Function that updates the global variable
def update_number():
 number = number + 2
 print('Within function: Number is', number)
# Calling the function
update_number()
print('Outside function: Number is', number)
# Output
Traceback (most recent call last):
 File "<ipython-input-8-267134da25e4>", line 8, in <module>
 update_number()
 File "<ipython-input-8-267134da25e4>", line 4, in update_number
 number = number + 2
UnboundLocalError: local variable 'number' referenced before assignment

To handle such a situation which demands modification of a global name, we define the global name within the python function followed by theglobalkeyword. Theglobalkeywords allow us to access the global name within the local scope. Let us run the above code, but with theglobalkeyword.

# Global variable
number = 5
# Function that updates the global variable
def update_number():
 global number
 number = number + 2
 print('Within function: Number is', number)
# Calling the function
update_number()
print('Outside function: Number is', number)
# Output
Within function: Number is 7
Outside function: Number is 7

Theglobalkeyword allowed us to modify the global variable from the local scope without any issues. This is very similar to the keywordnon-localwhich allows us to modify variables defined in the enclosing scope.

Built-in scope: This scope consists of names predefined within built-ins module in Python such assum,print,type, etc. Though we neither define these python functions anywhere in our program nor we import them from any external module they are always available to use.

To summarize, when executing a Python code, names are searched in various scopes in the following order:

Enclosing

Global

Built-in

If they are not found in any scope, Python will throw an error.

Lambda python functions

We have written functions above using thedefkeyword, function headers, DocStrings and function bodies. There's a quicker way to write on-the-fly functions in Python and they are known as lambda functions. They are also referred to as anonymous python functions sometimes. We use the keywordlambdato write such functions. The syntax for lambda functions is as follows:

lambda arguments: expression

Firstly, the syntax shows that there is no python function name. Secondly,argumentsrefers to parameters, and finally,expressiondepicts the python function body. Let us create a python functionsquarewhich squares the argument provided to it and returns the result. We create this python function using thedefkeyword.

# Function defnition
def square(arg):
 """Computes the square of an argument and returns the result.
 It does not implement the print statement."""
 result = arg * arg
 return result
# Calling the function and printing its output
print(square(3))
# Output
9

The python functionsquaredefined above can be re-written in a single line using thelambdakeyword as shown below:

# Creating a lambda function and assigning it to square
square = lambda arg: arg * arg
# Calling the lambda function using the name 'square'
print(square(3))
# Outpuut
9

In the above lambda python function, it takes one argument denoted byargand returns its square. Lambda python functions can have as many number of arguments as we want after thelambdakeyword during its definition. We will restrict our discussion up to two arguments to understand how multiple arguments work. We create another lambda function to raise the first argument to the power of the second argument.

# Creating a lambda function to mimic 'raise to power' operation
power = lambda a, b: a ** b
# Calling the lambda function using the name 'power'
print(power(2, 3))
# Output
8

Lambda python functions are extensively used along with built-inmapandfilterfunctions.

map()Function

Themapfunction takes two arguments: a function and a sequence such as a list. This python function makes an iterator that applies the function to each element of a sequence. We can pass lambda python function to thismapfunction without even naming it. In this case, we refer to lambda functions as an anonymous function. In the following example, we create a listnumsconsisting of numbers and pass it to amapfunction along with the lambda function which will square each element of the list.

# Creating a list of all numbers
nums = [1, 2, 3, 4, 5]
# Defining a lambda function to square each number and passing it as an argument to map function
squares = map(lambda num: num ** 2, nums)

The lambda python function in the above example will square each element of the listnumsand the map function will map each output to the corresponding elements in the original list. We then store the result into a variable calledsquares. If we print thesquarevariable, Python will reveal us that it is a map object.

# Printing squares
print(squares)
# Output
<map object at 0x00000000074EAD68>

To see what this object contains, we need to cast it to list using thelistpython function as shown below:

# Casting map object squares to a list and printing it
print(list(squares))
# Output
[1, 4, 9, 16, 25]

filter()Function

Thefilterfunction takes two arguments: a function orNoneand a sequence. This function offers a way to filter out elements from a list that don't satisfy certain criteria. Before we embed a lambda function with it, let's understand how it works.

# Creating a list of booleans
booleans = [False, True, True, False, True]
# Filtering 'booleans', casting it to a list, and finally printing it
print(list(filter(None, booleans)))
# Output
[True, True, True]

In the above example, we first create a list of random boolean values. Next, we pass it to thefilterfunction along with theNonewhich specifies to return the items that are true. Lastly, we cast the output of thefilterfunction to a list as it outputs a filter object. In a more advanced scenario, we can embed a lambda function in thefilterfunction. Consider that we have been given a scenario where we need to filter all strings whose length is greater than 3 from a given set of strings. We can use filter and lambda functions together to achieve this. This is illustrated below:

# Creating a pool of random strings
strings = ['one', 'two', 'three', 'four', 'five', 'six']
# Filtering strings using a lambda and filter functions
filtered_strings = filter(lambda string: len(string) > 3, strings)
# Casting 'filtered_strings' to a list and printing it
print(list(filtered_strings))
# Output
['three', 'four', 'five']

In the above example, a lambda python function is used within thefilterfunction which checks for the length of each string in thestringslist. And thefilterfunction will then filter out the strings which match the criteria defined by the lambda function.

Apart from themapandfilterpython functions discussed above, now we will learn another handy functionzipwhich can be used for iterating through multiple sequences simultaneously.

zip()Function

As regular computer users, we often comes across a file with.zipextension aka zip files. Basically, these files are the files which have zipped other files within them. In other words, zip files work as a container to hold other files.

In the Python world, thezippython function works more or less as a container for iterables instead of real files. The syntax for thezipis shown below:

zip(*iterables)

It takes an iterable as an input and returns the iterator that aggregates elements from each of the iterable. The output contains the iterator of a tuple. Thei-thelement in the iterator is the tuple consisting thei-thelement from each input. If the iterables in the input are of unequal sizes, the output iterator stops when the shortest input iterable is exhausted. With no input, it returns an empty iterator. Let us understand the working ofzipwith the help of an example.

# Defining iterables for the input
tickers = ['AAPL', 'MSFT', 'GOOG']
companies = ['Apple Inc', 'Microsoft Corporation', 'Alphabet Inc']
# Zipping the above defined iterables using the 'zip'
zipped = zip(tickers, companies)

We define two liststickersandcompanieswhich are used as an input to thezip. Thezippedobject is the iterator of typezipand hence we can iterate either over it using a looping technique to print its content:

# Iterating over a zipped object
for ticker, company in zipped:
 print('Ticker name of {} is {}.'.format(ticker, company))
# Output
Ticker name of AAPL is Apple Inc.
Ticker name of MSFT is Microsoft Corporation.
Ticker name of GOOG is Alphabet Inc.

or cast it to sequential data structures such as list or tuple easily.

# Casting the zip object to a list and printing it
print(list(zipped))
# Output
[('AAPL', 'Apple Inc.'),
 ('MSFT', 'Microsoft Corporation'),
 ('GOOG', 'Alphabet Inc.')]

As we should expect, the zipped object contains a sequence of tuples where elements are from the corresponding inputs. Azipobject in conjunction with*unzips the elements as they were before. For example:

# Unzipping the zipped object
new_tickers, new_companies = zip(*zipped)
# Printing new unzipped sequences
print(new_tickers)
('AAPL', 'MSFT', 'GOOG')
print(new_companies)
('Apple Inc.', 'Microsoft Corporation', 'Alphabet Inc.')

We unzip the zip objectzippedto two sequencesnew_tickersandnew_companies. By printing these sequences, we can see that the operation got successful and elements got unzipped successfully into respective tuples.

Conclusion

Thus we have seen the different types of python functions as well as how to call them. We also saw how python functions make our lives easier when it comes to programming. We also saw what a namespace in python functions is and its scope.

If you want to learn various aspects of Algorithmic trading then check out the Executive Programme in Algorithmic Trading (EPAT®). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti® makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
