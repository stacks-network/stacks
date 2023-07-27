# Stacker Signer Reference Implementation

This is the task of creating a stacker signer. The implementation would run as a separate process.

This task could be broken down further, but most of the work is going to be in cribbing the sBTC signer implementation and merging it with an API for querying unsigned blocks.

## Dependencies

- [Chainstate Accessor Trait](./chainstate_accessor_trait.md)
- [Stacker DB Client](./stacker_db_client.md)
- [Boot Contracts](./boot_contracts.md)

## Requirements

- The stacker can discover other stackers by looking at the .pox-4 Stacker DB
- The stacker can discover produced but not-yet-accepted blocks in the .block-producer Stacker DB
- The stacker can tentatively process produced blocks to check that they are valid
- The stacker can execute 2PC leader election to determine which stacker should coordinate signature share aggregation
- The stacker can execute the 2PC leader role by gathering signatures posted to the stacker DB, merging them, and propagating the signed block to the peer network
- The stacker can execute the 2PC follower role by posting signatures to the stacker DB
- The stacker can process newly-accepted blocks
- The stacker can identify equivocated blocks

## Testable interfaces

- Each step of the 2PC implementation, in each role
- API for detecting when leader election should occur

## Properties of a successful implementation

- Stackers successfully accept one valid block per Stacks block height
- Stackers detect producer equivocation and refuse to process any further blocks
- Stackers can recover from a split-brain where there are multiple competing leaders
- Stackers can compute the FROST signature quickly
