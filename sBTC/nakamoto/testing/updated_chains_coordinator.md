# Updated Chains Coordinator

Upgrade the chains coordinator subsystem to use the snapshot DB, and to cease caring about affirmation maps and other fork-sensitive data once this system’s rules go into effect.

## Dependencies

- [Stacks Block Acceptance](./stacks_block_acceptance.md)
- [Snapshot DB](./snapshot_db.md)

## Requirements

- The chains coordinator correctly processes Bitcoin and Stacks blocks using the old 2.4 rules up until Nakamoto (3.0) rules, and then switches over.

## Testable Interfaces

- All the same ones today, but under the switchover

## Properties of a successful implementation

- The chains coordinator no longer needs to unwind history or track block affirmations or detect PoX anchor blocks after 3.0 goes live.
- The chains coordinator only does the following:
- Process Stacks blocks between processed checkpoint block N and unprocessed checkpoint block N+1
- Process the Bitcoin block for N+1
- Process checkpoint block N+1
- Repeat
