---
title: "Boruta-Shap algorithm | A CPU and GPU version"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/boruta-shap-gpu-python/"
date: "2024-07-01"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Boruta-Shap algorithm | A CPU and GPU version

**来源**: [QuantInsti](https://blog.quantinsti.com/boruta-shap-gpu-python/)  
**日期**: 2024-07-01  
**作者**: QuantInsti

---

## 原文

The Boruta-Shap Algorithm: A CPU and GPU version

ByJosé Carlos Gonzáles TanakaAfter you do feature engineering, feature importance is a key step before deploying a strategy backtesting code. Boruta-Shap comes as a viable source for that purpose. However, this algorithm might take a lot of time to run with large datasets. This unique article provides us with an estimation of the mentioned algorithm using CPU parallelism and GPU to make it run faster. Code will be implemented using the XGBoost library and futures library for CPU parallelism. You can find the Boruta-Shap algorithm code onGitHubas well.

We will cover:

What is the Boruta-Shap algorithm?

How the Boruta-Shap algorithm works

Significance of Boruta-Shap

Accelerating Boruta-Shap Algorithm

A CPU-and-GPU-based algorithm to run quicker the Boruta-Shap algorithm

What is the Boruta-Shap algorithm?

The Boruta-Shap algorithm is a good technique for feature selection, especially inmachine learninganddata scienceapplications, is the Boruta-Shap algorithm. Boruta-Shap combines the Boruta feature selection process with the Shapley values to enhance feature importance assessment.

How the Boruta-Shap algorithm works

The Boruta-Shap algorithm works in the following way:

First, we create shuffled versions of all the input features.

Second, Boruta is used to identify a tentative set of important features using amachine learning model.

Then, Shapley values are calculated for these tentative features using the above model (often a tree-based model likeRandom ForestorGradient Boosting Machine). The tentative features are chosen based on comparing their usefulness with respect to their shuffled versions.

The Shapley values provide a more nuanced understanding of feature importance, capturing interactions between features and their impact on model predictions.

Finally, features are ranked based on their Shapley values, helping to prioritize the most influential features for model training and interpretation.

Significance of Boruta-Shap

The Boruta-Shap algorithm has the following benefits.

Robustness - it can produce accurate feature importance rankings even for noisy, high-dimensional datasets.

Interpretability is aided by the use of Shapley values, which provide information on how each feature affects model predictions.

Boruta-Shap considers feature interactions and the value of individual features, which is important in complex datasets.

This algorithm is used before you do feature engineering.

Industry expert and renowned author, Dr. Ernest Chan talks about Financial Data Science & Feature Engineering and shares his knowledge in this clip:

Accelerating Boruta-Shap Algorithm

Despite Boruta-Shap's strength, its computational cost can be high, particularly for large datasets with many characteristics. To solve this, I've included a Boruta-Shap code that uses the CPU and GPU in tandem to expedite the Boruta-Shap's execution. Cool, right?

This approach drastically cuts computation time by effectively allocating the workload and utilizing the parallel processing powers of both CPUs and GPUs.

A CPU-and-GPU-based algorithm to run quicker the Boruta-Shap algorithm

Let's dissect the code. Depending on the number of cores available in your CPU, the code will group the number of trials in buckets and each bucket will be run in parallel. We use a modified version of the code provided by Moosa Ali (2022), who implements the CPU-based algorithm.

Let’s code!

The following function is responsible for computing the minimum number of trials needed as a threshold to accept an input feature as a selected feature based on the probability mass function (pmf) and a significance level. It iterates over the pmf and accumulates theprobabilitiesuntil the cumulative probability exceeds the significance level.

The next function selects features based on the number of hits they receive during the trials. It categorizes features into two zones:

green zone (features with hits higher than a threshold) and

blue zone (features with hits between upper and lower thresholds).

The following last function is the main function implementing the Boruta-Shap algorithm. It takes input data X and target variable y, along with optional parameters such as trials, workers, significance_level, and seed.

Find below what the function does:

Set the seed

It initializes a dictionary features_hits to track the number of hits for each feature.

Shuffled column names are generated for feature shuffling.

The data is split into training and testing sets.

Label encoding is applied to the target variable y.

A classification model (XGBRFClassifier, a tool from theXGBoostlibrary) is defined. To make the classifier work with a GPU, you just need to set the tree_method to 'gpu_hist'. Creating the model from scratch will be something quite complex. However, you can create the model using theRapids libraries.

The features_hits_func function is defined to perform feature shuffling, model fitting, and Shapley value computation for each trial. This function can be run within a loop for each trial or all the trials can be computed in parallel with the CPU.

A multi-threading and a loop technique are used to run multiple trials concurrently. In this case, we group all the range of trials in buckets as per the number of workers (threads used). For example, if we have 25 trials and we have 10 threads to use:

We define params_list_for_loop as the first 20 trials and last_params_list as the last 5 trials. We will run the features_hits_func function for the first 10 trials in parallel.

Once this is run, we iterate to the next 10 trials, which will be run in parallel, too.

Once we’re done with that, we finally run the last 5 trials in parallel.

After all trials, the probability mass function is calculated, and the minimum number of trials as a threshold is determined.

Features are classified into green, blue, or rejected based on the thresholds and hits received.

The function returns the selected features. In case no features were selected, we select all.

References

Ali, Moosa (2022).Boruta Feature Selection Explained in Python. Medium,https://medium.com/geekculture/boruta-feature-selection-explained-in-python-7ae8bf4aa1e7

Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances in Neural Information Processing Systems (pp. 4765-4774).

Piatetsky-Shapiro, G., & Mateosian, R. (2017). Boruta feature selection in r. KDnuggets, 17(19), 1-7.

Conclusion

You have learned how to create the Boruta-Shap algorithm using both the CPU and GPU. You’ll see a great difference, compared with using only the CPU, if you use a dataframe with many observations. Besides, the higher the number of threads and cores, the better the parallelism and the quicker the loop will run.

What’s next? You would ask.Well, you can use the above code to get the feature importance as a starting point, then move on to the actual process ofhow to backtest a trading strategywith those features. We suggest you use the Boruta-Shap algorithm before you optimize a strategy's parameters. You can find the source file below.

In case you want to learn more about machine learning, keep track of this learningtrack! You’ll learn the basics of machine learning in finance.

Now that you've grasped the power of Boruta Shap for identifying key features, you might be wondering how to put it into practice for real-world problems. Here's where things get exciting! ThisMachine Learning & Deep Learning for Tradingcourse by Quantra helps you learn these techniques for building advanced trading strategies. You'll not only learn the theory behind Boruta Shap but also gain hands-on experience implementing it to select the most impactful features for your own trading algorithms.

It's the perfect next step to turn your newfound knowledge into action!Happy Learning!

File in the download:Boruta-Shap Python Notebook

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
