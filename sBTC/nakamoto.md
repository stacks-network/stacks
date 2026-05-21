# Nakamoto Release | Technical Specification Document

- [Blockchain Structure](./nakamoto/blockchain_structure.md)
- [Block Signing and Announcement](./nakamoto/block_signing_announcement.md)
- [sBTC Concerns](./nakamoto/sbtc_concerns.md)
- [Extension: Fixed Transaction Orders](./nakamoto/extensions/fixed_transaction_orders.md)
- [Extension: Overdue Term](./nakamoto/extensions/overdue_term.md)
- [Testing Plan](./nakamoto/testing-plan.md)
- [Deployment Plan](./nakamoto/deployment-plan.md)

## What is The Nakamoto Release?

The Nakamoto Release proposes a new consensus protocol for Stacks blockchain, enhancing security and significantly reducing transaction confirmation latency to seconds.

This document describes a new consensus protocol for the Stacks blockchain, The Nakamoto Release, superseding the competitive mining protocol described in [SIP-001](https://github.com/stacksgov/sips/blob/main/sips/sip-001/sip-001-burn-election.md) and [SIP-007](https://github.com/stacksgov/sips/blob/main/sips/sip-007/sip-007-stacking-consensus.md). In this proposed system, both miners and PoX stackers _cooperate_ through Byzantine fault-tolerant agreement to produce a linearized stream of confirmed transactions, in which the materialized view of the chainstate is periodically recorded to the Bitcoin blockchain.

This new arrangement allows for a significantly lower transaction confirmation latency time (_on the order of seconds instead of hours_), while also increasing the security budget of the chain from 51% of the miners' Bitcoin spends to _at least_ the sum of 67% of the miners' Bitcoin spends plus 67% of the total STX stacked. The chain's security budget reaches 51% of Bitcoin's mining power through periodic chainstate snapshots written to the Bitcoin chain by block producers and stackers, which are confirmed by the Bitcoin network as regular transactions. Once a Stacks chainstate snapshot is confirmed by the Bitcoin network, no subsequent Stacks fork can revert it -- any Stacks chain reorganization requires a Bitcoin chain reorganization.

### In summary, The Nakamoto Release

- Replaces competitive mining (ratified in [SIP-001](https://github.com/stacksgov/sips/blob/main/sips/sip-001/sip-001-burn-election.md) and [SIP-000](https://github.com/stacksgov/sips/blob/main/sips/sip-000/sip-000-stacks-improvement-proposal-process.md) with a cooperative system between miners and PoX stackers through Byzantine fault-tolerant (BFT) agreement that produces a linearized stream of confirmed transactions with periodic chainstate recording to Bitcoin blockchain.

### Impact of The Nakamoto Release

- A substantial reduction in transaction confirmation latency: from hours to seconds.
- An increased security budget: 67% of miners' Bitcoin spends + 67% of total STX stacked.
  - Reaching 51% of Bitcoin's mining power via periodic, irreversible Stacks chainstate snapshots, confirmed by the Bitcoin network.
  - Subsequent Stacks forks cannot revert confirmed snapshots; require Bitcoin chain reorganization.

## What specific problem does The Nakamoto Release solve?

> Since activation in January of 2021, the Stacks network has operated with limitations due to single-leader block production. As a result, issues including high transaction latency, independent security budget, MEV, and unequal mining rewards have arisen. These problems stem from forking behavior and the lack of equitable rewards for minoritarian miners.

Per SIP-001, block production in Stacks executes through a single-leader process: in each Bitcoin block, several miners compete to win the right to append a block to the Stacks blockchain through a cryptographic sortition process. While this has served to keep the network running, it has several limitations:

- High transaction latency: Transactions are confirmed at the same rate as the underlying Bitcoin transaction -- that is, on the order of hours. Even then, there is no true finality, since like Bitcoin, Stacks employs Nakamoto consensus to achieve only a probabilistic agreement on whether or not a transaction was accepted by the network.
- Independent security budget: Because the Stacks blockchain can fork -- a consequence of its single-leader block production rules -- the cost to remove a transaction from the canonical fork is proportional to the amount of Bitcoin that miners have spent building atop it. The amount of Bitcoin is, in turn, proportional to the value of the STX coinbase, which is worth substantially less than the Bitcoin coinbase. Therefore, the cost to reorganize the Stacks blockchain to orphan a given transaction is substantially lower than the cost to do the same for a Bitcoin transaction (but in no case can a malicious party _hide_ their behavior without attacking Bitcoin, which mitigates the damage they can cause in practice).
- Miner-extractable value (MEV): Because Bitcoin miners may also be Stacks miners, a Bitcoin miner can guarantee that they win a Stacks block by excluding other miners' Bitcoin transactions from the Bitcoin blocks they produce. This has already happened with some F2Pool blocks, for example. Doing so is more profitable than mining honestly, because the Bitcoin miner can realize an arbitrarily high profit margin by tailoring their block-commit transaction to pay almost zero BTC to PoX recipients and omit a transaction fee.
- Unequitable mining rewards: Because the Stacks blockchain can fork, a majoritarian mining coalition can deliberately exclude the minority's blocks from the canonical fork. More banally, if a majority of Stacks miners (by Bitcoin spend) are not well-connected to the minority, they can accidentally exclude the minority's blocks simply because they do not arrive on their nodes in time to build atop them. At least one of these phenomena has been witnessed in practice. In either case, the minority does not receive any reward for their work.

Each of these problems arises from the fact that Stacks is a single-leader blockchain. In order to tolerate the failure of single leader to replicate a block or even produce a valid block, the Stacks chain must support blockchain forks in order to permit other miners to repair the canonical fork and "work around" missing or invalid block data. This forking behavior combined with single-leader block production creates an independent security budget, and permits Bitcoin miners to extract value from Stacks by preventing other Stacks miners from competing. The forking behavior prevents equitable mining rewards from being materialized for honest but minoritarian miners: the system _cannot_ reward minoritarian miners who produce non-canonical blocks lest it create incentives to selfish-mine or deliberately mine orphans. Without extra cooperation between miners, the current system forces Stacks transaction confirmation latency to be no lower than the underlying burnchain (Bitcoin) -- the best-effort nature of single-leader mining precludes requiring other miners to agree on the same chain tip before mining.

## How does The Nakamoto Release provide a solution?

The Nakamoto Release suggests a new Stacks blockchain consensus protocol, focusing on cooperation between miners and PoX stackers. Block production involves three steps:

1. Production
2. Acceptance
3. Finalization

Miners propose blocks, which stackers validate and accept. Block finalization occurs through periodic Bitcoin transactions committing to the Stacks chain state. This speeds up transaction confirmations and enhances security. A producer set is introduced for block mining, ensuring fair coinbase reward distribution. Checkpoint transactions sync Stacks block production with Bitcoin state.

The proposal also addresses sBTC concerns and introduces extensions for fixed transaction orders and variable tenure length handling.

This document proposes a substantially different consensus protocol whereby miners and PoX stackers _cooperate_ to produce a linearized transaction history. In the proposed system, block production is a three-step procedure, whereby block _production_, block _acceptance_, and block _finalization_ are treated separately:

1. Miners coordinate to create and propose new blocks from pending transactions. A block is proposed if at least 67% of miners agree on the same block, as measured by the Bitcoin spent by the miners to produce it. Once a block is proposed, it is transmitted to all PoX stackers in the current reward cycle.
2. Stackers not only validate each proposed block, but also verify that it builds atop the current Stacks chain tip and faithfully applies any on-Bitcoin Stacks transactions. If at least 67% of Stackers agree to accept a proposed block, then it is added to the Stacks blockchain and replicated to all other Stacks nodes. Subsequent blocks must be built atop it -- Stacks forks are no longer permitted.
3. Every so often, Stackers and miners must collectively produce a Bitcoin transaction that commits to the state of the Stacks chain in order to continue to receive block rewards. Any Stacks block must descend from the chain state this snapshot represents. This _finalizes_ all blocks represented by the snapshot, such that retroactively changing Stacks chain history will be as expensive as retroactivelly changing Bitcoin history, regardless of the future valuation and distribution of STX and regardless of the intentions of future miners and stackers.

With these principal changes, Stacks block production is no longer inherently tied to Bitcoin block production. As described in more detail below, miners no longer commit to each block they produce via Bitcoin transactions, but instead submit Bitcoin transactions only to join a _producer set_ of miners and to periodically snapshot the chain state. Block production now happens via a dedicated peer network maintained by the producer set and stackers.

In this proposed system, transaction confirmation latency now depends on how quickly a Stacks block that contains it can be produced and accepted. This takes on the order of seconds, instead of hours. In addition, the security budget of a transaction confirmed this way is substantially higher than it is today -- due to BFT agreement in steps 1 and 2, the cost to remove an already-confirmed but not-yet-finalized transaction is equal to the sum of 67% of the miners' Bitcoin spends since the last snapshot, plus 67% of the worth of the stackers' locked STX. At the time of this writing (1 STX = `$0.63` USD, 1 BTC = `$29,747` USD, Stacks reward cycle 63), this represents a security budget increase from `$234.18` USD per block ($4,680.36 before a snapshot is expected to occur) to `$213,908,185.70` -- five orders of magnitude higher! The requirement for miners and stackers to periodically snapshot the Stacks chain state further increases this budget to that of Bitcoin's security budget, regardless of how cheap or easy it may be in the future to monopolize subsequent Stacks block production.

Requiring miners and Stackers to cooperate to produce blocks mitigates the impact of Bitcoin miner MEV and allows for equitable coinbase reward distribution. Would-be Stacks miners have a reasonably long window of time (measured by Bitcoin blocks) to join a producer set, meaning that Bitcoin MEV miner would need to mine _every_ Bitcoin block in this window to monopolize Stacks mining. The requirement that miners collectively produce a block weighted by Bitcoin spends enables the Stacks blockchain consensus rules to distribute the STX coinbase _pro-rata_ to each miner in the producer set, and distribute the transaction fees _pro-rata_ to each miner who actively worked to approve the block. This ensures that honest minoritarian miners receive STX for their BTC while retaining an incentive for miners to pack as many high-value transactions into a block as possible.

## Producer Set Terms and Block Production

> Utilizing a single producer set, this approach emphasizes collaboration during fixed-length terms for block mining. To be valid, blocks must receive signatures from over 67% of the set's weighted public keys. Block production spans 10 Bitcoin blocks, treating Stacks blocks and microblocks without distinction. Each term enforces a cost limit of 10 times the Stacks 2.4 single block limit. Producers are selected based on their BTC spent on enrollments, with the top 100 being chosen. The primary goals of this proposal are to enhance mining efficiency and reduce transaction fees.

Rather than requiring competition among miners to mine blocks, each block is mined by a single, globally visible, producer set. A _producer set_ collaborates to mine blocks during fixed length _terms_. For a given term, every Stacks block is assembled and signed by a Byzantine fault-tolerant majority of that term's producer set.

The producer set is a collection of weighted public keys. Each member of the producer set is associated with a public key and is assigned a weight according to the proportion of Bitcoin committed during the term's selection (see [Producer Set Selection](#producer-set-selection)).

For a block to be validated, it must be signed by over 67% of the producer set by weight. The signature scheme uses a weighted extension of FROST threshold signatures, described in [Signature Generation](./nakamoto/block_signing_announcement.md). A valid signature can be created if and only if this 67% threshold is achieved.

### Block Production during a Term

Each producer set term is 10 Bitcoin blocks in length. Stacks cost limits are applied to the term as a whole rather than individual Stacks blocks, and each term's cost limit is 10x the Stacks 2.4 single block limit (or the single block limit after improvements to the Clarity runtime and improved benchmark results).

During a term, there is no distinction between Stacks blocks and microblocks: there are only blocks. Terms are not limited to 10 Stacks blocks (i.e., there may be more than one Stacks block produced during a given Bitcoin block), but rather the only limit applied to the term is the overall cost limit (which may be increased through application of a VDF to accommodate an unusually long term length; see [Extension: Overdue Term](./nakamoto/extensions/overdue_term.md)).

The first block of a term always builds off the last block stackers accepted from the prior term, which itself is a descendant of the last on-Bitcoin snapshot. Producers may not choose to reorganize a prior term, nor may they reorganize any stacker-accepted blocks. But, any unannounced or not-yet-accepted blocks from the prior term are dropped.

### Producer Set Collaboration

While this proposal specifies how blocks mined by a producer set are validated, it leaves open the question of exactly how producer sets collaborate to assemble blocks. This is intentional: the validation of blocks is consensus-critical, but exactly how a valid block gets mined is not. However, the Stacks blockchain codebase will need to supply a default method for this assembly. There are, however, two requirements that producer set must adhere to:

- A proposed block must be signed by at least 67% of the producer set, measured by BTC spend.
- There exists at most one proposed block at a given height with respect to a given Bitcoin fork.

If either requirement is not met, then stackers halt block acceptance for the remainder of the term.

This SIP proposes that producer sets undergo a leader election once the producer set is chosen (or the current leader becomes inactive). Leader elections proceed in rounds until a leader is chosen by 67% of the weighted producer set. At the start of a round, each node in the producer set waits a random amount of time. If it does not receive a request for a leadership vote before that timeout, it puts itself forward for leadership, and submits a vote request to every other participant. If a node receives a vote request and it has not already voted in that round or submitted its own leadership request, it signs the vote request.

The leader is responsible for assembling a block and sending it to each producer set participant to collect the threshold signatures. There are many possible extensions and variations to this protocol. For example, each participant could have some heuristic about the best transaction ordering for a block, and if the proposal deviates too much, the node could opt not to sign, or try to trigger a leadership change.

### Producer Set Selection

The producer set selection for term _N_ occurs during term _N-2_. Similar to the leader block commitments used in the current miner selection process, as defined in [SIP-001](https://github.com/stacksgov/sips/blob/main/sips/sip-001/sip-001-burn-election.md) and amended in [SIP-007](https://github.com/stacksgov/sips/blob/main/sips/sip-007/sip-007-stacking-consensus.md), would-be producers issue a Bitcoin transaction known as a producer set enrollment.

### Producer Set Enrollments

As it is today, this SIP requires block producers to register a VRF public key on the Bitcoin chain prior to enrolling in a producer set. The process and wire-formats are the same as in SIP-001; see [VRF key registration](https://github.com/stacksgov/sips/blob/main/sips/sip-001/sip-001-burn-election.md#leader-vrf-key-registrations).

Producer set enrollments have the same constraints on the Bitcoin transaction's inputs as PoX leader block commitments. Specifically, the first input of this Bitcoin operation must originate from the same address as the second output of the VRF public key registration transaction. The first output of a producer set enrollment must be an `OP_RETURN` with the following data:

```
0      2  3      7     11    13          46      50        52   80

|------|--|------|-----|-----|------------|-------|--------|--------|

magic  op tenure  key   key     signing   snapshot snapshot padding

number block txoff   pubkey    block    txoff
```

Where `op = @` and:

- `tenure_number` is the target tenure for this producer, which should be `N`
- `key_block` is the Bitcoin block height of this producer's VRF key registration
- `key_txoff` is the transaction index for this producer's VRF key registration
- `signing_pubkey` is the compressed secp256k1 public key used by this producer to sign FROST signature-generation messages to be consumed by other producers.
- `snapshot_block` is the Bitcoin block height of the last valid snapshot transaction this producer has seen up to tenure `N-2`.
- `snapshot_txoff` is the transaction index of this snapshot transaction.

The subsequent output(s) in this transaction are the PoX outputs:

1. If the producer set enrollment is in a reward phase, then outputs 1 through 20 must go to the chosen PoX recipients.

- Recipients are chosen as described in "Stacking Consensus Algorithm" in SIP-007, using the final block announcement of term N-3 as the source: addresses are chosen without replacement, by using the sortition hash, mixed with the burn header hash of the final block announcement from term N-3 as the seed for the ChaCha12 pseudorandom function to select 20 addresses. Since a producer set term lasts 10 Bitcoin blocks, there are 20 PoX recipients, 2 per Bitcoin block, to maintain the same number of reward slots and payment frequency.
- The order of these outputs does not matter.
- Each of these outputs must receive the same amount of BTC.
- If the number of remaining addresses in the reward set, N, is less than 20, then the producer set enrollment must burn BTC by including (20-N) burn outputs

1. Otherwise, the second output must be a burn address (i.e. the enrollment falls into a prepare phase).

During a reward cycle, this enrollment transaction will include a somewhat large number of outputs: one `OP_RETURN`, 20 stacker rewards, and one change address, totaling 22 outputs. While this might seem like a substantial transaction, it effectively replaces ten separate transactions under the SIP-007 leader block commit scheme, each of which would have four outputs (one `OP_RETURN`, two stacker rewards, and one change address). Furthermore, the enrollment window's duration of ten blocks potentially allows would-be producers to take advantage of lower transaction fees during one of those blocks. Despite the higher fee for this larger transaction, the cost can be spread out or amortized across the ten blocks of the set, resulting in a lower overall cost compared to the previous system.

### Enrollment Censorship Resistance

The producer set enrollments for set _N_ can be included in any of the 10 Bitcoin blocks in producer set _N-2_. This makes it extremely difficult for a Bitcoin miner to censor these transactions, since to do so, they would need to control all 10 Bitcoin blocks in that term.

### Selecting Producers

Would-be producers with valid producer set enrollments in term _N-2_ are eligible to be included in the producer set for term _N_. The total number of producers in a set needs to be limited to prevent coinbase payouts from including too many accounts, as this could slow down event processing and even open a DoS vector. This cap will also prevent the block-signing process from becoming too CPU- and bandwidth-intensive. To this end, the total amount of BTC spent in the outputs described in "Producer Set Enrollments" is used to select the producer set. Would-be producers are ranked by these BTC expenditures, and the top 100 will be selected for the producer set.

## Producer Rewards

> Producers in the set receive a share of coinbase rewards and transaction fees for their produced blocks during a term. The coinbase reward is distributed proportionally based on BTC spent in producer set enrollments. All producers receive their share of the coinbase, regardless of block signing. Transaction fees are paid only to block signers, distributed based on their BTC spend in enrollments.

During a term, producers in the set are eligible to receive a portion of the coinbase rewards and transaction fees for blocks they produce. Since a term is defined as 10 Bitcoin blocks, the coinbase reward is equal to 10 times the coinbase. This amount is distributed to all producers in the set proportionally, based on the percentage of the total BTC spent in the producer set enrollments. All producers receive their portion of the coinbase, regardless of whether or not they signed the blocks produced by the set. The coinbase transaction should be the first transaction in a term.

The producer set is then incentivized to continue producing blocks throughout the term by the transaction fees. Transaction fees are paid only to producer set participants who signed the blocks produced. For each block, _B_, the total BTC spent by all signers block _B_ is computed, then the transaction fees for all transactions in block _B_ are distributed proportionally based on BTC spent by each signer in their producer set enrollment.

## Technical Requirements

The proposal includes a code audit, a network testbed with up to 1,000 Stacks nodes deployed worldwide, and ample testnet BTC for testing purposes.

- A code audit once the system is implemented
- A network testbed capable of deploying and running up to 1,000 Stacks nodes across the world in many different locations, as well as gathering diagnostic data from them while they run.
- Lots of testnet BTC

## Architectural Diagrams

Coming Soon
