## Stacks: Apps and Smart Contracts for Bitcoin

The Stacks blockchain brings predictable smart contracts and decentralized apps to Bitcoin. Bitcoin is the most durable and secure blockchain. Bitcoin is minimal by design and is meant to not change. Stacks extends the design of Bitcoin to enable smart contracts and apps without modifying Bitcoin and with minimal transaction load on Bitcoin. Thousands of Stacks transactions result in a single hash at the Bitcoin blockchain, and Stacks microblocks offer fast confirmations of streaming blocks.

Stacks cryptocurrency (STX) is used as fuel for smart contract execution, transaction processing, and digital asset registrations. STX is a unique crypto asset that can be locked by STX holders to actively participate in consensus and earn Bitcoin (BTC) rewards from the protocol. STX holders can either (a) lock STX in consensus to earn BTC rewards, or (b) use STX as fuel for smart contracts and transactions. More details on earning Bitcoin rewards is [here](https://github.com/blockstack/stacks/blob/master/stacking.md).

Stacks cryptocurrency was distributed to the general public through the first-ever SEC qualified token offering in US history. For a recent overview of the Stacks ecosystem see this [July 2020 update presentation slides](https://docs.google.com/presentation/d/15lKVjbpRpGPH4-sybepXS3X9hwsqw-h1rqo8VntbADM).

## Clarity Language for Smart Contracts

Clarity is a new language for smart contracts. Clarity is a decidable language, meaning you can know, with certainty, from the code itself what the program will do. Clarity is interpreted (not compiled) and the source code is published on the blockchain. See the [Clarity website](https://clarity-lang.org) and [Clarity Github](https://github.com/clarity-lang) for details.

## Proof-of-Transfer (PoX)

[PoX consensus](https://blockstack.org/pox.pdf) is a new algorithm that spans consensus between two blockchains. Leader election happens on a base chain and new blocks are written on a connected chain. PoX has the unique property that it establishes a native exchange pair between two cryptocurrencies. Miners use a base cryptocurrency to mine newly minted units of a new cryptocurrency.

## Stacks 2.0 blockchain

Stacks 2.0 blockchain is a layer-1 blockchain that uses the Bitcoin blockchain as a secure base-layer and brings apps and smart contracts to Bitcoin. Stacks implements PoX consensus and natively connects to Bitcoin. With PoX there is no need to modify Bitcoin to enable smart contracts around it. There are two types of participants on Stacks (a) STX miners, and (b) STX holders. 

**STX miners** can view state on both the Bitcoin blockchain and the Stacks blockchain. STX miners participate in leader election by sending transactions on the Bitcoin blockchain, a Verifiable Random Function (VRF) randomly selects leader of each round, and the leader writes the new block on the Stacks chain. STX miners get newly minted STX (coinbase rewards) and transaction fees and Clarity contract execution fees of each block. STX miners express the cost of mining in BTC and spend BTC to participate in leader election. 

**STX holders** can participate in consensus by locking their STX for a cycle, running a full node, and sending useful information on the network as transactions. STX holders who actively participate in consensus can earn Bitcoin rewards. Unlike proof of stake, there is no risk of slashing for STX holders. See the [STX earning model](https://github.com/blockstack/stacks/blob/master/stacking.md) for potential earning rate.

See [Stacks Improvement Proposals](https://github.com/blockstack/stacks-blockchain/tree/master/sip) (SIPS), and [SIP-007](https://github.com/blockstack/stacks-blockchain/blob/master/sip/sip-007-stacking-consensus.md) in particular for more details.

## Code

If you're just starting with Stacks, here are the main software repositories you should checkout:

- [Stacks Blockchain](https://github.com/blockstack/stacks-blockchain) - the reference implementation of the Stacks 2.0 blockchain in Rust.
- [Stacks Authenticator](https://github.com/blockstack/ux) - the Authenticator app and developer tools for decentralized login.
- [blockstack.js](https://github.com/blockstack/blockstack.js) - a JavaScript library for using identity, auth, and storage in your apps.
- [Stacks Explorer](https://github.com/blockstack/explorer) - blockchain explorer for Stacks 2.0 blockchain.

Check out the [latest docs](https://docs.blockstack.org) for the easiest way to get started!

## How to Help

- **Contribute open-source code** - send us pull requests with improvements! See some [good first issues](https://github.com/blockstack/stacks-blockchain/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
- **Help with software testing** - we encourage the community to run the software and file issues
- **Become a community evangelist** - [join community leaders](https://community.blockstack.org/evangelists) around the world supporting our mission
- **Weekly Stacks meetings** on [Discord](https://stacks.chat) (Thur at 10am ET).

## Resources

- [Stacks Forum](http://forum.blockstack.org)
- [Stacks.zone](https://stacks.zone), community wiki
- [Telegram, Discord](https://community.blockstack.org/groups), and other channels
- [Mailing List](https://blockstack.org/updates)
- [YouTube Videos](https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ)
- [Twitter](https://twitter.com/blockstack)
- [Stacks Events](https://community.blockstack.org/events)
- [Meetups](https://meetup.com/pro/blockstack)
