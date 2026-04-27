---
title: "Installing Keras - Using Python And R"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/installing-keras-python-r/"
date: "2018-10-18"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Installing Keras - Using Python And R

**来源**: [QuantInsti](https://blog.quantinsti.com/installing-keras-python-r/)  
**日期**: 2018-10-18  
**作者**: QuantInsti

---

## 原文

Installing Keras - Using Python And R

ByMario Pisa Peña

Installing Keras is a simple process that basically requires to decide to use the preferred backend engine and install Keras in the same way as any other Python library.

Keras is a Python library for Deep Learning. It has been developed to allow a fast and easy development and experimentation with Machine Learning, we can run Keras on top ofTensorFlow,CNTK, orTheano.

You should consider installing Keras if you want to play with deep learning without worrying too much about low-level details to build neural networks. Thanks to its high level of abstraction, modularity and ease of use, we can build AI systems in a simple way. In this article about installing Keras using Python and R, we would start with installing Keras.

Installing Keras - The Pre-installation

Keras runs on top ofTensorFlow,CNTK, orTheano, that is, we need a backend engine to run Keras on top of it.

Keras itself does not perform low-level operations, its advantage lies in its ability to model in a high-level layer, abstracting from the details of the low-level implementation. These low-level operations rely on the backend and, thanks to the Keras modularity, allows some of the following backends to be used:

TensorFlowis an open-source symbolic tensor manipulation framework developed by Google.

Theanois an open-source symbolic tensor manipulation framework developed by LISA Lab at Université de Montréal.

CNTKis an open-source toolkit for deep learning developed by Microsoft.

Therefore, we need to install some of them before installing Keras. Here we are going to rely onTensorFlowthat has great acceptance and high capabilities and is the default backend engine for Keras.

There are also some extensions available that can optionally be installed to help us solve some associated problems before installing Keras:

cuDNN: It’s needed to run Keras on the GPU.

h5py: HDF5 is a hierarchical file format to save data in a convenient manner, it’s useful to save a huge amount of dta and Keras models.

graphvizand pydot: A graphics libraries to plot Keras models.

Before we go ahead with installing Keras, let us look at the installation of Tensorflow.

TensorFlow installation

Mainly, there are two stable TensorFlow versions:

tensorflow: for running on CPU.

tensorflow-gpu: for running on GPU

Although with the GPU we can make very heavy computations without interrupting the work of the CPU, we are going to install the version for CPU for being simpler and is the ideal one to take the first steps with TensorFlow. You can read this article for guidelines and detailed steps oninstalling TensorFlow GPU.

There are also the same versions with the postfix nightly, which are unstable versions in development but include the latest updates and developments. Interesting for advanced users and try the most recent developments. To start with TensorFlow, they are not the most recommended.

So, to install the stable release ofTensorFlowwrite in your terminal:

$ pip install tensorflow

To install TensorFlow for running on GPU, you can refer tothis articlethat provides detailed steps.

Installing Keras on Python

Let's talk about installing Keras on Python. Installing Keras is no different from installing any other library in Python:

$ pip install keras

By default, while installing Keras, Keras will use TensorFlow as its tensor manipulation library. Followthese instructionsto configure the other Keras backends.

Testing Keras

To play with Keras, there are several interesting examples which you can play with it, but undoubtedly the examples that most interest us are related to markets, so I recommend you try reading this interesting post aboutArtificial Neural Network In Python Using KerasFor Predicting Stock Price Movement.

It is interesting to see how Keras abstracts the complexity of using directly TensorFlow on QuantInsti blog:Artificial Neural Network Using TensorFlow In PythonFor Predicting Stock Price

Installing Kerason R

Here, I would be explaining about installing Keras on R. Now, it is available the Keras package for R on CRAN. To install Keras on R proceed as usual:

install.packages("keras")
library(keras)

The Keras R interface uses the TensorFlow backend engine by default. For installing TensorFlow for R you must execute the following R command:

install_keras()

This process creates a Python Conda environment to manage the Keras and TensorFlow.

Conclusion

In this article about 'Installing Keras - Using Python And R' we have thus covered installing keras in Python and installing Keras in R. Keras is a Python Machine Learning library that allows us to abstract from the difficulties of implementing a low-level network. Thanks to its simple interface, we can quickly prototype machine learning experiments and worry about the problem itself, rather than the implementation.

As we have seen, installing Keras in Python does not entail any difficulties. If you want to start playing with Keras, the easiest thing to do is to start by beginning installing Keras - the default Keras engine, TensorFlow, and install the library as standard.

Installing Keras from R and using Keras does not have any difficulty either, although we must know that Keras in R, is really using a Python environment under the hoods.

To familiarize ourselves with Keras, we can use the examples from the official documentation, but we have seen some specific posts fromQuantInstito use Keras in trading.

If we talk about Deep Learning models, they require a lot of neural network layers and datasets for training and functioning and are critical in contributing to the field of Trading. To learn, how to apply deep learning models in trading visit our new courseNeural Networks In Tradingby the world-renowned Dr. Ernest P. Chan. It covers core concepts such as back and forward propagation to using LSTM models in Keras.

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
