# Blockstack

[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

Blockstack is decentralized DNS and identity.

With the Blockstack software, a network of computers collectively maintain a global registry of names.

When you run a Blockstack node, you join this network, which is more secure by design than traditional DNS systems and identity systems. This is because the system's registry and its records are secured by an underlying blockchain, which is extremely resilient against tampering and control.

In the registry that makes up Blockstack, each of the names has an owner, represented by a cryptographic keypair, and is associated with instructions for how DNS resolvers and other software should resolve the name.

Blockstack is already being used in production and currently [more than 46,000 names](https://resolver.onename.com/v2/namespaces) have been registered using it.

[![Documentation Site](https://raw.githubusercontent.com/blockstack/blockstack/docs/images/documentation-site-2x.png =250x62)](https://blockstack.org/docs)

![The Blockstack Network](/images/blockstack-network.png)

### Quick Installation

Run the following to install the Blockstack command line interface:

```
$ sudo pip install blockstack
```

### Project Links

Below are some repositories and tools that are needed to register, resolve, and authenticate names in a decentralized way:  

- [Blockstack Server](https://github.com/blockstack/blockstack-server) - the server that handles the core functionality of the decentralized domain name system and has an external storage system built-in for storing data records off-chain
- [Blockstack Client](https://github.com/blockstack/blockstack-client) - a CLI and client library that provides an interface for interacting with Blockstack servers and performing decentralized DNS operations
- [Virtualchain](https://github.com/blockstack/virtualchain) - a Python library for creating virtual blockchains on top of any underlying blockchain
- [Blockstack Resolvers](https://github.com/blockstack/blockstack-resolver) - scalable servers for resolving names to data records at scale
- [Blockstack Registrars](https://github.com/blockstack/blockstack-registrar) - servers that can do bulk Blockstack name registrations and updates
- [Blockstack DHT Mirrors](https://github.com/blockstack/dht-mirror) - software that improves read and write performance for the Blockstore DHT
- [Blockstack Auth JS](https://github.com/blockstack/blockstack-auth-js) and [Blockstack Auth JS](https://github.com/blockstack/blockstack-auth-python) - libraries that support generating, decoding and verifying auth request and auth response tokens

Most of these repositories are under heavy development and we appreciate any feedback, bug reports, or code contributions!

### Articles

- [How Blockstack Works](https://blockstack.org/docs/how-blockstack-works)
- [Blockstack vs. DNS](https://blockstack.org/docs/blockstack-vs-dns)
- [Blockstack vs. Namecoin](https://blockstack.org/docs/blockstack-vs-namecoin)
- [Blockstack Namespaces](https://blockstack.org/docs/namespaces)
- [Blockstack Light Clients](https://blockstack.org/docs/light-clients)

### Blockstack Papers

- ["Blockstack: Design and Implementation of a Global Naming System with Blockchains"](http://blockstack.org/blockstack.pdf) by Muneeb Ali, Jude Nelson, Ryan Shea, and Michael Freedman (Draft v3, under peer review, Feb 2016)

### Community Resources

- [GitHub](https://github.com/blockstack) - share code, file issues, discuss future features, plan and document community activities
- [Slack Group](http://chat.blockstack.org) - real-time chat for all things Blockstack
- [Forum](http://forum.blockstack.org) - discussion forum for all things Blockstack
- [Blog](https://medium.com/blockstack-review) - a blog with the latest Blockstack articles
- [Twitter](https://twitter.com/blockstackorg) - social media feed curating Blockstack-related content from around the web

### How You Can Help

- **Contribute code** - all Blockstack software is free and open source, so send us pull requests if you have any suggestions for ways the software can be improved
- **Help with software testing** - we really appreciate and value our testers, and encourage people who want to support Blockstack to run the software and file issues in the appropriate repository for any bugs that are found
- **Improve the documentation** - we can never have enough documentation so if there's anything you'd like to clarify or add, just fork any of the Blockstack repos, start writing and expanding on the docs, and submit a pull request
- **Organize community events** - we welcome anyone interested in putting together anything as simple as a meetup at a local library or community center to discuss the latest Blockstack developments and applications with like-minded people from your area
- **Produce and share content** - if you have ideas or insights about Blockstack or decentralized applications in general, write a post and submit it to theBlockstack community blog or share it in the forum
