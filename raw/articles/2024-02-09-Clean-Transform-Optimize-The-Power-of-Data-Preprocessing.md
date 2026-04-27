---
title: "Clean, Transform, Optimize: The Power of Data Preprocessing"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/data-preprocessing/"
date: "2024-02-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Clean, Transform, Optimize: The Power of Data Preprocessing

**来源**: [QuantInsti](https://blog.quantinsti.com/data-preprocessing/)  
**日期**: 2024-02-09  
**作者**: QuantInsti

---

## 原文

Clean, Transform, Optimize: The Power of Data Preprocessing

Data preprocessing is a basic requirement of any good machine learning model. Preprocessing the data implies using the data which is easily readable by the machine learning model.

This essential phase involves identifying and rectifying errors, handling missing values, and transforming data to enhance its suitability for analysis. As the first crucial step in the data preparation journey, preprocessing ensures data accuracy and sets the stage for effective modelling. From scaling and encoding to feature engineering, this process unleashes the true potential of datasets, empowering analysts and data scientists to uncover patterns and optimise predictive models.

Dive into the world of data preprocessing to unlock the full potential of your data. In this article, we will discuss the basics of data preprocessing and how to make the data suitable for machine learning models.

This article covers:

What is data preprocessing?

Why is data preprocessing required?

Data that needs-data-preprocessing

Data preprocessing with Python for different dataset types

Data cleaning vs data preprocessing

Data preparation vs data preprocessing

Data preprocessing vs feature engineering

Where can you learn more about data preprocessing?

What is data preprocessing?

Our comprehensive blog ondata cleaninghelps you learn all about data cleaning as a part of preprocessing the data, covering everything from the basics to performance, and more.

After data cleaning, data preprocessing requires the data to be transformed into a format that is understandable to the machine learning model.

Data preprocessing involves readying raw data to make it suitable for machine learning models. This process includes data cleaning, ensuring the data is prepared for input into machine learning models.

Automated data preprocessing is particularly advantageous when dealing with large datasets, enhancing efficiency, and ensuring consistency in the preparation of data for further analysis or model training.⁽¹⁾

To find out more about the introduction of data preprocessing, you can check this video:

Why is data preprocessing required?

Here, we will discuss the importance of data preprocessing in machine learning. Data preprocessing is essential for the following reasons:

Ensuring Accuracy:To render data readable for machine learning models, it must be devoid of missing, redundant, or duplicate values, ensuring accuracy.

Building Trust:The updated data should strive to be as accurate and trustworthy as possible, instilling confidence in its reliability.

Enhancing Interpretability:Preprocessed data needs to be correctly interpreted, promoting a better understanding of the information it conveys.

In summary, data preprocessing is vital to enable machine learning models to learn from accurate and reliable data, ensuring their ability to make correct predictions or outcomes.

Find out about what makes data preprocessing so important in this video by Dr. Ernest Chan.

Data that needs data preprocessing

Since data comes in various formats, there can be certain errors that need to be corrected. Let us discuss how different datasets can be converted into the correct format that the ML model can read accurately.

Here, we will see how to feed correct features from datasets with:

Missing values -Incomplete or absent data points within a dataset that require handling through methods like imputation or deletion.

Outliers -Anomalies or extreme values in a dataset that can skew analysis or modelling results, often addressed through identification and removal techniques.

Overfitting -A modelling phenomenon where a machine learning algorithm learns the training data too well, capturing noise and hindering generalisation to new, unseen data.

Data with no numerical values -Non-numeric data, typically categorical or textual, necessitating encoding techniques like one-hot encoding for use in numerical-based models.

Different date format -Diverse representations of dates in a dataset, requiring standardisation or conversion to a uniform format for consistency in time-based analyses.

This way, feeding the ML model with different data types helps with ensuring data quality in the preprocessing stage.

Data preprocessing with Python for different dataset types

Now that you know the different dataset errors, we can go ahead with learning how to use Python for preprocessing such a dataset.⁽²⁾

Let us learn about these dataset errors:

Missing values in a dataset

Outliers in a dataset

Overfitting in a dataset

Data with no numerical values in a dataset

Different date formats in a dataset

Missing values in a dataset

Missing values are a common problem while dealing with data! The values can be missed because of various reasons such as human errors, mechanical errors, etc.

Data cleansing is an important step before you even begin the algorithmic trading process, which begins with historical data analysis to make the prediction model as accurate as possible.

Based on this prediction model you create the trading strategy. Hence, leaving missed values in the dataset can wreak havoc by giving faulty predictive results that can lead to erroneous strategy creation and further the results can not be great to state the obvious.

There are three techniques to solve the missing values’ problem to find out the most accurate features, and they are:

Dropping

Numerical imputation

Categorical imputation

Dropping

Dropping is the most common method to take care of the missed values. Those rows in the dataset or the entire columns with missed values are dropped to avoid errors from occurring in data analysis.

Some machines are programmed to automatically drop the rows or columns that include missed values resulting in a reduced training size. Hence, the dropping can lead to a decrease in the model performance.

A simple solution for the problem of a decreased training size due to the dropping of values is to use imputation. We will discuss the interesting imputation methods further. In case of dropping, you can define a threshold to the machine.

For instance, the threshold can be anything. It can be 50%, 60% or 70% of the data. Let us take 60% in our example, which means that 60% of data with missing values will be accepted by the model/algorithm as the training dataset, but the features with more than 60% missing values will be dropped.

For dropping the values, the following Python codes are used:

By using the above Python codes, the missed values will be dropped and the machine learning model will learn on the rest of the data.

Numerical imputation

The word imputation implies replacing the missing values with such a value that makes sense. And, numerical imputation is done in the data with numbers.

For instance, if there is a tabular dataset with the number of stocks, commodities and derivatives traded in a month as the columns, it is better to replace the missed value with a “0” than leave them as it is.

With numerical imputation, the data size is preserved and hence, predictive models like linear regression can work better to predict most accurately.

A linear regression model can not work with missing values in the dataset since it is biased toward the missed values and considers them “good estimates”. Also, the missed values can be replaced with the median of the columns since median values are not sensitive to outliers, unlike averages of columns.

Let us see the Python codes for numerical imputation, which are as follows:

Categorical imputation

This technique of imputation is nothing but replacing the missed values in the data with the one which occurs the maximum number of times in the column. But, in case there is no such value that occurs frequently or dominates the other values, then it is best to fill the same as “NAN”.

The following Python code can be used here:

Outliers  in a dataset

An outlier differs significantly from other values and is too distanced from the mean of the values. Such values that are considered outliers are usually due to some systematic errors or flaws.

Let us see the following Python codes for identifying and removing outliers withstandard deviation:

In the codes above, “lower” and “upper” signify the upper and lower limit in the dataset.

Overfitting  in a dataset

In both machine learning and statistics,overfittingoccurs when the model fits the data too well or simply put when the model is too complex.

The overfitting model learns the detail and noise in the training data to such an extent that it negatively impacts the performance of the model on new data/test data.

The overfitting problem can be solved by decreasing the number of features/inputs or by increasing the number of training examples to make the machine learning algorithms more generalised.

The most common solution is regularisation in an overfitting case. Binning is the technique that helps with the regularisation of the data which also makes you lose some data every time you regularise it.

For instance, in the case of numerical binning, the data can be as follows:

Stock value

100-250

Lowest

251-400

401-500

Here is the Python code for binning:

Your output should look something like this:

Value    Bin
0     102     Low
1     300     Mid
2     107     Low
3     470     High

Data with no numerical values  in a dataset

In the case of the dataset with no numerical values, it becomes impossible for the machine learning model to learn the information.

The machine learning model can only handle numerical values and thus, it is best to spread the values in the columns with assigned binary numbers “0” or “1”. This technique is known as one-hot encoding.

In this type of technique, the grouped columns already exist. For instance, below I have mentioned a grouped column:

Infected

Covid variants

Lambda

Omicron

Lambda

Omicron

Omicron

Lambda

Now, the above-grouped data can be encoded with the binary numbers ”0” and “1” with one hot encoding technique. This technique subtly converts the categorical data into a numerical format in the following manner:

Infected

Lambda

Omicron

Hence, it results in better handling of grouped data by converting the same into encoded data for the machine learning model to grasp the encoded (which is numerical) information quickly.

Problem with the approach

Going further, in case there are more than three categories in a dataset that is to be used for feeding the machine learning model, the one-hot encoding technique will create as many columns. Let us say, there are 2000 categories, then this technique will create 2000 columns and it will be a lot of information to feed to the model.

Solution

To solve this problem, while using this technique, we can apply the target encoding technique which implies calculating the “mean” of each predictor category and using the same mean for all other rows with the same category under the predictor column. This will convert the categorical column into the numeric column and that is our main aim.

Let us understand this with the same example as above but this time we will use the “mean” of the values under the same category in all the rows. Let us see how.

In Python, we can use the following code:

Output:

Infected

Predictor

Predictor_encoded

Lambda

Omicron

Lambda

Omicron

In the output above, the Predictor column depicts the Covid variants and the Predictor_encoded column depicts the “mean” of the same category of Covid variants which makes 2+4/2 = 3 as the mean value for Delta, 4+6/2 = 5 as the mean value for Lambda and so on.

Hence, the machine learning model will be able to feed the main feature (converted to a number) for each predictor category for the future.

Different date formats  in a dataset

With the different date formats such as “25-12-2021”, “25th December 2021” etc. the machine learning model needs to be equipped with each of them. Or else, it is difficult for the machine learning model to understand all the formats.

With such a dataset, you can preprocess or decompose the data by mentioning three different columns for the parts of the date, such as Year, Month and Day.

In Python, the preprocessing of the data with different columns for the date will look like this:

Output:

In the output above, the dataset is in date format which is numerical. And because of decomposing the date into different parts such as Year, Month and Day, the machine learning model will be able to learn the date format.

The entire process mentioned above where data cleaning takes place can also be termed as data wrangling.

In the field of machine learning, effective data preprocessing in Python is crucial for enhancing the quality and reliability of the input data, ultimately improving the performance of the model during training and inference.

Data cleaning vs data preprocessing

In the context of trading, data cleaning may involve handling errors in historical stock prices or addressing inconsistencies in trading volumes.

However, data preprocessing is then applied to prepare the data for technical analysis or machine learning models, including tasks such as scaling prices or encoding categorical variables like stock symbols.

Aspect

Data Cleaning

Data Preprocessing

Objective

Identify and rectify errors or inaccuracies in stock prices.

Transform and enhance raw stock market data for analysis.

Eliminating inconsistencies and errors in historical price data.

Addressing missing values in daily trading volumes and handling outliers.

Removing duplicate entries.

Scaling stock prices for analysis.

Importance

Essential for ensuring accurate historical price data.

Necessary for preparing data for technical analysis and modelling.

Example Tasks

Removing days with missing closing prices. Correcting anomalies in historical data.

Scaling stock prices for comparability. Encoding stock symbols.

Dependencies

Often performed before technical analysis.

Typically follows data cleaning in the trading data workflow.

Outcome

A cleaned dataset with accurate historical stock prices.

A preprocessed dataset ready for technical analysis or algorithmic trading.

Data preparation vs data preprocessing

Now, let us see how preparing the data is different from data preprocessing with the table below.

Aspect

Data Preparation

Data Preprocessing

Objective

Prepare raw data for analysis or modelling.

Transform and enhance data for improved analysis or modelling.

Example Tasks

Collecting data from various sources, combining data from multiple datasets, aggregating data at different levels, and splitting data into training and testing sets.

Imputing missing values in a specific column, scaling numerical features for machine learning models, and encoding categorical variables for analysis.

Broader term encompassing various activities.

A subset of data preparation, focusing on specific transformations.

Data collection, data cleaning, data integration, data transformation, data reduction and data splitting.

Handling missing data, scaling features, encoding categorical variables, handling outliers, and feature engineering.

Importance

Essential for ensuring data availability and organisation.

Necessary for preparing data to improve analysis or model performance.

Dependencies

Often precedes data preprocessing in the overall data workflow.

Follows data collection and is closely related to data cleaning.

Outcome

Well-organised dataset ready for analysis or modelling.

Preprocessed dataset optimised for specific analytical or modelling tasks.

This version provides a cleaner presentation of the information without redundancies and unnecessary symbols.

Data preprocessing vs feature engineering

Data preprocessing involves tasks such as handling missing data and scaling, while feature engineering focuses on creating new features or modifying existing ones to improve the predictive power of machine learning models.

Both are crucial steps in the data preparation process. Let us see a table with a clear distinction between the two.

Aspect

Data Preprocessing

Feature Engineering

Objective

Transform and enhance raw data for analysis or modelling.

Create new features or modify existing ones for improved model performance.

Example Tasks

Imputing missing values and scaling numerical features.

Creating a feature for the ratio of two existing features and adding polynomial features.

Subset of data preparation, focusing on data transformations.

Specialised tasks within data preparation, focusing on feature creation or modification.

Handling missing data, scaling and normalisation, encoding categorical variables, handling outliers, and data imputation. Data preprocessing is a broader term which includes the tasks of data cleaning and data preparation as well.

Creating new features based on existing ones, Polynomial features, Interaction terms, and Dimensionality reduction.

Importance

Necessary for preparing data for analysis or modelling.

Enhances predictive power by introducing relevant features.

Dependencies

Typically follows data cleaning and precedes model training.

Often follows data preprocessing and precedes model training.

Outcome

A preprocessed dataset ready for analysis or modelling.

A dataset with engineered features optimised for model performance.

Where can you learn more about data preprocessing?

Learn more about data preprocessing with our courses mentioned below.

FREE Course |Introduction to Machine Learning in Trading

This course can help you learn the machine learning models and algorithms that are used for trading with thefinancial market data. Learning about machine learning in detail will help you understand how data preprocessing is essential.

Course |Data & Feature Engineering for Trading

With this course, you will equip yourself with the essential knowledge required for the two most important steps for any machine learning model, which are:

Data cleaning -This implies making the raw data error free by taking care of issues such as missed values, redundant values, duplicate values etc.

Feature engineering -To extract the important features for the machine learning model to learn the patterns of the dataset with solutions to similar inputs in future.

Conclusion

Data preprocessing is the prerequisite for making the machine learning model able to read the dataset and learn from the same. Any machine learning model can learn only when the data consists of no redundancy, no noise (outliers), and only such numerical values.

Hence, we discussed how to make the machine learning model learn with data it understands the best, learns from and performs with every time.

Moreover, since understanding the concept of data preprocessing is foundational to both trading and machine learning, we recognize the need for mentioning data preprocessing as a vital step in trading. We delved into the reasons behind its importance and its direct impact on enhancing model performance.

Moving beyond theory, our focus  in the blog extended to the practical realm. By exploring real-world examples and hands-on exercises in Python, we covered how to gain proficiency in applying data preprocessing techniques.

These skills are essential for handling various types of datasets effectively which is a key aspect in the intersection of trading and machine learning. Following a systematic set of steps, we went through the steps for preprocessing the data efficiently, that ensure its readiness for machine learning applications.

If you wish to explore more about data preprocessing in detail, explore this comprehensiveFeature Engineering courseby Quantra where you will find out the importance of data preprocessing in feature engineering while working with machine learning models.

You can master the concepts such as Exploratory Data Analysis, Data Cleaning, Feature Engineering, Technical Indicators, and more. You will get to elevate your skills in creating predictive models and learn the art of backtesting and paper trading. Don't miss this opportunity to transform your understanding and application of feature engineering. Happy learning!

Author:Chainika Thakar

Note: The original post has been revamped on 9th February 2024 for accuracy, and recentness.

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
