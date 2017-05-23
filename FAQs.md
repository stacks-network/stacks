---
title: FAQ
description: Review the questions most frequently asked about Blockstack.
image: /images/article-photos/chalkboard.jpg
---

# Frequently Asked Questions

### What is Blockstack?

Blockstack is a new decentralized internet.

With Blockstack, users control their data and apps run on their devices. There are no middlemen, no passwords, no massive data silos to breach, and no services tracking us around the internet.

The applications on blockstack are server-less and decentralized. Developers start by building a single-page application in Javascript, Then, instead of plugging the frontend into a centralized API, they plug into an API run by the user. Developers install a library called `blockstack.js` and don't have to worry about running servers, maintaining databases, or building out user management systems.

Personal user APIs ship with the Blockstack app and handle everything from identity and authentication to data storage. Applications can request permissions from users and then gain read and write access to user resources.

Data storage is simple and reliable and uses existing cloud infrastructure. Users connect with their Dropbox, Google Drive, etc and data is synced from their local device up to the cloud.

Identity is user-controlled and utilizes the blockchain for secure management of keys, devices and usernames. When users login with apps, they are anonymous by default and use an app-specific key, but their full identity can be revealed and proven at any time. Keys are for signing and encryption and can be changed as devices need to be added or removed.

Under the hood, Blockstack provides a decentralized domain name system (DNS), decentralized public key distribution system, and registry for apps and user identities.

### What is a Blockstack ID?

This is a the name & identity registered in the .id namespace on Blockstack. Your personal data and storage are built around this ID. Apps that want to access your data will be built around this as well.

### What is a decentralized internet?

A decentralized internet is one where users don't need to trust any intermediaries or remote services. We envision a world where users control their own data, and the power goes back to the users. Reducing the friction to deploying new Blockstack nodes is an important step towards that mission.

### What problems does Blockstack solve?

Developers can now build Web applications where:

* you own your data, not the application
* you control where your data is stored
* you control who can access your data

Developers can now build Web applications where:

* you don't have to deal with passwords
* you don't have to host everyone's data
* you don't have to run app-specific servers

Right now, Web application users are "digital serfs" and applications are the "digital landlords". Users don't own their data; the app owns it. Users don't control where data gets stored; they can only store it on the application. Users don't control access to it; they only advise the application on how to control access (which the application can ignore).

Blockstack applications solve both sets of problems. Users pick and choose highly-available storage providers like Dropbox or BitTorrent to host their data, and applications read it with the user's consent. Blockstack ensures that all data is signed and verified and (optionally) encrypted end-to-end, so users can treat storage providers like dumb hard drives: if you don't like yours, you can swap it out with a better one. Users can take their data with them if they leave the application, since it was never the application's in the first place.

At the same time, developers are no longer on the hook for hosting user data. Since users bring their own storage and use public-key cryptography for authentication, applications don't have to store anything--there's nothing to steal when they get hacked. Moreover, many Web applications today can be re-factored so that everything happens client-side, obviating the need for running dedicated application servers.

### What opportunities does Blockstack enable?

(coming soon)

### What is a "serverless" app?

The application itself should not run application-specific functionality on a server. All of its functionality should run on end-points. However, the application may use non-app-specific servers with the caveat that they must not be part of the trusted computing base. This is the case with storage systems like Amazon S3 and Dropbox, for example, because Blockstack's data is signed and verified end-to-end (so the storage systems are not trusted to serve data). Serverless can also mean applications where some amount of server-side logic is still written by the application developer but unlike traditional architectures is run in stateless compute containers that are event-triggered, ephemeral (may only last for one invocation)

### What is a "decentralized" app?

Decentralized apps are a new type of software program designed to exist on the Internet in a way that is not controlled by any single entity. Where bitcoin is a decentralized value exchange, a decentralized application aims to achieve functionality beyond transactions that exchange value. Many types of decentralized apps are starting to emerge as blockchain technology continues to progress. More companies and individuals are seeing the potential for what can be achieved in decentralizing not just money but almost any type of computing imaginable.

Decentralized apps potentially represent the next generation of computing. In a completely decentralized world all things occur using peer-to-peer networks and the idea of centralized entities are non-existent. This distributed future is still being designed and built but the early stages of development are looking promising.

### Who should build on Blockstack?

(coming soon)

### How are Blockstack domains different from normal DNS domains? 

Blockstack domains are not registered on the traditional DNS run by an organized called ICANN. Instead they're registered on a blockchain in a fully decentralized way. This means that Blockstack domains are truly owned by their owners and cannot be taken away. All Blockstack domains have public keys by default (public keys are required to own the domains), unlike the traditional DNS where a small fraction of domains get the (optional) public key certificates.

### What is Blockstack Core and who is working on it?

(coming soon)

### What is a virtual chain?

Blockstack is designed around a "virtual chain" concept, where nodes only need to reach consensus on the shared "virtual chain" they're interested in. Virtual chains do not interact with one another, and a single blockchain can host many virtual chains. These virtual chains can live in any blockchain for which there exists a driver, and virtual chain clients only need to execute their virtual chain transactions (i.e. Blockstack only processes Blockstack virtual chain transactions).

### What's the difference between Onename and Blockstack?

Onename is the free Blockstack ID registrar run by Blockstack to onboard new users. 

### How is Blockstack different from Namecoin?

Blockstack DNS differs from Namecoin DNS in a few fundamental ways: blockchain layering, storage models, name pricing models, and incentives for miners. We wrote a post where you can learn more here: https://blockstack.org/docs/blockstack-vs-namecoin

### I heard you guys were on Namecoin, what blockchain do you use now?

(coming soon)

### How is Blockstack different from Ethereum for building decentralized apps? 

You can think of Ethereum as a "heavy" blockchain that does everything for you. All the complexity is handled there, computations run there, and all scalability and security issues need to be handled at the blockchain layer. Blockstack puts minimal logic into a blockchain and handles scalability outside of the blockchain by re-using existing internet infrastructure in new ways. Read more about this in the following forum post: https://forum.blockstack.org/t/what-is-the-difference-between-blockstack-and-ethereum/781/2

### Can Blockstack only run on Bitcoin?

The model we're currently exploring is where Blockstack can process multiple blockchains to construct the global state where each namespace is tied to a single blockchain. Meaning that say the .id namespace is defined to run on Bitcoin and a .eth namespace is defined to run on Ethereum. Blockstack can process transactions from both blockchains and update the state of namespaces, but the consistency of any given namespace depends only on the underlying blockchain it was defined on.

### Does Blockstack use a DHT (Distributed Hash Table)?

It does not, as of November 2016.  It uses a much more reliable system called the Atlas Network.  Details here: https://blog.blockstack.org/blockstack-core-v0-14-0-release-aad748f46d#.30gzlthdw

### Can the Blockstack network fork? 

Yes, the Blockstack network can fork if the underlying blockchain encounters a deep fork.  In this case, blockstack nodes on either side of the fork will diverge from one another.

We have yet to encounter a deep fork.  If this does happen, then Blockstack will use the virtualchain state on the majority fork once the fork resolves.

### How is the Blockstack network upgraded over time? What parties need to agree on an upgrade?

We're working on an on-chain voting strategy similar to how mining works, where anyone can cast a vote proportional to the amount of Bitcoin burned.  Similar to how Bitcoin upgrades, a new feature will activate if a certain threshold (e.g. 80%) of votes consistently request its adoption over a given time interval (e.g. a couple weeks).

Until then, we will publicly announce the availability of new software, with the promise that each release will bring highly-desired features to make upgrading worth the users' whiles.

### Can miners take down Blockstack?

(coming soon)

### How many public Blockstack nodes are there?

(coming soon)

### Who gets the registration fees for name registrations?

With the current design, names are purchased by paying tribute with Bitcoin mining fees.

### How long has the project been around? What does the current development roadmap look like?

Work on the project started in late 2013. First public commits on the code are from Jan 2014. The first registrar for Blockstack was launched in March 2014 and the project has been growing since then. See this page for the current development roadmap

### Who started the project? Who maintains it?

The project was started by two engineers from Princeton University. Muneeb Ali and Ryan Shea met at the Computer Science department at Princeton, where Muneeb was finishing his PhD and Ryan was running the enterprenurship club. In 2014, frustrated by the walled-gardens and security problems of the current internet they started working on a decentralized internet secured by blockchains. The project is currently maintained by Jude Nelson, Muneeb Ali, Ryan Shea, Larry Salibra, and Guy Lepage. A full list of contributors can be found [here](https://github.com/blockstack/blockstack-core/graphs/contributors) and [here](https://github.com/blockstack/blockstack-portal).

### Where are the current core developers based? What are the requirements for being a core developer?

Most of the core developers work in NYC and Hong Kong. Developers who've contributed to the [core open-source software](https://github.com/blockstack/blockstack-core) over a long enough time period, by default, get included in the list of core developers. There is no formal process for being part of this informal list. Core develoipers, generally, have the ability to write high-quality code, understand distributed systems and applied crypto, and share a vision of building a truly decentralized internet and are dedicated to that cause.

### I heard some companies working on Blockstack have raised venture capital, how does that impact the project?

Blockstack, like Linux, is an open-source project with a GPLv3 license for the core technology. Just like different companies build apps and services on top of Linux and have different individual business models, there are companies who're building apps & services for Blockstack on top of the core open-source technology and these companies have various business models and funding sources respectively. Having more venture-backed companies join the ecosystem for a decentralized internet is a good thing for everyone participating in the ecosystem including users and developers.

### Can Blockstack control my data or ID when I use it?

No. When you're using a Blockstack client you control your data and ID with a private key. This private key never leaves your device and is meant to stay on your laptop/phone. As long as no one gets access to your private key, no one can control your data or ID. When you use Blockstack, by design, your private keys are never sent to any remote servers.

### How long can I own my Blockstack ID?

You own your name for ~2 years. You have to renew every 2 years or it expires, and someone else can claim it.

### Where is my data stored and how do I control who access it?

You control where your data is stored (you could run your own server, or use your own cloud storage - Dropbox, Amazon S3, and keep backups across all). You then use those places as locations pointed to by the URLs in your Blockstack ID's zone file. You can get the zone file with `blockstack lookup` in the CLI  (Check out the install video in our [CLI video tutorial series](https://www.youtube.com/playlist?list=PLXS8JJHIn4nGCU2uW85dHXpkQJ7QA5JkX). *need help on how users control who accesses the data*

### Why should I trust the information, like name ownership or public key mappings, read from Blockstack?

Blockstack records are extremely hard to tamper with. This is because the bindings for name ownership (names on Blockstack are owned by public keys) are announced in a proof-of-work blockchain (Bitcoin) and to change these binding an attacker will need to come up with a blockchain with more proof-of-work than the current Bitcoin blockchain but with a different history. Bitcoin's [current hash rate](https://blockchain.info/charts/hash-rate) makes this task almost impossible for non-state actors.  

### Can anyone register a TLD?

Yes, anyone can register a TLD. If a TLD has not been registered already and you're willing to pay the registration fee for it, you can go ahead and register that TLD. There is no centralized party that can stop you from registering a TLD. 

### Do apps using Blockstack work with a regular browser?

Yes! Apps using Blockstack run in the web browsers you know and love. You will need to download and install Blockstack on your computer to use certain features of apps that use Blockstack. 

### Where can I discover apps using Blockstack?

(coming soon)

### What programming language can I use to build these apps?

To make apps that run in the web browser using Blockstack, you can use JavaScript and any of the same web frameworks or libraries you use today such as React, AngularJs, Vue.js or jQuery. You can use any language you like for native apps as long as you are able to consume a JSON REST API.

### What is the Blockstack Portal?

This is a developer-facing term used for the application users use to create and manage their identities and configure their storage. It also handles authentication requests from apps that allow their users to log in with Blockstack. When a user clicks a Log In with Blockstack button, they are redirected to the Blockstack Portal to approve the request before being logged into the app. The Portal is also where users can go to discover and use apps using Blockstack.

### How can I use the Blockstack CLI?

(coming soon)

### How do I get started using Blockstack to build apps?

(coming soon)

### Do I need to run a full Blockstack node to use Blockstack?

(coming soon)

### What is the capacity per block for registrations using Blockstack?

Initial registrations can be done at an order of hundreds per block and once an identity is registered you can do “unlimited” updates to the data because that is off-chain. We’re also working on a more scalable solution where a very large number of identities can be registered but that’s not live yet and is in the pipeline as a rough benchmark. in summer 2015, Blockstack did 30,000+ identity registrations in a matter of few days live on the blockchain and Blockstack was actually throttling its servers and not taking up more than 100-200 transactions per block. It could’ve easily taken up more transactions without impacting the network.

### What language is the Blockstack software written in?

Python 2 and Node.js

### What incentives are there to run a Blockstack node?

Running a Blockstack node keeps you secure by ensuring that your app gets the right names and public keys.  It's not expensive; it takes as much resources as a Chrome tab.

### How does Blockstack perform against building apps on Heroku or AWS?

(coming soon)

### Can Blockstack apps scale, given that Blockstack uses blockchains which don't scale that well?

Yes.  Blockstack only uses the blockchain for name registration.  Everything else happens off-chain, so apps work just as fast as they do on the Web.

### What if the current companies and developers working on Blockstack disappear, would the network keep running?

Yes, the Blockstack network will keep running. All of Blockstack's code is open-source and anyone can deploy Blockstack nodes or maintain the code. Further, Blockstack nodes don't need to coordinate with each other to function. Any node that a user deploys can function correctly independently.

### What are the business models for companies working on Blockstack?

(coming soon)