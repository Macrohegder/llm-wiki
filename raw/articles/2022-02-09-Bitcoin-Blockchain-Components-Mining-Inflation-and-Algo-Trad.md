---
title: "Bitcoin Blockchain: Components, Mining, Inflation and Algo Trading"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/bitcoin-blockchain/"
date: "2022-02-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Bitcoin Blockchain: Components, Mining, Inflation and Algo Trading

**来源**: [QuantInsti](https://blog.quantinsti.com/bitcoin-blockchain/)  
**日期**: 2022-02-09  
**作者**: QuantInsti

---

## 原文

Bitcoin Blockchain: Components, Mining, Inflation and Algo Trading

ByUdisha Alok

In the previous blog, we exploredblockchaintechnology and its various components. Now, we delve further into a specific application of this technology which is probably the most well-known - Bitcoin. The Bitcoin blockchain has got everyone hooked to this technology.

We will discuss the components of the Bitcoin blockchain, the different exchanges that it is traded on, and look at a Bitcoin trading strategy in Python. So without further ado, let's get started!

We will be covering the following topics:

Bitcoin, the first blockchain

Bitcoin components

Bitcoin mining and Proof of Work

Transaction fee

Bitcoin and inflation

Trading Bitcoin using a crossover strategy

Bitcoin, the first blockchain

Once upon a time, in a trustless world of paper and plastic money and coins ruled by financial institutions, a blockchain named Bitcoin was born. It vowed to set the world free from the clutches of central power figures and make it a trust-free world where we could transact with strangers without the need for any trust.

Bitcoin is the most popular digital currency created by the mysterious person(s), Satoshi Nakamoto, in 2008, but it was not the first one.Ecashwas created by David Chaum back in 1983, andhashcashwas proposed in 1997 by Adam Back to counter spam-mail based on a proof-of-work scheme.

In 2004, Hal Finney further developed the hashcash into a reusable proof-of-work (RPOW), the first public implementation of a server designed to allow users throughout the world to verify its correctness and integrity in real-time.

The earlier proposals for distributed cryptocurrencies likebit goldby Nick Szabo (2005) andb-moneyby Wei Dei (1998) inspired the creation of Bitcoin. And the rest, as they say, is history.

Today exists the modern form of the Bitcoin blockchain, that owes it's present form to these events.

Bitcoin components

The shared ledger

The Bitcoin blockchain contains a very specialized type of data- simple transactional data about who paid whom and how much. However, the data is stored in Bitcoin in a way that the number of Bitcoins in the input of a transaction is equal to the number of Bitcoins in its output.

Each input refers to the previous transaction where the sender of this transaction received the coins. So each input will refer to an earlier transaction keeping track of each Bitcoin. This model is called the UTXO (Unspent Transaction Output) model.

Let us look at how the UTXO model works using this simplified diagram:

There are some transactions where the coins are generated ('mined') by the system. These transactions are called the Coinbase transactions, and they will not refer to any previous transactions as, in this case, the coins have come out of thin air, so to say.

Every block will have one coinbase transaction, which will have a single blank 'input'. Usually, the first transaction in each block is reserved for the coinbase transaction.

The nodes

Bitcoin is a public blockchain. It means that anyone can join the Bitcoin network and view the entire Bitcoin blockchain. Some of these nodes may take up 'mining' by competing to 'mine' the blocks for a reward.

The consensus algorithm

As discussed in our earlierblog, a consensus algorithm is simply the decision-making mechanism for a group. As the Bitcoin blockchain is a public blockchain with the largest number of nodes, a consensus algorithm becomes essential.

This is mainly to resolve the following issues:

Prevent malicious attacks

Solve the problem of double-spending

Decide which node will add the next block to the chain

Ensure the integrity and consistency of the blockchain

The consensus protocol used by Bitcoin is the Proof-of-Work (POW). Simply put, to add a block to the blockchain, all nodes compete to solve a cryptographic puzzle. This puzzle is computationally extensive, and a lot of energy goes into solving it.

So all the nodes have to 'work' on it. It makes it difficult for an attacker to mimic multiple nodes because the cost of setting up another mining node is considerable.

The first node to solve the cryptographic puzzle gets to add the next block to the chain as it shows the 'answer' as its proof-of-work and is rewarded with some Bitcoins (coinbase transaction). In the case of two versions of the chain getting created due to two nodes mining a block simultaneously, the longest chain is selected as the valid chain.

Interestingly, Nakamoto mined the first Bitcoin block with a reward of 50 Bitcoins, and Hal Finney (inventor of RPOW) became the recipient of the first Bitcoin transaction of 10 Bitcoins from Nakamoto.

Bitcoin Mining and Proof of Work

The Proof-of-Work (PoW) algorithm is designed so that one block is mined every 10 minutes. In order to ensure this time limit, the network sets a difficulty level for the puzzle.

The difficulty level is set by setting a target for the final hash of the block. In the case of Bitcoin, it means specifying the number of leading zeroes in the final hash of the block.

Now each node has the hash of the previous block and the current block of transactions. They need to calculate the nonce (a number used only once), which generates a hash with the given number of leading zeroes when combined with the above values.

When one leading zero is added to the target hash, the work is doubled, increasing the problem's difficulty. The Bitcoin network automatically configures the problem so that it takes approximately ten minutes to mine each block.

The first miner who finds a valid nonce (golden nonce) is rewarded, and the nonce is broadcast to the network for validation. The block is added to the Bitcoin blockchain after verification.

Mining a block is computationally-expensive work, so sometimes a group of miners come together and form a mining pool to increase their chances of mining a block.

Transaction fee

When miners mine a block, they receive a reward. They also get transaction fees which is a sum of the transaction fees for all the transactions in the block. The transaction fees incentivize the miners to continue to process the transactions by mining blocks. Else they may not continue to mine the blocks due to the high mining costs.

It is not mandatory for miners to pick up the transactions on a first-come-first-serve basis in the Bitcoin network. So the miners are free to choose the transaction they want to add to a block.

A block can hold only a finite number of transactions- each block size has a soft limit of 1MB. A higher transaction fee will make the transaction more attractive for a miner. Hence, a higher transaction fee block is more likely to get mined and added to the blockchain sooner than one with a lower transaction fee.

Note that a transaction becomes valid only once it is added to the blockchain. You can think of it as a simple money transfer transaction that remains in the processing stage unless the bank confirms it.

Bitcoin transaction fees depend on the network traffic. If more people are using the blockchain, the number of transactions to be confirmed goes up, pushing the transaction fees higher.

Bitcoin transaction fees depend on the network traffic. If there are more people using the blockchain, the number of transactions to be confirmed goes up, pushing the transaction fees higher.

Bitcoin and inflation

Nakamoto designed Bitcoin as a deflationary cryptocurrency. The logic behind this was that fiat currencies are in infinite supply as more and more money keeps getting added to the system by the central banks and governments, leading to a decrease in the value of money over time. This is inflation.

To counter this, Nakamoto capped the total number of Bitcoins that will be created at 21 million. So, like gold, Bitcoins supply will decrease over time and hence become scarcer, increasing their price.

After every 210,000 blocks are mined, the block reward is halved until it becomes nearly zero in 2140. It is currently 6.25 coins per block. As the block rewards continue to reduce, the transaction fees may be the primary incentive for miners.

Trading Bitcoin using a crossover strategy

Due to the rise in the popularity of cryptocurrency, Bitcoin is traded on many exchanges. Some decentralized exchanges even allow the users to remain pseudonymous, not asking them to reveal any personal information.

To enhance your trading skills, consider exploring acrypto trading coursethat covers key strategies and the use of indicators like RSI, Aroon, and Ichimoku Cloud.

Some of the top exchanges where Bitcoin is traded are:

Binance

Coinbase exchange

Crypto.com exchange

Kraken

Kucoin

Gemini

Bitcoin is a volatile market where there is always momentum. It makes sense to try out a momentum-based strategy in such markets.

We will build amomentum-based trading strategyfor Bitcoin using theAwesome Oscillator(AO) technical indicator. AO calculates the difference between a short term (usually 5) and a long term (usually 34) Simple Moving Average.

This SMA is calculated using the mid-point of each bar instead of the closing prices. Here is the code for this strategy:

df.head()

You can also use other technical indicators like theIchimoku cloudto trade on Bitcoin. To know more about algorithmic Bitcoin trading, clickhere.

Conclusion

Diving into the world of blockchain technology, this blog in the series dealt with Bitcoin blockchain. We explored the history of Bitcoin, its various components, Bitcoin mining, and transaction fees. We also looked at amomentum trading strategyusing the Awesome Oscillator technical indicator.

I hope you are excited to venture further into the world of cryptocurrencies. In our next blog in this series, we will explore the cryptocurrency that ushered another significant change in the world of crypto - Ethereum. Till then, keep reading!

Disclaimer: Any information regarding cryptocurrency in this article is intended to convey general information only. This article does not provide investment, legal, tax, etc. advice. You should not treat any information in this article as a call to make any particular decision regarding cryptocurrency usage, legal matters, investments, taxes, cryptocurrency mining, exchange usage, wallet usage, etc. We strongly suggest seeking advice from your own financial, investment, tax, or legal adviser. Neither QuantInsti®nor the author of this article accept responsibility for any loss, damage, or inconvenience caused as a result of reliance on information published in, or linked to, from this article.

---

*Imported from QuantInsti Blog on 2026-04-27*
