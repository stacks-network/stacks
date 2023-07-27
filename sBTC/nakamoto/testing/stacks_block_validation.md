# Stacks Block Validation

Implement new block validation consensus rules.

## Dependencies

- [Verifiable Delay Function](./verifiable_delay_function.md)
- [Block and Transaction Definitions](./block_and_transaction_definitions.md)
- [Chainstate Accessor Trait](./chainstate_accessor_trait.md)

## Requirements

- Block validation according to consensus rules
- Block processing according to consensus rules

## Testable Interfaces

- Block validation API
- Block processing API

## Properties of a successful implementation

- Block storage and validation logic happen in different, distinct functions
- All consensus rules are observed
- A block is processed exactly once — it is either accepted or rejected
- Blocks are processed in-order by parent/child linkage
- Forks are not permitted
