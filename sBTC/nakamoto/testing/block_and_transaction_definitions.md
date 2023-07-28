# Block and Transaction Definitions

Logic for parsing and validating on-Bitcoin and Stacks transactions and blocks.

## Dependencies

- [Chainstate accessor trait](./chainstate_accessor_trait.md)

## Requirements

- The new on-Bitcoin transaction definitions, parsing, and validation logic
- The new Stacks transaction definitions, parsing, and validation logic
- The new Stacks block definitions, parsing, and validation logic

## Testable interfaces

- Implementations of StacksMessageCodec
- Implementations of each burnchain op’s parse_data() and parse_from_tx() functions
- Block validation logic

## Properties of a successful implementation

- All validation logic is read-only
