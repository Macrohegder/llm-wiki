---
title: "Data Manipulation and Visualization Techniques in Julia"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/data-manipulation-visualization-using-julia/"
date: "2022-03-28"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Data Manipulation and Visualization Techniques in Julia

**来源**: [QuantInsti](https://blog.quantinsti.com/data-manipulation-visualization-using-julia/)  
**日期**: 2022-03-28  
**作者**: QuantInsti

---

## 原文

Data Manipulation and Visualization Techniques in Julia

In this article, we’ll look at data manipulation and visualization techniques in Julia. However, I’ll not get into the details of each parameter of every function, as the objective of this series is to use Juliaas a toolto achieve our goal, i.e.building andbacktesting trading strategies. So, we’ll stay focused on that.

You can refer to the detailed documentation of a function if you need it to solve any particular challenge you face while programming.

This article is divided into the following sections:

Data manipulationCreating new dataframesIndexing and summarising dataBasic mathematical operationsGeneral operationsGrouping dataDealing with missing data

Creating new dataframes

Indexing and summarising data

Basic mathematical operations

General operations

Grouping data

Dealing with missing data

Importing and exporting data as CSV and excel files

Data visualizationLine plotAttributes of a plotScatter plotHeatmapHistogramPie chartPlotting mathematical functionsSaving plotsAnimated plotsVarious packages for plotting in Julia

Line plot

Attributes of a plot

Scatter plot

Heatmap

Histogram

Pie chart

Plotting mathematical functions

Saving plots

Animated plots

Various packages for plotting in Julia

In my previous posts in this Julia programming series, Iintroduced the languageand started with thebasic syntax of Julia programming. You can check that out as well.

Data manipulation

You need to understand the data structures dealing with large heterogeneous data sets whenever you work with any programming language. In the Julia world, they are called dataframes.

Julia’s DataFrames.jl package provides a way to structure and manipulate data.

It can be installed using the “Pkg” module.

Creating new dataframes

Here’s an example of creating a new dataframe.

Output:

Column names can be accessed using the names() function.

Output:

3-element Vector{String}:
"Name"
"Team"
"Work_experience"

3-element Vector{Symbol}:
:Name
:Team
:Work_experience

Renaming columns can be done using the rename() function.

Indexing and summarising data

Indexing dataframes to use particular rows or columns for manipulation is a fundamental operation, and summarising data helps us understand it better. In Julia, summary stats of any dataset can be printed using the describe() function.

Another way to find the number of rows and columns in a dataframe is using ncol() and nrow() functions.

Output:
2
10

Let’s look at multiple methods of accessing rows and columns of a dataframe.

Output:
4-element Vector{String}:
"Vivek"
"Viraj"
"Rohan"
"Ishan"

4-element Vector{String}:
"EPAT"
"Marketing"
"Sales"
"Quantra"

3-element Vector{String}:
"EPAT"
"Marketing"
"Sales"

Basic mathematical operations

As discussed in my previous post, basic arithmetic operations can be performed on individual columns.

10-element Vector{Float64}:

-0.5474996670806442
 0.5174063588946236
-0.564150142575268
 0.12873854328766576
 0.2741519215981265
 0.20241852864291987
 0.09324017568958975
-0.41716724316286524
 0.2693306887583933
-0.5967498723478988

You’ll have to use the “.” operator for element-wise division.

10-element Vector{Float64}:

0.06754620232737023
3.013387340201863
0.4169119702423886
1.2293455286486041
1.4462537614868343
8.482279426917298
1.1103752688515762
0.21238611891693882
3.1244976300403002
0.38733760512833965

Basic operations

Rearranging columns

r” is a regex search string. Here, any column with a string “work” will be selected and moved to the first place. You can write the full column name as well.

Adding a new column in a dataframe

Here we add another column, “c”, to the dataframe df_2.

Dataframe-to-matrix conversion

10×3 Matrix{Float64}:

0.0396604  0.58716    0.741712
0.774389   0.256983   0.429361
0.403371   0.967521   0.989583
0.690069   0.56133    0.50599
0.888493   0.614341   0.152574
0.229472   0.0270531  0.932589
0.937996   0.844756   0.0745573
0.112492   0.52966    0.712178
0.396105   0.126774   0.397762
0.377277   0.974027   0.685073

Grouping data

Let’s look at ways to group data, which comes in handy while summarising data.

In-built datasets in Julia

The package RDatasets.jl in Julia helps you import all the in-build packages in R that can be used for testing purposes.

Here’s how you can find out the list of available datasets. It has 763 datasets.

We’ll work with one of the in-built datasets (“iris”) in this section. “iris” provides the data for multiple measurements of 3 plant species and 4 features for each of them. More details about this dataset can be foundhere.

The following snapshot shows the variables in the iris dataset.

Here’s the summary of this dataset.

Let’s look at some of the questions you might want to answer using the iris dataset.

We can perform arithmetic operations by grouping data based on various columns. Here’s how we can get the answer to the following question -

What’s the mean value of the sepal length of each species?

Another package that helps make the operations more intuitive is Pipe.jl. It lets you write operations as they are performed instead of the backward approach.

Dealing with missing data

Julia has a “missing” object that is used for unavailable data. You can use skipmissing() function to perform operations ignoring the missing values.

Output:

You can use dropmissing() function to remove the missing values.

More details for dealing with missing values can be foundhere.

Importing and exporting data as CSV and Excel files

Reading data is the first step in analysing any kind of data. Most of the information we come across is either in CSV or excel format, so we’ll focus on these two. We will work with CSV.jl and XLSX.jl for dealing with CSV and Excel files.

Reading and writing CSV files

We’ll read a CSV file (infy.csv), as a dataframe, containing historical stock price data for Infosys downloaded from Yahoo finance for the period 21-Dec-2020 to 22-Dec-2021.

Here’s a summary for this data.

Here, we calculate the range -

This updated dataframe can be saved using CSV.write() function.

Reading and writing excel files

We’ll use the XLSX.jl package in Julia to read and write excel files.

Here’s how it can be done -

We can write an excel file using the writetable() function.

Julia has in-built read() and write() open() close() functions to work with text files. More details can be foundhere.

Data can be written in .jld format as well. .jld is Julia’s data format built using the JLD.jl package.

Details for the following packages can be found here -

JLD.jl

CSV.jl

Other formats

Data visualization

Data visualization is crucial for understanding and analysing data. We’ll now look at some of the plots using Plots.jl. Plots.jl is one of the commonly used plotting libraries in Julia.

Line plot

Here’s a simple line plot.

Attributes of a plot

The following attributes can be added to the plot. These attributes can be used for all the plots discussed in this article.

xlabel- For x-axis label

ylabel- For y-axis label

title- Title of the plot

ylims- Range of y-axis

xlims- Range of the x-axis

label- Label names in the legend

linewidth/lw- For adjusting the width of the line

color- For adding specific colours to the lines

legend- Require legend or not and position of the legend. It can take: “topleft”, “topright”, “bottomleft”, “bottomright”, “right”, “bottom”, “top”, “right”, true, false

layout- For adding multiple plots in the same image.

size -Size of the plot

This list is not exhaustive; many attributes can be used. However, as I have mentioned earlier, we’ll stay focused on the question: How do we use Julia to achieve our goal?

The attributes presented above are most commonly used and should suffice for creating plots.

Here’s an example that combines all the features mentioned above.

Scatter plot

Scatter plots can be generated using multiple methods. Here are a few examples -

Heatmap

Histogram

Pie chart

Here’s a sample layout with different plots.

Plotting mathematical functions

Here are some plots of mathematical functions.

Saving plots

The plot generated can be saved in various formats using the savefig() function.

Animated plots

We can also use the plots and covert and save them as gifs or videos.

Lorenz attractor

The following is the code of the Lorenz attractor as seen in theJulia documentation:

More details about animated plots can be foundhere.

Various packages for plotting in Julia

Plots.jl is the basic plotting library in Julia. There are other packages for visualization such as -

GadFly.jl

GoogleCharts.jl

Makie.jl

PyPlot.jl

PGFPlotsX.jl

UnicodePlots.jl and

VegaLite.jl

Conclusion

This article covers the foundations of data manipulation and visualization using Julia.

In the following article, we’ll look at methods to get timeseries data for stock prices and analyse it using the tools presented in this article. Until then, take this article as a building block and explore the aspects you found interesting in detail!

However, if you are looking to pursue and venture into algorithmic trading then our comprehensivealgo trading coursetaught by industry experts, trading practitioners and stalwarts like Dr. E. P. Chan, Dr. Euan Sinclair to name a few - is just the thing for you. Enroll now!

Author:Anshul Tayal

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
