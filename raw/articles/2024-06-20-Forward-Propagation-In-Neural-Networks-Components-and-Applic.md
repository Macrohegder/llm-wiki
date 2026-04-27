---
title: "Forward Propagation In Neural Networks: Components and Applications"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/forward-propagation-neural-networks/"
date: "2024-06-20"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Forward Propagation In Neural Networks: Components and Applications

**来源**: [QuantInsti](https://blog.quantinsti.com/forward-propagation-neural-networks/)  
**日期**: 2024-06-20  
**作者**: QuantInsti

---

## 原文

Forward Propagation In Neural Networks: Components and Applications

Originally written byVarun DivakarandRekhit Pachanekarand edited byChainika Thakar

What exactly is forward propagation in neural networks? Well, if we break down the words, "forward" implies moving ahead, and "propagation" refers to the spreading of something. In neural networks, forward propagation means moving in only one direction: from input to output. Think of it as moving forward in time, where we have no option but to keep moving ahead!

In this blog, we will delve into the intricacies of forward propagation, its calculation process, and its significance in different types of neural networks, including feedforward propagation, CNNs, and ANNs.

We will also explore the components involved, such as activation functions, weights, and biases, and discuss its applications across various domains, including trading. Additionally, we will discuss the examples of forward propagation implemented using Python, along with potential future developments and FAQs.

This blog covers:

What are neural networks?

What is forward propagation?

Forward propagation algorithm

Forward vs backward propagation in neural network

Forward propagation in different types of neural networks

Components of forward propagation

Applications of forward propagation

Process of forward propagation in trading

Forward propagation in neural networks for trading using Python

Challenges with forward propagation in trading

FAQs while using forward propagation in neural networks for trading

What are neural networks?

For centuries, we've been fascinated by how the human mind works. Philosophers have long grappled with understanding human thought processes. However, it's only in recent years that we've started making real progress in deciphering how our brains operate. This is where conventional computers diverge from humans.

You see, while we can create algorithms to solve problems, we have to consider all sorts of probabilities. Humans, on the other hand, can start with limited information and still learn and solve problems quickly and accurately. Hence, we began researching and developing artificial brains, now known asneural networks.

Definition of a neural network

A neural network is a computational model inspired by the human brain's neural structure, consisting of interconnected layers of artificial neurons. These networks process input data, adjust through learning, and produce outputs, making them effective for tasks like pattern recognition, classification, and predictive modelling.

What does a neural network look like?

A neural network could be simply described as follows:

The basic structure of a neural network is the perceptron, inspired by the neurons in our brains.

In a neural network, there are inputs to the neuron, marked with yellow circles, and then it emits an output signal after processing these inputs.

The input layer resembles the dendrites of a neuron, while the output signal is comparable to the axon. Each input signal is assigned a weight (wi), which is multiplied by the input value. Then the weighted sum of all input variables is stored.

Following this an activation function is applied to the weighted sum, resulting in the output signal.

One popular application of neural networks is image recognition software, capable of identifying faces and tagging the same person in different lighting conditions.

Now, let's delve into the details of forward propagation beginning with its definition.

What is forward propagation?

Forward propagation is a fundamental process in neural networks that involves moving input data through the network to produce an output. It's essentially the process of feeding input data into the network and computing an output value through the layers of the network.

During forward propagation, each neuron in the network receives input from the previous layer, performs a computation using weights and biases, applies an activation function, and passes the result to the next layer. This process continues until the output is generated. In simple terms, forward propagation is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.

Next, we will see the forward propagation algorithm in detail.

Forward propagation algorithm

Here's a simplified explanation of the forward propagation algorithm:

Input Layer:The process begins with the input layer, where the input data is fed into the network.

Hidden Layers:The input data is passed through one or more hidden layers. Each neuron in these hidden layers receives input from the previous layer, computes a weighted sum of these inputs, adds a bias term, and applies an activation function.

Output Layer:Finally, the processed data moves to the output layer, where the network produces its output.

Error Calculation:Once the output is generated, it is compared to the actual output (in the case of supervised learning). The error, also known as the loss, is calculated using a predefined loss function, such as mean squared error or cross-entropy loss.

The output of the neural network is then compared to the actual output (in the case of supervised learning) to calculate the error. This error is then used to adjust the weights and biases of the network during the backpropagation phase, which is crucial for training the neural network.

I will explain forward propagation with the help of a simple equation of a line next.

We all know that a line can be represented with the help of the equation:

y = mx + b

Where,

y is the y coordinate of the point

m is the slope

x is the x coordinate

b is the y-intercept i.e. the point at which the line crosses the y-axis

But why are we jotting the line equation here?This will help us later on when we understand the components of a neural network in detail.

Remember how we said neural networks are supposed to mimic the thinking process of humans?Well, let us just assume that we do not know the equation of a line, but we do have graph paper and draw a line randomly on it.

For the sake of this example, you drew a line through the origin and when you saw the x and y coordinates, they looked like this:

This looks familiar. If I asked you to find the relation between x and y, you would directly say it is y = 3x. But let us go through the process of how forward propagation works. We will assume here that x is the input and y is the output.

The first step here is the initialisation of the parameters. We will guess that y must be a multiplication factor of x. So we will assume that y = 5x and see the results then. Let us add this to the table and see how far we are from the answer.

Note that taking the number 5 is just a random guess and nothing else. We could have taken any other number here. I should point out that here we can term 5 as the weight of the model.

All right, this was our first attempt, now we will see how close (or far) we are from the actual output. One way to do that is to use the difference between the actual output and the output we calculated. We will call this the error. Here, we aren’t concerned with the positive or negative sign and hence we take the absolute difference of the error.

Thus, we will update the table now with the error.

If we take the sum of this error, we get the value 30. But why did we total the error? Since we are going to try multiple guesses to come to the closest answer, we need to know how close or how far we were from the previous answers. This helps us refine our guesses and calculate the correct answer.

Wait. But if we just add up all the error values, it feels like we are giving equal weightage to all the answers. Shouldn’t we penalise the values which are way off the mark? For example, 10 here is much higher than 2. It is here that we introduce the somewhat famous “Sum of squared Errors” or SSE for short. In SSE, we square all the error values and then add them. Thus, the error values which are very high get exaggerated and thus, help us in knowing how to proceed further.

Let’s put these values in the table below.

Now the SSE for the weight 5 (Recall that we assumed y = 5x), is 145. We call this the loss function. The loss function is important to understand the efficiency of the neural network and also helps us when we incorporatebackpropagationin the neural network.

All right, so far we understood the principle of how the neural network tries to learn. We have also seen the basic principle of the neuron. Next, we will see the forward vs backward propagation in the neural network.

Forward propagation vs backward propagation in neural network

Below is the table for a clear difference between forward and backward propagation in the neural network.

Aspect

Forward Propagation

Backward Propagation

Purpose

Compute the output of the neural network given inputs

Adjust the weights of the network to minimise error

Direction

Forward from input to output

Backwards, from output to input

Calculation

Computes the output using current weights and biases

Updates weights and biases using calculated gradients

Information flow

Input data -> Output data

Error signal -> Gradient updates

1. Input data is fed into the network.

2. Data is processed through hidden layers.

3. Output is generated.

1. Error is calculated using a loss function.

2. Gradients of the loss function are calculated.

3. Weights and biases are updated using gradients.

Used in

Prediction and inference

Training the neural network

Next, let us see the forward propagation in different types of neural networks.

Forward propagation in different types of neural networks

Forward propagation is a key process in various types of neural networks, each with its own architecture and specific steps involved in moving input data through the network to produce an output.

Forward propagation is a fundamental process in various types of neural networks, including:

Feedforward Neural Networks (FNN):In FNNs, also known as Multi-layer Perceptrons (MLPs), forward propagation involves passing the input data through the network's layers from the input layer to the output layer without any feedback loop.

Convolutional Neural Networks (CNN):In CNNs, forward propagation involves passing the input data through convolutional layers, pooling layers, and fully connected layers. Convolutional layers apply convolution operations to the input data, extracting features. Pooling layers reduce the spatial dimensions of the data. Fully connected layers perform the final classification.

Recurrent Neural Networks (RNN):In RNNs, forward propagation involves passing the input sequence through the network's layers. RNNs have recurrent connections, allowing information to persist. Each step in the sequence feeds the output of the previous step back into the network.

Long Short-Term Memory Networks (LSTM):LSTM networks are a type of RNN designed to address the vanishing gradient problem. Forward propagation in LSTMs involves passing input sequences through gates that control the flow of information. These gates include input, forget, and output gates, which regulate the flow of information in and out of the cell.

Autoencoder Networks:In autoencoder networks, forward propagation involves encoding the input data into a lower-dimensional representation and then decoding it back to the original input space.

Moving forward, let us discuss the components of forward propagation.

Components of forward propagation

In the above diagram, we see a neural network consisting of three layers. The first and the third layer are straightforward, input and output layers. But what is this middle layer and why is it called the hidden layer?

Now, in our example, we had just one equation, thus we have only one neuron in each layer.

Nevertheless, the hidden layer consists of two functions:

Pre-activation function: The weighted sum of the inputs is calculated in this function.

Activation function:Here, based on the weighted sum, an activation function is applied to make the network non-linear and make it learn as the computation progresses. The activation function uses bias to make it non-linear.

Going forward, we must check out the applications of forward propagation to learn about the same in detail.

Applications of forward propagation

In this example, we will be using a 3-layer network (with 2 input units, 2 hidden layer units, and 2 output units). The network and parameters (or weights) can be represented as follows.

Let us say that we want to train this neural network to predict whether the market will go up or down. For this, we assign two classes Class 0 and Class 1.

Here, Class 0 indicates the data point where the market closes down, and conversely, Class 1 indicates that the market closes up. To make this prediction, a train data(X) consisting of two features x1, and x2. Here x1 represents the correlation between the close prices and the 10-day simple moving average (SMA) of close prices, and x2 refers to the difference between the close price and the 10-day SMA.

In the example below, the data point belongs to class 1. The mathematical representation of the input data is as follows:

X = [x1, x2] = [0.85,.25] y= [1]

Example with two data points:

The output of the model is categorical or a discrete number. We need to convert this output data into a matrix form. This enables the model to predict the probability of a data point belonging to different classes. When we make this matrix conversion, the columns represent the classes to which that example belongs, and the rows represent each of the input examples.

In the matrix y, the first column represents class 0 and second column represents class 1. Since our example belongs to Class 1, we have 1 in the second column and zero in the first.

This process of converting discrete/categorical classes to logical vectors/matrices is called One-Hot Encoding. It's sort of like converting the decimal system (1,2,3,4....9) to binary (0,1,01,10,11). We use one-hot encoding as the neural network cannot operate on label data directly. They require all input variables and output variables to be numeric.

In neural network learning, apart from the input variable, we add a bias term to every layer other than the output layer. This bias term is a constant, mostly initialised to 1. The bias enables moving the activation threshold along the x-axis.

When the bias is negative the movement is made to the right side, and when the bias is positive the movement is made to the left side. So a biassed neuron should be capable of learning even such input vectors that an unbiased neuron is not able to learn. In the dataset X, to introduce this bias we add a new column denoted by ones, as shown below.

Let us randomly initialise the weights or parameters for each of the neurons in the first layer. As you can see in the diagram we have a line connecting each of the cells in the first layer to the two neurons in the second layer. This gives us a total of 6 weights to be initialized, 3 for each neuron in the hidden layer. We represent these weights as shown below.

Here, Theta1is the weights matrix corresponding to the first layer.

The first row in the above representation shows the weights corresponding to the first neuron in the second layer, and the second row represents the weights corresponding to the second neuron in the second layer. Now, let’s do the first step of the forward propagation, by multiplying the input value for each example by their corresponding weights which are mathematically shown below.

Theta1* X

Before we go ahead and multiply, we must remember that when you do matrix multiplications, each element of the product, X*θ, is the dot product sum of the row in the first matrix X with each of the columns of the second matrix θ.

When we multiply the two matrices, X and θ, we are expected to multiply the weights with the corresponding input example values. This means we need to transpose the matrix of example input data, X so that the matrix will multiply each weight with the corresponding input correctly.

z2= Theta1*XtHere z2is the output after matrix multiplication, and Xtis the transpose of X.The matrix multiplication process:$$
\begin{bmatrix}
    0.1 & 0.2 & 0.3 \\
    0.4 & 0.5 & 0.6 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.85 \\
    0.25 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.1*1 + 0.2*0.85 + 0.3*0.25 \\
    0.4*1 + 0.5*0.85 + 0.6*0.25 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.02 \\
    0.975 \\
    \end{bmatrix}
$$Let us say that we have applied a sigmoid activation after the input layer. Then we have to element-wise apply the sigmoid function to the elements in the z² matrix above. The sigmoid function is given by the following equation:$$ f(x) = \frac{1}{1+e^{-x}} $$After the application of the activation function, we are left with a 2x1 matrix as shown below.$$ a^{(2)}
=
\begin{bmatrix}
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$Here a(2)represents the output of the activation layer.These outputs of the activation layer act as the inputs for the next or the final layer, which is the output layer. Let us initialize another random weights/parameters called Theta2for the hidden layer. Each row in Theta2represents the weights corresponding to the two neurons in the output layer.$$ Theta_2
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
$$After initializing the weights (Theta2), we will repeat the same process that we followed for the input layer. We will add a bias term for the inputs of the previous layer. The a(2)matrix looks like this after the addition of bias vectors:$$ a^{(2)}
=
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$Let us see how the neural network looks like after the addition of the bias unit:Before we run our matrix multiplication to compute the final output z³, remember that before in z² calculation we had to transpose the input data a¹ to make it “line up” correctly for the matrix multiplication to result in the computations we wanted. Here, our matrices are already lined up the way we want, so there is no need to take the transpose of the a(2)matrix. To understand this clearly, ask yourself this question: “Which weights are being multiplied with what inputs?”.
Now, let us perform the matrix multiplication:z3= Theta2*a(2)where z3is the output matrix before the application of an activation function.Here for the last layer, we will be multiplying a 2x3 with a 3x1 matrix, resulting in a 2x1 matrix of output hypotheses. The mathematical computation is shown below:$$
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.5*1 + 0.4*0.735 + 0.3*0.726 \\
    0.2*1 + 0.5*0.735 + 0.1*0.726 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.0118 \\
    0.6401 \\
    \end{bmatrix}
$$After this multiplication, before getting the output in the final layer, we apply an element-wise conversion using the sigmoid function on the z² matrix.a3= sigmoid(z3)Where a3denotes the final output matrix.$$ a^3
=
\begin{bmatrix}
    0.7333 \\
    0.6548 \\
    \end{bmatrix}
$$The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.Process of forward propagation in tradingForward propagation in trading using neural networks involves several steps.Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.Forward propagation in neural networks for trading using PythonBelow, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:Step 1: Import necessary librariesThis step imports essential libraries required for data processing, fetching stock data, and building a neural network.In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.Step 2: Function to fetch historical stock dataThe function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.Step 3: Function to preprocess stock dataIn this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.Step 4: Function to create input features and target labelsThis function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.Step 5: Fetch historical stock dataThis step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.Step 6: Preprocess stock dataHere, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.Step 7: Create input features and target labelsIn this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.Step 8: Split the data into training, validation, and test setsThe dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.Step 9: Define the neural network architectureThis step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.Step 10: Compile the modelThe neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.Step 11: Train the modelIn this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.Step 12: Evaluate the modelThe trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.Step 13: Make predictions on test dataPredictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.Step 14: Create a DataFrame to compare predicted and actual pricesA DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.Output:Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.Challenges with forward propagation in tradingBelow are the challenges with forward propagation in trading and also the method for each challenge to be overcome.Challenges with Forward Propagation in TradingWays to OvercomeOverfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.Computational Resources: Training large neural networks on large datasets can require significant computational resources.Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.FAQs while using forward propagation in neural networks for tradingBelow, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.ConclusionForward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!File in the downloadForward propagation in neural networks for trading - Python notebookLogin to DownloadNote: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Here z2is the output after matrix multiplication, and Xtis the transpose of X.The matrix multiplication process:$$
\begin{bmatrix}
    0.1 & 0.2 & 0.3 \\
    0.4 & 0.5 & 0.6 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.85 \\
    0.25 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.1*1 + 0.2*0.85 + 0.3*0.25 \\
    0.4*1 + 0.5*0.85 + 0.6*0.25 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.02 \\
    0.975 \\
    \end{bmatrix}
$$Let us say that we have applied a sigmoid activation after the input layer. Then we have to element-wise apply the sigmoid function to the elements in the z² matrix above. The sigmoid function is given by the following equation:$$ f(x) = \frac{1}{1+e^{-x}} $$After the application of the activation function, we are left with a 2x1 matrix as shown below.$$ a^{(2)}
=
\begin{bmatrix}
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$Here a(2)represents the output of the activation layer.These outputs of the activation layer act as the inputs for the next or the final layer, which is the output layer. Let us initialize another random weights/parameters called Theta2for the hidden layer. Each row in Theta2represents the weights corresponding to the two neurons in the output layer.$$ Theta_2
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
$$After initializing the weights (Theta2), we will repeat the same process that we followed for the input layer. We will add a bias term for the inputs of the previous layer. The a(2)matrix looks like this after the addition of bias vectors:$$ a^{(2)}
=
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$Let us see how the neural network looks like after the addition of the bias unit:Before we run our matrix multiplication to compute the final output z³, remember that before in z² calculation we had to transpose the input data a¹ to make it “line up” correctly for the matrix multiplication to result in the computations we wanted. Here, our matrices are already lined up the way we want, so there is no need to take the transpose of the a(2)matrix. To understand this clearly, ask yourself this question: “Which weights are being multiplied with what inputs?”.
Now, let us perform the matrix multiplication:z3= Theta2*a(2)where z3is the output matrix before the application of an activation function.Here for the last layer, we will be multiplying a 2x3 with a 3x1 matrix, resulting in a 2x1 matrix of output hypotheses. The mathematical computation is shown below:$$
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.5*1 + 0.4*0.735 + 0.3*0.726 \\
    0.2*1 + 0.5*0.735 + 0.1*0.726 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.0118 \\
    0.6401 \\
    \end{bmatrix}
$$After this multiplication, before getting the output in the final layer, we apply an element-wise conversion using the sigmoid function on the z² matrix.a3= sigmoid(z3)Where a3denotes the final output matrix.$$ a^3
=
\begin{bmatrix}
    0.7333 \\
    0.6548 \\
    \end{bmatrix}
$$The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.Process of forward propagation in tradingForward propagation in trading using neural networks involves several steps.Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.Forward propagation in neural networks for trading using PythonBelow, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:Step 1: Import necessary librariesThis step imports essential libraries required for data processing, fetching stock data, and building a neural network.In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.Step 2: Function to fetch historical stock dataThe function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.Step 3: Function to preprocess stock dataIn this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.Step 4: Function to create input features and target labelsThis function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.Step 5: Fetch historical stock dataThis step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.Step 6: Preprocess stock dataHere, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.Step 7: Create input features and target labelsIn this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.Step 8: Split the data into training, validation, and test setsThe dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.Step 9: Define the neural network architectureThis step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.Step 10: Compile the modelThe neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.Step 11: Train the modelIn this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.Step 12: Evaluate the modelThe trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.Step 13: Make predictions on test dataPredictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.Step 14: Create a DataFrame to compare predicted and actual pricesA DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.Output:Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.Challenges with forward propagation in tradingBelow are the challenges with forward propagation in trading and also the method for each challenge to be overcome.Challenges with Forward Propagation in TradingWays to OvercomeOverfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.Computational Resources: Training large neural networks on large datasets can require significant computational resources.Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.FAQs while using forward propagation in neural networks for tradingBelow, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.ConclusionForward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!File in the downloadForward propagation in neural networks for trading - Python notebookLogin to DownloadNote: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Here z2is the output after matrix multiplication, and Xtis the transpose of X.The matrix multiplication process:$$
\begin{bmatrix}
    0.1 & 0.2 & 0.3 \\
    0.4 & 0.5 & 0.6 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.85 \\
    0.25 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.1*1 + 0.2*0.85 + 0.3*0.25 \\
    0.4*1 + 0.5*0.85 + 0.6*0.25 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.02 \\
    0.975 \\
    \end{bmatrix}
$$Let us say that we have applied a sigmoid activation after the input layer. Then we have to element-wise apply the sigmoid function to the elements in the z² matrix above. The sigmoid function is given by the following equation:$$ f(x) = \frac{1}{1+e^{-x}} $$After the application of the activation function, we are left with a 2x1 matrix as shown below.$$ a^{(2)}
=
\begin{bmatrix}
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$Here a(2)represents the output of the activation layer.These outputs of the activation layer act as the inputs for the next or the final layer, which is the output layer. Let us initialize another random weights/parameters called Theta2for the hidden layer. Each row in Theta2represents the weights corresponding to the two neurons in the output layer.$$ Theta_2
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
$$After initializing the weights (Theta2), we will repeat the same process that we followed for the input layer. We will add a bias term for the inputs of the previous layer. The a(2)matrix looks like this after the addition of bias vectors:$$ a^{(2)}
=
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$Let us see how the neural network looks like after the addition of the bias unit:Before we run our matrix multiplication to compute the final output z³, remember that before in z² calculation we had to transpose the input data a¹ to make it “line up” correctly for the matrix multiplication to result in the computations we wanted. Here, our matrices are already lined up the way we want, so there is no need to take the transpose of the a(2)matrix. To understand this clearly, ask yourself this question: “Which weights are being multiplied with what inputs?”.
Now, let us perform the matrix multiplication:z3= Theta2*a(2)where z3is the output matrix before the application of an activation function.Here for the last layer, we will be multiplying a 2x3 with a 3x1 matrix, resulting in a 2x1 matrix of output hypotheses. The mathematical computation is shown below:$$
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.5*1 + 0.4*0.735 + 0.3*0.726 \\
    0.2*1 + 0.5*0.735 + 0.1*0.726 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.0118 \\
    0.6401 \\
    \end{bmatrix}
$$After this multiplication, before getting the output in the final layer, we apply an element-wise conversion using the sigmoid function on the z² matrix.a3= sigmoid(z3)Where a3denotes the final output matrix.$$ a^3
=
\begin{bmatrix}
    0.7333 \\
    0.6548 \\
    \end{bmatrix}
$$The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.Process of forward propagation in tradingForward propagation in trading using neural networks involves several steps.Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.Forward propagation in neural networks for trading using PythonBelow, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:Step 1: Import necessary librariesThis step imports essential libraries required for data processing, fetching stock data, and building a neural network.In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.Step 2: Function to fetch historical stock dataThe function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.Step 3: Function to preprocess stock dataIn this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.Step 4: Function to create input features and target labelsThis function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.Step 5: Fetch historical stock dataThis step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.Step 6: Preprocess stock dataHere, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.Step 7: Create input features and target labelsIn this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.Step 8: Split the data into training, validation, and test setsThe dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.Step 9: Define the neural network architectureThis step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.Step 10: Compile the modelThe neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.Step 11: Train the modelIn this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.Step 12: Evaluate the modelThe trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.Step 13: Make predictions on test dataPredictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.Step 14: Create a DataFrame to compare predicted and actual pricesA DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.Output:Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.Challenges with forward propagation in tradingBelow are the challenges with forward propagation in trading and also the method for each challenge to be overcome.Challenges with Forward Propagation in TradingWays to OvercomeOverfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.Computational Resources: Training large neural networks on large datasets can require significant computational resources.Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.FAQs while using forward propagation in neural networks for tradingBelow, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.ConclusionForward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!File in the downloadForward propagation in neural networks for trading - Python notebookLogin to DownloadNote: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

The matrix multiplication process:

Let us say that we have applied a sigmoid activation after the input layer. Then we have to element-wise apply the sigmoid function to the elements in the z² matrix above. The sigmoid function is given by the following equation:

After the application of the activation function, we are left with a 2x1 matrix as shown below.

Here a(2)represents the output of the activation layer.

These outputs of the activation layer act as the inputs for the next or the final layer, which is the output layer. Let us initialize another random weights/parameters called Theta2for the hidden layer. Each row in Theta2represents the weights corresponding to the two neurons in the output layer.

After initializing the weights (Theta2), we will repeat the same process that we followed for the input layer. We will add a bias term for the inputs of the previous layer. The a(2)matrix looks like this after the addition of bias vectors:

Let us see how the neural network looks like after the addition of the bias unit:

Before we run our matrix multiplication to compute the final output z³, remember that before in z² calculation we had to transpose the input data a¹ to make it “line up” correctly for the matrix multiplication to result in the computations we wanted. Here, our matrices are already lined up the way we want, so there is no need to take the transpose of the a(2)matrix. To understand this clearly, ask yourself this question: “Which weights are being multiplied with what inputs?”.
Now, let us perform the matrix multiplication:z3= Theta2*a(2)where z3is the output matrix before the application of an activation function.Here for the last layer, we will be multiplying a 2x3 with a 3x1 matrix, resulting in a 2x1 matrix of output hypotheses. The mathematical computation is shown below:$$
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.5*1 + 0.4*0.735 + 0.3*0.726 \\
    0.2*1 + 0.5*0.735 + 0.1*0.726 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.0118 \\
    0.6401 \\
    \end{bmatrix}
$$After this multiplication, before getting the output in the final layer, we apply an element-wise conversion using the sigmoid function on the z² matrix.a3= sigmoid(z3)Where a3denotes the final output matrix.$$ a^3
=
\begin{bmatrix}
    0.7333 \\
    0.6548 \\
    \end{bmatrix}
$$The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.Process of forward propagation in tradingForward propagation in trading using neural networks involves several steps.Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.Forward propagation in neural networks for trading using PythonBelow, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:Step 1: Import necessary librariesThis step imports essential libraries required for data processing, fetching stock data, and building a neural network.In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.Step 2: Function to fetch historical stock dataThe function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.Step 3: Function to preprocess stock dataIn this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.Step 4: Function to create input features and target labelsThis function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.Step 5: Fetch historical stock dataThis step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.Step 6: Preprocess stock dataHere, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.Step 7: Create input features and target labelsIn this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.Step 8: Split the data into training, validation, and test setsThe dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.Step 9: Define the neural network architectureThis step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.Step 10: Compile the modelThe neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.Step 11: Train the modelIn this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.Step 12: Evaluate the modelThe trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.Step 13: Make predictions on test dataPredictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.Step 14: Create a DataFrame to compare predicted and actual pricesA DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.Output:Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.Challenges with forward propagation in tradingBelow are the challenges with forward propagation in trading and also the method for each challenge to be overcome.Challenges with Forward Propagation in TradingWays to OvercomeOverfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.Computational Resources: Training large neural networks on large datasets can require significant computational resources.Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.FAQs while using forward propagation in neural networks for tradingBelow, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.ConclusionForward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!File in the downloadForward propagation in neural networks for trading - Python notebookLogin to DownloadNote: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

z3= Theta2*a(2)where z3is the output matrix before the application of an activation function.Here for the last layer, we will be multiplying a 2x3 with a 3x1 matrix, resulting in a 2x1 matrix of output hypotheses. The mathematical computation is shown below:$$
\begin{bmatrix}
    0.5 & 0.4 & 0.3 \\
    0.2 & 0.5 & 0.1 \\
    \end{bmatrix}
*
\begin{bmatrix}
    1 \\
    0.735 \\
    0.726 \\
    \end{bmatrix}
$$


$$
=
\begin{bmatrix}
    0.5*1 + 0.4*0.735 + 0.3*0.726 \\
    0.2*1 + 0.5*0.735 + 0.1*0.726 \\
    \end{bmatrix}
=
\begin{bmatrix}
    1.0118 \\
    0.6401 \\
    \end{bmatrix}
$$After this multiplication, before getting the output in the final layer, we apply an element-wise conversion using the sigmoid function on the z² matrix.a3= sigmoid(z3)Where a3denotes the final output matrix.$$ a^3
=
\begin{bmatrix}
    0.7333 \\
    0.6548 \\
    \end{bmatrix}
$$The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.Process of forward propagation in tradingForward propagation in trading using neural networks involves several steps.Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.Forward propagation in neural networks for trading using PythonBelow, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:Step 1: Import necessary librariesThis step imports essential libraries required for data processing, fetching stock data, and building a neural network.In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.Step 2: Function to fetch historical stock dataThe function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.Step 3: Function to preprocess stock dataIn this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.Step 4: Function to create input features and target labelsThis function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.Step 5: Fetch historical stock dataThis step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.Step 6: Preprocess stock dataHere, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.Step 7: Create input features and target labelsIn this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.Step 8: Split the data into training, validation, and test setsThe dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.Step 9: Define the neural network architectureThis step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.Step 10: Compile the modelThe neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.Step 11: Train the modelIn this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.Step 12: Evaluate the modelThe trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.Step 13: Make predictions on test dataPredictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.Step 14: Create a DataFrame to compare predicted and actual pricesA DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.Output:Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.Challenges with forward propagation in tradingBelow are the challenges with forward propagation in trading and also the method for each challenge to be overcome.Challenges with Forward Propagation in TradingWays to OvercomeOverfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.Computational Resources: Training large neural networks on large datasets can require significant computational resources.Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.FAQs while using forward propagation in neural networks for tradingBelow, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.ConclusionForward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!File in the downloadForward propagation in neural networks for trading - Python notebookLogin to DownloadNote: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Here for the last layer, we will be multiplying a 2x3 with a 3x1 matrix, resulting in a 2x1 matrix of output hypotheses. The mathematical computation is shown below:

After this multiplication, before getting the output in the final layer, we apply an element-wise conversion using the sigmoid function on the z² matrix.

a3= sigmoid(z3)

Where a3denotes the final output matrix.$$ a^3
=
\begin{bmatrix}
    0.7333 \\
    0.6548 \\
    \end{bmatrix}
$$The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.Process of forward propagation in tradingForward propagation in trading using neural networks involves several steps.Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.Forward propagation in neural networks for trading using PythonBelow, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:Step 1: Import necessary librariesThis step imports essential libraries required for data processing, fetching stock data, and building a neural network.In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.Step 2: Function to fetch historical stock dataThe function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.Step 3: Function to preprocess stock dataIn this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.Step 4: Function to create input features and target labelsThis function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.Step 5: Fetch historical stock dataThis step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.Step 6: Preprocess stock dataHere, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.Step 7: Create input features and target labelsIn this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.Step 8: Split the data into training, validation, and test setsThe dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.Step 9: Define the neural network architectureThis step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.Step 10: Compile the modelThe neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.Step 11: Train the modelIn this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.Step 12: Evaluate the modelThe trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.Step 13: Make predictions on test dataPredictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.Step 14: Create a DataFrame to compare predicted and actual pricesA DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.Output:Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.Challenges with forward propagation in tradingBelow are the challenges with forward propagation in trading and also the method for each challenge to be overcome.Challenges with Forward Propagation in TradingWays to OvercomeOverfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.Computational Resources: Training large neural networks on large datasets can require significant computational resources.Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.FAQs while using forward propagation in neural networks for tradingBelow, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.ConclusionForward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!File in the downloadForward propagation in neural networks for trading - Python notebookLogin to DownloadNote: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

The output of a sigmoid function is the probability of the given example belonging to a particular class. In the above representation, the first row represents the probability that the example belonging to Class 0 and the second row represents the probability of Class 1.

That’s all there is to know about forward propagation in Neural networks. But wait! How can we apply this model in trading? Let’s find out below.

Process of forward propagation in trading

Forward propagation in trading using neural networks involves several steps.

Step 1: Data Collection andPreprocessing:Firstly,historical market data, including price, volume, and other relevant features, is collected and preprocessed. This involves cleaning, normalising, and transforming the data as needed, and splitting it into training, validation, and test sets.

Step 2: Model Architecture:Next, a suitable neural network architecture is designed for the trading task. This includes choosing the number and types of layers, the number of neurons in each layer, and the activation functions.

Step 3: Input Data Preparation:The input data is prepared by defining input features (e.g., past prices, volume) and output targets (e.g., future prices, buy/sell signals).

Step 4: Forward Propagation:During forward propagation, the input data is fed into the neural network, and the network computes the predicted output values using the current weights and biases. Activation functions are applied at each layer to introduce non-linearity into the network.

Step 5: Loss Calculation:The loss or error between the predicted output values and the actual target labels is then calculated using a suitable loss function.

Step 6: Backpropagation and optimisation:Backpropagation is used to update the weights and biases of the neural network to minimise the loss.

Step 7: Model evaluation:The trained model is evaluated on a validation set to assess its performance, and adjustments are made to the model architecture and hyperparameters as needed.

Step 8: Forward propagation of new data:Once the model is trained and evaluated, forward propagation is used on new, unseen data to make predictions.

Step 9: Trading strategy implementation:Finally, a trading strategy is developed and implemented based on the model predictions, and the performance of the strategy is monitored and iterated upon over time.

Last but not least, you must keep monitoring the performance of the trading strategy in real-world market conditions and evaluate the profitability and risk of the trading on a continuous basis.

Now that you have understood the steps thoroughly, let us move forward to find the steps of forward propagation for trading with Python.

Forward propagation in neural networks for trading using Python

Below, we will usePython programmingto predict the price of our stock “AAPL”. Here are the steps with the code:

Step 1: Import necessary libraries

This step imports essential libraries required for data processing, fetching stock data, and building a neural network.

In the code,numpyis used for numerical operations, pandas for data manipulation,yfinanceto download stock data, tensorflow for creating and training the neural network, andsklearnfor splitting data and preprocessing.

Step 2: Function to fetch historical stock data

The function in the code above uses yfinance to download historical stock data for a specified ticker symbol within a given date range. It returns a DataFrame containing the stock data, which includes information such as the closing prices, which are crucial for subsequent steps.

Step 3: Function to preprocess stock data

In this step, the function scales the stock's closing prices to a range between 0 and 1 using MinMaxScaler.

Scaling the data is important for neural network training as it standardises the input values, improving the model's performance and convergence.

Step 4: Function to create input features and target labels

This function generates the dataset for training by creating sequences of data points. It takes the scaled data and creates input features (X) and target labels (y). Each input feature is a sequence of time_steps number of past prices, and each target label is the next price following the sequence.

Step 5: Fetch historical stock data

This step involves fetching the historical stock data for Apple Inc. (ticker: AAPL) from January 1, 2010, to May 20, 2024, using the get_stock_data function defined earlier. The fetched data is stored in stock_data.

Step 6: Preprocess stock data

Here, the closing prices from the fetched stock data are scaled using the preprocess_data function. The scaled data and the scaler used for transformation are returned for future use in rescaling predictions.

Step 7: Create input features and target labels

In this step, input features and target labels are created using a window of 30 time steps (days). The create_dataset function is used to transform the scaled closing prices into the required format for the neural network.

Step 8: Split the data into training, validation, and test sets

The dataset is split into training, validation, and test sets. First, 70% of the data is used for training, and the remaining 30% is split equally into validation and test sets. This ensures the model is trained and evaluated on separate data subsets.

Step 9: Define the neural network architecture

This step defines the neural network architecture using TensorFlow'sKerasAPI. The network has three layers: two hidden layers with 64 and 32 neurons respectively, both using the ReLU activation function, and an output layer with a single neuron to predict the stock price.

Step 10: Compile the model

The neural network model is compiled using the Adam optimizer and mean squared error (MSE) loss function. Compiling configures the model for training, specifying how it will update weights and calculate errors.

Step 11: Train the model

In this step, the model is trained using the training data. The training runs for 50 epochs with a batch size of 32. During training, the model also evaluates its performance on the validation data to monitor overfitting.

Step 12: Evaluate the model

The trained model is evaluated on the test data to measure its performance. The loss value (mean squared error) is printed to indicate the model's prediction accuracy on unseen data.

Step 13: Make predictions on test data

Predictions are made using the test data. The predicted scaled prices are transformed back to their original scale using the inverse transformation of the scaler, making them interpretable.

Step 14: Create a DataFrame to compare predicted and actual prices

A DataFrame is created to compare the actual and predicted prices, including the difference between them. This comparison allows for a detailed analysis of the model's performance.

Finally, the actual and predicted stock prices are plotted for visual comparison. The plot includes labels and legends for clarity, helping to visually assess how well the model's predictions align with the actual prices.

Output:

Date             Actual Price   Predicted Price   Difference
0   2022-03-28    149.479996       152.107712   -2.627716
1   2022-03-29     27.422501        27.685801   -0.263300
2   2022-03-30     13.945714        14.447398   -0.501684
3   2022-03-31     14.193214        14.936252   -0.743037
4   2022-04-01     12.434286        12.938693   -0.504407
..         ...           ...              ...         ...
534 2024-05-13    139.070007       136.264969    2.805038
535 2024-05-14     12.003571        12.640266   -0.636696
536 2024-05-15      9.512500         9.695284   -0.182784
537 2024-05-16     10.115357         9.872525    0.242832
538 2024-05-17    187.649994       184.890900    2.759094

So far we have seen how forward propagation works and how to use it in trading, but there are certain challenges with using the same that we will discuss next so as to remain well aware of the same.

Challenges with forward propagation in trading

Below are the challenges with forward propagation in trading and also the method for each challenge to be overcome.

Challenges with Forward Propagation in Trading

Ways to Overcome

Overfitting: Neural networks may overfit to the training data, resulting in poor performance on unseen data.

Use techniques such as regularisation (e.g., L1, L2 regularisation) to prevent overfitting. Use dropout layers to randomly drop neurons during training to reduce overfitting. Use early stopping to halt training when the validation loss starts to increase.

Data Quality: Poor quality or noisy data can negatively impact the performance of the neural network.

Perform thorough data cleaning and preprocessing to remove outliers and errors. Use feature engineering to extract relevant features from the data. Use data augmentation techniques to increase the size and diversity of the training data.

Lack of Interpretability: Neural networks are often considered black-box models, making it difficult to interpret their decisions.

Use techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to explain the predictions of the neural network. Visualise the learned features and activations to gain insights into the model's decision-making process.

Computational Resources: Training large neural networks on large datasets can require significant computational resources.

Use techniques such as mini-batch gradient descent to train the model on smaller batches of data. Use cloud computing services or GPU-accelerated hardware to speed up training. Consider using pre-trained models or transfer learning to leverage models trained on similar tasks or datasets.

Market Volatility: Sudden changes or volatility in the market can make it challenging for neural networks to make accurate predictions.

Use ensemble methods such as bagging or boosting to combine multiple neural networks and reduce the impact of individual network errors. Implement dynamic learning rate schedules to adapt the learning rate based on the volatility of the market. Use robust evaluation metrics that account for the uncertainty and volatility of the market.

Noisy data: Inaccurate or mislabelled data can lead to incorrect predictions and poor model performance.

Perform thorough data validation and error analysis to identify and correct mislabelled data. Use semi-supervised or unsupervised learning techniques to leverage unlabelled data and improve model robustness. Implement outlier detection and anomaly detection techniques to identify and remove noisy data points.

Coming to the end of the blog, let us see some frequently asked questions while using forward propagation in neural networks for trading.

FAQs while using forward propagation in neural networks for trading

Below, there is a list of commonly asked questions which can be explored for better clarity on forward propagation.

Q: How can overfitting be addressed in trading neural networks?A: Overfitting can be addressed by using techniques such as regularisation, dropout layers, and early stopping during training.

Q: What preprocessing steps are required before forward propagation in trading neural networks?A: Preprocessing steps include data cleaning, normalisation, feature engineering, and splitting the data into training, validation, and test sets.

Q: Which evaluation metrics are used to assess the performance of trading neural networks?A: Common evaluation metrics include accuracy, precision, recall, F1-score, and mean squared error (MSE).

Q: What are some best practices for trainingneural networks for trading?A: Best practices include using ensemble methods, dynamic learning rate schedules, robust evaluation metrics, and model interpretability techniques.

Q: How can I implement forward propagation in trading using Python?A: Forward propagation in trading can be implemented using Python libraries such as TensorFlow, Keras, and scikit-learn. You can fetch historical stock data using yfinance and preprocess it before training the neural network.

Q: What are some potential pitfalls to avoid when using forward propagation in trading?A: Some potential pitfalls include overfitting to the training data, relying on noisy or inaccurate data, and not considering the impact of market volatility on model predictions.

Conclusion

Forward propagation in neural networks is a fundamental process that involves moving input data through the network to produce an output. It is like passing a message through a series of people, with each person adding some information before passing it to the next person until it reaches its destination.

By designing a suitable neural network architecture, preprocessing the data, and training the model using techniques like backpropagation, traders can make informed decisions and develop effective trading strategies.

You can learn more about forward propagation with our learning track onmachine learning and deep learning in tradingwhich consists of courses that cover everything from data cleaning to predicting the correct market trend. It will help you learn how different machine learning algorithms can be implemented in financial markets as well as to create your own prediction algorithms using classification and regression techniques. Enroll now!

File in the download

Forward propagation in neural networks for trading - Python notebook

Login to Download

Note: The original post has been revamped on 20thJune 2024 for recentness, and accuracy.

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
