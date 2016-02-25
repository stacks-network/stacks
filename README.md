# [Blockstack](http://blockstack.org)

[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

Blockstack is decentralized DNS and identity.

With the Blockstack software, a network of computers collectively maintain a global registry of names.

When you run a Blockstack node, you join this network, which is more secure by design than traditional DNS systems and identity systems. This is because the system's registry and its records are secured by an underlying blockchain, which is extremely resilient against tampering and control.

In the registry that makes up Blockstack, each of the names has an owner, represented by a cryptographic keypair, and is associated with instructions for how DNS resolvers and other software should resolve the name.

You can install blockstack by:
```
$ sudo pip install blockstack
```

Detailed install instruction at [here](http://github.com/blockstack/blockstack-client). For more information checkout these [tutorials](https://blockstack.org/docs) on the website or read the following paper:

* Muneeb Ali, Jude Nelson, Ryan Shea, Michael Freedman, ["Blockstack: Design and Implementation of a Global Naming System with Blockchains"](http://blockstack.org/blockstack.pdf), Draft v3, under peer review, Feb 2016

## Project Links

Below are some repositories and tools that are needed to register, resolve, and authenticate names in a decentralized way:  

- [Blockstack-server](https://github.com/blockstack/blockstack-server), which is used for registering names on the Bitcoin blockchain. Blockstack-server handles the core functionality of decentralized DNS for blockchain applications and has an external storage system built-in for storing data records off-chain.  
- [Blockstore-client](https://github.com/blockstack/blockstore-client), which provides an interface for interacting with the Blockstack server and to perform decentralized DNS operations.   
- [Blockchain-auth-js](https://github.com/blockstack/blockchain-auth-js) or [blockchain-auth-python](https://github.com/blockstack/blockchain-auth-python), libraries that support generating, decoding and verifying auth request and auth response tokens.  
- [Blockstack-resolver](https://github.com/blockstack/blockstack-resolver), a scalable server for resolving names to data records at scale.  
- [Blockstack-registrar](https://github.com/blockstack/blockstack-registrar), software that can do bulk registrations and updates.  
- [Virtual chain](https://github.com/blockstack/virtualchain), a Python library for creating virtual blockchains on top of a well-known cryptocurrency.  
- [DHT mirror](https://github.com/blockstack/dht-mirror), software that improves read/write performance for the Blockstore DHT.  

Most of these repositories are under heavy development and we appreciate any feedback, bug reports, or code contributions!

## Blockstack vs. DNS

A detailed discussion of differences is [here](https://blockstack.org/docs/blockstack-vs-dns).

## Blockstack vs. Namecoin

A detailed discussion of differences is [here](https://blockstack.org/docs/blockstack-vs-namecoin).


## Community

[GitHub](https://github.com/blockstack) - share code, file issues, discuss future features, plan and document community activities

[Slack](http://chat.blockstack.org) - real-time chat for all things Blockstack

[Forum](http://forum.blockstack.org) - discussion forum for all things Blockstack

[Twitter](https://twitter.com/blockstackorg) - social media feed curating Blockstack-related content from around the web

[YouTube](https://www.youtube.com/channel/UCvDtRhHLNDyKiY-iwhneNbw) - videos and playlists featuring Blockstack-related content

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
