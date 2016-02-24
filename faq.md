---
title: FAQ
description: Review the questions most frequently asked about Blockstack.
image: chalkboard.jpg
---

### How is Blockstack DNS different from ICANN DNS?

See this article for a full explanation:

[Blockstack DNS vs ICANN DNS](/docs/blockstack-vs-dns)

### How is Blockstack DNS different from Namecoin DNS?

See this article for a full explanation:

[Blockstack DNS vs Namecoin DNS](/docs/blockstack-vs-namecoin)

### What blockchain is Blockstack DNS built on?

Blockstack DNS is operated by nodes that read and write data to an underlying blockchain. The Blockstack DNS architecture is portable--the domain name system's logic is fully decoupled from the blockchain's logic. This lets Blockstack DNS leverage the most secure blockchain. This is the Bitcoin blockchain today but may be any other blockchain at some point in the future.

### Why isn't there a Blockstack network on a blockchain other than the Bitcoin blockchain?

It makes sense to focus on building one network out and putting energy into helping that network grow and succeed.

Of course, anyone could create a parallel Blockstack network on another blockchain, but the Blockstack development community has made the decision to operate the first network on top of the Bitcoin blockchain.

### Are DNS records stored in the blockchain?

No, only hashes of these records are stored in the blockchain. The records themselves are stored elsewhere and the Blockstack resolvers look up the full records by their hash. By default, records are stored in the Blockstack DHT (based on Kademlia).

### Can I run my own Blockstack node?

Yes, it's simple to get up and running. See this article for full instructions:

[Blockstack installation](/docs/installation)

### Why does a name have to be preordered before it is registered?

When a name is registered, that name registration is broadcast to the world. Anyone who sees a broadcasted transaction can replay the transaction, so if there was just a single registration step, then names would get stolen all the time. A two-stage commit process is employed to fix this, where one first says "I'm registering an undisclosed name" and then later says "I'm registering this name and here's proof that I meant to register this particular name earlier on" (referencing a hash in the first transaction).

### Is there support for names that don't ever expire?

Yes. Each namespace has it's own settings, so if you'd like to register names that don't expire, simply use a namespace that has a flag set for non-expiration.

### Does name ownership have multi-party support?

Absolutely. Blockstack supports multi-party ownership and more (in bitcoin, this is accomplished using multi-signature addresses). Any valid Bitcoin script (also known as a "scriptPubKey") may be set as the owner of a name.
