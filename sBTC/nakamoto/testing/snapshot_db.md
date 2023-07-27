# Snapshot DB

This is a novel database that will store Bitcoin snapshot state derived from the burnchain DB, and used to validate checkpoint transactions. It will need to be able to read from the Sortition DB, but the data it produces will live in a separate table. The design and implementation of this is otherwise somewhat green field.

## Dependencies

- [Chainstate accessor trait](./chainstate_accessor_trait.md)

## Requirements

- Trait definitions that wrap the connection and transaction structs for the sortition DB, so that the rest of the codebase can read from either the sortition DB or snapshot DB with the same API (if at all possible)
- Load/store logic for Bitcoin block data
- Interfacing with the burnchain DB
- Interfacing with the chains coordinator
- Trait implementations for the relevant chainstate accessor trait APIs

## Testable Interfaces

- The connection and transaction objects
- The database connection/instantiation function
- Any schema migration or data import logic from the sortition DB

## Properties of a successful implementation

- ACID guarantee for new Bitcoin state
