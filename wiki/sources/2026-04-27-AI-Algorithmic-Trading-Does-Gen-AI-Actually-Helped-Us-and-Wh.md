---
title: "AI + Algorithmic Trading: Does Gen AI Actually Helped Us (and What Wasted Time)"
author: "SetupAlpha"
source: "Substack"
url: "https://setup4alpha.substack.com/p/ai-algorithmic-trading-does-gen-ai"
date: "2026-04-27"
topics: ["systematic-trading", "algorithmic-trading"]
---

# AI + Algorithmic Trading: Does Gen AI Actually Helped Us (and What Wasted Time)

**来源**: [SetupAlpha](https://setup4alpha.substack.com/p/ai-algorithmic-trading-does-gen-ai)  
**日期**: 2026-04-27  
**作者**: SetupAlpha

---

## 摘要

AI + Algorithmic Trading: Does Gen AI Actually Helped Us (and What Wasted Time)
Generative AI in Algorithmic & Systematic Trading in 2025
SetupAlpha
Sep 24, 2025
4
1
2
Share
We wanted to see where AI actually saves research time for systematic traders (idea shaping, codes, papers etc) and where it quietly injects curve-fit risk and debugging debt.
Keep that question in mind. Because in practice, we saw both sides and the difference came down to how we used AI.
About us
We help traders and funds build robust, automated trading strategies/portfolios that save time and reduce stress without wasting years coding and research.
Explore our strategies
HERE
.
1.0
Context & Research
Hedge funds are all-in.
AIMA’s latest survey says 95% of fund managers are already using generative AI and 58% expect...

---

## 原文

AI + Algorithmic Trading: Does Gen AI Actually Helped Us (and What Wasted Time)
Generative AI in Algorithmic & Systematic Trading in 2025
SetupAlpha
Sep 24, 2025
4
1
2
Share
We wanted to see where AI actually saves research time for systematic traders (idea shaping, codes, papers etc) and where it quietly injects curve-fit risk and debugging debt.
Keep that question in mind. Because in practice, we saw both sides and the difference came down to how we used AI.
About us
We help traders and funds build robust, automated trading strategies/portfolios that save time and reduce stress without wasting years coding and research.
Explore our strategies
HERE
.
1.0
Context & Research
Hedge funds are all-in.
AIMA’s latest survey says 95% of fund managers are already using generative AI and 58% expect to lean on it more for investment processes next year. GPT‑4/ChatGPT is the default pick.
https://www.aima.org/article/press-release-front-office-gen-ai-adoption-shifts-from-if-to-when-for-leading-fund-managers-aima-research-finds.html
and
https://www.aima.org/article/press-release-getting-in-pole-position-how-hedge-funds-are-leveraging-gen-ai-to-get-ahead.html
Text returns isn’t fantasy.
Lopez‑Lira & Tang (2024) show ChatGPT’s news‑headline sentiment had
predictive power for next‑day returns
in their tests.
https://arxiv.org/abs/2304.07619
But coding reliability is a pain.
Even QuantConnect launched an in‑platform LLM assistant (Mia) because
general LLMs often miss platform‑specific details.
One user comment on their release:
“I’ve been using ChatGPT… it usually gets [QC‑specific code] wrong.”
Model choices are diverging.
Anthropic launched
Claude for Financial Services
(long‑context, doc analysis).
Perplexity grew as a financial research assistant.
We research
the
alpha
for the
retail
and
institutional traders.
Subscribe
A recent write‑up even compared
ChatGPT vs DeepSeek
on market prediction, with ChatGPT ahead in that test.
But next,, what happened when we used AI in a
RealTest
workflow ourselves.
Our Setup (RealTest + GPT): What We Wanted to Learn
We didn’t ask AI to “find alpha.” We asked it to
help us work
: draft scripts, speed up research, and generate clean variants to test (filters, position sizing, timing). The question:
does AI reduce grind time without increasing our error rate?
If AI can shave hours without adding fragility, that’s real value. If it pushes us into debugging rabbit holes, it’s a net negative.
The Backtest
We ran a series of hands‑on trials where we prompted GPT to write or modify RealTest strategies.
What happened, repeatedly:
Sometimes it nailed it.
We pasted the AI’s RealTest code and it ran. Huge time saver.
Sometimes it failed hard.
The draft wouldn’t run (syntax/logic issues) or missed obvious platform specifics (e.g., index membership filters / survivorship safeguards we always apply).
Sometimes it mixed languages.
GPT output
RealTest + Python hybrids
in one go (e.g., Python functions inside a RealTest block). That broke the flow and sent us into cleanup mode.
Net effect:
our role drifted from research/backtesting to
debugging AI‑written code
, exactly what we didn’t want. We saved time on drafting, then spent it (and more) on fixing.
This matched what the broader community reports: LLMs are amazing at scaffolding, but platform‑specific glue is where they stumble.
Keep this in mind, because in the next section you’ll see how we changed our prompts and process to flip the cost/benefit back in our favor.
What Worked for Us
These adjustments made AI genuinely helpful and cut the rework:
Single‑language outputs.
We now force prompts to return RealTest only (no Python) or Python only never both.
Platform checklists.
We keep a mini‑checklist in the prompt: “Use index‑membership filters (avoid survivorship), realistic costs, and no look‑ahead.” AI won’t always obey, but the hit rate improves.
Diff‑based edits.
Instead of “write a strategy,” we ask: “Here’s the RealTest script. Propose a minimal diff to add a 200‑day trend filter and position cap.” Less room to hallucinate.
Variant burst, then validate.
We let AI generate 3–5 variants (filters/position sizing/timeframes) and then we do the
robustness work
ourselves:
out‑of‑sample splits, parameter sweeps, Monte Carlo on trade sequences, stress periods.
Use specialist tools for research.
We use
Perplexity
for fast research with citations and
Claude
for long PDF/transcript digestion. Then we decide, in RealTest, what’s worth testing.
Result: AI became a
junior quant assistant
again, not the driver of our day.
Interpretation
AI saves draft time
but
increases review time
unless you constrain it. The balance flips to positive when you keep outputs narrow and ask for small diffs.
AI won’t fix drawdowns
or cure curve fitting. That still comes from discipline: walk‑forward, Monte Carlo, out‑of‑sample.
Where AI shines:
idea throughput, documentation, and boilerplate. It’s great at
“what if we add X filter?”
and at summarizing dense research so you can test the one thing that matters.
Where it hurts:
mixed‑language output, platform‑specific misses, and false confidence. If you don’t know what to check, you’ll ship fragile code faster.
The Bigger Picture
The institutional pattern is clear: use AI as
co‑pilot
, not oracle. Funds are embedding it in research and coding workflows, but humans own validation and risk. (AIMA surveys above; etc)
For RealTest users, that translates to a simple operating rule:
Use AI to accelerate. Never to outsource robustness.
That mindset gave us the benefits (speed, breadth) without (hidden bias, broken code, wasted hours).
Closing
We wanted to know whether AI actually helps RealTest traders. Our answer, after real trials:
yes if you constrain it.
Force single‑language outputs, use platform checklists, ask for diffs, and keep your validation gauntlet. Do that, and AI becomes the assistant that lets you test more, learn faster, and keep your equity curves saner.
This is the type of work we do every day at
SetupAlpha
. Our mission is simple: give RealTest users robust strategies they can trust, without wasted time or curve-fit illusions. If you’re ready to add proven systems to your portfolio, you’ll find them here:
https://setupalpha.com/collections/realtest-strategies-and-backtests
Research you’ll actually want to read.
Subscribe
References & Further Reading
AIMA 2025 press release: 95% of fund managers now use GenAI and usage is rising:
https://www.aima.org/article/press-release-front-office-gen-ai-adoption-shifts-from-if-to-when-for-leading-fund-managers-aima-research-finds.html
AIMA 2024 survey overview:
https://www.aima.org/article/press-release-getting-in-pole-position-how-hedge-funds-are-leveraging-gen-ai-to-get-ahead.html
Federal Reserve: LLMs can classify FOMC minutes topics accurately:
https://www.federalreserve.gov/econres/notes/feds-notes/using-generative-ai-models-to-understand-fomc-monetary-policy-discussions-20241206.html
ChatGPT news‑headline sentiment predicts next‑day returns (Lopez‑Lira & Tang):
https://arxiv.org/html/2304.07619v5
QuantConnect “Ask Mia” announcement + user feedback:
https://www.quantconnect.com/announcements/15995/ask-mia-interactive-ai-llm/
and docs:
https://www.quantconnect.com/docs/v2/ai-assistance/mia-chatbot
Claude for Financial Services (document & data analysis workflows):
https://www.anthropic.com/news/claude-for-financial-services
MarketWatch summary: ChatGPT vs DeepSeek market‑prediction study:
https://www.marketwatch.com/story/a-chinese-paper-finds-chatgpt-not-deepseek-can-generate-stock-market-returns-but-the-key-insight-doesnt-have-anything-to-do-with-ai-ae3c9e5f
Share
4
1
2
Share

---

*由 Substack Strategy Tracker 自动抓取*

---

*Imported from Substack on 2026-04-27*
