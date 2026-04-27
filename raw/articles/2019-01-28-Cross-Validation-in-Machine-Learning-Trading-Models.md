---
title: "Cross Validation in Machine Learning Trading Models"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/cross-validation-machine-learning-trading-models/"
date: "2019-01-28"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Cross Validation in Machine Learning Trading Models

**来源**: [QuantInsti](https://blog.quantinsti.com/cross-validation-machine-learning-trading-models/)  
**日期**: 2019-01-28  
**作者**: QuantInsti

---

## 原文

Cross Validation In Machine Learning Trading Models

ByIshan Shah

What is cross validation in machine learning?

Cross validation in machine learning is a technique that provides an accurate measure of the performance of a machine learning model. This performance will be closer to what you can expect when the model is used on a future unseen dataset.

Determine if the machine learning model is good in predicting buy signal and/or sell signal

Demonstrate the performance of your machine learning trading model in different stress scenarios

Comprehensively do the cross validation in machine learning trading model

Importing the necessary libraries

Fetching the data

Defining the input and output dataset

Training the machine learning model

Importing the libraries

importquantrautilasqimportnumpyasnpfromsklearnimporttree

quantrautil- this will be used to fetch the price data of the AAPL stock from yahoo finance.

numpy- to perform the data manipulation on AAPL stock price to compute the input features and output. If you want to read more about numpy then it can be foundhere.

tree from sklearn - Sklearn has a lot of tools and implementation of machine learning models. 'tree' will be used to create Decision Tree classifier model.

Fetching the data

aapl=q.get_data('aapl','2000-1-1','2019-1-1')print(aapl.tail())

[*********************100%***********************]  1 of 1 downloaded
                  Open        High         Low       Close   Adj Close  \
Date                                                                     
2018-12-24  148.149994  151.550003  146.589996  146.830002  146.830002   
2018-12-26  148.300003  157.229996  146.720001  157.169998  157.169998   
2018-12-27  155.839996  156.770004  150.070007  156.149994  156.149994   
2018-12-28  157.500000  158.520004  154.550003  156.229996  156.229996   
2018-12-31  158.529999  159.360001  156.479996  157.740005  157.740005   


Date         Volume         
2018-12-24  37169200  
2018-12-26  58582500  
2018-12-27  53117100  
2018-12-28  42291400  
2018-12-31  35003500

Creating input and output dataset

Input variable: I have used '(Open-Close)/Open', '(High - Low)/Low', standard deviation of last 5 days returns (std_5), and average of last 5 days returns (ret_5)

Output variable: If tomorrow’s close price is greater than today's close price then the output variable is set to 1 and otherwise set to -1. 1 indicates to buy the stock and -1 indicates to sell the stock.

# Features constructionaapl['Open-Close']=(aapl.Open-aapl.Close)/aapl.Openaapl['High-Low']=(aapl.High-aapl.Low)/aapl.Lowaapl['percent_change']=aapl['Adj Close'].pct_change()aapl['std_5']=aapl['percent_change'].rolling(5).std()aapl['ret_5']=aapl['percent_change'].rolling(5).mean()aapl.dropna(inplace=True)# X is the input variableX=aapl[['Open-Close','High-Low','std_5','ret_5']]# Y is the target or output variabley=np.where(aapl['Adj Close'].shift(-1)>aapl['Adj Close'],1,-1)

Training the machine learning model

clf=tree.DecisionTreeClassifier(random_state=5)model=clf.fit(X,y)

Cross validation of the machine learning model

fromsklearn.metricsimportaccuracy_scoreprint('Correct Prediction: ',accuracy_score(y,model.predict(X),normalize=False))print('Total Prediction: ',X.shape[0])

Correct Prediction:  4775
Total Prediction:  4775

print(accuracy_score(y,model.predict(X),normalize=True)*100)

How do you overcome this problem of using the same data for training and testing?

# Total dataset lengthdataset_length=aapl.shape[0]# Training dataset lengthsplit=int(dataset_length*0.75)split

# Splittiing the X and y into train and test datasetsX_train,X_test=X[:split],X[split:]y_train,y_test=y[:split],y[split:]# Print the size of the train and test datasetprint(X_train.shape,X_test.shape)print(y_train.shape,y_test.shape)

(3581, 4) (1194, 4)
(3581,) (1194,)

# Create the model on train datasetmodel=clf.fit(X_train,y_train)

# Calculate the accuracyaccuracy_score(y_test,model.predict(X_test),normalize=True)*100

49.413735343383586

K-Fold Cross Validation Technique

How do you select the number of folds?

Why is this better than the original method of a single train and test split?

How can you perform cross validation of the model on a dataset which is prior to the dataset used to train the model? Is it not historically accurate?

Code K-fold in Python

fromsklearn.model_selectionimportKFoldkf=KFold(n_splits=4,shuffle=False)

kf.split(X)

<generator object _BaseKFold.split at 0x0000000009936F68>

print("Train: ","TEST:")fortrain_index,test_indexinkf.split(X):print(train_index,test_index)

Train:  TEST:
[1194 1195 1196 ... 4772 4773 4774] [   0    1    2 ... 1191 1192 1193]
[   0    1    2 ... 4772 4773 4774] [1194 1195 1196 ... 2385 2386 2387]
[   0    1    2 ... 4772 4773 4774] [2388 2389 2390 ... 3579 3580 3581]
[   0    1    2 ... 3579 3580 3581] [3582 3583 3584 ... 4772 4773 4774]

# Initialize the accuracy of the models to blank list. The accuracy of each model will be appended to this listaccuracy_model=[]# Iterate over each train-test splitfortrain_index,test_indexinkf.split(X):# Split train-testX_train,X_test=X.iloc[train_index],X.iloc[test_index]y_train,y_test=y[train_index],y[test_index]# Train the model
    model = clf.fit(X_train, y_train)
    # Append to accuracy_model the accuracy of the model
    accuracy_model.append(accuracy_score(y_test, model.predict(X_test), normalize=True)*100)# Print the accuracyprint(accuracy_model)

[50.502512562814076, 49.413735343383586, 51.75879396984925, 49.79044425817267]

Stability of the model

np.std(accuracy_model)

0.8939494614206329

np.mean(accuracy_model)

50.3663715335549

Confusion Matrix

# Import the pandas for creating a dataframeimportpandasaspd# To calculate the confusion matrixfromsklearn.metricsimportconfusion_matrix# To plot%matplotlibinlineimportmatplotlib.pyplotaspltimportseabornassn# Initialize the array to zero which will store the confusion matrixarray=[[0,0],[0,0]]# For each train-test split: train, predict and compute the confusion matrixfortrain_index,test_indexinkf.split(X):# Train test splitX_train,X_test=X.iloc[train_index],X.iloc[test_index]y_train,y_test=y[train_index],y[test_index]# Train the modelmodel=clf.fit(X_train,y_train)# Calculate the confusion matrixc=confusion_matrix(y_test,model.predict(X_test))# Add the score to the previous confusion matrix of previous model
    array = array + c# Create a pandas dataframe that stores the output of confusion matrixdf=pd.DataFrame(array,index=['Buy','Sell'],columns=['Buy','Sell'])# Plot the heatmapsn.heatmap(df,annot=True,cmap='Greens',fmt='g')plt.xlabel('Predicted')plt.ylabel('Actual')plt.show()

---

*Imported from QuantInsti Blog on 2026-04-27*
