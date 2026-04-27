---
title: "Python Numpy Tutorial: Installation, Arrays And Random Sampling"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-numpy-tutorial-installation-arrays-random-sampling/"
date: "2019-07-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Numpy Tutorial: Installation, Arrays And Random Sampling

**来源**: [QuantInsti](https://blog.quantinsti.com/python-numpy-tutorial-installation-arrays-random-sampling/)  
**日期**: 2019-07-25  
**作者**: QuantInsti

---

## 原文

Python Numpy Tutorial: Installation, Arrays And Random Sampling

ByJay Parmar

NumPy, an acronym for Numerical Python, is a package to perform scientific computing in Python efficiently. It includes random number generation capabilities, functions for basic linear algebra and much more.Today we will learn the basics of the Python Numpy module as well as understand some of the codes. This blog article is an excerpt from thePython Basics Handbookcreated for the simple purpose of making the reader understand the beauty and simplicity of thePython language.The contents of this article include:

Installing NumPy

NumPy Arrays

Array creation using built-in functions

Random Sampling in NumPy

Array Attributes and Methods

Array Manipulation

Array Indexing and Iterating

Summary

Conclusion

Installing Numpy

NumPy is not a part of the Python Standard Library and hence, as with any other such library or module, it needs to be installed on a workstation before it can be used.Based on the Python distribution one uses,  it can be installed via a command prompt, conda prompt, or terminal using the following command.

pip install numpy

One point to note is that if we use the Anaconda distribution to install Python, most of the libraries (like NumPy, pandas, scikit-learn, matplotlib, etc.) used in the scientific Python ecosystem come pre-installed.Note:If we use the Python or iPython console to install the NumPy library, the command to install it would be preceded by the character!Once installed we can use it by importing into our program by using the import statement. The de facto way of importing is shown below:

import numpy as np

Here, the NumPy library is imported with an alias of np so that any functionality within it can be used with convenience. We will be using this form of alias for all the examples in this section.

NumPy Arrays

A Python list is a pretty powerful sequential data structure with some nifty features like index sub-setting and traversal. But lists lack an important feature, carrying out operations over an entire collection of elements in an efficient manner.For example, consider a case where we calculate PCR (Put Call Ratio) for the previous 5 days. Say, we have put and call options volume (in Lacs) stored in lists call_vol and put_vol respectively.We then compute the PCR by dividing put volume by call volume as illustrated in the below script:

put_vol = [52.89, 45.14, 63.84, 77.1, 74.6] # Put volume in lacs

call_vol = [49.51, 50.45, 59.11, 80.49, 65.11] # Call volume in lacs

# Computing Put Call Ratio (PCR)
put_vol / call_vol
Traceback (most recent call last):

  File "<ipython-input-12-9f9b38fcc5f4>", line 1, in <module>
    put_vol / call_vol

TypeError: unsupported operand type(s) for /: 'list' and 'list'

Unfortunately, Python threw an error while calculating PCR values as it has no idea on how to do calculations on lists. We can do this by iterating over each item in lists and calculating the PCR for each day separately.However, doing so is inefficient and tiresome too. A way more elegant solution is to use Python NumPy arrays, an alternative to the regular Python list.Let us execute the same operation using a Python NumPy array. To do this, we use array() function from the NumPy package and create the Python NumPy version of put_vol and call_vol lists.In[]

# Importing NumPy library
import numpy as np

# Creating arrays
n_put_vol = np.array(put_vol)

n_call_vol = np.array(call_vol)

n_put_vol

Out[]array([52.89, 45.14, 63.84, 77.1 , 74.6 ])In[]n_call_volOut[]array([49.51, 50.45, 59.11, 80.49, 65.11])Here, we have two arrays n_put_vol and n_call_vol which holds put and call volume respectively.Now, we can calculate PCR in one line:In[]

# Computing Put Call Ratio (PCR)
pcr = n_put_vol / n_call_vol

pcr

array([1.06826904, 0.89474727, 1.0800203 , 0.95788297, 1.14575334])

This time it worked, and calculations were performed element-wise. The first observation in PCR array was calculated by dividing the first element in n_put_vol by the first element in the n_call_vol array and so on.Python NumPy works with arrays as if they are scalars. But we need to pay attention here. Python NumPy can do this easily because it assumes that array can only contain values of a single type.It’s either an array of integers, floats or booleans and so on. If we try to create an array of different types like the one mentioned below, the resulting NumPy array will contain a single type only.String in the below case:

np.array([1, 'Python', True])

array(['1', 'Python', 'True'], dtype='<U11')

Note:NumPy arrays are made to be created as homogeneous arrays, considering the mathematical operations that can be performed on them. It would not be possible with heterogeneous data sets.In the example given above, an integer and a boolean were both converted to strings. NumPy array is a new type of data structure type like the Python list type that we have seen before. This also means that it comes with its own methods, which will behave differently from other types.Let us implement the + operation on the Python list and NumPy arrays and see how they differ.In[]

# Creating lists
list_1 = [1, 2, 3]

list_2 = [5, 6, 4]

# Adding two lists
list_1 + list_2

[1, 2, 3, 5, 6, 4]

# Creating arrays
arr_1 = np.array([1, 2, 3])

arr_2 = np.array([5, 6, 4])

# Adding two arrays
arr_1 + arr_2

array([6, 8, 7])

As can be seen in the above example, performing the + operation with list_1 and list_2, the list elements are pasted together, generating a list with 6 elements.On the other hand, if we do this with NumPy arrays, Python will do an element-wise sum of the arrays.

N-dimensional arrays

Until now, we have worked with two arrays: n_put_vol and n_call_vol. If we are to check its type using type(), Python tells us that they are of type numpy.ndarray as shown below:In[]

# Checking array type
type(n_put_vol)

numpy.ndarray

Based on the output we received, it can be inferred that they are of data type ndarray which stands for n-dimensional array within Python NumPy.These arrays are one-dimensional arrays, but Python NumPy also allows us to create two dimensional, three dimensional and so on. We will stick to two dimensional for our learning purposes.We can create a 2D (two dimensional) Python NumPy array from a regular Python list of lists.Let us create one array for all put and call volumes.In[]

# Recalling put and call volumes lists
put_vol

[52.89, 45.14, 63.84, 77.1, 74.6]

call_vol

[49.51, 50.45, 59.11, 80.49, 65.11]

# Creating a two-dimensional array
n_2d = np.array([put_vol, call_vol])

array([[52.89, 45.14, 63.84, 77.1 , 74.6 ],
       [49.51, 50.45, 59.11, 80.49, 65.11]])

We see that n_2d  array is a rectangular data structure.  Each list provided in the np.array creation function corresponds to a row in the two- dimensional NumPy array. Also for 2D arrays, the NumPy rule applies: an array can only contain a single type.If we change one float value in the above array definition, all the array elements will be coerced to strings, to end up with a homogeneous array. We can think of a 2D array as an advanced version of lists of a list. We can perform an element-wise operation with 2D as we had seen for a single dimensional array.

Array creation using built-in functions

An explicit input has been provided while creating n_call_vol and n_put_vol arrays. In contrast, Python NumPy provides various built-in functions to create arrays and input to them will be produced by Python NumPy.Below we discuss a handful of such functions:1. zeros(shape, dtype=float)returns an array of a given shape and type, filled with zeros. If the dtype is not provided as an input, the default type for the array would be float.In[]

# Creating a one-dimensional array
np.zeros(5)

array([0., 0., 0., 0., 0.])

# Creating a two-dimensional array
np.zeros((3, 5))

array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

# Creating a one-dimensional array of integer type
np.zeros(5, dtype=int)

Out[]array([0, 0, 0, 0, 0])

2. ones(shape, dtype=float)returns an array of a given shape and type, filled with ones.

# Creating a one-dimensional array
np.ones(5)

array([1., 1., 1., 1., 1.])

# Creating a one-dimensional array of integer type
np.ones(5, dtype=int)

array([1, 1, 1, 1, 1])

3. full(shape, fill_value, dtype=None)returns an array of a given shape and type, fill with fill_value given in input parameters.

# Creating a one-dimensional array with value as 12
np.full(5, 12)

array([12, 12, 12, 12, 12])

# Creating a two-dimensional array with value as 9
np.full((2, 3), 9)

array([[9, 9, 9],
       [9, 9, 9]])

4. arange([start, ]stop,  [step])returns an array with evenly spaced values within a given interval. Here the start and step parameters are optional. If they are provided Python NumPy will consider them while computing the output. Otherwise, range computation starts from 0. For all cases, stop value will be excluded in the output.

# Creating an array with only stop argument
np.arange(5)

array([0, 1, 2, 3, 4])

# Creating an array with start and stop arguments
np.arange(3, 8)

array([3, 4, 5, 6, 7])

# Creating an array with given interval and step value as 0.5
np.arange(3, 8, 0.5)

array([3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. , 7.5])

5. linspace(start, stop, num=50, endpoint=True)returns evenly spaced numbers over a specified interval. The number of samples to be returned is specified by the num parameter. The endpoint of the interval can optionally be excluded.

# Creating an evenly spaced array with five numbers within interval 2 to 3
np.linspace(2.0, 3.0, num=5)

array([2.  , 2.25, 2.5 , 2.75, 3.  ])

# Creating an array excluding end value
np.linspace(2.0, 3.0, num=5, endpoint=False)

array([2. , 2.2, 2.4, 2.6, 2.8])

# Creating an array with ten values within the specified interval
np.linspace(11, 20, num=10)

array([11., 12., 13., 14., 15., 16., 17., 18., 19., 20.])

Random Sampling in NumPy

In addition to built-in functions discussed above, we have a random sub-module within the Python NumPy that provides handy functions to generate data randomly and draw samples from various distributions.Some of the widely used functions are discussed here.1. rand([d0, d1, ..., dn])is used to create an array of a given shape and populate it with random samples from a uniform distribution over [0, 1). It takes only positive arguments. If no argument is provided, a single float value is returned.

# Generating single random number
np.random.rand()

0.1380210268817208

# Generating a one-dimensional array with four random values
np.random.rand(4)

array([0.24694323, 0.83698849, 0.0578015 , 0.42668907])

# Generating a two-dimensional array
np.random.rand(2, 3)

array([[0.79364317, 0.15883039, 0.75798628],
       [0.82658529, 0.12216677, 0.78431111]])

2. randn([d0, d1, ..., dn])is used to create an array of the given shape and populate it with random samples from a standard normal distribution.It takes only positive arguments and generates an array of shape (d0, d1, ..., dn) filled with random floats sampled from a univariate normal distribution of mean 0 and variance 1. If no argument is provided, a single float randomly sampled from the distribution is returned.

# Generating a random sample
np.random.randn()

0.5569441449249491

# Generating a two-dimensional array over N(0, 1)
np.random.randn(2, 3)

array([[ 0.43363995, -1.04734652, -0.29569917],
       [ 0.31077962, -0.49519421,  0.29426536]])

# Generating a two-dimensional array over N(3, 2.25)
1.5 * np.random.randn(2, 3) + 3

array([[1.75071139, 2.81267831, 1.08075029],
       [3.35670489, 3.96981281, 1.7714606 ]])

3. randint(low, high=None, size=None)returns a random integer from a discrete uniform distribution with limits of low (inclusive) and high (exclusive). If high is None (the default), then results are from 0 to low. If the size is specified, it returns an array of the specified size.

# Generating a random integer between 0 and 6
np.random.randint(6)

# Generating a random integer between 6 and 9
np.random.randint(6, 9)

Out[]7In[]

# Generating a one-dimensional array with values between 3 and 9
np.random.randint(3, 9, size=5)

array([6, 7, 8, 8, 5])

# Generating a two-dimensional array with values between 3 and 9
np.random.randint(3, 9, size=(2, 5))

array([[5, 7, 4, 6, 4],
       [6, 8, 8, 5, 3]])

4. random(size=None)returns a random float value between 0 and 1 which is drawn from the continuous uniform distribution.

# Generating a random float
np.random.random()

0.6013749764953444

# Generating a one-dimensional array
np.random.random(3)

array([0.69929315, 0.61152299, 0.91313813])

# Generating a two-dimensional array
np.random.random((3, 2))

array([[0.55779547, 0.6822698 ],
       [0.75476145, 0.224952  ],
       [0.99264158, 0.02755453]])

5. binomial(n, p, size=None)returns samples drawn from a binomial distribution with n trials and p probability of success where n is greater than 0 and p is in the interval of 0 and 1.

# Number of trials, probability of each trial
n, p = 1, .5

# Flipping a coin 1 time for 50 times
samples = np.random.binomial(n, p, 50)

samples

array([1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1,
       0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0,
       0, 1, 0, 0, 1, 0])

6. normal(mu=0.0, sigma=1.0,  size=None)draws random samples from anormal (Gaussian) distribution. If no arguments provided, a sample will be drawn from N(0, 1).

# Initialize mu and sigma
mu, sigma = 0, 0.1

# Drawing 5 samples in a one-dimensional array
np.random.normal(mu, sigma, 5)

array([ 0.06790522,  0.0092956 ,  0.07063545,  0.28022021, -0.13597963])

# Drawing 10 samples in a two-dimensional array of shape (2, 5)
np.random.normal(mu, sigma, (2, 5))

Out[]array([[-0.10696306, -0.0147926 , -0.07027478, 0.04399432, -0.03861839], [-0.02004485, 0.08760261, 0.18348247, -0.09351321, -0.19487115]])

7. uniform(low=0.0, high=1.0, size=None)draws samples from a uniform distribution over the interval 0 (including) and 1 (excluding), if no arguments are provided. In other words, any value drawn is equally likely within the interval.

# Creating a one-dimensional array with samples drawn within [-1, 0)
np.random.uniform(-1, 0, 10)

array([-0.7910379 , -0.64144624, -0.64691011, -0.03817127, -0.24480339,
       -0.82549031, -0.37500955, -0.88304322, -0.35196588, -0.51377252])

# Creating a two-dimensional array with samples drawn within [0, 1)
np.random.uniform(size=(5, 2))

array([[0.43155784, 0.41360889],
       [0.81813931, 0.70115211],
       [0.40003811, 0.2114227 ],
       [0.95487774, 0.92251769],
       [0.91042434, 0.98697917]])

In addition to the functions shown above, we can draw samples from various other distributions such as Poisson, Gamma, Exponential, etc. using Python NumPy.

Array Attributes and Methods

We now have some idea about the working of Python NumPy arrays. Let us now explore the functionalities provided by them. As with any Python object,NumPy arrays also have a rich set of attributes and methods which simplifies the data analysis process to a great extent. Following are the most useful array attributes. For illustration purpose, we will be using previously defined arrays.1. ndimattribute displays the number of dimensions of an array. Using this attribute on n_call_vol and pcr, we expect dimensions to be 1 and 2 respectively. Let’s check.

# Checking dimensions for n_call_vol array
np_call_vol.ndim

n_2d.ndim

2. shapereturns a tuple with the dimensions of the array.  It may also be used to reshape the array in-place by assigning a tuple of array dimensions to it.

# Checking the shape of the one-dimensional array
n_put_vol.shape

# Checking shape of the two-dimensional array
n_2d.shape

(2, 5)# It shows 2 rows and 5 columns

# Printing n_2d with 2 rows and 5 columns
n_2d

array([[52.89, 45.14, 63.84, 77.1 , 74.6 ],
       [49.51, 50.45, 59.11, 80.49, 65.11]])

# Reshaping n_2d using the shape attribute
n_2d.shape = (5, 2)

# Printing reshaped array
n_2d

array([[52.89, 45.14],
       [63.84, 77.1 ],
       [74.6 , 49.51],
       [50.45, 59.11],
       [80.49, 65.11]])

3. sizereturns the number of elements in the array.

n_call_vol.size

n_2d.size

4. dtypereturns the data-type of the array’s elements. As we learned above, NumPy comes with its own data type just like regular built-in data types such as int, float, str, etc.

n_put_vol.dtype

dtype('float64')

In an ideal data analysis process, we generally have thousands of numbers which need to be analyzed. Simply staring at these numbers won’t provide us with any insights. Instead, what we can do is generate summary statistics of the data.Among many useful features, Python NumPy also provides various statistical functions which are good to perform such statistics on arrays.Let us create a sample array and populate it with samples drawn from a normal distribution with a mean of 5 and a standard deviation of 1.5 and compute various statistics on it.

# Creating a one-dimensional array with 1000 samples drawn from a normal distribution
samples = np.random.normal(5, 1.5, 1000)

# Creating a two-dimensional array with 25 samples drawn from a normal distribution
samples_2d = np.random.normal(5, 1.5, size=(5, 5))

samples_2d

array([[5.30338102, 6.29371936, 2.74075451, 3.45505812, 7.24391809],
       [5.20554917, 5.33264245, 6.08886915, 5.06753721, 6.36235494],
       [5.86023616, 5.54254211, 5.38921487, 6.77609903, 7.79595902],
       [5.81532883, 0.76402556, 5.01475416, 5.20297957, 7.57517601],
       [5.76591337, 1.79107751, 5.03874984, 5.05631362, 2.16099478]])

5. mean(a, axis=None)returns the average of the array elements. The average is computed over the flattened array by default, otherwise over the specified axis.average(a, axis=None) returns the average of the array elements and works similar to that of mean().

# Computing mean
np.mean(samples)

5.009649198007546

np.average(samples)

5.009649198007546

# Computing mean with axis=1 (over each row)
np.mean(samples_2d, axis=1)

array([5.00736622, 5.61139058, 6.27281024, 4.87445283, 3.96260983])

np.average(samples_2d, axis=1)

array([5.00736622, 5.61139058, 6.27281024, 4.87445283, 3.96260983])

np.max(samples)

9.626572532562523

np.max(samples_2d, axis=1)

array([7.24391809, 6.36235494, 7.79595902, 7.57517601, 5.76591337])

7. median(a, axis=None)returns the median along the specified axis.

np.median(samples)

5.0074934668143865

np.median(samples_2d)

5.332642448141249

8. min(a, axis=None)returns the minimum of an array or minimum along an axis.

np.min(samples)

0.1551821703754115

np.min(samples_2d, axis=1)

array([2.74075451, 5.06753721, 5.38921487, 0.76402556, 1.79107751])

9. var(a, axis=None)returns the variance of an array or along with the specified axis.

np.var(samples)

2.2967299389550466

np.var(samples_2d)

2.93390175942658

np.var(samples_2d, axis=0) # Here, the variance is computed over each column of numbers

array([0.07693981, 4.95043105, 1.26742732, 1.10560727, 4.37281009])

10. std(a, axis=None)returns the standard deviation of an array or along the specified axis.

np.std(samples)

1.5154965981337756

np.std(samples_2d)

1.7128636137844075

11. sum(a, axis=None)returns the sum of array elements.

# Recalling the array n_put_vol
n_put_vol

array([52.89, 45.14, 63.84, 77.1 , 74.6 ])

# Computing sum of all elements within n_put_vol
np.sum(n_put_vol)

313.57

# Computing sum of all array over each row
np.sum(samples_2d, axis=1)

Out[]array([25.03683109, 28.05695291, 31.36405118, 24.37226413, 19.81304913])

12. cumsum(a, axis=None)returns the cumulative sum of the elements along a given axis.In[]

np.cumsum(n_put_vol)

array([ 52.89,  98.03, 161.87, 238.97, 313.57])

The methods discussed above can also be directly called upon NumPy objects such as samples, n_put_vol, samples_2d, etc. instead of using the np. format as shown below.The output will be the same in both cases.

# Using np. format to compute the sum
np.sum(samples)

5009.649198007546

# Calling sum() directly on a NumPy object
samples.sum()

5009.649198007546

Array Manipulation

Python NumPy defines a new data type calledndarrayfor the array object it creates. This also means that various operators such as arithmetic operators, logical operator, boolean operators, etc. work in ways unique to it as we’ve seen so far.There’s a flexible and useful array manipulation technique thatPython NumPyprovides to use on its data structure using broadcasting.The term broadcasting describes how Python NumPy treats arrays with different shapes during arithmetic operations (with certain constraints). The smaller array is ’broadcast’ across the larger array so that they have compatible shapes. It also provides a mean of vectorizing array operations.Python NumPy operations are usually done on pairs of arrays on an element-by-element basis. In the simplest case, the two arrays must have exactly the same shape as in the following example.

a = np.array([1, 2, 3])

b = np.array([3, 3, 3])

a * b

array([3, 6, 9])

Python NumPy’s broadcasting rule relaxes this constraint when the array’s shapes meet certain constraints.The simplest broadcasting example occurs when an array and a scalar value are combined in operation as depicted below:

a = np.array([1, 2, 3])

b = 3

a * b

array([3, 6, 9])

The result is equivalent to the previous example where b was an array. We can think of the scalar b in the above example being stretched during the arithmetic operation into an array with the same shape as a.The new elements in b are simply copies of the original scalar. Here, the stretching analogy is only conceptual. Python NumPy is smart enough to use the original scalar value without actually making copies so that broadcasting operations are as memory and computationally efficient as possible.The code in the last example is more efficient because broadcasting moves less memory around during the multiplication than that of its counterpart defined above it.Along with efficient number processing capabilities, Python NumPy also provides various methods for array manipulation thereby proving its versatility.We discuss some of them here.1. exp(*args)returns the exponential of all elements in the input array. The numbers will be raised to e also known as Euler’s number.

# Computing exponentials for the array 'a'
np.exp(a)

array([ 2.71828183,  7.3890561 , 20.08553692])

2. sqrt(*args)returns the positive square-root of an array, element-wise.

# Computing square roots of a given array
np.sqrt([1, 4, 9, 16, 25])

array([1., 2., 3., 4., 5.])

3. reshape(new_shape)gives a new shape to an array without changing its data.

# Creating a one-dimensional array with 12 elements
res = np.arange(12)

res

array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

# Reshaping the 'res' array to 2-dimensional array
np.reshape(res, (3, 4))

array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

# Reshaping the dimensions from (3, 4) to (2, 6)
np.reshape(res, (2, 6))

array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])

4. resize(a, new_shape)return a new array with the specified shape.  If the new array is larger than the original array, then the new array is filled with repeated copies of a.

# Creating a one-dimensional array
demo = np.arange(4)

demo

array([0, 1, 2, 3])

# Resizing a 'demo' array to (2, 2)
np.resize(demo, (2, 2))

array([[0, 1],
       [2, 3]])

# Resizing a 'demo' greater than its size.
np.resize(demo, (4, 2))

Out[]array([[0, 1], [2, 3], [0, 1], [2, 3]])

5. round(a, decimals=0)round an array to the given number of decimals. If decimals are not given, elements will be rounded to the whole number.

# Creating a one-dimensional array
a = np.random.rand(5)

# Printing array
a

array([0.71056952, 0.58306487, 0.13270092, 0.38583513, 0.7912277 ])

# Rounding to 0 decimals
a.round()

array([1., 1., 0., 0., 1.])

# Rounding to 0 decimals using the np.round syntax
np.round(a)

array([1., 1., 0., 0., 1.])

# Rounding to 2 decimals
a.round(2)

array([0.71, 0.58, 0.13, 0.39, 0.79])

# Rounding to 3 decimals using the np.round syntax
np.round(a, 3)

array([0.711, 0.583, 0.133, 0.386, 0.791])

6. sort(a, kind='quicksort')returns a sorted copy of an array.  The default sorting algorithm used is quicksort. Other available options are mergesort and heapsort.

np.sort(n_put_vol)

array([45.14, 52.89, 63.84, 74.6 , 77.1 ])

np.sort(samples_2d)

array([[2.74075451, 3.45505812, 5.30338102, 6.29371936, 7.24391809],
       [5.06753721, 5.20554917, 5.33264245, 6.08886915, 6.36235494],
       [5.38921487, 5.54254211, 5.86023616, 6.77609903, 7.79595902],
       [0.76402556, 5.01475416, 5.20297957, 5.81532883, 7.57517601],
       [1.79107751, 2.16099478, 5.03874984, 5.05631362, 5.76591337]])

7. vstack(tup)stacks arrays provided via tup in sequence vertically (row-wise).

hstack(tup)stacks arrays provided via tup in sequence horizontally (column-wise).

column_stack(tup)stacks 1-dimensional arrays as column into a 2- dimensional array. It takes a sequence of 1-D arrays and stacks them as columns to make a single 2-D array.

# Creating sample arrays
a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

c = np.array([7, 8, 9])

# Stacking arrays vertically
np.vstack((a, b, c))

array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

# Stacking arrays horizontally
np.hstack((a, b, c))

array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Stacking two arrays together
np.column_stack((a, b))

array([[1, 4],
       [2, 5],
       [3, 6]])

# Stacking three arrays together
np.column_stack((a, b, c))

array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])

8. transpose()permutes the dimensions of an array.

# Creating a two-dimensional array with shape (2, 4)
a = np.arange(8).reshape(2, 4)

# Printing it
a

array([[0, 1, 2, 3],
       [4, 5, 6, 7]])

# Transposing the array
a.transpose()

array([[0, 4],
       [1, 5],
       [2, 6],
       [3, 7]])

Array Indexing and Iterating

NumPy is an excellent library for efficient number crunching along with ease of use. It seamlessly integrates with Python and its syntax. Following this attribute, Python NumPy provides subsetting and iterating techniques very similar to lists.We can use square brackets to subset NumPy arrays, Python built-in constructs to iterate, and other built-in methods to slice them.

Indexing and Subsetting

NumPy arrays follow indexing structure similar to Python lists. Index starts with 0 and each element in an array is associated with a unique index. Below table shows NumPy indexing for a one-dimensional array.

Index          0      1      2      3      4np.array    52    88       41    63    94

The two arrays arr_1d and arr_2d which depicts the above-shown structure have been created below:

# Creating one-dimensional array
arr_1d = np.array([52, 88, 41, 63, 94])

# Creating two-dimensional array
arr_2d = np.array([['a', 'b', 'c'],
    ...:                    ['d', 'e', 'f'],
    ...:                    ['g', 'h', 'i']])

We use square brackets [] to subset each element from NumPy arrays. Let us subset arrays created above using indexing.

# Slicing the element at index 0
arr_1d[0]

# Slicing the last element using negative index
arr_1d[-1]

# Slicing elements from position 2 (inclusive) to 5 (exclusive)
arr_1d[2:5]

array([41, 63, 94])

In the above examples, we sliced a one-dimensional array. Similarly, square brackets also allow slicing two-dimensional using the syntax [r, c] where r is a row and c is a column.

# Slicing the element at position (0, 1)
arr_2d[0, 1]

# Slicing the element at position (1, 2)
arr_2d[1, 2]

# Slicing the element at position (2, 0)
arr_2d[2, 0]

# Slicing the first row
arr_2d[0, ]

array(['a', 'b', 'c'], dtype='<U1')

# Slicing the last column
arr_2d[:, 2]

array(['c', 'f', 'i'], dtype='<U1')

Notice the syntax in the last example where we slice the last column.The “:” has been provided as an input which denotes all elements and then filtering the last column. Using only “:” would return us all elements in the array.

arr_2d[:]

array([['a', 'b', 'c'],
       ['d', 'e', 'f'],
       ['g', 'h', 'i']], dtype='<U1')

Boolean Indexing

NumPy arrays can be indexed with other arrays (or lists). The arrays used for indexing other arrays are known as index arrays. Mostly,  it is a simple array which is used to subset other arrays.The use of index arrays ranges from simple, straightforward cases to complex and hard to understand cases. When an array is indexed using another array, a copy of the original data is returned, not a view as one gets for slices.To illustrate:

# Creating an array
arr = np.arange(1, 10)

# Printing the array
arr

array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Subsetting the array `arr` using an anonymous array
arr[np.array([2, 5, 5, 1])]

array([3, 6, 6, 2])

We create an array arr with ten elements in the above example. Then we try to subset it using an anonymous index array.The index array consisting of the values 2, 5, 5 and 1 correspondingly create an array of length 4, i.e. same as the length index array.Values in the index array work as an index to subset (in the above-given operation) and it simply returns the corresponding values from the arr.Extending this concept, an array can be indexed with itself. Using logical operators, NumPy arrays can be filtered as desired. Consider a scenario, where we need to filter array values which are greater than a certain threshold.This is shown below:

# Creating an random array with 20 values
rand_arr = np.random.randint(1, 50, 20)

# Printing the array
rand_arr

array([14, 25, 39, 18, 40, 10, 33, 36, 29, 25, 27,  4, 28, 43, 43, 19, 30,
       29, 47, 41])

# Filtering the array values which are greater than 30
rand_arr[rand_arr > 30]

array([39, 40, 33, 36, 43, 43, 47, 41])

Here, we create an array with the name rand_arr with 20 random values. We then try to subset it with values which are greater than 30 using the logical operator >. When an array is being sliced using the logical operator,Python NumPy generates an anonymous array of True and False values which is then used to subset the array. To illustrate this, let us execute the code used to subset the rand_arr, i.e. code written within the square brackets.

filter_ = rand_arr > 30

filter_

array([False, False,  True, False,  True, False,  True,  True, False,
       False, False, False, False,  True,  True, False, False, False,
        True,  True])

It returned a boolean array with only True and False values. Here, True appears wherever the logical condition holds true. Python NumPy uses this outputted array to subset the original array and returns only those values where it is True.Apart from this approach, Python NumPy provides a where method using which we can achieve the same filtered output. We pass a logical condition within where condition, and it will return an array with all values for which conditions stands true.We filter out all values greater than 30 from the rand_arr using the where condition in the following example:

# Filtering an array using np.where method
rand_arr[np.where(rand_arr > 30)]

array([39, 40, 33, 36, 43, 43, 47, 41])

We got the same result by executing rand_arr[rand_arr > 30] and rand_arr[np.where(rand_arr > 30)]. However, the where method provided by Python NumPy just do not filter values. Instead, it can be used for more versatile scenarios.Below given is the official syntax:

np.where[condition[, x, y]]

It returns the elements, either from x or y, depending on condition. As these parameters, x and y are optional, a condition when true yields x if given or boolean True, otherwise y or boolean False.Below we create an array height that contains 20 elements with the height ranging from 150 to 160 and look at various uses of where method.

# Creating an array heights
heights = np.random.uniform(150, 160, size=20)

heights

array([153.69911134, 154.12173942, 150.35772942, 151.53160722,
       153.27900307, 154.42448961, 153.25276742, 151.08520803,
       154.13922276, 159.71336708, 151.45302507, 155.01280829,
       156.9504274 , 154.40626961, 155.46637317, 156.36825413,
       151.5096344 , 156.75707004, 151.14597394, 153.03848597])

Usage 1: Without x and y parametersUsing the where method without the optional parameter as illustrated in the following example would return the index values of the original array where the condition is true.

np.where(heights > 153)

(array([ 0,  1,  4,  5,  6,  8,  9, 11, 12, 13, 14, 15, 17, 19],
       dtype=int64),)

The above codes returned index values of the heights array where values are greater than 153. This scenario is very similar to the one we have seen above with the random array rand_arr where we tried to filter values above 30.Here, the output is merely the index values. If we want the original values, we need to subset the heights array using the output that we obtained.Usage 2: With x as True and y as FalseHaving these optional parameters in place would return either of the parameters based on the condition. This is shown in the below example:

np.where(heights > 153, True, False)

array([True, True, False,  False, True, True, True, False, True,
        True, False, True, True, True, True, True, False, True,
       False, True])

The output in the Usage 2 provides either True or False for all the elements in the heights array in contrast to the Usage 1 where it returned index values of only those elements where the condition was true.The optional parameters can also be an array-like element instead of scalars or static value such as True or False.Usage 3: With x and y being arraysNow that we have quite a good understanding of how the method works, it is fairly easy to guess the output. The output will contain values from either x array or y array based on the condition in the first argument.For example:

# Creating an array 'x_array'
x_array = np.arange(11, 31, 1)

x_array

array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
       28, 29, 30])

# Creating an array 'y_array'
y_array = np.arange(111, 131, 1)

y_array

array([111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
       124, 125, 126, 127, 128, 129, 130])

np.where(heights > 153, x_array, y_array)

array([ 11,  12, 113, 114,  15,  16,  17, 118,  19,  20, 121,  22,  23,
        24,  25,  26, 127,  28, 129,  30])

As expected, the output of the above code snippet contains values from the array x_array when the value in the heights array is greater than 153, otherwise, the value from the y_array will be outputted.Having understood the working of where method provided by the Python NumPy library, let us now see how it is useful in back-testing strategies. Consider a scenario where we have all the required data for generating trading signals.Data that we have for this hypothetical example is the close price of a stock for 20 periods and its average price.

# Hypothetical close prices for 20 periods
close_price = np.random.randint(132, 140, 20)

# Printing close_price
close_price

array([137, 138, 133, 132, 134, 139, 132, 138, 137, 135, 136, 134, 134,
       139, 135, 133, 136, 139, 132, 134])

We are to generate trading signals based on the buy condition given to us. i.e. we go long or buy the stock when the closing price is greater than the average price of 135.45. It can be easily computed using the where method as shown below:

# Average close price
avg_price = 135.45

# Computing trading signals with 1 being 'buy' and 0 represents 'no signal'
signals = np.where(close_price > avg_price, 1, 0)

# Printing signals
signals

array([1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0])

The signals array contains the trading signals where 1 represents the buy and 0 represents no trading signal.

Iterating Over Arrays

NumPy arrays are iterable objects in Python which means that we can directly iterate over them using the iter() and next() methods as with any other iterable. This also implies that we can use built-in looping constructs to iterate over them.The following examples showiterating NumPy arraysusing a for loop.

# Looping over a one-dimensional array
for element in arr_1d:
     print(element)

52
88
41
63
94

Looping over a one-dimensional array is easy and straight forward. But, if we are to execute the for loop with arr_2d, it will traverse all rows and provide that as the output.It is demonstrated in the following example.

for element in arr_2d:
  print(element)

['a' 'b' 'c']
['d' 'e' 'f']
['g' 'h' 'i']

To iterate over two-dimensional arrays, we need to take care of both axes. A separate for loop can be used in a nested format to traverse through each element as shown below:

for element in arr_2d:
 for e in element:
       print(e)

a
b
c
d
e
f
g
h
i

The output that we got can also be achieved using nditer() method of Python NumPy, and it works for irrespective of dimensions.

for element in np.nditer(arr_2d):
   print(element)

a
b
c
d
e
f
g
h
i

This brings us to the end of a journey with the Python NumPy module. The examples provided above depicts only a minimal set of Python NumPy functionalities.Though not comprehensive, it should give us a pretty good feel about what is NumPy and why we should be using it.

Summary

NumPy library is used to perform scientific computing in Python.

It is not a part of the Python Standard Library and needs to be installed explicitly before it can be used in a program.

It allows creating n-dimensional arrays of the type ndarray.

NumPy arrays can hold elements of single data type only.

They can be created using any sequential data structures such as lists or tuples, or using built-in NumPy functions.

The random module of the NumPy library allows generating samples from various data distributions.

NumPy supports for element-wise operation using broadcast functionality.

Similar to lists, NumPy arrays can also be sliced using square brackets [] and starts indexing with 0.

It is also possible to slice NumPy arrays based on logical conditions. The resultant array would be an array of boolean True or False based on which other arrays are sliced or filtered. This is known as boolean indexing.

Conclusion

To reiterate, this article is an excerpt from thePython Basics Handbook, which was created for both; beginners who are starting out inPythonas well as accomplished traders who can use it as a handy reference while coding their strategy.Do let us know if you loved the article and any other feedback in the comments below.Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
