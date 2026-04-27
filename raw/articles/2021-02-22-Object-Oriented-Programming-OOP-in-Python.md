---
title: "Object Oriented Programming (OOP) in Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/object-oriented-programming-python/"
date: "2021-02-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Object Oriented Programming (OOP) in Python

**来源**: [QuantInsti](https://blog.quantinsti.com/object-oriented-programming-python/)  
**日期**: 2021-02-22  
**作者**: QuantInsti

---

## 原文

Object Oriented Programming (OOP) in Python

ByJay Parmar

Python being a general-purpose programming language supports multiple programming paradigms, viz procedural, functional, and object-oriented programming (OOP). Each Pythoneer often uses a combination of these programming styles and usually has her preferred style of coding. As a Python programmer, you can write code in a style that you like.

Considering the number of concepts that OOP encompasses and its popularity, it demands more than one article. However, I will limit the discussion to some of the most widely used object-oriented programming concepts here.

I will cover the following topics and their implementation in Python:

Difference between Procedural programming and Functional programming

What is OOP and why is it required?

What are classes and their objects?

What are the attributes and methods?

What is init method?

What is a self keyword, and why do we use it?

Note:This article assumes some familiarity with Python programming. In case you want to brush up your knowledge on Python, I urge you to go through some of the initial chapters of thePython handbook. Before we jump to the discussion about OOP, let's clear the difference between procedural and functional programming.

Difference between Procedural programming and Functional programming

Procedural programming is the one we learn when we start programming. In its simplest form, procedural programming takes the top-down approach of executing code. The code will be executed line by line sequentially in an order it has been written. That's it, that's procedural programming for you.

If you learn by example, here it is:

Below is the output:

First, this line will execute.
Next, Python executes this line.
Then, this line shows up.
Finally, Python completes execution by printing this line.

Instead ofprintstatements, we can have any code. No matter what code, Python will execute it. In case, the Python interpreter cannot execute the code, it will throw the appropriate error and will finish the execution abnormally. I can say it is a pretty easy programming style.

Next comes the functional programming style. Here, we try to combine code lines into logical blocks that can be reused as and when required.

Say you want to learnhow to backtest a trading strategyand write the Python code to automate it.

The steps to do so usually involves:

Downloading thehistorical data

Calculating buy and hold returns

Computing the statistical ortechnical indicators

Generating trading signals

Calculating strategy returns and other evaluation metrics

Visualising the performance of the strategy

Each of the above-listed steps can take one or more lines of code to achieve the defined objective. You can use either approach, procedural or functional, both work. However, the focus, here, would be to understand functional programming. We can create a dedicated function that encapsulates one or more steps defined above.

Below is an example workflow involving various functions to backtest a given strategy:

How many functions should be created and what function performs what functionality generally depends on the coder and how the problem statement is being approached.

Why is a grouping of functionality preferred?

The answer lies in the flexibility it provides. For example, using this programming style, we may choose to create utility functions that can be used across various Python scripts, thereby allowing us to modularise the overall project.

Additionally, it also minimises the chance of accidentally modifying the code that does not require any alteration. As a programmer, we can get a clear idea of which function is causing an error, thereby, focusing only on that particular piece of code.

Consider a scenario that requires a particular task to be executed quite often. If we code it using procedural programming, it involves writing the same piece of code over and over again, and it is not a good programming practice.

Instead, if we use functional programming that defines a function for that particular task, we can call it whenever required without having to repeat the code.

Having this knowledge in mind, we can appreciate how different programming styles enable us as a programmer to code efficiently. Or to say, it allows answering, what programming style is more apt given the scenario.

Onward to the main topic of this article now.

What is OOP and why is it required?

In the virtual world of programming, the OOP enables us to code the real-world objects as they are. The constructs of OOP allow us to define and organise the code such that they reflect the real-world scenarios.

Wondering what I mean by real-world objects?They are cars, books, chairs, keyboards, water bottles, pens, and so on. Intuitively, one can think of these objects to be common nouns. Often these objects are characterised by specific attributes/ properties and functions that they can perform.

Consider a car, for example. It has attributes like colour, transmission type, number of seats, fuel type, and many others. The functions that a car can perform be (self) drive, take a turn, drive reverse, lower windows, apply brakes, turn on/off the engine, play audio, and so on.

The OOP paradigm allows us to write a code that mimics the car's exact behaviour or to say any objects. Hence, the name, object-oriented programming. It enables us to encapsulate the attributes and functions of objects.

This does not mean that other paradigms are not useful; they are, but for different types of applications. Procedural programming might be a preferred choice to create an automation script and not the OOP.

The object-oriented approach enables programmers to write clear and logical code for small and large projects alike with proper organisation.

Some of the popular Python packages that are built using this approach are:

pandas

sklearn

zipline

The above list hints that the object-oriented approach enables us to develop large and complex projects with wide-ranging capabilities. At this point, we are sufficiently acquainted with what OOP is and its potential.

Let's learn about some of its primary constructs, classes and objects and see how to implement them using Python.

What are classes and their objects?

Let's continue with the example of a car. If we think in abstract terms, a car is nothing but the replication of an abstract idea. That is, a car itself is a generic term used to define a particular type of vehicle. In other words, it is one of the classes of vehicles. In programming terminology, we represent this abstract idea by aclass.

Now, let's think for a minute. If we say that a car is a concept, then what do we call a particular car, such as Toyota Corolla (or any of your favourite ones), what is it? As you might have guessed, it is anobjectof the car. And what is a car? It is a class (probably under the vehicle universe).

If we take an abstract look, we find that these cars are nothing but the replication of one abstract thing (idea) with different attributes and functions. In programming parlance, this thing isclass. In other words, the concept of a car provides us with a template or a blueprint from which we can define/create various objects of the car.

Can you try to think of some other classes and their objects?

Below are some examples:

Object

Mobile

iPhone X

Mumbai

Person

Mr Bean

At this juncture, I firmly assume that I was able to convey the idea of classes and objects to you. If not, do let me know in a comment below.

It's time to learn to implement these newly learned concepts in Python. The below code shows a class definition in Python.

We define a class with the help of a keywordclass, followed by the name of the class, and we end the sentence with:. The body of the class should contain its attributes and functions.

However, we define the classCarwith an empty body represented by the keywordpass. In the OOP paradigm, functions that go within the class are referred to as methods; now onwards, I will refer to functions as methods.

Once we have a class defined, we can create its instances, known asobjects. The classCarworks as a template to create new objects, as shown in the example below:

Often when we create an object of a class, we assign it to some variable. That variable is called the object of the class. Here, in our example,car_1andcar_2are examples of the classCar. This process is also known as theinstantiatingof an object. These objects are also known asclass instances.

Each of these objects can have different properties, and they can be set as follows:

Now, both objects have thecolourattribute. And if we are to print it, we would write as follows:

And the output we will get is the following:

The colour of Car 1 is Carbon Black
The colour of Car 2 is Magma Grey

So far, we have created a classCarand its objectscar_1andcar_2. However, currently, theCarclass in its current form can hardly be mapped to its real-world counterpart. For example, we know that every car will have certain features in common, like colour, number of types, number of seats, etc., and so some functions. Hence, instead of defining an empty class, we can define a class which encompasses these common attributes and functions.

What are the attributes and methods?

I am pretty sure that you know what I mean by attributes and methods. We have seen examples of attributes and methods multiple times by now. Keeping this in mind, I will directly jump to its implementation in Python.

The below example shows how to define a class with some default attributes and methods:

The updated class definition now resembles a real-world car to some extent. This time it has got two attributes,colourandseating_capacity, and two methods,drive_forward()andlower_windows()built-in it. That means, when we create an object of such a class, it will have these attributes and methods by default.

Of course, we can update these attribute values (neither all cars are White in colour nor all cars have a seating capacity of five). A new car object created below using the new class defined demonstrates this point.

The output is shown below:

The colour of Car 3 is: White
The seating capacity of Car 3 is: 5

As we can see in the above example, we can access a given object's attributes (and methods) using the dot operator. To modify default behaviour, we simply assign new values to attributes as shown below.

It will yield the following result:

The colour of Car 3 is: Magma Red
The seating capacity of Car 3 is: 2

In the real-world analogy, this operation is similar to modifying a car in real. The methods within a class define functionalities of a car. This means we can call methods using the objects only. Because if we don't have a car, there won't be a question of accessing its functionality.

We call methods oncar_3, as shown below:

Calling methods, as shown above, would output the following:

Driving 500 meters ahead
Lowering windows on all doors
Windows lowered

One thing to note here is, we cannot alter the behaviour of the methods defined within a class using their objects.

In this fashion, we can create as many objects of the classCaras we need. But wait, let's consider that we create twenty objects.

In this case, thecolourattribute of all those objects would have the same value,White. And we all know that in the real world, we have cars with all imaginable colours.

To replicate such a scenario, we might want to change the colour of those twenty objects. In the current implementation, we would need to change the colour attributes of all those objects. This approach does not seem to be efficient.

Instead,what if we can have a facility to change each object's colour the moment we create them?__init__method to our rescue.

What is init method?

You might have guessed what__init__does and mean for? If not, here you go,__init__means initialisation. We use this method to initiate the attributes with values provided by the object when it gets created. In other words, the__init__methods gets called as soon as a new object is created. Let's implement it in ourCarclass and see how we can leverage it.

In this implementation of the class, we define all variables (and methods) in the__init__that needs to be assigned (and called) upon creating a new object. How? As demonstrated in the below code:

We provide the values to be assigned tocolourandseating_capacityattributes while creating an object. This way, we can overcome the requirement to set each object's attribute values after they have been created.

If we access the newly created object's attributes, it would have the values we provided while creating them.

The output would be as shown below:

The colour of Car 4 is: Ocean Blue
The seating capacity of Car 4 is: 2

We can also place a method within the body of__init__to ensure that the method gets executed upon creation of an object. For those of you who come from any other object-oriented programming language, would be able to relate the__init__method with the constructor method.

You might have noticed that while defining these methods,__init__or any normal for that purpose, the first parameter these methods take is theselfkeyword.

Why is this keyword necessary, and why do we need to provide this keyword?We discuss it next.

What is a self keyword, and why do we use it?

In Python, everything is an object. I mean by this statement that whenever we create anyvariable in Python, it will be an object of some class, either built-in or user-defined. You may say that it is not the case.

Further, you may say that we can define any variable without the class notation. For example, as shown in the example below, we can define a variable without creating any instance of a class:

x = 'Python is easy.'

That's true. However, when we define a variable in this manner, Python recognises the type of value we assign to the variable and creates the object of the appropriate class on its own. We can check this as follows:

print(type(x))

It will show us that the type of the variablexisstr. Does that meanxis an instance of the string class? Let's verify:

print(isinstance(x, str))

Executing the above command returnsTrueas an output, which means that the variablexis an instance/object of the classstr.

Now, when I try to, say, count the number of occurrences oftin the variablexusing the methodcount()onx, I need to provide the letter for which I want the number of occurrences. This is shown below:

print(x.count('t'))

Notice that I am not providing the actual string in which the occurrence needs to be counted. Instead, I am invoking thecount()method on the object of the string. In this case also, where I am not providing the actual string, I will get the output as1.

So the question is, how does Python recognise which string to consider?

The answer is, when we call a method using the object, Python passes that object to the calling method and the respective calling method will handle it using theselfkeyword.

To elaborate, when we call thecount()using the notationx.count('t'), Python will send the objectxto thecount()method. Thiscount()method will then handle the objectxusing theselfkeyword. Hence, theselfkeyword goes as the first parameter in the method definition.

Let's take one more example to make this clear. Recall ourCarclass. All methods in theCarclass haveselfas the first parameter. Hence, when we call a method as follows:

car_4.lower_windows()

Consider the above command; when we call a method, as shown above, Python will pass the objectcar_4tolower_windows()method to convey that you need to perform action mentioned in the method body for the objectcar_4.

On the receiving side, the method will handle the object using theselfkeyword. In a nutshell, theselfkeyword refers to the object that is calling that particular method.

If you try to print theselfin the body of the method, it will print the object's memory location. Let's try this out. To do so, I add a new methodtemp()to the classCar.

Creating a new object of the classCar:

car_5 = Car('Blood Red', 1)

First, I print the newly created objectcar_5as

print(car_5)

This outputs the memory location ofcar_5on my machine which is,

<__main__.Car object at 0x0000022EB95BEA30>

If I execute thetemp()method oncar_5that prints theselfkeyword, I should get the same output. Here's the try:

car_5.temp()

And the output is

<__main__.Car object at 0x0000022EB95BEA30>

This process validates the claim that the object and theselfrefers to the same thing.

Summing up

I am hopeful that you have a good idea of classes, attributes, methods and objects. This understanding will allow you to further foray into the world object-oriented programming.

Before concluding, here's my attempt to put everything we covered in this article and quickly summarising it. Below-shown is a new example from thefinancial markets:

Answer the following questions before reading further:

What is the name of the class?

Which methods will be executed on its own upon creation of new objects?

What parameter do we need to provide while creating an object?

Can we define methods in the above class without theselfkeyword?

Can we update the value of theshort_sellingvariable while creating the object?

Is it possible to invoke multiple methods upon creation of the object?

Can I say that the default value ofshort_sellingvariable will beTruefor all objects I create?

I hope you won't find these questions difficult. Or have you any doubts or any difficulty answering these questions, do let me know in the comment section below.

Here are the answers:

The class name isStock.

The__init__method will get executed on its own every time a new object is created.

We need to passcn,mp,ex,ts,ssarguments while creating a new object.

Not really. Python will throw an error when we call a method that is defined without theselfkeyword being its first parameter. This is because Python will automatically pass the calling object to the method, and the method won't be able to handle it.

Nope, we won't be able to update the value of theshort_sellingvariable when creating a new object. We would be able to update its value after the object has been created.

Of course, yes. We can call a method within the body of__init__method that needs to be called upon object creation.

Yes, the default value ofshort_sellingfor all objects will beTrue.

Creating an object is a straightforward task. It can be created as follows:

AAPL = Stock('Apple Inc.', 234, 'NYSE', 2000, True)

And accessing attributes is also a no-brainer:

print('The total shares of AAPL are', AAPL.total_shares)

It would output the following:

The total shares of AAPL are 2000

Concluding Notes

In this article on object-oriented programming, you learned a few of the building blocks in detail. We started with the difference between procedural and functional programming.

Then you understood what object-oriented programming allows us to mimic the real-world and how it binds everything using the concepts of an object. Along the lines, you'd seen how to define classes and create objects.

You also learned how to make classes with (default) attributes and methods. Towards the end, we understood how the__init__method helps us and the use of theselfkeyword.

This article allows us to get started with OOP and by no means is comprehensive coverage on the topic. I plan to cover advanced topics on this subject in the upcoming article. Thanks for reading. Adios.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
