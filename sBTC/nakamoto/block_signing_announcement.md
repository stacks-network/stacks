# Block Signing and Announcement

> Block signing and announcement are integral to the Stacks blockchain. New blocks require signatures from the current tenure's producers and the current reward cycle's stackers. The involvement of stackers ensures block availability and transaction linearizability. Stacker DBs are introduced to facilitate FROST signature generation. Producers propose blocks, and 67% of producers' signers must sign a block for it to be valid. Stackers monitor the producer Stacker DB for valid blocks and append them to the blockchain. State snapshots are used to prevent conflicting chain histories. Stackers are incentivized to cooperate with producers to create snapshots.

Creating a new block requires two parties to sign it: the current tenure's producers, and the current reward cycle's stackers. The reasons for involving the stackers in this process are two-fold:

- **Block availability**: By requiring stackers to sign the block, the producers are compelled to divulge the blocks they produce. They cannot work on a hidden fork, nor can they build atop blocks that are not readily available to the peer network.
- **Transaction linearizability**: Stackers will only accept blocks that constitute a linearized transaction history. Even if producers create multiple conflicting blocks, at most one block will be appended to the Stacks chain. Moreover, if a Bitcoin fork arises that invalidates some Bitcoin-dependent transactions, Stackers ensure that any non-Bitcoin-dependent transactions that were previously accepted remain accepted (see "Extension: Fixed Transaction Orders").

## Facilities for Signature Generation

For each Bitcoin block, it is unambiguous as to which producer set and stacker set are active. All Stacks nodes which share the same view of the Bitcoin and Stacks chains can independently determine which tenure and reward cycle are active, and as such, can determine the public key(s) and Bitcoin spends of each producer, and the public key(s) and STX holdings of each stacker.

Producers and stackers use this information to bootstrap two FROST-generated public keys: one that represents the producers, and one that represents the stackers. A block is only appended to the Stacks chain if it contains two Schnorr signatures -- one from the producers and one from the stackers -- which are valid with respect to these two public keys.

The reader will recall that FROST is a threshold signature scheme in which _M_ out of _N_ (where _0 < M <= N_) signers cooperate to produce a single Schnorr signature. If all signers faithfully cooperate, they can generate signatures with a single round of communication per signature. However, this requires a pre-computation protocol to be executed by the signers beforehand.

In the pre-computation step, each signer must generate and share _N - 1_ encrypted messages with each other signer. When there are hundreds of signers, as will be the case for this proposal, the size of the digital representation of this data will be on the order of megabytes. Moreover, the pre-computation step must be re-executed each time the set of signers change, or if at least one signer misbehaved.

In order to employ FROST signing for block producers and stackers, this document defines a standard communication medium by which hundreds of signers can readily carry out the pre-computation step, accommodating even the degenerate case of having to perform it _N - M_ times in order to exclude the maximum number of _N - M - 1_ malicious signers that the protocol can tolerate while maintaining safety. The communication medium, called a _Stacker DB_ (described below), leverages every connected Stacks node to store and replicate the FROST pre-computation state, as well as store and forward signature generation messages.

By leveraging Stacks network infrastructure via Stacker DBs, producer and stacker signer implementations do not need to concern themselves with implementing durable data storage and highly-available communication. Instead, it is sufficient for these signer processes to contact a trusted Stacks node to send, store, and receive this data on its behalf. This significantly reduces the trusted computing base for producer and stacker signer implementations, and allows the block production process to benefit from independent improvements to the Stacks peer-to-peer network over time. Furthermore, it allows all Stacks nodes to monitor the behavior of block producers and signers, so they can detect and handle network partitions (see below).

### Stacker DBs

To facilitate FROST key and signature generation for producers and stackers, the Stacks peer network will be extended to support Stacker DBs. A _Stacker DB_ is an eventually-consistent replicated shared memory system, comprised of an array of bound-length slots into which authorized writers may store a single chunk of data that fits into the slot's maximum size.

Stacks nodes exchange a list of up to 256 Stacker DBs to which they are subscribed when they exchange peer-to-peer handshake messages (see SIP-003). Each Stacks node maintains an ordered list of Lamport clocks, called a _chunk inventory_, for each slot in each Stacker DB replica it hosts, which it exchanges with peer Stacks nodes that host replicas of the same DB (note that this is _not_ a vector clock; write causality is _not_ preserved). Nodes exchange chunk data with one another such that eventually, in the absence of in-flight writes and network partitions, all replicas will contain the same state. Chunks with old version numbers are discarded by the node, and never replicated again once a new version is discovered.

Chunks are replicated asynchronously through the Stacks p2p network through gossipping. A Stacks node will periodically query neighbors who replicate the same Stacker DB for their replicas' chunk inventories, as well as the number of inbound and outbound neighbor connections this node currently has. If any slots are discovered that contain "later" versions than the local slot, the node will fetch that slot's chunk, authenticate it (see below), and store it along with an updated version. In addition, if the node discovers that it has the latest version of a chunk out of all neighbors and it discovers a neighbor with an older chunk, it will push its local chunk to the neighbor with probability inversely proportional to either the neighbor's reported number of total neighbors (if the local node treats this neighbor as an outbound neighbor), or to the reported number of outbound neighbors (if the local node treats this neighbor as an inbound neighbor).

Stacker DB clients (i.e. producers and stackers) read and write chunks via the node's RPC interface. The Stacker DB "read" endpoint returns the chunk data, the chunk version (as a Clarity value), and the chunk signer's compressed secp256k1 public key as a JSON struct, conforming to the following specification:

```json
{
  "chunk": {
    "type": "string",
    "pattern": "^[0-9a-fA-F]*$"
  },
  "version": {
    "type": "string",
    "pattern": "^(0x)?00[0-9a-fA-F]{16}$"
  },
  "public_key": {
    "type": "string",
    "pattern": "^[0-9a-fA-F]{33}$"
  }
}
```

Note that chunk versions are serialized Clarity unsigned integers.

A chunk with version `0x000000000000000000` is always an empty chunk, and has a `chunk` field with zero length. It is used to represent a chunk that has not been written. The content of the `public_key` field in this case is undefined.

A "write" to the Stacker DB occurs through an RPC endpoint. The "write" consists of the array index, the chunk version, the chunk data, and a recoverable secp256k1 signature over the aforementioned data. The node leverages the Stacker DB's smart contract to authenticate the write by passing it the array index, chunk version, chunk hash (SHA512/256), and signature via a read-only function called `stackerdb-auth-write`, whose signature is produced below:

```clarity
(define-read-only (stackerdb-auth-write
(chunk-idx uint)
(chunk-version uint)
(chunk-hash (buff 32))
(chunk-sig (buff 65))))
```

The `auth-write` function evaluates to `true` if the write is allowed, or `false` if not. If `true`, then the Stacks node verifies that the version is equal to or greater than the last-seen version for this chunk. If it is equal, but the chunk is different, then the write will be accepted only if the hash of the chunk has strictly more leading 0's than the current chunk. If this is the case, or if the version is strictly greater than the last-seen version of this chunk, then the node stores the chunk locally, updates the DB's chunk inventory, and announces it to its peer nodes which replicate the Stacker DB. If authentication fails, or if the version is less than the last-seen version, or if the version is equal to the last-seen version and the hash of the new chunk has less than or equal leading 0-bits in its hash, then the Stacks node NACKs the RPC request with an HTTP `403` response.

The reason for accepting chunks with the same version but lesser hashes is to allow the system to both recover from and throttle nodes that equivocate. Automatically resolving conflicts that arise from equivocation keeps all Stacker DB replicas consistent, regardless of the schedule by which the equivocated writes are replicated. The use of the chunk hash to resolve equivocation conflicts makes it increasingly difficult for the writer to continue equivocating about the chunk for this version -- the act of replacing a chunk with version _V_ for _K_ times requires _O(2\*\*K)_ computing work in expectation. This, in turn, severely limits the amount of excess disk-writes the a Stacks node can be made to perform by the equivocating writer, and severely limits the number of distinct states that this version of the chunk can be in.

To support equivocation throttling in this manner, the chunk inventory for the Stacker DB encodes both the version and the number of leading 0-bits in the chunk's hash.

The node will periodically query the smart contract in a read-only fashion to determine if any chunks may be evicted. To determine the periodicity, the node queries the smart contract in a read-only fashion via its `stackerdb-garbage-collect?` function once per Bitcoin block processed:

```clarity
(define-read-only (stackerdb-garbage-collect?))
```

This function evaluates to `true` if the node should begin garbage-collection for this DB, and `false` if not.

If the node should garbage-collect the DB, it will determine which chunks are garbage via the smart contract's `stackerdb-is-garbage?` function, whose signature is produced below:

```clarity
(define-read-only (stackerdb-is-garbage?
(chunk-idx uint)
(chunk-version uint)
(chunk-hash (buff 32))
(chunk-sig (buff 65))))
```

If this function evaluates to `true`, then the chunk will be deleted and its version reset to `u0`. If `false`, then the chunk will be retained.

Further details of the Stacker DB wire formats, controlling smart contracts, and RPC endpoints can be found in Appendix A.

### Boot Contracts

Each Stacks node must subscribe to two Stacker DB instances -- one for producers, and one for stackers -- in order to ensure that each producer and stacker can reliably participate in FROST signature generation. The producer Stacker DB contract is controlled through `SP000000000000000000002Q6VF78.block-producers` (henceforth referred to as `.block-producers` for brevity), and the Stacker DB contract for stackers is controlled through a new PoX contract `SP000000000000000000002Q6VF78.pox-4` (henceforth referred to as `.pox-4`). Only nodes that act as producers and/or stackers need to subscribe to these Stacker DBs; however, each producer and each stacker will need to subscribe to both.

Like with the PoX contract, the data spaces for these two contracts are controlled directly by the Stacks node. In particular, the data space for `.block-producers` is populated at the start of each term with the public keys of the tenure's block producers that will be used to validate DB chunks for the coming tenure, as well as data about the highest-known on-Bitcoin state snapshot. The public keys are obtained from the enrollment transactions on Bitcoin for this tenure.

The `.pox-4` contract will become the current PoX contract. This PoX implementation behaves identically to the current version, except in two ways. First, the signatures of the `stack-stx` and `delegate-stx` functions in `.pox-4` are modified to accept an additional `(buff 33)` argument, which encodes a compressed secp256k1 public key. This effectively requires stackers to supply a chunk-signing key when they stack. Second, this state is stored in a new data map within `.pox-4`, which will be queried by the Stacker DB interface to authenticate chunk writes.

Both contracts will have read-only getter functions so that other smart contracts can query the chunk-signing keys for their own purposes.

## Signature Generation

In both `.block-producers` and `.pox-4`, the concept of "signature weight" is embodied by the number of signers that each producer or stacker represents. A _signer_ in this context refers to a fixed-sized portion of the threshold signature. For block production, there are 100 signers, and at least 67 of them must participate to produce a valid block signature. For stacker signing, there are up to 4,000 signers (one for each claimed reward slot), of which 67% must participate (up to 2,680 signers).

### Producer DB Setup

The `.block-producers` contract defines a Stacker DB with 300 slots. The first 100 slots store the pre-computed FROST state for each signer, slots 100-199 are used to store in-flight signature generation state for FROST, and slots 200-299 store proposed block data. The signers are assigned to a tenure's producers in quantities proportional to their share of Bitcoin spent. At the start of tenure N, it evicts all signing state for tenure N-1 by garbage-collecting each chunk. It then determines how many slots to allot each producer by distributing them in a round-robin fashion from smallest producer by Bitcoin spend to largest producer by Bitcoin spend. It breaks ties by sorting each tied producers' last enrollment transaction IDs in lexographic order.

The number of DB signer slots are assigned to a producer represents the weight of the producer's signature. For example, if four producers each registered for tenure N, and each spent 10%, 20%, 30%, and 40% of the BTC, then the 10% producer would receive 10 slots, the 20% producer would receive 20 slots, the 30% 30 slots, and the 40% 40 slots. The 10% producer receives DB slots `0, 10, 20, 30, 40, 50, 60, 70, 80, ... 180, 190`; the 20% producer receives DB slots `1, 2, 11, 12, 21, 22, ..., 191, 192`; the 30% producer receives DB slots `3, 4, 5, 13, 14, 15, 23, 24, 25, ..., 193, 194, 195`; the 40% producer receives DB slots `6, 7, 8, 9, 16, 17, 18, 19, ..., 196, 197, 198, 199`. The `.block-producers` contract's `stackerdb-auth-write` function ensures that each producer can only write to their assigned slots; the requisite state for doing so is directly written into the contract's data space at the start of each tenure, which this function queries.

The proposed block slots are allotted to producers in ascending order by BTC weight. In the above example, slot 200 is allotted to the 10% producer, slot 201 to the 20% producer, slot 202 to the 30% producer, and slot 203 to the 40% producer. If there are fewer than 100 producers, then the remaining slots are unused.

### Producer Signing Protocol

When the FROST pre-computation step is executed, each producer generates their signers' data and uploads them to their assigned slots. The producer then fetches and decrypts the messages from the other producers' signers in order to obtain the necessary FROST state required to produce signatures.

When proposing blocks, each block producer may submit a candidate assembled block to their assigned block slots (i.e. slots 200-299) for other producers to see. Producers then collectively decide on which candidate block to sign. The protocol for agreeing on the block is implementation-defined and not consensus-critical, but this document requires the implementation to provide a necessary ingredient to Byzantine fault-tolerant implementations: each block must be signed by at least 67% of the producers' signers.

The signed block is automatically propagated to stackers via the `.block-producer` Stacker DB.

### Stacker Signer DB Setup

Like the `.block-producers` contract, the `.pox-4` contract maintains a set of DB slots for storing FROST pre-computed data and signature data. The stacker signer DB has 8,000 slots. The first 4,000 are allotted to stackers based on how many reward slots they earn. These slots are assigned to stackers in contiguous ranges, based on the order in which their STX were stacked for this reward cycle (i.e. as determined by the `.pox-4` contract's `reward-cycle-pox-address-list` map), and are used to hold each stackers' signers' FROST pre-computation state. The last 4,000 are similarly allotted to stackers, but are used to contain in-flight signature metadata regarding the proposed block.

### Stacker Signing Protocol

Stacker signers monitor the producer Stacker DB to watch for a completed, valid, sufficiently-signed producer-proposed block. If such a block is created, then each stacker attempts to append the block to its local node's chainstate. If the block is acceptable, then stackers execute the distributed FROST signature algorithm to produce the signature by storing their signature shares to their allotted signature slots. Once enough signature slots have been acknowledged and filled for this block, then the block and both producer and stacker signatures are replicated to the broader peer network. Note that block replication can happen independent of signature replication; future work may leverage this property to implement an optimistic eager block replication strategy and a fast _post-hoc_ signature-replication strategy to speed the delivery of blocks from producers to the rest of the network.

Because the block production algorithm is implementation-defined, stackers must take the utmost care in choosing whether or not to append a produced block to the blockchain. The produced block must meet the following criteria:

- It must be valid under the consensus rules
- At least 67% of producers' signers have signed the block
- There must not exist another block at the same height on the same Bitcoin fork

If producers equivocate and create two valid but different blocks for the same Stacks height, then stackers should not only refuse to sign it, but also stackers should refuse to sign any further blocks from that tenure.

If the underlying Bitcoin chain forks, then stackers may need to sign a producer block with the same Stacks block height as an existing Stacks block but happens to be evaluated against a different Bitcoin fork. Stackers determine which Bitcoin fork by examining the sequence of checkpoint transactions in the ancestors of the block.

## State Snapshots

Once per tenure, stackers and the producer set create a "snapshot" Bitcoin transaction that contains a recent digest of the Stacks chain history. Specifically, the stackers and producer set who are active in tenure N must send a snapshot transaction that contains the hash of the last block produced in tenure N-2 (i.e. the block that all blocks in tenure N-1 build upon, which has subsequently received at least 10 Bitcoin confirmations). The presence of this transaction in the Bitcoin chain prevents any future set of producers and stackers from producing a conflicting chain history. All blocks represented by the snapshot transaction are treated as finalized -- the act of creating an alternative transaction history is tantamount to reorganizing the Bitcoin chain to remove conflicting snapshot transactions.

Crafting and sending this transaction is not free, so its creation must be incentivized by the consensus rules. To ensure that it gets created and mined on-time, the producer block reward disbursal for tenure N will not happen until a snapshot for tenure N-2 _or later_ is mined on Bitcoin. To similarly incentivize stackers to cooperate with producers to create the snapshot, PoX payouts during subsequent tenures are diverted to a Bitcoin burn address and their STX are indefinitely locked until the snapshot for tenure N-2 (or later) is mined on Bitcoin. In other words, producers and stackers can only get paid if they create and broadcast the snapshot on Bitcoin in a timely fashion. To avoid missed payments, stackers and producers are encouraged to produce the snapshot for tenure N-2 at the start of tenure N.

The wire format for a snapshot transaction's `OP_RETURN` payload is as follows:

0      2  3       7                 39                        80

|------|--|-------|------------------|-------------------------|

magic  op  tenure   block hash        padding

id

Where `op = 0x73` (ASCII `s`) and:

- `tenure_id` is the tenure number (i.e. N-2)
- `block_hash` is the index hash of the last checkpoint block in the identified tenure

In addition, the snapshot transaction must contain at least two inputs: a FROST-generated Schnorr signature from the producer set in tenure N, and a FROST-generated Schnorr signature from the stackers in the current reward cycle. The producer set funds the transaction fee; the stackers sign the transaction with `SIGHASH_ANYONECANPAY`.

## Liveness Incentives

The producer set is incentivized to produce blocks and snapshot transactions because if either process stops, then the STX coinbase and transaction fees also stop.

The stackers are incentivized to sign snapshot transactions, but what incentivizes them to validate and sign producer blocks? The answer is sBTC (see SIP-021). Stackers are already incentivized to accept blocks that materialize sBTC from deposits and dematerialize sBTC from withdrawals. If they do not complete these tasks in a timely fashion, then their PoX rewards are diverted to a burn address and their STX are indefinitely locked until all unfulfilled sBTC deposits and withdrawals are handled. In addition, stackers are incentivized to sign blocks that contain their own stacking operations, so that they can continue to receive PoX rewards.

This is enough to drive stacker liveness. In order to process a stacking or sBTC (de)materialization operation in Stacks block _N_, the stacker must process and accept all blocks prior to _N_. Therefore, stackers will continuously accept valid blocks from producers so that they will be able to complete these actions on-time.
