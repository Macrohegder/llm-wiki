---
title: "R Programming Best Practices - R you writing the R way"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/r-best-practices-r-you-writing-the-r-way/"
date: "2017-04-13"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# R Programming Best Practices - R you writing the R way

**来源**: [QuantInsti](https://blog.quantinsti.com/r-best-practices-r-you-writing-the-r-way/)  
**日期**: 2017-04-13  
**作者**: QuantInsti

---

## 原文

R Best Practices: R you writing the R way!

ByMilind Paradkar

Any programmer inevitably writes tons of codes in his daily work. However, not all programmers inculcate the habit of writing clean codes which can be easily be understood by others. One of the reasons can be the lack of awareness among programmers of the best practices followed in writing a program. This is especially the case for novice programmers. In this post, we list some of the R programming best practices which will lead to improved code readability, consistency, and repeatability. Read on!

Best practices of writing in R

1) Describe your code– When you start coding describe what the R code does in the very first line. For subsequent blocks of codes follow the same method of describing the blocks. This makes it easy for other people to understand and use the code.

Example:

# This code captures the 52-week high effect in stocks
# Code developed by Milind Paradkar

2) Load Packages– After describing your code in the first line, use the library function to list and load all the relevant packages needed to execute your code.

Example:

library(quantmod);  library(zoo); library(xts);
library(PerformanceAnalytics); library(timeSeries); library(lubridate);

3) Use Updated Packages– While writing your code ensure that you are using the latest updated R packages. To check the version of any R package you can use the packageVersion function.

Example:

packageVersion("TTR")
[1] ‘0.23.1’

4) Organize all source files in the same directory –Store all the necessary files that will be used/sourced in your code in the same directory. You can use the respective relative path to access them.

Example:

# Reading file using relative path
df = read.csv(file = "NIFTY.csv", header = TRUE)# Reading file using full path
df =  read.csv(file = "C:/Users/Documents/NIFTY.csv", header = TRUE)

5) Use a consistent style for data structure types –R programming language allows for different data structures like vectors, factors, data frames, matrices, and lists. Use a similar naming for a particular type of data structure. This will make it easy to recognize the similar data structures used in the code and to spot the problems easily.

Example:You can name all different data frames used in your code by adding .df as the suffix.

aapl.df   = as.data.frame(read.csv(file = "AAPL.csv", header = TRUE))
amzn.df = as.data.frame(read.csv(file = "AMZN.csv", header = TRUE))
csco.df  = as.data.frame(read.csv(file = "CSCO.csv", header = TRUE))

6) Indent your code– Indentation makes your code easier to read, especially, if there are multiple nested statements like For-loop and If statement.

Example:

# Computing the Profit & Loss (PL) and the Equity
dt$PL = numeric(nrow(dt))
for (i in 1:nrow(dt)){
   if (dt$Signal[i] == 1) {dt$PL[i+1] = dt$Close[i+1] - dt$Close[i]}
   if (dt$Signal[i] == -1){dt$PL[i+1] = dt$Close[i] - dt$Close[i+1]}
}

7) Remove temporary objects –For long codes, running in thousands of lines, it is a good practice to remove temporary objects after they have served their purpose in the code. This can ensure that R does not into memory issues.

8) Time the code –You can time your code using the system.time function. You can also use the same function to find out the time taken by different blocks of code. The function returns the amount of time taken in seconds to evaluate the expression or a block of code. Timing codes will help to figure out any bottlenecks and help speed up your codes by making the necessary changes in the script.

To find the time taken for different blocks we wrapped them in curly braces within the call to the system.time function.

The two important metrics returned by the function include:
i) User time - time charged to the CPU(s) for the code
ii) Elapsed time - the amount of time elapsed to execute the code in entirety

Example:

# Generating random numbers
system.time({
mean_1 = rnorm(1e+06, mean = 0, sd = 0.8)
})

user    system    elapsed
0.40      0.00       0.45

9) Use vectorization –Vectorization results in faster execution of codes, especially when we are dealing with large data sets. One can use statements like the ifelse statement or the with function for vectorization.

Example:Consider the NIFTY 1-year price series. Let us find the gap opening for each day using both the methods (using for-loop and with function) and time them using the system.time function. Note the time taken to execute the for-loop versus the time to execute the with function in combination with the lagpad function.

library(quantmod)
# Using FOR Loop
system.time({
df = read.csv("NIFTY.csv")
df = df[,c(1,3:6)]
df$GapOpen = double(nrow(df))
for ( i in 2:nrow(df)) {
df$GapOpen[i] = round(Delt(df$CLOSE[i-1],df$OPEN[i])*100,2)
}
print(head(df))
})

# Using with function + lagpad, instead of FOR Loop
system.time({
df = read.csv("NIFTY.csv")
df = dt[,c(1,3:6)]

lagpad = function(x, k) {
c(rep(NA, k), x)[1 : length(x)]
}

df$PrevClose = lagpad(df$CLOSE, 1)
df$GapOpen_ = with(df, round(Delt(df$PrevClose,df$OPEN)*100,2))
print(head(df))
})

10) Folding codes– Folding codes is a way wherein the R programmer can fold a code of line or code sections. This allows hiding blocks of code whenever required, and makes it easier to navigate through lengthy codes. Code folding can be done in two ways:
i) Automatic folding of codes
ii) User-defined folding of codes

Automatic folding of codes:RStudio automatically provides the flexibility to fold the codes. When a coder writes a function or conditional blocks, RStudio automatically creates foldable codes.

User-defined folding of codes:One can also fold a random group of codes by using Edit -> Folding -> Collapse or by simply selecting the group of codes and pressing Alt+L key.

User-defined folding can also be done via Code Sections:To insert a new code section you can use the Code -> Insert Section command. Alternatively, any comment line which includes at least four trailing dashes (-), equal signs (=) or pound signs (#) automatically creates a code section.

11) Review and test your code rigorously –Once your code is ready, ensure that you test it code rigorously on different input parameters. Ensure that the logic used in statements like for-loop, if statement, ifelse statement is correct. It is a nice idea to get your code reviewed by your colleague to ensure that the work is of high quality.

12) Don’t save your workspace–When you want to exit R it checks if you want to save your workspace. It is advisable to not save the workspace and start in a clean workspace for your next R session. Objects from the previous R sessions can lead to errors which can be hard to debug.

These were some of the best practices of writing in R that one can follow to make your codes easy to read, debug and to ensure consistency.

Next Step

“Shorting at High”is one of the strategies that is formulated as project work. This post explains the strategy in brief and the coding part.

Disclaimer:All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
