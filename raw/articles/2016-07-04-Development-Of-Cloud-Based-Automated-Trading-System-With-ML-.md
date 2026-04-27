---
title: "Development Of Cloud-Based Automated Trading System With ML [EPAT PROJECT]"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/epat-project-automated-trading-maxime-fages-derek-wong/"
date: "2016-07-04"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Development Of Cloud-Based Automated Trading System With ML [EPAT PROJECT]

**来源**: [QuantInsti](https://blog.quantinsti.com/epat-project-automated-trading-maxime-fages-derek-wong/)  
**日期**: 2016-07-04  
**作者**: QuantInsti

---

## 原文

Development Of Cloud-Based Automated Trading System With Machine Learning [EPAT PROJECT]

This article is the final project submitted by the authors as a part of their coursework in Executive Programme in Algorithmic Trading (EPAT) at QuantInsti.

Authors

Maxime FagesMaxime’s career spanned across the strategic aspects of value and risk, with a particular focus on trading behaviors andmarket microstructureover the past few years. He embraced a quantitative angle in M&A, fund management or currently corporate strategy and has always been an avid open-source software user. Maxime holds an MBA from Insead and an MSc, Engineering from Ecole Nationale Superieure D’Arts et Metiers; he is currently the Sr. Director for Ripple.

Derek began his career on the floor of the CBOT then moved upstairs to focus on proprietary trading and strategy development. He manages global multi-strategy portfolios, focusing in the futures and options space. He is currently the Deputy Director of Systematic Trading at Foretrade Investment Co Ltd.

Ideation

By the end of theExecutive Programme in Algorithmic Trading (EPAT)lectures, Derek and I were spending a significant amount of time exchanging views over a variety of media. We discussed ideas for a project, and the same themes were getting us excited. First, we were interested in dealing with Futures rather than cash instruments. Second, we both had a solid experience using R for quantitative research and were interested in getting our hands dirty on the execution side of things, especially on the implementation ofevent driven trading strategiesin Python (which neither of us knew before the EPAT program). Third, we had spent hours discussing and assessing the performance ofmachine learning for tradingapplications and were pretty eager to try our ideas out. Finally, we were very interested in practical architecture design, particularly in what was the best way to manage the variable resource needs of any Machine Learning framework (training vs. evaluating).

The scope of our project, therefore, came about naturally:developing a fully cloud-basedautomated trading systemthat would leverage on simple, fast mean-reverting or trend-following execution algorithms and call on Machine learning technology to switch between these.

Project description

The machine learning class of theEPATprogramme featured the use of aSupport Vector Machineand evidenced how it did slightly perform better than aGARCH modelat predicting volatility. Literature suggested that RecurrentNeural Networksmodels could perform even better under the right circumstances [1], and that combining models (“thick modeling”) might mitigate over-fitting concerns [2]. That indeed was an appealing prospect, but our dabbling in using ML frameworks (mostly e1071, caret and nnet for R, and the excellent scikit-learn or the easier pybrain in Python) had shed light on a key issue: resource management. The learning phase of most models can be painfully long on a mid-range desktop computer, and the sheer size of most datasets will soak up a considerable amount of RAM. A relatively high-end PC, for example, would probably do reasonably well using GPU-optimization. However, that would bring further challenges beyond the cost: administering such a system is an art in itself, and one we had no experience in. Besides, most libraries mentioned above can be tricky to setup properly; this is particularly problematic for machine learning research, as neuron coefficients, for example, don’t have salient values that can easily be sanity-checked. A model that performs poorly has enough potential root causes not to add a layer of amateur administration, especially at our scale.

Structure

Figure 1: Technology Stack

Our architecture is relatively simple and was designed to live in remote servers. After the initiation sequence when historical market data is pulled, a timekeeper process triggers an update of mean and standard deviation [3] along with an incremental minute-data bar update. Every 5 minutes, it will trigger a call of the machine learning stack to get an assessment of the next 5 minutes. Data streamed from the broker is queued and processed by the handler to update all key trading parameters. A very simple strategy continuously assesses the signals: if the machine learning stack indicated a trending regime, it will watch for a Z-Score threshold as a starting trend, otherwise it will go for a mean-reversion trade. Signals are queued where the order execution will fetch them and “naively” process orders. Practically, the execution executes a limit order at the bid (long) or ask (short) and wait for an ack (ack messages are pushed in a third queue when caught from the broker’s API). If an ack isn’t detected within a time out parameter, the order is considered stale and either cancelled if it is an initial position order or changed to a market order if it is a profit taking or stop order. Fills inferred from acks are added to the plot.ly monitor (third-party charting of stream).

Figure 2: Realtime plotly monitor, with trade execution and indicators

We will not release the full details of themachine learningmodel, but the general principle is that we have two “hemispheres” trained separately to predict ranging or trending conditions. Each hemisphere features three different models with specific parameters, and each side polls its models to decide on upcoming conditions. In the event both sides disagree (e.g. “range” and “trend” conditions detected), the stack assesses the confidence parameters of models to decide.

Figure 3: Overview of the Machine Learning stack

Figure 4: Distribution of out-of-sample results

One of the very nice features about the Azure Machine Learning Studio is that it enables the development of custom functions. In our case, we developed a simple polling methodology to poll both “hemispheres” and, should inconsistencies occur, go with the side whose confidence was collectively highest.

# Map 1-based optional input ports to variables
dataset1 <- maml.mapInputPort(1) # class: data.frame
#simple polling 
dataset1$trend_poll <- ifelse((dataset1$trend_NN == "trend") +(dataset1$trend_TCdeep == "trend") + (dataset1$trend_boostDT == "trend") >
                                (dataset1$trend_NN == "notrend") +(dataset1$trend_TCdeep == "notrend") + (dataset1$trend_boostDT == "notrend"), "trend", "notrend")#poll trend confindence (as in "sum of confidence if youwere right")
dataset1$trend_poll_conf <- (dataset1$trend_NN == dataset1$trend_poll)*dataset1$trend_NNprob+
  (dataset1$trend_TCdeep == dataset1$trend_poll)*dataset1$trend_TCdeepprob+
  (dataset1$trend_boostDT == dataset1$trend_poll)*dataset1$trend_boostDTprob
#simple polling as the threshold is not really helping
dataset1$range_poll <- ifelse((dataset1$range_NN == "range") +(dataset1$range_TCdeep == "range") + (dataset1$range_boostDT == "range") >
                                (dataset1$range_NN == "norange") +(dataset1$range_TCdeep == "norange") + (dataset1$range_boostDT == "norange"), "range", "norange")
#poll trend confindence (as in "sum of confidence if youwere right")
dataset1$range_poll_conf <- (dataset1$range_NN == dataset1$range_poll)*dataset1$range_NNprob+
  (dataset1$range_TCdeep == dataset1$range_poll)*dataset1$range_TCdeepprob+
  (dataset1$range_boostDT == dataset1$range_poll)*dataset1$range_boostDTprob

dataset1$final <- ifelse(dataset1$trend_poll == "trend" & dataset1$range_poll == "norange", "trend",
                         ifelse(dataset1$trend_poll == "notrend" & dataset1$range_poll == "range", "range",
                                ifelse(dataset1$trend_poll == "trend" & dataset1$range_poll == "range",
                                       ifelse(dataset1$trend_poll_conf>dataset1$range_poll_conf,"trend","range"),"nothing")))

data.set <- as.data.frame(dataset1$final)
# Select data.frame to be sent to the output Dataset port
maml.mapOutputPort("data.set")

R Snippet 1: simple polling device, connected to the Azure Stack network

In some rare instances, neither side conclude to a signal, in which case we do nothing for 5 mn. The choice of this 5 mn was not entirely arbitrary, but rather an educated compromise between our view on a “stable” (even temporarily) trading environment and the actual definitive periods of WTI [4] ( thewavelet packagewas pretty useful).

Figure 5: Wavelet (spectral) view of WTI prices

The out-of-sample performance was an impressive 74%, with the very important caveat that our sample was limited to 6 months 1-min bars. The R code to wrangle data is part of the github repository, and essentially converts a series on “standard” indicators (SMA, LMA,RSI, ATR, etc.) for the previous 5 mn into a single 50 data points (input) + 1 output. Training on the Azure framework is fast, and the brilliant interface makes it easy to add in custom code in python or R. Going from training to a live RESTful API is blissfully simple, and the response time clearly under 100ms.

#eyeball using quantmod
eyeb<-function(x){
i=x
start <- index(df)[1]+i*60*5
mid <-start+5*60
end <- start+10*60
tmp <- df[index(df) >=start & index(df) < mid]
tmp2 <- df[index(df) >=mid & index(df) < end]
tmp3 <- df[index(df) >=start & index(df) < end]

mychartTheme <- chart_theme()
mychartTheme$rylab = T 
chart_Series(tmp3[,c("open","high","low","close")], theme=mychartTheme)

slp_av <- mean(tail(tmp2$trend,3))
ln_slp <- function(x){xts(coredata(first(x)+slp_av*as.numeric((index(x)-first(index(x))))),order.by=index(x))}
dummy <- (tmp2$high+tmp2$low)/2
add_TA(ln_slp(dummy),on=1, col=3)
ta_up <- xts(rep(mean(tmp$close)+z_thresh*last(tmp$atr),length(index(tmp2))),order.by = index(tmp2))
add_TA(ta_up, on=1, col=4)
ta_dn <- xts(rep(mean(tmp$close)-z_thresh*last(tmp$atr),length(index(tmp2))),order.by = index(tmp2))
add_TA(ta_dn, on=1, col=4)

}

R Snippet 2: Eyeball function to generate Figures 6 & 7

Trading Strategy Development

We determined three guiding principles that we maintained during our strategy development. Primarily, we needed a strategy that would significantly rely on and leverage the machine learning architecture. Secondarily, we needed the strategy to perform in such a way that the empirical analysis of performance from different regime states would allow us to judge the trading strategy itself but also see if the machine learning was performing well in real time. Finally, of course, with all trading strategies, we wanted it to be profitable.

The innate complexities of our machine learning architecture lead us to stay relatively simplistic in our trading strategy. This was essential for several reasons, simplified trading logic allowed us to avoid classic strategy development pitfalls. For instance: over fitting, limiting degrees of freedom, confounding logic errors, and data contamination. When running several different types of training and back tests, first for the machine learning architecture, then developing the trading logic itself posed twice as many opportunities to fall into the classic strategy development traps.

The trading system is based on frequentist statistical inference for our calculations. We decided to use a simple statistical measure, Z-score as the foundation of our strategy. This is an extremely simple standard statistical formula. The reason for this is because we did not want additional complexity to arise from the combination of the ML structure plus our trading logic model.

zscore = (self.last_trade - self.cur_mean)/self.cur_sd

Python Snippet 1: z-score formula snippet

Entry Trigger Process

Our entry’s condition was simply based on two factors, primarily the machine learning market regime state and a Z score generated trigger condition.

Table 1: Entry condition logic matrix

if abs(zscore) >= self.zscore_thresh and \
                abs(zscore) <= settings.Z_THRESH + settings.Z_THRESH_UP and \
                self.trading.is_set() and \
        (self.fill_dict == [] or self.fill_dict[-1]["type"] != "main") and \
                self.flag != "nothing":
    self.exec_logger.info("signal for main detected - strategy")
    try:

        if zscore >= self.zscore_thresh:
            if self.flag == "trend":
                action = "BUY"

            if self.flag == "range":
                action = "SELL"

        if zscore <= -self.zscore_thresh:
            if self.flag == "trend":
                action = "SELL"

            if self.flag == "range":
                action = "BUY"

Python Snippet 2:  Trading logic trigger condition

Our reasoning for using simple symmetrical trigger logic is as follows. By maintaining the absolute simplest method for triggering, we can maximize our reliance on the machine learning. If the market regime is incorrect due to the simplistic nature of the trigger, the amount of independent alpha generated should be close to 0 or negative if you include market frictions. This is making the assumption that markets for short periods of high-frequency data are a Geometric Brownian Motion (GBM) Processes e.g. random walk.

If the machine learning can detect when that is not the case and there is some distribution where the tails are divergent from a log-normal distribution then we can generate alpha. For example, we have three regime states: trend, range, and nothing. If GBM holds true, the time series should be either in nothing or range. This is made clear by Figure 4, however, we do show a statistically significant portion of the time is spent in the trending area. Which would show that time series has variance in the kurtosis, and stochastic volatility. This leads to areas where we can generate alpha from trending strategies due to excess kurtosis. However, a standard Z-score is incapable of being able to discern these different time series regimes, and it makes the assumption of a normal distribution. Hence, the trading trigger can become profitable if and only if the machine learning architecture can accurately discern the market regime state.

This strategy also includes the same type of assumptions that are present in our machine learning two hemispheres, that in different regimes we should have two types of market price distributions. One would be more leptokurtic and lead to fatter tails, marking a trend regime. The other would be a more normal or even platykurtic with comparably thinner tails, leading to a range regime.

The Z-score would assume a normal distribution which means all of the targetable activity that we are looking to take advantage is in the tails. Therefore by using a Z-score trigger we can simply do that and only have trigger points at what we judged to be extreme values, looking to take advantage of different tail conditions. Our parameter trigger point was any Z-Score between 2 and 2.5 (ZTHRESH  and ZTHRESH + ZTHRESHUP)

Our exits are extremely simple as well, given our primary goals. We use two types of exit conditions. For “range” regimemean revertingtrades a Z-score higher than our Z_TARGET for longs or lower for shorts was used. We expect mean reverting activity which would be a Z-score of 0 but we have it a slightly larger range to close a position of +/-0.2 in our parameters.  We also have an additional 4 tick trailing stop, this was used for both systems. However for the trending trade was the only exit condition.

Parameters

Our parameter set was taken directly from the normal distribution assumption.  These are controlled by a separate config file in our architecture, which makes for easy modification. We used a Z-score threshold (ZTHRESH) of 2 and limited to a 2.5 (ZTHRESH + ZTHRESHUP). This is so we do not try to enter trades that have already diverged extremely far away. The STOPOFFSET are in ticks for a trailing stop, and ZTARGET is Z-score of 0.2 where we close mean reverting positions around the mean.

# trading parameters
Z_THRESH = 2
Z_THRESH_UP = 0.5
STOP_OFFSET = 0.04
Z_TARGET = 0.2

Python Snippet 3:  Trading logic parameters

How did the project go?

The parameters we have been using lead to a 14x-16x turn per hours (7-8 round turns). It is significant, especially if looking at the number from a nominal perspective: that is roughly 16.5MUSD nominal traded every day, on around 5KUSD of margin (the latter, however, is the only interesting parameter from on ROE perspective)

The strategy performed fairly well: 45% wins at around 1.8 ticks per contract, 29% losses at around 1.7 ticks per contract, and 26% scratch. However, the average profit, at ca. 0.32 tick per round-trip trade has to be put in perspective with the 1.42USD that IB would charge us for each trade [5]; the economics for retail traders are tough. Net, 3.2USD profit for 2.84USD brokerage and exchange fees would yield a theoretic 20%-30% monthly return on the margin posted. This might look impressive, but given the leverage involved doesn’t nearly compensate for the potential loss that could arise from unforeseen, odd market conditions (spike linked to announcements, liquidity drops) and even less so for operational risks (bug or system breakage). Besides, it is not clear we could have scaled the strategy enough to make returns worth some “true” investments without significant slippage.

On the other hand, resource costs were ridiculously low: the AWS micro instance is free for a year, and given the heavy lifting (ML) is done at azure that was enough processing power for us, and the Azure stack comes out at under 10USD/m (“seat” and then 50ct for a 1,000 API calls)

Conclusion

With regards to trading, our three main conclusions are:

Software as a service for machine learning makes absolute sense whenever possible. Response time at 50ms-100ms is a clear limit, but the incremental investment and operational risk to go under that mark is very significant. For any longer horizon application, the technology, and Microsoft’s Azure ML Studio in particular is worth exploring.

It is still possible to make money on automated trading with limited resources, even on outrights. However, exchanges/brokerage fees can quickly erode or even cancel profits. Incentive/Tiered program are of paramount importance for such strategies to be profitable. And yes, this is stating the obvious, but we now have a first-hand experience.

Between the obvious research and coding part, engineering abstract concepts into actionable objects and code is probably more art than science. There is a clear premium to having actual experience (and failures) under one’s belt in that area.

Recommendations to future students/coders:

Explore libraries, and get a thorough understanding of what they can/will do. IBPY, for example, has the merit of simply existing. Documentation is almost inexistent, but it does have a very large number of wrappers calling all API functionalities. Chances are we ended up re-writing some functionalities that existed (and when we did, our implementation is very likely to be worst)

“A game of chess is like a swordfight, you must think first before you move” – Wu-Tang Clan. This ancient wisdom definitely also applies to development, especially for when classes and concurrency are involved. Since we had no experience of such development or designing software architecture, we started by hacking throughJames Ma “High Frequency” project. It’s safe to say almost nothing remains from James’ excellent work in our project; working around limitations induced by the scope differences always eventually ended in blocks, and refactoring. In the end, we would havesaved a lot of time thinking longer about conceptual blocks and then working toward them from the ground up(with the caveat that at the time we had no idea how to do that, and Jame’s work was a good bootstrap). Ironically, our eventual architecture looks very much like the one in Quantinsti’sSystem Architecture 101.

Most of our R/Python at work involves sequential workflow, developed iteratively. Trading systems involve data being streamed from the exchanges, orders being pushed based on signals, acknowledgements or orders, etc. In hindsight, this, of course screams “threads” and “concurrency”, but James had (very well) managed to keep his work sequential and relying on classes alone. This did not work for us, and compounded with the aforementioned issue led to the first refactoring (unsuccessfully, since we had bet on the wrong library for the job:threading). We would very much encourage anyone looking into python for trading todig intoasyncioif one’s using python 3.5 orconcurrent.Futureswhich is backported for 2.7 as well(we used the later). Now, multiprocessing has its own frustrating challenges: thread dying in silence, (not) thread-safe objects, etc. and is generally a very different design paradigm. On the plus side, it is incredibly gratifying when it does work

Quality Assurance is probably the least sexy aspect of development. It is also the one we have, and will, invest a lot of learning/reading time in.  This is not a skill that is as critical in a notebook-type environment because debugging can be performed on the go for the most part, one step at a time. Of course, when multiple threads interact with data from various sources, this is a very different situation. Writing print statements everywhere won’t cut it, and bothloggingandtracebackare libraries very much worth investing time in.To be fair, none are particularly intuitive (nor is theExceptionclass use, by the way) but systematic try/except and logging points truly is a lifesaver

The old “feel the pain now or feel the pain later” moniker is particularly apt when it comes to development. Using class and other less-than-intuitive taxonomy of object and process is a double-edged sword. Most classes and functions will not be straight forward to test, and attempting to test basic functionalities (proper typing of output, e.g.) in an integrated test is a recipe for disaster. We ended up using the very nice__main__python semantic to “scaffold” individual classes with basics required to run, as a poor man’sunitest(another un-sexy library that is really critical). In the end, the time required to develop testing features is not insignificant (we assume it could have been around 20%) but it is a very good use of resource. A good example is that we did not build a market simulator. That was a decision we had made based on the limited interest we had actually trading much with IB (due in large part to contractual restrictions) and, quite frankly, on the skills we had at the beginning. This was a really bad decision from a time perspective alone: the boot sequence to register on IB is roughly 20 seconds long. Accounting for a signal to happen, this is probably 30 seconds minimum which in a 4-hours development sequence might require 20 to 30 reboots. Conservatively, 10-20 minutes of wasted time or 5%-10% or productivity loss. That is before even being able to test specific situations rather than waiting for one to happen, and there is no doubt in our mind that even biting the bullet mid-way would still have been largely beneficial (including for parameters adjustment).

Broadly speaking, this was the key takeaway: getting a project 80% done is the easy and fun part. The hard and tedious one is the last 20%, and that is also where actual skills matter (especially in quality assurance).

We gained a lot in the process and would like to thank the faculty for their help and guidance. We do not plan to maintain the public release of the program given our respective contractual limitations but plan on working together again in the near-term.

Github Repository:https://github.com/FaGuoMa/Azure-IB/.

References

[1] Non-Linear Time Series Models in Empirical Finance - Philip Hans Franses, Dick van Dijk; Direction-of-Change Forecasting Using a Volatility Based Recurrent Neural Network – Stelio Bekiros and Dimitris Georgoutsos

[2] Is Combining Classifiers Better than Selecting the Best One – Saso Dzeroski and Bernard Zenko; Popular Ensemble Methods: An Empirical Study – D Opitz and R. Maclin

[3] For the standard deviation we have used the unbiased estimator  (R Almgren – Time Series Analysis and Statistical arbitrage, NUY)

[4] Wavelet Multiresolution Analysis of Financial Time Series – M. Ranta

[5] The retail commissions would be 0.85USD brokerage plus 1.45USD for NYMEX exchange fees. However, under the Tiered volume program of both NYMEX/CME and IB, the rates would likely be 0.65USD and 0.77USD per trade, respectively

Next Steps

For more such student projects, checkStatistical Arbitrage Strategy using R.If you are a coder or a tech professional looking to start your own automated trading desk. Learn automated trading from live Interactive lectures by daily-practitioners.Executive Programme in Algorithmic Tradingcovers training modules like Statistics & Econometrics, Financial Computing & Technology, and Algorithmic & Quantitative Trading.Enroll now!

---

*Imported from QuantInsti Blog on 2026-04-27*
