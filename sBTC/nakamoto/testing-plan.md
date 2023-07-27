# Testing Plan

Broadly speaking, this workstream can be divided into the following testable blackbox modules. Each module will need to be implemented and tested completed before its listed dependencies.

1. [Verifiable Delay Function (VDF)](./testing/verifiable_delay_function.md): Implement VDF for tenure extensions with calibration and validation functions.
2. [Chainstate Accessor Trait](./testing/chainstate_accessor_trait.md): API for querying Stacks and Bitcoin blocks, ancestors, consensus, and more.
3. [Network Accessor Trait](./testing/network_accessor_trait.md): API for querying neighbor information and block inventories.
4. [Block and Transaction Definitions](./testing/block_and_transaction_definitions.md): Logic for parsing and validating on-Bitcoin and Stacks transactions and blocks.
5. [Snapshot DB](./testing/snapshot_db.md): Store Bitcoin snapshot state, validate checkpoint transactions, and interface with burnchain DB.
6. [Stacker DB](./testing/stacker_db.md): Create a distributed database for FROST signature data exchange and block decisions.
7. [Stacks Block Storage Trait](./testing/stacks_block_storage_trait.md): API for committing processed Stacks blocks to storage.
8. [Stacks Block Storage DB](./testing/stacks_block_storage_db.md): Load and store Stacks block streams, interface with Stacks chain state, and sortition DB.
9. [Stacks Block Inventory Synchronization](./testing/stacks_block_inventory_synchronization.md): Network state-machine to query and verify blocks peers can serve.
10. [Stacks Block Bulk Download](./testing/stacks_block_bulk_download.md): Network state-machine for downloading blocks based on inventory state.
11. [Stacks Block Antientropy](./testing/stacks_block_antientropy.md): Extend antientropy to push missing blocks to neighbors.
12. [Stacks Block Relay](./testing/stacks_block_relay.md): Update relayer to process and schedule new block data for relay.
13. [Stacks Block Validation](./testing/stacks_block_validation.md): Implement new block validation consensus rules.
14. [Stacks Block Acceptance](./testing/stacks_block_acceptance.md): Update blockchain state with a block's new information.
15. [Boot Contracts](./testing/boot_contracts.md): Create new boot contracts .pox-4, .block-producers, and .vdf.
16. [Updated Chains Coordinator](./testing/updated_chains_coordinator.md): Upgrade chains coordinator to use snapshot DB and adapt to new rules.
17. [Threshold FROST Signatures](./testing/threshold_frost_signatures.md): Port sBTC threshold FROST signature work to Stacks.
18. [Stacker DB Client](./testing/stacker_db_client.md): Produce RESTful client crate for loading and storing StackerDB state.
19. [Block Producer Reference Implementation](./testing/block_producer_reference_implementation.md): Create a block producer process for mining and coordination.
20. [Stacker Signer Reference Implementation](./testing/stacker_signer_reference_implementation.md): Create a stacker signer process for coordination and block signing.
