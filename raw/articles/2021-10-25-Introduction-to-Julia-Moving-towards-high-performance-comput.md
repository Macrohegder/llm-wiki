---
title: "Introduction to Julia | Moving towards high-performance computing"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/julia-programming/"
date: "2021-10-25"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Introduction to Julia | Moving towards high-performance computing

**来源**: [QuantInsti](https://blog.quantinsti.com/julia-programming/)  
**日期**: 2021-10-25  
**作者**: QuantInsti

---

## 原文

Introduction to Julia

This article introduces the Julia programming language, which is specifically designed for scientific computing, that solves the “two-language problem”, i.e. it provides the performance at par with C and the dynamic nature of Python and R.

This series of articles will take you through the journey of getting started with Julia programming tobacktestingand implementing live trading strategies in it.

This is the first article in the series and has the following sections -

What is Julia?

Why do we need another programming language?

Is Julia faster than Python or R?

How to install Julia?

How to run Julia in a Jupyter notebook?

How to install packages in Julia?

Basic packages in Julia

Julia packages for Algorithmic Trading

What is Julia?

Julia is a high-performance programming language specifically designed for efficient numerical computing. It aims to provide high computational speed combined with an easy-to-write programming language.

Julia project was started in 2009 and was released as an open-source language (under MIT license) through ablog postin 2012. Julia 1.0 was released in 2018. The Julia user base has grown widely as the scientific community realised its potential. As of July 2021, Julia has 203,400+ GitHub stars, provides 6000+ registered packages and has over 29 million downloads.

Why do we need another programming language?

The scientific community has always faced a trade-off between the high-performance vs dynamic nature of programming. Programming languages like Matlab, R or Python are widely used in the scientific community.

However, when it comes to solving challenges that require enormously high computation power, the code has to be re-written in languages like C or Fortran to achieve this goal. This is called the “two-language problem”.

Julia claims to solve this challenge by combining the best of both worlds, i.e., speed and easy-to-write language.

Is Julia faster than Python or R?

Let’s look at some benchmarks.

Computation times

The following figure shows the computation time for various languages on different operations (mentioned in the legend). The vertical axis shows each benchmark time normalised against the C implementation.

As we can see, Julia is closest to C for most of the operations, lagging behind LuaJIT and Rust in some cases. It’s much faster than Python or R. More details on this benchmark test can be foundhere.

Multiple operations on large datasets

The below chart compares the task of thegroupbyfunction across various packages. “Query 1” in the figure below is one of the tests performed, and DF.jl (a Julia package) turned out to be the fastest. There are many other queries performedhere.

For query 1: “sum v1 by Id1”: 100 groups of ~10,000,000 rows, Python (pandas package) and R (dplyr package) resulted in an internal error and out of memory error, respectively while Julia took 2.4 seconds the first time and 1.8 seconds the second time.

How to install Julia?

Let’s get started with the installation. Here are the steps to install Julia:

Step 1

Download the current stable version of Julia fromhere.

Step 2

Extract the file and set up Julia using the following commands:

Installing Julia on Linux:

tar -xvzf "downloaded-file-name"

sudo cp -r julia-1.6.3 /opt/

sudo ln -s /opt/julia-1.6.3/bin/julia /usr/local/bin/julia

Open the terminal and type “julia":

Installing Julia on Mac:

Run the downloaded .dmg file

Move the Julia file to the application folder

Click on the Julia icon.

Installing Julia on Windows:

Run the downloaded .exe file

Select the installation directory

Check the box “Add Julia to PATH”

Check the box “Run Julia”

A Julia window is now open, and you’re ready to code in Julia!

How to run Julia in a Jupyter notebook?

To run Julia in a Jupyter notebook, you’ll have to add a package “IJulia” that provides this feature. In your Julia terminal, type:

using Pkg

Pkg.add(“IJulia”)

Julia is now added to your Jupyter Notebook.

Open your Jupyter notebook by typing “jupyter-notebook” on your anaconda terminal.

On the top right corner, click on “New”.

Select “Julia 1.6.3” from the drop-down menu.

You’re now ready to code in Julia using Jupyter Notebook!

How to install packages in Julia?

One of the first steps in getting started with any programming language is installing various packages for different purposes.

To add any packages in Julia, follow these steps:

using Pkg

Pkg.add(“package-name”)

using "package-name"

If you’re familiar with Python, the “using” keyword in Julia is equivalent to “import” in Python and “pip install package-name” in Python is equivalent to “Pkg.add(“package-name”)”. “Pkg” is the package manager in Julia.

For example - The screenshot below is an example of adding the package “CSV.jl”, which is used to read “.csv” files in Julia.

Basic packages in Julia

As I mentioned earlier, there are6000+ registered packagesin Julia.

Here are some packages that will help you get started with the most common operations:

CSV.jlis used to read .csv files,

XLSX.jlcan be used for reading excel sheets,

JLD.jlfor saving and loading Julia variables,

DataFrames.jlis used to manage dataframes.

Plots.jlis used for generating plots.

Images.jlfor image processing,

RCall.jlandPyCall.jlfor using R and Python code in Julia.

For more specific applications, these packages are used:

Mocha.jlfor training neural networks,

Tensorflow.jlandScikitLearn.jlfor ML models,

DifferentialEquations.jlfor solving differential equations.

These packages will be a good starting point on your Julia journey. There are many more useful packages that we will talk about later.

Julia packages for algorithmic trading

Algorithmic trading is an example of a field that requires intensive computing capabilities in some cases. In such a field, processing data faster using an easy-to-write programming language can add a lot of value for traders and investors.

It could also open up the space for non-expert programmers who want to get started and be more actively involved.

Julia has various registered packages available for quantitative finance, such as:

MarketTechnicals.jl- Forfinancial time seriestechnical analysis.

FinancialDerivatives.jl- For financial derivatives modelling and pricing

QuantLib.jl- Aims to provide a Julia version of QuantLib written in C++.

QuantEcon.jl- For quantitative economics

Jib.jl- Julia implementation of Interactive Brokers API

BusinessDays.jl- Highly optimised business days calculator written in Julia

Quandl.jl- For data fromQuandl Python API

YStockData.jl- For data from Yahoo Finance

TradingLogic.jl- For backtesting and live trading

Some of these packages are not very stable since Julia is still an emerging language. They should give us an idea of the possibilities and the enthusiasm for this language in quantitative finance.

Bibliography

https://julialang.org/

https://julialang.org/downloads/

https://juliacomputing.com/

Conclusion

This article provided an introduction to Julia programming language. We looked into the idea behind creating Julia, how to set it up and an idea about a few packages available in it. This article provides the motivation to get started with Julia.

We live in the age of technological revolution; we need to keep up with technological advancements; we need to adapt, like everything else around us, to survive and bring out the best in us.

As Marie Curie once said:

“Nothing in life is to be feared; it is only to be understood. Now is the time to understand more so that we may fear less.”

So, let’s understand!

Future articles in this series will delve into getting started with the basic operations and syntax, data manipulation, visualisation, analysis and much more. Stay tuned!

If you are a trader, a programmer, a student or someone looking to pursue and venture into algorithmic trading then our comprehensive 6 monthExecutive Programme in Algorithmic Trading (EPAT)taught by industry experts, trading practitioners and stalwarts like Dr. E. P. Chan, Dr. Euan Sinclair to name a few - is just the thing for you.

Author:Anshul Tayal

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
