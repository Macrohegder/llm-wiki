---
title: "Long-only, Low frequency, Asset-allocation Algorithms"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/long-only-low-frequency-asset-allocation-algorithms-project-vivin-thomas/"
date: "2021-05-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Long-only, Low frequency, Asset-allocation Algorithms

**来源**: [QuantInsti](https://blog.quantinsti.com/long-only-low-frequency-asset-allocation-algorithms-project-vivin-thomas/)  
**日期**: 2021-05-20  
**作者**: QuantInsti

---

## 原文

Long-only, Low frequency, Asset-allocation Algorithms

Understand and learn, how you can focus on algorithms that leverage machine learning at its core to make the capital allocation choice. You can come up with a low-frequency strategy that can optimally allocate its prevailing capital amongst a pre-selected set of underliers (basket assets) at regular intervals.

With this process, you can create Long-only, low frequency, asset-allocation algorithms. Besides this, you will also learn to benchmark these against a vanilla allocation strategy which only depends on empiricalmomentum indicatorsfor its decision making.

The link for the complete code used in this project is available at the end of the article.

This article is the final project submitted by the author as a part of his coursework in the Executive Programme in Algorithmic Trading (EPAT®) at QuantInsti®. Do check ourProjects pageand have a look at what our students are building.

About the Author

Vivin Thomasis a Quant in the financial services industry and is based out of Mumbai, India. He has a cumulative professional experience of 9 years in quantitative finance, covering derivatives pricing and risk.

He has grown across multiple roles and organizations, notably holding the position of Vice President with two globally reputable investment banks in recent years. Vivin possesses a Bachelor’s and Masters in Engineering from one of the premier institutions in India, IIT Madras. Vivin is also a proud recipient of the EPAT Certificate of Excellence.

Project Abstract

The aim of this project is to come up with a low frequency strategy which can optimally allocate its prevailing capital amongst a pre-selected set of underliers (basket assets) at regular intervals.

There are many choices available for the kind algorithm/strategy. In this project we mostly focus on those algorithms which leverage machine learning at its core to make the capital allocation choice for us. A suite of machine learning algorithms are used in this regard and each is compared against the other.

To ensure we have an appropriate baseline, we also try coming up with an allocation scheme which is ‘rule-based’ (i.e., non-ML), primarily for comparison purposes. This would help understand whether ML algos do indeed provide a visible edge vs rule-based algos developed for the same purpose.

How we go about choosing our underlier set is also an important consideration, especially the number of assets in the basket. This is discussed in more detail in the next section.

Project motivation

The idea here is to come up with a long-only asset allocation strategy that optimally re-distributes its current capital amongst a pre-determined set of basket underliers.

This re-distribution is also referred to as rebalancing and occurs with a fixed frequency, chosen to be 7 days in our case. The idea is sensible diversification – i.e., when one of the assets in my basket performs bad, I would hopefully expect the other assets in the basket to ‘cushion’ it via a significant outperformance.

The allocation can be fractional or whole i.e., within a rebalancing period. We can choose to either allocate our entire capital to a single asset in the basket or allocate fractional wealth to each asset within the basket based on what our algorithm predicts is going to be the best performing asset(s) for the incoming rebalancing period.

The reason why we go long only is to replicate the simplicity of a conventional fund/portfolio. Shorting as a concept may not be easily understandable by a large majority of (not-so-sophisticated) retail investors who may be looking to invest in your fund which may make them less comfortable to invest.

Simplicity is also the reason why we try to set the rebalance frequency to a reasonable value. An extremely low frequency would make it difficult for us to make accurate predictions (its relatively easier to predict outperformance over 1 day rather than 1 year).

On the other hand, an extremely high frequency would introduce significant transaction costs and slippage thus diminishing our overall returns. Naturally, we could have introduced transaction costs in our backtesting and ‘optimized’ over the rebalance frequency as well.

However, we’ve kept that discussion out-of-scope as it would have added an additional dimension to our already high dimensional optimization problem (as we will see later)

Choice of basket underliers

As stated earlier, the number and exact names of the underliers chosen for the purpose of this exercise was also an important consideration.

The aim was to first come-up with a definition for what we would consider ‘categories’ followed-up by choosing reasonable representative assets for each category.

A category could be sector based (pharma, IT, infra, Finance etc) or capitalization based (large, mid, small cap) or based on asset type (stocks, bonds). I ended up going with the first definition. The choice was arbitrary, and the same algorithm could be executed for any of the other category definitions (albeit with different optimal parameters).

The choice to fix this definition was made to ensure simplicity in our setup. For the same reason, I decided to go with the choice of ETFs to represent each sector rather than running another complicated exercise to choose the ‘right set of representative stocks’ for each category.

This would additionally ensure that idiosyncratic behaviours resulting from stock selection do not play a part in our overall algo performance.

Just to get the ball rolling, I chose 4 ETFs in addition to pure ‘cash’ as the initial candidates. These ETFs were

a PSU Bank ETF (KOTAKPSUBK.NS),

an infra ETF (INFRABEES.NS),

a gold ETF (HDFCMFGETF.NS) and

the Nifty-50 ETF (I chose the index ticker ^NSEI for this purpose due to some data issues. Generally speaking, this should be OK).

The realized returns for each ETF over the entire period in consideration for our analysis can be found below.

There are obvious drawbacks of having a relatively large basket such as this one (5 in total including cash). These drawbacks become even more severe when we try to solve for a multiclass classification problem.

The classifier makes a prediction based on which label is assigned the highest ‘prediction probability’ amongst the overall set. The probability thresholds would naturally get smaller as we increase the number of labels for prediction thus increasing the noise in our prediction making it susceptible to more incorrect predictions.

Moreover, if ‘N’ technical indicators are used as features in the prediction (which is the case here – we will see in later sections) then each asset addition would lead to an addition of N new features in your classification model which could potentially lead to model overfitting.

This hypothesis was also informally confirmed when I ran the entire workflow (described in subsequent sections) on this basket of size 5.

The results obtained were indeed quite poor which was the main driver behind me going back and running some more analysis on the choice of assets.

Some intuition behind the analysis can be found below:

The main item to consider was anti-correlation. Recollect the idea of ‘cushioning’ described in the earlier part of the section.

The reason for having multiple underliers to choose from is driven by the assumption that when your base underlier (let’s take Nifty 50 as an example) is doing bad you have another underlier which can ‘anchor’ your strategy.

A reasonable degree of anticorrelation is necessary for such a behaviour. If 2 underliers in your set are positively correlated, then it makes little sense to expect one to ‘anchor’ the other.

A quick correlation computation between the 5-day returns (arbitrarily chosen to reduce noise) of each of our underliers yields the following:-

KOTAKPSUBK.NS

INFRABEES.NS

HDFCMFGETF.NS

(I’ve truncated the matrix but it’s clearly observable that the only asset which shares a negative correlation with the base underlier isGold.)

Another way we can visualize this relationship is by plotting how often has one of the other underliers given us positive vs negative returns (frequency) for a given return value (over 5-days, arbitrarily chosen) of the market/base underlier (Nifty 50).

Crude histogram visualizations can be found below.

As you can see, the Gold ETF has a significant advantage over the other 2 underliers – on days when the market generates negative returns, Gold has a >50% likelihood of generating positive returns. The profile is infact literally inverted compared to the other 2

This is when I decided to truncate my initial underlies list to include just 3, including cash. Gold ETF must be in the list either way as it’s the only asset which is negatively correlated with the rest.

The choice for the other could be either of the remaining 3. I choose to discuss results obtained using both Nifty-50 and the Infra ETF so that the algo appropriateness can be assessed under more than 1 scenario.

Description of the algorithms- Both the rule-based and classifier-based asset allocation models are described in more detail in the following subsections

Momentum-based asset allocation (rule based)

The idea is to compute a per-asset metric at each rebalance date and allocate a fraction of your available capital proportional to this metric for each asset.

For this case, I try to come up with a metric which is reflective of the underlying momentum in the asset. The idea is that if an asset starts to build momentum, it will trend in that direction on an average, within a reasonable timeframe (time horizon).

The timeframe we are interested in for our case is 7 days (discussed previously). The higher the momentum metric, potentially stronger is the trend and higher the fraction we should consider allocating (if trend is positive).

If an asset has a negative momentum/trend metric, then our algorithm should ensure that it receives no allocation. If all assets have negative momentum, then we should simply allocate nothing to our basket and instead reserve all our capital as cash.

The momentum metric I decided to go with is a simple average of close-to-close returns taken over MAwindow days. This metric was arrived at heuristically (i.e., there is no literature which necessarily supports the advantage this specific calculation would hold over other momentum metrics).

Where,

Momi,jis the momentum metric corresponding to the ithasset in the basket observed as of the jthtrading day,

rkis the close-to-close %price return from the (k-1)thto the kthday.

MAwindowis the number of historical dates over which we want to take the returns average.

This is taken as one of the hyperparameters of the model.

On each rebalance day, the weights assigned to each asset are computed as the following.

Where,

wi,jis the weight corresponding to the ithasset as of the jth trading day

Momi,jhas been defined above and

Mcis the default momentum value we assign to cash.

Mcis the second hyperparameter in our model.

Note that for cases where all basket assets have 0 or negative momentum and Mcis set to 0, all weights are automatically assigned to 0 as we can see in the equation above.

wiare computed at every rebalance day from which we get the approximate capital that needs to be assigned to asset i.We then compute the number of shares by dividing this approximate capital with the prevailing close price of that asset. This number is floored to the nearest integer to get the actual number of shares from which we can obtain the actual assigned capital.The actual assigned capital is summed up across all assets and the difference of this total amount with the total prevailing capital at that rebalance day is how much is left in cash.The difference in number of shares assigned per asset on a given rebalance day vs the rebalance day preceding it is the number of shares that needs to be bought/sold on that rebalance day.It is quite apparent that this is afractionalallocation strategy. We could also switch it to awholeallocation strategy by simply assigning all our capital to the asset with the highest momentum.But for the purpose of this analysis, we keep the assignment fractional.Multiclass ML asset allocationHere we don’t make any decisions based on rules. Rather, we train a multiclass classification model to do the decisioning on our behalf.Note that in order to maintain simplicity, this ML allocation strategy runs under thewholemode i.e., at the beginning of every rebalance period, our entire capital is to be assigned to the asset attributed as the predictedwinning tickerfor that period.The predicted (dependent) variable is calledwinning ticker. On any arbitrary observation date, we look at the cumulative future returns for each asset over the rebalancing period.The asset with the highest cumulative returns is assigned as thewinning tickerfor that date (Note that the cumulative returns for cash is assumed to be 1).As part of this exercise, the predicted variable can fall in either one of the below 2 sets: {INFRABEES.NS, HDFCMFGETF.NS, Cash} or {^NSEI, HDFCMFGETF.NS, Cash}The choice of independent variables or features can be numerous. We made the choice of going with standard technical indicators available on talib (specifically MACD, 7-day ROCP and RSI).How exactly we went about choosing the exact types and numbers of indicators is discussed in the subsequent sections.As is it with any good machine learning exercise, we first divide our entire data set into train, validation and test datasets. I chose 60-20-20 as the split. The above-mentioned technical indicators (features) are populated for each asset in the basket along with thewinning tickeri.e., the predicted variable.The choice of classification model to fit your data to and make subsequent predictions can be numerous. Conventional classification models such as:K-nearest neighbours,support vector classifiers,decision tress,logistic regression,ridge regression,naïve bayes - are always the first choice.From there one leverage boosting or bagging techniques if the performance of conventional classifiers is not upto the mark – bagging and boosting the native classifiers, random forests, xgboost etc can be tried out.On the extreme end, we can also leverage neural network classifiers as a last resort if everything else fails.Point to note is that although the predictive power of the classifier would be invoked once at the beginning of every rebalance period, the training and validation itself is carried out on each day of the daily historical time series.Down-sampling in order to keep the granularity of the training and validation datasets equal to the backtesting is unnecessary and would only lead to a reduction in sample size.Infrastructural setupThe code has been setup in as modular a fashion as possible. This is done so as to ensure that minor changes/additions which need to be made for experimentation purposes don’t necessitate a change in the code which implements the core functionality. Also, the entire codebase has been version controlled in git.Salient features/components of the infrastructure are as follows: -lib.enginesMany core functionalities which can be re-used across multiple strategies can be found in lib.engines. This includes various historical data generators, simulators and the strategy ‘interfaces’ to promote duck-typing.The interface style has been chosen to ensure that any strategy which is codified would necessarily have to implement certain key methods so that they can be invoked in common backtester or optimizer scripts.These methods include, but not limited to, ones which read/write relevant market data from/to db/file, write results from the algo execution to db/file, update of indicators, signal generators, order placements, performance metrics computation etc.lib.strategiesThe actual strategies (the classes) can be found in lib.strategies. Each strategy should inherit from one of the interfaces defined in lib.engines to ensure that they can be called by common backtester or optimizer functions.These classes would need to implement all methods listed above in addition to any other bespoke methods depending on strategy functionality.lib.configsThe various strategy configurations are kept fully separate from the core strategy implementations within lib.configs. There are multiple configs intended to help out with various tasks.There is an optimizer config which stores the array/combination of strategy hyperparameters over which the strategy would need to be optimized over.There is another config which store hyperparameter settings for specific runs, uniquely identified using its own run_name identifier string etclib.examplesThe executables can be found in lib.examples. Executables could be optimizer scripts which can be used to sequentially run the test+validation over multiple parameter configurations defined in the optimizer configs.There are backtesting scripts which would run the backtesting based on the run_name input provided to help identify which specific config it needs to run on. Both the optimizer and backtester scripts would save-down bar-by-bar execution details and corresponding performance metrics to file/db.A ‘plotter’ executable script which plots multiple strategy performances against each other has also been included. We only need to specify the file/table names and the plotter executable would do the rest.Each of these executables have been implemented in a way so as to be able to invoke a run via the command line with multiple configurations specifiable via arguments.lib.experimentsThe lib.experiments folder, as the name suggests, includes ad-hoc experimentation codes which have on final bearing on any of the other files.Scripts within this folder include ones used to run the above correlation analysis, trials for various moving averages and another one to experiment with PCA.utils scriptThere is a standalone utils script within lib. In addition to helper functions used across the project, this script also contains the function which assigns and fits the appropriate classification model based on the input parameters provided via the config.Finally, I’ve added a few batch files within the batch folder which prove helpful when we’re looking to run multiple backtesting or optimizer executables sequentially.Analysis of the resultsWe skip through to discuss the final results. The sequence of trials and experimentations undertaken to come up with the final configurations whose backtesting results have been presented here will be discussed in the next section.This is especially important for the ML models where hundreds of different configurations were tested and compared including many classifiers which are not even included in the final results, such as:Ridge/Logistic regression,Bagged KNN,Adaptive Boosting, etc.The total period which was considered for the purpose of this analysis was 5th October 2010 to 29th May 2020. The training-validation-testing split was 60-20-20 for the ML models.For the rule-based momentum allocator this split was 80-20 as there is no training phase, only an optimization phase.Raw ResultsThe strategy comparison over the testing period for {^NSEI, HDFCMFGETF.NS} can be seen below:The strategy comparison over the testing period for {INFRABEES.NS, HDFCMFGETF.NS} can be seen below:Shown below are the performance statistics of each individual strategy for {^NSEI, HDFCMFGETF.NS}:Shown below are the performance statistics of each individual strategy for {INFRABEES.NS, HDFCMFGETF.NS}CommentaryThe rule-basedmomentum tradingrebalancing strategy seems to be the most consistent amongst all strategies considered. In both cases, its performance during the testing phase atleast equals that of the best performing asset in the pair being considered.Amongst the ML models, I find that the KNN classifier with uniform weights gives the most stable results. Like the rule-based strategy, here too the performance in both cases during the testing phase almost matches the performance of the best performing asset. Also, in general KNN with uniform weights is a better choice over KNN with distance-based weights as the results from the later would be heavily biased towards training data which is ‘closest’ to it in terms of Euclidian distance hence making it heavily susceptible to noise.The most optimaldecision treemodel performs quite poorly in both cases and can be safely dropped from consideration. Same can be said for the XGBoost classifier.SVC did stupendously well in the second case. This makes sense when you compare the outsample scores of SVC vs the rest where it visibly outperforms. However, the performance is quite average for the first case. It may not be a good decision to go with a strategy whose performance is dependent on the actual choice of data pairs because that can be taken as an indication that the strategy may potentially not work well under a different regime.It’s difficult to pinpoint how exactly do the fitting scores/metrics translate into strategy performance. But few interesting points to keep in mind:In general, the closer the insample metrics are to the outsample metrics, the better is the performance. A divergence (such as extremely high insample scores and exceptionally low outsample scores) is indicative of overfitting. For example, the divergence looks generally higher for the DecisionTree classifier (for the ‘optimal’ hyperparameters chosen). This classifier also tends to underperform the other classifiers across both cases.In general, the strategy performance is seen to be better for those configurations where the prediction correctness/accuracy is more evenly distributed across all 4 classes. It is also preferrable to have, within the same class, an even distribution amongst precision score and recall score. KNN seems to do well in this regard and we thus see its performance to be relatively more stable across both cases. On the other hand, we notice that the XGB classifier running on the first case has low scores for cash potentially causing the dip in performance. This is also the reason why we should think twice about using the SVC (second case, especially) since its insample recall score for cash is quite low.Experimentations to help with the ML model formulationIn the following section, we discuss some of the many experiments that I needed to run prior to the final backtesting stage.Feature selectionOne of the most essential exercises to be run in the case of ML models is to come up with an appropriate set of features to make your prediction.We initially started-off with manually computed features to represent short-term momentum, short-term risk, long-term momentum and long-term risk.‘Short-term’ was arbitrarily represented by a rolling window of 10 days while ‘long-term’ was arbitrarily represented by a rolling window of 100 days.‘Momentum’ is represented by the mean of the close-to-close returns computed over the selected time window.‘Risk’ is represented by the standard deviation of the close-to-close returns computed over the selected time window.These metrics were computed for each asset within the basket. So, if we choose to have N assets in the basket, we will end up with 4*N features.We pivoted from the above formulation to another one which was based onTA-libindicators. These indicators are numerous but can be classified into a handful functional groups – such as:momentum,volume,volatility,cycle indicators andpattern recognition indicators, to name a few.Initially, the idea was to chose 1-2 representative indicators from each group – ADX, MACD, RSI, ROCP, ATR, OBV.As discussed earlier however, given that every such indicator would be added for each asset in the basket, each new indicator would effectively increase the feature set by ‘N’.Large feature sets in any regression/classification problem would suffer from well knows drawbacks such as overfitting. Therefore, minimizing the feature set to only those which are most important is imperative.Perhaps the most straightforward ways is to leverage one of the many algorithms present in the sklearn.feature_selection module, such as RFE.I however decided to go ahead with a relatively more manual approach of explicitly adding features one-by-one and choosing those which gave the most incremental (qualitative) improvement in insample+outsample fit quality.This turned out to be MACD, RSI and 7-day ROCP. Note that these indicators were computed for each asset in the basket.Feature reduction (PCA)The 3 TA-lib indicators selected above would still mean that we end up with 6 (3*N where N=2) features to run our classification on. It is difficult to conclude whether our formulation would be susceptible to overfitting.Whether or not, it may still be good practice to understand whether our choice of features can be decomposed into fewer components through which we can explain a large fraction of the overall variance. This can be achieved via a simple PCA.We first apply a StandardScaler() transform to each feature individually, prior to running it through PCA. This would help ensure that all features are equalized by converting them into unit variance and 0 mean variables.We can also specify a variance threshold (default of 95%) to help reduce the dimensionality of the feature set. The training/validation/testing is carried out on the transformed+reduced feature set.Feature NormalizationGenerally, in conventional classification/regression problems, normalization has empirically been observed to produce better quality fits.Hence its preferrable to have this as an option – generate fit qualities before and after normalization and observe whether there’s been any significant improvement post normalization.The code has been implemented in such a way so as to be able to easily apply any of the available normalization routines in sklearn. I chose ‘QuantileTransformer’ for the purpose of this exercise.If there is no significant improvement in fit quality post normalization, then it’s better to revert to the non-normalized dataset.Price smoothingFinancial data is known to have a high signal-to-noise ratio. As a result, any ML model we try to fit to financial data would automatically be more susceptible to noise.One way to potentially circumvent this issue is to smoothen the price data by applying any suitable moving average or frequency filters. While such application may increase the SNR (and as a result stabilize variance of the classification model), fudging of the feature values itself may introduce a bias and/or response delay.Therefore, if we don’t observe any significant improvement post application of a smoothing, then its better to revert to the original time series.I tried EMA, DEMA, MAMA, SMA, WMA in an ad-hoc fashion (i.e., not gone as far as to support seamless application of smoothing via config unlike some of the other experiments) by locally changing the code.There were no significant improvements in fit quality. Infact I observed a slight reduction in performance. Hence, decided to go ahead with the raw price data.Sample weightingIt is possible that for samples where the market conditions were benign (each individual asset moved by only small amounts over the rebalance period), thewinning tickerwas more difficult to predict.Moreover, getting thewinning tickerwrong in such a market scenario is also less of a concern as the cost of such a mistake is also relatively small. However, samples derived from said benign market could potentially increase the variability in our model predictions (noisy samples?).Moreover, it is naturally more important to get those predictions correct where the market moved violently which resulted in a high cost of getting thewinning tickerprediction wrong.Keeping this in mind, we include the ability to scale samples by the ‘cost of getting the prediction wrong’. This cost is computed for each sample by taking the sum of squares of the difference in returns between thewinning tickerand the other tickers, including cash.The higher the difference, the larger the weight. As a result, samples derived from more volatile conditions would be assigned larger weight.Hopefully, this would also mean that the high impact scenarios are predicted more accurately.The implementation allows the user to be able to specify whether to apply this weighting scheme or not. The computation of the sample weights itself is hardcoded (the L2-style weighting described above).Note that not all classifiers support application of sample weights. During the course of the experimentation, I did observe that some classifier models seemed to perform better (in terms of overall strategy performance) with sample weighting.Predict probability threshold applicationAll classifier predictions have an associated ‘prediction probability’ which represents the certainty of the prediction. Naturally, higher the prediction probability, higher is the certainty.In a multi-class classification problem such as the one we attempt to solve here, more the classes, lower is the typical probability against a class necessary to assign it as the predicted feature.For example:If there are only 2 classes to choose from, the prediction probability of the class to be assigned as the predicted class for that sample would need to be greater than 50%.If there are 3 classes, then it’s possible that 34% is enough and so on.Therefore, as we increase the number of classes to chose from in our classification problem its possible that our predictions become even noisier and the thresholds get lower.One way to circumvent this issue is to reduce the size of the class set we run our prediction on. This is exactly what was carried out in Section 2.1.Another way is to introduce a degree of conservativeness by explicitly specifying a minimum threshold requirement to make a prediction.For example, we can set a probability threshold of 0.7 and assign the predicted variable as thewinning tickeronly if its probability crosses this threshold. If not, then we assignCashas thewining tickerfor that sample.I considered both 0.5, 0.7 and ‘no threshold’ as the scenarios to optimize on. These values are specifiable via the config.Synthetic data generationWe normally have only limited data to train and test our model on. One of the ways to increase the size of the dataset is to run a simulation. However, we need to account for the underlying characteristics of the stock diffusion such as autocorrelation, volatility clustering etc. You can read more aboutAutocorrelation and Autocovariance.For multi-asset baskets, we would also need to additionally account for the pairwise correlations. All-in-all the exercise would be quite intense.Moreover, if any of the underlying characteristics are not satisfied and we end up training our model on such data then its possible that our final predictions go haywire.So, while I did run some experimentations on synthetic data, I did keep in mind the potential drawbacks. Therefore, any of the optimization results obtained via synthetic data were not used in the actual backtesting. Rather they were only used for ‘exclusion’ testing.For example, if the most optimal configuration obtained on the actual historical data was the least optimal configuration on any synthetic dataset, then that configuration was excluded from the backtesting.Additionally, generation of trivial datasets was helpful to eliminate the presence of any obvious bugs in the code.For example, if you feed in synthetic pair data where one of the assets is always increasing while the other is stagnant (or decreasing), then you would expect the ML classifier to pick up the first asset all the time.Or if the prices oscillate but while one grows the other falls and vice versa, then too you would expect the classifier to make the correct prediction most times.I also implemented a ‘data shuffler’ to act as a proxy to cross validation which was also mostly used only for exclusion testing.OptimizationMost if not all the bells and whistles described in the earlier subsections were optimized upon. We also additionally optimized on specific hyperparameters depending on which classifier was being optimized.A typical configuration over which the optimization is run may look like the following:-The optimization was run both on ‘global’ parameters such as ‘do_pca’, ‘predict_probab_thresh’ etc and on model specific hyperparameters defined under ‘model_params’.The otpimization would be run on a multi-dimensional space defined by the cross product of each individual ‘optimized’ parameter vs the other.Specific experiments such as feature selection, price smoothing, and synthetic data generation were carried out as one-time exercises and not meant to be optimized on.Metrics Generation and comparisonThe final step is to choose the most optimal configuration post the optimization process.The mechanism for determining such a configuration would be based on comparing certain metrics generated by each configuration and picking the one which gave the best results.The list of metrics can be viewed in the table provided under Section 5.1. The most important metrics are the performance indicators such as hit ratio, normalized hit ratio, CAGR, sharpe, sortino etc.Additionally for the ML models we also generate the overall accuracy score and precision and recall scores corresponding to each class, both insample and outsample.Proposing the most optimal configuration from the heap of numbers generated post the optimization step is a non-trivial task. I decided to keep this process manual.Most times we may be tempted to choose the configuration with the highest sharpe/sortino and/or CAGR. However, most times such configurations are simply ‘lucky’ performers.That’s one of the reasons why I decided to run this exercise on 2 separate baskets – {^NSEI, HDFCMFGETF.NS} and {INFRABEES.NS, HDFCMFGETF.NS}.A reasonable configuration should perform decently well for both baskets. Also, as discussed in Section 6.7 they shouldn’t perform badly against synthetic data. More-often-than-not we observe that it’s the configurations in the 70-80%ile range that are the most consistent across scenarios.ConclusionThe conclusion that I was able to draw from the project is that the rule-based momentum rebalancer strategy performed most consistently across all configurations tested.Raw results can be viewed in Section 5.1. The optimization results were relatively more stable and the performances in the validation and testing datasets were more-or-less consistent.When it comes to the ML algorithms, there is quite some scope to improve its performance specifically by considering some of the following additions:-Regime identification via hidden markov models (HMM)Basically, we attempt to cluster the entire historical data period into individual regimes (bear vs bull, benign vs volatile etc) and train different models for different regimes. In backtesting or live trading we would need to first identify the regime and apply a prediction using the model specifically trained for that regime.Better feature selectionThe features were chosen from the choices available on TA-lib. It is possible that there are features out there which are better predictors than TA-lib indicators derived from historical prices. We could consider using alternative data.Robust synthetic data generationWhile this was attempted as described in Section 6.7, its application was limited to blacklisting specific configurations rather than increasing the robustness of existing models by feeding more data. This is certainly something which can improve model performance drastically.Optimize over rebalance periods and/or addition of rebalance triggersI chose a reasonably low rebalance frequency and kept it constant. Its highly likely that the backtesting performance would be monotonically increasing with frequency (the classification models would be expected to make more accurate predictions for shorter prediction intervals).However, higher rebalance frequencies would have incurred higher transaction costs. We could obviously have added transaction costs as a parameter and optimized over rebalance frequency but that would have added a degree of uncertainty as these costs are not easily observable.Additionally, we could have added triggers to signal a premature rebalance opportunity if the asset chosen as thewinning tickerunderperforms the top-performing asset by a certain margin within the rebalance period.This may have ensured that we get out of loss-making positions as soon as possible without waiting for the end of the rebalance period.Long/ShortThis applies both to the rule-based strategy and the ML strategies. Instead of limiting ourselves to only remaining long or nothing, we can also attempt to short the asset which we predict would be the underperformer (with negative returns) over the rebalance period.This has the potential to bump-up our returns by leveraging stock ‘falls’. Also, depending on the broker/exchange, going long+short may reduce our overall margin requirements thus also adding to our overall returns.BibliographyScikit Learn(to understand and setup the various classification algorithms)Stack exchange(for learning)If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!You can access the complete code here:Login to AccessDisclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

We then compute the number of shares by dividing this approximate capital with the prevailing close price of that asset. This number is floored to the nearest integer to get the actual number of shares from which we can obtain the actual assigned capital.

The actual assigned capital is summed up across all assets and the difference of this total amount with the total prevailing capital at that rebalance day is how much is left in cash.

The difference in number of shares assigned per asset on a given rebalance day vs the rebalance day preceding it is the number of shares that needs to be bought/sold on that rebalance day.

It is quite apparent that this is afractionalallocation strategy. We could also switch it to awholeallocation strategy by simply assigning all our capital to the asset with the highest momentum.

But for the purpose of this analysis, we keep the assignment fractional.

Multiclass ML asset allocation

Here we don’t make any decisions based on rules. Rather, we train a multiclass classification model to do the decisioning on our behalf.

Note that in order to maintain simplicity, this ML allocation strategy runs under thewholemode i.e., at the beginning of every rebalance period, our entire capital is to be assigned to the asset attributed as the predictedwinning tickerfor that period.

The predicted (dependent) variable is calledwinning ticker. On any arbitrary observation date, we look at the cumulative future returns for each asset over the rebalancing period.

The asset with the highest cumulative returns is assigned as thewinning tickerfor that date (Note that the cumulative returns for cash is assumed to be 1).

As part of this exercise, the predicted variable can fall in either one of the below 2 sets: {INFRABEES.NS, HDFCMFGETF.NS, Cash} or {^NSEI, HDFCMFGETF.NS, Cash}

The choice of independent variables or features can be numerous. We made the choice of going with standard technical indicators available on talib (specifically MACD, 7-day ROCP and RSI).

How exactly we went about choosing the exact types and numbers of indicators is discussed in the subsequent sections.

As is it with any good machine learning exercise, we first divide our entire data set into train, validation and test datasets. I chose 60-20-20 as the split. The above-mentioned technical indicators (features) are populated for each asset in the basket along with thewinning tickeri.e., the predicted variable.

The choice of classification model to fit your data to and make subsequent predictions can be numerous. Conventional classification models such as:

K-nearest neighbours,

support vector classifiers,

decision tress,

logistic regression,

ridge regression,

naïve bayes - are always the first choice.

From there one leverage boosting or bagging techniques if the performance of conventional classifiers is not upto the mark – bagging and boosting the native classifiers, random forests, xgboost etc can be tried out.

On the extreme end, we can also leverage neural network classifiers as a last resort if everything else fails.

Point to note is that although the predictive power of the classifier would be invoked once at the beginning of every rebalance period, the training and validation itself is carried out on each day of the daily historical time series.

Down-sampling in order to keep the granularity of the training and validation datasets equal to the backtesting is unnecessary and would only lead to a reduction in sample size.

Infrastructural setup

The code has been setup in as modular a fashion as possible. This is done so as to ensure that minor changes/additions which need to be made for experimentation purposes don’t necessitate a change in the code which implements the core functionality. Also, the entire codebase has been version controlled in git.

Salient features/components of the infrastructure are as follows: -

lib.engines

Many core functionalities which can be re-used across multiple strategies can be found in lib.engines. This includes various historical data generators, simulators and the strategy ‘interfaces’ to promote duck-typing.

The interface style has been chosen to ensure that any strategy which is codified would necessarily have to implement certain key methods so that they can be invoked in common backtester or optimizer scripts.

These methods include, but not limited to, ones which read/write relevant market data from/to db/file, write results from the algo execution to db/file, update of indicators, signal generators, order placements, performance metrics computation etc.

lib.strategies

The actual strategies (the classes) can be found in lib.strategies. Each strategy should inherit from one of the interfaces defined in lib.engines to ensure that they can be called by common backtester or optimizer functions.

These classes would need to implement all methods listed above in addition to any other bespoke methods depending on strategy functionality.

lib.configs

The various strategy configurations are kept fully separate from the core strategy implementations within lib.configs. There are multiple configs intended to help out with various tasks.

There is an optimizer config which stores the array/combination of strategy hyperparameters over which the strategy would need to be optimized over.

There is another config which store hyperparameter settings for specific runs, uniquely identified using its own run_name identifier string etc

lib.examples

The executables can be found in lib.examples. Executables could be optimizer scripts which can be used to sequentially run the test+validation over multiple parameter configurations defined in the optimizer configs.

There are backtesting scripts which would run the backtesting based on the run_name input provided to help identify which specific config it needs to run on. Both the optimizer and backtester scripts would save-down bar-by-bar execution details and corresponding performance metrics to file/db.

A ‘plotter’ executable script which plots multiple strategy performances against each other has also been included. We only need to specify the file/table names and the plotter executable would do the rest.

Each of these executables have been implemented in a way so as to be able to invoke a run via the command line with multiple configurations specifiable via arguments.

lib.experiments

The lib.experiments folder, as the name suggests, includes ad-hoc experimentation codes which have on final bearing on any of the other files.

Scripts within this folder include ones used to run the above correlation analysis, trials for various moving averages and another one to experiment with PCA.

utils script

There is a standalone utils script within lib. In addition to helper functions used across the project, this script also contains the function which assigns and fits the appropriate classification model based on the input parameters provided via the config.

Finally, I’ve added a few batch files within the batch folder which prove helpful when we’re looking to run multiple backtesting or optimizer executables sequentially.

Analysis of the results

We skip through to discuss the final results. The sequence of trials and experimentations undertaken to come up with the final configurations whose backtesting results have been presented here will be discussed in the next section.

This is especially important for the ML models where hundreds of different configurations were tested and compared including many classifiers which are not even included in the final results, such as:

Ridge/Logistic regression,

Bagged KNN,

Adaptive Boosting, etc.

The total period which was considered for the purpose of this analysis was 5th October 2010 to 29th May 2020. The training-validation-testing split was 60-20-20 for the ML models.

For the rule-based momentum allocator this split was 80-20 as there is no training phase, only an optimization phase.

Raw Results

The strategy comparison over the testing period for {^NSEI, HDFCMFGETF.NS} can be seen below:

The strategy comparison over the testing period for {INFRABEES.NS, HDFCMFGETF.NS} can be seen below:

Shown below are the performance statistics of each individual strategy for {^NSEI, HDFCMFGETF.NS}:

Shown below are the performance statistics of each individual strategy for {INFRABEES.NS, HDFCMFGETF.NS}

Commentary

The rule-basedmomentum tradingrebalancing strategy seems to be the most consistent amongst all strategies considered. In both cases, its performance during the testing phase atleast equals that of the best performing asset in the pair being considered.

Amongst the ML models, I find that the KNN classifier with uniform weights gives the most stable results. Like the rule-based strategy, here too the performance in both cases during the testing phase almost matches the performance of the best performing asset. Also, in general KNN with uniform weights is a better choice over KNN with distance-based weights as the results from the later would be heavily biased towards training data which is ‘closest’ to it in terms of Euclidian distance hence making it heavily susceptible to noise.

The most optimaldecision treemodel performs quite poorly in both cases and can be safely dropped from consideration. Same can be said for the XGBoost classifier.

SVC did stupendously well in the second case. This makes sense when you compare the outsample scores of SVC vs the rest where it visibly outperforms. However, the performance is quite average for the first case. It may not be a good decision to go with a strategy whose performance is dependent on the actual choice of data pairs because that can be taken as an indication that the strategy may potentially not work well under a different regime.

It’s difficult to pinpoint how exactly do the fitting scores/metrics translate into strategy performance. But few interesting points to keep in mind:

In general, the closer the insample metrics are to the outsample metrics, the better is the performance. A divergence (such as extremely high insample scores and exceptionally low outsample scores) is indicative of overfitting. For example, the divergence looks generally higher for the DecisionTree classifier (for the ‘optimal’ hyperparameters chosen). This classifier also tends to underperform the other classifiers across both cases.

In general, the strategy performance is seen to be better for those configurations where the prediction correctness/accuracy is more evenly distributed across all 4 classes. It is also preferrable to have, within the same class, an even distribution amongst precision score and recall score. KNN seems to do well in this regard and we thus see its performance to be relatively more stable across both cases. On the other hand, we notice that the XGB classifier running on the first case has low scores for cash potentially causing the dip in performance. This is also the reason why we should think twice about using the SVC (second case, especially) since its insample recall score for cash is quite low.

Experimentations to help with the ML model formulation

In the following section, we discuss some of the many experiments that I needed to run prior to the final backtesting stage.

Feature selection

One of the most essential exercises to be run in the case of ML models is to come up with an appropriate set of features to make your prediction.

We initially started-off with manually computed features to represent short-term momentum, short-term risk, long-term momentum and long-term risk.

‘Short-term’ was arbitrarily represented by a rolling window of 10 days while ‘long-term’ was arbitrarily represented by a rolling window of 100 days.

‘Momentum’ is represented by the mean of the close-to-close returns computed over the selected time window.

‘Risk’ is represented by the standard deviation of the close-to-close returns computed over the selected time window.

These metrics were computed for each asset within the basket. So, if we choose to have N assets in the basket, we will end up with 4*N features.

We pivoted from the above formulation to another one which was based onTA-libindicators. These indicators are numerous but can be classified into a handful functional groups – such as:

momentum,

volume,

volatility,

cycle indicators and

pattern recognition indicators, to name a few.

Initially, the idea was to chose 1-2 representative indicators from each group – ADX, MACD, RSI, ROCP, ATR, OBV.

As discussed earlier however, given that every such indicator would be added for each asset in the basket, each new indicator would effectively increase the feature set by ‘N’.

Large feature sets in any regression/classification problem would suffer from well knows drawbacks such as overfitting. Therefore, minimizing the feature set to only those which are most important is imperative.

Perhaps the most straightforward ways is to leverage one of the many algorithms present in the sklearn.feature_selection module, such as RFE.

I however decided to go ahead with a relatively more manual approach of explicitly adding features one-by-one and choosing those which gave the most incremental (qualitative) improvement in insample+outsample fit quality.

This turned out to be MACD, RSI and 7-day ROCP. Note that these indicators were computed for each asset in the basket.

Feature reduction (PCA)

The 3 TA-lib indicators selected above would still mean that we end up with 6 (3*N where N=2) features to run our classification on. It is difficult to conclude whether our formulation would be susceptible to overfitting.

Whether or not, it may still be good practice to understand whether our choice of features can be decomposed into fewer components through which we can explain a large fraction of the overall variance. This can be achieved via a simple PCA.

We first apply a StandardScaler() transform to each feature individually, prior to running it through PCA. This would help ensure that all features are equalized by converting them into unit variance and 0 mean variables.

We can also specify a variance threshold (default of 95%) to help reduce the dimensionality of the feature set. The training/validation/testing is carried out on the transformed+reduced feature set.

Feature Normalization

Generally, in conventional classification/regression problems, normalization has empirically been observed to produce better quality fits.

Hence its preferrable to have this as an option – generate fit qualities before and after normalization and observe whether there’s been any significant improvement post normalization.

The code has been implemented in such a way so as to be able to easily apply any of the available normalization routines in sklearn. I chose ‘QuantileTransformer’ for the purpose of this exercise.

If there is no significant improvement in fit quality post normalization, then it’s better to revert to the non-normalized dataset.

Price smoothing

Financial data is known to have a high signal-to-noise ratio. As a result, any ML model we try to fit to financial data would automatically be more susceptible to noise.

One way to potentially circumvent this issue is to smoothen the price data by applying any suitable moving average or frequency filters. While such application may increase the SNR (and as a result stabilize variance of the classification model), fudging of the feature values itself may introduce a bias and/or response delay.

Therefore, if we don’t observe any significant improvement post application of a smoothing, then its better to revert to the original time series.

I tried EMA, DEMA, MAMA, SMA, WMA in an ad-hoc fashion (i.e., not gone as far as to support seamless application of smoothing via config unlike some of the other experiments) by locally changing the code.

There were no significant improvements in fit quality. Infact I observed a slight reduction in performance. Hence, decided to go ahead with the raw price data.

Sample weighting

It is possible that for samples where the market conditions were benign (each individual asset moved by only small amounts over the rebalance period), thewinning tickerwas more difficult to predict.

Moreover, getting thewinning tickerwrong in such a market scenario is also less of a concern as the cost of such a mistake is also relatively small. However, samples derived from said benign market could potentially increase the variability in our model predictions (noisy samples?).

Moreover, it is naturally more important to get those predictions correct where the market moved violently which resulted in a high cost of getting thewinning tickerprediction wrong.

Keeping this in mind, we include the ability to scale samples by the ‘cost of getting the prediction wrong’. This cost is computed for each sample by taking the sum of squares of the difference in returns between thewinning tickerand the other tickers, including cash.

The higher the difference, the larger the weight. As a result, samples derived from more volatile conditions would be assigned larger weight.

Hopefully, this would also mean that the high impact scenarios are predicted more accurately.

The implementation allows the user to be able to specify whether to apply this weighting scheme or not. The computation of the sample weights itself is hardcoded (the L2-style weighting described above).

Note that not all classifiers support application of sample weights. During the course of the experimentation, I did observe that some classifier models seemed to perform better (in terms of overall strategy performance) with sample weighting.

Predict probability threshold application

All classifier predictions have an associated ‘prediction probability’ which represents the certainty of the prediction. Naturally, higher the prediction probability, higher is the certainty.

In a multi-class classification problem such as the one we attempt to solve here, more the classes, lower is the typical probability against a class necessary to assign it as the predicted feature.

For example:If there are only 2 classes to choose from, the prediction probability of the class to be assigned as the predicted class for that sample would need to be greater than 50%.If there are 3 classes, then it’s possible that 34% is enough and so on.Therefore, as we increase the number of classes to chose from in our classification problem its possible that our predictions become even noisier and the thresholds get lower.

One way to circumvent this issue is to reduce the size of the class set we run our prediction on. This is exactly what was carried out in Section 2.1.

Another way is to introduce a degree of conservativeness by explicitly specifying a minimum threshold requirement to make a prediction.

For example, we can set a probability threshold of 0.7 and assign the predicted variable as thewinning tickeronly if its probability crosses this threshold. If not, then we assignCashas thewining tickerfor that sample.

I considered both 0.5, 0.7 and ‘no threshold’ as the scenarios to optimize on. These values are specifiable via the config.

Synthetic data generation

We normally have only limited data to train and test our model on. One of the ways to increase the size of the dataset is to run a simulation. However, we need to account for the underlying characteristics of the stock diffusion such as autocorrelation, volatility clustering etc. You can read more aboutAutocorrelation and Autocovariance.

For multi-asset baskets, we would also need to additionally account for the pairwise correlations. All-in-all the exercise would be quite intense.

Moreover, if any of the underlying characteristics are not satisfied and we end up training our model on such data then its possible that our final predictions go haywire.

So, while I did run some experimentations on synthetic data, I did keep in mind the potential drawbacks. Therefore, any of the optimization results obtained via synthetic data were not used in the actual backtesting. Rather they were only used for ‘exclusion’ testing.

For example, if the most optimal configuration obtained on the actual historical data was the least optimal configuration on any synthetic dataset, then that configuration was excluded from the backtesting.

Additionally, generation of trivial datasets was helpful to eliminate the presence of any obvious bugs in the code.

For example, if you feed in synthetic pair data where one of the assets is always increasing while the other is stagnant (or decreasing), then you would expect the ML classifier to pick up the first asset all the time.

Or if the prices oscillate but while one grows the other falls and vice versa, then too you would expect the classifier to make the correct prediction most times.

I also implemented a ‘data shuffler’ to act as a proxy to cross validation which was also mostly used only for exclusion testing.

Optimization

Most if not all the bells and whistles described in the earlier subsections were optimized upon. We also additionally optimized on specific hyperparameters depending on which classifier was being optimized.

A typical configuration over which the optimization is run may look like the following:-

The optimization was run both on ‘global’ parameters such as ‘do_pca’, ‘predict_probab_thresh’ etc and on model specific hyperparameters defined under ‘model_params’.

The otpimization would be run on a multi-dimensional space defined by the cross product of each individual ‘optimized’ parameter vs the other.

Specific experiments such as feature selection, price smoothing, and synthetic data generation were carried out as one-time exercises and not meant to be optimized on.

Metrics Generation and comparison

The final step is to choose the most optimal configuration post the optimization process.

The mechanism for determining such a configuration would be based on comparing certain metrics generated by each configuration and picking the one which gave the best results.

The list of metrics can be viewed in the table provided under Section 5.1. The most important metrics are the performance indicators such as hit ratio, normalized hit ratio, CAGR, sharpe, sortino etc.

Additionally for the ML models we also generate the overall accuracy score and precision and recall scores corresponding to each class, both insample and outsample.

Proposing the most optimal configuration from the heap of numbers generated post the optimization step is a non-trivial task. I decided to keep this process manual.

Most times we may be tempted to choose the configuration with the highest sharpe/sortino and/or CAGR. However, most times such configurations are simply ‘lucky’ performers.

That’s one of the reasons why I decided to run this exercise on 2 separate baskets – {^NSEI, HDFCMFGETF.NS} and {INFRABEES.NS, HDFCMFGETF.NS}.

A reasonable configuration should perform decently well for both baskets. Also, as discussed in Section 6.7 they shouldn’t perform badly against synthetic data. More-often-than-not we observe that it’s the configurations in the 70-80%ile range that are the most consistent across scenarios.

Conclusion

The conclusion that I was able to draw from the project is that the rule-based momentum rebalancer strategy performed most consistently across all configurations tested.

Raw results can be viewed in Section 5.1. The optimization results were relatively more stable and the performances in the validation and testing datasets were more-or-less consistent.

When it comes to the ML algorithms, there is quite some scope to improve its performance specifically by considering some of the following additions:-

Regime identification via hidden markov models (HMM)

Basically, we attempt to cluster the entire historical data period into individual regimes (bear vs bull, benign vs volatile etc) and train different models for different regimes. In backtesting or live trading we would need to first identify the regime and apply a prediction using the model specifically trained for that regime.

Better feature selection

The features were chosen from the choices available on TA-lib. It is possible that there are features out there which are better predictors than TA-lib indicators derived from historical prices. We could consider using alternative data.

Robust synthetic data generation

While this was attempted as described in Section 6.7, its application was limited to blacklisting specific configurations rather than increasing the robustness of existing models by feeding more data. This is certainly something which can improve model performance drastically.

Optimize over rebalance periods and/or addition of rebalance triggers

I chose a reasonably low rebalance frequency and kept it constant. Its highly likely that the backtesting performance would be monotonically increasing with frequency (the classification models would be expected to make more accurate predictions for shorter prediction intervals).

However, higher rebalance frequencies would have incurred higher transaction costs. We could obviously have added transaction costs as a parameter and optimized over rebalance frequency but that would have added a degree of uncertainty as these costs are not easily observable.

Additionally, we could have added triggers to signal a premature rebalance opportunity if the asset chosen as thewinning tickerunderperforms the top-performing asset by a certain margin within the rebalance period.

This may have ensured that we get out of loss-making positions as soon as possible without waiting for the end of the rebalance period.

Long/Short

This applies both to the rule-based strategy and the ML strategies. Instead of limiting ourselves to only remaining long or nothing, we can also attempt to short the asset which we predict would be the underperformer (with negative returns) over the rebalance period.

This has the potential to bump-up our returns by leveraging stock ‘falls’. Also, depending on the broker/exchange, going long+short may reduce our overall margin requirements thus also adding to our overall returns.

Bibliography

Scikit Learn(to understand and setup the various classification algorithms)

Stack exchange(for learning)

If you want to learn various aspects of Algorithmic trading then check out theExecutive Programme in Algorithmic Trading (EPAT). The course covers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading. EPAT equips you with the required skill sets to build a promising career in algorithmic trading.Enroll now!

You can access the complete code here:

Login to Access

Disclaimer: The information in this project is true and complete to the best of our Student’s knowledge. All recommendations are made without guarantee on the part of the student or QuantInsti®. The student and QuantInsti®disclaim any liability in connection with the use of this information. All content provided in this project is for informational purposes only and we do not guarantee that by using the guidance you will derive a certain profit.

---

*Imported from QuantInsti Blog on 2026-04-27*
