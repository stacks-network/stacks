# Blockstack

[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

Blockstack is decentralized DNS and identity.

With the Blockstack software, a network of computers collectively maintain a global registry of names.

When you run a Blockstack node, you join this network, which is more secure by design than traditional DNS systems and identity systems. This is because the system's registry and its records are secured by an underlying blockchain, which is extremely resilient against tampering and control.

In the registry that makes up Blockstack, each of the names has an owner, represented by a cryptographic keypair, and is associated with instructions for how DNS resolvers and other software should resolve the name.

Blockstack is already being used in production and currently [more than 60,000 names](https://resolver.onename.com/v2/namespaces) have been registered using it.

<a href="https://blockstack.org/docs">
<img src="/images/documentation-site-2x.png" data-canonical-src="/images/documentation-site-2x.png" width="250" height="62" />
</a>

### Quick Installation

Run the following to install the Blockstack command line interface:

```
$ sudo pip install blockstack
```

### Project Links

![The Blockstack Network](/images/blockstack-network.png)

If you're just starting with Blockstack, here are the two main repositories you should checkout: 

- [Blockstack Server](https://github.com/blockstack/blockstack-server) - the server that handles the core functionality of the decentralized domain name system and has an external storage system built-in for storing data records off-chain
- [Blockstack Client](https://github.com/blockstack/blockstack-client) - a CLI and client library that provides an interface for interacting with Blockstack servers and performing decentralized DNS operations

If you're already familiar with basic concepts of Blockstack, below are some repositories and tools that can help in building applications using Blockstack or to run your own services using Blockstack:

- [Virtualchain](https://github.com/blockstack/virtualchain) - a Python library for creating virtual blockchains on top of any underlying blockchain
- [Blockstack Resolvers](https://github.com/blockstack/blockstack-resolver) - scalable servers for resolving names to data records at scale
- [Blockstack Registrars](https://github.com/blockstack/blockstack-registrar) - servers that can do bulk Blockstack name registrations and updates
- [Blockstack DHT Mirrors](https://github.com/blockstack/dht-mirror) - software that improves read and write performance for the Blockstore DHT
- [Blockstack Auth JS](https://github.com/blockstack/blockstack-auth-js) and [Blockstack Auth Python](https://github.com/blockstack/blockstack-auth-python) - libraries that support generating, decoding and verifying auth request and auth response tokens

Most of these repositories are under heavy development and we appreciate any feedback, bug reports, or code contributions!

### Articles

- [How Blockstack Works](https://blockstack.org/docs/how-blockstack-works)
- [Blockstack vs. DNS](https://blockstack.org/docs/blockstack-vs-dns)
- [Blockstack vs. Namecoin](https://blockstack.org/docs/blockstack-vs-namecoin)
- [Blockstack Namespaces](https://blockstack.org/docs/namespaces)
- [Blockstack Light Clients](https://blockstack.org/docs/light-clients)

### Blockstack Papers

- ["Blockstack: A Global Naming and Storage System Secured by Blockchains"](https://github.com/blockstack/blockstack/blob/master/papers/blockstack_usenix16.pdf), Proc. USENIX Annual Technical Conference (ATC ’16), June 2016
- ["Extending Existing Blockchains with Virtualchain"](https://github.com/blockstack/blockstack/blob/master/papers/virtualchain_dccl16.pdf), Proc. Workshop on Distributed Cryptocurrencies and Consensus Ledgers (DCCL '16), July 2016
- ["Bootstrapping Trust in Distributed Systems with Blockchains"](https://github.com/blockstack/blockstack/blob/master/papers/blockstack_login16.pdf), USENIX ;login: Magazine (pre-print)

### Community Resources

- [GitHub](https://github.com/blockstack) - share code, file issues, discuss future features, plan and document community activities
- [Slack Group](http://chat.blockstack.org) - real-time chat for all things Blockstack
- [Forum](http://forum.blockstack.org) - discussion forum for all things Blockstack
- [Blog](https://medium.com/blockstack-review) - a blog with the latest Blockstack articles
- [Twitter](https://twitter.com/blockstackorg) - social media feed curating Blockstack-related content from around the web

### Requests for Comments

- [Blockstack RFCs](/blockstack-rfcs.md)

### How You Can Help

- **Contribute code** - all Blockstack software is free and open source, so send us pull requests if you have any suggestions for ways the software can be improved
- **Help with software testing** - we really appreciate and value our testers, and encourage people who want to support Blockstack to run the software and file issues in the appropriate repository for any bugs that are found
- **Improve the documentation** - we can never have enough documentation so if there's anything you'd like to clarify or add, just fork any of the Blockstack repos, start writing and expanding on the docs, and submit a pull request
- **Organize community events** - we welcome anyone interested in putting together anything as simple as a meetup at a local library or community center to discuss the latest Blockstack developments and applications with like-minded people from your area
- **Produce and share content** - if you have ideas or insights about Blockstack or decentralized applications in general, write a post and submit it to theBlockstack community blog or share it in the forum
