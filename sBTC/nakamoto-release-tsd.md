# Nakamoto Release | Technical Specification Document

## Executive Summary:

> 👉 _At a high-level what is The Nakamoto Release - its purpose, target audience, and benefits?_ > </br>

The Nakamoto Release proposes a new consensus protocol for Stacks blockchain, enhancing security and significantly reducing transaction confirmation latency to seconds.

This document describes a new consensus protocol for the Stacks blockchain, The Nakamoto Release, superseding the competitive mining protocol described in SIP-001 and SIP-007. In this proposed system, both miners and PoX stackers _cooperate_ through Byzantine fault-tolerant agreement to produce a linearized stream of confirmed transactions, in which the materialized view of the chainstate is periodically recorded to the Bitcoin blockchain.

This new arrangement allows for a significantly lower transaction confirmation latency time (_on the order of seconds instead of hours_), while also increasing the security budget of the chain from 51% of the miners' Bitcoin spends to _at least_ the sum of 67% of the miners' Bitcoin spends plus 67% of the total STX stacked. The chain's security budget reaches 51% of Bitcoin's mining power through periodic chainstate snapshots written to the Bitcoin chain by block producers and stackers, which are confirmed by the Bitcoin network as regular transactions. Once a Stacks chainstate snapshot is confirmed by the Bitcoin network, no subsequent Stacks fork can revert it -- any Stacks chain reorganization requires a Bitcoin chain reorganization.

### In summary, The Nakamoto Release:

- Replaces competitive mining (ratified in SIP-001 and SIP-00 with a cooperative system between miners and PoX stackers through Byzantine fault-tolerant (BFT) agreement that produces a linearized stream of confirmed transactions with periodic chainstate recording to Bitcoin blockchain.

### The impact of The Nakamoto Release, includes:

- A substantial reduction in transaction confirmation latency - from hours to seconds.
- An increased security budget: 67% of miners' Bitcoin spends + 67% of total STX stacked.
  - Reaching 51% of Bitcoin's mining power via periodic, irreversible Stacks chainstate snapshots, confirmed by the Bitcoin network.
  - Subsequent Stacks forks cannot revert confirmed snapshots; require Bitcoin chain reorganization.

## **Problem Statement:**

> 👉 _What specific problem does The Nakamoto Release solve?_ > </br>

Since activation in January of 2021, the Stacks network has operated with limitations due to single-leader block production. As a result, issues including high transaction latency, independent security budget, MEV, and unequal mining rewards have arisen. These problems stem from forking behavior and the lack of equitable rewards for minoritarian miners.

Per SIP-001, block production in Stacks executes through a single-leader process: in each Bitcoin block, several miners compete to win the right to append a block to the Stacks blockchain through a cryptographic sortition process. While this has served to keep the network running, it has several limitations:

- High transaction latency: Transactions are confirmed at the same rate as the underlying Bitcoin transaction -- that is, on the order of hours. Even then, there is no true finality, since like Bitcoin, Stacks employs Nakamoto consensus to achieve only a probabilistic agreement on whether or not a transaction was accepted by the network.
- Independent security budget: Because the Stacks blockchain can fork -- a consequence of its single-leader block production rules -- the cost to remove a transaction from the canonical fork is proportional to the amount of Bitcoin that miners have spent building atop it. The amount of Bitcoin is, in turn, proportional to the value of the STX coinbase, which is worth substantially less than the Bitcoin coinbase. Therefore, the cost to reorganize the Stacks blockchain to orphan a given transaction is substantially lower than the cost to do the same for a Bitcoin transaction (but in no case can a malicious party _hide_ their behavior without attacking Bitcoin, which mitigates the damage they can cause in practice).
- Miner-extractable value (MEV): Because Bitcoin miners may also be Stacks miners, a Bitcoin miner can guarantee that they win a Stacks block by excluding other miners' Bitcoin transactions from the Bitcoin blocks they produce. This has already happened with some F2Pool blocks, for example. Doing so is more profitable than mining honestly, because the Bitcoin miner can realize an arbitrarily high profit margin by tailoring their block-commit transaction to pay almost zero BTC to PoX recipients and omit a transaction fee.
- Unequitable mining rewards: Because the Stacks blockchain can fork, a majoritarian mining coalition can deliberately exclude the minority's blocks from the canonical fork. More banally, if a majority of Stacks miners (by Bitcoin spend) are not well-connected to the minority, they can accidentally exclude the minority's blocks simply because they do not arrive on their nodes in time to build atop them. At least one of these phenomena has been witnessed in practice. In either case, the minority does not receive any reward for their work.

Each of these problems arises from the fact that Stacks is a single-leader blockchain. In order to tolerate the failure of single leader to replicate a block or even produce a valid block, the Stacks chain must support blockchain forks in order to permit other miners to repair the canonical fork and "work around" missing or invalid block data. This forking behavior combined with single-leader block production creates an independent security budget, and permits Bitcoin miners to extract value from Stacks by preventing other Stacks miners from competing. The forking behavior prevents equitable mining rewards from being materialized for honest but minoritarian miners: the system _cannot_ reward minoritarian miners who produce non-canonical blocks lest it create incentives to selfish-mine or deliberately mine orphans. Without extra cooperation between miners, the current system forces Stacks transaction confirmation latency to be no lower than the underlying burnchain (Bitcoin) -- the best-effort nature of single-leader mining precludes requiring other miners to agree on the same chain tip before mining.

## **Solution:**

> 👉 _How does The Nakamoto Release provide a solution to the identified problem?_

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

In this proposed system, transaction confirmation latency now depends on how quickly a Stacks block that contains it can be produced and accepted. This takes on the order of seconds, instead of hours. In addition, the security budget of a transaction confirmed this way is substantially higher than it is today -- due to BFT agreement in steps 1 and 2, the cost to remove an already-confirmed but not-yet-finalized transaction is equal to the sum of 67% of the miners' Bitcoin spends since the last snapshot, plus 67% of the worth of the stackers' locked STX. At the time of this writing (1 STX = $0.63 USD, 1 BTC = $29,747 USD, Stacks reward cycle 63), this represents a security budget increase from $234.18 USD per block ($4,680.36 before a snapshot is expected to occur) to $213,908,185.70 -- five orders of magnitude higher! The requirement for miners and stackers to periodically snapshot the Stacks chain state further increases this budget to that of Bitcoin's security budget, regardless of how cheap or easy it may be in the future to monopolize subsequent Stacks block production.

Requiring miners and Stackers to cooperate to produce blocks mitigates the impact of Bitcoin miner MEV and allows for equitable coinbase reward distribution. Would-be Stacks miners have a reasonably long window of time (measured by Bitcoin blocks) to join a producer set, meaning that Bitcoin MEV miner would need to mine _every_ Bitcoin block in this window to monopolize Stacks mining. The requirement that miners collectively produce a block weighted by Bitcoin spends enables the Stacks blockchain consensus rules to distribute the STX coinbase _pro-rata_ to each miner in the producer set, and distribute the transaction fees _pro-rata_ to each miner who actively worked to approve the block. This ensures that honest minoritarian miners receive STX for their BTC while retaining an incentive for miners to pack as many high-value transactions into a block as possible.

## **Producer Set Terms and Block Production**

> 👉 Utilizing a single producer set, this approach emphasizes collaboration during fixed-length terms for block mining. To be valid, blocks must receive signatures from over 67% of the set's weighted public keys. Block production spans 10 Bitcoin blocks, treating Stacks blocks and microblocks without distinction. Each term enforces a cost limit of 10 times the Stacks 2.4 single block limit. Producers are selected based on their BTC spent on enrollments, with the top 100 being chosen. The primary goals of this proposal are to enhance mining efficiency and reduce transaction fees.

Rather than requiring competition among miners to mine blocks, each block is mined by a single, globally visible, producer set. A _producer set_ collaborates to mine blocks during fixed length _terms_. For a given term, every Stacks block is assembled and signed by a Byzantine fault-tolerant majority of that term's producer set.

The producer set is a collection of weighted public keys. Each member of the producer set is associated with a public key and is assigned a weight according to the proportion of Bitcoin committed during the term's selection (see [Producer Set Selection](#producer-set-selection)).

For a block to be validated, it must be signed by over 67% of the producer set by weight. The signature scheme uses a weighted extension of FROST threshold signatures, described in [Signature Generation](#signature-generation). A valid signature can be created if and only if this 67% threshold is achieved.

### **Block Production during a Term**

Each producer set term is 10 Bitcoin blocks in length. Stacks cost limits are applied to the term as a whole rather than individual Stacks blocks, and each term's cost limit is 10x the Stacks 2.4 single block limit (or the single block limit after improvements to the Clarity runtime and improved benchmark results).

During a term, there is no distinction between Stacks blocks and microblocks: there are only blocks. Terms are not limited to 10 Stacks blocks (i.e., there may be more than one Stacks block produced during a given Bitcoin block), but rather the only limit applied to the term is the overall cost limit (which may be increased through application of a VDF to accomodate an unusually long term length; see [Extension: Overdue Term](#overdue-terms)).

The first block of a term always builds off the last block stackers accepted from the prior term, which itself is a descendant of the last on-Bitcoin snapshot. Producers may not choose to reorganize a prior term, nor may they reorganize any stacker-accepted blocks. But, any unannounced or not-yet-accepted blocks from the prior term are dropped.

### **Producer Set Collaboration**

While this proposal specifies how blocks mined by a producer set are validated, it leaves open the question of exactly how producer sets collaborate to assemble blocks. This is intentional: the validation of blocks is consensus-critical, but exactly how a valid block gets mined is not. However, the Stacks blockchain codebase will need to supply a default method for this assembly. There are, however, two requirements that producer set must adhere to:

- A proposed block must be signed by at least 67% of the producer set, measured by BTC spend.
- There exists at most one proposed block at a given height with respect to a given Bitcoin fork.

If either requirement is not met, then stackers halt block acceptance for the remainder of the term.

This SIP proposes that producer sets undergo a leader election once the producer set is chosen (or the current leader becomes inactive). Leader elections proceed in rounds until a leader is chosen by 67% of the weighted producer set. At the start of a round, each node in the producer set waits a random amount of time. If it does not receive a request for a leadership vote before that timeout, it puts itself forward for leadership, and submits a vote request to every other participant. If a node receives a vote request and it has not already voted in that round or submitted its own leadership request, it signs the vote request.

The leader is responsible for assembling a block and sending it to each producer set participant to collect the threshold signatures. There are many possible extensions and variations to this protocol. For example, each participant could have some heuristic about the best transaction ordering for a block, and if the proposal deviates too much, the node could opt not to sign, or try to trigger a leadership change.

### **Producer Set Selection**

The producer set selection for term _N_ occurs during term _N-2_. Similar to the leader block commitments used in the current miner selection process, as defined in [SIP-001](https://github.com/stacksgov/sips/blob/main/sips/sip-001/sip-001-burn-election.md) and amended in [SIP-007](https://github.com/stacksgov/sips/blob/main/sips/sip-007/sip-007-stacking-consensus.md), would-be producers issue a Bitcoin transaction known as a producer set enrollment.

### **Producer Set Enrollments**

As it is today, this SIP requires block producers to register a VRF public key on the Bitcoin chain prior to enrolling in a producer set. The process and wire-formats are the same as in SIP-001; see [VRF key registration](https://github.com/stacksgov/sips/blob/main/sips/sip-001/sip-001-burn-election.md#leader-vrf-key-registrations).

Producer set enrollments have the same constraints on the Bitcoin transaction's inputs as PoX leader block commitments. Specifically, the first input of this Bitcoin operation must originate from the same address as the second output of the VRF public key registration transaction. The first output of a producer set enrollment must be an `OP_RETURN` with the following data:

0      2  3      7     11    13          46      50        52   80

|------|--|------|-----|-----|------------|-------|--------|--------|

magic  op tenure  key   key     signing   snapshot snapshot padding

number block txoff   pubkey    block    txoff

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

### **Enrollment Censorship Resistance**

The producer set enrollments for set _N_ can be included in any of the 10 Bitcoin blocks in producer set _N-2_. This makes it extremely difficult for a Bitcoin miner to censor these transactions, since to do so, they would need to control all 10 Bitcoin blocks in that term.

### **Selecting Producers**

Would-be producers with valid producer set enrollments in term _N-2_ are eligible to be included in the producer set for term _N_. The total number of producers in a set needs to be limited to prevent coinbase payouts from including too many accounts, as this could slow down event processing and even open a DoS vector. This cap will also prevent the block-signing process from becoming too CPU- and bandwidth-intensive. To this end, the total amount of BTC spent in the outputs described in "Producer Set Enrollments" is used to select the producer set. Would-be producers are ranked by these BTC expenditures, and the top 100 will be selected for the producer set.

## **Producer Rewards**

> 👉 Producers in the set receive a share of coinbase rewards and transaction fees for their produced blocks during a term. The coinbase reward is distributed proportionally based on BTC spent in producer set enrollments. All producers receive their share of the coinbase, regardless of block signing. Transaction fees are paid only to block signers, distributed based on their BTC spend in enrollments.

During a term, producers in the set are eligible to receive a portion of the coinbase rewards and transaction fees for blocks they produce. Since a term is defined as 10 Bitcoin blocks, the coinbase reward is equal to 10 times the coinbase. This amount is distributed to all producers in the set proportionally, based on the percentage of the total BTC spent in the producer set enrollments. All producers receive their portion of the coinbase, regardless of whether or not they signed the blocks produced by the set. The coinbase transaction should be the first transaction in a term.

The producer set is then incentivized to continue producing blocks throughout the term by the transaction fees. Transaction fees are paid only to producer set participants who signed the blocks produced. For each block, _B_, the total BTC spent by all signers block _B_ is computed, then the transaction fees for all transactions in block _B_ are distributed proportionally based on BTC spent by each signer in their producer set enrollment.

## **Blockchain Structure**

> 👉 To synchronize Stacks block production with newly-discovered Bitcoin state, this approach introduces "checkpoint transactions." Producers create these transactions for each new Bitcoin block, signaling Stacks nodes to process the Bitcoin block before Stacks blocks. Checkpoint transactions ensure that Stacks transactions dependent on Bitcoin state are processed after the referenced Bitcoin block. Each Bitcoin block must have one checkpoint transaction, arranged in the same order as the referenced Bitcoin blocks. The ability to create checkpoint transactions is exclusive to the producer set. The proposal also outlines the structure of Stacks blocks and the validation process for checkpoint blocks.

Because Stacks block production is no longer tied to Bitcoin block production, producers and stackers must explicitly determine the earliest Stacks block at which newly-discovered Bitcoin state can be queried. To achieve this, producers propose a special-purpose _checkpoint transaction_ for each new Bitcoin block they see that does not already have one.

A checkpoint transaction serves to identify the new Bitcoin block header and serve as a synchronization hint for Stacks nodes. When they see a block with a checkpoint transaction, Stacks nodes pause Stacks block-processing in order to ensure that they have first processed the identified Bitcoin block. Once they have done so, they can proceed to process this block and its descendants.

Checkpoint transactions are necessary to ensure that Stacks transactions which are causally-dependent on Bitcoin state are only processed once the referenced Bitcoin block has been processed. Checkpoint transactions also ensure that bootstrapping Stacks nodes validate Bitcoin-dependent Stacks transactions only once they have obtained the relevant Bitcoin state to do so. As such, there must exist one checkpoint transaction for each Bitcoin block, and they must be in the same order in the Stacks transaction history as the Bitcoin blocks they reference.

The Stacks blockchain is thus composed of long swaths of regular transactions punctuated by checkpoint transactions. If a block contains a checkpoint transaction, it must be the first transaction in that block. A block containing a checkpoint transaction is a _checkpoint block_.

Only the producer set can create a checkpoint transaction. This is enforced via the consensus rules, instead of via a transaction authorization structure. The contents of the transaction authorization structure for a checkpoint transaction are undefined -- it can contain any valid structure (i.e. the producer who proposed the block could simply sign it).

### **Block Structure**

This document proposes that the structure of a Stacks block now contains the following:

- A header:
- A version byte
- A 2-byte sequence number
- The SHA512/256 hash of its parent block
- The SHA512/256 hash of a Merkle tree containing the block's transactions
- A FROST Schnorr signature from the current producer set
- A bitmap of which producers contributed to the signature (used for determining transaction fee distribution)
- A body:
- A 4-byte big-endian unsigned integer, equal to the number of transactions the block contains
- The sequence of encoded Stacks transactions

### **Checkpoint Transaction Structure**

The checkpoint transaction contains information that today is found in anchored Stacks blocks (see SIP-005). At a high level, the payload for a checkpoint transaction contains:

- The total number of Stacks blocks so far
- The total amount of BTC spent to produce this chain as of the parent of this Bitcoin block
- A VRF proof
- The Stacks chainstate root hash as of the end of processing this block and all of its ancestors.
- The Bitcoin block header
- The consensus hash of the Bitcoin block
- VDF calibration data (see [Extension: Overdue Term](#extension-overdue-term))
- The location of the last-seen snapshot transaction in the Bitcoin chain

The wire formats for this new transaction can be found in Appendix B.

### **Block Validation**

As before, transactions are processed in order within their blocks, and blocks are processed in order by parent/child linkage. Block-processing continues until a checkpoint block is reached, at which the node must proceed to process the associated Bitcoin block. After the Bitcoin block has been processed, the node compares the Stacks chainstate root hash hash to the checkpoint transaction's root hash. If they do not match, then the checkpoint block is treated as invalid (and producers should try again to produce a checkpoint block for the given Bitcoin block). If they do match, then the next stream of regular blocks may be processed.

Each time a block is processed, the Stacks chainstate MARF index commits to the block's index hash and height, as well as its parent's index hash and height. The index hash is the SHA512/256 hash of the concatenation of the consensus hash of the last-processed Bitcoin block (i.e. this is committed to by the last checkpoint transaction), and the hash of the regular block's header. Previously, this commitment only occurred when processing anchored Stacks blocks, and not microblocks. This step is required for Clarity functions like `get-block-info?` to work correctly.

Because non-checkpoint Stacks blocks do not contain a new VRF proof, the VRF seed for each block is calculated as the SHA512/256 hash of the parent block's encoded header and the parent block's VRF seed. This value is returned by the `get-block-info?` function in Clarity for a given Stacks block.

### **Checkpoint Block Validation**

When processing a Stacks block with a checkpoint transaction, the node must ensure that there is exactly one checkpoint transaction, and it is the first transaction in the block.

The VRF proof generation and validation logic differs from the system today, because the VRF seed is no longer updated only once per Bitcoin block (but instead once per Stacks block). When a block producer proposes a checkpoint block, they calculate their VRF proof over the hash of the parent block's VRF seed concatenated with the new Bitcoin block's header hash. Nodes verify this proof as part of validating the checkpoint block.

### **Checkpoint Block Production**

Producers must create checkpoint transactions for each Bitcoin block in their tenure, as well as for any Bitcoin blocks in any prior tenures that have not yet received them (back to the last chain state snapshot transaction). This behavior is enforced by the consensus rules; each Stacks node independently watches the Bitcoin blockchain for new Bitcoin blocks, and will only accept a Stacks blockchain history with the appropriate checkpoint blocks in the right order.

When a producer sees a Bitcoin block, one of two things happen, depending on whether or not it sees a new Bitcoin block before its checkpoint block, or vice versa:

- If the producer sees a new Bitcoin block but not a checkpoint block for it, the producer immediately creates a checkpoint block for it and attempts to get other producers to sign it.
- If the producer sees a checkpoint block, it will immediately attempt to synchronize its view of the Bitcoin blockchain. If the checkpoint block corresponds to a newly-discovered Bitcoin block, and this Bitcoin block the _lowest_ such block without a checkpoint block, then it will immediately sign it.

Because Bitcoin block propagation is not inherently reliable, it is possible that other block producers are unable to validate it because they either have not seen the Bitcoin block, or have seen a sibling Bitcoin block on their view of the canonical Bitcoin fork. To overcome these inconsistencies, producers will continuously retry creating checkpoint blocks if they do not observe any other producers acting on an in-flight checkpoint block after a timeout passes.

In the event that a tenure ends before checkpoint blocks can be created for all of its Bitcoin blocks, the producer set in the subsequent tenure(s) must backfill the Stacks chain with missing checkpoint blocks.

In the event that a reward cycle change-over happens before all checkpoint blocks can be signed for the prior tenure, the new stackers may sign the checkpoint blocks from the old producers if they are available. Otherwise, the new producers will need to recreate them for the new stackers to sign (note that a reward cycle change-over is also the start of a new tenure).

## **Block Signing and Announcement**

> 👉 Block signing and announcement are integral to the Stacks blockchain. New blocks require signatures from the current tenure's producers and the current reward cycle's stackers. The involvement of stackers ensures block availability and transaction linearizability. Stacker DBs are introduced to facilitate FROST signature generation. Producers propose blocks, and 67% of producers' signers must sign a block for it to be valid. Stackers monitor the producer Stacker DB for valid blocks and append them to the blockchain. State snapshots are used to prevent conflicting chain histories. Stackers are incentivized to cooperate with producers to create snapshots.

Creating a new block requires two parties to sign it: the current tenure's producers, and the current reward cycle's stackers. The reasons for involving the stackers in this process are two-fold:

- **Block availability**. By requiring stackers to sign the block, the producers are compelled to divulge the blocks they produce. They cannot work on a hidden fork, nor can they build atop blocks that are not readily available to the peer network.
- **Transaction linearizability**. Stackers will only accept blocks that constitute a linearized transaction history. Even if producers create multiple conflicting blocks, at most one block will be appended to the Stacks chain. Moreover, if a Bitcoin fork arises that invalidates some Bitcoin-dependent transactions, Stackers ensure that any non-Bitcoin-dependent transactions that were previously accepted remain accepted (see "Extension: Fixed Transaction Orders").

### **Facilities for Signature Generation**

For each Bitcoin block, it is unambiguous as to which producer set and stacker set are active. All Stacks nodes which share the same view of the Bitcoin and Stacks chains can independently determine which tenure and reward cycle are active, and as such, can determine the public key(s) and Bitcoin spends of each producer, and the public key(s) and STX holdings of each stacker.

Producers and stackers use this information to bootstrap two FROST-generated public keys: one that represents the producers, and one that represents the stackers. A block is only appended to the Stacks chain if it contains two Schnorr signatures -- one from the producers and one from the stackers -- which are valid with respect to these two public keys.

The reader will recall that FROST is a threshold signature scheme in which _M_ out of _N_ (where _0 < M <= N_) signers cooperate to produce a single Schnorr signature. If all signers faithfully cooperate, they can generate signatures with a single round of communication per signature. However, this requires a pre-computation protocol to be executed by the signers beforehand.

In the pre-computation step, each signer must generate and share _N - 1_ encrypted messages with each other signer. When there are hundreds of signers, as will be the case for this proposal, the size of the digital representation of this data will be on the order of megabytes. Moreover, the pre-computation step must be re-executed each time the set of signers change, or if at least one signer misbehaved.

In order to employ FROST signing for block producers and stackers, this document defines a standard communication medium by which hundreds of signers can readily carry out the pre-computation step, accommodating even the degenerate case of having to perform it _N - M_ times in order to exclude the maximum number of _N - M - 1_ malicious signers that the protocol can tolerate while maintaining safety. The communication medium, called a _Stacker DB_ (described below), leverages every connected Stacks node to store and replicate the FROST pre-computation state, as well as store and forward signature generation messages.

By leveraging Stacks network infrastructure via Stacker DBs, producer and stacker signer implementations do not need to concern themselves with implementing durable data storage and highly-available communication. Instead, it is sufficient for these signer processes to contact a trusted Stacks node to send, store, and receive this data on its behalf. This significantly reduces the trusted computing base for producer and stacker signer implementations, and allows the block production process to benefit from independent improvements to the Stacks peer-to-peer network over time. Furthermore, it allows all Stacks nodes to monitor the behavior of block producers and signers, so they can detect and handle network partitions (see below).

**Stacker DBs**

To facilitate FROST key and signature generation for producers and stackers, the Stacks peer network will be extended to support Stacker DBs. A _Stacker DB_ is an eventually-consistent replicated shared memory system, comprised of an array of bound-length slots into which authorized writers may store a single chunk of data that fits into the slot's maximum size.

Stacks nodes exchange a list of up to 256 Stacker DBs to which they are subscribed when they exchange peer-to-peer handshake messages (see SIP-003). Each Stacks node maintains an ordered list of Lamport clocks, called a _chunk inventory_, for each slot in each Stacker DB replica it hosts, which it exchanges with peer Stacks nodes that host replicas of the same DB (note that this is _not_ a vector clock; write causality is _not_ preserved). Nodes exchange chunk data with one another such that eventually, in the absence of in-flight writes and network partitions, all replicas will contain the same state. Chunks with old version numbers are discarded by the node, and never replicated again once a new version is discovered.

Chunks are replicated asynchronously through the Stacks p2p network through gossipping. A Stacks node will periodically query neighbors who replicate the same Stacker DB for their replicas' chunk inventories, as well as the number of inbound and outbound neighbor connections this node currently has. If any slots are discovered that contain "later" versions than the local slot, the node will fetch that slot's chunk, authenticate it (see below), and store it along with an updated version. In addition, if the node discovers that it has the latest version of a chunk out of all neighbors and it discovers a neighbor with an older chunk, it will push its local chunk to the neighbor with probability inversely proportional to either the neighbor's reported number of total neighbors (if the local node treats this neighbor as an outbound neighbor), or to the reported number of outbound neighbors (if the local node treats this neighbor as an inbound neighbor).

Stacker DB clients (i.e. producers and stackers) read and write chunks via the node's RPC interface. The Stacker DB "read" endpoint returns the chunk data, the chunk version (as a Clarity value), and the chunk signer's compressed secp256k1 public key as a JSON struct, conforming to the following specification:

{

"chunk": {

"type": "string",

"pattern": "^[0-9a-fA-F]\*$"

},

"version": {

"type": "string",

"pattern": "^(0x)?00[0-9a-fA-F]{16}$"

},

"public_key": {

"type": "string",

"pattern": "^[0-9a-fA-F]{33}$"

}

}

Note that chunk versions are serialized Clarity unsigned integers.

A chunk with version `0x000000000000000000` is always an empty chunk, and has a `chunk` field with zero length. It is used to represent a chunk that has not been written. The content of the `public_key` field in this case is undefined.

A "write" to the Stacker DB occurs through an RPC endpoint. The "write" consists of the array index, the chunk version, the chunk data, and a recoverable secp256k1 signature over the aforementioned data. The node leverages the Stacker DB's smart contract to authenticate the write by passing it the array index, chunk version, chunk hash (SHA512/256), and signature via a read-only function called `stackerdb-auth-write`, whose signature is produced below:

(define-read-only (stackerdb-auth-write

(chunk-idx uint)

(chunk-version uint)

(chunk-hash (buff 32))

(chunk-sig (buff 65))))

The `auth-write` function evaluates to `true` if the write is allowed, or `false` if not. If `true`, then the Stacks node verifies that the version is equal to or greater than the last-seen version for this chunk. If it is equal, but the chunk is different, then the write will be accepted only if the hash of the chunk has strictly more leading 0's than the current chunk. If this is the case, or if the version is strictly greater than the last-seen version of this chunk, then the node stores the chunk locally, updates the DB's chunk inventory, and announces it to its peer nodes which replicate the Stacker DB. If authentication fails, or if the version is less than the last-seen version, or if the version is equal to the last-seen version and the hash of the new chunk has less than or equal leading 0-bits in its hash, then the Stacks node NACKs the RPC request with an HTTP 403 response.

The reason for accepting chunks with the same version but lesser hashes is to allow the system to both recover from and throttle nodes that equivocate. Automatically resolving conflicts that arise from equivocation keeps all Stacker DB replicas consistent, regardless of the schedule by which the equivocated writes are replicated. The use of the chunk hash to resolve equivocation conflicts makes it increasingly difficult for the writer to continue equivocating about the chunk for this version -- the act of replacing a chunk with version _V_ for _K_ times requires _O(2\*\*K)_ computing work in expectation. This, in turn, severely limits the amount of excess disk-writes the a Stacks node can be made to perform by the equivocating writer, and severely limits the number of distinct states that this version of the chunk can be in.

To support equivocation throttling in this manner, the chunk inventory for the Stacker DB encodes both the version and the number of leading 0-bits in the chunk's hash.

The node will periodically query the smart contract in a read-only fashion to determine if any chunks may be evicted. To determine the periodicity, the node queries the smart contract in a read-only fashion via its `stackerdb-garbage-collect?` function once per Bitcoin block processed:

(define-read-only (stackerdb-garbage-collect?))

This function evaluates to `true` if the node should begin garbage-collection for this DB, and `false` if not.

If the node should garbage-collect the DB, it will determine which chunks are garbage via the smart contract's `stackerdb-is-garbage?` function, whose signature is produced below:

(define-read-only (stackerdb-is-garbage?

(chunk-idx uint)

(chunk-version uint)

(chunk-hash (buff 32))

(chunk-sig (buff 65))))

If this function evaluates to `true`, then the chunk will be deleted and its version reset to `u0`. If `false`, then the chunk will be retained.

Further details of the Stacker DB wire formats, controlling smart contracts, and RPC endpoints can be found in Appendix A.

**Boot Contracts**

Each Stacks node must subscribe to two Stacker DB instances -- one for producers, and one for stackers -- in order to ensure that each producer and stacker can reliably participate in FROST signature generation. The producer Stacker DB contract is controlled through `SP000000000000000000002Q6VF78.block-producers` (henceforth referred to as `.block-producers` for brevity), and the Stacker DB contract for stackers is controlled through a new PoX contract `SP000000000000000000002Q6VF78.pox-4` (henceforth referred to as `.pox-4`). Only nodes that act as producers and/or stackers need to subscribe to these Stacker DBs; however, each producer and each stacker will need to subscribe to both.

Like with the PoX contract, the data spaces for these two contracts are controlled directly by the Stacks node. In particular, the data space for `.block-producers` is populated at the start of each term with the public keys of the tenure's block producers that will be used to validate DB chunks for the coming tenure, as well as data about the highest-known on-Bitcoin state snapshot. The public keys are obtained from the enrollment transactions on Bitcoin for this tenure.

The `.pox-4` contract will become the current PoX contract. This PoX implementation behaves identically to the current version, except in two ways. First, the signatures of the `stack-stx` and `delegate-stx` functions in `.pox-4` are modified to accept an additional `(buff 33)` argument, which encodes a compressed secp256k1 public key. This effectively requires stackers to supply a chunk-signing key when they stack. Second, this state is stored in a new data map within `.pox-4`, which will be queried by the Stacker DB interface to authenticate chunk writes.

Both contracts will have read-only getter functions so that other smart contracts can query the chunk-signing keys for their own purposes.

### **Signature Generation**

In both `.block-producers` and `.pox-4`, the concept of "signature weight" is embodied by the number of signers that each producer or stacker represents. A _signer_ in this context refers to a fixed-sized portion of the threshold signature. For block production, there are 100 signers, and at least 67 of them must participate to produce a valid block signature. For stacker signing, there are up to 4,000 signers (one for each claimed reward slot), of which 67% must participate (up to 2,680 signers).

**Producer DB Setup**

The `.block-producers` contract defines a Stacker DB with 300 slots. The first 100 slots store the pre-computed FROST state for each signer, slots 100-199 are used to store in-flight signature generation state for FROST, and slots 200-299 store proposed block data. The signers are assigned to a tenure's producers in quantities proportional to their share of Bitcoin spent. At the start of tenure N, it evicts all signing state for tenure N-1 by garbage-collecting each chunk. It then determines how many slots to allot each producer by distributing them in a round-robin fashion from smallest producer by Bitcoin spend to largest producer by Bitcoin spend. It breaks ties by sorting each tied producers' last enrollment transaction IDs in lexographic order.

The number of DB signer slots are assigned to a producer represents the weight of the producer's signature. For example, if four producers each registered for tenure N, and each spent 10%, 20%, 30%, and 40% of the BTC, then the 10% producer would receive 10 slots, the 20% producer would receive 20 slots, the 30% 30 slots, and the 40% 40 slots. The 10% producer receives DB slots 0, 10, 20, 30, 40, 50, 60, 70, 80, ... 180, and 190; the 20% producer receives DB slots 1, 2, 11, 12, 21, 22, ..., 191, and 192; the 30% producer receives DB slots 3, 4, 5, 13, 14, 15, 23, 24, 25, ..., 193, 194, and 195; the 40% producer receives DB slots 6, 7, 8, 9, 16, 17, 18, 19, ..., 196, 197, 198, and 199. The `.block-producers` contract's `stackerdb-auth-write` function ensures that each producer can only write to their assigned slots; the requisite state for doing so is directly written into the contract's data space at the start of each tenure, which this function queries.

The proposed block slots are alloted to producers in ascending order by BTC weight. In the above example, slot 200 is alloted to the 10% producer, slot 201 to the 20% producer, slot 202 to the 30% producer, and slot 203 to the 40% producer. If there are fewer than 100 producers, then the remaining slots are unused.

**Producer Signing Protocol**

When the FROST pre-computation step is executed, each producer generates their signers' data and uploads them to their assigned slots. The producer then fetches and decrypts the messages from the other producers' signers in order to obtain the necessary FROST state required to produce signatures.

When proposing blocks, each block producer may submit a candidate assembled block to their assigned block slots (i.e. slots 200-299) for other producers to see. Producers then collectively decide on which candidate block to sign. The protocol for agreeing on the block is implementation-defined and not consensus-critical, but this document requires the implementation to provide a necessary ingredient to Byzantine fault-tolerant implementations: each block must be signed by at least 67% of the producers' signers.

The signed block is automatically propagated to stackers via the `.block-producer` Stacker DB.

**Stacker Signer DB Setup**

Like the `.block-producers` contract, the `.pox-4` contract maintains a set of DB slots for storing FROST pre-computed data and signature data. The stacker signer DB has 8,000 slots. The first 4,000 are allotted to stackers based on how many reward slots they earn. These slots are assigned to stackers in contiguous ranges, based on the order in which their STX were stacked for this reward cycle (i.e. as determined by the `.pox-4` contract's `reward-cycle-pox-address-list` map), and are used to hold each stackers' signers' FROST pre-computation state. The last 4,000 are similarly alloted to stackers, but are used to contain in-flight signature metadata regarding the proposed block.

**Stacker Signing Protocol**

Stacker signers monitor the producer Stacker DB to watch for a completed, valid, sufficiently-signed producer-proposed block. If such a block is created, then each stacker attempts to append the block to its local node's chainstate. If the block is acceptable, then stackers execute the distributed FROST signature algorithm to produce the signature by storing their signature shares to their allotted signature slots. Once enough signature slots have been acknowledged and filled for this block, then the block and both producer and stacker signatures are replicated to the broader peer network. Note that block replication can happen independent of signature replication; future work may leverage this property to implement an optimistic eager block replication strategy and a fast _post-hoc_ signature-replication strategy to speed the delivery of blocks from producers to the rest of the network.

Because the block production algorithm is implementation-defined, stackers must take the utmost care in choosing whether or not to append a produced block to the blockchain. The produced block must meet the following criteria:

- It must be valid under the consensus rules
- At least 67% of producers' signers have signed the block
- There must not exist another block at the same height on the same Bitcoin fork

If producers equivocate and create two valid but different blocks for the same Stacks height, then stackers should not only refuse to sign it, but also stackers should refuse to sign any further blocks from that tenure.

If the underlying Bitcoin chain forks, then stackers may need to sign a producer block with the same Stacks block height as an existing Stacks block but happens to be evaluated against a different Bitcoin fork. Stackers determine which Bitcoin fork by examining the sequence of checkpoint transactions in the ancestors of the block.

### **State Snapshots**

Once per tenure, stackers and the producer set create a "snapshot" Bitcoin transaction that contains a recent digest of the Stacks chain history. Specifically, the stackers and producer set who are active in tenure N must send a snapshot transaction that contains the hash of the last block produced in tenure N-2 (i.e. the block that all blocks in tenure N-1 build upon, which has subsequently received at least 10 Bitcoin confirmations). The presence of this transaction in the Bitcoin chain prevents any future set of producers and stackers from producing a conflicting chain history. All blocks represented by the snapshot transaction are treated as finalized -- the act of creating an alternative transaction history is tantamount to reorganizing the Bitcoin chain to remove conflicting snapshot transactions.

Crafting and sending this transaction is not free, so its creation must be incentivized by the consensus rules. To ensure that it gets created and mined on-time, the producer block reward disbursal for tenure N will not happen until a snapshot for tenure N-2 _or later_ is mined on Bitcoin. To similarly incentivize stackers to cooperate with producers to create the snapshot, PoX payouts during subsequent tenures are diverted to a Bitcoin burn address and their STX are indefinitely locked until the snapshot for tenure N-2 (or later) is mined on Bitcoin. In other words, producers and stackers can only get paid if they create and broadcast the snapshot on Bitcoin in a timely fashion. To avoid missed payments, stackers and producers are encouraged to produce the snapshot for tenure N-2 at the start of tenure N.

The wire format for a snapshot transaction's `OP_RETURN` payload is as follows:

0      2  3       7                 39                        80

|------|--|-------|------------------|-------------------------|

magic  op  tenure   block hash        padding

id

Where `op = 0x73` (ASCII `s`) and:

- `tenure_id` is the tenure number (i.e. N-2)
- `block_hash` is the index hash of the last checkpoint block in the identified tenure

In addition, the snapshot transaction must contain at least two inputs: a FROST-generated Schnorr signature from the producer set in tenure N, and a FROST-generated Schnorr signature from the stackers in the current reward cycle. The producer set funds the transaction fee; the stackers sign the transaction with `SIGHASH_ANYONECANPAY`.

### **Liveness Incentives**

The producer set is incentivized to produce blocks and snapshot transactions because if either process stops, then the STX coinbase and transaction fees also stop.

The stackers are incentivized to sign snapshot transactions, but what incentivizes them to validate and sign producer blocks? The answer is sBTC (see SIP-021). Stackers are already incentivized to accept blocks that materialize sBTC from deposits and dematerialize sBTC from withdrawals. If they do not complete these tasks in a timely fashion, then their PoX rewards are diverted to a burn address and their STX are indefinitely locked until all unfulfilled sBTC deposits and withdrawals are handled. In addition, stackers are incentivized to sign blocks that contain their own stacking operations, so that they can continue to receive PoX rewards.

This is enough to drive stacker liveness. In order to process a stacking or sBTC (de)materialization operation in Stacks block _N_, the stacker must process and accept all blocks prior to _N_. Therefore, stackers will continuously accept valid blocks from producers so that they will be able to complete these actions on-time.

## **sBTC Concerns**

> 👉 Notable changes are proposed for the sBTC system (**SIP-021**) in the Stacks blockchain. These changes include delaying sBTC materialization until Bitcoin transactions receive at least one tenure of confirmations, simplifying sBTC transfers as regular SIP-010 token transfers without requiring materialization on the Bitcoin chain, and eliminating the need for unconfirmed or frozen blocks and stacker blessings since Stacks no longer experiences forks. These modifications effectively address concerns related to sBTC operations and consensus rules in the Stacks blockchain.

This SIP proposes incorporating the sBTC system described in **SIP-021**, but with the following changes.

### **sBTC Wallet Operations**

The act of sending BTC to the stacker-controlled Bitcoin wallet would not materialize sBTC until the Bitcoin transaction had received at least one tenure of Bitcoin confirmations. Similarly, withdrawing BTC for sBTC would require at least one tenure of Bitcoin confirmations before its effects materialized on Stacks, as would transferring the wallet's BTC from one set of stackers to the next. Because there are no longer any Stacks forks, a BTC withdrawal would no longer require 150 Bitcoin confirmations.

### **sBTC Transfers**

Because Stacks no longer forks, sBTC transfers would be treated as any other SIP-010 token transfer. They can be mined as quickly as any other Stacks transaction, and do not need to be materialized on the Bitcoin chain.

### **sBTC Consensus Rules**

Because Stacks no longer forks, there is no longer a need for the system to identify blocks as unconfirmed or frozen. Also, there is no longer a need for stacker blessings. Instead, this document makes it so that the concerns these protocols were meant to address no longer arise.

## **Extension: Fixed Transaction Orders**

> 👉 An extension is proposed to manage fixed transaction orders in the Stacks blockchain. Its primary goal is to handle potential inconsistencies caused by short-lived Bitcoin forks. The extension introduces speculative execution for Bitcoin-dependent transactions, enabling processing with the understanding that there might be a risk of invalidation during a fork event. In case of a Bitcoin fork, the Stacks blockchain ensures that Stacks transactions are reprocessed in the same order as initially accepted, and any invalid transactions are treated as runtime errors. Additionally, the proposal addresses sBTC wallet operations and indicates potential future work on taint tracking for confirming volatile state.

This document proposes that Stacks continue to support on-Bitcoin transactions for `stack-stx`, `transfer-stx`, and `delegate-stx`. However, the absence of Stacks forks makes it possible for non-finalized Stacks chain state to become inconsistent with the Bitcoin chain. For example, if Alice send 10 STX to Bob via a `stack-stx`, but the `stack-stx` is mined in a Bitcoin block that later gets orphaned, then Alice's and Bob's new balances are inconsistent with Bitcoin -- a node attempting to bootstrap from the Bitcoin and Stacks chains would not process the now-missing `stack-stx` transaction, and would be unable to authenticate the Stacks blocks against subsequent state snapshots (and thus be unable to finish booting).

Bitcoin forks are rare events, and forks lasting longer than six blocks are extremely unlikely. This document proposes that a Bitcoin transaction which receives at least one tenure of Bitcoin confirmations (i.e. at least 10 Bitcoin confirmations) is sufficiently confirmed that it can be assumed that it will remain confirmed forever.

Nevertheless, short-lived Bitcoin forks arise often. A naive stawman way of dealing with Stacks chain state inconsistency created by these short-lived forks is presented below for illustrative purposes:

- Process all on-Bitcoin transactions at the end of the block, instead of the beginning (as it is done today). Then, the transactions in the block that are not on-Bitcoin are at least not causally-dependent on the on-Bitcoin transactions.
- Do not process on-Bitcoin transactions that arise in tenure N until the state snapshot for tenure N is mined. This all but guarantees that these on-Bitcoin transactions will never be orphaned.
- Report only Bitcoin data as of the last state snapshot via Clarity functions. For example, `get-burn-block-info?` would only report Bitcoin state up to the Bitcoin block which contained the last state snapshot.

While this naive approach would work, the problem is that the second and third requirements introduce a very high transaction confirmation latency for Bitcoin-dependent transactions -- users would need to wait for over two tenures (over 20 Bitcoin blocks) before their Bitcoin-dependent transactions could be processed.

Because Bitcoin forks are rare, this document proposes a form of speculative execution whereby Bitcoin-dependent transactions are processed as soon as they are available (and Bitcoin-dependent information exposed to Clarity as soon as available), but with the caveat that unfinalized transactions may be discarded if a fork arises. To minimize the disruption this would cause, stackers require that producers

### **Recovery from Bitcoin Forks**

In the event that a Bitcoin fork arises and invalidates transactions, the Stacks blockchain would guarantee that all Stacks transactions (but not on-Bitcoin transactions) are reprocessed in the same order that they were initially accepted. Stackers will only sign produced blocks that contain the same Stacks transactions as before. However, it is possible that not all Stacks transactions will be valid, since they may be causally dependent on Bitcoin state that is no longer canonical. For this reason, transactions no longer invalidate Stacks blocks; the inclusion of an invalid transaction is treated as a runtime error in all cases.

Old Stacks blocks that contain potentially-invalid state are discarded.

### **Bitcoin Forks and sBTC**

The sBTC wallet operations already require sufficient Bitcoin confirmations that it is effectively guaranteed that they will never be orphaned by the time the producer set processes them. As such, sBTC by itself is not speculatively instantiated or destroyed -- it can only materialize or dematerialize once its deposit and withdraw transactions are sufficiently confirmed, Consequently, sBTC transfers will remain valid even when Stacks transactions are replayed to recover from Bitcoin forks.

### **Future Work: Taint Tracking**

A future SIP may propose that the Clarity VM performs taint-tracking on state that may still be volatile. This information is not consensus-critical. However, this information would be useful to off-chain services who need to determine whether or not state they intend to act upon is sufficiently confirmed by Bitcoin.

## **Extension: Overdue Term**

> 👉 This extension suggests the implementation of a replicated verifiable delay function (VDF) to manage variations in tenure length within the Stacks blockchain. Block producers execute the VDF and submit proofs to increase their tenure's execution budget in case it takes longer than anticipated. VDF calibration adjusts the required ticks for a valid proof based on historical tenure data. Checkpoint blocks report the adjusted tick count, which is then recorded on-chain for reference by Clarity contracts. The primary objective is to eliminate idle time and enhance overall efficiency within the Stacks network.

Naively, the execution budget available to block producers can be treated as equal to the number of Stacks blocks' budgets today, multipled by the tenure length. Ideally, block producers would produce blocks at a rate such that under network congestion, the tenure budget is completely consumed just as the tenure ends.

It is very difficult in practice to realize this idealized block production schedule, because the length of a tenure has very high variance and is not known in advance. If the block producers reach their tenure budget before the tenure is over, then the Stacks network stalls, which significantly increases transaction latency and degrades the user experience.

To eliminate these periods of idle time, this document proposes implementing a replicated verifiable delay function (VDF) which block producers individually run in order to prove that a tenure is taking too long. If enough block producers can submit VDF proofs that indicate that they have waited for the expected tenure length, then if the tenure is still ongoing, their tenure's execution budget is increased for an additional tenure. The process repeats indefinitely -- as long as block producers can submit VDF proofs, they earn more execution budget until their tenure is terminated by the arrival of the first Bitcoin block of the next tenure.

### **VDF Execution**

Concurrent with producing blocks, members of the producer set continuously evaluate a VDF for a protocol-defined number of "ticks" (i.e. one pass of the VDF's sequential proof-generation algorithm). The VDF proof must show that the producer evaluated the VDF for at least as many ticks.

Producers are incentivized to evaluate their local VDFs as quickly as possible, because gaining additional tenure execution budget means more transaction fees are available to them. Each time they can create a VDF proof, they submit it as a transaction to the mempool. Because the tenure execution budget grows only once at least 67% of producers (weighted by BTC spend) submit a VDF proof, each producer is incentivized to confirm a new VDF proof transaction as soon as possible by including it in the next block they propose.

Once enough valid VDF proofs have materialized in the blockchain, the tenure's budget expands.

### **VDF Calibration**

The consensus rules for checkpoint blocks require that the first checkpoint block in a tenure reports an adjusted number of ticks required to produce a valid VDF proof in this tenure. The tick count is adjusted over many tenures such that a producer running the VDF as fast as they can in the current tenure would complete a VDF proof in the expected duration of the tenure (i.e. 100 minutes). The number of ticks can be adjusted up or down, depending on historical tenure data.

To calculate the minimum number of ticks for tenure N, a node will load the following data for the past 15 tenures (about 25 hours of data):

- The wall-clock time of the tenure, calculated as the difference in the UNIX epoch timestamps between the last and first Bitcoin blocks in the tenure (as an array `TIMES`). _ The consumed execution budget for the tenure (as an array `EXECUTION`). _ The minimum number of ticks for the tenure (as an array `TICKS`). \* The integer number of times the execution budget was increased in the tenure (as an array `EXCEEDED`).

The node then calculates the scaled average number of times the tenure budget was exceeded as:

s = (sum(TIMES) / 1500) \* (sum(EXCEEDED) / 15)

If `s >= 0.5`, then it means that in the average tenure in this sample, producers were able to earn expanded tenures with over 50% probability. This indicates that the tick count needs to be increased, because producers were able to regularly evaluate the VDF faster than the tenures completed. In this case, it is multiplicatively incrased by a factor of `min(2.0, s / 0.5)`, and rounded down to the nearest integer.

If `s < 0.5`, then in the average tenure, producers did not expand the budget over 50% of the time. This could be due to any of three reasons:

- The average tenure length was less than 10 minutes, so the budget was never exceeded and no VDF proofs were produced
- There was no network congestion, so producers simply didn't need to submit any VDF proofs
- There was network congestion, but the minimum tick count was so high that producers were unable to earn more budget to address it

We are interested in distinguishing that last case from the others, which do not warrant a minimum tick decrease. To do so, the node examines each consumed budget in `EXECUTION[i]` where `TIMES[i] > 6000`. If the majority of each such `EXECUTION[i]` contains a cost parameter that is over 95% of the allotted budget, we can infer that the network was congested but producers were unable to ask for more budget (i.e. Bitcoin didn't terminate their tenure early). In this case, the minimum tick count is multiplicatively decreased by a factor of `min(2.0, a)` where `a` is an adjusted scale factor, calculated to only consider tenures where producers really did need to increase the budget:

n = len(EXCEEDED[i] where TIMES[i] > 6000 and EXECUTION[i] has a near-full cost parameter)

a = (sum(TIMES) / 1500) \* (sum(EXCEEDED) / n)

The final tick count reported in the checkpoint block can be as low as 1, or as high as `u128::MAX`. The initial tick count will be calculated once a VDF implementation is written and tested.

The initial tick count is unconditionally used for the first 15 tenures.

### **VDF On-Chain State**

Each checkpoint block will contain a special-purpose transaction from the producers which contains the new tick count. Each Stacks node independently performs the VDF calibration above; the VDF calibration transaction merely announces it.

The VDF tick counts are recorded to a boot code contract `SP000000000000000000002Q6VF78.vdf`, and exposed via read-only functions so that Clarity contracts can act on them.

# break

# **Technical Requirements:**

> 👉 What technical requirements and criteria must The Nakamoto Release meet to be fully functional and successfully implemented?

The proposal includes a code audit, a network testbed with up to 1,000 Stacks nodes deployed worldwide, and ample testnet BTC for testing purposes.

- A code audit once the system is implemented
- A network testbed capable of deploying and running up to 1,000 Stacks nodes across the world in many different locations, as well as gathering diagnostic data from them while they run.
- Lots of testnet BTC

# break

# **Architectural Diagrams:**

Forthcoming

# break

# **Testing Plan:**

> 👉 _What is the comprehensive testing plan in place to ensure quality assurance?_

Broadly speaking, this workstream can be divided into the following testable blackbox modules. Each module will need to be implemented and tested completed before its listed dependencies. The modules can be summarized as follows:

**Testing Plan, Summarized:**

1. Verifiable Delay Function (VDF): Implement VDF for tenure extensions with calibration and validation functions.
2. Chainstate Accessor Trait: API for querying Stacks and Bitcoin blocks, ancestors, consensus, and more.
3. Network Accessor Trait: API for querying neighbor information and block inventories.
4. Block and Transaction Definitions: Logic for parsing and validating on-Bitcoin and Stacks transactions and blocks.
5. Snapshot DB: Store Bitcoin snapshot state, validate checkpoint transactions, and interface with burnchain DB.
6. Stacker DB: Create a distributed database for FROST signature data exchange and block decisions.
7. Stacks Block Storage Trait: API for committing processed Stacks blocks to storage.
8. Stacks Block Storage DB: Load and store Stacks block streams, interface with Stacks chain state, and sortition DB.
9. Stacks Block Inventory Synchronization: Network state-machine to query and verify blocks peers can serve.
10. Stacks Block Bulk Download: Network state-machine for downloading blocks based on inventory state.
11. Stacks Block Antientropy: Extend antientropy to push missing blocks to neighbors.
12. Stacks Block Relay: Update relayer to process and schedule new block data for relay.
13. Stacks Block Validation: Implement new block validation consensus rules.
14. Stacks Block Acceptance: Update blockchain state with a block's new information.
15. Boot Contracts: Create new boot contracts .pox-4, .block-producers, and .vdf.
16. Updated Chains Coordinator: Upgrade chains coordinator to use snapshot DB and adapt to new rules.
17. Threshold FROST Signatures: Port sBTC threshold FROST signature work to Stacks.
18. Stacker DB Client: Produce RESTful client crate for loading and storing StackerDB state.
19. Block Producer Reference Implementation: Create a block producer process for mining and coordination.
20. Stacker Signer Reference Implementation: Create a stacker signer process for coordination and block signing.

**Testing Plan, Detailed:**

## **Verifiable Delay Function (VDF)**

This is the VDF implementation that will be used to implement tenure extensions. I think we can crib this from an existing blockchain. If there’s an IETF RFC or equivalent standard (even if it’s pending), then that’d be even better.

- **Dependencies:** none
- **Requirements**
- A workable VDF implementation
- An initial VDF calibration, based on benchmarks on commodity hardware
- Validation and testing of the negative feedback loop for dynamically adjusting the VDF
- It may very well be that the negative feedback loop defined above will need to be changed
- **Testable interfaces**
- The VDF functions (setup(), prove(), verify())

## **Chainstate Accessor Trait**

This encompasses a new type of “accessor” that will be used to pull data from the burnchain DB, header DB, sortition DB, and stacks chainstate DB, as well as from new databases defined here. The purpose of this trait is to bridge between the old chainstate DBs and the new ones for read-only access.

- **Dependencies**: none
- **Requirements**
- An API for querying Stacks blocks by index hash
- Return value indicates whether or not the block is processed
- An API for querying a Stacks block’s ancestor at a given height
- Only works for processed blocks
- An API for querying a range of Stacks blocks’ index hashes
- Only works for processed blocks
- An API for querying the canonical Stacks chain tip
- An API for querying a Bitcoin block’s header and burnchain operations
- An API for calculating a snapshot of a Bitcoin block
- We already have BlockSnapshot ; we can make this into an enum to capture both the current sortition DB as well as the new snapshot DB state
- An API for querying the consensus hash of a Bitcoin block
- An API for querying a Bitcoin block’s ancestor at a given height
- An API for querying the canonical Bitcoin chain tip
- An API for validating Stacker signatures
- An API for validating block producer signatures
- An API for getting the producer set in a given tenure
- An API for getting the list of Stackers in a given reward cycle
- A mocked implementation of all of the above APIs
- **Testable interfaces**
- All of the above APIs
- **Properties of a successful implementation**
- We can use this accessor trait in place of all of the struct-specific connection and transaction objects that we currently use for reading chainstate from these various DBs
- The APIs exposed by the accessor are sufficient to allow us to mock the new modules we’re going to build so we an test them on synthesized data in isolation

## **Network Accessor Trait**

This encompasses the work required to create a trait definition for querying information from various PeerNetwork state machines. Some state machines need to read state in others, but we don’t want to block implementation work by waiting for dependent state machines to be available.

- **Dependencies**: none
- **Requirements**
- An API for iterating through the list of neighbors
- For each neighbor, this reports
- whether or not the neighbor is authenticated
- whether or not it is inbound or outbound
- estimated in-degree and out-degree of the neighbor
- last contact time
- last seen block height of this neighbor
- whether or not this neighbor is a bootstrap peer
- which stacker DBs this neighbor subscribes to
- NeighborKey
- An API for getting the block inventories from neighbors
- **Testable interfaces**
- All of the above
- **Properties of a successful implementation**
- This trait can be implemented for PeerNetwork and can be mocked for tests
- We can use this trait in some form for working on multiple network stack upgrades in parallel

## **Block and Transaction Definitions**

This encompasses all of the new types of transactions we will need to support

- **Dependencies**: Chainstate accessor trait
- **Requirements**
- The new on-Bitcoin transaction definitions, parsing, and validation logic
- The new Stacks transaction definitions, parsing, and validation logic
- The new Stacks block definitions, parsing, and validation logic
- **Testable interfaces**
- Implementations of StacksMessageCodec
- Implementations of each burnchain op’s parse_data() and parse_from_tx() functions
- Block validation logic
- **Properties of a successful implementation**
- All validation logic is read-only

## **Snapshot DB**

This is a novel database that will store Bitcoin snapshot state derived from the burnchain DB, and used to validate checkpoint transactions. It will need to be able to read from the Sortition DB, but the data it produces will live in a separate table. The design and implementation of this is otherwise somewhat green field.

- **Dependencies:** Chainstate accessor trait
- **Requirements**
- Trait definitions that wrap the connection and transaction structs for the sortition DB, so that the rest of the codebase can read from either the sortition DB or snapshot DB with the same API (if at all possible)
- Load/store logic for Bitcoin block data
- Interfacing with the burnchain DB
- Interfacing with the chains coordinator
- Trait implementations for the relevant chainstate accessor trait APIs
- **Testable Interfaces**
- The connection and transaction objects
- The database connection/instantiation function
- Any schema migration or data import logic from the sortition DB
- **Properties of a successful implementation**
- ACID guarantee for new Bitcoin state

## **Stacker DB**

This is a novel distributed database that producers and stackers use to communicate their FROST signature data to one another, as well as their decisions on which blocks to create.

- **Dependencies**: Network accessor trait
- **Requirements**
- P2P message definitions and validation logic
- RPC API
- Local database for storing DB state
- State machine for replica discovery and synchronization
- Throttling and rate-limiting against overly-chatty or misbehaving replicas
- **Testable Interfaces**
- P2P message StacksMessageCodec implementations
- DB connection and transaction objects:
- For load/store of stacker DB chunks
- Each state machine step, with explicit pre/post-conditions to validate the state transition
- Smart contract callbacks for write authentication and garbage-collection
- Throttling and rate-limiting statistical reports
- **Properties of a successful implementation**
- End-to-end reachability (eventually, all replicas are reachable from all peers)
- End-to-end replication (eventually, all replicas have the same state)
- Partition recovery (peers re-achieve end-to-end reachability)
- Only correct peers remain connected; all bad peers are throttled or banned

## **Stacks Block Storage Trait**

This encompasses a trait definition for committing a processed stacks block to disk.

- **Dependencies**: Block and transaction defintions
- **Requirements**:
- An API for writing an unprocessed block to storage for later processing
- An API for finding the next block to process
- An API for attempting to process the block
- **Testable interfaces**
- All of the above
- **Properties of a successful implementation**
- We can use this trait to mock the chainstate DBs faithfully enough that we can blackbox test other modules in isolation, without doing any disk I/O

## **Stacks Block Storage DB**

This encompasses the work needed to store streams of blocks into the Stacks chain state. This does not encompass block-processing. The work here will read from the existing Stacks chain state DB, but store new block data in separate tables (since the data we care about will be different)

- **Dependencies**: Block and transaction definitions, Stacks Block Storage Trait
- **Requirements**:
- API for loading and storing streams of blocks to disk, and their signatures
- Recommendation: store a stream grouped by the starting checkpoint block and ending with the last block before the next checkpoint block
- A streaming state-machine for loading up and buffering a range of blocks and their signatures
- Trait implementations for the relevant chainstate accessor trait APIs
- Trait implementations for the Stacks Block Storage Trait
- **Testable Interfaces**
- The load/store API for Stacks blocks
- The storage streaming state-machine
- The trait implementations for the chainstate accessor
- Stacks Block Storage Trait implementation
- **Properties of a successful implementation**
- We have a fast, efficient mechanism for loading and storing blocks that is amenable to network access. We will need to benchmark it against alternative implementations.
- The streaming state-machine correctly reproduces the same sequence of bytes as the SIP-003-encoded list of blocks, regardless of how many or few bytes get fetched per iteration

## **Stacks Block Inventory Synchronization**

This encompasses a new network state-machine for determining which Stacks blocks a remote peer can serve. This module is expected to be much simpler than the one it replaces, because there are no forks and there are no missing PoX anchor blocks.

- **Dependencies:** Chainstate accessor trait
- **Requirements**
- P2P inventory message for querying a range of blocks and their signatures
- P2P inventory message for representing a range of blocks and their signatures
- In practice, this would be a set of checkpoint blocks and their signatures. If we can get the hashes of checkpoint blocks N-1 and N and authenticate their signatures, then we can do likewise for the range of blocks between them when we download them later.
- Network state machine for querying neighbors’ latest blocks and block histories, and authenticating peer set and stacker signatures on their hashes
- Relevant network accessor trait implementations
- **Testable Interfaces**
- Each step of the inventory synchronization state-machine
- Network accessor trait implementation
- **Properties of a successful implementation**
- A query for a range of blocks and their signatures can always be serviced with less than 1ms of wall-clock time
- Inventory state is only treated as authentic if the producer set and stacker set signatures are valid
- When the state-machine completes, the node knows the hashes of all checkpoint blocks, and can verify that each snapshot transaction corresponds to its identified checkpoint block.

## **Stacks Block Bulk Download**

This encompasses a new network state-machine for downloading streams of Stacks blocks, based on inventory state.

- **Dependencies**: Chainstate Accessor Trait, Network Accessor Trait
- **Requirements**:
- A new RESTful API endpoint for querying a range of blocks, given a starting checkpoint block and an ending checkpoint block
- Network state machine for discovering and downloading new blocks
- **Testable interfaces**
- The RPC endpoint handlers
- Each step of the network state machine
- **Properties of a successful implementation**
- If any neighbor has a block that this local peer does not, then this local peer will receive a copy of the block from the first neighbor to successfully send it
- A block is never downloaded if we already have it
- A downloaded range of blocks must “connect” the identified starting and ending checkpoint blocks
- The downloaded range of blocks must be signed by the correct producer set and stackers

## **Stacks Block Antientropy**

This encompasses the work needed to extend the antientropy state machines to push blocks to neighbors that don’t have them

- **Dependencies**: Chainstate Accessor Trait, Stacks Block Storage Trait, Network Accessor Trait
- **Requirements**
- A new RESTful API endpoint for receiving a pushed range of blocks between two consecutive checkpoint blocks
- Network state machine for identifying neighbors with missing blocks (based on synchronized inventory data), and pushing the missing blocks to them
- **Testable Interfaces**
- The RPC endpoint handler for pushed block streams
- Each step of the network state machine
- **Properties of a successful implementation**
- Each neighbor of the local peer that does not have blocks that this peer does will receive a copy of them pushed to their endpoint
- This peer pushes a bound amount of data per state machine pass, so as not to DoS the remote peer
- This peer sends data probabilistically, based on the in-degree and out-degree of the remote peer’s neighbor links, such that the odds of the remote peer receiving duplicate data from other peers who can also serve it missing data are low

## **Stacks Block Relay**

This encompasses the work needed to update the relayer thread to process newly-obtained block data and schedule blocks for relay.

- **Dependencies**: Stacks Block Storage Trait, Network Accessor Trait
- **Requirements**
- Updated logic for representing newly-obtained streams of Stacks blocks and pushing them to neighbors
- **Testable interfaces**
- APIs for storing newly-discovered blocks
- APIs for selecting neighbors to receive blocks to relay
- **Properties of a successful implementation**
- All newly-obtained blocks are stored to the Stacks Blocks DB via the trait implementation
- No block is stored twice
- Blocks can be obtained and relayed out of order

## **Stacks Block Validation**

This is the new block validation consensus rules.

- **Dependencies**: Verifiable Delay Function, Block and Transaction Definitions, Chainstate Accessor Trait
- **Requirements**
- Block validation according to consensus rules
- Block processing according to consensus rules
- **Testable Interfaces**
- Block validation API
- Block processing API
- **Properties of a successful implementation**
- Block storage and validation logic happen in different, distinct functions
- All consensus rules are observed
- A block is processed exactly once — it is either accepted or rejected
- Blocks are processed in-order by parent/child linkage
- Forks are not permitted

## **Stacks Block Acceptance**

This is the act of updating the materialized view of the blockchain with a block’s new information

- **Dependencies**: Stacks Block Validation
- **Requirements**:
- The Stacks chainstate DB is updated and indexed to reflect all state transitions in a block’s transactions
- **Testable Interfaces**
- The API for committing a block to persisted storage
- **Properties of a successful implementation**
- A block’s effects are only visible after it is processed
- No block can be accepted twice
- All Clarity built-ins and account functionality works as it did before
- Rollbacks and replays of unfinalized blocks are permitted (this is effectively supported today via the MARF)

## **Boot Contracts**

This encompasses creating the new .pox-4 and .block-producers boot contracts, as well as the .vdf boot contract

- **Dependencies**: Stacks Block Acceptance
- **Requirements**
- The block-processing logic inserts the relevant tenure data into .block-producers
- The block-processing logic inserts the relevant VDF data into .vdf
- The stacking operations’ method signatures are updated
- **Testable Interfaces**
- The public getters for .block-producers
- The public getters for .vdf
- The API for getting Stacker signing public keys
- **Properties of a successful implementation**
- The Clarity functions are able to serve as API endpoints to the producer set and stacker set

## **Updated Chains Coordinator**

This is the act of upgrading the chains coordinator subsystem to use the snapshot DB, and to cease caring about affirmation maps and other fork-sensitive data once this system’s rules go into effect

- **Dependencies**: Stacks Block Acceptance, Snapshot DB
- **Requirements**:
- The chains coordinator correctly processes Bitcoin and Stacks blocks using the old 2.4 rules up until Nakamoto (3.0) rules, and then switches over.
- **Testable Interfaces**
- All the same ones today, but under the switchover
- **Properties of a successful implementation**
- The chains coordinator no longer needs to unwind history or track block affirmations or detect PoX anchor blocks after 3.0 goes live.
- The chains coordinator only does the following:
- Process Stacks blocks between processed checkpoint block N and unprocessed checkpoint block N+1
- Process the Bitcoin block for N+1
- Process checkpoint block N+1
- Repeat

## **Threshold FROST Signatures**

This is the act of porting the sBTC threshold FROST signature work to the Stacks blockchain

- **Dependencies**: none
- **Requirements:**
- Weighted Threshold FROST works as expected
- **Testable Interfaces**
- Everything covered in the sBTC FROST library
- **Properties of a successful implementation**
- Producers and stackers can create threshold signatures which represent their respective signing weights

## **Stacker DB Client**

This is the task of producing a Stacker DB RESTful client crate, which downstream Rust projects can use to load and store StackerDB state.

- **Dependencies**: Stacker DB
- **Requirements**:
- API to query a Stacker DB’s metadata
- API to query a Stacker DB’s chunk(s)
- API to sign new chunks
- API to upload new chunks
- APIs for generating all of the relevant messages to achieve the above
- **Testable Interfaces**
- All of the above
- **Properties of a successful implementation**
- Message-crafting should be separated from the act of sending it over a socket. The APIs for doing this should be public.

## **Block Producer Reference Implementation**

This is the task of creating a block producer. It would leverage and supersede the miner code in the Stacks blockchain. The implementation would run as a separate process.

This task could be broken down further, but I suspect that a lot of this work can be cribbed from the sBTC signer implementation and merging it with the [miner.rs](https://miner.rs/) file.

- **Dependencies**: Chainstate Accessor Trait, Stacker DB Client, Boot Contracts
- **Requirements**:
- The producer can walk through the mempool to find new transaction that can be mined, and do so efficiently
- The producer will create a valid block from mempool transaction
- The producer will use the .block-producers Stacker DB to find other producers and coordinate with them to produce a threshold FROST signature on the block
- If needed, the producer will query the stacker’s Stacker DB for historic but now orphaned blocks so as to determine the correct sequence of transactions to reply in order to recover from a Bitcoin fork
- **Testable Interfaces**
- The API for creating a block from a mempool DB and chainstate DB
- Each step of the reference implementation algorithm for coordinating with other producers
- **Properties of a successful implementation**
- A single producer can produce a valid block by itself with a 1-of-1 signature
- A set of producers can produce the same valid block with M-of-N signatures

## **Stacker Signer Reference Implementation**

This is the task of creating a stacker signer. The implementation would run as a separate process.

This task could be broken down further, but I suspect that most of the work is going to be in cribbing the sBTC signer implementation and merging it with an API for querying unsigned blocks.

- **Dependencies**: Chainstate Accessor Trait, Stacker DB Client, Boot Contracts
- **Requirements**:
- The stacker can discover other stackers by looking at the .pox-4 Stacker DB
- The stacker can discover produced but not-yet-accepted blocks in the .block-producer Stacker DB
- The stacker can tentatively process produced blocks to check that they are valid
- The stacker can execute 2PC leader election to determine which stacker should coordinate signature share aggregation
- The stacker can execute the 2PC leader role by gathering signatures posted to the stacker DB, merging them, and propagating the signed block to the peer network
- The stacker can execute the 2PC follower role by posting signatures to the stacker DB
- The stacker can process newly-accepted blocks
- The stacker can identify equivocated blocks
- **Testable interfaces**
- Each step of the 2PC implementation, in each role
- API for detecting when leader election should occur
- **Properties of a successful implementation**
- Stackers successfully accept one valid block per Stacks block height
- Stackers detect producer equivocation and refuse to process any further blocks
- Stackers can recover from a split-brain where there are multiple competing leaders
- Stackers can compute the FROST signature quickly

# break

# **Deployment Plan:**

> 👉 _What does the deployment plan entail, including infrastructure requirements, deployment processes, and monitoring strategies?_

In short, this is a very big undertaking; almost as big as Stacks 2.0.

Fortunately, there are a lot of things that can be tested and deployed on mainnet without creating a hard fork. The pieces of infrastructure that I suspect will need by far and away the most testing (since they’re filled with unknown-unknowns) are the stacker DB implementation and the producer set and stacker signer FROST groups.

## Epic 1: **Stacker DB Rollout**

We can implement the stacker DB system well before anything else needs to be implemented. I recommend finishing the in-flight implementation and using it to try replicating databases of similar size to the producer and stacker signer DBs using Hiro and Foundation nodes. We can benchmark and improve the performance of replication concurrently with everything else

## Epic 2: **Producer and Signer Rollout**

Once we have Stacker DBs live, we can create mocked .pox-4 and .block-producer contracts on mainnet, which will allow us to test producer and stacker signer implementations. In particular, we can verify that:

- A set of producers will elect a leader
- The producer leader will create a valid mainnet block
- The producer set will sign that block
- The stackers will see the signed block, and sign it as well

We can build out the producer and stacker binaries in parallel — we can mock a produced block for stackers to sign, so stacker signers can be tested without producers being live.

## Epic 3: **Verifiable Delay Function Rollout**

We can test and calibrate the VDF implementation in a set of separate processes, which each post their statistics to a fake .vdf smart contract deployed on mainnet. This will give us some indication of how good the producers will be at executing it in a wide variety of environments, and how good our VDF calibration algorithm actually is when presented with mainnet data.

## Epic 4: **Blockchain Changes Rollout**

The bulk of the blockchain changes need to be tested via unit tests, property tests, and finally a testnet implementation. Fortunately, this can be done in parallel to the above, so that when it comes time to run 3.0 on the Bitcoin testnet, we’ll have a very robust Stacker DB and signer implementation.

The consensus rules, block snapshotting, block acceptance, network state machines, and so on can be tested with existing unit test and integration test tooling as they are completed. However, some degree of live testing will be necessary. I suggest the following rollout phases, based on what we did for Stacks 2.0:

### **Helium 3.0**

This is like the Helium testnet — there is one producer and one stacker, and they just produce and sign blocks at a fixed rate. This functions like a local devnet.

### **Neon 3.0**

This is like the Neon testnet. It’s public, but the set of producers and signers would be fixed and hard-coded. This is just to test producers’ ability to create blocks and stackers’ ability to accept them via their respective distributed agreement protocols.

### **Argon 3.0**

This extends Neon with producers chosen from tenures, and signers chosen from stackers. This implementation contains the boot contracts.

### **Krypton 3.0**

This is the release we’d use to test the migration from the current testnet to the 3.0 testnet. We’d test the migration as many times as we need to until we’re convinced it works.

Krypton 3.0 is otherwise feature-complete.

### **Xenon 3.0**

This would become the new testnet. Xenon 3.0 launches from the mainline Stacks testnet using the migration logic we perfected in Krypton 3.0.
