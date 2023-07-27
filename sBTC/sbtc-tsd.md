# sBTC | Technical Specifications Document

- [Product Requirements Document for sBTC](sbtc-prd.md).
- [Product Requirements Document for sBTC Signer](sbtc-signer-prd.md).

## What technical requirements must sBTC meet to be fully functional and successfully implemented?

[sBTC](./../sBTC-FAQ.md) implements the [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) token standard and enables the minting, burning, locking, and unlocking of sBTC tokens. The Peg-in [sBTC Signer](./sbtc-signer-prd.md) API facilitates the signing of peg-in requests by Stackers to approve the transfer of Bitcoin into the sBTC system.

[sBTC](./../sBTC-FAQ.md) is a protocol and therefore has no particular intrinsic technical requirements, however, different reference implementations of the protocol may have different requirements. Generically, a network-connected VM with an 100Mb/s network and 95% uptime should be sufficient to participate in the protocol.

## Architectural Diagram

[The architecture is explained in the sBTC technical docs](https://github.com/stacks-network/sbtc-docs/blob/master/src/architecture.md).

## What is the comprehensive testing plan in place to ensure quality assurance?

Testing a protocol is very different from testing a typical software product.

The strategy in [sBTC](./../sBTC-FAQ.md) is to break the final sBTC application into two deliverables to test the different aspects of the protocol.

1. Release a _custodial version_ of the protocol to test the user interface of [sBTC](./../sBTC-FAQ.md).
2. Release a _non-consensus breaking version_ of the protocol to allow testing of operator implementations.

## What does the sBTC deployment plan look like?

### sBTC Protocol Deployment

First let’s define what a deployment is for a protocol. We define a deployment of an [sBTC](./../sBTC-FAQ.md) version as:

1. A smart contract deployed on the [Stacks blockchain](https://github.com/stacks-network/stacks-blockchain/) defining an sBTC [SIP-010](https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md) token.
2. [Documentation explaining the protocol](https://github.com/stacks-network/sbtc-docs), and how to interact with the sBTC token as well as how to participate in the network.
3. Published reference implementations of any software binaries and tools needed to participate in the protocol as a user or operator.

### sBTC Deployment Epics

The plan is to deploy the following versions:

1. **sBTC Alpha**: A _custodial version_ of the protocol maintained by a single entity, to support an initial version of the sBTC interface
2. **sBTC Mini**: A decentralized version of the protocol _without any consensus-breaking changes_
3. **sBTC MVP**: A consensus-breaking decentralized version with a minimal feature set
4. **sBTC 1.0**: The first version of the protocol which is economically sound, decentralized and secure

### sBTC Monitoring Strategy

All operations on sBTC are visible on-chain, but there are no plans currently for a hosted sBTC dashboard.
