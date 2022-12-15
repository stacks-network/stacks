# sBTC FAQ

sBTC is a trustless two-way Bitcoin peg mechanism through which users can peg BTC from Bitcoin L1 to Bitcoin layers and then back. More specifically, sBTC is enabled by the unique properties of the [Stacks Bitcoin layer](https://stacks.co/stacks.pdf) and proposed as an upgrade to Stacks layer (see [SIP-021](https://github.com/stacksgov/sips/blob/56b73eada5ef1b72376f4a230949297b3edcc562/sips/sip-021/sip-021-trustless-two-way-peg-for-bitcoin.md)). 

Two resources for sBTC information:

- The [sBTC whitepaper](https://stacks.co/sbtc.pdf).
- sBTC [website + slides](https://stacks.co/sbtc).

### Q: Is sBTC really 'trustless'? 

A: sBTC is not BTC on Bitcoin L1. It is a pegged asset where BTC gets locked at Bitcoin L1 and sBTC is minted by the Stacks layer consensus. A decentralized group of signers are economically incentivized to sign the peg-out requests. This is an open-membership group (anyone can join), the group is dynamic (signers can come and go), and the signers have economic incentives to follow protocol rules (they lock STX capital in consensus and get BTC rewards for doing the work of signing). Some people may prefer to call this 'trust-minimized peg' or 'decentralized peg' vs a 'trustless peg'. The reason to call the peg trustless is that (a) there is no custodian or centralized company in the middle, (b) there is no fixed/known federation in the middle, (c) the system is open with open-source code and on-chain data where anyone can verify the state of the peg and locked BTC backing sBTC, and (d) the system follows the censorship properties of Bitcoin mining and finality properties of Bitcoin L1. If you consider Bitcoin to be trustless then you might consider sBTC peg to be trustless. The confusion might be that the sBTC authors are **not implying** that sBTC is as secure as BTC on Bitcoin L1. If you are pegging BTC from Bitcoin L1 to any Bitcoin layer (Lightning, Stacks, RSK, Liquid) you are taking on some additional risk and complexity than Bitcoin L1. Lightning arguably has the least amount of additional risk out of the existing Bitcoin layers. However, the sBTC peg mechanism is 'trustless' (or trust-minimized if you prefer that term) because there is no central party or federation that you are trusting in the middle.
