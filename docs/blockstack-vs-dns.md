---
title: Blockstack DNS vs. Traditional DNS
description: Learn about how Blockstack DNS differs from traditional ICANN DNS.
image: /images/article-photos/football.jpg
next: blockstack-vs-namecoin
---

### Blockstack vs. Traditional DNS

As with the traditional domain name system, the Blockstack domain name system allows users to lookup, register, renew, and transfer names, as well as manage name resolution information.

But Blockstack DNS differs in a few fundamental ways from traditional DNS.

#### Decentralization

While the traditional domain name system is run by an international organization called ICANN, the Blockstack name registry is maintained in a completely decentralized way. It is run by everyone and it is controlled by no one, giving Blockstack DNS incredible and unprecedented technical and socio-political resilience. This is because each Blockstack DNS node independently calculates the current, global state of all names in the network, without needing to trust a 3rd party principal.

#### Protection Against Cache Poisoning

Traditional DNS relies on a fragile system of DNS caches for disseminating name resolution information. Meanwhile, Blockstack DNS's explicit cache invalidation system serves as a powerful mechanism for securely transmitting name resolution information that is both timely and 100% accurate. This helps make Blockstack DNS invulnerable to cache poisoning, without also requiring you to trust a central third party like a DNSSEC root server.

#### Cryptographic Keypair Bindings

Blockstack DNS and traditional DNS differ in how they associate names with certificates. Traditional DNS relies on a hierarchy of anointed organizations to attest to the ownership of domains. Here, each organization represents a systemic threat to name resolution security. Misbehavior of a single organization has wide-reaching, devastating consequences, because it effectively decides who controls which name. By contrast, every name in Blockstack DNS is automatically associated with a cryptographic keypair such that only the private key owner can control the name. Moreover, any end-user can audit and verify the authenticity of each name's record and ownership history.
