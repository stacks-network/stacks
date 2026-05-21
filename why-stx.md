# Why is the STX token needed for Stacks?

After Stacks Nakamoto release developers and users will be able to simply use BTC in apps and pay gas fees in BTC by using sBTC (BTC on L2). To keep the Stacks L2 network decentralized the STX asset is used for incentives for sequencers (miners) and validators (signers). Without STX, you'd end up with a federation like Liquid.

Many Bitcoin community members are skeptical of new tokens and rightly so. There are countless projects out there that force the use of a token on their project and in many cases a token is actually not needed. Stacks project was started by Bitcoin builders who have a long history of building apps & protocols on Bitcoin L1 without any token (e.g., BNS launched [in 2015 on Bitcoin L1](https://twitter.com/muneeb/status/642714729169985537) which was one of the largest protocols using OP_RETURN on Bitcoin L1). So why did a bunch of Bitcoin builders decided to have a separate token for Stacks L2? Great question! Let's dig into the details.

The Stacks token (STX) is primarily meant to be used for two things (details in [Stacks paper](https://stacks.co/stacks.pdf)):

1) Incentives for Stacks L2 sequencers (miners)
2) Incentives for validators (peg-out signers)

The only way to remove the token is to build Stacks as a federated network like Liquid. In a federation the pre-selected group of companies control the mining and block production and a pre-selected group of companies need to be trusted for peg-out transactions. Stacks developers wanted to design an open and permissionsless system. The only way to have a decentralized mining process is through incentives. This is how Bitcoin works as well, where newly minted BTC are used as incentives to mine new blocks and anyone in the world can decide to become a miner. Anyone with BTC can mine the Stacks L2 chain, it is open and permissionless. 

Similarly, the way the decentralized BTC peg, called sBTC (see the [sBTC paper](https://stacks.co/sbtc.pdf)), is designed is that the group of signer is open and permissionless (unlike a federation). These signers have economic incentives to correctly follow the protocol for peg-out requests. In a federation, users need to blindly trust the pre-set federation members to get their BTC out of the federation and back on Bitcoin L1. Stacks developers wanted to have an open, permissionless, and decentralized way to move BTC from Bitcoin L1 to Stacks L2 and back. This is made possible through economic incentives i.e., need for a token.

Once the upcoming sBTC peg is live most of the economy of Stacks L2 is expected to follow a Bitcoin standard and work using BTC as the economic unit. It is expected that users will mostly interact with BTC in wallets and apps and pay gas fees in BTC. It is important to note that BTC **cannot** be used for mining incentives on Stacks L2 because the only way to incentivize decentralized block production is through newly minted assets by the protocol (similar to how Bitcoin works itself) i.e., need for a token.

More details about these tradeoffs can be found in the ["Bitcoin L2 trilemma"](https://x.com/muneeb/status/1717542872545628394?s=20) post.

Hope this FAQ is helpful. If you have more comments or questions then feel free to [start a Github issue](https://github.com/stacks-network/stacks/issues/new) for discussion.

Related FAQ: [Why is Stacks a Bitcoin L2?](https://github.com/stacks-network/stacks/blob/master/stacks-l2.md)
