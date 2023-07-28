# Block Producer Reference Implementation

This is the task of creating a block producer. It would leverage and supersede the miner code in the Stacks blockchain. The implementation would run as a separate process.

This task could be broken down further, but a lot of this work can be cribbed from the sBTC signer implementation and merging it with the [miner.rs](https://github.com/stacks-network/stacks-blockchain/blob/master/src/chainstate/stacks/miner.rs) file.

## Dependencies

- [Chainstate Accessor Trait](./chainstate_accessor_trait.md)
- [Stacker DB Client](./stacker_db_client.md)
- [Boot Contracts](./boot_contracts.md)

## Requirements

- The producer can walk through the mempool to find new transaction that can be mined, and do so efficiently
- The producer will create a valid block from mempool transaction
- The producer will use the .block-producers Stacker DB to find other producers and coordinate with them to produce a threshold FROST signature on the block
- If needed, the producer will query the stacker’s Stacker DB for historic but now orphaned blocks so as to determine the correct sequence of transactions to reply in order to recover from a Bitcoin fork

## Testable Interfaces

- The API for creating a block from a mempool DB and chainstate DB
- Each step of the reference implementation algorithm for coordinating with other producers

## Properties of a successful implementation

- A single producer can produce a valid block by itself with a 1-of-1 signature
- A set of producers can produce the same valid block with M-of-N signatures
