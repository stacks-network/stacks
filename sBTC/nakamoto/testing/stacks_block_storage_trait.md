# Stacks Block Storage Trait

API for committing processed Stacks blocks to storage.

## Dependencies

- [Block and transaction definitions](./block_and_transaction_definitions.md)

## Requirements

- An API for writing an unprocessed block to storage for later processing
- An API for finding the next block to process
- An API for attempting to process the block

## Testable interfaces

- All of the above

## Properties of a successful implementation

- We can use this trait to mock the chainstate DBs faithfully enough that we can blackbox test other modules in isolation, without doing any disk I/O
