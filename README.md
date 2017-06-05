# Blockstack

[![Slack](http://chat.blockstack.org/badge.svg)](http://chat.blockstack.org/)

Blockstack is a new decentralized internet where you own your data and your apps run locally without remote servers.

Blockstack provides decentralized services for naming/DNS, identity, authentication and storage. Developers can use JavaScript libraries to build serverless apps and they don't need to worry about managing infrastructure. Blockstack replaces the current client/server model; users control their data, apps run client-side, and the open Blockstack network replaces server-side functionality.

## Table of Contents

- [Architecture](#architecture)
- [Code](#code)
- [Tutorials](#tutorials)
- [Papers](#papers)
- [Events](#events)
- [Swag & Brand](#swag-&amp;-brand)
- [Requests for Comments](#requests-for-comments)
- [How to Help](#how-to-help)
- [Media Guide](#media-guide)

## Architecture

Blockstack has been used in production for 3+ years and [70,000+ domains](https://resolver.onename.com/v2/namespaces) have been registered using it.

With the Blockstack software, a network of computers collectively maintain a global registry of names. When you run a Blockstack node, you join this network, which is more secure by design than traditional DNS and identity systems. This is because the system's registry and its records are secured by an underlying blockchain, which is extremely resilient against tampering and control.

In the registry that makes up Blockstack, each of the names has an owner, represented by a cryptographic keypair, and is associated with instructions for how DNS resolvers and other software should resolve the name. 

Different layers of Blockstack are shown in the following figure:

<p>
<img src="https://raw.githubusercontent.com/blockstack/blockstack/master/images/bsk-architecture-diagram5.png" data-canonical-src="https://raw.githubusercontent.com/blockstack/blockstack/master/images/bsk-architecture-diagram5.png" />
</p>

You can read more details about Blockstack's architecture by reading the following articles:
- [What is Blockstack Core?](https://blockstack.org/articles/blockstack-core)
- [How Blockstack Works](https://blockstack.org/articles/how-blockstack-works)

## Code

If you're just starting with Blockstack, here are the main software repositories you should checkout: 

- [Blockstack Core](https://github.com/blockstack/blockstack-core) - the reference implementation of Blockstack written in Python.
- [Blockstack Portal](https://github.com/blockstack/blockstack-portal) - the Blockstack Browser Portal providing a graphical interface.
- [blockstack.js](https://github.com/blockstack/blockstack-portal) - a JavaScript library for using Blockstack identity and authentication in your apps.

## Tutorials

- CLI (Command Line Interface)
  - [Installation & Usage](https://blockstack.org/docs)
  - [VIDEO Tutorials](https://www.youtube.com/playlist?list=PLXS8JJHIn4nGCU2uW85dHXpkQJ7QA5JkX)
- Decentralized Apps
  - [Hello World](https://blockstack.org/tutorials/hello-blockstack)

## Papers

- ["Blockstack: A Global Naming and Storage System Secured by Blockchains"](https://github.com/blockstack/blockstack/blob/master/papers/blockstack_usenix16.pdf), Proc. USENIX Annual Technical Conference (ATC ’16), June 2016
- ["Extending Existing Blockchains with Virtualchain"](https://github.com/blockstack/blockstack/blob/master/papers/virtualchain_dccl16.pdf), Proc. Workshop on Distributed Cryptocurrencies and Consensus Ledgers (DCCL '16), July 2016
- ["Bootstrapping Trust in Distributed Systems with Blockchains"](https://github.com/blockstack/blockstack/blob/master/papers/blockstack_login16.pdf), USENIX ;login: Magazine (pre-print)

## Online Communities

- [Mailing List](http://blockstack.us14.list-manage1.com/subscribe?u=394a2b5cfee9c4b0f7525b009&id=0e5478ae86) (3,000+ members)
- [Blockstack Forum](http://forum.blockstack.org)
- [Live chat on Slack](http://chat.blockstack.org/) (2,400+ members)
- [Meetup Groups](http://www.meetup.com/topics/blockstack/) - Join Meetup groups around the world
- [Engineering Blog](https://blockstack.org/blog) - Engineering updates by developers
- [YouTube](https://www.youtube.com/channel/UC3J2iHnyt2JtOvtGVf_jpHQ) - Watch videos on the YouTube channel
- [Twitter](https://twitter.com/blockstackorg) - Follow the tweets of the Blockstack community

## Events

* [Blockstack Events](/events/README.md)
  * [Event Hosting Checklist](/events/events-guidelines.md)
  * [Past Events](/events/archive.md)

## Swag & Brand

* [Swag](https://github.com/blockstack/blockstack/issues/96)
* [Blockstack Brand](https://projects.invisionapp.com/d/main#/boards/4846740)

## Requests for Comments

- [Blockstack RFCs](/blockstack-rfcs.md)

## How to Help

- **Contribute code** - all Blockstack software is free and open source, so send us pull requests if you have any suggestions for ways the software can be improved
- **Help with software testing** - we really appreciate and value our testers, and encourage people who want to support Blockstack to run the software and file issues in the appropriate repository for any bugs that are found
- **Improve the documentation** - we can never have enough documentation so if there's anything you'd like to clarify or add, just fork any of the Blockstack repos, start writing and expanding on the docs, and submit a pull request
- **Organize community events** - we welcome anyone interested in putting together anything as simple as a meetup at a local library or community center to discuss the latest Blockstack developments and applications with like-minded people from your area
- **Produce and share content** - if you have ideas or insights about Blockstack or decentralized applications in general, write a post and submit it to the Blockstack community blog or share it in the forum

#### [Become a local Blockstack Community Evangelist](/community/README.md)

### [Media Guide](/media/README.md)

- [Appearances](/media/appearances.md)
- [Messaging](/media/messaging.md)
- [Terminology](/media/terminology.md)
- [Bio](https://github.com/blockstack/blockstack/blob/master/media/bios.md)
