---
title: Light Clients
description: Learn about fast bootstrapping and lightweight name verification
image: https://images.unsplash.com/photo-1423666639041-f56000c27a9a?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&w=1080&fit=max&s=98326a6e44d1b6bbcddb0d89f75ed95c
next: faq
---

Each Blockstack DNS node maintains a 100% replica of all names and name records.  To do so, it must continuously crawl the underlying blockchain to discover more name operations.  While this is acceptable for desktops and servers with an "always-on" Internet connection, it may not be suitable for laptops and mobile devices where bandwidth, connectivity, and power are limited.

At the same time, starting up a new Blockstack DNS node can take a while, because it must search through all of the blockchain's transactions.  The bootstrapping process is network-bound, much like booting up a new Bitcoin node.

To overcome these challenges, Blockstack DNS uses a secure, light-weight consensus protocol that lets anyone query a full-fledged node for name data *without having to trust it*.  The client uses an offline copy of the underlying blockchain's transaction headers (e.g. SPV headers in Bitcoin) and a special hash called a **consensus hash** to validate the node's query responses.

The consensus hash gives Blockstack DNS a couple useful properties:
* If two Blockstack DNS peers agree on the same consensus hash, then they have processed the exact same sequence of name operations (with extremely high probability).
* If a client has a consensus hash at block height `h`, then it can verify the authenticity of any operations in previous blocks with `O(log h)` queries and `O(K + (log h)^2)` bytes transferred (where `K` is the maximum size of a block).

### Consensus Hash Construction

Recall that a Blockstack DNS node broadcasts name operations by writing them as transactions on an underlying blockchain.  Peer nodes discover them by reading the blockchain and replaying the operations sequentially.  In doing so, the blockchain serves as an append-only log of name operations, which when replayed in sequence allow a Blockstack DNS peer to determine the current and prior states of each name and namespace.

<img src="/images/article-diagrams/consensus-hash-construction.png" class="img-fluid" alt="Overview of how Blockstack DNS constructs a consensus hash.">
_Figure 1: Overview of how Blockstack DNS constructs a consensus hash.  The records are organized into a Merkle tree whose root is fed into the consensus hash, along with a geometric series of prior consensus hashes._

When broadcasting new operations, a Blockstack DNS node maintains a consensus hash for the current blockchain height, and embeds it within the operation's data.  The consensus hash is a cryptographic hash calculated over the last block's sequence of name operations, as well as a logarithmic number of prior consensus hashes (Figure 1).  Specifically, at block height `h`, the consensus hash is calculated by first hashing the canonical forms of each name operation in transaction order, organizing them into a Merkle tree, and then hashing the Merkle tree root and the prior consensus hashes for all blocks at heights `{h | h - 2^i && i > 0 && h - 2^i >= h0}` (where `h0` is the block height of the first-ever name operation).  As a result, two Blockstack DNS peers at block `h` will calculate the same consensus hash if they observed the same sequence of name operations.

The usefulness of fast bootstrapping and lightweight name verification depend on the client first obtaining a reasonably fresh consensus hash.  To facilitate this, Blockstack DNS peers reject operations that do not have fresh consensus hashes (e.g. the operation must be found within 40 blocks of the height that its embedded consensus hash corresponds to).  This gives clients a straightfoward way to discover a recent consensus hash:  get it from a transaction in the underlying blockchain known to have been accepted by Blockstack DNS.  The Blockstack DNS client software makes it easy for users and application developers to discover these consensus hashes, such as (but not limited to) using a transaction the client itself recently issued, using a valid transaction a trusted friend issued, or fetching and validating a (possibly old) copy of an untrusted Blockstack DNS peer's database and fetching only the new transactions that have not yet been processed.

### Fast Bootstrapping

Recall that a full Blockstack DNS peer not only stores each name and namespace it finds while processing the blockchain, but also the history of operations on it.  In particular, a client can query a name or namespace _as it was at a prior blockchain height_.  For example, suppose Alice preordered `alice.id` at block 400000, registered it at block 400010, updated it twice in block 400020, and transferred it to Bob at block 400030.  Then, Charlie can query a Blockstack DNS node for the state of the name `alice.id` as it was at block 400011, and see that it was registered to Alice.  At block 400009, he would see that it was still preordered.  He can query it at block 400025 and see that Alice had updated the name (he would see the effect of the second update).  He can also query the name at block 400031 and see that it was transferred to his public key.

As part of storing each name and namespace's history, a Blockstack DNS node can determine at which block heights a record was changed.  For example, Charlie can query the change history for `alice.id`, and get back the list `[400000, 400010, 400020, 400030]`.

Because a name or namespace can be affected by multiple transactions within a single block, the Blockstack DNS node additionally keeps track of the transaction-level ordering of a name's history.  For example, Charlie can query the number of times the record for `alice.id` changed in block 400020, and would be informed that it changed twice (because Alice sent two update-transactions).  If he queried the state of `alice.id` at block 400020, the node would give him two versions of `alice.id`:  `alice.id` as it was when it was registered but not updated, and `alice.id` as it was when it was updated for the first time.

These three features--querying a record's past states, querying the block heights where a record changed, and querying how often it changed in a block--allow a new Blockstack DNS node to use a trusted consensus hash to verify the authenticity of an untrusted peer's database.  Once it has done so, it can use the peer's now-trusted database *instead of* having to re-create its own copy by downloading the blockchain.

To see how it works, consider that each record has the following information:

* the index into the block of the transaction that changed it ('`txindex`')
* the list of block heights where it changed ('`history`')
* for each block height in '`history`', a list of '`txindex`' values where the name changed.
* for each '`txindex`' value at a given block height, the list of fields that were changed by the transaction ('`changeset`') 
* a record-specific method ('`rollback`') that takes a record's history, changeset, historical block height, and transaction index as arguments and returns the record as it was at that particular block height and transaction.  This is simply a matter of iteratively copying over the fields from '`changeset`' into the current state in order from present back to a past block height and transaction index (similar to how a version control system would roll a source file back to a particular commit).

To verify the authenticity of an untrusted database, the bootstrapping Blockstack DNS node executes the following algorithm (Figure 2).

```
input:
   trusted_consensus_hash:  the trusted consensus hash
   h:  the height of the block with the trusted consensus hash
   h0: the initial block height
   db: the untrusted database, as a list of records

output:
   if successful, True
   if unsuccessful, False

subroutines:
   CONSENSUS_HASH( recs, consensus_hash_list ):  calculate the canonical serializations of each record in recs, and then calculate the cryptographic hash over them as well as the given consensus hash list

let consensus_hashes = []
for each block i from h0 to h

   let recs_i = [rec where i in rec.history for rec in db]
   let block_i_recs = []
   let block_i_consensus_hashes = []

   sort recs_i on 'txindex'
   for rec in recs_i
      let txindexes = rec.history[i]
      sort txindexes

      for txi in txindexes:
         let historic_rec = rec.rollback(rec.history, rec.changeset, i, txi)
         block_i_recs = block_i_recs ++ [historic_rec]
   
   let j = i - 1
   while j >= h0
      block_i_consensus_hashes = blockstack_i_consensus_hashes ++ [consensus_hashes[j]]
      j = j / 2
   
   let ch = CONSENSUS_HASH( block_i_recs, block_i_consensus_hashes )
   consensus_hashes = consensus_hashes ++ [ch]

if consensus_hashes[h] == trusted_consensus_hash
   print "db is consistent with the trusted consensus hash"
   return True

else
   print "db is not consistent with the trusted consensus hash"
   return False 
```

_Figure 2: The fast bootstrapping algorithm's pseudocode.  A bootstrapping Blockstack DNS node executes this to verify the authenticity of another node's database.  If the authenticity is verified, then the peer can bootstrap itself from the database, without having to download the blockchain and regenerate its own database from scratch_

In effect, the bootstrapping node translates the database back into the sequence of transactions the untrusted peer processed, and replays them to recalculate the final consensus hash.  If it matches the trusted consensus hash, then the database is trustworthy.  Importantly, this is a *CPU-bound* process--it can be done offline.

One nice thing about this feature is that once you know *any* consensus hash, you can take an up-to-date Blockstack DNS node's database and validate all records that were processesed up to that consensus hash's block height.  If you had a copy of the name database that incorporated operations up to block 300000, but your consensus hash corresponds to block 250000, you can still use it to construct a trusted database with all records prior to block 250000.  You can then download the remaining 5000 blocks to finish the bootstrapping process.

### Lightweight Name Lookups

The set of back-links from a given block `h` to all blocks `h - 2^i` constitute a _Merkle skip-list_ (Figure 2).  Given the consensus hash at height `h`, a client can query an untrusted Blockstack DNS server to determine the name operations at any block with a lower height.  The query requires a logarithmic number of requests relative to the number of blocks, and only requires a squared logarithmic number of bytes transferred relative to the blockchain's size (plus all the records for the block with the record to verify).  The process of verifying the authenticity of a prior name operation with a later known-good consensus hash is called _Simplified Name Verification_ (SNV).

<img src="/images/article-diagrams/snv-overview.png" class="img-fluid" alt="Overview of how lightweight name lookups work.">
_Figure 3: Overview of Simplified Name Verification (SNV) protocol.  Each row represents the blockchain, in decreasing block height order from left to right (h > h0).  The user wishes to verify the authenticity of a name operation in the block marked with a `?`.  In each step, the user trusts the consensus hash for the white outlined block, and uses it to verify the authenticity of that block's name operations, as well as the set of prior consensus hashes (belonging to yellow blocks indicated by the arrows).  By iteratively fetching name operations and consensus hashes for prior blocks, the user will eventually prove the authenticity of all name operations in the `?` block._

To see how this works, suppose that a user trusts the consensus hash at height `h`, but needs to verify a name operation in block `h - 11`.  Suppose that the blockchain currently has 17 blocks beyond height `h0` (Figure 2).  To do so, the user queries any Blockstack DNS node to obtain all of the name operations processed at height `h`, and the consensus hashes for blocks `h - 1`, `h - 2`, `h - 4`, `h - 8`, and `h - 16`.  Once obtained, the user serializes the name operations and prior consensus hashes to re-calculate the consensus hash at `h`.  If the trusted consensus hash matches, then the user knows that both the name operations the prior consensus hashes are authentic.  The user then iteratively downloads name operations and consensus hashes in this way, until block `h - 11` is reached.  Then, the user will have obtained and verified the authenticity of all name operations in that block, including the desired name operation.

Extrapolating, the general SNV algorithm works as follows (Figure 4).

```
input:
   trusted_consensus_hash:  the trusted consensus hash 
   h:  the height of the block with the trusted consensus hash 
   rec_id:  the name or namespace ID to query
   h_rec:  the height of the record to query (must be less than h)
   h0:  the height of the block with the first-ever Blockstack DNS operation

output:
   if successful, the queried record as it was at height h_rec
   if unsuccessful, False

subroutines:
   HISTORIC_RECORDS(h):  query to Blockstack DNS that finds all records affected by transactions at height h, restores them to their state at height h, and returns them
   CH(h):  query to Blockstack DNS that returns the consensus hash at height h
   CONSENSUS_HASH( recs, consensus_hash_list ):  calculates the consensus hash from a list of records and prior consensus hashes

let current_h = h
trusted_consensus_hash_table = {
   h: trusted_consensus_hash
}

while current_h >= h_rec
   let historic_recs = HISTORIC_RECORDS(current_h)
   let current_consensus_hashes = []
   let i = 1

   while current_h - 2^i >= h0
      let ch = CH(current_h - 2^i)
      current_consensus_hashes = current_consensus_hashes ++ [ch]
      i = i + 1

   let ch_at_h = CONSENSUS_HASH(historic_recs, current_consensus_hashes)
   if ch_at_h != trusted_consensus_hash_table[current_h]
      print "Consensus hash mismatch at height ", ch_at_h
      return False

   if current_h == h_rec
      break
 
   else
      let current_h = minimum([k for k in trusted_consensus_hash_table.keys where k >= h_rec])
   
print "Consensus hash matches"
find rec in historic_recs where rec.rec_id == rec_id
return rec
```

_Figure 4: The SNV algorithm pseudocode.  A client executes this algorithm to use a known-good consensus hash to determine the prior state of a given record.  The client does not need to trust the Blockstack DNS node._

Because of the way the consensus hash is constructed, a Blockstack DNS peer cannot serve invalid data without the client noticing.  The worst it can do is not serve data at all.  Once you have a recent consensus hash, you can use it to look up any prior version of a name record without running either a Blockstack DNS node or a full Bitcoin node.

### Consensus Hash Updating

If your consensus hash gets too stale, you'll be unable to verify the authenticity of more and more names as they get updated.  Fortunately, there are two easy ways to solve this.

The first way is to simply have your lightweight nodes re-sync as full nodes every so often.  You start by fetching and validating an untrusted peer's database and installing it on your lightweight clients, as described above.  Then, every so often (as power and connectivity permit), you have your lightweight clients synchronize with the blockchain by downloading new blocks and updating their databases.  As long as your lightweight clients receive valid blocks from the underlying blockchain (such as from a trusted Bitcoin node, or using an SPV client with known-good headers to validate an untrusted Bitcoin node's blocks), they will derive the same, correct consensus hashes in the future.  The Blockstack DNS client software comes with an SPV client to facilitate communicating with untrusted full Bitcoin nodes.

The second solution requires you to have a spare computer you can keep running somewhere, like a Raspberry Pi.  **It does not need to be a server**--it just needs an out-bound Internet connection (no port-forwarding needed).  You would give this computer its own cryptographic keypair, and have it run full Blockstack DNS node.  You'd configure it so that every so often, it would sign its latest consensus hash and upload it somewhere public where your lightweight clients can find it (such as your Dropbox folder).  Then, you give your lightweight nodes the public key, and have them download and verify the consensus hash every so often.  This way, there is no need for your lightweight nodes to sync up with the blockchain--they only need to re-download the latest consensus hash every so often, and make sure they never receive a duplicate.
