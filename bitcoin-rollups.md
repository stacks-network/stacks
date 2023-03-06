
# How does the Stacks layer compare with rollups?

Rollups are an exciting development for scaling decentralized applications. There are many different types of rollups, they're broadly divided into
ZK rollups and Optimistic rollups although other classifications are also there (see [this overview](https://era.zksync.io/docs/dev/fundamentals/rollups.html#what-are-rollups)).

Rollups are generally considered layer-2 (L2) technology that runs on top of a layer-1 blockchain like Bitcoin or Ethereum. One important aspect of rollups is 
the trustless nature where logic running on the L1 chain can determine if something that happened on the rollup was valid or not. This is not true for all types of
rollups and there is some fuzziness around exact definitions. [Sovereign rollups](https://blog.celestia.org/sovereign-rollup-chains/) for example only use the underlying L1 for data availability (DA) and not for consensus.

Most of the rollups work on Ethereum uses Ethereum L1 both as a data availability layer and for consensus i.e., validity of rollup transactions are determined by
logic running on Ethereum L1. Newer systems, [like Celestia](https://celestia.org/), are taking a more modular approach and are separating DA from consensus. One 
interesting aspect of separating DA is that more established and durable chains like Bitcoin can be used for DA as well. Below is an interesting comparison of
sidechains and two types of rollups possible on Bitcoin (John Light posted this [on Twitter](https://twitter.com/lightcoin/status/1630301411962388481?s=20)):

<img src="https://user-images.githubusercontent.com/669932/223139236-f43fba13-7b50-4ec7-9183-6871d8bd5d6d.png" width=70%>

What this image broadly means is that developers can build sovereign rollups on Bitcoin today but you'll need a "trusted" setup for moving BTC in and out of the rollup.
In fact, people are already doing this -- see the recent [Rollkit announcement](https://rollkit.dev/blog/sovereign-rollups-on-bitcoin/). To build validity rollups, meaning
Bitcoin L1 enforces withdraws of BTC from the rollup, you'll need modificaitons to Bitcoin L1. See [this overview](https://bitcoinrollups.org/) for more details.

## How does Stacks layer compare?

Stacks is not really a sidechain, given with the Nakamoto release (see [latest Stacks paper](https://stacks.co/stacks.pdf)), Stacks layer will follow Bitcoin finality with 100% Bitcoin hashpower.
Also, Stacks layer has various other direct connections to Bitcoin L1 that sidechains typically do not have -- see [this FAQ](https://github.com/stacks-network/stacks/blob/master/stacks-l2.md) for details if Stacks is a Bitcoin L2 or not; short answer is depends on the
definiton you use.

Stacks with the Nakamoto release will have close to Bitcoin-grade reorg resistance. The designers of Nakamoto release have decided to wait 150 blocks before Bitcoin finality kicks in, this
is mostly done to allow short-term forks to be resolved at the Stacks level. This design also means that most Maximal Extractable Value (MEV) action happens on the Stacks
layer side and not on the Bitcoin side. There is always a fear of MEV incentives messing with Bitcoin mining and Stacks layer explicitly attracts most MEV activity to happen on the 
Stacks layer vs Bitcoin L1 (the assumption here is that most MEV activity will happen within 150 blocks). It is important to note that changing the variable from 150 to 6 blocks is trivial technically
and can be configured as needed. Sovereign rollups use a variable of 0 blocks effectively and work quite similar to Stacks layer for reorg resistance.

For data availability, Stacks publishes only hashes of data to Bitcoin every Bitcoin blocks instead of publishing all the data to Bitcoin. The designers separate
data validation from data availability. Bitcoin is used for data validation, which is important. Bitcoin L1 and only Bitcoin L1 can confirm if a presented Stacks layer history
is valid or not. The block data itself is kept outside of Bitcoin L1 for scalability. As long as STX has any market cap, there is an incentive for Stacks miners to keep copies
of the Stacks layer ledger around. Even if a single copy of the Stacks ledger exists it can be independently verified against Bitcoin L1. Sovereign rollups publish all data to Bitcoin L1 which gives both Bitcoin-grade data validity and data 
availability. The potential downside is scalability at Bitcoin L1 but the hope is that rollup data will not become very large.

## Can Stacks layer work with rollups?

Yes! There is already an active R&D effort looking at integrating rollups with the Stacks layer.
