---
title: "Python Data Visualization using Bokeh for algo traders and quants"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/python-data-visualization-using-bokeh/"
date: "2016-11-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Python Data Visualization using Bokeh for algo traders and quants

**来源**: [QuantInsti](https://blog.quantinsti.com/python-data-visualization-using-bokeh/)  
**日期**: 2016-11-07  
**作者**: QuantInsti

---

## 原文

Data Visualization In Python Using Bokeh

A picture is worth a thousand words or said a wise woman a hundred years ago. True to every word of the idiom, the beauty of visualization lies in how clearly it might convey multiple messages. Visualization of data is one of the key functions of a data scientist and decoding the visual messages is of primary importance to the algo trader. The patterns (both hidden and the obvious) are of utmost importance to the traders and analysts as they decide theirtrading strategyand next move based on these interpretations.

Python offers cool ways of creating appealing plots and graphics. Some of the popular packages includeMatplotlib, Bokeh,PlotlyandSeaborn. In this blog post we will explore Bokeh, which is a Python interactive visualization library that uses modern web browsers for presentation. Using Bokeh one can quickly and easily create interactive plots, dashboards, and data applications.

Bokeh for Python Data Visualization

Bokeh is a Python interactive visualization library that uses modern web browsers for presentation. Using Bokeh we can quickly create interactive plots, dashboards, and data applications with ease[1]

Bokeh’s ultimate objective is to give graceful looking and apt visual depictions of data in the form of D3.js. Bokeh is useful for all those who wish to quickly and easily create interactive plots, dashboards, and data applications. Let us see how Python Data Visualization is done using Bokeh.

Plot Types

The main plot types in Bokeh are:

Server App plots

These are connected to the Bokeh server, and the data can be updated which in turn updates the plot and the UI.

Standalone plots

These plots do not use the Bokeh server. However, they still have many interactive tools and features, including linked panning, brushing, and hover inspectors.

Installing Bokeh

Installing Bokeh is simple and can be installed in python from PyPI (Python Package Index) using the following pip command:

pip install bokeh

Alternatively, Anaconda users can simply run the command:

conda install bokeh

This will install the most recent published Bokeh release from the Continuum Analytics Anaconda repository, along with all the dependencies.

Some of the Bokeh examples rely on sample data that is not included in the Bokeh GitHub repository or released packages, due to their size. Once Bokeh is installed, the sample data can be obtained by executing the following command in a Python interpreter:

Getting Started in Bokeh

The architecture of Bokeh is such that high-level “model objects” (representing things like plots, ranges, axes, glyphs, etc.) are created in Python, and then converted to a JSON format that is consumed by the client library, BokehJS. BokehJS renders the visuals and handles the UI interactions for Bokeh plots and widgets in the browser.

Bokeh offers two main interfaces that include:

bokeh.models

A low-level interface which provides complete control over how Bokeh plots and Bokeh widgets are put together and configured. Most of the models are very simple, usually consisting of a few property attributes and no methods.

bokeh.plotting

A mid-level interface which provides a convenient way to create plots centred around glyphs. Glyphs are the basic visual building blocks of Bokeh plots, e.g. lines, rectangles, squares, wedges, patches, etc.

There are various ways to generate output for Bokeh documents. They include:

output_file- Generates simple standalone HTML documents for Bokeh visualizations

output_notebook- Displays Bokeh visualizations inline inJupyter notebookcells

These functions are most often used together with the show or save functions.

Let us now plot some charts which will demonstrate the ease and power of Bokeh plots. We will explain the bokeh functions, methods, and attributes as we take you through the charting examples illustrated below.

Example 1: NIFTY Sectoral Indices Performance

Let us start with this example by plotting the NIFTY Sectoral Indices performance over the last one year. The names of the different sectors and the corresponding yearly returns are contained in the lists; “factors” and “x”. We create a dot object using the figure function from bokeh.plotting, and apply the “segment”, and the “circle” methods to draw the lines and the circle at the end of the lines in the dot plot.

Since the returns include both positive as well as negative returns, we have usedif elsestatement in afor loop, and have created a list (LineColor) wherein a “green” colour is assigned to positive returns and a “red” colour for negative returns.

In the “output_file” function we have specified file type and file name. The “show” function displays the plot in the html format.

Example 2: NIFTY Media Stocks Performance

You can see from the plot above, the Media Sector gained the most (approx.30%) in the last one year. Now let us visualize the gains clocked by the various stocks comprising the NIFTY Media Sector. The stock returns data is loaded using the read_csv function from pandas. Next, we use the Scatter function from bokeh.charts to create the ‘scatter’ object. We specify the stock names on the x-axis, and plot the returns on the y-axis. The “show” function displays the scatter plot in html format. You can also save the plot using the “save” function.

Example 3: Comparing TVTODAY Vs NIFTY series

What did you observe from the scatter plot?

We can see that TVTODAY stock was one of the top performing stocks in the NIFTY Media sector clocking more than 40% returns in the last one year. Let us now plot the TVTODAY price series and compare it with the NIFTY index. We load the TVTODAY and the NIFTY price series data using read_csv function from pandas. Using the figure function we create ‘n’ object, and plot the TVTODAY price series using the line method. Similarly, we plot the NIFTY time series.

To display the time series plots one below another we use the “column” function from bokeh.layouts and pass the ‘n’ and ‘p’ objects to the “column” function which is nested in the “show” function (Last line of the code). This will produce time series plots one below another.

Example 4: TVTODAY Quarterly Y/Y Sales & Profit growth

Comparing the two price series above, we can observe that TVTODAY stock saw a sharp upside move during the period Nov’15 – Jan’16, while NIFTY trended downwards during the same time frame. Can the TVTODAY stock fundamentals explain the sharp upside? We looked at the sales and profit growth numbers for TVTODAY stock and plotted a bar plot covering the last four quarters.

For plotting, we create a dictionary which contains the fundamental data (sales and net profit) for the last four quarters and apply it to the “Bar” function from bokeh.charts.

From the bar plot, we deduce that TVTODAY saw good results for the Sep’15, Dec’15, and the Mar’16 quarters. Also, there was favourable news for the company in the early December month, which allowed for NRI investment in the company. The good quarterly results and the favourable news gives some explanation for the upside move seen during Nov’15 – Jan’16.

Here is a great article toreadon implementing Python codes in Interactive Brokers API.

To Conclude

As illustrated by the examples above, Bokeh is very user-friendly, feature-rich, and can be used to create interactive charts easily. The extensive documentation of various interfaces, functions, methods on its site makes it easy for the beginners to learn bokeh.

Useful links from the Bokeh site

Installation- This section details the installation process of BokehReference guide- This document provides the complete API reference for BokehPlotting with Basic Glyphs- Details Bokeh plots created using the bokeh.plotting interfaceHandling Categorical Data- Details handling categorical data in Bokeh plotsAdding Annotations– Details supplemental information that can be added to the visualizations

Next Step

Learn the basic operations that can be performed on stock data using Python to analyze and build algorithmic trading strategies. In our article 'Basic Operations On Stock Data Using Python' we run through some basic operations that can be performed on a stock data using Python and we start by reading the stock data from a CSV file.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

List of files in the zip archive:

Data files as input

Python codes for all examples

HTML files containing output

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
