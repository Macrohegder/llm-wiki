---
title: "Python Pandas Tutorial: Installation, Series and DataFrame"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-pandas-tutorial/"
date: "2019-09-18"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Pandas Tutorial: Installation, Series and DataFrame

**来源**: [QuantInsti](https://blog.quantinsti.com/python-pandas-tutorial/)  
**日期**: 2019-09-18  
**作者**: QuantInsti

---

## 原文

Python Pandas Tutorial: Installation, Series and DataFrame

ByJay Parmar

Pandasis a Python library to deal with sequential and tabular data. It includes many tools to manage, analyze and manipulate data in a convenient and efficient manner. We can think of its data structures as akin to database tables or spreadsheets.

Pandas is built on top of the Numpy library and has two primary data structures viz. Series (1-dimensional) and DataFrame (2-dimensional). It can handle both homogeneous and heterogeneous data, and some of its many capabilities are:

ETL tools (Extraction, Transformation and Load tools)

Dealing with missing data (NaN)

Dealing with data files (csv, xls, db, hdf5, etc.)

Time-series manipulation tools

In the Python ecosystem, Pandas is the best choice to retrieve, manipulate, analyze and transform financial data.

In this Python Pandas tutorial, we will learn the basics of the Python Pandas module as well as understand some of the codes. This blog article is an excerpt from thePython Basics Handbookcreated for the simple purpose of making the reader understand the beauty and simplicity of thePython language.

The contents of this article include:

Installing Python Pandas

What problem does Python Pandas solve?

Python Pandas Series

Python Pandas DataFrame

Importing data in Python Pandas

Indexing and Subsetting

Manipulating a Python Pandas DataFrame

Statistical Exploratory data analysis

Filtering Python Pandas DataFrame

Iterating Python Pandas DataFrame

Merge, Append and Concat Python Pandas DataFrame

Time-Series in Pandas

Installing Python Pandas

In this section of the Python Pandas tutorial, we will start by going through the official documentation which has a detailed explanationhereon installing Pandas. We summarize it below.

With pip

The simplest way to install Pandas is from PyPI.

In a terminal window, run the following command.

pipinstallpandas

In your code, you can use the escape character '!' to install pandas directly from your Python console.

!pipinstallpandas

Pip is a useful tool to manage Python's packages and it is worth investing some time in knowing it better.

piphelp

With Conda environments

For advanced users, who like to work with Python environments for each project, you can create a new environment and install pandas as shown below.

condacreate-nEPATpythonsourceactivateEPATcondainstallpandas

Testing Pandas installation

To check the installation, Pandas comes with a test suite to test almost all of the codebase and verify that everything is working.

importpandasaspdpd.test()

What problem does Python Pandas solve?

In this section of the Python Pandas tutorial, we will understand the use of Python Pandas.

Python Pandas works with homogeneous data series (1-Dimension) and heterogeneous tabular data series (2-Dimensions). It includes a multitude of tools to work with these data types, such as:

Indexes and labels.

Searching of elements.

Insertion, deletion and modification of elements.

Apply set techniques, such as grouping, joining, selecting, etc.

Data processing and cleaning.

Work with time series.

Make statistical calculations

Draw graphics

Connectors for multiple data file formats, such as, csv, xlsx, hdf5, etc.

Pandas Documentation: 10 minutes with Pandas

Python Pandas Series

The first data structure we will go through in the Python Pandas tutorial is the Series.

Python Pandas Series are homogeneous one-dimensional objects, that is, all data are of the same type and are implicitly labelled with an index.

For example, we can have a Series of integers, real numbers, characters, strings, dictionaries, etc. We can conveniently manipulate these series performing operations like adding, deleting, ordering, joining, filtering, vectorized operations, statistical analysis, plotting, etc.

Let's see some examples of how to create and manipulate a Python Pandas Series:

We will start by creating an empty Python Pandas Series:

importpandasaspds=pd.Series()print(s)Out[]:Series([],dtype:float64)

Let's create a Python Pandas Series of integers:

importpandasaspds=pd.Series([1,2,3,4,5,6,7])print(s)Out[]:01122334455667dtype:int64

Let's create a Python Pandas Series of characters:

importpandasaspds=pd.Series(['a','b','c','d','e'])print(s)Out[]:01122334455667dtype:int64

Let's create a random Python Pandas Series of float numbers:

importpandasaspdimportnumpyasnps=pd.Series(np.random.randn(5))print(s)Out[]:00.38356710.86976121.1009573-0.25968940.704537dtype:float64

In all these examples we saw in the Python Pandas tutorial, we have allowed the index label to appear by default (without explicitly programming it). It starts at 0, and we can check the index as:

In[]:s.indexOut[]:RangeIndex(start=0,stop=5,step=1)

But we can also specify the index we need, for example:

In[]:s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])Out[]:a1.392051b0.515690c-0.432243d-0.803225e0.832119dtype:float64

Let's create a Python Pandas Series from a dictionary:

importpandasaspddictionary={'a':1,'b':2,'c':3,'d':4,'e':5}s=pd.Series(dictionary)print(s)Out[]:a1b2c3d4e5dtype:int64

In this case, the Python Pandas Series is created with the dictionary keys as index unless we specify any other index.

Simple operations with Python Pandas Series

When we have a Python Pandas Series, we can perform several simple operations on it.

For example, in this section of the Python Pandas tutorial, let's create two Series. One from a dictionary and the other from an array of integers:

In[]:importpandasaspddictionary={'a':1,'b':2,'c':3,'d':4,'e':5}s1=pd.Series(dictionary)array=[1,2,3,4,5]s2=pd.Series(array)Out[]:a1b2c3d4e5dtype:int640112233445dtype:int64

We can perform operations similar to Numpy arrays:

Selecting one item from the Python Pandas Series by means of its index:

In[]:s1[0]# Select the first elementOut[]:1In[]:s1['a']Out[]:1In[]:s2[0]Out[]:1

Selecting several items from the Python Pandas Series by means of its index:

In[]:s1[[1,4]]Out[]:b2e5dtype:int64In[]:s1[['b','e']]Out[]:b2e5dtype:int64In[]:s2[[1,4]]Out[]:b2e5dtype:int64

Get the Python Pandas series starting from an element:

In[]:s1[2:]Out[]:c3d4e5dtype:int64In[]:s2[2:]Out[]:233445dtype:int64

Get the Python Pandas series up to one element:

In[]:s1[:2]Out[]:c3d4e5dtype:int64In[]:s2[:2]Out[]:233445dtype:int64

We can perform operations like a dictionary:

Assign a value:

In[]:s1[1]=99s1['a']=99Out[]:a1b99c3d4e5dtype:int64In[]:s2[1]=99print(s2)Out[]:01199233445dtype:int64

Get a value by index (like dictionary key):

In[]:s.get('b')Out[]:2

Here are some powerful vectorized operations that let us perform quickly calculations, for example:

Add, subtract, multiply, divide, power, and almost any NumPy function that accepts NumPy arrays.

s1+2s1-2s1*2s1/2s1**2np.exp(s1)

We can perform the same operations over two Python Pandas Series although these must be aligned, that is, to have the same index, in other cases, perform a Union operation.

In[]:s1+s1# The indices are alignedOut[]:a2b4c6d8e10dtype:int64In[]:s1+s2# The indices are unalignedOut[]:aNaNbNaNcNaNdNaNeNaN0NaN1NaN2NaN3NaN4NaNdtype:float64

Python Pandas DataFrame

The second data structure in Python Pandas that we are going to see is the DataFrame.

Python Pandas DataFrame is a heterogeneous two-dimensional object, that is, the data are of the same type within each column but it could be a different data type for each column and are implicitly or explicitly labelled with an index.

We can think of a Python Pandas DataFrame as a database table, in which we store heterogeneous data. For example, a Python Pandas DataFrame with one column for the first name, another for the last name and a third column for the phone number, or a Python Pandas dataframe with columns to store the opening price, close price, high, low, volume, and so on.

The index can be implicit, starting with zero or we can specify it ourselves, even working with dates and times as indexes as well.

Let's see some examples of how to create and manipulate a Python Pandas DataFrame.

Creating an empty Python Pandas DataFrame:

In[]:importpandasaspds=pd.DataFrame()print(s)Out[]:EmptyDataFrameColumns:[]Index:[]

Creating an empty structure Python Pandas DataFrame:

In[]:importpandasaspds=pd.DataFrame(columns=['A','B','C','D','E'])print(s)Out[]:EmptyDataFrameColumns:[A,B,C,D,E]Index:[]In[]:importpandasaspds=pd.DataFrame(columns=['A','B','C','D','E'],index=range(1,6))print(s)Out[]:ABCDE1NaNNaNNaNNaNNaN2NaNNaNNaNNaNNaN3NaNNaNNaNNaNNaN4NaNNaNNaNNaNNaN5NaNNaNNaNNaNNaN

Creating a Python Pandas DataFrame passing a NumPy array:

In[]:array={'A':[1,2,3,4],'B':[4,3,2,1]}pd.DataFrame(array)Out[]:AB014123232341

Creating a Python Pandas DataFrame passing a NumPy array, with datetime index:

In[]:importpandasaspdarray={'A':[1,2,3,4],'B':[4,3,2,1]}index=pd.DatetimeIndex(['2018-12-01','2018-12-02','2018-12-03','2018-12-04'])pd.DataFrame(array,index=index)Out[]:AB2018-12-01142018-12-02232018-12-03322018-12-0441

Creating a Python Pandas DataFrame passing a Dictionary:

In[]:importpandasaspddictionary={'a':1,'b':2,'c':3,'d':4,'e':5}pd.DataFrame([dictionary])Out[]:abcde012345

Viewing a Python Pandas DataFrame: We can use some methods to explore the Pandas DataFrame:

First, we go to create a Python Pandas DataFrame to work with it.

In[]:importpandasaspdpd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10),'C':np.random.randn(10)})Out[]:ABC00.1643581.6891831.7459631-1.8303850.0356180.04783221.3043392.2368090.92048430.3656161.877610-0.2875314-0.741372-1.443922-1.5668395-0.119836-1.249112-0.1345606-0.848425-0.569149-1.2229117-1.1726880.5154431.49249280.7658360.3073030.78881590.761520-0.4092061.298350

Get the first three rows:

In[]:importpandasaspddf=pd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10),'C':np.random.randn(10)})df.head(3)Out[]:ABC00.1643581.6891831.7459631-1.8303850.0356180.04783221.3043392.2368090.920484

Get the last three rows:

In[]:importpandasaspddf=pd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10),'C':np.random.randn(10)})df.tail(3)Out[]:ABC7-1.1726880.5154431.49249280.7658360.3073030.78881590.761520-0.4092061.298350

Get the Python Pandas DataFrame's index:

In[]:importpandasaspddf=pd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10),'C':np.random.randn(10)})df.indexOut[]:RangeIndex(start=0,stop=10,step=1)

Get the Python Pandas DataFrame's columns:

In[]:importpandasaspddf=pd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10),'C':np.random.randn(10)})df.columnsOut[]:Index(['A','B','C'],dtype='object')

Get the Python Pandas DataFrame's values:

In[]:importpandasaspddf=pd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10),'C':np.random.randn(10)})df.valuesOut[]:array([[0.6612966,-0.60985049,1.11955054],[-0.74105636,1.42532491,-0.74883362],[0.10406892,0.5511436,2.63730671],[-0.73027121,-0.11088373,-0.19143175],[0.11676573,0.27582786,-0.38271609],[0.51073858,-0.3313141,0.20516165],[0.23917755,0.55362,-0.62717194],[0.25565784,-1.4960713,0.58886377],[1.20284041,0.21173483,2.0331718],[0.62247283,2.18407105,0.02431867]])

Importing data in Python Pandas

Python Pandas DataFrame is able to read several data formats, some of the most used are: CSV, JSON, Excel, HDF5, SQL, etc.

CSV to DataFrame

One of the most useful functions isread_csvthat allows us to read csv files with almost any format and load it into our Python Pandas DataFrame to work with it. Let's see how to work with csv files:

importpandasaspddf=pd.read_csv('Filename.csv')type(df)Out[]:pandas.core.frame.DataFrame

This simple operation loads the csv file into the Python Pandas DataFrame after which we can explore it as we have seen before.

Customizing pandas import

Sometimes the format of the csv file comes with a particular separator or we need specific columns or rows. In this section of the Python Pandas tutorial, we will now see some ways to deal with this.

In this example, we want to load a csv file with blank space as separator:

importpandasaspddf=pd.read_csv('Filename.csv',sep=' ')

In this example, we want to load columns from 0 and 5 and the first 100 rows:

importpandasaspddf=pd.read_csv('Filename.csv',usecols=[0,1,2,3,4,5],nrows=100)

It's possible to customize the headers, convert the columns or rows names and carry out a good number of other operations.

Check the IO tools from Pandas documentation.

Importing sheets from Excel files

In the same way that we have worked with csv files, we can work with Excel file with theread_excelfunction, let's see some examples:

In this example, we want to load the sheet 1 from an Excel file:

importpandasaspddf=pd.read_excel('Filename.xls',sheet_name='Sheet1')

This simple operation loads Sheet 1 from the Excel file into the Pandas DataFrame.

Indexing and Subsetting

Once we have the Python Pandas DataFrame prepared, independent of the source of our data (csv, Excel, hdf5, etc.) we can work with it, as if it were a database table, selecting the elements that interest us. We will work with some examples of how to index and extract subsets of data.

Let's begin with loading a csv file having details of a market instrument.

In[]:importpandasaspddf=pd.read_csv('MSFT.csv',usecols=[0,1,2,3,4,5])df.head()df.shapeOut[]:DateOpenHighLowCloseVolume02008-12-2919.150019.2118.6418.9658512800.012008-12-3019.010019.4919.0019.3443224100.022008-12-3119.310019.6819.2719.4446419000.032009-01-0219.532820.4019.3720.3350084000.042009-01-0520.200020.6720.0620.5261475200.0(1000,6)

Here, we have read a csv file, of which we only need the columns of date, opening, closing, high, low and volume (the first 6 columns) and we check the form of the DataFrame that has 1000 rows and 6 columns.

Selecting a single column

In the previous code, we have read directly the first 6 columns from the csv file. This is a filter that we applied because we were only interested in those columns.

We can apply selection filters to the Python Pandas DataFrame itself, to select one column to work with. For example, we could need theClosecolumn:

In[]:close=df['Close']close.head()Out[]:Close018.96119.34219.44320.33420.52

Selecting multiple columns

We can select multiple columns too:

In[]:closevol=df[['Close','Volume']]closevol.head()Out[]:CloseVolume018.9658512800.0119.3443224100.0219.4446419000.0320.3350084000.0420.5261475200.0

Selecting rows via [].

We can select a set of rows by index:

In[]:importpandasaspddf=pd.read_csv('TSLA.csv')df[100:110]Out[]:

Or we can select a set of rows and columns:

In[]:df[100:110][['Close','Volume']]Out[]:CloseVolume100320.084236029.0101320.876942493.0102326.174980316.0103325.848547764.0104337.344463807.0105337.025715817.0106345.104888221.0107351.815032884.0108359.654898808.0109355.753280670.0

Selecting via .loc[] (By label)

Withdf.locwe can do the same selections using labels:

To select a set of rows, we can code the following using the index number as label:

In[]:df.loc[100:110]Out[]:

Or we can select a set of rows and columns like before:

In[]:df.loc[100:110,['Close','Volume']]Out[]:CloseVolume100320.084236029.0101320.876942493.0102326.174980316.0103325.848547764.0104337.344463807.0105337.025715817.0106345.104888221.0107351.815032884.0108359.654898808.0109355.753280670.0110350.605353262.0

Selecting via .iloc[] (By position)

Withdf.ilocwe can do the same selections using integer position:

In[]:df.iloc[100:110]Out[]:

In the last example, we used the index as an integer position rather than by label.

We can select a set of rows and columns like before:

In[]:df.iloc[100:110,[3,4]]Out[]:LowClose100317.25320.08101316.66320.87102323.20326.17103323.56325.84104336.16337.34105336.25337.02106344.34345.10107348.20351.81108354.13359.65109350.07355.75

Boolean indexing

So far in the Python Pandas tutorial, we have sliced subsets of data by label or by position. Now let's see how to select data that meet some criteria. We do this with Boolean indexing. We can use the same criteria similar to what we have seen with Numpy arrays. We show you just two illustrative examples here. This is by no means enough to get comfortable with it and so would encourage you to check the documentation and further readings at the end of this chapter to learn more.

We can filter data that is greater (less) than a number.

In[]:df[df.Close>110]Out[]:

1083 rows × 14 columns

In[]:df[(df['Close']>110)|(df['Close']<120)]Out[]:`

1083 rows × 14 columns

Manipulating a Python Pandas DataFrame

When we are working with data, the most common structure is the DataFrame. We have seen how to create them, make selections and find data in the Python Pandas tutorial. We are now going to see how to manipulate the Python Pandas DataFrame to transform it into another Python Pandas DataFrame that has the form that our problem requires.

We'll see how to sort it, re-index it, eliminate unwanted (or spurious) data, add or remove columns and update values.

.T (Transposing)

The Python Pandas DataFrame transpose functionTallows us to transpose the rows as columns, and logically the columns as rows:

In[]:importpandasaspddf=pd.read_csv('TSLA.csv')df2=df[100:110][['Close','Volume']]df2.TOut[]:

.sort_index()

When we are working with Python Pandas Dataframe it is usual to add or remove rows, order by columns, etc. That's why it's important to have a function that allows us to easily and comfortably sort the Python Pandas DataFrame by its index. We do this with thesort_indexfunction of Pandas DataFrame.

In[]:df.sort_index()Out[]:

.sort_values()

Sometimes, we may be interested in sorting the Python Pandas DataFrame by some column or even with several columns as criteria. For example, sort the column by first names and the second criterion by last names. We do this with thesort_valuesfunction of Python Pandas DataFrame.

In[]:df.sort_values(by='Close')Out[]:

In[]:df.sort_values(by=['Open','Close'])Out[]:

.reindex()

The Python Pandas' reindex function let us realign the index of the Series or DataFrame, it's useful when we need to reorganize the index to meet some criteria.

For example, we can play with the Series or DataFrame that we create before to alter the original index. For example, when the index is a label, we can reorganize as we need:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5),index=['a','b','c','d','e'])dfOut[]:

Now, we can reorganize the index as follows:

In[]:df.reindex(['b','a','d','c','e'])Out[]:

When the index is numeric we can use the same function to order by hand the index:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5))df.reindex([4,3,2,1,0])Out[]:

Later in this section, we'll see how to work and reorganize date and time indices.

Adding a new column. For e.g. df[‘new_column’] = 1

Another interesting feature of Python Pandas DataFrames is the possibility of adding new columns to an existing DataFrame.

For example, we can add a new column to the random DataFrame that we have created before:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5))Out[]:

To add a new column, we only need to include the new column name in the DataFrame and assign an initialization value, or assign to the new column a Pandas Series or another column from other DataFrame.

In[]:df['new']=1dfOut[]:

Delete existing column

Likewise, we can remove one or more columns from the Python Pandas DataFrame. Let's create a DataFrame with 5 rows and 4 columns with random values to delete one column.

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4))dfOut[]:

Now, we can delete the column that we specify by index or by the label if any:

In[]:deldf[0]Out[]:

In[]:df['new']=1dfOut[]:

In[]:deldf['new']Out[]:

.at[] (By label)

Withatwe can locate a specific value by row and column labels as follows:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)df.at['a','A']Out[]:

In[]:df.at['a','A']Out[]:0.9964957014209125

It is possible to assign a new value with the same function too:

In[]:df.at['a','A']=0Out[]:

.iat[] (By position)

Withiatwe can locate a specific value by row and column index as follows:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)df.iat[0,0]Out[]:0.996496

It is possible to assign a new value with the same function too:

In[]:df.iat[0,0]=0Out[]:

Conditional updating of values. For e.g. df[df > 0] = 1

Another useful function is to update values that meet some criteria, for example, update values whose values are greater than 0:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)df[df>0]=1dfOut[]:

We can also update the values of a specific column that meet some criteria, or even work with several columns as criteria and update a specific column.

In[]:df['A'][df['A']<0]=1print(df)Out[]:

In[]:df['A'][(df['B']<0)&(df['C']<0)]=9print(df)Out[]:

.dropna()

Occasionally, we may have a Python Pandas DataFrame that, for whatever reason, includes NA values. This type of values is usually problematic when we are making calculations or operations and must be treated properly before proceeding with them.

The easiest way to eliminate NA values is to remove the row that contains it.

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:

In[]:df['A'][(df['B']<0)&(df['C']<0)]=np.nanprint(df)Out[]:

In[]:df=df.dropna()print(df)Out[]:

Here we are deleting the whole row that has, in any of its columns, a NaN value, but we can also specify that it deletes the column that any of its values is NaN:

df=df.dropna(axis=1)print(df)

We can specify if a single NaN value is enough to delete the row or column, or if the whole row or column must have NaN to delete it.

```pythondf=df.dropna(how='all')print(df)

.fillna()

With the previous function, we have seen how to eliminate a complete row or column that contains one or all the values to NaN, this operation can be a little drastic if we have valid values in the row or column.

For this, it is interesting to use thefillnafunction that substitutes the NaN values with some fixed value.

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:

In[]:df['A'][(df['B']<0)&(df['C']<0)]=np.nanprint(df)Out[]:

In[]:df=df.fillna(999)print(df)Out[]:

.apply()

applyis a very useful way to use functions or methods in a DataFrame without having to loop through it.

We can apply the Apply function to a Series or DataFrame to apply a function to all rows or columns of the DataFrame. Let's see some examples.

Suppose we are working with the randomly generated Python Pandas DataFrame and need to apply a function. In this example, for simplicity's sake, we're going to create a custom function to square a number.

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:`

defsquare_number(number):returnnumber**2# Test the functionIn[]:square_number(2)Out[]:4

Now, let's use the custom function through Apply:

In[]:df.apply(square_number,axis=1)Out[]:

This methodapplythe functionsquare_numberto all rows of the DataFrame.

.shift()

Theshiftfunction allows us to move a row to the right or left and/or to move a column up or down. Let's look at some examples.

First, we are going to move the values of a column downwards:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:

In[]:df['D'].shift(1)Out[]:

We are going to move the values of a column upwards

In[]:df['shift']=df['D'].shift(-1)Out[]:

This is very useful for comparing the current value with the previous value.

Statistical Exploratory data analysis

Python Pandas DataFrame allows us to make some descriptive statistics calculations, which are very useful to make a first analysis of the data we are handling. Let's see some useful functions.

info()

It is a good practice to know the structure and format of our DataFrame, theInfofunction offers us just that:

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:

In[]:df.info()Out[]:<class'pandas.core.frame.DataFrame'>Index:5entries,atoeDatacolumns(total5columns):A5non-nullfloat64B5non-nullfloat64C5non-nullfloat64D5non-nullfloat64shift4non-nullfloat64dtypes:float64(5)memoryusage:240.0+bytes

describe()

We can obtain a statistical overview of the DataFrame with the `describe function, which gives us the mean, median, standard deviation, maximum, minimum, quartiles, etc. of each DataFrame column.

In[]:importpandasaspdimportnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:`

In[]:df.describe()Out[]:

.value_counts()

The functionvalue_countscounts the repeated values of the specified column:

In[]:df['A'].value_counts()Out[]:0.0882791-0.05251510.0602951-0.6332491-1.3529121Name:A,dtype:int64

.mean()

We can obtain the mean of a specific column or row by means of themeanfunction.

In[]:
df['A'].mean()# specifying a columnOut[]:-0.3780203497252693`

In[]:df.mean()# by columndf.mean(axis=0)# by columnOut[]:A-0.378020B-0.371703C0.195449D-0.394319shift-0.638513dtype:float64`

In[]:
df.mean(axis=1)# by rowOut[]:a-0.526386b0.002084c0.001304d-0.659462e-0.382222dtype:float64

.std()

We can obtain the standard deviation of a specific column or row by means of thestdfunction.

In[]:df['A'].std()# specifying a columnOut[]:0.6186812554819784`

In[]:df.std()# by columndf.std(axis=0)# by columnOut[]:A0.618681B1.325046C0.773876D1.054633shift1.041857dtype:float64`

In[]:df.std(axis=1)# by rowOut[]:a1.563475b0.491499c0.688032d0.980517e1.073244dtype:float64

Filtering Python Pandas DataFrame

We have already seen how to filter data in a Python Pandas DataFrame, including logical statements to filter rows or columns with some logical criteria. Let's remember some examples:

For example, we will filter rows whose column 'A' is greater than zero:

In[]:importnumpyasnpdf=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df)Out[]:`

In[]:
df_filtered=df[df['A']>0]print(df_filtered)Out[]:

We can also combine logical statements, we will filter all rows whose column 'A' and 'B' have their values greater than zero.

In[]:df_filtered=df[(df['A']>0)&(df['B']>0)]print(df_filtered)Out[]:

Iterating Python Pandas DataFrame

We can go through the Python Pandas DataFrame row by row to do operations in each iteration, let's see some examples.

In[]:foritemindf.iterrows():print(item)Out[]:('a',A-0.633249B-2.699088C0.574052D0.652742shiftNaNName:a,dtype:float64)('b',A0.060295B-0.150527C0.149123D-0.701216shift0.652742Name:b,dtype:float64)('c',A-0.052515B0.469481C0.899180D-0.608409shift-0.701216Name:c,dtype:float64)('d',A-1.352912B0.103302C0.457878D-1.897170shift-0.608409Name:d,dtype:float64)('e',A0.088279B0.418317C-1.102989D0.582455shift-1.897170Name:e,dtype:float64)

Merge, Append and Concat operation on a Python Pandas DataFrame

Another interesting feature of Python Pandas DataFrames is that we can merge, concatenate them and add new values, let's see how to do each of these operations in this section of Python Pandas tutorial.

mergefunction allows us to merge two Python Pandas DataFrame by rows:

In[]:importnumpyasnpdf1=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df1)Out[]:`

df2=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df2)`

In[]:df3=pd.merge(df1,df2)print(df3)Out[]:EmptyDataFrameColumns:[A,B,C,D]Index:[]

appendfunction allows us to append rows from one Python Pandas DataFrame to another Python Pandas DataFrame by rows:

In[]importnumpyasnpdf1=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df1)df2=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df2)df3=df1.append(df2)print(df3)Out[]

concatfunction allows us to merge two Python Pandas DataFrame by rows or columns:

In[]:importnumpyasnpdf1=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df1)df2=pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])print(df2)df3=pd.concat([df1,df2])# concat by rowprint(df3)Out[]:`

In[]:df3=pd.concat([df1,df2],axis=0)# concat by rowprint(df3)Out[]:`

In[]:df3=pd.concat([df1,df2],axis=1)# concat by columnprint(df3)Out[]:

TimeSeries in Python Pandas

Python Pandas TimeSeries includes a set of tools to work with Series or DataFrames indexed in time.

Usually, the series of financial data are of this type and therefore, knowing these tools will make our work much more comfortable.

In this section of the Python Pandas tutorial, we are going to start creating time series from scratch and then we will see how to manipulate them and convert them to different frequencies.

Indexing Python Pandas TimeSeries

Withdate_rangePanda's method, we can create a time range with a certain frequency. For example, create a range starting on December 1st, 2018, with 30 occurrences with an hourly frequency.

In[]:rng=pd.date_range('12/1/2018',periods=30,freq='H')print(rng)Out[]:DatetimeIndex(['2018-12-01 00:00:00','2018-12-01 01:00:00','2018-12-01 02:00:00','2018-12-01 03:00:00','2018-12-01 04:00:00','2018-12-01 05:00:00','2018-12-01 06:00:00','2018-12-01 07:00:00','2018-12-01 08:00:00','2018-12-01 09:00:00','2018-12-01 10:00:00','2018-12-01 11:00:00','2018-12-01 12:00:00','2018-12-01 13:00:00','2018-12-01 14:00:00','2018-12-01 15:00:00','2018-12-01 16:00:00','2018-12-01 17:00:00','2018-12-01 18:00:00','2018-12-01 19:00:00','2018-12-01 20:00:00','2018-12-01 21:00:00','2018-12-01 22:00:00','2018-12-01 23:00:00','2018-12-02 00:00:00','2018-12-02 01:00:00','2018-12-02 02:00:00','2018-12-02 03:00:00','2018-12-02 04:00:00','2018-12-02 05:00:00'],dtype='datetime64[ns]',freq='H')

We can do the same to get a daily frequency (or any other,see the documentation). We can use thefreqparameter to adjust this.

In[]:rng=pd.date_range('12/1/2018',periods=30,freq='D')print(rng)Out[]:DatetimeIndex(['2018-12-01','2018-12-02','2018-12-03','2018-12-04','2018-12-05','2018-12-06','2018-12-07','2018-12-08','2018-12-09','2018-12-10','2018-12-11','2018-12-12','2018-12-13','2018-12-14','2018-12-15','2018-12-16','2018-12-17','2018-12-18','2018-12-19','2018-12-20','2018-12-21','2018-12-22','2018-12-23','2018-12-24','2018-12-25','2018-12-26','2018-12-27','2018-12-28','2018-12-29','2018-12-30'],dtype='datetime64[ns]',freq='D')

Now, we have aDateTimeIndexin therngobject and we can use it to create a Series or DataFrame:

In[]:ts=pd.DataFrame(np.random.randn(len(rng),4),index=rng,columns=['A','B','C','D'])print(ts)Out[]:`

In[]:ts=pd.Series(np.random.randn(len(rng)),index=rng)print(ts)Out[]:2018-12-010.3492342018-12-02-1.8077532018-12-030.1127772018-12-040.4215162018-12-05-0.9924492018-12-061.2549992018-12-07-0.3111522018-12-080.3315842018-12-090.1969042018-12-10-1.6191862018-12-110.4785102018-12-12-1.036074

Sometimes, we read the data from internet sources or from csv files and we need to convert the date column into the index to work properly with the Series or DataFrame.

In[]:importpandasaspddf=pd.read_csv('TSLA.csv')df.tail()Out[]:

Here, we can see the index as numeric and a Date column, let's convert this column into the index to indexing our DataFrame, read from a csv file, in time. For this, we are going to use the Python Pandasset_indexmethod

In[]:df=df.set_index('Date')df.tail()Out[]:

Now, we have Pandas TimeSeries ready to work.

Resampling Pandas TimeSeries

A very useful feature of Python Pandas TimeSeries is the resample capacity, this allows us to pass the current frequency to another higher frequency (we can't pass to lower frequencies, because we don't know the data).

As it can be supposed, when we pass from one frequency to another data could be lost, for this, we must use some function that treats the values of each frequency interval, for example, if we pass from an hourly frequency to daily, we must specify what we want to do with the group of data that fall inside each frequency, we can do a mean, a sum, we can get the maximum or the minimum, etc.

In[]:rng=pd.date_range('12/1/2018',periods=30,freq='H')ts=pd.DataFrame(np.random.randn(len(rng),4),index=rng,columns=['A','B','C','D'])print(ts)Out[]:`

In[]:ts=ts.resample("1D").mean()print(ts)Out[]:

Manipulating TimeSeries

We can manipulate the Python Pandas TimeSeries in the same way that we have done until now, since they offer us the same capacity that the Pandas Series and the Pandas DataFrames.

Additionally, we can work comfortably with all jobs related to handling dates. For example, to obtain all the data from a date, to obtain the data in a range of dates, etc.

In[]:rng=pd.date_range('12/1/2018',periods=30,freq='D')ts=pd.DataFrame(np.random.randn(len(rng),4),index=rng,columns=['A','B','C','D'])print(ts)Out[]:

Getting all values from a specific date:

In[]:ts['2018-12-15':]Out[]:

Getting all values inside a date range:

In[]:ts['2018-12-15':'2018-12-20']Out[]:

Summary

Let us summarise a few points we learnt in the Python Pandas tutorial

Python Pandas DataFrame and Python Pandas Series are some of the most important data structures. It is a must to acquire fluency in its handling because we will find them in practically all the problems that we handle.

A Python Pandas DataFrame is a data structure formed by rows and columns and has an index.

We must think of them as if they were data tables (for the Array with a single column) with which we can select, filter, sort, add and delete elements, either by rows or columns.

Help in ETL processes (Extraction, Transformation and Loading)

We can select, insert, delete and update elements with simple functions.

We can perform computations by rows or columns.

Has the ability to run vectorized computations.

We can work with several DataFrames at the same time.

Indexing and subsetting are the most important features of Python Pandas.

Facilitates the statistical exploration of the data.

It offers us a variety of options for handling NaN data.

Another additional advantage is the ability to read & write multiple data formats (CSV, Excel, HDF5, etc.).

Retrieve data from external sources (Yahoo, Google,Quandl Python API, etc.)

Finally, it has the ability to work with date and time indexes and offersus a set of functions to work with dates.

Conclusion

To reiterate, this article is an excerpt from thePython Basics Handbook, which was created for both; beginners who are starting out inPythonas well as accomplished traders who can use it as a handy reference while coding their strategy.Do let us know if you loved the article and any other feedback in the comments below.Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
