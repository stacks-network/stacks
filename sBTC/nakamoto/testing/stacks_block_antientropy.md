# Stacks Block Antientropy

This encompasses the work needed to extend the antientropy state machines to push missing blocks to neighbors that don’t have them.

## Dependencies

- [Chainstate Accessor Trait](./chainstate_accessor_trait.md)
- [Stacks Block Storage Trait](./stacks_block_storage_trait.md)
- [Network Accessor Trait](./network_accessor_trait.md)

## Requirements

- A new RESTful API endpoint for receiving a pushed range of blocks between two consecutive checkpoint blocks
- Network state machine for identifying neighbors with missing blocks (based on synchronized inventory data), and pushing the missing blocks to them

## Testable Interfaces

- The RPC endpoint handler for pushed block streams
- Each step of the network state machine

## Properties of a successful implementation

- Each neighbor of the local peer that does not have blocks that this peer does will receive a copy of them pushed to their endpoint
- This peer pushes a bound amount of data per state machine pass, so as not to DoS the remote peer
- This peer sends data probabilistically, based on the in-degree and out-degree of the remote peer’s neighbor links, such that the odds of the remote peer receiving duplicate data from other peers who can also serve it missing data are low
