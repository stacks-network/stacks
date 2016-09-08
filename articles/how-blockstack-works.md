---
title: How Blockstack Works
description: Learn how Blockstack works under the hood.
image: /images/article-photos/typewriter.jpg
next: blockstack-papers
---

Blockstack Core is a decentralized network of computers that provides secure naming and identity services.

For a quick overview of Blockstack Core, check out [What is Blockstack Core?](/articles/blockstack-core), and continue reading on for a deeper dive into how blockstack works under the hood.

### Technical Overview

Blockstack's domain name system is supported by a network of Blockstack nodes. Each of these nodes maintains a database of domain names, the cryptographic keypairs that own the names, and the data records the names resolve to.

The Blockstack nodes build and continuously update the name database by processing a sequence of name operations, which include name registrations, name transfers, updates of data records associated with names, and more.

Blockstack name operations are embedded in the transactions of an underlying blockchain.  Once incorporated into a block, they are read and processed by all Blockstack nodes, where each node updates its local copy of the name database. Right now, there is only one network of Blockstack nodes, and it sits on top of the Bitcoin blockchain.

<img src="/images/article-diagrams/blockstack-network.png" class="img-fluid" alt="The Blockstack Network">

### Virtual Blockchains

When a Blockstack node boots up, it derives a name database that matches the databases stored by all other nodes. It does this by connecting to a Bitcoin node that it trusts (ideally one that is local) and reading all of the transactions in the blockchain in sequence.

If a transaction has a sequence of data that identifies it as a Blockstack transaction, the node parses it, checks that it has both the proper form and it doesn't violate any authorization rules, and then adds it to the list of valid operations for that block.  Invalid transactions are ignored and discarded.  Once the sequence of operations for a block is validated, the Blockstack node executes them to update its name database.  Because each Blockstack node evaluates the same blockchain data, they will each calculate the same database.  For example, if a keypair issues an operation attempting to transfer a name that it doesn't own, the operation is flagged as invalid and discarded.  But if the keypair that actually owns the name issues a transfer operation, every Blockstack node processes the name transfer.

<img src="/images/article-diagrams/virtual-blockchain.png" class="img-fluid" alt="Virtual Blockchains">

The embedded sequence of valid Blockstack operations make up what is referred to as a virtual blockchain. That is because the transactions of the underlying blockchain are filtered and interpreted in a context that the underlying blockchain is not aware of.   Blockstack gives the transactions extra meaning; they otherwise look like normal transactions to the underlying blockchain's nodes. For example, a Bitcoin node may look at a Blockstack transaction and only see that bitcoins are moving from one address to another and that an unintelligible sequence of data has been attached in a data field (e.g. a field identified by OP_RETURN). Meanwhile, a Blockstack node will look at that data and will know how to interpret it in a way that updates the name database.

### Name Databases

Blockstack nodes update their name databases by iterating through each block in the virtual blockchain and processing each of the operations in that block.  All operations are committed at the same time in a given block. Thus, two transfer operations on the same name will not be processed. Time marches forward in a quantized fashion, where every accepted operation is non-conflicting with every other operation in the block.

The first type of operation is a name preorder, where the sender announces that it will register an undisclosed name in the future.  It doesn't want to reveal the name yet, because doing so would allow an eavesdropping attacker to race the sender and steal the name. These operations do not result in any changes to the name database. Instead, they add a record to a pre-order pool.

The second type of operation is a name registration, where the sender announces it is registering a particular name and provides evidence that the name was preordered in a previous transaction.

These two operations together are known as a two-phase cryptographic commitment. In the preorder step, the value that is broadcasted is a hash of the name and the public key that the name should be registered under. Then, in the register step the name and public key are both revealed and the hash in the first step is verified.

The third type of operation is a name transfer, where the sender announces it is transferring ownership of a name it owns to another cryptographic keypair.

The fourth type of operation is a name update, where the sender announces it is replacing the name's associated data record with a new data record. In this operation, only the hash of the data record is provided in the transaction and the data itself is stored elsewhere.

<img src="/images/article-diagrams/name-database.png" class="img-fluid" alt="Name Databases">

Even though only data record hashes are stored in blockchain transactions, we can use them to verify the authenticity and integrity of the data itself once we get it.  For example, you can host your data in S3, and other peers can verify your data by first obtaining the hash from Blockstack DNS and then checking it against your data's hash.  Because only the name's cryptographic keypair could have feasibly signed the transaction in the blockchain that announced the hash, it is safe to assume that the data is authentic.

### Data Record Storage

By default, Blockstack nodes store the data records in a distributed hash table (DHT) that all Blockstack nodes are connected to (the Blockstack nodes each have their own accompanying DHT nodes). Every Blockstack node knows to look in the DHT to resolve the hash of a data record to the data record itself.  The DHT is spam-proof--because each Blockstack node knows the entire set of data record hashes, it effectively has a data white-list.  It will only store data if its hash is in this set.

<img src="/images/article-diagrams/data-record-storage.png" class="img-fluid" alt="Data Record Storage">

While the DHT is the default storage location for all data records, other copies of the data records may be stored in other locations. In fact, data mirrors may be set up that continuously crawl the DHT and maintain their own copies of the entire data set.  Blockstack nodes may be configured to look in these data mirrors first before looking in the DHT or anywhere else for the record, for better performance and higher availability.

When a data record is sent to the DHT to be stored, the nodes of the DHT use their routing algorithm to collectively assign the record to be stored by a subset of the nodes. The number of nodes that store the record is specified by the replication factor. For example, a replication factor of 20 means that a minimum of 20 nodes will store the record.

When a data record is looked up by its hash value, the nodes of the DHT coordinate to figure out which of the nodes can respond with the record and then one of those nodes responds to the requester with the appropriate value. The requester then checks to make sure that the value can be hashed to match the value hash that it used as the lookup term (known as a "key" in a key-value store, but not to be confused with a cryptographic key).  More information on DHTs can be found [here](https://en.wikipedia.org/wiki/Distributed_hash_table).  The Blockstack DNS reference implementation uses [Kademila](https://en.wikipedia.org/wiki/Kademlia).

Blockstack DNS uses the DHT as its built-in storage mechanism, but it also has a storage plugin system that allows you to mix and match different storage providers as you see fit for your records.  As long as other users have the same plugins, they can retrieve and validate the data records you publish.
