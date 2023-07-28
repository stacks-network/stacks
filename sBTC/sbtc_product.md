# sBTC Product | Requirements Document

- [Technical Specifications Document](./sbtc_technical.md)
- [sBTC Signer Product Requirement Document](./sbtc_signer.md)

## At a high-level what is sBTC?

[sBTC](./../sBTC-FAQ.md) is a new and novel digital asset that lets you move Bitcoin in and out of the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/). With [sBTC](./../sBTC-FAQ.md), you can use Bitcoin in [Clarity smart contracts](https://clarity-lang.org/), which will enable new applications such decentralized lending, decentralized exchanges, and BTC-backed stablecoins. This will have a crucial role in scaling Bitcoin, as well as introducing new and innovative functionalities to users, growing the overall potential of the ecosystem.

[sBTC](./../sBTC-FAQ.md) is a [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) token on the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/), backed 1:1 against BTC, and operated by a decentralized and open set of members. As a non-custodial digital asset, sBTC facilitates seamless movement of Bitcoin between the Bitcoin L1 and the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/) since it will allow all BTC holders to interact with [Clarity smart contracts](https://clarity-lang.org/) without the need for a trusted third-party. When BTC is locked on the Bitcoin L1, an equivalent amount of sBTC is issued on the Stacks layer, ensuring a consistent 1:1 ratio of `sBTC:BTC`.

## What specific problem does sBTC solve?

By design, Bitcoin's limited expressiveness makes it unsuitable for most decentralized applications. This leaves users with no options to use financial applications, like lending and derivatives trading, without entrusting their Bitcoin to centralized entities. This can also expose them to counterparty risk, which has the potential to result in lost funds. This centralization contradicts a fundamental principles of Bitcoin and dampens the potential to unlock new functionality and scalability for users.

Bitcoin, being the most secure and decentralized blockchain with the largest market capitalization, has known limitations in its scripting system, making it challenging for developers to build applications directly on Bitcoin. These limitations and a lack of expressiveness in Bitcoin's smart contract language has led developers to seek alternative ecosystems that provide them with greater flexibility and tooling.

A solution to this problem is to enable a secure and decentralized movement of Bitcoin in and out of the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/), providing fully decentralized and scalable applications for Bitcoin. The goal is to implement a protocol, [sBTC](./../sBTC-FAQ.md), that allows BTC holders to participate in smart contracts without relying on trusted third parties, ensuring the continuous 1:1 backing of `sBTC:BTC`. By addressing these challenges, [sBTC](./../sBTC-FAQ.md) seeks to open up opportunities for Bitcoin, enhancing its utility and accessibility while preserving the core principles of decentralization and self-sovereignty.

## How does sBTC provide a solution?

[sBTC](./../sBTC-FAQ.md) is being built as a protocol to allow for secure movement of Bitcoin in/out of the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/), enabling fully decentralized and scalable Bitcoin applications. It implements the [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) token standard and is managed by a decentralized group of signers, known as Stackers, on the Bitcoin blockchain. By bringing a _representation_ of BTC to the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/), [sBTC](./../sBTC-FAQ.md) presents a revolutionary new protocol that addresses the problem of limited expressiveness in the Bitcoin scripting system.

The [sBTC](./../sBTC-FAQ.md) protocol ensures a secure transfer of Bitcoin between the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/), providing users with a non-custodial digital asset that maintains a 1:1 backing `sBTC:BTC`. A decentralized group of signers, known as Stackers, safeguards the Bitcoin wallet, and users can deposit BTC into this wallet while proving the transaction on the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/).

With this deposit, [sBTC](./../sBTC-FAQ.md) tokens are minted, and users can seamlessly transact using [Clarity smart contracts](https://clarity-lang.org/) on the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/) while also having the freedom to redeem sBTC tokens for the underlying BTC at any time, with the signers executing the transaction to the user's specified address.

The [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/) allows for verification of the 1:1 `sBTC:BTC` ratio, enhancing transparency compared to custodial approaches like WBTC. Additionally, the management of the Bitcoin script/wallet on the Bitcoin blockchain is decentralized and open, involving multiple participants rather than a single entity or fixed federation. This ensures a more resilient and trustworthy system, where signers are economically incentivized to execute peg-out transactions efficiently.

Overall, [sBTC's](./../sBTC-FAQ.md) innovative protocol not only addresses the limitations of the Bitcoin scripting system but also provides a secure and decentralized solution for utilizing Bitcoin in various applications, aligning with the principles of self-sovereignty and economic freedom.

## What are the features of sBTC?

[sBTC](./../sBTC-FAQ.md) implements the [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) token standard and enables the minting, burning, locking, and unlocking of [sBTC](./../sBTC-FAQ.md) tokens. The Peg-in [sBTC](./../sBTC-FAQ.md) Signer API facilitates the signing of peg-in requests by Stackers to approve the transfer of Bitcoin into the [sBTC](./../sBTC-FAQ.md) system.

### sBTC Asset

[sBTC](./../sBTC-FAQ.md) implements the [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) token standard, using a special implementation designed to keep 1:1 parity with Bitcoin. In addition to standard [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) functionality, the focus of this contract is to mint, burn, lock, and unlock sBTC tokens as mandated by the [sBTC](./../sBTC-FAQ.md) protocol.

### Deposits (Minting sBTC)

1. A user submits Bitcoin to a P2TR deposit address.
2. Stackers then need to spend that Bitcoin within a specific timeframe and move it to the threshold wallet address.
3. Once that is done, the spend transaction is submitted via the sBTC protocol in order to mint the sBTC tokens to the user account that sent the peg-in.

### Withdrawals (Redeeming sBTC)

1. A user generates a P2TR address with a script that allows the Stackers to spend it, while at the same time revealing a user signature used to link the user to a Stacks account.
2. The user funds the address with some Bitcoin to pay for the gas fees of pegging out. That transaction and its unlock script are submitted via the sBTC protocol, locking the user’s sBTC for a predetermined duration.
3. The Stackers then spend that output to pay for the transaction fee of fulfilling the peg-out request. If the Stackers do not process the peg-out transaction in time then it will expire, allowing the user to reclaim the locked sBTC tokens.

### sBTC Signer API

The Peg-in sBTC Signer API forms a pivotal part of the sBTC system, acting as the mechanism enabling Stackers to sign peg-in requests.

Once users register their peg-in requests into sBTC smart contracts, the API facilitates Stackers to review and sign these requests, effectively approving the transfer of the user's Bitcoin into the sBTC system. This essential process maintains the security, functionality, and fluidity of the sBTC system, allowing for seamless interaction between Bitcoin and [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/).

## What is the development timeline for sBTC?

- [A detailed timeline can be found here](https://www.bitcoinwrites.com/p/growing-bitcoin-economy-road-sbtc)

### Phase 1: Foundation (Timeframe: 0-6 months)

**Milestone**: Testnet Launch and Developer Release

#### Objectives:

- Conduct user research and product validation.
- Develop strategic partnerships for wider adoption.
- Recruit founders for Bitcoin DeFi applications.
- Educate the community and developers about sBTC.

#### Success Criteria:

- Testnet activation and early developer feedback.
- Defined brand positioning and targeted use cases.
- Foundational partnerships on track for launch.

### Phase 2: Improved Bitcoin User Experience (6-12 months)

**Milestone**: sBTC Launch on Mainnet and Nakamoto Release

#### Objectives:

- Conduct security audits for codebase.
- Expand partnerships for more accessibility and liquidity.
- Host hackathons to boost user activity and app development.

#### Success Criteria:

- Strong user confidence in the system's security.
- Flagship apps available on launch.

### Phase 3: Thriving Bitcoin Economy (Timeframe: 12-24 months)

**Milestone**: Scalability

#### Objectives:

- Focus on scalability to handle increased usage.
- Build an app ecosystem to expand the Bitcoin economy.
- Drive sBTC adoption among developers through education.

#### Success Criteria:

- sBTC becomes the most widely available decentralized Bitcoin protocol.
- Seamless app experience with frictionless interactions.

## How will sBTC’s success be measured?

- Funds are secure
  - trustworthiness
  - stability of the platform
  - maintain 1:1 backing
- Successfully deploy Bitcoin capital in applications, products, and smart contracts that prove that you can unlock Bitcoin into productive use cases
- **TVL** or Total liquidity of sBTC available to deploy
- Number of apps launched and have X% MoM user growth
- 150 new developers in the ecosystem six months post-launch
