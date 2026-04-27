---
title: "DBSCAN vs K-Means: Overcoming Clustering Limitations in Machine Learning"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/dbscan-vs-kmeans/"
date: "2025-02-06"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# DBSCAN vs K-Means: Overcoming Clustering Limitations in Machine Learning

**来源**: [QuantInsti](https://blog.quantinsti.com/dbscan-vs-kmeans/)  
**日期**: 2025-02-06  
**作者**: QuantInsti

---

## 原文

DBSCAN Vs K-Means

ByRekhit Pachanekar

You know that machine learning can be broadly categorised into supervised and unsupervised learning. Supervised learning uses labelled data, where the model learns from input-output pairs to make predictions or classifications.

On the other hand, unsupervised learning works with unlabeled data to discover hidden patterns or structures. For instance, it can group similar items together or identify overarching trends, such as market regimes.

In the realm of unsupervised learning, K-means clustering is a popular choice among analysts. If you ask anyone for a one line explanation of K-means, they will tell you that it organises data into distinct groups based on similarity. That’s pretty good, but everything has its limitations and K-means is no exception.

So today, we will first delve a bit on how K-means works, its limitation and how DBSCAN model can overcome these limitations. Along the way, we will use examples so it doesn’t feel like a theoretical lecture. Let us first start with the content in this blog.

Prerequisites

To fully benefit from the concepts discussed here, it’s crucial to have a solid foundation. Refresh your fundamentals, start with these blogs:

An Introduction to Unsupervised Learning for Trading– Discover how techniques like clustering can unearth hidden market patterns.

K-Means Clustering Algorithm for Pair Selection in Python– Learn how to apply K-Means to identify potential pair trades and automate the process in Python.

We will cover the following topics:

Brief Description of the K-means Clustering Algorithm

Limitation of the K-means Clustering Algorithm

How does DBSCAN overcome the limitation of K-means

Brief Description of the K-means Clustering Algorithm

To illustrate how K-means algorithm works, we will take an example in the trading domain to understand the process of K-means clustering algorithm.

Let’s say you're observing the stock price of Apple. Each day, you calculate two technical indicators for Apple:RSI(which measures overbought or oversold conditions) andADX(which measures trend strength).

You think to yourself, can I know if the stock is in a bullish, bearish or sideways phase by looking at these two indicator values?

For example, if both RSI and ADX indicator values are high, you might assume that the stock is in the bullish phase.

But what should be the threshold to decide that the stock is in the bullish phase?

This is where you could use the unsupervised learning model: K-means.

Let’s see how you can use K-means clustering to classify the stock's behaviour into different regimes:

First, decide how many regimes you want to classify the stock into. For simplicity, let's choose K = 3. These three clusters will represent potential stock regimes: bullish, bearish, and sideways range.

Next, the algorithm first randomly select three initial "centres" in the RSI-ADX space. Think of these centres as hypothetical regimes that the model will adjust to better represent the actual data.

For each day in your dataset:

The algorithm checks its RSI and ADX values. Then it will calculate the distance between that day's data point and each of the three centres. And finally, it will assign the day to the cluster whose centre is closest.

For example:

- A day with a high RSI and a high ADX might be assigned to the bullish cluster.

- A day with a low RSI and a low ADX might fall into the bearish cluster.

- A day with moderate RSI and low ADX might belong to the sideways range cluster.

After assigning all days to clusters, the algorithm again calculates the average RSI and ADX values of all days in each cluster. These averages become the new centres of the clusters. The clusters now represent the actual "centres" of the regimes based on your data.

This process is repeateduntil the centres stop moving significantly.

Now, you will have three clusters classifying the stock data into bullish, bearish, and sideways range regimes.

This sounds great! So what exactly is the limitation of K-means?

Limitation of the K-means Clustering Algorithm

The k in k means has to be decided beforehand. Ideally, we can use the ‘within-cluster-sum-of-squares’ or WCSS method to find the ideal number of clusters.

But there can be times when there is no apparent decline in the graph.

K means uses a centroid (centre point) and considers points in a cluster, “cluster” or stick together. Another way to explain is it assumes that clusters are spheres of equal size. But there can be times when this is not the case. What if the clusters are not regularly shaped?

Here, you can see that there are two circles, inner and outer circle. And you will cluster the points in the same manner. But K-means clustering algorithm thinks differently.

The k means algorithm will split it into two to form two clusters, as shown above.

You can see that A and B have more in common with each other but due to the centroid based distance approach, they are in different clusters.

Is there a different approach which can work better?

Yes! Let’s see how the DBSCAN algorithm overcomes this limitation.

How does DBSCAN overcome the Limitation of K-means

Density-based spatial clustering of applications with noise (DBSCAN) is a clustering technique that can deal with the noise in the data.

The unique thing about this algorithm is that you don’t have to set the number of clusters beforehand. The algorithm does that work for you!

DBSCAN clustering requires two parameters.

Distance parameter: It is the maximum distance between two points for them to be in the neighbourhood of each other. We will call this epsilon.

Minimum number of points required in the cluster, including itself, in the neighbourhood of a point.

But how do you define the neighbourhood of a point?

Let’s take an example. Consider a point.

If we draw a circle with a point as it's centre and radius equal to epsilon. The circle is called the neighbourhood of the point. Based on the dataset you are working with, you can define the neighbourhood of the point.

Let’s see how the DBSCAN clustering method works now. Consider the points as shown below.

First we will set the parameters of DBSCAN as follows:

Epsilon equals to 2

Minimum number of points as 4.

We will go through the graph one by one.

For point A, draw a circle with radius 2 units around it.

How many points do you see in the neighbourhood of point A? None. Hence, point A is an outlier. It will not be a part of the cluster.

Next, move the circle to point B.

As you can see, it has 4 points in it’s neighbourhood. This is equal to the minimum number of points required. Such a point is called a core point.

Let's represent the core point using a colour, say red. And all the other points in its neighbourhood by using light red. The light red points are called the boundary points.

We will continue to move the circle to point C. As point C has 4 points in its neighbourhood, it is also a core point.

Is point D also a core point? No. It has only 3 points, including itself, in its neighbourhood. Therefore it is not a core point. It is a boundary point.

What about point E? It has only 2 points in its neighbourhood.

A point is classified into a cluster if it is a core point. A point is also classified into a cluster if it is a boundary point in the neighbourhood of a core point, i.e. if it lies at a distance of less than epsilon from a core point.

Point E does not satisfy any of the given criteria. Hence, it does not classify into a cluster and is treated as an outlier.

Next, consider the 4 points at the bottom-left. Will they belong to a cluster? All the 4 points lie in the neighbourhood of point F.

Hence, they form a cluster. We will represent this cluster in blue colour.

Not only point F, but all the other points in the cluster are also core points.

Therefore, we have two clusters with the given points.

This is essentially how the DBSCAN algorithm works. It creates clusters based on the density of the points, i.e. the number of points in the neighbourhood of a point. And this is the motivation behind the name of the algorithm.

That’s great, isn’t it?

The DBSCAN clustering improved the way the K-means algorithm works. You can use the sklearn python library to implement the DBSCAN algorithm in your Python notebook.

You can learn more about the working of each K-means and DBSCAN clustering by exploring the course titledUnsupervised Learning in Trading!

Conclusion

While the K-means algorithm is a robust clustering algorithm, it has certain limitations which might limit the scope of implementation. Also, you need to specify the clusters to be formed, which lead to certain bias. In contrast, the DBSCAN algorithm uses a different approach to cluster datapoints based on the density or distribution of the datapoints.

Continue Learning:

1. Expand your knowledge with the following blogs:

K-Nearest Neighbors Algorithm: Steps to Implement in Python– A beginner-friendly guide that walks you through using KNN for classification and regression.

Top 10 Machine Learning Algorithms for Beginners– Get a quick rundown of popular ML algorithms and how they fit into trading strategy design.

For a deeper dive, download ourMachine Learning for Trading eBook, which covers the core concepts in more detail and provides practical tips for building ML-driven strategies.

2. Deep Dive with Quantra

If you’re ready to go a step further,Quantra's Learning Track on Artificial Intelligence in Trading Advancedoffers a structured learning track from Intermediate to Advanced. This progression helps you steadily build expertise on complete lifecycle of strategy creation and backtesting using advanced artificial intelligence in trading, including neural network, deep learning, and LLMs.

3. Taking a Structured Approach with EPAT

For a comprehensive, hands-on program that covers the entire spectrum of algorithmic trading and machine learning, consider theExecutive Programme in Algorithmic Trading (EPAT).

Check out the EPAT Projects by Students:

Prediction of the price trend of Metals with Machine Learning

Portfolio Assets Allocation with Machine Learning

Building a Machine Learning model for a Long-only strategy to be used as a Retail Trader

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
