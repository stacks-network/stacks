---
title: Peer Network
image: /images/article-photos/chalkboard.jpg
---

One of the more interesting innovations in Blockstack is in
how it distributes the set of zone files to all peers.  
Like several other decentralized Web infrastructure projects, the original system used a [DHT](https://en.wikipedia.org/wiki/Distributed_hash_table)
(distributed hash table).  This was acceptable for building a prototype implementation while the network
was small and mostly-reliable.  However, this would have been unacceptable in the long-term due to the
stability and security problems inherent to DHTs.  Since November 2016, we have been distributing zone
files using a decentralized storage system built from first principles called the Atlas Network.

## DHTs: Unsafe at any Speed

DHTs came into being in the 1990's and 2000's, and were among the first
scalable decentralized data stores.  The most widely-used DHTs power file-sharing
software like BitTorrent and eMule.  These are based on the [Kademlia
DHT](http://www.maymounkov.org/papers/maymounkov-kademlia-lncs.pdf), and enjoy widespread usage today.

### Easy to Misuse

Since the mid 2000's, the distributed systems research community has learned several
hard but important lessons about the usability of DHTs.  In particular, DHTs are
only useful if *all* of the following are true for your application:

* **You can't store a 100% replica**.  Your application stores so much data that
it is unreasonable to try to keep a full copy on any single node.

* **You will tolerate arbitrarily slow I/O**.  Due to the way DHTs handle
requests, reads and writes have very variable latency.  Some incrmenetal
work on DHTs (like
[DSHTs](http://www.scs.stanford.edu/~dm/home/papers/freedman:coral.pdf)) try to
fix this for frequently-requested data, but the long-tail performance is still
terrible.  This is inherent to DHT routing protocols; a pathological
request can needlessly bounce through several high-latency network links
before being handled.

* **You will periodically re-announce data**.  Public-access DHTs allow
anyone to write to them.  To deal with so much data, they simply delete stale
data to relieve memory pressure.  At the same time, nodes can come and go as
they please, which can cause key/value pairs to get dropped.  To deal with this,
applications need to re-replicate data every so often to keep it available.

* **You will never change a key/value pair**.  DHTs can split into one or more disjoint
networks due to partitions, and re-join later on.  While split, a client can
write conflicting key/value pairs to nodes on either side of the partition.
This leads to externally-visible inconsistency--some clients will see one value
for the key, and other clients will see a different value.  To avoid this, the
application must ensure that there is at most one value per key (i.e. data is
immutable once written).

These are difficult demands to meet.  Each application process effectively needs
to be online 24/7 to ensure its data is available, and even then the developer needs to 
adress data consistency and I/O performance via some other way.

The reason BitTorrent and eMule can get
away with using DHTs is because (1) they use them only for "soft state," and (2)
they do not rely on them for correctness.  Specifically, they use a DHT to
store tracking and routing information for a particular file.  
This information is small by comparison to the
file, and can be re-created quickly by any peer.  There are no consistency
concerns since since the `.torrent` file contains all the chunk hashes, and
there are no negative consequences of
receiving invalid tracking data since the hashes are known to all peers
beforehand.  Peers also do not share data via the DHT, but connect to one
another directly.

### Hard to Secure

The difficulties do not end there, though.  DHTs are still vulnerable to three
types of attacks that can harm even the most resilient DHT-powered application.

* **Endless Data DDoS**.  Without some rate-limiting or access-control mechanism, a DHT has no way
to limit the amount of data inserted.  An adversary can flood the DHT with lots
of garbage data and knock nodes offline.  (This never applied to Blockstack,
since our DHT only accepted key/value pairs whose hashes were written to the
Bitcoin blockchain).

* **Hash-Bucket Takeover**.  By joining with the right nodes in a DHT, a Sybil
node can take over responsibility for specific hash buckets in the network.   In
doing so, the Sybil will both be able to see who's asking for the data (a
privacy concern), and will be able to censor the data by ignoring or slowing
down requests (an availability concern).  A Sybil node can also do extensive
damage to a running DHT by repeatedly joining it, taking over heavily-requested
buckets, and then dropping them.

* **Route-table Takeover**.  Suppose that the DHT let the developer "pin" 
hash buckets to honest nodes to thwart hash-bucket
takeovers.  This does not fix the availability problem, since a Sybil can insert itself
as the immediate neighbors of the honest node and prevent the rest of the
system from discovering it.  This works because DHT nodes do not have a global
view of which nodes have which buckets.  Instead, each node keeps a short list of
which nodes host buckets that are "close to" its buckets in the key space.
If the Sybil node can become an honest node's neighbors, then it can prevent
other nodes from discovering the honest node's data.

## The Problem with DHTs
Before v0.14, we had used a patched Kademlia DHT implementation for hosting zone files. Our patches ensured that (1) each key was the hash of its value, and (2) each key corresponded to an accepted name-update Blockstack transaction on Bitcoin. This prevented most classical DHT attacks — no one could overwrite a user’s key/value pairs, and no one could flood the DHT with lots of junk data.

However, DHTs are still vulnerable to routing attacks. Instead of trying to mess with the key/value pairs, an attacker can add and remove nodes in order to take control of individual hash buckets. These nodes can simply deny requests for data, censoring keys. If they take over all nodes with a copy of a key/value pair, they can simply discard it, leading to permanent zone file loss. This is a fundamental challenge to using structured overlay networks for decentralized storage (DHTs being one example). Since nodes do not store a full replica of the state, they have to route data requests to each other. Since anyone can add nodes to these networks, attackers can take control of routes to deny service and destroy data.

# Atlas Network
We overcome the challenges with DHTs with a new network called the Atlas network. With the Atlas network we make use of the property that (1) zone files are small (<4KB each), and (2) the total number grows at a fixed rate. It doesn’t take a lot of disk space to have each node host a full copy of all zone files (only ~300MB today). The Atlas network solves a special case of the general problem of reliable decentralized storage — the case where (1) the data set is small in size and (2) there is a full index of data available to the network.

Atlas nodes maintain a 100% state replica, and they organize into an unstructured overlay network to stay resilient against targeted node attacks. An Atlas node works a lot like a BitTorrent node. Each node gets the set of zone file hashes from the blockchain, and they constantly try to get zone files they don’t have.
The Atlas network implements a K-regular random graph. Each node selects K other nodes at random to be its neighbors via MHRWDA, and regularly asks them for the set of zone files they have. Peers pull missing zone files in rarest-first order to maximize availability (like BitTorrent), and store them both to locally and at remote backup locations (e.g., a user chosen storage service like Dropbox or S3). When it receives a missing zone file from a client, the node pushes it to its immediate neighbors that don’t have it yet.

The Atlas network is much more reliable than the previous DHT network. Like the DHT, Atlas nodes already know the hashes of the zone files, so no one can upload invalid data. But unlike the DHT, data is replicated on O(N) nodes instead of only on a small subset of nodes.

This strategy makes unavailability attacks expensive. To censor a target zone file for a single node, an attacker must persistently eclipse all of that node’s neighbors. Censoring the entire network requires attacking O(N) nodes. By contrast, only O(log N) DHT nodes need to be taken over to censor a zone file for everyone. Even then, the victim node will detect the censorship unless the attacker also eclipses the victim’s Bitcoin node (which requires building a fraudulent blockchain fork with sufficient PoW).
We believe that the Atlas network is a major step forward towards having a reliable, hard-to-censor, and decentralized data store for zone files and we’re excited to announce that v0.14 will start using the Atlas network in production. We plan to release detailed documentation and design on the Atlas network soon.
