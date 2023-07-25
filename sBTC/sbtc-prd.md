# sBTC Product | Requirements Document

> Detailed Technical Specifications Document can be found [here](sbtc-tsd.md).

> Detailed Product Requirements Document for sBTC Signer can be found [here](sbtc-signer-prd.md).

## Executive Summary:

> 👉 _At a high-level what is sBTC - its purpose, target audience, and benefits?_

sBTC is a digital asset that lets you move Bitcoin in and out of the Stacks blockchain. With sBTC, you can use Bitcoin in Clarity smart contracts, which enables decentralized lending, decentralized exchange, and BTC-backed stablecoins.

sBTC is a SIP-010 token on the Stacks chain, backed 1:1 against BTC, and operated by a decentralized open set of members. It serves the purpose of enabling BTC holders to engage in smart contracts without the need for a trusted third-party. As a non-custodial digital asset, sBTC facilitates seamless movement of Bitcoin between the Bitcoin L1 and the Stacks blockchain. When BTC is locked on the Bitcoin L1, an equivalent amount of sBTC is issued on the Stacks layer, ensuring a constant 1:1 backing to BTC's value.

By leveraging sBTC, Bitcoin can be effectively utilized in Clarity smart contracts, unlocking various possibilities, including decentralized lending, decentralized exchange, and the creation of BTC-backed stablecoins. This capability plays a crucial role in scaling Bitcoin and introducing innovative functionalities to users, enhancing the overall potential of the ecosystem.

## Problem Statement:

> 👉 _What specific problem does sBTC solve?_

Bitcoin's limited expressiveness makes it unsuitable for most decentralized applications. This leaves users with no options to use financial applications like lending and derivatives trading without entrusting their Bitcoin to centralized entities. This exposes them to counterparty risk, resulting in billions of dollars in lost funds.

Bitcoin, being the most secure and decentralized blockchain with the largest market cap, faces limitations in its scripting system, making it challenging for developers to build applications directly on its chain. The lack of expressiveness in Bitcoin's smart contract language has led developers to seek alternative ecosystems with greater flexibility and tooling.

As a consequence, there is a significant unmet demand for using Bitcoin in various decentralized financial applications, including lending and derivatives trading. However, existing solutions require users to entrust their Bitcoin to centralized entities, exposing them to counterparty risks and substantial financial losses. This centralization contradicts the fundamental principles of Bitcoin and hampers its potential to unlock new functionality and scalability for users.

The problem at hand is to create a solution that enables secure and decentralized movement of Bitcoin in and out of the Stacks blockchain, providing fully decentralized and scalable applications for the Bitcoin currency. The goal is to implement a protocol, sBTC, that allows BTC holders to participate in smart contracts without relying on trusted third parties, ensuring the continuous backing of 1:1 BTC value to sBTC. By addressing these challenges, sBTC seeks to open up opportunities for Bitcoin in DeFi, enhancing its utility and accessibility while preserving the core principles of decentralization and self-sovereignty.

## Solution:

> 👉 _How does sBTC provide a solution to the identified problem?_

sBTC is a protocol enabling secure movement of Bitcoin in/out of the Stacks blockchain for fully decentralized, scalable Bitcoin applications. It implements the SIP10 token standard and is managed by a decentralized group of signers, known as Stackers, on the Bitcoin main chain.

By bringing a representation of BTC to the Stacks blockchain, sBTC presents a revolutionary protocol that addresses the problem of limited expressiveness in the Bitcoin scripting system. This solution enables fully decentralized and scalable applications for the Bitcoin currency, unlocking new possibilities in the DeFi space.

The sBTC protocol ensures a secure transfer of Bitcoin between the Stacks blockchain, providing users with a non-custodial digital asset that maintains a 1:1 backing to BTC's value. A decentralized group of signers, known as Stackers, safeguards the Bitcoin wallet, and users can deposit BTC into this wallet while proving the transaction on the Stacks blockchain.

With this deposit, sBTC tokens are minted, and users can seamlessly transact using Clarity smart contracts offered by the Stacks blockchain. Users also have the freedom to redeem sBTC for the underlying BTC at any time, with the signers executing the transaction to the user's specified address.

The transparent Stacks blockchain allows for verification of the 1:1 BTC to sBTC ratio, enhancing transparency compared to custodial approaches like WBTC. Additionally, the management of the Bitcoin script/wallet on the Bitcoin main chain is decentralized and open, involving multiple participants rather than a single entity or fixed federation. This ensures a more resilient and trustworthy system, where signers are economically incentivized to execute peg-out transactions efficiently.

Overall, sBTC's innovative protocol not only addresses the limitations of the Bitcoin scripting system but also provides a secure and decentralized solution for utilizing Bitcoin in various DeFi applications, aligning with the principles of self-sovereignty and economic freedom.

## Product Requirements:

> 👉 _What are the features, functionality, and characteristics of sBTC?_

sBTC implements the SIP10 token standard and enables the minting, burning, locking, and unlocking of sBTC tokens. The Peg-in sBTC Signer API facilitates the signing of peg-in requests by Stackers to approve the transfer of Bitcoin into the sBTC system.

### **sBTC Asset**

sBTC implements the SIP10 token standard, using a special implementation designed to keep 1:1 parity with Bitcoin. In addition to standard SIP10 functions, the focus of this contract is to mint, burn, lock, and unlock sBTC tokens as mandated by the sBTC protocol.

### **Deposits - Minting sBTC**

1. A user submits Bitcoin to a P2TR deposit address.
2. Stackers then need to spend that Bitcoin within a specific timeframe and move it to the threshold wallet address.
3. Once that is done, the spend transaction is submitted to the sBTC protocol in order to mint the sBTC tokens to the user account that sent the peg-in.

#### **Withdrawals - Redeeming sBTC**

1. A user generates a P2TR address with a script that allows the Stackers to spend it, while at the same time revealing a user signature used to link the user to a Stacks account.
2. The user funds the address with some Bitcoin to pay for the gas fees of pegging out. That transaction and its unlock script are submitted to the sBTC protocol, locking the user’s sBTC for a predetermined duration.
3. The Stackers then spend that output to pay for the transaction fee of fulfilling the peg-out request. If the Stackers do not process the peg-out in time, then it will expire, allowing the user to reclaim the locked sBTC tokens.

### **sBTC Signer API**

The Peg-in sBTC Signer API forms a pivotal part of the sBTC system, acting as the mechanism enabling Stackers to sign peg-in requests.

Once users register their peg-in requests into the sBTC smart contracts, the API facilitates Stackers to review and sign these requests, effectively approving the transfer of the user's Bitcoin into the sBTC system. This essential process maintains the security, functionality, and fluidity of the sBTC system, allowing for seamless interaction between the Bitcoin and Stacks blockchains.

## Go-To-Market Timeline:

> 👉 _What is the development timeline for sBTC?_

A detailed timeline can be found [here](https://www.bitcoinwrites.com/p/growing-bitcoin-economy-road-sbtc).

### Phase 1: Foundation (Timeframe: 0-6 months)

- Milestone: Testnet Launch and Developer Release
- Objectives:
  - Conduct user research and product validation.
  - Develop strategic partnerships for wider adoption.
  - Recruit founders for Bitcoin DeFi applications.
  - Educate the community and developers about sBTC.
- Success Criteria:
  - Testnet activation and early developer feedback.
  - Defined brand positioning and targeted use cases.
  - Foundational partnerships on track for launch.

### Phase 2: Improved Bitcoin User Experience (6-12 months)

- Milestone: sBTC Launch on Mainnet and Nakamoto Release
- Objectives:
  - Conduct security audits for codebase.
  - Expand partnerships for more accessibility and liquidity.
  - Host hackathons to boost user activity and app development.
- Success Criteria:
  - Strong user confidence in the system's security.
  - Flagship apps available on launch.

### Phase 3: Thriving Bitcoin Economy (Timeframe: 12-24 months)

- Milestone: Scalability
- Objectives:
  - Focus on scalability to handle increased usage.
  - Build an app ecosystem to expand the Bitcoin economy.
  - Drive sBTC adoption among developers through education.
- Success Criteria:
  - sBTC becomes the most widely available decentralized Bitcoin protocol.
  - Seamless app experience with frictionless interactions.

## Success Metrics:

> 👉 _How will sBTC’s success be measured?_

- Funds are secure (trustworthiness, stability of the platform, always 1:1 backed)
- Successfully deploy Bitcoin capital in apps, products, and smart contracts alike that prove that you can unlock Bitcoin into productive use cases
- “TVL” or Total liquidity of sBTC available to deploy
- Number of apps launched and have X% MoM user growth
- 150 new developers in the ecosystem six months post-launch
