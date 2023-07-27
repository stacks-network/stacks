# Boot Contracts

Create the new .pox-4, .block-producers, and the .vdf boot contract.

## Dependencies

- [Stacks Block Acceptance](./stacks_block_acceptance.md)

## Requirements

- The block-processing logic inserts the relevant tenure data into .block-producers
- The block-processing logic inserts the relevant VDF data into .vdf
- The stacking operations’ method signatures are updated

## Testable Interfaces

- The public getters for .block-producers
- The public getters for .vdf
- The API for getting Stacker signing public keys

## Properties of a successful implementation

- The Clarity functions are able to serve as API endpoints to the producer set and stacker set
