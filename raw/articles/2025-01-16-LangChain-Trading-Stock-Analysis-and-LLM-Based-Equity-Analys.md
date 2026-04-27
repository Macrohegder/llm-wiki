---
title: "LangChain Trading: Stock Analysis and LLM-Based Equity Analysis in Python"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/langchain-trading-stock-analysis-llm-financial-python/"
date: "2025-01-16"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# LangChain Trading: Stock Analysis and LLM-Based Equity Analysis in Python

**来源**: [QuantInsti](https://blog.quantinsti.com/langchain-trading-stock-analysis-llm-financial-python/)  
**日期**: 2025-01-16  
**作者**: QuantInsti

---

## 原文

LangChain for Equity Investment Analysis

ByManusha Rao

Investment analysts increasingly use artificial intelligence to process financial data, identify trends, and gain deeper insights. LangChain is a promising open-source framework that brings the power of language models like GPT into investment analysis. This blog will explore how LangChain can ease the initial investment research process, from integrating financial data sources to creating sophisticated, custom models that provide predictive insights.

In this blog, we will explore the following:

Why LangChain?

What is LangChain?

Components of LangChain

Equity analysis using LangChain and OpenAI in Python

Why LangChain?

Let’s ask ChatGPT to analyze the performance of the NIFTY50 index using price data for the last 5 years.

As you can see from the response above, ChatGPT has no data readily available to do the analysis.

Here is where LangChain comes to our rescue. LangChain facilitates the integration of financial data sources with the LLMs, reshaping how investors analyze and interpret market data. LangChain's ability to analyze large volumes of textual data, including news articles, earnings reports, and social media sentiment, provides analysts with richer and more timely insights, aiding in better investment decisions.

What is LangChain?

LangChain acts as an interface between large language models and external data sources to create AI-powered applications. LangChain allows developers to build real-world applications that connect to databases, retrieve information, process inputs, and offer structured output.

LLMs are deep-learning models trained on large amounts of data that can generate responses to user queries. LangChain provides tools and abstractions to improve the customization, accuracy, and relevancy of the information the models generate. LangChain supports a wide range of LLM models. (List of supported LLMs:https://python.langchain.com/docs/integrations/llms/)

Components of LangChain

Let’s now demonstrate how to implement the components of LangChain in Python.

The version of langchain_openai used is mentioned below(for 1 to 3):

Using LLMs

LangChain allows the integration of multiple LLMs (Large Language Models) through prompting, enabling the generation of sophisticated responses tailored to specific tasks or queries.

Temperature talks about the amount of randomness in the model.If it is set to zero, we get a deterministic output, i.e. same output each time you run the code.

Output:

Here the output consists of many elements, we are interested only in the content part. Hence, to extract only the content part you can do the following:

2.Prompt Templates

Prompt templates are predefined structures or formats that generate prompts for language models like GPT-4. These templates help craft consistent and contextually relevant queries or commands to obtain desired responses from the model. Prompt templates can include placeholders that are dynamically filled with specific data or parameters.

3.Chains

A “chain” refers to a sequence of steps or operations linked together to perform a complex task using language models. Chains can combine multiple prompt templates, data processing steps, API calls, and other actions to build robust and reusable workflows for natural language processing tasks.

The expression “chain = prompt | llm” creates a sequence where a prompt is passed through an LLM to generate a response.

A "batch" refers to simultaneously processing multiple data instances through the chain. This can significantly enhance efficiency by leveraging parallel processing, where multiple data inputs are processed together in one go instead of sequentially.

4.Agents

An "agent" is an autonomous entity that performs specific tasks using language models. Agents can make decisions, execute actions, and interact with various data sources or APIs based on the tasks they are designed to handle. LangChain agents are typically used to automate complex workflows, perform real-time decision-making, and interact with users or systems dynamically.

The tool in the example below is PythonREPLTool(), which lets you run Python code within a LangChain agent or chain. This allows you to process, analyze, or compute data directly using Python code while interacting with other parts of LangChain, such as LLMs, prompts, and external data sources.

Please note that LangChain version of the below code is“langchain-core<0.2”

Let’s now see how we can use these components to analyze equities using different data sources.

Equity analysis using LangChain and OpenAI in Python

Let’s now build a simple LLM-based application, to analyze if a given stock ticker is a worthy candidate to consider for investing.

This application uses the following data:

Google news

Historical data on the stock

ChatGPT agent uses this data to synthesize the data and generate a response.

In this code, we will use agents to generate responses. You can also usefunction callingfor a more structured output.

Pre-requisites:

An OpenAI API key is required. You can visit thelinkto sign up and generate the API key. Please note the API key is available at a cost.

SERP API key is required. You can visit thislinkto create an API key. This API is required to obtain the latest news of a particular ticker.

Import the libraries.

Before we start importing the necessary libraries, ensure that you install the below-mentioned version of the Pydantic library.

Now import the required libraries as shown below:

The langChain_core.tools module in LangChain is designed to define and manage tools that agents can used or integrate into workflows. Tools in LangChain represent discrete functionalities that an agent can invoke to perform specific tasks, such as calculations, database queries, web searches, or API interactions.

The langchain.agents library in LangChain provides the framework for building and running agents—LLM-powered systems capable of reasoning, decision-making, and dynamically using tools to perform tasks. Agents follow a thought-action-observation loop, where they "think" about the next action to take, execute the action (often by invoking tools), and "observe" the result before proceeding.

The langchain_core.prompts library is a crucial part of LangChain, providing tools to design, manipulate, and manage prompts for language models. Prompts serve as the instructions or templates that guide the behavior of a language model. This library supports creating flexible and dynamic prompts for tasks such as question answering, summarization, and custom workflows.

2.Get the latest news on ticker.

Define a function to get the latest news for the ticker using SERP API. Plug in your API key in place of “YOUR_SERPAPI_API_KEY”.

3.Get the historical price data.

Extract one year of historical stock price data using Yahoo Finance.

4.Function to analyze whether to invest or not.

Define a function to define the rules to decide whether to invest.

5.Define the tools

Define the functions we defined in the previous steps as three tools: get_news, get_historical_data, and analyze_stock.

6.Define the prompt.

7.Create the agent and generate the response.

Responses

Response 1:

Response 2:

We have successfully implemented a basic equity analyzer based on historical data and the latest news.

The responses are just a preliminary analysis based on the data and context provided and require further research. The responses should not be considered professional advice or a definitive solution. The blog demonstrates how, by integrating financial sources(historical data and news), LLMs can assist in analyzing trends and providing data-driven insights, enabling quicker and more informed decisions.

Disclaimer: The content provided in this blog is for informational and educational purposes only. It is based on the version of LangChain and related libraries available at the time of writing. Given that LangChain is an evolving framework, updates, new features, and changes to its API may occur frequently. Readers are advised to verify the latest documentation and releases of LangChain and its dependencies before implementing any code or concepts discussed here.
For the most up-to-date information, please refer to the official LangChain documentation.

---

*Imported from QuantInsti Blog on 2026-04-27*
