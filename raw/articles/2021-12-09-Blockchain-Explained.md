---
title: "Blockchain Explained"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/blockchain/"
date: "2021-12-09"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Blockchain Explained

**来源**: [QuantInsti](https://blog.quantinsti.com/blockchain/)  
**日期**: 2021-12-09  
**作者**: QuantInsti

---

## 原文

Blockchain Explained

ByUdisha Alok

Blockchain has been a topic of interest in various circles for some time now. It keeps popping up in multiple discussions and varied contexts - and for a good reason!

As per a recentreport, the blockchain market size is projected to grow from USD 4.9 billion in 2021 to USD 67.4 billion by 2026, at a Compound Annual Growth Rate (CAGR) of 68.4% during the forecast period.

The blockchain is like a magical genie with seemingly infinite powers, and it is impossible to cover everything about it in just one article. Let us try to put this genie in a bottle by looking briefly at what the blockchain is and what makes it disruptive.

Here are some of the things we will be talking about in this article.

Internet of Value

What is Blockchain?

Components of a Blockchain

Strengths of Blockchain

Applications of Blockchain

Challenges of using Blockchain

Internet of Value

Before we get started on the topic of blockchain, let us first look back at another technology that held a similar promise of decentralisation, accessibility and anonymity that the blockchain lures us with - the internet.

The advent of the internet heralded a new era for humankind, so much so that it is difficult to imagine existence without it. Communicating and interacting with a person across the globe, the freedom of sharing one's views, opinions and creativity with a broader audience, accessibility to a whole new world of technology at minimal costs- the benefits of the internet are massive.

This was the Internet of Information - designed to transfer information, not things of value like money or property rights; at least not without a third party like a bank, Paypal, or the government.

But are we really anonymous when we post anything on the web?

In recent times, it is evident that the actions on the internet are closely monitored. By offering us free accounts and services, major companies have been collecting essential bits of information regarding us. Information about our marital status, income, places we visit, things we buy, websites we spend more time on, likes and dislikes, our friends, our political and religious inclinations, etc.

Bit-by-bit, they are building a digital persona of each of us that may ultimately sound more authentic than ourselves- would you remember the restaurant you went to five years back on this day or the dish you 'absolutely loved' that day? The digital persona will!

One of the benefits of the internet is to be able to share information freely with anyone. When you take a selfie and share it with a friend, you share a copy of it. So you can share it with any number of people and still have the original with you. So the internet, as it is now, cannot be used to share anything of value, like money.

But what if you could use the internet to share assets too? What if you could track each asset, like a work of art or money, and send it to a friend using the internet?So that the multiple devices powered by the internet, not just communicate with each other, but also purchase their electricity maybe?

This is Internet 2.0 -the Internet of Value.

What is Blockchain?

A blockchain essentially is a database that is distributed across multiple nodes/computers. It is made up of 'blocks' of information, and each block is 'chained' to its previous block. Blocks? Chains? Let’s break it down further.

Blocks, chains and hashes

A block is made up of several records, like a table in a regular database or a spreadsheet. But what makes it different from a traditional database is that each block is connected or chained to the previous block. We will see how this 'chaining' happens in a while.

Now, before we move any further, let us briefly touch upon what a hash is. Just like fingerprints are used to identify human beings, a hash is a string of seemingly random numerical values that represents any file - an image, text, audio, etc. Every time you create a hash of a file - you will get the same value.

However, even a minor modification to the file, be it whitespace, or even a comma, will change the hash.

There are different types of hashing algorithms, but the one usually used in blockchain is SHA256. Here, SHA means Secure Hash Algorithm.

In Python, we can use the 'hashlib' module to generate hashes for a file/string. This module supports many different types of hashing algorithms.

sha1 algorithm is available.
sha3_256 algorithm is available.
shake_256 algorithm is available.
blake2b algorithm is available.
sha3_512 algorithm is available.
sha256 algorithm is available.
sha384 algorithm is available.
md5 algorithm is available.
sha224 algorithm is available.
sha3_224 algorithm is available.
shake_128 algorithm is available.
sha512 algorithm is available.
blake2s algorithm is available.
sha3_384 algorithm is available.

Here is an illustration of generating a SHA256 hash for a string in Python, and how the hash changes with tiny changes in the string.

The hash for Hello World! is 7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069.
The hash for Hello World is a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e.
The hash for hello World! is e4ad0102dc2523443333d808b91a989b71c2439d7362aca6538d49f76baaa5ca.
The hash for hello world! is 7509e5bda0c762d2bac7f90d758b5b2263fa01ccbc542ab5e3df163be08e6ca9.

As we can see above, even a minor change in the string leads to a different hash.

Each block contains the data for that block along with the hash of the previous block. For the first block of the chain, called the ‘Genesis’ block, the value of the previous hash is a string of all zeros.

The second block contains the hash of the genesis block and the data, and the third block contains the hash of the second block and data, etc.

Here is an example of a simple blockchain in Python:

Data for this block is:
Sender: Sender1
Receiver: Receiver1
Amount: 1000
Block number 1 is added to the blockchain.
Its hash is dc19a1fa6ece23fec46ba93c14ea351bf0eea7246e7051bd493727109bd3fc22.
Hash of previous block is 41bc2398bddbf8813f63c1f33e936982770a97388f01f58e0558ca9ad8abbd93.Data for this block is:
Sender: Sender2
Receiver: Receiver2
Amount: 2000
Block number 2 is added to the blockchain.
Its hash is faa7596e965277014878f3c1016f4c55af75524f06972c6f0c0830fd70fcb798.
Hash of previous block is dc19a1fa6ece23fec46ba93c14ea351bf0eea7246e7051bd493727109bd3fc22.Data for this block is:
Sender: Sender3
Receiver: Receiver3
Amount: 3000
Block number 3 is added to the blockchain.
Its hash is 9353c830b5fdfc1534ddd4c459d5aa7cef9f187c578fed68ca149f590cefcb82.
Hash of previous block is faa7596e965277014878f3c1016f4c55af75524f06972c6f0c0830fd70fcb798.Data for this block is:
Sender: Sender4
Receiver: Receiver4
Amount: 4000
Block number 4 is added to the blockchain.
Its hash is 17d753bb661639ef1ff95664d51a19d183a718c55824436eefe380ba693b5e0f.
Hash of previous block is 9353c830b5fdfc1534ddd4c459d5aa7cef9f187c578fed68ca149f590cefcb82.Data for this block is:
Sender: Sender5
Receiver: Receiver5
Amount: 5000
Block number 5 is added to the blockchain.
Its hash is 31421253ef41c82bb65fb46cc95933016c608cd4c46b27d8a670f89637694673.
Hash of previous block is 17d753bb661639ef1ff95664d51a19d183a718c55824436eefe380ba693b5e0f.Data for this block is:
Sender: Sender6
Receiver: Receiver6
Amount: 6000
Block number 6 is added to the blockchain.
Its hash is affaaf4e8589071fda3b9229a96fcd4515934a48e72822106998492c9e092694.
Hash of previous block is 31421253ef41c82bb65fb46cc95933016c608cd4c46b27d8a670f89637694673.Data for this block is:
Sender: Sender7
Receiver: Receiver7
Amount: 7000
Block number 7 is added to the blockchain.
Its hash is c982a9bdd32d4f39ae1a9cf7a4db3433dbbb69aa79fd3c6324c0a1bc6288d6c2.
Hash of previous block is affaaf4e8589071fda3b9229a96fcd4515934a48e72822106998492c9e092694.Data for this block is:
Sender: Sender8
Receiver: Receiver8
Amount: 8000
Block number 8 is added to the blockchain.
Its hash is 3294043edb16abe51417fd1ba2d3ecdc497d11c897fdcbc96d6edc8ada661c26.
Hash of previous block is c982a9bdd32d4f39ae1a9cf7a4db3433dbbb69aa79fd3c6324c0a1bc6288d6c2.Data for this block is:
Sender: Sender9
Receiver: Receiver9
Amount: 9000
Block number 9 is added to the blockchain.
Its hash is eb21c2beb4405f91a075a564c5c276ab061a6c5e8b0c18d3e3135df265e49e3b.
Hash of previous block is 3294043edb16abe51417fd1ba2d3ecdc497d11c897fdcbc96d6edc8ada661c26.Data for this block is:
Sender: Sender10
Receiver: Receiver10
Amount: 10000
Block number 10 is added to the blockchain.
Its hash is dc512044c05d96a74fe97b27c374f1eefe0aa7e70dceaacedc691e35eee212f3.
Hash of previous block is eb21c2beb4405f91a075a564c5c276ab061a6c5e8b0c18d3e3135df265e49e3b.

Now, if any of the blocks are modified, the hash for that block will change, and it will not be consistent with the value of the previous hash in the next block. Hence the chain will be broken!

How it all comes together

In the previous section, we saw how data is stored on a blockchain. But you may wonder what makes this any different from any other database. Let us now understand the blockchain’s properties that give it the edge over other technologies and make it disruptive.

A blockchain is a distributed ledger. The data on the blockchain is a set of transactional records. Each block is timestamped. Once the data is recorded on the blockchain in the form of a block, it is broadcast to all the nodes. So a copy of the ledger will reside at each of the nodes in the network.

In case any node gets corrupted, the data is updated using the remaining peer nodes. As we have seen earlier, once recorded, the data cannot be altered or changed as it will cause the remaining nodes to become invalid.

Hence, a blockchain is immutable - it is animmutable,distributedledger.

Components of a Blockchain

Let us look at the components of a typical blockchain to understand how it works.

A shared ledger

As we saw earlier, the block is the data structure used to record the data in a blockchain. The blocks are chained to the preceding blocks and organized chronologically. This blockchain is a digital ledger that records all the transactions on a blockchain network, shared with all the nodes.

The nodes

Many computers are a part of the blockchain network. Addition to this network may be voluntary or based on some rule- for example, a banking blockchain network may allow only banks to join. Each node maintains a current updated copy of the ledger.

The consensus algorithm

Let us imagine a meeting where the person who comes and stands on the dais gets a reward. Only one person is allowed to stand there. Can you imagine the chaos that will follow? Everyone will fight to be the one at the dais.

But what if a question is asked and the first one to answer that question comes to the stand? Or maybe each person can submit a list of attendees who support her and vote for her to take the stand?

In each of these situations, we can reach a consensus without arguments.

Blockchain technology applies a similar principle. In the case of a peer-to-peer network such as a blockchain, a consensus algorithm (or a consensus protocol) is used to decide which node will add the next block to the blockchain because the node doing it will be rewarded.

Every time a new block is to be added, the nodes compete as per the consensus algorithm, and the winning node gets to add the block to claim the reward. These nodes are calledminers.

In a generic context, the consensus algorithm may be thought of as a methodology to adjudicate who decides the current state of the blockchain. It is a way to establish trust between independent parties. That is why the blockchain is also sometimes referred to as the 'trust protocol.'

Different blockchain networks may use different consensus algorithms. For example, Bitcoin usesProof-of-Work (PoW), where the miners compete to solve a complex mathematical problem and the node that solves it first gets to add the block and claim a reward.

Proof-of-Stake (PoS)is the consensus algorithm used by Ethereum wherein the nodes are required to lock some coins (usually more than the cost of the block to be added) with the system, and the winner is decided based on the size of the stake.

There are many otherconsensus algorithmslike:

Proof-of-Capacity,

Proof-of-Burn (PoB),

Proof-of-Elapsed Time, and

Practical Byzantine Fault Tolerance (PBFT), etc.

Strengths of Blockchain

Let us now look at some of the superpowers of blockchain technology that make it so disruptive.

Security

What gives blockchain its super-strength is the Public Key Infrastructure (PKI). PKI is used to implement data encryption and authentication on the blockchain, making it completely secure. It also makes it pseudonymous.

So each user can have a public key (like your UPI id or your bank account number). It is known to everyone, and anyone can send an asset to her using it. Similarly, each user also has a private key (like your ATM or UPI PIN) which she can use to authorize a transaction from her end. The private key is secret, and no one except the user should know it.

This makes it simple to identify a user unequivocally on the blockchain network using her public key without revealing complete information about her. Hence the privacy of the user is preserved, and the authenticity of the transaction is confirmed.

All this without a third party acting as an intermediary!

Affordability

The transaction costs go down as the need for an intermediary is eliminated. Micro-transactions are possible, and the location of the sender and receiver do not matter anymore. The internet promised to be inclusive, but the fact remains that many people globally still do not have access to the internet. Blockchain goes a step further.

While Bitcoin (the first application of blockchain technology) was designed to work on the internet, it can operate without it if needed. A person can access the blockchain through a Simplified Payment Verification mode that works on cell phones. It allows a person with a simple mobile handset to be a part of the blockchain- without the need for an identity or even a bank account.

In fact, the Australian micropayment service mHITS (Mobile Handset Initiated Transactions) has launched a service allowing users to buy international mobile top-up using Bitcoin by just sending a text message.

Transparency

A copy of the ledger resides with each node of the network. So the data is there for anyone to see. Each transaction is time stamped and signed digitally using the private key of the sender. Hence, it is easy to track the movement of the asset along the blockchain.

Also, if a change in protocol is to be made, the majority of the nodes have to agree for it to be implemented.

There is no central authority to change the rules- no central bank or government to pass a law so that suddenly all the currency notes you hold in your wallet mean nothing more than coloured paper.

Immutability

Once a block gets added to the chain, there is no going back. It is 'set in stone'. No one can come and fudge the books or meddle with the ledger. The chaining of the block, coupled with the cryptography and the consensus algorithm, makes it nearly impossible for a malicious attacker to attack or change the data.

Traceability

Each transaction is recorded immutably in the blockchain and signed cryptographically. So the audit trail makes it easier to trace the movement of any asset across the network.

Applications of Blockchain

I hope that you can appreciate how impressive blockchain technology is. It holds promise to change the way we think, alter the way we do business, modify the concept of trust in transactions, and so much more.

Let us now look at some areas where blockchain can make, or is already making, an impact.

Financial transactions

This is probably the most well-known use case of the blockchain. In fact, the term blockchain is used almost synonymously with Bitcoin, perhaps because Satoshi Nakamoto (the founder of Bitcoin) used the terms' block' and 'chain' in his 2008 paper on Bitcoin.

But Bitcoin is just the first use case of blockchain technology. Many cryptocurrencies have followed- Ethereum, Ripple, Monero, Cardano, etc. Exchanges like NASDAQ, Korea Exchange, Moscow Exchange Group, Luxembourg Stock Exchange, etc., have already started implementing blockchain technology. You can read more about how blockchain is changing stock marketshere.

Blockchains make micro-payments possible and eliminate the need for a third party. They also make the transactions pseudonymous, so even people without identities can make transactions.

Tokens built on blockchains are being used as virtual currencies for investment and economic purposes. You can get more information on cryptocurrency walletshere.

Smart Contracts

Smart contracts are agreements between two or more parties, with a mutually-agreed set of well-defined conditions that execute automatically.

Let's take an example- my friend and I bet on the outcome of a cricket match. We fix that the information from a particular website would be considered authentic and used to confirm the match's outcome.

So both my friend and I deposit our share of money with the system, and the person who wins the bet gets the whole amount automatically based on the match outcome, as per the agreed website. Of course, this is probably too much diligence in case of a simple bet between two friends.

But what about a wager between two strangers across the globe who do not have an existing relationship making it impossible to have a basis of trust without involving a third party as a mediator.

Imagine more complicated business scenarios:

A musician putting up all the details regarding her latest song on the blockchain with smart contracts with a music company.

She allows the company to use her song as per some clearly-defined and mutually -agreed conditions for a certain period, subject to the receipt of a certain percentage of the sales as a royalty.

Her account gets auto-credited every month based on the sales of her records that can be tracked on the blockchain network, and the penalty is paid immediately if either party violates any clause.

Ah, a world without the need for lawsuits for violation of contracts! No police and government to ensure that everyone follows the rules! Sounds utopian, right?

Self-sovereign identities

The proof of our existence lies in the birth certificates issued by the local authority. The evidence of our employment are the identity cards issued by our employer. The certificate of our earning and driving ability are the documents issued by the relevant authorities.

We are, in essence, nothing but a set of records in different databases created by various entities!

We need a trusted third party to certify our existence authentically. But what if you lose all your documents- as in the case of an immigrant.

Relief workers are now working on blockchain projects that can help create identities for such people. A blockchain can help create an authentic unequivocal identity for anyone.

Now you don't have to get your identity certified by a third party. You don't need to divulge all your personal information to get that identity and then have that information used for all sorts of things behind your back. You should control how much information you want to reveal and sell it for money if you wish!

If information is power, you should control who gets it from you and how much.

Supply chain management

If the transactions are recorded on the blockchain at each step of the process, it will make the entire supply chain more transparent.

The producers would be paid fairly without any middlemen and can track the whole journey of their produce. The consumers can be sure of the origin and quality of the products they purchase. There will not be any fake products being sold, no more counterfeit vaccines and medicines from the black market. A win-win situation!

As we can see, due to the strengths lent by the very structure of blockchains, they have applications in many areas of our life, be itmusic,solar energy,real estate, etc.

Challenges of using Blockchain

Blockchain technology has huge potential. It's like Thor's hammer. But we don't want to use it to hammer a nail in the wall because the strengths of the blockchain are powered by heavy energy-intensive technology.

Some challenges that blockchain presents are as follows:

Each node of a blockchain maintains a copy of the ledger, but this immutability comes at the cost of redundancy.

The consensus algorithms like proof-of-work need a lot of computing power - a lot of energy goes into adding each block to the blockchain.

Then comes the challenge of digitally signing items on the supply chain. You can stamp the hash of an automobile part onto the metal, but how will you mark the tomatoes and apples? Here we have to depend on manual intervention to enter the data, which affects the efficiency of the system.

Also, if we use the blockchain as an immutable encrypted storage of important records like birth certificates or driving licenses, the authenticity of the records is still certified by a third party.

Conclusion

The blockchain is a powerful technology that provides a great solution to problems that require decentralization, immutability, and security. So before we think of implementing a blockchain solution, let us first think if these are essential aspects of our problem. Let us focus on solving the problem and not finding a blockchain solution to it.

I hope you enjoyed reading about blockchain technology and its potential to transform the world as we know it. This blog is just a window into the promised world of blockchain, and I hope it gets you started on your journey to explore it further.

Stay tuned for more articles on the aspects of this topic in the coming weeks. Together, we will explore some of the prominent cryptocurrencies in the next blogs in this series. Keep reading!

If you too wish to dive deeper into the world of cryptocurrencies and explore trading opportunities in cryptocurrency, leverage your knowledge of blockchain with Quantra's intermediateCrypto Trading Course. Enroll now!

Disclaimer: All investments and trading in the stock market involve risk. Any decision to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

---

*Imported from QuantInsti Blog on 2026-04-27*
