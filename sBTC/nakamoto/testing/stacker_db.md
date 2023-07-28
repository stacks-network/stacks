# Stacker DB

This is a novel distributed database that producers and stackers use to communicate their FROST signature data to one another, as well as their decisions on which blocks to create.

## Dependencies

- [Network accessor trait](./network_accessor_trait.md)

## Requirements

- P2P message definitions and validation logic
- RPC API
- Local database for storing DB state
- State machine for replica discovery and synchronization
- Throttling and rate-limiting against overly-chatty or misbehaving replicas

## Testable Interfaces

- P2P message StacksMessageCodec implementations
- DB connection and transaction objects
  - For load/store of stacker DB chunks
  - Each state machine step, with explicit pre/post-conditions to validate the state transition
  - Smart contract callbacks for write authentication and garbage-collection
  - Throttling and rate-limiting statistical reports

## Properties of a successful implementation

- End-to-end reachability (eventually, all replicas are reachable from all peers)
- End-to-end replication (eventually, all replicas have the same state)
- Partition recovery (peers re-achieve end-to-end reachability)
- Only correct peers remain connected; all bad peers are throttled or banned
