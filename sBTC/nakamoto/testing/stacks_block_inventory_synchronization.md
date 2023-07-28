# Stacks Block Inventory Synchronization

Network state-machine to query and verify blocks peers can serve. This module is expected to be much simpler than the one it replaces, because there are no forks and there are no missing PoX anchor blocks.

## Dependencies

- [Chainstate accessor trait](./chainstate_accessor_trait.md)

## Requirements

- P2P inventory message for querying a range of blocks and their signatures
- P2P inventory message for representing a range of blocks and their signatures
- In practice, this would be a set of checkpoint blocks and their signatures. If we can get the hashes of checkpoint blocks N-1 and N and authenticate their signatures, then we can do likewise for the range of blocks between them when we download them later.
- Network state machine for querying neighbors’ latest blocks and block histories, and authenticating peer set and stacker signatures on their hashes
- Relevant network accessor trait implementations

## Testable Interfaces

- Each step of the inventory synchronization state-machine
- Network accessor trait implementation

## Properties of a successful implementation

- A query for a range of blocks and their signatures can always be serviced with less than 1ms of wall-clock time
- Inventory state is only treated as authentic if the producer set and stacker set signatures are valid
- When the state-machine completes, the node knows the hashes of all checkpoint blocks, and can verify that each snapshot transaction corresponds to its identified checkpoint block.
