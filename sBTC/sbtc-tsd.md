# sBTC | Technical Specifications Document

> Detailed Product Requirements Document for sBTC can be found [here](sbtc-prd.md).

> Detailed Product Requirements Document for sBTC Signer can be found [here](sbtc-signer-prd.md).

## Introduction:

> 👉 _What can you learn from exploring the Product Requirements Document for sBTC? Discover its purpose, target audience, benefits, problem-solving capabilities, and implementation details._

Introducing a revolutionary protocol on the Stacks chain, enabling secure movement of Bitcoin and fully decentralized applications for the Bitcoin currency. Discover how this non-custodial digital asset, sBTC, facilitates seamless transactions and unlocks new possibilities in DeFi while preserving the core principles of decentralization and self-sovereignty. Explore how its 1:1 BTC backing and decentralized management address existing challenges and offer a more transparent and trustworthy solution compared to custodial approaches. Embrace the comprehensive solution that bridges the gap between Bitcoin's limitations and the demand for decentralized financial applications.

## Technical Requirements:

> 👉 _What technical requirements and criteria must sBTC meet to be fully functional and successfully implemented?_

sBTC implements the SIP10 token standard and enables the minting, burning, locking, and unlocking of sBTC tokens. The Peg-in sBTC Signer API facilitates the signing of peg-in requests by Stackers to approve the transfer of Bitcoin into the sBTC system.

sBTC is a protocol and therefore has no particular intrinsic technical requirements. Different implementations of the protocol may have different requirements. Typically, a network-connected VM with an 100Mb/s network and 95% uptime should be enough to participate in the protocol.

## Architectural Diagrams:

The architecture is explained in the sBTC technical docs [here](https://github.com/stacks-network/sbtc-docs/blob/master/src/architecture.md). For the sake of brevity, the details are omitted in this document.

## Testing Plan:

> 👉 _What is the comprehensive testing plan in place to ensure quality assurance?_

Testing a protocol is very different from testing a typical software product.

The strategy in sBTC is to break the final sBTC delivery into two main sub deliveries to test different aspects of the protocol.

1. Release a custodial version of the token to test the user interface of sBTC.
2. Release a non-consensus breaking version of the protocol to enable testing of operator implementations.

## Deployment Plan:

> 👉 _What does the deployment plan entail, including infrastructure requirements, deployment processes, and monitoring strategies?_

### sBTC Protocol Deployment

First let’s define what a deployment is for a protocol. We define a deployment of an sBTC version as:

1. A smart contract deployed on the Stacks chain defining an sBTC token.
2. Documentation explaining the protocol, how to interact with this particular sBTC token and how to participate in operating it.
3. Published implementation of any software binaries and tools needed to participate in the protocol as a user or operator.

### sBTC Deployment Epics

The plan is to deploy the following versions:

1. sBTC Alpha. A custodial version of the protocol operated by a single entity, supporting an initial version of the sBTC interface.
2. sBTC Mini. A decentralized version of the protocol without any consensus-breaking changes.
3. sBTC MVP. A consensus-breaking decentralized version with a minimal feature set.
4. sBTC 1.0. The first version of the protocol which is economically sound, decentralized and secure.

### sBTC Monitoring Strategy

Currently we are lacking a monitoring strategy. All operations on sBTC are visible on-chain, but no plan for a sBTC dashboard capable of tracking interesting metrics for sBTC has been made yet.
