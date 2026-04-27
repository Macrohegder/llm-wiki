---
title: "Polynomial Regression: Adding Non-Linearity To A Linear Model"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/polynomial-regression-adding-non-linearity-to-a-linear-model/"
date: "2018-05-30"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Polynomial Regression: Adding Non-Linearity To A Linear Model

**来源**: [QuantInsti](https://blog.quantinsti.com/polynomial-regression-adding-non-linearity-to-a-linear-model/)  
**日期**: 2018-05-30  
**作者**: QuantInsti

---

## 原文

Polynomial Regression: Adding Non-Linearity To A Linear Model

ByLamarcus Coleman

Introduction

In this post we're going to learn how we can address a key concern of linear models, the assumption of linearity. We'll take a look at Linear Regression, a foundational statistical learning technique, learn what's happening under the hood of the model,some things that we want to be aware of, and then learn more about some of the weaknesses of the model. We'll then introduce the idea of polynomial regression as being a solution to a key weakness of linear models, namely Linear Regression in this post.

Let's Review Linear Regression

Let's Build a Model

#data analysis and manipulationimportnumpyasnpimportpandasaspd#data collectionimportpandas_datareaderaspdr#data visualizationimportmatplotlib.pyplotaspltimportseabornassns

#setting our testing periodstart='2016-01-01'end='2018-01-01'pnb=pdr.get_data_yahoo('PNB.NS',start,end)

pnb.head()

plt.figure(figsize=(10,6))plt.plot(pnb['Close'])plt.title('PNB 2016-2018 Performance')plt.show()

#making a copy of our data framePNB=pnb.copy()

#creating our predictor variables#Lag 1 PredictorPNB['Lag 1']=PNB['Close'].shift(1)#Lag 2 PredictorPNB['Lag 2']=PNB['Close'].shift(2)#Higher High PredictorPNB['Higher High']=np.where(PNB['High']>PNB['High'].shift(1),1,-1)#Lower Low PredictorPNB['Lower Low']=np.where(PNB['Low']<PNB['Low'].shift(1),1,-1)

Now let's review our PNB dataframe.

PNB.head()

Now let's import our Linear Regression Model from sci-kit learn.

fromsklearn.linear_modelimportLinearRegression

Now that we have our model, let's import our traintestsplit object from sklearn.

fromsklearn.model_selectionimporttrain_test_split

Now we're ready to create training and testing sets for our data. But first, let's initialise our X and y variables. Remember X denotes our predictor variables, and y denotes our response or what we're actually trying to predict.

#creating our predictor variablesX=PNB.drop(['Open','High','Low','Close','Volume','Adj Close'],axis=1)#initializing our response variabley=PNB['Close']

Now we're ready to split our data into training and testing sets.

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.20,random_state=101)

lm=LinearRegression()

Now we can pass in our training sets into our model. We must fill the NaN values in our X_train set first.

#fitting our model to our training datalm.fit(X_train.fillna(0),y_train)

#making predictionspredictions=lm.predict(X_test.fillna(0))

Now that we have our predictions, we can check to see how well our model performed. There a variety of different things that we would like to view to assess our model's performance. Our model'sR2, R-Squared tells us the percentage variance in our response that can be explained by our predictors. We would also like to look at our model's errors. Our errors tell us how much our model deviated from the actual response value. Our objective is to create a model that achieves the lowest possible error.

#checking our model's coefficientslm.coef_

fromsklearnimportmetrics

#getting our R-Squared valueprint('R-Squared:',metrics.explained_variance_score(y_test,predictions))

#printing our errorsprint('MSE:',metrics.mean_squared_error(y_test,predictions))print('MAE:',metrics.mean_absolute_error(y_test,predictions))print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,predictions)))

MSE: 11.1707624541 MAE: 2.48608751953 RMSE: 3.3422690577

Let's now plot our actual response and our predicted responses. We can also calculate our residuals or errors.

sns.jointplot(predictions,y_test,kind='regplot')plt.xlabel('Predictions')plt.ylabel('Actual')

<matplotlib.text.Text at 0x1f40c5ef9e8>

The above plot shows that our predictions and actual responses are highly correlated. It also shows a really small p-value as well. Let's now plot our residuals.

residuals=y_test-predictions

#plotting residualssns.distplot(residuals,bins=100)

<matplotlib.axes._subplots.AxesSubplot at 0x1f40b94d5c0>

sns.jointplot(residuals,predictions)

<seaborn.axisgrid.JointGrid at 0x1f409fcfa20>

Polynomial Regression

lm.intercept_

array([ 0.93707237, 0.01904699, 0.27980978, -1.93943157])

Checking ourB0

lm.intercept_

6.0817053905353902

We'll create a dataframe to better visualize our coefficients.

coefficients=pd.DataFrame(lm.coef_,index=X_train.columns,columns=['Coefficients'])

coefficients

Now we can clearly see ourB1s for each feature. Let's visualise our features so that we have an idea of which ones we would like to transform.

sns.jointplot(PNB['Lag 1'],PNB['Close'],kind='regplot')

<seaborn.axisgrid.JointGrid at 0x1f40a83f5c0>

Our lower low feature has the lowestB1coefficient. Let's visualise it.

plt.figure(figsize=(10,6))sns.boxplot(x='Lower Low',y='Close',hue='Lower Low',data=PNB)

C:\Anaconda3\lib\site-packages\seaborn\categorical.py:482: FutureWarning: removena is deprecated and is a private function. Do not use. boxdata = removena(groupdata[hue_mask])

<matplotlib.axes._subplots.AxesSubplot at 0x1f40bded5c0>

We can see a significant drop between the coefficient of our Lag 1 feature and our Lag 2 feature. Let's visualise our Lag 2 feature.

plt.figure(figsize=(10,6))sns.lmplot('Lag 2','Close',data=PNB)

plt.figure(figsize=(10,6))sns.boxplot(x='Higher High',y='Close',data=PNB)

C:\Anaconda3\lib\site-packages\seaborn\categorical.py:454: FutureWarning: removena is deprecated and is a private function. Do not use. boxdata = removena(groupdata)

<matplotlib.axes._subplots.AxesSubplot at 0x1f40c719ac8>

PNB.head()

Now let's add ourLag22variable.

PNB['Lag 2 Squared']=PNB['Lag 2']**2

Let's recheck our dataframe.

PNB.head()

Okay now let's rebuild our model and see if we were able to reduce our MSE.

polynomial_model=LinearRegression()

We can now set our X and y variables.

#dropping all columns except our features and storing in XX_2=PNB.drop(['Open','High','Low','Close','Adj Close','Volume','Lag 2'],axis=1)#Initializing our Responsey_2=PNB['Close']

X_train_2,X_test_2,y_train_2,y_test_2=train_test_split(X_2,y_2,test_size=0.2,random_state=101)

Now that we have our training and testing data, we can use it to fit our model and generate predictions.

#fitting our modelpolynomial_model.fit(X_train_2.fillna(0),y_train_2)

LinearRegression(copyX=True, fitintercept=True, n_jobs=1, normalize=False)

We've just fitted our polynomial_model to our training data. Now let's use it to make predictions using our testing data.

predictions_2=polynomial_model.predict(X_test_2)

We've just made our predictions. We can now calculate our coefficients, residuals, and our errors. Let's start by creating a dataframe to hold the coefficients from our polynomial model.

polynomial_df=pd.DataFrame(polynomial_model.coef_,index=X_train_2.columns,columns=['Polynomial Coefficients'])

Now let's view our polynomial df.

polynomial_df.head()

Now let's create our residuals and plot them. Then we will recalculate our models' metrics.

sns.distplot(residuals_2,bins=100)

<matplotlib.axes._subplots.AxesSubplot at 0x1f40a75f978>

R_Squared_2=metrics.explained_variance_score(y_test_2,predictions_2)

#printing the R-Squared of our polynomial modelprint('Polynomial Model R-Squared:',R_Squared_2)

Polynomial Model R-Squared: 0.988328254058

Now let's calculate our errors.

#Calculating MSEMSE_2=metrics.mean_squared_error(y_test_2,predictions_2)#Calculating MAEMAE_2=metrics.mean_absolute_error(y_test_2,predictions_2)#Calculating RMSERMSE_2=np.sqrt(MSE_2)#Printing out Errorsprint('Polynomial MSE:',MSE_2)print('Polynomial MAE:',MAE_2)print('Polynomial RMSE:',RMSE_2)

Okay. Let's Review!

Learn More

---

*Imported from QuantInsti Blog on 2026-04-27*
