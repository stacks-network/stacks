# Deployment Plan

_This is a very big undertaking; almost as big as Stacks 2.0_.

Fortunately, there are a lot of things that can be tested and deployed on mainnet without creating a hard fork. The pieces of infrastructure that will need by far and away the most testing (since they’re filled with unknown-unknowns) are the stacker DB implementation and the producer set and stacker signer FROST groups.

## Epic 1: Stacker DB Rollout

We can implement the stacker DB system well before anything else needs to be implemented. It is recommended to finish the in-flight implementation and using it to try replicating databases of similar size to the producer and stacker signer DBs using Hiro and Foundation nodes. We can benchmark and improve the performance of replication concurrently with everything else.

## Epic 2: Producer and Signer Rollout

Once we have Stacker DBs live, we can create mocked .pox-4 and .block-producer contracts on mainnet, which will allow us to test producer and stacker signer implementations. In particular, we can verify that:

- A set of producers will elect a leader
- The producer leader will create a valid mainnet block
- The producer set will sign that block
- The stackers will see the signed block, and sign it as well

We can build out the producer and stacker binaries in parallel — we can mock a produced block for stackers to sign, so stacker signers can be tested without producers being live.

## Epic 3: Verifiable Delay Function Rollout

We can test and calibrate the VDF implementation in a set of separate processes, which each post their statistics to a fake .vdf smart contract deployed on mainnet. This will give us some indication of how good the producers will be at executing it in a wide variety of environments, and how good our VDF calibration algorithm actually is when presented with mainnet data.

## Epic 4: Blockchain Changes Rollout

The bulk of the blockchain changes need to be tested via unit tests, property tests, and finally a testnet implementation. Fortunately, this can be done in parallel to the above, so that when it comes time to run 3.0 on the Bitcoin testnet, we’ll have a very robust Stacker DB and signer implementation.

The consensus rules, block snapshotting, block acceptance, network state machines, and so on can be tested with existing unit test and integration test tooling as they are completed. However, some degree of live testing will be necessary. I suggest the following rollout phases, based on what we did for Stacks 2.0:

### Helium 3.0

This is like the Helium testnet — there is one producer and one stacker, and they just produce and sign blocks at a fixed rate. This functions like a local devnet.

### Neon 3.0

This is like the Neon testnet. It’s public, but the set of producers and signers would be fixed and hard-coded. This is just to test producers’ ability to create blocks and stackers’ ability to accept them via their respective distributed agreement protocols.

### Argon 3.0

This extends Neon with producers chosen from tenures, and signers chosen from stackers. This implementation contains the boot contracts.

### Krypton 3.0

This is the release we’d use to test the migration from the current testnet to the 3.0 testnet. We’d test the migration as many times as we need to until we’re convinced it works.

Krypton 3.0 is otherwise feature-complete.

### Xenon 3.0

This would become the new testnet. Xenon 3.0 launches from the mainline Stacks testnet using the migration logic we perfected in Krypton 3.0.
