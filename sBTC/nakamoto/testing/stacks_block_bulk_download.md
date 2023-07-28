# Stacks Block Bulk Download

Network state-machine for downloading streams of Stacks blocks, based on inventory state.

## Dependencies

- [Chainstate Accessor Trait](./chainstate_accessor_trait.md)
- [Network Accessor Trait](./network_accessor_trait.md)

## Requirements

- A new RESTful API endpoint for querying a range of blocks, given a starting checkpoint block and an ending checkpoint block
- Network state machine for discovering and downloading new blocks

## Testable interfaces

- The RPC endpoint handlers
- Each step of the network state machine

## Properties of a successful implementation

- If any neighbor has a block that this local peer does not, then this local peer will receive a copy of the block from the first neighbor to successfully send it
- A block is never downloaded if we already have it
- A downloaded range of blocks must “connect” the identified starting and ending checkpoint blocks
- The downloaded range of blocks must be signed by the correct producer set and stackers
