---
title: "Prophet Library | Installation on Mac"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/installing-prophet-library-mac/"
date: "2021-09-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Prophet Library | Installation on Mac

**来源**: [QuantInsti](https://blog.quantinsti.com/installing-prophet-library-mac/)  
**日期**: 2021-09-09  
**作者**: QuantInsti

---

## 原文

Installing Prophet library on Mac

ByMario Pisa

Prophet is a large library developed by Facebook Inc. that facilitates Natural Language Processing (NLP) tasks. In this post we understand how to install Prophet on Mac machines, because depending on the configuration we have on the machine, we may face some installation problems.

We cover:

Beginning with Prophet

Checking the Python environment before installing Prophet

Installing the Prophet dependencies

Installing the Prophet library

Testing Prophet

Beginning with Prophet

Sometimes we can find ourselves with a Python environment on our machine that may well look like a junk drawer. The versions of Python and the libraries we are already using can give us some headaches when installing Prophet and more specifically its main dependency, which is the Pystan library.

In order to make the installation process of Prophet on Mac less painful, I have created this post based on theofficial documentationwhich I strongly recommend you to read.

Checking the Python environment before installing Prophet

Before installing Prophet let's check if we have the Python environment correctly installed.

Normally, you should haveAnacondaorMinicondainstalled on your machine. If you haven't installed it yet,check this post.

Hence, with anaconda or Miniconda installed, press CMD+<space bar> to search in Mac Spotlight, type Terminal and open Terminal.app. If you are using Conda environments choose your preferred.

Let’s check the python version:

% python --version

If the Python version is 3.6, 3.7, 3.8 or 3.9 it’s ok, if not, you can create a Python environment as in the referencedpost.

I suggest to create a new python environment for this project, hence you can type the below commands:

% cd% conda create -n prophet39 python=3.9
% conda activate prophet39

At this point we have a python 3.9 ready to install new libraries.

If you want to use Jupyter notebooks, you need to install some other libraries:

% conda install ipykernel
% python -m ipykernel install --name prophet39 --user
% conda install jupyter

Installing the Prophet dependencies

As the official documentation says, the major dependency that the Prophet has is pystan. PyStan has its owninstallation instructions. Install pystan with pip before using pip to install prophet.

% pip install pystan==2.19.1.1

It’s possible that you get some errors like these:

ERROR: Command errored out with exit status 1
Cython>=0.22 and NumPy are required.
ERROR: Failed building wheel for pystan

Don’t worry about that and let the installation process continue up to the end, because it will install the dependencies in the right way. The process is very slow, be patient. At the end you will see the message:

Successfully installed Cython-0.29.24 numpy-1.21.1 pystan-2.19.1.1

With PyStan and its dependencies installed on your system, you need to install Prophet.

Installing the Prophet library

To install the Prophet library, you can proceed as usual with the pip command:

% pip install prophet

Again, you may see some errors in the installation process as below:

ERROR: Command errored out with exit status 1:

ModuleNotFoundError: No module named 'pandas'

ERROR: Failed building wheel for prophet

Don’t worry about that and let the installation process continue up to the end, because it will install the dependencies in the right way. The process is very slow, be patient. At the end you will see the message:

Successfully installed Cython-0.29.24
LunarCalendar-0.0.9
cmdstanpy-0.9.68
convertdate-2.3.2
ephem-4.0.0.2
hijri-converter-2.2.0
holidays-0.11.2
korean-lunar-calendar-0.2.1
pandas-1.1.5
prophet-1.0.1
pymeeus-0.5.11
pystan-2.19.1.1
setuptools-git-1.2
tqdm-4.62.2
ujson-4.1.0

Testing Prophet

Finally, let’s check if all the things are working finewith a simple test.

Be sure you havethis csv data filein your project folder. You can check where you are as follow:

This command gives you the absolute path in your machine where you are now, copy the csv data file there with the Finder.

Open a Jupyter notebook and select the prophet39 kernel, or your preferred editor and type the following example: (you must use several code blocks to check every sentence)

See the attached notebook for the code:

If all works fine, you have the Prophet library correctly installed in your machine!

Conclusion

As we have seen, the installation does not differ from the official configuration. Here we have only taken into account the Conda environments, the versions we are installing and, fundamentally, the patience we must have when we encounter errors, as the installation process will try to finish correctly.

Finally, we have seen a simple example taken from the official documentation to test our installation.

If you consider machine learning as an important part of the future in financial markets, you can't afford to miss this highly-recommended learning track onMachine Learning & Deep Learning in Financial Marketsfor those interested in ML and its applications in trading by Quantra. Enroll now!

Files in the download:

Prophet python code

Prophet data file

Login to Download

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
