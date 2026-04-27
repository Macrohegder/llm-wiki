---
title: "Application of LLMs in Portfolio Management: Creating Thematic Universe Index"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/application-llm-portfolio-management-thematic-index/"
date: "2024-12-05"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Application of LLMs in Portfolio Management: Creating Thematic Universe Index

**来源**: [QuantInsti](https://blog.quantinsti.com/application-llm-portfolio-management-thematic-index/)  
**日期**: 2024-12-05  
**作者**: QuantInsti

---

## 原文

Application of LLMs in Portfolio Management: Creating Thematic Universe Index

ByAjay PawarIn this article, we will explore the application of Large Language Models (LLMs) in Finance, covering topics like:

Quantitative finance

Portfolio management

Sentiment analysis

News analysis

OpenAI API and Python

We will demonstrate how LLMs, paired with tools like OpenAI API and Python, can streamline processes such as generating thematic portfolios and analysing trends for smarter investment decisions.

This blog is for you if you are are motivated by:

Ideation:Learning innovative ways to apply LLMs in finance and quantitative analysis.

Implementation:Gaining practical guidance on integrating LLMs for tasks likenews trading strategiesand sentiment analysis, thematic investing, or automating financial research.

Efficiency:Discovering how LLMs simplify complex, time-intensive workflows inquantitative portfolio managementand financial analysis.

Reading Level:Advanced

Prerequisites

You have the basic idea of usingChatGPT for Trading. You know how to write prompts to create a simple Python code and have been able to enhance it further.

You have read aboutTrading using LLM. You are aware of a few examples of how Generative AI & Sentiment Analysis in Finance/Sentiment Analysis for tradingcan assist traders in finding an edge in volatile market situations.

This blog covers:

How to Create Thematic Universe for Portfolio Strategies Using GenAI

How to Create Thematic Universe for Portfolio Strategies Using GenAI? - Python notebook

How to Create Thematic Universe for Portfolio Strategies Using GenAI

What is Thematic Index investing?

Thematic investing focuses on capturing long-term trends, disruptive technologies, or specific sectors that align with an investor’s preferences. One popular strategy isThematic Index Investing, where investors focus on companies that meet certain criteria, such as sustainability, technology adoption, or demographic trends.

In this blog, we demonstrate how to create athematic universe for healthcare companies developing AI solutions. Doing such research manually is time-consuming, resource-intensive, and often prone to oversight. By leveraging Generative AI (GenAI), we can automate this process to extract meaningful insights and create a shortlist of companies aligned with our thematic goals.

Thematic Focus: Healthcare and AI

Let’s say we want to invest inhealthcare companies that are actively developing AI solutions. This is a highly relevant theme as AI is becoming a critical component of advancements in diagnostics, treatment, and medical research.

Problem Statement

Manually identifying and analysing companies that fit this theme requires combing through:

Large datasets like the S&P 500.

Sector-specific information, such as healthcare companies.

Publicly available information like news articles or company reports.

This process is not only resource-intensive but also subject to human error.

Our Approach Using GenAI

By using Generative AI, we automate this process to:

Fetch the S&P 500 data and filter it by sector to isolate healthcare companies.

Fetch News for the Tickers.

Analyse available information for each company, such as:

Solutions: Products or services they provide.

Technology: Specific tools or platforms they are leveraging.

R&D: Innovations under development.

4. Summarise how AI is being used by these companies based on publicly available information, such as news articles.

5. Shortlist the companies that align with the thematic goal ofhealthcare and AI.

Results

Initial Universe: The S&P 500 contains 62 healthcare companies after filtering for the sector.

Final Thematic Universe: After applying the GenAI-powered process, we identified 19 companies actively developing or utilising AI solutions.

Time Efficiency: What would have taken hours or days of manual research was accomplished in minutes using the provided code.

APIs Used

OpenAI API: A paid service that powers the Generative AI analysis for summarising and classifying company information.

NewsAPI: A free developer version (https://newsapi.org/) with a limit of 100 requests per day, used to fetch news articles related to the companies.

Disclaimer

This blog and code are foreducational and research purposes only.

We are not promoting or endorsing any company, brand, or product mentioned in this blog.

Some of the information isLLM-generated and may require cross-validationfor accuracy.

This isnot investment adviceand should not be construed as a recommendation to invest in any of the companies mentioned.

How to Create Thematic Universe for Portfolio Strategies Using GenAI? - Python notebook

Login to Download

By using this method, we showcase how Generative AI can streamline the process of creating thematic universes forportfolio strategiesand identify potential candidates for thematic index investing.

This analysis highlights 19 healthcare companies leveraging AI in areas such as diagnostics, drug development, patient care, surgical precision, research, sustainability, and healthcare tools. The list is based on the last six months of news, constrained by the News API's data access. While additional companies may fall outside this scope, the curated selection provides a focused starting point.

Generated by LLMs, the analysis may include hallucinations, overlaps, or misinterpretations, necessitating manual validation for accuracy. Despite this, it saves time by narrowing the field for deeper exploration.

Portfolio managers and traders can use this universe alongside quantitative tools to identify market opportunities, optimise timing, and diversify investments. Investors focused on healthcare can overweight high-growth potential companies, while traders can track firms nearing key milestones, such as drug approvals, for active monitoring and strategic market entries.

Summary

Generative AI is transforming investment research by offering innovative tools to uncover opportunities and trends with unparalleled speed and precision.

In this blog, we explored how Generative AI can assist in creating a thematic universe forhealthcare companies actively developing AI solutions. Our approach involved filtering the S&P 500 healthcare companies, gathering relevant news, analysing it with large language models (LLMs), and extracting critical information in a structured format. By incorporating an AI-specific keyword filter, we identified companies working on innovative technologies and solutions.

This process generated a comprehensive database outlining each company's solutions, technologies, and R&D efforts. Such a database can be leveraged to create or refine themes. For instance, companies focused on diabetes/cancer solutions can be easily identified from the existing approach. Traditionally, conducting such an extensive study across a large universe could take weeks. However, our analysis achieved a focused output within minutes, significantly reducing time and labor. Nevertheless, manual validation remains essential to ensure accuracy, as the quality of insights heavily relies on available data and LLM models.

For investors and traders, this approach adds a new dimension to decision-making. Healthcare-focused investors can strategically overweight specific categories of companies with strong growth potential, while traders can actively monitor firms nearing key milestones, such as drug approvals. By combining this thematic analysis with quantitative tools, market participants can optimise timing, diversify investments, and uncover actionable opportunities more effectively.

Takeaways:

In this blog we covered:

Ideation: Generating new ideas for leveraging LLMs in portfolio management, sentiment analysis, and thematic investing.

Implementation: Practical steps to apply tools like the OpenAI API and Python for automating research workflows.

Use Cases: Real-world examples of AI integration into finance by constructing thematic universes.

Tools & Techniques: Insights into combining LLMs with quantitative tools to uncover and act on market opportunities effectively.

Conclusion

Generative AI offers a scalable, efficient blueprint for constructing thematic universes tailored to investor goals and market opportunities. As this technology evolves, its role in refining investment strategies will become even more vital. By balancing AI-driven insights with human expertise, market participants can make smarter, more informed, and efficient decisions, capitalising on trends in the healthcare industry and beyond.

Relevant Advanced Courses on Quantra

1. For Traders:

Utilise Large Language Models (LLMs) to build sentiment-driven trading strategies. This course covers LLM basics, prompt engineering for actionable insights, and practical use in trading. Learn to extract sentiment scores from event transcripts like FED meetings or earnings calls, and develop different strategies around it. Analyse your strategy's performance rigorously, leveraging LLM capabilities for informed trading decisions.

Course link:Trading Using LLM: Concepts and Strategies

2. For Portfolio Managers:

Are you looking to useAI in tradingto figure out how much to invest in different stocks? This course has got the answers, thanks to LSTM networks. This course covers fundamental portfolio management with mean-variance optimisation and practical application of AI algorithms. Master walk-forward optimisation, hyperparameter tuning, and real-world portfolio management. Gain hands-on experience with live trading templates and capstone projects.

Course link:AI for Portfolio Management: LSTM Networks

File in the download

Steps to Create Thematic Universe for Portfolio Strategies Using GenAI - Python notebook

Login to Download

AbouttheAuthorAjay Pawar is a Quantitative Researcher and Analyst at Quantinsti, specializing in Computational Finance, Algorithmic Trading, Data Science, and Portfolio Management. In his prior roles at CRISIL, Axis Securities, BITA and HTTS, he has developed advanced quantitative tools, stock selection models, and algorithmic solutions. Ajay holds an M.Sc. in Financial Data Intelligence from Rennes School of Business, a B.Sc. Economics From Symbiosis School of Economics and is an EPAT (Executive Programm in Algorithmic Trading) Alumnus, He has several other certifications in Business Analytics and Data Science as well. His strong academic foundation and technical expertise make him a standout professional in quantitative finance.

---

*Imported from QuantInsti Blog on 2026-04-27*
