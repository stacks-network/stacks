# Blockchain Structure

> To synchronize Stacks block production with newly-discovered Bitcoin state, this approach introduces "checkpoint transactions." Producers create these transactions for each new Bitcoin block, signaling Stacks nodes to process the Bitcoin block before Stacks blocks. Checkpoint transactions ensure that Stacks transactions dependent on Bitcoin state are processed after the referenced Bitcoin block. Each Bitcoin block must have one checkpoint transaction, arranged in the same order as the referenced Bitcoin blocks. The ability to create checkpoint transactions is exclusive to the producer set. The proposal also outlines the structure of Stacks blocks and the validation process for checkpoint blocks.

Because Stacks block production is no longer tied to Bitcoin block production, producers and stackers must explicitly determine the earliest Stacks block at which newly-discovered Bitcoin state can be queried. To achieve this, producers propose a special-purpose _checkpoint transaction_ for each new Bitcoin block they see that does not already have one.

A checkpoint transaction serves to identify the new Bitcoin block header behaves as a synchronization hint for Stacks nodes. When they see a block with a checkpoint transaction, Stacks nodes pause Stacks block-processing in order to ensure that they have first processed the identified Bitcoin block. Once they have done so, they can proceed to process this block and its descendants.

Checkpoint transactions are necessary to ensure that Stacks transactions which are causally-dependent on Bitcoin state are only processed once the referenced Bitcoin block has been processed. Checkpoint transactions also ensure that bootstrapping Stacks nodes validate Bitcoin-dependent Stacks transactions only once they have obtained the relevant Bitcoin state to do so. As such, there must exist one checkpoint transaction for each Bitcoin block, and they must be in the same order in the Stacks transaction history as the Bitcoin blocks they reference.

The Stacks blockchain is thus composed of long swaths of regular transactions punctuated by checkpoint transactions. If a block contains a checkpoint transaction, it must be the first transaction in that block. A block containing a checkpoint transaction is a _checkpoint block_.

Only the producer set can create a checkpoint transaction. This is enforced via the consensus rules, instead of via a transaction authorization structure. The contents of the transaction authorization structure for a checkpoint transaction are undefined -- it can contain any valid structure (i.e. the producer who proposed the block could simply sign it).

## Block Structure

This document proposes that the structure of a Stacks block now contains the following:

- Header
  - A version byte
  - A 2-byte sequence number
  - The SHA512/256 hash of its parent block
  - The SHA512/256 hash of a Merkle tree containing the block's transactions
  - A FROST Schnorr signature from the current producer set
  - A bitmap of which producers contributed to the signature (used for determining transaction fee distribution)
- Body
  - A 4-byte big-endian unsigned integer, equal to the number of transactions the block contains
  - The sequence of encoded Stacks transactions

## Checkpoint Transaction Structure

The checkpoint transaction contains information that today is found in anchored Stacks blocks (see SIP-005). At a high level, the payload for a checkpoint transaction contains:

- The total number of Stacks blocks so far
- The total amount of BTC spent to produce this chain as of the parent of this Bitcoin block
- A VRF proof
- The Stacks chainstate root hash as of the end of processing this block and all of its ancestors
- The Bitcoin block header
- The consensus hash of the Bitcoin block
- VDF calibration data (see [Extension: Overdue Term](./extensions/overdue_term.md))
- The location of the last-seen snapshot transaction in the Bitcoin chain

The wire formats for this new transaction can be found in Appendix B.

## Block Validation

As before, transactions are processed in order within their blocks, and blocks are processed in order by parent/child linkage. Block-processing continues until a checkpoint block is reached, at which the node must proceed to process the associated Bitcoin block. After the Bitcoin block has been processed, the node compares the Stacks chainstate root hash to the checkpoint transaction's root hash. If they do not match, then the checkpoint block is treated as invalid (and producers should try again to produce a checkpoint block for the given Bitcoin block). If they do match, then the next stream of regular blocks may be processed.

Each time a block is processed, the Stacks chainstate MARF index commits to the block's index hash and height, as well as its parent's index hash and height. The index hash is the SHA512/256 hash of the concatenation of the consensus hash of the last-processed Bitcoin block (i.e. this is committed to by the last checkpoint transaction), and the hash of the regular block's header. Previously, this commitment only occurred when processing anchored Stacks blocks, and not microblocks. This step is required for Clarity functions like `get-block-info?` to work correctly.

Because non-checkpoint Stacks blocks do not contain a new VRF proof, the VRF seed for each block is calculated as the SHA512/256 hash of the parent block's encoded header and the parent block's VRF seed. This value is returned by the `get-block-info?` function in Clarity for a given Stacks block.

## Checkpoint Block Validation

When processing a Stacks block with a checkpoint transaction, the node must ensure that there is exactly one checkpoint transaction, and it is the first transaction in the block.

The VRF proof generation and validation logic differs from the system today, because the VRF seed is no longer updated only once per Bitcoin block (but instead once per Stacks block). When a block producer proposes a checkpoint block, they calculate their VRF proof over the hash of the parent block's VRF seed concatenated with the new Bitcoin block's header hash. Nodes verify this proof as part of validating the checkpoint block.

## Checkpoint Block Production

Producers must create checkpoint transactions for each Bitcoin block in their tenure, as well as for any Bitcoin blocks in any prior tenures that have not yet received them (back to the last chain state snapshot transaction). This behavior is enforced by the consensus rules; each Stacks node independently watches the Bitcoin blockchain for new Bitcoin blocks, and will only accept a Stacks blockchain history with the appropriate checkpoint blocks in the right order.

When a producer sees a Bitcoin block, one of two things happen, depending on whether or not it sees a new Bitcoin block before its checkpoint block, or vice versa:

- If the producer sees a new Bitcoin block but not a checkpoint block for it, the producer immediately creates a checkpoint block for it and attempts to get other producers to sign it.
- If the producer sees a checkpoint block, it will immediately attempt to synchronize its view of the Bitcoin blockchain. If the checkpoint block corresponds to a newly-discovered Bitcoin block, and this Bitcoin block the _lowest_ such block without a checkpoint block, then it will immediately sign it.

Because Bitcoin block propagation is not inherently reliable, it is possible that other block producers are unable to validate it because they either have not seen the Bitcoin block, or have seen a sibling Bitcoin block on their view of the canonical Bitcoin fork. To overcome these inconsistencies, producers will continuously retry creating checkpoint blocks if they do not observe any other producers acting on an in-flight checkpoint block after a timeout passes.

In the event that a tenure ends before checkpoint blocks can be created for all of its Bitcoin blocks, the producer set in the subsequent tenure(s) must backfill the Stacks chain with missing checkpoint blocks.

In the event that a reward cycle change-over happens before all checkpoint blocks can be signed for the prior tenure, the new stackers may sign the checkpoint blocks from the old producers if they are available. Otherwise, the new producers will need to recreate them for the new stackers to sign (note that a reward cycle change-over is also the start of a new tenure).
