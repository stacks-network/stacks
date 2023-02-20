
# Why is Stacks a Bitcoin L2? 

There are no clear definitions on what is a layer-1 (L1) or layer-2 (L2) in the Bitcoin and crypto industry. Any classification of chains as L1, L2, or other terms like sidechains depends on the exact definition used. With that said, generally speaking L1 chains are sovereign meaning that (a) they have their own security budget, and (b) they can survive without the need for any other L1 chain. L2 chains typically do not have their own security budget and share the security of the underlying L1 chain, and they cannot live without the underlying L1 chain.

The initial release of Stacks in early 2021 had a separate security budget from Bitcoin L1. Even though the Stacks layer could not function without Bitcoin L1, the developers working on the project described it as a different system that does not fit neatly into existing classifications, sometimes using the term layer 1.5 (see [this Decrypt article](https://decrypt.co/82019/bitcoin-defi-thing-says-stacks-founder-muneeb-ali) for example).

The upcoming planned release of Stacks, called the Nakamoto release (convention to use names of famous Computer Scientists for major releases), will no longer have a separate security budget from Bitcoin. Instead, a 100% of Bitcoin hashpower will determine finality on Stacks making it more clearly a Bitcoin L2. After the next upgrade, to reorg Stacks blocks/transactions the attacker will need to reorg Bitcoin L1 itself (which is very hard to do and therefore a great security property for a Bitcoin L2 to have). More details in the [latest whitepaper](https://stacks.co/stacks.pdf).

There are some other properties that also help the case for Stacks as a Bitcoin L2:

1) Bitcoin finality, as discussed above, where 100% of the Bitcoin hashpower decides block ordering and transaction finality. 
2) Stacks consensus runs on Bitcoin L1, and Stacks L2 cannot operate or survive without Bitcoin L1.
3) With the upcoming decentralized Bitcoin peg, called sBTC (see [sBTC paper](https://stacks.co/sbtc.pdf)), most of economy on Stacks L2 will likely use BTC as the unit of economy. It is expected that most users will simply use Bitcoin in wallets and apps and then peg out their BTC to Bitcoin L1.
4) All data and transactions on Stacks are automatically hashed and permanently stored on Bitcoin L1 on every Bitcoin block. Anyone can verify that some data on Stacks is valid by checking the corresponding hash on Bitcoin L1. This compact storage of hashes on L1 is somewhat similar to rollups (although there are other differences).
5) Contracts on Stacks L2 can read Bitcoin L1 transactions and respond to them. Assets on Stacks L2 can be moved simply through Bitcoin L1 transactions.

Given all the details above, why would some people think that Stacks is not a Bitcoin L2? There are a couple of reasons why this question comes up often:
1) The initial version of Stacks (released early 2021) was more like a layer 1.5 than a Bitcoin L2 and there is old material and blog posts floating around that still talk about Stacks as a layer 1.5. The old materials will likely get updated with time.
2) There is one specific definition of L2s which says that a user should be able to withdraw their base-layer assets purely by doing a L1 transaction and relying only on L1 security (this is true for Lightning for example). In the upcoming Stacks release, users can withdraw their BTC by sending just a Bitcoin L1 transaction but Bitcoin L1 cannot validate that complex transaction and a majority of peg-out signers will need to sign on the peg-out request. In an ideal world Bitcoin miners can validate such transactions but that would require a change to Bitcoin L1. Therefore, Stacks design optimizes for a method that is decentralized and can be deployed without any changes to Bitcoin L1. If in the future it is possible to make changes to Bitcoin L1 then Stacks L2 security can benefit from that as well.
3) Bitcoin community members are generally skeptical of claims and on a look out for people making any false marketing claims. This is generally a healthy thing for the Bitcoin ecosystem and builds up the immune system. Some such community members might be skeptical about Stacks as a Bitcoin L2 until they fully read the technical details and reasoning. There is a [good Twitter thread](https://twitter.com/lopp/status/1623756872976158722?s=20) about his topic as well.

Hope this FAQ is helpful. If you have more comments or questions then feel free to [start a Github issue](https://github.com/stacks-network/stacks/issues/new) for discussion.
