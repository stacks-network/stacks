# Stacks Block Storage DB

Load and store Stacks block streams, interface with Stacks chain state, and sortition DB (_This does not encompass block-processing_). The work here will read from the existing Stacks chain state DB, but store new block data in separate tables (since the data we care about will be different).

## Dependencies

- [Block and transaction definitions](./block_and_transaction_definitions.md)
- [Stacks Block Storage Trait](./stacks_block_storage_trait.md)

## Requirements

- API for loading and storing streams of blocks to disk, and their signatures
- Recommendation: store a stream grouped by the starting checkpoint block and ending with the last block before the next checkpoint block
- A streaming state-machine for loading up and buffering a range of blocks and their signatures
- Trait implementations for the relevant chainstate accessor trait APIs
- Trait implementations for the Stacks Block Storage Trait

## Testable Interfaces

- The load/store API for Stacks blocks
- The storage streaming state-machine
- The trait implementations for the chainstate accessor
- Stacks Block Storage Trait implementation

## Properties of a successful implementation

- We have a fast, efficient mechanism for loading and storing blocks that is amenable to network access. We will need to benchmark it against alternative implementations.
- The streaming state-machine correctly reproduces the same sequence of bytes as the SIP-003-encoded list of blocks, regardless of how many or few bytes get fetched per iteration
