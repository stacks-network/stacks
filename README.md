## Stacks: A Foundation for a User-owned Internet

The Stacks blockchain enables a user-owned internet connected to Bitcoin. Stacks blockchain introduces predictable smart contracts and decentralized apps that anchor to the security of Bitcoin. Bitcoin is the most durable and secure blockchain that is minimal by design. Stacks extends the design of Bitcoin to enable smart contracts and apps without modifying Bitcoin and with minimal transaction load on Bitcoin. Thousands of Stacks transactions result in a single hash at the Bitcoin blockchain, and Stacks microblocks offer fast confirmations of streaming blocks.

Stacks cryptocurrency (STX) is used as fuel for smart contract execution, transaction processing, and digital asset registrations. STX is a unique crypto asset that can be locked by STX holders to actively participate in consensus and earn Bitcoin (BTC) rewards from the protocol. STX is a yield generating asset when used in consensus and functions as a utility token when consumed as fuel. Stacks cryptocurrency was distributed to the general public through the first-ever SEC qualified token offering in US history.

For a recent overview of the Stacks ecosystem see this [July 2020 update presentation slides](https://docs.google.com/presentation/d/15lKVjbpRpGPH4-sybepXS3X9hwsqw-h1rqo8VntbADM).

## Clarity Language for Smart Contracts

Clarity is a new language for smart contracts. Clarity is a decidable language, meaning you can know, with certainty, from the code itself what the program will do. Clarity is interpreted (not compiled) and the source code is published on the blockchain. See the [Clarity website](https://clarity-lang.org) and [Clarity Github](https://github.com/clarity-lang) for details.

## Stacks 2.0 blockchain

Stacks 2.0 blockchain implements [Proof-of-Transfer (PoX)](https://blockstack.org/pox.pdf) mining and connects to Bitcoin for security. The main idea is that the Bitcoin blockchain is the most durable and secure base-layer and a separate blockchain like Stacks can connect to it to enable smart contracts and apps. With PoX there is no need to modify Bitcoin to enable smart contracts around it. Miners on the Stacks chain can view state on both the Bitcoin blockchain and the Stacks blockchain, they participate in leader election by sending transactions on the Bitcoin blockchain, a Verificable Random Function (VRF) randomly selects leader of each round, and the leader writes the new block on the Stacks chain. Stacks miners get newly minted STX (coinbase rewards) and transaction fees and Clarity contract execution fees of each block. STX miners express the cost of mining in BTC and spend BTC to participate in leader election. Stacks holders can lock STX to actively participate in consensus and earn Bitcoin rewards.

See [Stacks Improvement Proposals](https://github.com/blockstack/stacks-blockchain/tree/master/sip) (SIPS), and [SIP-007](https://github.com/blockstack/stacks-blockchain/blob/master/sip/sip-007-stacking-consensus.md) in particular for more details.

## Code

If you're just starting with Stacks, here are the main software repositories you should checkout:

- [Stacks Blockchain](https://github.com/blockstack/stacks-blockchain) - the reference implementation of the Stacks 2.0 blockchain in Rust.
- [Stack Authenticator](https://github.com/blockstack/ux) - the Authenticator app and developer tools for decentralized login.
- [blockstack.js](https://github.com/blockstack/blockstack.js) - a JavaScript library for using identity, auth, and storage in your apps.
- [Stacks Explorer](https://github.com/blockstack/explorer) - blockchain explorer for Stacks 2.0 blockchain.

Check out the [latest docs](https://docs.blockstack.org) for the easiest way to get started!

## How to Help

- **Contribute code** - all software is open-source, so send us pull requests with improvements! See some [good first issues](https://github.com/blockstack/stacks-blockchain/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
- **Help with software testing** - we value testers, and encourage the community to run the software and file issues
- **[Become a community evangelist](https://community.blockstack.org/evangelists)** - join other passionate community leaders around the world supporting our mission
- **Weekly Stacks meetings** on [Discord](https://stacks.chat) (Thur at 10am ET).

## Resources

- [Stack Forum](http://forum.blockstack.org)
- [Stacks.zone](https://stacks.zone), community wiki
- [Telegram, Discord, and other channels](https://community.blockstack.org/groups)
- [Mailing List](https://blockstack.org/updates)
- [YouTube Videos](https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ)
- [Twitter](https://twitter.com/blockstack)
- [Stacks Events](https://community.blockstack.org/events)
- [Meetups](https://meetup.com/pro/blockstack)
