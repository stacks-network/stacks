---
title: Blockstack DNS vs. Namecoin
description: Learn about how Blockstack DNS differs from Namecoin.
image: /images/article-photos/sprinting.jpg
next: namespaces
---

Blockstack DNS differs from Namecoin DNS in a few fundamental ways.

#### Blockchain Layering

Blockstack and Namecoin differ in how the domain name system is operated. Namecoin DNS is operated by nodes of a cryptocurrency called Namecoin, which is a fork of Bitcoin that requires its own separate blockchain. Blockstack DNS, meanwhile, has a portable architecture. It is designed to be able to read and write data to *any* blockchain and the logic for operating the domain name system is decoupled from the logic of the underlying blockchain. This allows one to run Blockstack DNS on the most secure blockchain. While this is currently the Bitcoin blockchain, Blockstore DNS and all of the network's state can be seamlessly ported to another blockchain if it ever makes sense to do so.

#### Storage Models

With Namecoin DNS, routing information is stored directly in the blockchain, which can lead to quite a bit of blockchain bloat. Blockstack DNS, meanwhile, stores only hashes of routing information records in the blockchain, deciding to store the rest in decentralized content-addressable storage units (by default, Blockstack is configured to store data in a DHT). These routing records then can link to other data stored elsewhere, whether that be in a DHT or on a hosted data storage provider like S3. This makes for a much more scalable and cost-efficient design.

#### Name Pricing Models

With Namecoin DNS, all names are set at the same low price and there are no options for users to create new namespaces and set their own name pricing schemes. This results in rampant squatting, which significantly degrades the user experience for anyone trying to register names. Blockstack DNS, meanwhile, has a wide range of options for users to create their own namespaces and set their own name pricing schemes. Namespaces can be created with really cheap names (great for a username namespace) or they can be created with really expensive names (great for a domain namespace resilient to squatting).

Name prices can be set to go down with an increase in the number of characters or with the presence of numbers and special characters. Furthermore, names can be set to expire in an arbitrary amount of time (e.g. a year), or they can be set to never expire at all. All these options allow users to design namespaces that encourage registration of names that users want and are willing to pay for, while dis-incentivizing the mass registration of names by squatters. All this leads to a superior user experience for everyone involved.

As an example, a name can be registered for a relatively low registration fee like $0.20 (in addition to a transaction fee of a few cents). Meanwhile, a shorter, desirable name may cost $10 or more.

#### Incentives for Miners

In the Namecoin system, money spent on name registrations is destroyed as a sacrifice. Blockstack works in a similar way today, but going forward registration fees for names will start going to miners. This creates a significant economic incentive for miners to contribute additional resources to the underlying blockchain, and it aligns everyone's interests around supporting a decentralized DNS system.
