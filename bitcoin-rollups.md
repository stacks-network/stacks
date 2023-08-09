
# How do rollups compare with the Stacks layer?

Rollups are an exciting development for scaling decentralized applications. There are many different types of rollups; they're broadly divided into ZK rollups and Optimistic rollups, although other classifications are also there (see [this overview](https://era.zksync.io/docs/dev/fundamentals/rollups.html#what-are-rollups)).

Rollups are generally considered layer-2 (L2) technology that runs on top of a layer-1 blockchain like Bitcoin or Ethereum. A critical aspect of rollups is the trustless nature where logic running on the L1 chain can determine whether something that happened on the rollup was valid. This is not true for all types of rollups, and there is some fuzziness around exact definitions. [Sovereign rollups](https://blog.celestia.org/sovereign-rollup-chains/), for example, only use the underlying L1 for data availability (DA) and not for consensus.

Most of the rollups work on Ethereum uses Ethereum L1 both as a data availability layer, and for consensus, i.e., the validity of rollup transactions is determined by logic running on Ethereum L1. Newer systems, [like Celestia](https://celestia.org/), are taking a more modular approach and are separating DA from consensus. One interesting aspect of separating DA is that more established and durable chains like Bitcoin can be used for DA as well. Below is an interesting comparison of sidechains and two types of rollups possible on Bitcoin (John Light posted this [on Twitter](https://twitter.com/lightcoin/status/1630301411962388481?s=20)):

<img src="https://user-images.githubusercontent.com/669932/223139236-f43fba13-7b50-4ec7-9183-6871d8bd5d6d.png" width=70%>

This image broadly means developers can build sovereign rollups on Bitcoin today, but you'll need a "trusted" setup for moving BTC in and out of the rollup. In fact, people are already doing this -- see the recent [Rollkit announcement](https://rollkit.dev/blog/sovereign-rollups-on-bitcoin/). To build validity rollups, meaning Bitcoin L1 enforces BTC withdrawals from the rollup, you'll need modifications to Bitcoin L1. See [this overview](https://bitcoinrollups.org/) for more details.

## How does the Stacks layer compare?

Stacks is not really a sidechain, given the Nakamoto release (see [latest Stacks paper](https://stacks.co/stacks.pdf)), Stacks layer will follow Bitcoin finality with 100% Bitcoin hashpower. Also, the Stacks layer has various other direct connections to Bitcoin L1 that sidechains typically do not have -- see [this FAQ](https://github.com/stacks-network/stacks/blob/master/stacks-l2.md) for details if Stacks is a Bitcoin L2 or not; the short answer is it depends on the definition you use.

Stacks with the Nakamoto release will have Bitcoin-grade reorg resistance following Bitcoin finality (typically people wait 6 blocks on Bitcoin). This is very similar to reorg resistance of sovereign rollups.

For data availability, Stacks publishes only hashes of data to Bitcoin every Bitcoin block instead of posting all the data to Bitcoin. The designers separate data validation from data availability. Bitcoin is used for data validation, which is important. Bitcoin L1 and only Bitcoin L1 can confirm whether a presented Stacks layer history
is valid. The block data itself is kept outside of Bitcoin L1 for scalability. As long as STX has any market cap, there is an incentive for Stacks miners to keep copies of the Stacks layer ledger around. Even if a single copy of the Stacks ledger exists, it can be independently verified against Bitcoin L1. Sovereign rollups publish all data to Bitcoin L1, giving both Bitcoin-grade data validity and data availability. The potential downside is scalability at Bitcoin L1, but the hope is that rollup data will not become very large.

## Can Stacks layer work with rollups?

Yes! There is already an active R&D effort to integrate rollups with the Stacks layer. Both with the Stacks layer and sovereign rollups the technically challenging part is how to get BTC in and out of the Stacks layer or the sovereign rollup. The decentralized BTC peg, see [the sBTC paper](https://stacks.co/sbtc.pdf), applies to both the Stacks layer and sovereign rollups. Without modifying Bitcoin L1, an sBTC-like design with a decentralized open-membership group of signers is the most trust-minimized way to move BTC in and out of Bitcoin layers. Once the necessary upgrades to Bitcoin L1 can be made to enable validity rollups i.e., Bitcoin L1 can enforce BTC withdrawal from a layer, then the Stacks layer can also upgrade to benefit from it.

Given a trust-minimized asset like sBTC is needed for sovereign rollups, with the launch of sBTC such sovereign rollups become even more interesting to deploy. The Stacks layer can potentially provide the decentralized group of signers for a trust-minimized BTC asset that can be used in a sovereign rollup, and DA comes directly from Bitcoin L1 e.g., with Ordinals. If you want to learn more, please join [the sBTC working group](https://github.com/stacks-network/stacks/discussions/469). There might be a dedicated rollups working group in the Stacks project soon as well.

Related FAQ: [Why is Stacks a Bitcoin L2?](https://github.com/stacks-network/stacks/blob/master/stacks-l2.md)
