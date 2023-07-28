# Chainstate Accessor Trait

API for querying Stacks and Bitcoin blocks, ancestors, consensus, and more. The purpose of this trait is to bridge between the old chainstate DBs and the new ones for read-only access.

## Dependencies

- none

## Requirements

- An API for querying Stacks blocks by index hash
- Return value indicates whether or not the block is processed
- An API for querying a Stacks block’s ancestor at a given height
- Only works for processed blocks
- An API for querying a range of Stacks blocks’ index hashes
- Only works for processed blocks
- An API for querying the canonical Stacks chain tip
- An API for querying a Bitcoin block’s header and burnchain operations
- An API for calculating a snapshot of a Bitcoin block
- We already have BlockSnapshot; we can make this into an enum to capture both the current sortition DB as well as the new snapshot DB state
- An API for querying the consensus hash of a Bitcoin block
- An API for querying a Bitcoin block’s ancestor at a given height
- An API for querying the canonical Bitcoin chain tip
- An API for validating Stacker signatures
- An API for validating block producer signatures
- An API for getting the producer set in a given tenure
- An API for getting the list of Stackers in a given reward cycle
- A mocked implementation of all of the above APIs

## Testable interfaces

- All of the above APIs

## Properties of a successful implementation

- We can use this accessor trait in place of all of the struct-specific connection and transaction objects that we currently use for reading chainstate from these various DBs
- The APIs exposed by the accessor are sufficient to allow us to mock the new modules we’re going to build so we can test them on synthesized data in isolation
