---
title: "Statistical Thinking and Data Analysis: Introduction to Smarter Decision-Making"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/statistical-thinking/"
date: "2025-04-10"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Statistical Thinking and Data Analysis: Introduction to Smarter Decision-Making

**来源**: [QuantInsti](https://blog.quantinsti.com/statistical-thinking/)  
**日期**: 2025-04-10  
**作者**: QuantInsti

---

## 原文

Introduction to Statistical Thinking for Smarter Choices and Analysis

Statistical thinking is an approach to process information through the lens of probability and statistics so as to make informed decisions.

This series of blogs takes you through a journey where we begin with introducing statistical thinking, make a brief stopover to understand Bayesian statistics and then dwell on its applications in financial markets using Python.

“Statistical thinking will one day be as necessary for efficient citizenship as the ability to read and write!”H.G. Wells (1866-1946), the father of science fiction

Making choices is a part of our daily lives, be it personal or professional. If you apply statistical thinking wherever possible, you can make better choices.

In this article, we’ll go step by step in deconstructing the decision-making process under limited information. We’ll look at some examples, the jargon and the importance of statistics in the process.

What is statistics?

What is a statistical question?

Why do we need statistics?

Descriptive statistics vs Inferential statistics

Should we use descriptive statistics or inferential statistics?

Jargon in statistics

Population

Sample

Observation

Statistic

Parameter

Hypothesis

Hypothesis testing

Estimate

Why should we spend time on statistical inference?

What is statistics?

There are two ways to define statistics. Formally statistics is defined as "The science of statistics deals with the collection, analysis, interpretation, and presentation of data."

Intuitively, statistics is defined as "Statistics is the science of making decisions under uncertainty."

That is, statistics is a tool that helps you make decisions when you don’t have complete information.

What is a statistical question?

Looking at the above image, let's address some questions!

How many cats does the above picture have?4, right?

Do we have all the information to answer this question?Yes.

Do all healthy cats have four legs?Yes.

Do we have all the information to answer this question?No. Because this is a picture of only 4 out of all the existing cats in the world!

But can we still answer it with certainty?Yes.

So, is it a statistical question?No.

Why?Because if you have all the information to answer the question or if you can answer this question with certainty, it’s not a statistical question.

For a question to be a statistical question,

The question has to go beyond the available information, and

The question shouldn’t be answerable with certainty.

This concept will be reinforced repeatedly in this article, i.e., statistics is the science of decision making underuncertainty.

Why do we need statistics?

We now work with a toy example through this post to answer the above question.

Suppose we decide to design aQuantracourse on Julia programming.

How do we decide if we should put time and effort into building this course?

What if our designed course fails and doesn’t get many interested users?

These are important business decisions that require substantial resources. Therefore, we decide to survey if such a course would sell.

Now, that raises the following questions:

Who would our potential paid users be?

Who should we approach? Programmers? Data scientists? Researchers? College graduates? Quantitative Analysts?

Ideally, all of them, right?

However,

Can we get access to all of these people?Unlikely.

So, what should we do?

Should we drop the idea of designing the new course?

That doesn’t sound right.

If we had access to all the people, the process would have been simple. If the majority say that they would buy such a course, you create it. If not, then drop it.

However, since we can’t do it, we do the next best thing, i.e. we ask the maximum number of people we can reach out to, and, based on their response, weestimatethe likelihood of this course being successful.

To calculate thisestimate,we needstatistics.

To generalize this idea, in real-world scenarios, we rarely have complete information related to the decision we want to make, whether for individuals or businesses.

Hence, we need a tool that can help us decide with limited information. Statistics is one such tool, and making these decisions within a statistical framework is called statistical thinking.

Statistical thinkingis not just about using formulas to calculate p-values and z-scores; it’s a way to think about the world. Once you internalize this idea, it will change how you see the world. You’ll start thinking in terms of probabilities instead of certainties, which will help you make better decisions in your professional and personal life.

Descriptive statistics vs Inferential statistics

Descriptive statisticsis the process of taking the data and describing its features using measures of central tendency (mean, median and mode), measures of dispersion (standard deviations, interquartile range ), etc.

However, inferential statistics is about working with the limited data and using it to infer something about a larger question we pose to ourselves a priori. This question cannot be answered with certainty.

Our article focuses on the latter, i.e. inferential statistics.

Should we use descriptive or inferential statistics?

It depends on the question you’re asking and the available data. A simple question to ask yourself while deciding which one to use is:

Do we want to describe the existing data? OR

Do we want to draw inferences from the existing data (sample) to extrapolate about the population?

We go with descriptive statistics for the former and inferential statistics for the latter.

Jargon in statistics

Let’s look at some of the key terms used in statistics that will help you in understanding the concepts better.

Population

The universe of items we’re interested in. Going back to our Quantra course example, the population would be every person in this world who would be interested in the Julia course.

Sample

It is a subset of the population, i.e. the amount of information wecanget. This could be the Quantra or EPAT user base we have. We could frame our question as:How likely are you to buy a course on Julia (on a scale of 1 to 10)?

Statistic

A summary measure of the data available, i.e. from the sample. Here, it could be the average score of say, 7 obtained from Quantra and EPAT users for the above question.

Parameter

Aparameteris a summary measure of the population. Here, it could be the average score of say, 6 obtained from the population (as defined above).

Astatisticis a summary measure of the existing data (sample), whereas aparameteris the same for the population.

Hypothesis

A description of how we think the world works. We hypothesize that EPAT and Quantra users are unlikely to buy a course on Julia (rating of 1). This is the assumption we start with that we call the null hypothesis.

Null Hypothesis

It’s crucial to have a null hypothesis before starting with any statistical analysis. And the null hypothesis is mostly status quo. The alternative hypothesis is the theory that you think could be true and are looking for evidence to verify it.

So to clarify, our null hypothesis \({H_0}\) and alternative hypothesis \({H_1}\) here are \({H_0}\): EPAT and Quantra users are unlikely to buy a course on Julia (Mean rating = 5)

\({H_1}\): EPAT and Quantra users are likely to buy the course (Mean rating >=5)

Hypothesis testing

Hypothesis testingis a method to draw conclusion about the data from the sample i.e. to test whether a hypothesis is correct or not.

Estimate

And estimate can be defined as a variable that is the best guess of the actual value of the parameter.

Why should we spend time on statistical inference?

Let’s consider two scenarios:

Scenario 1- We had access to only one user, and she rated 6 for the likelihood of buying the course.

Scenario 2- We had access to 10 users, and they gave an average rating of 8 for buying the course.

These are our best estimates. However,

Which one is the better estimate?The one with 10 users because it has more data.

Is the estimate of scenario 2 good enough to act on?Should we create the course because 10 people have a high likelihood of buying the course?Maybe not.

Why?Because the response from 10 users is probably not enough, and so could lead to a poorly worked out decision.

This is where statistical inference comes in.

As we have mentioned before, If you want the correct answer, youwillneedallthe data. No silver bullet can give you the right answer with limited data. But remember, as we discussed, statistics is the science of making decisions underuncertainty.

We’re not interested in knowing thecorrectanswer with statistical inference because we can’t!

Using inferential statistics, the question you want to answer is:

Is the best guess good enough to change our minds?

This forms the basis of everything we do in statistical inference. Notice that the question mentions “changing our mind”. This means that we would need to already have something in our minds in the first place, a decision, an opinion.

We can only change our minds if we have already decided to do something by default. Remember we mentioned the importance of having a null hypothesis?

The hypothesis could be that people are extremely unlikely to buy the Quantra course on Julia programming, so we willnot createa new course if the best guess isnot good enough to change our minds.

This is where the need to have a predefined hypothesis comes in. This is another fundamental concept in inferential statistics. Suppose we are to make statistical inferences.

In that case, weneedto have a predefined decision or an opinion because, at the cost of being repetitive,  the question we’re asking using statistics is:

Is the best guess good enough to change our minds?

The entire exercise of statistical inference makes sense if you have a default action. If you don’t have a default action, just go with your best guess from the sample data.

Let’s take another example to understand this. Imagine if PepsiCo decides to change the colour of its logo to black or green. The responses of 1 million people are recorded as a sample.

Now, here’s the summary of which decision we can take based on our default action and data:

Default action

Results from data

Decision

Not decided

Data favours green.

Go with the best guess. Green.

Don’t change

Data marginally favours black

Logo remains unchanged

Don’t change

Data overwhelmingly favours green

Change the logo to green.

The table above consists of 3 scenarios to explain to concepts presented above.

In the first scenario, there’s no default action and the data supports green. So we go ahead and change the logo to green.

In the second scenario, the default action is “don’t change the color” and the data supports black but not strongly enough. So the logo color remains unchanged.

In the third scenario, the default action is “don’t change the color” but the data strongly supports green. So the logo is changed to green.

Resources for learning about statistical thinking

Here are a few resources that you can refer to for a detailed understanding of the topic:

Think Bayes

The Cartoon Guide to Statistics

Bayesian Analysis with Python

Conclusion

We hope this write-up has piqued your interest in applying a statistical approach when  confronted with choices. Do share your thoughts and comments about the blog in the below section. Until next time!

If you're serious about building a data-driven edge in trading, understanding statistics is non-negotiable — and the Module 2:Statistics for Financial Markets Coursefrom EPAT delivers exactly that. This module focuses on applying probability, risk metrics, hypothesis testing, and trading strategy development directly to financial markets using real-world tools like Excel.

To explore the full curriculum and gain skills across machine learning, financial computing, quant trading strategies, and more, check out the completeExecutive Programme in Algorithmic Trading (EPAT). Whether you're just starting out or looking to level up, EPAT gives you the structure, depth, and practical expertise to succeed in today’s markets.

Authors:Vivek KrishnamoorthyandAnshul Tayal

Disclaimer: All data and information provided in this article are for informational purposes only. QuantInsti®makes no representations as to accuracy, completeness, currentness, suitability, or validity of any information in this article and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. All information is provided on an as-is basis.

---

*Imported from QuantInsti Blog on 2026-04-27*
