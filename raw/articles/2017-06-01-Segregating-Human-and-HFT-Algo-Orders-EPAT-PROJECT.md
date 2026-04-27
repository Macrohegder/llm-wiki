---
title: "Segregating Human and HFT Algo Orders [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/project-work-segregating-human-hft-algo-orders/"
date: "2017-06-01"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Segregating Human and HFT Algo Orders [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/project-work-segregating-human-hft-algo-orders/)  
**日期**: 2017-06-01  
**作者**: QuantInsti

---

## 原文

Segregating Human and HFT Algo Orders [EPAT PROJECT]

ByNarasimha Sriharsha Kanduri

Introduction

Market price is determined by the participants. The trending and range bound markets are the moods of the participants. By analyzing the participants we can have a wide variety of conclusions. Consider the two extreme participants, HFT Algos and humans.

Now let us analyze human oriented orders. Humans cannot replace the orders hundreds of times per second, nor can they adjust the price in fractions so as to profit from them. On the other hand, the Algos can replace the orders even in a fraction of a second and they try to make profit from even the small edges.

The idea of the study is to segregate the human and machine orders based on the minimum time to replace the order before the execution of the order. If the minimum replace time is more than threshold time Ts, then the order is considered as a human order else HFT algo order. The effectiveness of the segregation is then determined with the sample data that has the human and HFT algo that has the human and HFT algo order details.

Background

The study is based on the historical tick by tick (TBT) sample data. Every tick (order) in the historical data has been attributed to “algo” or “non-algo”. So if we can segregate the orders based on the average replace time (ts), we can compare our effectiveness using the attributes of the historical data.

Implementation

The program for the backtesting is written in python and for some functions, cython library has been used. Below is a flow chart for segregating the trades based on the average replace time.

Functions for calculating the average replace time and segregation of the orders based on the average replace time are added the program. Program for generating confusion matrix from the summary is also given.

Instructions for running the program:

Windows pc with spyder installed and all the modulesrbtree, odict, numpy, pandas, gzip, logging, os, sys, time, csv, copy

rbtree, odict, numpy, pandas, gzip, logging, os, sys, time, csv, copy

Unpack the code

Place the data to be tested in the same folder as the code (let it be datatest.csv)

Compile the c code usingpython .\setup.py build_ext --inplace

python .\setup.py build_ext --inplace

Run the program using\output .\datanew.csv

\output .\datanew.csv

The summary of the all the executed order along with their average modification time, the number of modification is in the summary file

To generate confusion matrixRun classification.py on the summary.csv

Run classification.py on the summary.csv

Python classification.py summary.csv

Conclusions

After the segregation is done, confusion matrix is generated according to the following rule and the results are used for the analysis.

The orders which are algo are classified as algo at a higher percentage when the average replace time is less than 1sec and as the average replace time increases that percentage reduces. For human orders, this percentage doesn’t change much and remains in the range from 36%  to 47% which means there are some algos which have been employed to trade on higher time frames also. And also there is a slight jump in the percentages around 10 seconds threshold.

Note: These conclusions/observations are not final as the market keeps on adjusting itself continuously and the results will change with the latest data.

About the author

Narasimha Sriharsha K. is a full-time trader and market enthusiast. He spends most of his time trying to find the next entry/ exits. He predominantly trades futures and options. His interest in stock markets led him to pursue EPAT™ at QuantInsti®.

Motivation for the project

There is no strategy which works well in all the bull, bear and sideways markets, but by analyzing the behavior of market participants, we can use strategies which are better suitable for the situation. This above premise, the book ‘Market Microstructure’ by Larrys Harris and Mr. Raizada’s lecture on Market Microstructure are the inspiration for this project.

If you want to learn various aspects ofAlgorithmic tradingthen check out theExecutive Programme in Algorithmic Trading (EPAT™). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT™ equips you with the required skill sets to be a successful trader.Enroll now!

---

*Imported from QuantInsti Blog on 2026-04-27*
