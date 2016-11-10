---
title: Blockstack DNS
description: Blockstack DNS is a new domain name system and public key distribution system.
image: /images/article-photos/football.jpg
---

Blockstack DNS is Blockstack's decentralized domain name system and public key distribution system. It operates in parallel to the traditional domain name system and certificate authority system and offers several major benefits.

With Blockstack DNS, bindings are established between domain names, public keys, and cryptographic hashes.

These bindings are maintained in a global registry that is maintained by Blockstack Core servers, which form the backbone of the Blockstack system.

When you run a Blockstack Core node, you join this network and process updates to the registry alongside all of the other nodes.

Blockstack Core nodes update the registry by connecting to a blockchain and reading the transactions in sequence. Some of these transactions have specially encoded data that instructs the Blockstack Core nodes to make a registry update. If the transactions are properly formatted and fit into the consensus rules of the Blockstack Core nodes, those transactions are accepted and the registry is updated.

Blockstack DNS provides:

- name lookups on a decentralized naming system
- name registrations and transfers without centralized registrars
- automatic binding of names to owning cryptographic keypairs
- automatic cache invalidation
- immunity to cache poisoning
- robust certificate pinning capabilities
- resistance to censorship of name registration and resolution
