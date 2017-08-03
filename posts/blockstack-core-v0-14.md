---
title: Blockstack Core v0.14.0 Release
description: We are pleased to announce the upcoming release of version 0.14.0 of Blockstack Core
image: /images/article-photos/blockstack-core-v0-14/header.png
next: blockstack-core-v0-14-0-release
date: October 6, 2016
---

This is the largest release of Blockstack Core since the initial release in September 2015 and is a major update. Version 0.14 is a hard fork that will activate at Bitcoin block 436363. This release removes our dependence on a distributed hash table (DHT) network, improves performance, reduces memory footprint, and adds support for multisig and a RESTful API.

<img src="/images/article-photos/blockstack-core-v0-14/warning.png" width="100%" alt="Version 0.14 is a hard fork that will activate at Bitcoin block 436363" />

Below are some notable features that are included in this release:

- **Better Data Reliability.** When we launched Blockstack, we included a default DHT-based network for storing additional data. The pointers for data were in the blockchain and the off-chain routing data (zone files) were stored in the DHT. DHTs are traditionally unreliable and hard to scale and we faced these challenges in our production deployment. The biggest change in v0.14 is that it replaces the Blockstack DHT with a new unstructured BitTorrent-like network called the Atlas network which is much more reliable than the previous DHT network.
- **20x RAM reduction.** The earlier version of Blockstack Core used a flat JSON file for storing data, which worked at small scale but had performance issues at larger scale. More specifically, the memory footprint of using a flat JSON file became too much. Blockstack Core v0.14 stores its state in a sqlite3 database, which yields an overall 20x reduction in RAM usage (down to 150MB from 3GB), and reduces the complexity of adding support for new types of data queries.
- **6x Faster Synchronization.** One of the main bottlenecks for boot up time for new nodes is the speed at which it can synchronize with the underlying blockchain. The v0.14 release of Virtualchain now fetches most of its data from Bitcoin’s peer-to-peer network, instead of via RPC. This yields a 6x performance improvement and removes the need for the multiprocess work pool used in v0.13. We had to write custom software to fetch data directly from the Bitcoin backplane, instead of the widely used RPC interface, and we hope that other projects in the ecosystem can also use our open-source code for faster block-fetching.
- **Multisig Support.** Security of name ownership is very important to us. The v0.14 release now supports multisig — that is, a quorum of key-pairs can pay for and manage names. This is more secure than using a single key, since now the user can divide up the set of keys across multiple devices and multiple trusted parties. Version 0.14 of the client release defaults to a 2-of-3 quorum, using pay-to-script-hash Bitcoin addresses.
- **RESTful API.** In order to make it simpler to use Blockstack Core, we’ve included a RESTful interface with built-in documentation in the v0.14 release, in addition to the already existing RPC interface. We’ve also merged independent servers/components like the resolver, search, and a few others into a single, easily accessible API with the v0.14 release.
- **Testnet Support.** We want to make it easier for developers to rapidly test their applications without worrying about spending tokens on the live network. The v0.14 release supports Bitcoin’s testnet network, which we leverage in version v0.14 in our integration test framework.

<img src="/images/article-photos/blockstack-core-v0-14/diagram.png" width="100%" alt="Blockstack protocol diagram" />

### Better Data Reliability

One of the biggest milestones of this release is the addition of the Atlas network. It solves a [long-standing issue](https://github.com/blockstack/blockstack-core/issues/219) of ensuring zone file data reliability. We want to ensure that zone files stay online and don’t get lost, even if Blockstack nodes come and go. This is vital for resolving Blockstack profiles, since zone files link the on-chain pointers to off-chain state in external storage.

#### The Problem with DHTs

Before v0.14, we had used a patched [Kademlia DHT implementation](https://github.com/bmuller/kademlia) for hosting zone files. Our patches ensured that (1) each key was the hash of its value, and (2) each key corresponded to an accepted name-update Blockstack transaction on Bitcoin. This prevented most classical DHT attacks — no one could overwrite a user’s key/value pairs, and no one could flood the DHT with lots of junk data.

However, **DHTs are still vulnerable to routing attacks**. Instead of trying to mess with the key/value pairs, an attacker can add and remove nodes in order to take control of individual hash buckets. These nodes can simply deny requests for data, censoring keys. If they take over all nodes with a copy of a key/value pair, they can simply discard it, leading to permanent zone file loss. **This is a fundamental challenge to using structured overlay networks for decentralized storage** (DHTs being one example). Since nodes do not store a full replica of the state, they have to route data requests to each other. Since anyone can add nodes to these networks, attackers can take control of routes to deny service and destroy data.

#### Atlas Network

We overcome the challenges with DHTs with a new network called the Atlas network. With the Atlas network we make use of the property that (1) zone files are small (<4KB each), and (2) the total number grows at a fixed rate. It doesn’t take a lot of disk space to have each node host a full copy of all zone files (only ~300MB today). The Atlas network solves a special case of the general problem of reliable decentralized storage — the case where (1) the data set is small in size and (2) there is a full index of data available to the network.

Atlas nodes maintain a 100% state replica, and they organize into an unstructured overlay network to stay resilient against targeted node attacks. An Atlas node works a lot like a BitTorrent node. Each node gets the set of zone file hashes from the blockchain, and they constantly try to get zone files they don’t have.

The Atlas network implements a K-regular random graph. Each node selects K other nodes at random to be its neighbors via [MHRWDA](http://www4.ncsu.edu/~dyeun/pub/sigmetrics%2712-full-double-column.pdf), and regularly asks them for the set of zone files they have. Peers pull missing zone files in rarest-first order to maximize availability (like BitTorrent), and store them both to locally and at remote backup locations (e.g., a user chosen storage service like Dropbox or S3). When it receives a missing zone file from a client, the node pushes it to its immediate neighbors that don’t have it yet.

The Atlas network is much more reliable than the previous DHT network. Like the DHT, Atlas nodes already know the hashes of the zone files, so no one can upload invalid data. But unlike the DHT, data is replicated on O(N) nodes instead of only on a small subset of nodes.

This strategy makes unavailability attacks expensive. To censor a target zone file for a single node, an attacker must persistently eclipse all of that node’s neighbors. Censoring the entire network requires attacking O(N) nodes. By contrast, only O(log N) DHT nodes need to be taken over to censor a zone file for everyone. Even then, the victim node will detect the censorship unless the attacker also eclipses the victim’s Bitcoin node (which requires building a fraudulent blockchain fork with sufficient PoW).

We believe that the Atlas network is a major step forward towards having a reliable, hard-to-censor, and decentralized data store for zone files and we’re excited to announce that v0.14 will start using the Atlas network in production. We plan to release detailed documentation and design on the Atlas network soon.

### Consensus Notes

Version 0.14 is a consensus-breaking release — once deployed, it will not be compatible with earlier releases. This is because earlier releases do not accept transactions sent from multisig outputs. As such, v0.14 is a **hard fork** from v0.13. Every node operator is encouraged to upgrade to v0.14 as soon as we release it, since v0.13 and v0.14 will [diverge into two separate fork sets](https://blog.blockstack.org/blockchains-for-distributed-systems-ffd68e6341b5#.ei40w6m6h).

Version 0.14 implements phase 1 of a 2-phase improvement in how we manage names and identities. The end goal is that a user’s on-chain *identity* information (i.e. its zone file and public key hashes) will have a unique serial number in the .id namespace and will never expire. Names in the .id namespace will point to these identities, and must be periodically renewed. Version 0.15 will implement phase 2 of our improvement plan, and will be implemented as another hard-fork one year from now. The discussion thread and a description of the plan can be found [here](https://github.com/blockstack/blockstack-core/issues/244#issuecomment-251226177).

We will switch our infrastructure over from v0.13 to v0.14 at **block 436363 in the Bitcoin blockchain**. After this block height, v0.13 and v0.14 are expected to diverge, since this is the height at which the consensus-breaking changes in v0.14 will activate.

**Node operators have about 3 weeks to upgrade. If you need help doing so, please drop us a line on our Slack channel at [chat.blockstack.org](http://chat.blockstack.org).**

### Getting Blockstack Core

Please check out the [repository](https://github.com/blockstack/blockstack-core) on GitHub, and star it if you like it!

Please note that v0.14 will be unusable until block 436363. This is when the new features activate. However, if you want to test them in an offline deployment, see the documentation [here](https://github.com/blockstack/blockstack-integration-tests/blob/rc-0.14.0/README.md).

### Contributors

We would like to thank the following people for helping us get the 0.14 release ready. Thank you everyone for sending pull requests, helping us test the software, submitting bug reports, and being patient with us while we fix them!

- @aagorelik
- Aran Dunkley
- Burt Bielicki
- Carver Harrison
- Charles Lehner
- @cryptid11
- Daniel Buchner
- Derek Martin
- Donncha O’ Cearbhaill
- @fpischedda
- George Ty
- @Gitju
- Guy Lepage
- @JFiscella
- John Light
- Jude Nelson
- Justin Drake
- @JZA
- @koinster
- Muneeb Ali
- Larry Salibra
- Odin Hørthe Omdal
- Pandu Rao
- @ruxton
- Ryan Shea
- Sam Wood
- Samantha Atkins
- Santiago Siri
- Sebastian Pir
- Stanislas Marion
- Stephen Edgar
- Stian Ellingsen
- @syck
- Whit Jackson
- @wutengcoding
- Xiaowei Liu

![Blockstack social icons](/images/article-photos/blockstack-core-v0-14/social.png)

- Website . [blockstack.org](http://blockstack.org)
- Slack . [chat.blockstack.org](http://chat.blockstack.org)
- Reddit . [r/blockstack](http://reddit.com/r/blockstack)
- Twitter . [@blockstackorg](http://twitter.com/blockstackorg)
- Medium . [blog.blockstack.org](http://blog.blockstack.org)
- GitHub . [@blockstack](http://github.com/blockstack)
- YouTube . [https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ](https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ)