---
title: Introduction
image: /images/article-photos/chalkboard.jpg
---

# Table of Contents 

1. Introduction
2. Blockchain
3. Name System
4. Peer Network
5. Storage
6. Identity
7. Auth
8. Related Work
9. Software
10. Conclusion & Future Work

With the Blockstack Core software, a network of computers collectively maintain a global registry of domain names, public keys, and cryptographic hashes. With this registry, Blockstack Core serves as a decentralized domain name system (DNS) and decentralized public key infrastructure (PKI).

When you run a Blockstack Core node, you join this network, which is more secure by design than traditional naming and digital registry systems. This is because the system's registry and its records are secured by an underlying blockchain, which is extremely resilient against tampering and control.

In the Blockstack Core registry, each of the names has an owner, represented by a cryptographic keypair, and is associated with instructions for how DNS resolvers and other software should resolve the name.

Blockstack provides:

- name lookups on a decentralized naming system
- name registrations and transfers without centralized registrars
- automatic binding of names to owning cryptographic keypairs
- automatic cache invalidation
- immunity to cache poisoning
- robust certificate pinning capabilities
- resistance to censorship of name registration and resolution

<img src="../images/blockstack-network.png" class="img-fluid" alt="The Blockstack Network">
