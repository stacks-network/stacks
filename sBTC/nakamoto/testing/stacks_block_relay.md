# Stacks Block Relay

Update the relayer thread to process newly-obtained block data and schedule blocks for relay.

## Dependencies

- [Stacks Block Storage Trait](./stacks_block_storage_trait.md)
- [Network Accessor Trait](./network_accessor_trait.md)

## Requirements

- Updated logic for representing newly-obtained streams of Stacks blocks and pushing them to neighbors

## Testable interfaces

- APIs for storing newly-discovered blocks
- APIs for selecting neighbors to receive blocks to relay

## Properties of a successful implementation

- All newly-obtained blocks are stored to the Stacks Blocks DB via the trait implementation
- No block is stored twice
- Blocks can be obtained and relayed out of order
