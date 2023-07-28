# Network Accessor Trait

API for querying neighbor information and block inventories. Some state machines need to read state in others, but we don’t want to block implementation work by waiting for dependent state machines to be available.

## Dependencies

- none

## Requirements

- An API for iterating through the list of neighbors
- For each neighbor, this reports
- whether or not the neighbor is authenticated
- whether or not it is inbound or outbound
- estimated in-degree and out-degree of the neighbor
- last contact time
- last seen block height of this neighbor
- whether or not this neighbor is a bootstrap peer
- which stacker DBs this neighbor subscribes to
- NeighborKey
- An API for getting the block inventories from neighbors

## Testable interfaces

- All of the above

## Properties of a successful implementation

- This trait can be implemented for PeerNetwork and can be mocked for tests
- We can use this trait in some form for working on multiple network stack upgrades in parallel
