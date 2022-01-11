## Stacks: Smart Contracts for Bitcoin

Stacks is a programming layer for Bitcoin. The Stacks blockchain enables smart contracts and decentralized apps for Bitcoin.

[>> Read the Stacks whitepaper](https://gaia.blockstack.org/hub/1AxyPunHHAHiEffXWESKfbvmBpGQv138Fp/stacks.pdf).<br>
[>> See the Stacks overview slides](https://drive.google.com/file/d/19IX1PHshiXfdg7HXVJSQ8bPME_uizH6-/view).

Why Bitcoin? Bitcoin is the most durable and secure blockchain. Bitcoin is minimal by design and is meant to not change. Stacks extends the design of Bitcoin to enable smart contracts and apps without modifying Bitcoin and with minimal transaction load on Bitcoin. Thousands of Stacks transactions result in a single hash at the Bitcoin blockchain, and Stacks microblocks offer fast confirmations of streaming blocks. Bitcoin is used as a settlement layer and ultra-fast transactions are implemented as [scalable subnets](https://www.youtube.com/watch?t=230&v=XnPGauXzino&feature=youtu.be), amongst other scalability solutions (like [appchains](https://gist.github.com/jcnelson/c982e52075337ba75e00b79942164e31)). 

Stacks cryptocurrency (STX) is used as fuel for smart contract execution, transaction processing, and digital asset registrations. STX is a unique crypto asset that can be locked by STX holders to actively participate in consensus and earn Bitcoin (BTC) rewards from the protocol. STX holders can either (a) lock STX in consensus to earn BTC rewards, or (b) use STX as fuel for smart contracts and transactions. More details on earning Bitcoin rewards are at [stacking.club](https://stacking.club).

Stacks cryptocurrency was distributed to the general public through the first-ever SEC qualified token offering in US history. The project decentralized before the mainnet launch in Jan 2021. There are 30+ independent companies that work in the ecosystem.

## Clarity Language for Smart Contracts

Clarity is a new language for smart contracts. Clarity is a decidable language, meaning you can know, with certainty, from the code itself what the program will do. Clarity is interpreted (not compiled) and the source code is published on the blockchain. See the [Clarity book](https://book.clarity-lang.org/) and [Clarity website](https://clarity-lang.org) for details.

## Proof-of-Transfer (PoX)

[PoX consensus](https://blockstack.org/pox.pdf) is a new algorithm that spans consensus between two blockchains. Unlike burning electricity in proof-of-work, miners bid by spending BTC and get a random probability for becoming a leader. Leader election happens on the base chain (Bitcoin) and new blocks are written on the connected chain. Miners use a base cryptocurrency (Bitcoin) to mine newly minted units of a new cryptocurrency. PoX has the unique property that it establishes a native exchange pair between two cryptocurrencies. (See a [community post](https://medium.com/@sonkaos999/the-bullish-case-for-stacks-8ef75849861f) on PoX for more details.)

## Stacks blockchain

Stacks blockchain is a blockchain that uses the Bitcoin blockchain as a secure base-layer and brings apps and smart contracts to Bitcoin. Stacks implements PoX consensus and natively connects to Bitcoin. With PoX there is no need to modify Bitcoin to enable smart contracts around it. There are two types of participants on Stacks (a) STX miners, and (b) STX holders. 

**STX miners** can view state on both the Bitcoin blockchain and the Stacks blockchain. STX miners participate in leader election by sending transactions on the Bitcoin blockchain, a Verifiable Random Function (VRF) randomly selects leader of each round, and the leader writes the new block on the Stacks chain. STX miners get newly minted STX (coinbase rewards), transaction fees, and Clarity contract execution fees of each block. STX miners express the cost of mining in BTC and spend BTC to participate in leader election. 

**STX holders** can participate in consensus by locking their STX for a cycle, running a full node, and sending useful information on the network as transactions. STX holders who actively participate in consensus can earn Bitcoin rewards. Unlike proof of stake, there is no risk of slashing for STX holders. See the [STX earning model](https://github.com/blockstack/stacks/blob/master/stacking.md) for potential earning rate and [stacking.club](https://stacking.club) for details.

Some resources for further details:
- [Post on the Stacks blockchain](https://stacks.org/stacks-blockchain).
- In-depth [video interview](https://www.youtube.com/watch?v=dEQFPNWaOHY) for Stacks blockchain and consensus.
- [Stacks Improvement Proposals](https://github.com/stacksgov/sips/tree/main/sips) (SIPS), and [SIP-007](https://github.com/stacksgov/sips/blob/main/sips/sip-007/sip-007-stacking-consensus.md) in particular for more details.

## Code

Check out the [latest docs](https://docs.stacks.co/) for the easiest way to get started!

If you're just starting with Stacks, here are the main software repositories you should checkout:

- [Stacks Blockchain](https://github.com/blockstack/stacks-blockchain) - the reference implementation of the Stacks blockchain in Rust.
- [Stacks Authenticator](https://github.com/blockstack/ux) - the Authenticator app and developer tools for decentralized login.
- [stacks.js](https://github.com/blockstack/stacks.js) - a JavaScript library for using identity, auth, and storage in your apps.
- [Stacks Explorer](https://github.com/blockstack/explorer) - blockchain explorer for Stacks.

## How to Help

- **Contribute open-source code** - send us pull requests with improvements! See some [good first issues](https://github.com/blockstack/stacks-blockchain/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
- **Help with software testing** - we encourage the community to run the software and file issues
- **Become a community evangelist** - [join community leaders](https://community.stacks.org/evangelists) around the world supporting our mission
- **Weekly Stacks meetings** on [Discord](https://stacks.chat) (Thur at 10am ET).

## Resources

- [Stacks Forum](http://forum.stacks.org)
- [Telegram](https://t.me/StacksChat)
- [Discord](https://stacks.chat)
- [Mailing List](https://stacks.org/updates)
- [YouTube Videos](https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ)
- [Twitter](https://twitter.com/stacks)
