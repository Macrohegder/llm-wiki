---
title: "Kalman Filter Python: Tutorial and Strategies"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/kalman-filter/"
date: "2024-05-07"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Kalman Filter Python: Tutorial and Strategies

**来源**: [QuantInsti](https://blog.quantinsti.com/kalman-filter/)  
**日期**: 2024-05-07  
**作者**: QuantInsti

---

## 原文

Kalman Filter Python: Tutorial and Strategies

Originally written byRekhit Pachanekarand Edited byChainika Thakar

The Kalman filter, developed by Rudolf Kalman in the 1960s, is a powerful mathematical tool used for estimating the state of a dynamic system from a series of noisy measurements. Originally designed for aerospace applications, the Kalman filter has found widespread use in various fields, including finance and trading.

At its core, the Kalman filter combines information from a series of measurements with predictions from a dynamic model to produce optimal estimates of the system's state. It does so by recursively updating its estimate based on new measurements, while also taking into account the uncertainty associated with both the measurements and the model predictions.

This blog covers:

What is a Kalman filter?

Applications of Kalman filter in trading

Real-world examples of Kalman filter usage in trading

Key statistical terms and concepts of Kalman filterKalman filter equationsStatus update equationState extrapolation equationKalman gain equationEstimate uncertainty updateEstimate uncertainty extrapolation

Kalman filter equations

Status update equation

State extrapolation equation

Kalman gain equation

Estimate uncertainty update

Estimate uncertainty extrapolation

Kalman filter and other filtering techniques

Steps for implementing Kalman filter in Python

Pairs trading using Kalman filter in Python

Future trends and developments in Kalman filter technology

What is a Kalman filter?

Imagine the Kalman filter as a useful conductor leading an orchestra of data. What is the use of it?⁽¹⁾

The use would be to seamlessly merge noisy measurements with predictive models and craft an estimation of a system's state. This blend of past observations and dynamic forecasts is the secret, empowering traders to sail through the uncertainty in the markets with confidence.

Next, we will talk about the applications of the Kalman filter in the trading domain.

Applications of Kalman filter in trading

Below are some useful applications of the Kalman filter in trading.

Pairs Trading:One common application of the Kalman filter in trading ispairs trading, where traders identify pairs of assets with a historically stable relationship and exploit deviations from this relationship. The Kalman filter can be used to dynamically estimate the hedge ratio between the two assets and adjust trading positions as the relationship evolves over time.

Volatility Estimation:In options trading, accurately estimating volatility is crucial for pricing and risk management. The Kalman filter can be employed to estimate volatility from noisy market data, providing traders with more reliable inputs for option pricing models and hedging strategies.

Market Impact Modelling:When executing large trades, traders need to consider the potential impact on market prices. The Kalman filter can help in modelling market impact by estimating the relationship between trade size and price movements, allowing traders to optimise trade execution strategies to minimise costs.

Portfolio Optimisation:The Kalman filter can aid in portfolio optimisation by estimating thecovariance matrixof asset returns. By incorporating these estimates into mean-variance optimisation models, traders can construct more efficient portfolios that maximise returns for a given level of risk.

Now, let us move ahead to find out the real world examples of usage of the Kalman filter.

Real-world examples of Kalman filter usage in trading

One quite interesting real world example of Kalman filter usage is depicted in anarticle by Bayes Business Schoolin the United Kingdom. An event was held in the school in 2020 led by Dr Veronika Lunina, Quantitative Vice President at NatWest Markets.

In this event, Dr Veronika spoke about the use of the Kalman filter and was positive about her own experiences using the extended Kalman filter for automated marking of FX implied volatility surface.

According to aresearch paper, Nkomo et al. (2013) introduced the Kalman filter to process stock price data and proposed the K-AC-M algorithm based on the Kalman filter, leveragingmomentum effectsto expand the AC algorithm and obtained superior excess returns in strategy simulation compared to the AC algorithm.

Jin et al. (2013) initially combined the traditional autoregressive (AR) model with the Kalman filter to obtain improved predictive performance over a single AR model and a single Kalman filter. They further combined the support vector regression (SVR) with the UKF into a new model, with SVR used to address parameter selection issues in the UKF.⁽²⁾

As such, the Kalman filter can be considered a heavy topic when it comes to the use of maths and statistics. Thus, we will go through a few terms before we dig into the equations. Feel free to skip this section and head directly to the equations if you wish.

Key statistical terms and concepts of Kalman filter

Kalman Filter uses the concept of a normal distribution in its equation to give us an idea about the accuracy of the estimate. Let us step back a little and understand how we get a normal distribution of a variable.

Let us suppose we have a football team of ten people who are playing the nationals. As part of a standard health check-up, we measure their weights. The weights of the players are given below.

Player Number

Weight

Now if we calculate the average weight, ie the mean, we get the value as (Total of all player weights) / (Total no. of players)

= 720/10 = 72

The mean is usually denoted by the Greek alphabet μ. If we consider the weights as w1, w2 respectively and the total number of players as N, we can write it as: μ = (w1 + w2+ w3+ w4+.....+ wn)/N

Now, on a hunch, we decide on seeing how much each player’s weight varies from the mean. This can be easily calculated by subtracting the individual’s weight from the mean value.

Now, the first team player’s weight varies in the following manner,

(Individual player’s weight) - (Mean value) = 72 - 72 = 0.

Similarly, the second player’s weight varies by the following: 75 - 72 = 3.

Let’s update the table now.

Player Number

Weight

Difference from mean

Now, we want to see how much the entire team’s weights vary from the mean. A simple addition of the entire team’s weight difference from the mean would be 0 as shown below.

Thus, we square each individual’s weight difference and find the average. Squaring is done to eliminate the negative sign of a score + penalise greater divergence from the mean.

The updated table is as follows:

Player Number

Weight

Difference from mean

Squared difference from the mean

Now if we take the average, we get the equation as,

The variance tells us how much the weights have been spread. Since the variance is the average of the squares, we will take the square root of the variance to give us a better idea of the distribution of weights. We call this term the standard deviation and denote it by σ.

Since standard deviation is denoted by σ, the variance is denoted by σ2.

But why do we need standard deviation?

While we calculated the variance and standard deviation of one football team, maybe we could find for all the football teams in the tournament, or if we are more ambitious, we can do the same for all the football teams in the world. That would be a large dataset.

One thing to understand is that for a small dataset we used all the values, i.e. the entire population to compute the values. However, if it is a large dataset, we usually take a sample at random from the entire population and find the estimated values.

In this case, we replace N by (N-1) to get the most accurate answer as perBessel's correction. Of course, this introduces some errors, but we will ignore it for now.

Thus, the updated equation is,

Now, looking at different research conducted in the past, it was found that given a large dataset, most of the data was concentrated around the mean, with 68% of the entire data variables coming within one standard deviation from the mean.

This means that if we had data about millions of football players, and we got the same standard deviation and variance which we received now, we would say that the probability that the player’s weight is +-3.46 from 72 kg is 68.26%. This means that 68.26% of the players’ weights would be from 68.53 kg to 75.46.

Of course, for this to be right, the data should be random.

Let’s draw a graph to understand this further. This is just a reference of how the distribution will look if we had the weights of 100 people with mean as 72 and standard deviation as 3.46.

This shows how the weights are concentrated around the mean and taper off towards the extremes. If we create a curve, you will find that it is shaped like a bell and thus we call it a bell curve. Thenormal distributionof the weights with mean as 72 and standard deviation as 3.46 will look similar to the following diagram.

Normal distribution is also called aprobability density function. While the derivation is quite lengthy, we have certain observations regarding the probability density function.

One standard deviation contains 68.26% of the population.

Two standard deviations contain 95.44% of the population while three contain 99.74%.

The probability density function is given as follows,

The reason we talked about normal distribution is that it forms an important part in Kalman filters.

Let’s now move on to the Kalman filter equations.

Kalman filter equations

Kalman Filter is a type of prediction algorithm. Thus, the Kalman filter’s success depends on our estimated values and its variance from the actual values. In the Kalman filter, we assume that depending on the previous state, we can predict the next state.

At the outset, we would like to clarify that this Kalman Filter tutorial is not about the derivation of the equations but trying to explain how the equations help us in estimating or predicting a value.

Now, as we said earlier, we are trying to predict the value of something which cannot be directly measured. Thus, there will obviously be some error in the predicted value and the actual value.

If the system itself contains some errors, then it is calledmeasurement noise.For example, if the weighing scale itself shows different readings for the same football player, it will be measurement noise.

If the process when the measurement takes place has certain factors which are not taken into account, then it is calledprocess noise.For example, if we are predicting the Apollo Rocket’s position, and we could not account for the wind during the initial blast off phase, then we will encounter some error between the actual location and the predicted location.

Kalman Filter is used to reduce these errors and successfully predict the next state.

Now, suppose we pick out one player and weigh that individual 10 times, we might get different values due to some measurement errors.

Mr. Rudolf Kalman developed the status update equation taking into account three values, i.e.

True value

The estimated or predicted value

Measured value

Status update equation

The status update equation is as follows:

Current state estimated value= Predicted value of current state + Kalman Gain * ( measured value - predicted value of the state)

Let us understand this equation further.

In our example, we can say that given the measured values of all ten measurements, we will take the average of the values to estimate the true value.

To work this equation, we take one measurement which becomes the measured value. In the initial step, we guess the predicted value.

Now since the average is computed, in this example, the Kalman gain would be (1/N) as with each successive iteration, the second part of the equation would be decreasing, thus giving us a better-estimated value.

We should note that the current estimated value becomes the predicted value of the current state in the next iteration.

For now, we know that the actual weight is constant, and hence it was easy to predict the estimated value. But what if we had to take into account that the state of the system (which was the weight in this case) changes?

For that, we will now move on to the next equation in the Kalman Filter tutorial i.e. State extrapolation.

State extrapolation equation

The state extrapolation system helps us to find the relation between the current state and the next state i.e. predict the next state of the system.

Until now, we understood that the Kalman filter is recursive in nature and uses the previous values to predict the next value in a system. While we can easily give the formula and be done with it, we want to understand exactly why it is used. In that respect, we will take another example to illustrate the state extrapolation equation.

Now, let’s take the example of a company trying to develop a robotic bike. If you think about it, when someone is riding a bike, they have to balance the bike, control the accelerator, turn etc.

Let’s say that we have a straight road and we have to control the bike’s velocity. For this, we would have to know the bike’s position. As a simple case, we measure the wheels’ rotation to predict how much the bike has moved. We remember that the distance travelled by an object is equal to the velocity of the object multiplied by the time travelled.

Now, Let’s suppose we measure the rotation at a certain instant of time, ie Δt.

If we say that the bike has a constant velocity v, then we can say the following:

The predicted position of the bike is equal to the current estimated position of the bike + the distance covered by the bike in time Δt.

Here the distance covered by the bike will be the result of Δt multiplied by the velocity of the bike.

Suppose that the velocity is kept constant at 2 m/s. And the time Δt is 5 seconds. That means the bike moves 10 metres between every successive measurement.

But what if we check the next time and find out the bike moved 12 metres? This gives us an error of 2 metres. This could mean two things,

The device used to measure the velocity has an error (measurement error)

The bike is moving at different velocities, in this instance maybe it is a downhill slope (process error)

We try to find out how to minimise this error by having different gains to apply to the state update equation.

Now, we will introduce a new concept to the Kalman filter tutorial, i.e. the α - β filter.

Now, if we recall the status update equation, it was given as,

Current state estimated value= Predicted value of current state + Kalman Gain * ( measured value - predicted value of the state)

We will say that α is used to reduce the error in the measurement, and thus it will be used to predict the value of the position of the object.

Now if we keep the α in place of the Kalman gain, you can deduce that a high value of α gives more importance to the measured value and a low level of α gives less weightage to the measured value. In this way, we can reduce the error while predicting the position.

Now, if we assume that the bike is moving with different velocities, we would have to use another equation to compute the velocity and which in turn would lead to a better prediction to the position of the bike. Here we use β in place of Kalman gain to estimate the velocity of the bike.

We tried to see the relation of how α and β impact the predicted value. But how do we know for sure the correct value of α and β in order to get the predicted value closer to the actual value?

Let us move on to the next equation in the Kalman filter tutorial, i.e. the Kalman Gain equation.

Kalman gain equation

Recall that we talked about the normal distribution in the initial part of this blog. Now, we can say that the errors, whether measurement or process, are random and normally distributed in nature. In fact, taking it further, there is a higher chance that the estimated values will be within one standard deviation from the actual value.

Now, Kalman gain is a term which talks about the uncertainty of the error in the estimate. Put simply, we denote ρ as the estimated uncertainty.

Since we use σ as the standard deviation, we would denote the variance of the measurement σ2 due to the uncertainty as ⋎.

Thus, we can write the Kalman Gain as,

(Uncertainty in estimate)

(Uncertainty in estimate + Uncertainty in measurement)

(Uncertainty in estimate)(Uncertainty in estimate + Uncertainty in measurement)

In the Kalman filter, the Kalman gain can be used to change the estimate depending on the estimated measure.

Since we saw the computation of the Kalman gain, in the next equation we will understand how to update the estimated uncertainty.

Before we move to the next equation in the Kalman filter tutorial, we will see the concepts we have gone through so far. We first looked at the state update equation which is the main equation of the Kalman filter.

We further understood how we extrapolate the current estimated value to the predicted value which becomes the current estimate in the next step. The third equation is the Kalman gain equation which tells us how the uncertainty in the error plays a role in calculating the Kalman gain.

Now we will see how we update the Kalman gain in the Kalman filter equation.

Let’s move on to the fourth equation in the Kalman filter tutorial.

Estimate uncertainty update

In the Kalman Filter tutorial, we saw that the Kalman gain was dependent on the uncertainty in the estimation. Now, as we know with every successive step, the Kalman Filter continuously updates the predicted value so that we get the estimated value as close to the actual value of a variable, thus, we have to see how this uncertainty in the error can be reduced.

While the derivation of the equation is lengthy, we are only concerned about the equation.

Thus, the estimate uncertainty update equation tells us that the estimated uncertainty of the current state varies from the previous estimate uncertainty by the factor of (1 - Kalman gain). We can also call this the covariance update equation.

This brings us to the last equation of the Kalman filter tutorial, which we will see below.

Estimate uncertainty extrapolation

The reason why the Kalman filter is popular is because it continuously updates its state depending on the predicted and measured current value. Recall that in the second equation, we had extrapolated the state of the estimate. Similarly, the estimated uncertainty of the current error is used to predict the uncertainty of the error in the next state.

Ok. That was simple!

This was a no equation way to describe the Kalman filter. If you are confused, let us go through the process and see what we have learned so far.

For input, we have measured value. Initially, we use certain parameters for the Kalman gain as well as the predicted value. We will also make a note of the estimated uncertainty.

Now we use the Kalman filter equation to find the next predicted value.

In the next iteration, depending on how accurate our predicted variable was, we make changes to the uncertainty estimate which in turn would modify our Kalman gain.

Thus, we get a new predicted value which will be used as our current estimate in the next phase.

In this way, with each step, we would get closer to predicting the actual value with a reasonable amount of success.

That is all there is to it. We would reiterate in this Kalman filter tutorial that the reason the Kalman filter is popular is because it only needs the previous value as input and depending on the uncertainty in the measurement, the resulting value is predicted.

In the real world, the Kalman filter is used by implementing matrix operations as the complexity increases when we take real-world situations. If you are interested in the maths part of the Kalman filter, you can go through thisresourceto find many examples illustrating the individual equations of the Kalman filter.

Moving forward, we will see the comparison of Kalman filter with other filtering techniques to make the topic more clear.

Kalman filter and other filtering techniques

Let us dive into the differences between Kalman filtering and other filtering techniques on the basis of advantages, disadvantages and applicability of each technique.⁽³⁾

Filtering Technique

Advantages

Disadvantages

Applicability

Kalman Filter

Optimal under Gaussian noise assumptions. Efficient for linear systems. Provides estimates of state and error covariance.

Assumes linearity and Gaussian noise, which may not hold in all cases. Can be computationally expensive for high-dimensional systems.

Tracking moving averages in trading algorithms. Predicting future price movements based on historical data.

Extended Kalman Filter (EKF)

Allows for nonlinear system models by linearizing them via Taylor series expansion. More flexible than the standard Kalman filter.

Linearization introduces approximation errors, leading to suboptimal performance in highly nonlinear systems. May suffer from divergence issues if the linearization is inaccurate.

Modelling complextrading strategiesinvolving non-linear relationships between market variables.

Unscented Kalman Filter (UKF)

Avoids linearization by propagating a set of sigma points through the nonlinear functions. More accurate than EKF for highly nonlinear systems. Better performance with non-Gaussian noise.

Requires tuning parameters for the selection of sigma points, which can be challenging. May suffer from sigma point degeneracy in high-dimensional spaces.

Estimating the state of a financial market model with highly nonlinear dynamics.

Particle Filter (Sequential Monte Carlo)

Handles nonlinear and non-Gaussian systems without requiring linearisation. Robust to multimodal distributions. Can represent complex distributions with particles.

Computational complexity increases with the number of particles, making it less efficient for high-dimensional state spaces. Sampling inefficiency can lead to particle degeneracy and sample impoverishment.

Tracking multiple potential market scenarios simultaneously, such as predicting the movement of various assets in a portfolio.

Complementary Filter

Simple to implement and computationally efficient. Effective for fusing data from multiple sensors with complementary characteristics.

Requires manual tuning of sensor fusion parameters, which may not be optimal in all situations. Limited applicability to systems with highly correlated sensor errors.

Combining technical indicators, such as moving averages and momentum oscillators, to generate trading signals.

When it comes to trading, the Kalman filter forms an important component in the pairs trading strategy. Let us build a simple pairs trading strategy using the Kalman Filter inPythonnow.

Steps for implementing Kalman filter in Python

Implementing a Kalman filter in Python involves several steps.

Here's a basic guide to the steps used:

Step 1: Import Libraries

Step 2: Initialise State and Covariance

Step 3: Iterative Update

Step 4: Visualisation

Step 1: Import Libraries

Step 2: Initialise State and Covariance

Step 3: Iterative Update

Step 4: Visualisation

Output:

Here's what each component of the plot represents:

True State:This is the true underlying state of the system over time. It represents the ideal scenario without any noise or errors.

Estimated State:This is the state estimated by the Kalman filter based on the noisy measurements. The Kalman filter attempts to estimate the true state by combining the predictions from the system dynamics and the corrections from the measurements.

Measurements:These are the noisy measurements obtained from sensors or other sources. They represent the imperfect observations of the true state.

The plot allows you to visualise how well the Kalman filter is able to estimate the true state despite the presence of noise in the measurements.

Ideally, the estimated state should closely track the true state, providing a smooth and accurate representation of the underlying system dynamics.

Next, we will see the use of the Kalman filter in the pairs trading strategy where the Kalman filter is mostly used.

Pairs trading using Kalman filter in Python

(Thanks toChamundeswari Koppisettifor providing the code.)

Step 1: Import libraries

Let us start by importing the necessary libraries for the Kalman Filter.

Step 2: Fetch data

We will consider the 4 years (January 1st, 2020 - January 1st, 2024) Adjusted Close price data for Bajaj Auto Limited (BAJAJ-AUTO.NS) and Hero MotoCorp Limited (HEROMOTOCO.NS).

We have included the data file in the zip file along with the code for you to run on your system later. The link to download the files can be found at the end of the blog.

Output:

Bajaj         Hero     Ratio
Date                                          
2019-01-01  2726.649902  3127.600098  0.871803
2019-01-02  2692.000000  3046.550049  0.883622
2019-01-03  2701.350098  3014.649902  0.896074
2019-01-04  2734.199951  2987.850098  0.915106
2019-01-07  2658.550049  2957.949951  0.898781
...                 ...          ...       ...
2023-12-22  6372.100098  3935.699951  1.619051
2023-12-26  6464.549805  4067.449951  1.589337
2023-12-27  6709.649902  4064.300049  1.650875
2023-12-28  6703.299805  4173.250000  1.606254
2023-12-29  6797.250000  4139.549805  1.642026

Step 3: Apply the Kalman filter

Hyperparameters of the Kalman Filter can be changed for instance:

Multi dimensional transition matrices, use more past information for making predictions at each point

Different values of observation and transition covariance

Output:

Step 4: Apply Pairs trading strategy

In thepairs tradingstrategy, we buy one stock and sell the other stockchoosing the quantityas the hedge ratio.

Output:

Total returns: -0.03794040475865804

You can optimise the strategy parameters to get different results.

It is important to note that backtesting results do not guarantee future performance. The presented strategy results are intended solely for educational purposes and should not be interpreted as investment advice. A comprehensive evaluation of the strategy across multiple parameters is necessary to assess its effectiveness.

Next, let us find out what future trends and developments are in the pipeline for the trading domain using Kalman filter technology.

Future trends and developments in Kalman filter technology

Here are some potentialfuture trendsand developments in Kalman filter technology:⁽⁴⁾

Enhanced Integration with Machine Learning:Kalman filters are already used alongside machine learning models for tasks like filtering noise and improving prediction accuracy. We might see a tighter integration, where the Kalman filter refines the data used to train machine learning models, leading to more robust and adaptable trading algorithms.

Multi-factor Kalman Filters:Traditional Kalman filters handle a single underlying state variable. The future could see the development of multi-factor filters that can account for multiple variables simultaneously, providing a more comprehensive picture of market dynamics.

Kalman Filters for Alternative Data Sources:As alternative data (e.g., social media sentiment, satellite imagery) becomes more prominent, Kalman filters could be adapted to incorporate and analyse these non-traditional sources alongside price data, potentially revealing new trading signals.

Cloud-Based Kalman Filtering:Cloud computing offers vast processing power. Kalman filter applications could leverage the cloud for real-time data analysis and faster decision-making, especially in high-frequency trading scenarios.

Explainable Kalman Filters:A challenge with Kalman filters is their "black box" nature, where it can be difficult to understand why they generate specific outputs. Future developments might focus on creating more interpretable Kalman filters, allowing traders to better understand the reasoning behind the filter's recommendations.

Overall, Kalman filters are likely to play an increasingly important role in algorithmic trading. By integrating with advanced machine learning techniques, handling more complex data sources, and becoming more interpretable, Kalman filters could provide traders with a powerful tool to navigate the ever-evolving financial markets.

Conclusion

By mastering statistical concepts and Kalman filter equations, we gained insight into how it optimally combines measurements and predictions to estimate a system's state with precision.

Exploring real-world examples showcased its versatility in pairs trading, volatility estimation, market impact modelling, portfolio optimisation, and algorithmic trading strategies. We delved into practical implementation steps in Python, emphasising efficiency and accuracy through optimised code and performance strategies.

Comparisons with other filtering techniques highlighted its strengths in Gaussian noise environments while envisioning future trends focused on integration with machine learning, multi-factor modelling, alternative data sources, cloud-based processing, and explainability.

With these insights, traders are empowered to leverage the Kalman filter effectively, navigating the complexities of financial markets with confidence and adaptability. As we embrace the future of algorithmic trading, the Kalman filter remains a cornerstone, evolving alongside technological advancements to meet the challenges of tomorrow's trading landscape.

You can learn more about theKalman filter and the statistical conceptssuch as co-integration, ADF test to identify trading opportunities in order to create trading models using spreadsheets and Python. Happy trading!

Files in the download

Kalman filter in trading (example)

Pairs trading using Kalman filter - Python notebook

Login to Download

Note: The original post has been revamped on 7thMay 2024 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
