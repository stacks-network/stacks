# Stacks Block Acceptance

This is the act of updating the materialized view of the blockchain with a block’s new information.

## Dependencies

- [Stacks Block Validation](./stacks_block_validation.md)

## Requirements

- The Stacks chainstate DB is updated and indexed to reflect all state transitions in a block’s transactions

## Testable Interfaces

- The API for committing a block to persisted storage

## Properties of a successful implementation

- A block’s effects are only visible after it is processed
- No block can be accepted twice
- All Clarity built-ins and account functionality works as it did before
- Rollbacks and replays of unfinalized blocks are permitted (this is effectively supported today via the MARF)
