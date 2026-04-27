---
title: "Collaborating in an Open Source Trading project"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/collaborating-open-source-trading-project/"
date: "2021-03-22"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Collaborating in an Open Source Trading project

**来源**: [QuantInsti](https://blog.quantinsti.com/collaborating-open-source-trading-project/)  
**日期**: 2021-03-22  
**作者**: QuantInsti

---

## 原文

Collaborating in an Open Source Trading Project

ByMario Pisa

A must-have tool for any individual programmer or development team is version control software. In this post, we introduce you toGit/Githubto modify an open source project such as thePyfoliolibrary.

Topics covered:

An introduction to Pyfolio

An introduction to Git and GitHub

Getting the pyfolio source code

Improving the pyfolio library

Publishing the new functionality

One of the basic principles of software engineering is not to reinvent the wheel. Well developed pieces of software can be used over and over again in multiple projects.

Pythonand its ecosystem ofopen source librariesallow us to build software using the work of countless development teams and individual programmers.

Every Python project uses libraries in one way or another. These are nothing more than pieces of software that package classes and functions with specific functionalities such as:

Matplotlib, etc.

These libraries are generic and flexible enough to adapt to any software we are building and save us a lot of time by not having to implement from scratch the functionality that these libraries offer.

In our trading environment, a recurring need for all projects is a performance analysis of our strategies. It would not make sense to code our statistics over and over again, so having a performance analysis library is a necessity.

We can either build our own library that calculates:

Returns

Standard deviation

Sharpe ratio

Sortino ratio

Performance graphs

and a myriad of performance parameters. Or we can use an existing library and improve it if possible, with our own performance indicators.

In this post, we are going to modify an open-source and free software library `pyfolio` to adapt it to our needs and maybe our changes will be useful for the community. We will release our modification so that other developers can benefit from it. In the process,  we will also learn how to use the Git/GitHub tools to control changes and software versions.

`Pyfolio` is distributed under Apache 2.0 license, which allows us to modify the code, distribute it and even commercialize it. However, it is worth reading the license agreement, at least one time in your life.

Here we will not go into the many licenses under which open and/or free source is distributed nor into the philosophy.

An introduction to Pyfolio

Pyfolio is a performance and risk analysis python library for financial portfolios developed by Quantopian Inc.

Note: This company hasstopped its operationsalthough their libraries are still alive on the Internet.

Pyfolio is a comprehensive library that generates performance reports that cover the basic needs of any analyst quite well.

Outstanding features of Pyfolio:

Simple tear sheet:

Summary performance statistics table:

Annual return

Cumulative returns

Annual volatility

Sharpe ratio

Maximum drawdown

Kurtosis

And many more key performance indicators.

Plots:

Cumulative returns

Rolling beta

Rolling Sharpe

Underwater

And more

Returns tear sheet

Summary performance statistics table

Plots:

Rolling returns

Rolling beta

Rolling Sharpe

Rolling Fama-French risk factors

Drawdowns

Underwater plot

Monthly and annual return plots

Daily similarity plots and

Return quantile box plot

Full tear sheet

Summary performance statistics table

Returns tear sheet

Transactions tear sheet

Round trip tear sheet

Interesting times tear sheet

Capacity tear sheet

Performance attribute tear sheet

All these features make the Pyfolio library something to consider. The library is flexible enough to effectively cover a performance analysis of a strategy or portfolio.

An introduction to Git and GitHub

Gitis a distributed version and changes control software developed by Linus Torvalds and currently owned by Microsoft. It is a tool that allows controlling changes and versions in the software over time, with ease to recover the code in any of its previous states.

It allows distributed development, where different teams of programmers can make changes and generate their own versions or contribute their work to the main version.

Basically, Git is a code repository associated with each individual project that we update through commits.

Outstanding features of Git:

Branches are used to work on and modify the code without affecting the main version. They also allow us to initiate alternative developments, where the branch becomes a new library that, due to the scope of the changes and new functionality, requires a new independent version.

Commit to save the code in a time point, a commit saves the work and adds an identification with a message in order to be able to recover this development state in the future.

Merge to fuse different branches

Rollbacks to revert changes at any point time saved through the commits.

This functionality alone is enough to merit the attention of any individual developer and even more so for development teams working on the same project.

The GitHub tool is nothing more than a Git server in the cloud that allows us to publish our Git repositories on the Internet so that any other developer can use the code or contribute with her own development.

It also has a very interesting tool such as the ticket manager to manage bugs or improvements in the software and other tools to help in collaborative development.

Getting the pyfolio source code

At this point, we have decided to use the pyfolio library as our performance analysis library. That way we avoid spending huge amounts of time developing our own library. However, we wish to modify the library to suit our purposes.

We also assume that you have already configured your machine to develop like a pro, if not,check this post before continuing.

Then the first step is to copy in our development machine all the code of the library. To do this we will clone the library from the public repository on GitHub.

From the folder where you have your projects type the following command:

You will see something like this:

At this point, you will have cloned the pyfolio repository in your machine. The next figure shows a graphical representation.

Let’s move to the pyfolio folder and list the files inside it to check the code files and folders.

In the root folder, you can see the files for the package with the license, readme, whatsnew between some interesting files to read. There is also the setup.py script to install the library in our python environment.

If we type the commandgit log —onelinewe can see all the historical commits performed by all developers involved in the project. More interestingly, we can move at any point for the historical development timeline and check the messages left by developers to get knowledge about the reason for the change.

To check the change details for any commit, you can type thegit show <commit Id>.You can see the author, date, the message or reason for the change and some lines in red and green. The red lines are the old code, and the green lines are the new code.

To install the pyfolio library located in our machine and in order to be able to modify the code without having to install the library over and over again every time we make a change in the code we are going to use thedevelopparameter so that python reads the files of the project under development instead of doing an ordinary installation.

Let's check that we have indeed installed the library on our machine with the command conda list

So, we already have the development library installed on our machine and we can create a project in our favourite IDE or editor.

Improving the pyfolio library

The first thing we are going to do before modifying the code is to create our own branch in Git to avoid modifying the master branch before knowing if our changes will have the expected result.

Let's check the current situation in Git with thegit statuscommand.

The output shows that we are on the branch master and the branch is up to date.

The origin branch is the original pyfolio repository on GitHub, as we can see with thegit remote -vcommand:

Let’s create a branch in order to have a new development path in our Git repository with the git checkout -b mypyfolio command:

We can check it with the git status command:

This tells us that we are working on the branchmypyfolioand that there are no changes yet.

Graphically we can represent it as follows:

Dropping Zipline references

Let’s create a new project in order to use the pyfolio library.

When we import the pyfolio library, we get the following warning message:

pyfolio/pyfolio/pos.py:27: UserWarning: Module "zipline.assets" not found; multipliers will not be applied to position notionals. 'Module "zipline.assets" not found; multipliers will not be applied'

The message indicates to us that the zipline.assets library is not installed in our machine, since it’s a warning, it’s not mandatory to install it.

The zipline.assets library comes with the zipline library and this requires python 3.5 and we are using Python 3.6.

A workaround could be to ignore the warnings as:

warnings.filterwarnings('ignore')

However, that filters any warning message and possibly hides other important messages.

So, let’s modify the source code to drop any reference to zipline. The warning message says that the warning comes from the pyfolio/pyfolio/pos.py file line 27.

Lines 21-22 are trying to import the library zipline.assets, if not possible, then it triggers the warning message we can see when we import the pyfolio library.

Another interesting thing is the variable named ZIPLINE. In python, when a developer capitalizes the variable name, it means that the assigned value will be constant throughout the code runtime.

Hence, let's look for theZIPLINEconstant in all the pyfolio library files to see where it is being used.

In lines 23, 25 we have seen that there is the try-except construct to try to import the zipline.assets library. The constant ZIPLINE is used in line 146 whenever the zipline.assets library is imported includes the multiplier for futures, since the multiplier for stocks is 1.

So for this simple example, we assume that we will not have a multiplier and simply avoid importing the zipline.assets library. To do this, we delete or comment out the entire try-except and initialize the ZIPLINE variable to False.

Now, we can import again the library to check if we are avoiding the warning message. As we no longer see the warning when importing the pyfolio library, the change is perfect, so let's check the changes in Git.

With thegit statuscommand, we can check what has changed in the code.

We can see that we are in the branchmypyfolioand that the modified file ispyfolio/pos.py.It also tells us the recommended commands to add the file to the Git tracker and/or commit the changes we have made.

Before this, let's check what differences exist between the file from the last version registered in Git and the file we have modified. To do this we use the commandgit diff pyfolio/pos.py

We see the lines in red that have been modified with respect to the last version registered in Git and we also see in green the lines that have been added with respect to the last version registered in git. Moreover, these are precisely the changes that we have just made, so we are satisfied with the result.

Let's register our changes in git with the commandgit add pyfolio/pos.py and commit -m <message to record with the commit>

If we type the git status command again, we can see that

Checking the git status again, we can see that out branchmypyfoliois one commit ahead from the branch origin.

Changing the Sharpe ratio function

Currently, the pyfolio library relies heavily on theempyricallibrary, also developed by Quantopian, to calculate many of the performance indicators. We are going to modify the function thatcalculates the Sharpe ratioto use our own code instead of relying on the empyrical library.

To do this, open the pyfolio/timeseries.py file, which is in charge of orchestrating the time series analysis, and look for the Sharpe ratio function.

The block from lines 651 to 665 is in charge of calling the functions that calculate the performance indicators and we can see that the Sharpe ratio is calculated with theempyricallibrary.

Therefore, we are going to modify line 655 to call our function to calculate the Sharpe ratio.

In the timeseries.py file itself, there is a function to calculate the Sharpe ratio in line 262, but as the function's decoration indicates it is deprecated and in fact, it calls the function of theempyricallibrary.

So we are going to modify this function to calculate our Sharpe ratio

We introduce the necessary changes to calculate our Sharpe ratio and save the file.

With these changes, all that remains is to test to see if we are indeed calculating the Sharpe ratio correctly with our function.

Everything seems to work correctly, so let's check the changes in git. We type the commandgit statusto check it out

We can see again that we are working in themypyfoliobranch and that we have modified the pyfolio/timeseries.py file.

We can also review the changes in detail with thegit diff pyfolio/timeseries.pycommand.

Again we can see in red the situation before the change and in green the current situation after the change. This corresponds exactly to the modifications we have made.

Let's register the change in git and merge it with the branch master with the commandsgit add pyfolio/timeseries.pyandgit commit -m <reason for change>.

The changes we have made are in themypyfoliobranch, however, we are going to merge ourmypyfoliobranch with themasterbranch.

The command git merge mvypyfolio master does the merge and gives us a summary of the changes from the previous situation.

If we check the git status again we can see that our master branch is two commits ahead of the origin repository hosted on GitHub.

At this point, we have two alternatives to publish our changes to the world.

Scenario 1:we publish our changes in the original pyfolio repository on GitHub maintained by Quantopian (remember, that this company has discontinued).

git push -u origin master

Launching the above command does not mean that it is automatically published since it is necessary to manually manage the repository to approve and accept the changes if applicable by the administrators.

Scenario 2:we create our own GitHub repository and publish it so that anyone can install the library or even participate in the development.

In the next section, we will look at scenario two.

Publishing the new functionality

At this point, what we want to do is to publish our changes in our own GitHub repository.

We can create a public repository from the GitHub web interface itself:

Then we must configure the new repository of our GitHub with the command:

git remote add forked https://github.com/mariope/mypyfolio.git

Note that forked can be any name. We can also see that we now have two remote GitHub for our pyfolio library. One called origin which is the original Quantopian repository and the forked one which is our own GitHub repository.

Finally, to publish our changes to our GitHub repository we type the commandgit push -u forked master.

With this command, we push our local git repository to our GitHub repository and is public and available to anyone who wants to use, modify or fix it.

Don't forget to modify the README file to include a comment about your changes and alert any potential user.

Conclusion

In this post, we have seen how to modify an open source library like pyfolio to introduce our own modifications and publish them in the cloud.

Along the way, we have learned how version control software works and how to handle basic git/github commands.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
