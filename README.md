# [Blockstack](http://blockstack.org)

[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

Blockstack is decentralized DNS and identity.

With the Blockstack software, a network of computers collectively maintain a global registry of names.

When you run a Blockstack node, you join this network, which is more secure by design than traditional DNS systems and identity systems. This is because the system's registry and its records are secured by an underlying blockchain, which is extremely resilient against tampering and control.

In the registry that makes up Blockstack, each of the names has an owner, represented by a cryptographic keypair, and is associated with instructions for how DNS resolvers and other software should resolve the name.

Blockstack is already being used in production and currently [more than 46,000 names](https://resolver.onename.com/v2/namespaces) have been registered using it.

[![View the Docs](/view-the-docs.png)](https://blockstack.org/docs)

![The Blockstack Network](/blockstack-network.png)

### Quick Installation

Run the following to install the Blockstack command line interface:

```
$ sudo pip install blockstack
```

## Project Links

Below are some repositories and tools that are needed to register, resolve, and authenticate names in a decentralized way:  

- [Blockstack Server](https://github.com/blockstack/blockstack-server) - the server that handles the core functionality of the decentralized domain name system and has an external storage system built-in for storing data records off-chain
- [Blockstack Client](https://github.com/blockstack/blockstack-client) - a CLI and client library that provides an interface for interacting with Blockstack servers and performing decentralized DNS operations
- [Virtualchain](https://github.com/blockstack/virtualchain) - a Python library for creating virtual blockchains on top of any underlying blockchain
- [Blockstack Resolvers](https://github.com/blockstack/blockstack-resolver) - scalable servers for resolving names to data records at scale
- [Blockstack Registrars](https://github.com/blockstack/blockstack-registrar) - servers that can do bulk Blockstack name registrations and updates
- [Blockstack DHT Mirrors](https://github.com/blockstack/dht-mirror) - software that improves read and write performance for the Blockstore DHT
- [Blockstack Auth JS](https://github.com/blockstack/blockstack-auth-js) and [Blockstack Auth JS](https://github.com/blockstack/blockstack-auth-python) - libraries that support generating, decoding and verifying auth request and auth response tokens

Most of these repositories are under heavy development and we appreciate any feedback, bug reports, or code contributions!

## Articles

- [How Blockstack Works](https://blockstack.org/docs/how-blockstack-works)
- [Blockstack vs. DNS](https://blockstack.org/docs/blockstack-vs-dns)
- [Blockstack vs. Namecoin](https://blockstack.org/docs/blockstack-vs-namecoin)
- [Blockstack Namespaces](https://blockstack.org/docs/namespaces)
- [Blockstack Light Clients](https://blockstack.org/docs/light-clients)

## The Blockstack Paper

* Muneeb Ali, Jude Nelson, Ryan Shea, Michael Freedman, ["Blockstack: Design and Implementation of a Global Naming System with Blockchains"](http://blockstack.org/blockstack.pdf), Draft v3, under peer review, Feb 2016

## Community Resources

- [GitHub](https://github.com/blockstack) - share code, file issues, discuss future features, plan and document community activities
- [Slack Group](http://chat.blockstack.org) - real-time chat for all things Blockstack
- [Forum](http://forum.blockstack.org) - discussion forum for all things Blockstack
- [Blog](https://medium.com/blockstack-review) - a blog with the latest Blockstack articles
- [Twitter](https://twitter.com/blockstackorg) - social media feed curating Blockstack-related content from around the web

## How You Can Help

#### Contribute code

All Blockstack software is free and open source, so you can inspect every line of code and send us pull requests if you have any suggestions for ways the software can be improved. You can also file an issue if you find a bug and want to discuss ways it can be fixed.

#### Debug Blockstack software

Testing software and uncovering bugs around the edge cases is one of the most thankless tasks in software development, but someone’s gotta do it! We really appreciate and value our testers, and encourage people who want to support Blockstack to run the software and file issues in the appropriate repository for any bugs that are found.

#### Improve documentation on any of our GitHub repositories

It’s easy to focus so much on coding that documentation becomes out of date. While we try our best to keep our document informative, up-to-date, and easy to read, we could always use a fresh pair of eyes. If you think of a way that we could improve our documentation, please let us know!

#### Organize community events

It’s great to hang out and collaborate online, but it’s also important to sync up in person from time to time. In-person events help catalyze new ideas, new projects, and new relationships that can have a big impact on our lives, and this is no less true in the Blockstack community. These events don’t have to be big, fancy conferences - it could be as simple as a meetup at a local library or community center to discuss the latest Blockstack developments and applications with like-minded people from your area. Documents produced for past events are stored [here](https://github.com/blockstack/events/wiki), and we will continue adding more with each additional event that is organized by the community.

#### Curate content for social media channels

Our social channels rely on a steady stream of content from around the web about the latest in Blockstack, blockchain, and decentralized application development. If you find an article, blog post, project, video, podcast, or anything else online that you think would be of interest to the Blockstack community, share it via Twitter @blockstackorg or #blockstack, Slack, or the Blockstack forum so we can add it to our feed.

#### Produce and share Blockstack content

We want to continue reaching more people who are interested in decentralized application development, and this means producing a steady stream of content about Blockstack to attract new people to our community. If you have ideas or insights about Blockstack or decentralized application development in general, write them down and share it in the Blockstack forum - even better if you can have your post published on another site with an audience we might not reach otherwise. You can also help by sharing content produced by other members of the community on your website or social media accounts.

#### Improve our website

Just like the Blockstack software, the Blockstack website is [open source](https://github.com/blockstack/blockstack-site) too! We welcome any and all suggestions for how we can improve the website to make it more inviting and informative for visitors. Whether it’s creating an explainer or tutorial video, adding an infographic, or updating the copy, every little improvement helps.
