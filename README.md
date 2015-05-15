# Blockchain Name System

The Blockchain Name System (BNS), formerly known as Openname, is very similar to the Domain Name System (DNS), but differs in that it gives stronger guarantees on ownership and security, has no trusted parties or "root servers", and is completely decentralized.

The Blockchain Name System is composed of several layers. At the bottom layer, raw identity data corresponding to user passcards is stored in a decentralized (usually blockchain-based) key-value store like Namecoin or Blockstore. In the middle layer, resolvers read, interpret, and verify data from the datastore and make it readily accessible to services. In the top layer, passcard galleries grab data from resolvers and render it into a visual format.

[![Read the Wiki](https://raw.githubusercontent.com/namesystem/namesystem/master/images/read-the-wiki.png)](https://github.com/namesystem/namesystem/wiki)

![Blockchain Name System Layers](https://raw.githubusercontent.com/namesystem/namesystem/master/images/blockchain-name-system-1.png)