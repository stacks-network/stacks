---
title: How Blockstack Works
description: Learn how Blockstack works under the hood.
image: https://images.unsplash.com/photo-1451187863213-d1bcbaae3fa3?crop=entropy&dpr=2&fit=crop&fm=jpg&h=1100&ixjsv=2.1.0&ixlib=rb-0.3.5&q=50&w=1500
next: faq
---

Blockstack is a decentralized network of computers that provides secure domain name services.

For a quick overview of what Blockstack is, check out [What is Blockstack?](/docs/what-is-blockstack), and continue reading on for a deeper dive into how blockstack works under the hood.

### Technical Overview

Blockstack's domain name system is supported by a network of Blockstack nodes. Each of these nodes maintains a database of domain names, the cryptographic keypairs the names are owned by, and the data records the names resolve to.

The Blockstack nodes build and continuously update the name database by processing a sequence of name operations, which include name registrations, name transfers, updates of data records associated with names, and more.

Blockstack name operations are embedded in blockchain transactions. After they are embedded and make it into a block, they are read by all Blockstack nodes, where each node then updates the its local copy of the name database. Right now, there is only one network of Blockstack nodes and that one sits on top of the Bitcoin blockchain.

<img src="/images/docs/blockstack-network.png" class="img-fluid" alt="The Blockstack Network">

### Virtual Blockchains

When a Blockstack node boots up, it must derive a name database that matches the databases stored by all other nodes. It does this by connecting to a Bitcoin node that it trusts (ideally one that is local) and reading all of the transactions in the blockchain in sequence.

If a transaction has a sequence of data that identifies it as a Blockstack transaction, it passes through the transaction filter and is inspected for validity. Otherwise it is ignored. If a Blockstack transaction has both the proper form and it doesn't violate any authorization rules, then it is added to the list of valid operations and queued up for processing (so that the name database may be updated). Otherwise, if the transaction is considered invalid, it is thrown away. For example, if a keypair issues an operation attempting to transfer a name that it doesn't own, the operation is flagged as invalid and discarded.

<img src="/images/docs/virtual-blockchain.png" class="img-fluid" alt="Virtual Blockchains">

All of the valid Blockstack operations make up what is referred to as a virtual blockchain. That is because the transactions of the underlying blockchain are filtered and interpreted in a context that the underlying blockchain is not aware of. The transactions are given meaning beyond what the underlying nodes maintaining the underlying blockchain are aware of. For example, a Bitcoin node may look at a Blockstack transaction and only see that bitcoins are moving from one place to another and that an unintelligible sequence of data has been attached in a data field (e.g. a field identified by OP_RETURN). Meanwhile, a Blockstack node will look at that data and will know how to read it and interpret it in a way that makes sense in the context of updating the name database.

### Name Databases

Blockstack nodes update their name databases by iterating through each block in the virtual blockchain and processing each of the operations in that block. For a given block all operations are committed at the same time. Thus, two name transfer operations cannot be processed in the same block. Time marches forward in a quantized fashion, where every operation must be non-conflicting with every other operation in the block.

The first type of operation is a name preorder, where the sender announces that it will register an undisclosed name in the future, but it doesn't want to reveal what name it is going to register yet, because doing so would allow attackers to execute replay attacks and steal the name. These operations do not result in any changes to the name database. Instead, they add a record to a pre-order pool..

The second type of operation is a name registration, where the sender announces it is registering a particular name and provides evidence that the name was preordered in a previous transaction.

These two operations together are known as a two-phase cryptographic commitment. In the preorder step, the value that is broadcasted is a hash of the name and the cryptographic keypair that the name should be registered under. Then, in the register step the name and the cryptographic keypair are both revealed and the hash in the first step can be verified.

The third type of operation is a name transfer, where the sender announces it is transferring ownership of a name it owns to another cryptographic keypair.

The fourth type of operation is a name update, where the sender announces it is updating the existing data record associated with a name it owns to a new data record. In this operation, only the hash of the data record is provided in the transaction and the data itself is stored elsewhere.

<img src="/images/docs/name-database.png" class="img-fluid" alt="Name Databases">

Even though only data record hashes are stored in blockchain transactions, and not the full records themselves, we know we can trust the validity of the records because of the valid cryptographic assumption that only one known data record can be hashed to produce a given hash. Put another way, for strong hash functions, collisions are assumed to be improbable to the point of practical impossibility. Once a hash value has been signed by a keypair and we find a piece of data that hashes to a given hash value, we can say by extension that the data itself has been signed. Note that this practice is ubiquitous and foundational to cryptographic signature systems.

### Data Record Storage

By default, Blockstack nodes store the data records associated with names in a distributed hash table (DHT) that all Blockstack nodes are connected to (the Blockstack nodes each have their own accompanying DHT nodes). Every Blockstack node knows to look in the DHT to resolve the hash of a data record to the data record itself.

<img src="/images/docs/data-record-storage.png" class="img-fluid" alt="Data Record Storage">

While the DHT is the default storage location for all data records, other copies of the data records may be stored in other locations. In fact, data mirrors may be set up that continuously mine the DHT records and maintain their own copies of the entire data set. And Blockstack nodes may be configured to look in these data mirrors first before looking in the DHT or anywhere else for the record.

When a data record is sent to the DHT to be stored, the nodes of the DHT use their routing algorithm to collectively assign the record to be stored by a subset of the nodes. The number of nodes that store the record is specified by the replication factor. For example, a replication factor of 20 means that a minimum of 20 nodes will store the record.

When a data record is looked up by its hash value, the nodes of the DHT coordinate to figure out which of the nodes can respond with the record and then one of those nodes responds to the requester with the appropriate value. The requester then checks to make sure that the value can be hashed to match the value hash that it used as the lookup term (known as a "key" in a key-value store, but not to be confused with a cryptographic key).
