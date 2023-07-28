# Stacker DB Client

This is the task of producing a Stacker DB RESTful client crate, which downstream Rust projects can use to load and store StackerDB state.

## Dependencies

- [Stacker DB](./stacker_db.md)

## Requirements

- API to query a Stacker DB’s metadata
- API to query a Stacker DB’s chunk(s)
- API to sign new chunks
- API to upload new chunks
- APIs for generating all of the relevant messages to achieve the above

## Testable Interfaces

- All of the above

## Properties of a successful implementation

- Message-crafting should be separated from the act of sending it over a socket. The APIs for doing this should be public.
