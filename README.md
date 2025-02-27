## Stacks: A Bitcoin Layer for Smart Contracts


Stacks is a Bitcoin layer for smart contracts; it enables smart contracts and decentralized applications to trustlessly use Bitcoin as an asset and settle transactions on the Bitcoin blockchain. 

➡️ Read the Stacks whitepaper [html](https://stacks-network.github.io/stacks/stacks.html) [pdf](https://stacks-network.github.io/stacks/stacks.pdf)<br>
➡️ Read the sBTC whitepaper [html](https://stacks-network.github.io/stacks/sbtc.html) [pdf](https://stacks-network.github.io/stacks/sbtc.pdf)<br>
[>> See the Stacks overview slides](https://drive.google.com/file/d/19IX1PHshiXfdg7HXVJSQ8bPME_uizH6-/view) (slightly outdated).

The initial version of Stacks, launched in early 2021, introduced Bitcoin settlement of transactions, the Clarity language for safe contracts that can respond to Bitcoin transactions, and atomic swaps of assets with BTC. The next major proposed upgrade of Stacks, the Nakamoto release (see [SIP-021](https://github.com/stacksgov/sips/blob/56b73eada5ef1b72376f4a230949297b3edcc562/sips/sip-021/sip-021-trustless-two-way-peg-for-bitcoin.md)), adds important capabilities that will enhance the power of Stacks as a Bitcoin layer: (a) a trustless, two-way Bitcoin peg to move BTC in/out of the layer and write to Bitcoin, (b) transactions secured by Bitcoin finality, and (c) fast transactions in between Bitcoin blocks. The resulting Stacks layer makes Bitcoin a fully programmable asset in a trustless manner. This can make hundreds of billions of dollars of passive Bitcoin capital productive, and make Bitcoin the backbone of a more secure web3.

The Stacks layer for smart contracts has the following innovations that make it unique:<br><br>
**S – S**ecured by the entire hash power of Bitcoin (Bitcoin finality).<br>
**T – T**rustless Bitcoin peg mechanism; write to Bitcoin.<br>
**A – A**tomic BTC swaps and assets owned by BTC addresses.<br>
**C – C**larity language for safe, decidable contracts.<br>
**K – K**nowledge of full Bitcoin state; read from Bitcoin.<br>
**S – S**calable, fast transactions that settle on Bitcoin.<br>

Why Bitcoin? Bitcoin is the most durable and secure blockchain. Bitcoin is minimal by design and is meant to not change. Stacks layer brings more functionality to Bitcoin without modifying Bitcoin L1. Thousands of transactions at the Stacks layer result in a settlement at the Bitcoin L1, and Stacks microblocks offer fast confirmations of streaming transactions. Bitcoin is used as a settlement layer and fast transactions in-between two Bitcoin blocks are proposed for the Nakamoto release ([SIP-21](https://github.com/stacksgov/sips/blob/56b73eada5ef1b72376f4a230949297b3edcc562/sips/sip-021/sip-021-trustless-two-way-peg-for-bitcoin.md)). Further, scalability is enabled as [subnets](https://github.com/hirosystems/stacks-subnets), amongst other scalability solutions (like [appchains](https://gist.github.com/jcnelson/c982e52075337ba75e00b79942164e31)).

Bitcoin's Stacks layer makes BTC productive in two ways:
- Stacks consensus enables a trust-minimized Bitcoin peg mechanism, called sBTC. A dynamic group of economically incentivized actors operate the peg. See the [sBTC page](https://stacks.co/sbtc) for more details.
- Further, through atomic swaps BTC can be trustlessly swapped and deployed into DeFi applications, NFT marketplaces etc. For example, see [Magic BTC atomic swaps](https://magic.fun) and [Catamaran BTC atomic swaps](https://www.hiro.so/blog/bitcoin-defi-is-here-a-deep-dive-into-trust-less-swaps), and [Lightning swaps](https://lnswap.org). 

You can see some applications built using Stacks [here](https://www.stacks.co/explore/discover-apps).

Stacks asset (STX) is used for mining incentives (block subsidy for miners) of the Stacks layer and for incentives for sBTC peg-out signing. These miners secure the global ledger of the Stacks layer. This data cannot be stored at the Bitcoin main chain and needs to be stored outside Bitcoin. STX is also used as gas for smart contract execution. STX is a unique crypto asset that can be locked by STX holders to earn Bitcoin rewards from the protocol. More details on earning Bitcoin rewards are at [stacking.club](https://stacking.club).

STX was distributed to the general public through the first-ever SEC qualified token offering in US history. The project decentralized before the mainnet launch in Jan 2021. There are [30+ independent companies](https://twitter.com/zrixes/status/1433248424271355905?s=20) that work in the ecosystem.

## Clarity Language for Smart Contracts

Clarity is a new language for smart contracts that [focuses on safety](https://stacks.org/bringing-clarity-to-8-dangerous-smart-contract-vulnerabilities/). Clarity is a decidable language, meaning you can know, with certainty, from the code itself what the program will do. Clarity is interpreted (not compiled) and the source code is published on the blockchain (see [this deployed code](https://explorer.stacks.co/txid/SP000000000000000000002Q6VF78.pox?chain=mainnet) for the PoX contract).

For details, see the [Clarity book](https://book.clarity-lang.org/) and [Clarity website](https://clarity-lang.org).

## Proof-of-Transfer (PoX)

[PoX consensus](https://blockstack.org/pox.pdf) is a new algorithm that spans consensus between the Bitcoin blockchain and the Stacks layer. Unlike burning electricity in proof-of-work, miners bid by spending BTC and get a random probability for becoming a leader. Leader election happens on Bitcoin and new blocks are written on the Stacks layer. Miners use BTC to mine newly minted STX. PoX recycles proof-of-work energy to provide Nakamoto-style consensus for the Stacks layer. 

See [this post](https://medium.com/@sonkaos999/the-bullish-case-for-stacks-8ef75849861f) on PoX for more details.

## Resources

Some resources for further details:
- [Working groups](https://github.com/stacks-network/stacks/discussions) for non-custodial BTC peg and faster blocks<br>
- In-depth [video interview](https://www.youtube.com/watch?v=dEQFPNWaOHY) for Stacks blockchain and consensus.
- [Stacks Improvement Proposals](https://github.com/stacksgov/sips/tree/main/sips) (SIPS)

## Code

Check out the [latest docs](https://docs.stacks.co/) for the easiest way to get started!

If you're just starting with Stacks, here are the main software repositories you should checkout:

- [Stacks Layer Code](https://github.com/stacks-network/stacks-blockchain) - the reference implementation of the Stacks layer in Rust.
- [Stacks Documentation](https://github.com/stacks-network/docs) - community documentation for Stacks
- [stacks.js](https://github.com/hirosystems/stacks.js) - a JavaScript library for using identity, auth, and storage in your apps.
- [Stacks Explorer](https://github.com/hirosystems/explorer) - explorer for Stacks layer.

## How to Help

- **Contribute open-source code** - send us pull requests with improvements! See some [good first issues](https://github.com/stacks-network/stacks-blockchain/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
- **Help with software testing** - we encourage the community to run the software and file issues.
- **Become a community evangelist** - [join community leaders](https://community.stacks.org/evangelists) around the world supporting our mission.
- **Weekly Stacks meetings** on [Discord](https://stacks.chat).

## Resources

- [Stacks Forum](https://forum.stacks.org)
- [Telegram](https://t.me/StacksChat)
- [Discord](https://stacks.chat)
- [Mailing List](https://stacks.org/updates)
- [YouTube Videos](https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ)
- [Twitter](https://twitter.com/stacks)
