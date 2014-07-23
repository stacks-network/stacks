Open Name System Specifications
=============

### Table of Contents
[Overview](#overview)  
[Installation](#installation)  
[User Schema](#schema)  
[User Schema RFC](#schema-rfc)  
[Identity Verification](#verification)  
[Usernames](#usernames)  
[Profile Explorers](#explorers)  
[Registering Users](#registration)  
[Domains](#domains)  
[Key-Value Stores](#kvstores)  

<a name="overview"/>
## Overview

### The Open Name System

The Open Name System (ONS) is a protocol that extends DNS by supporting the registration and resolution of:

1. user handles on the blockchain (deployed)
1. domains on the blockchain (design phase)

#### ONS = ICANN DNS + blockchain handles + blockchain domains

ONS is 100% backwards compatible with ICANN DNS and simply extends the functionality.

### ONS Specifications

This repository includes the specifications, standards, and schema for the Open Name System.

### Getting Started

Here are a few ways to get started:

+ <a href="https://opennamesystem.org">Read the overview</a>
+ <a href="https://github.com/opennamesystem/openspecs">Download and fork opendig</a>  (the ONS equivalent of dig)
+ <a href="/openspecs/userschema_rfc.py">Explore and comment on the RFC specifications in this repo</a>
+ [Install openspecs](#installation) and try testing sample profiles against the JSON schema.
+ <a href="/scripts/profile_builder.py">Try out the profile builder</a> (for profiles linked to blockchain user handles)

<a name="installation"/>
## Installation

    >>> pip install openspecs

<a name="schema"/>
## User Schema (v0.2)

On ONS, users may register a username and then have that name resolve to a description of their identity as a user on the web. This schema is a standardization of user descriptions.

### Notes

This schema specifies a way to publicly describe a user. All data involved in this description is public, and all fields are optional. If there are any fields that you would prefer to keep private (your email address, for example), then it is advised that you do not include that information in your profile. Further, at some point the specifications may support other measures to enable the inclusion of private data, for example by using URI's leading to encrypted data containers.

[View the full JSON schema](/openspecs/userschema/schema.py).

### Fields

+ name
+ location
+ bio
+ website
+ bitcoin
+ avatar
+ cover
+ github
+ twitter
+ pgp
+ orgs
+ v

### Example
<pre><code>{
    "name": {
        "formatted": "Naval Ravikant"
    },
    "location": {
        "formatted": "San Francisco, CA"
    },
    "bio": "Co-founder AngelList \\u2022 Founder Epinions, Vast \\u2022 Author Startupboy, Venture Hacks \\u2022 Investor Twitter, Uber, Yammer, Postmates",
    "website": "https://angel.co/naval",
    "bitcoin": {
        "address": "1919UrhYyhs471ps8CFcJ3DRpWSda8qtSk"
    },
    "cover": {
        "url": "https://pbs.twimg.com/profile_banners/745273/1355705777/web_retina"
    },
    "avatar": {
        "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg"
    },
    "twitter": {
        "username": "naval"
    },
    "v": "0.2"
}</code></pre>

<a name="schema-rfc"/>
## User Schema RFC (v0.3)

The ONS User Schema v0.2 is planned to be phased out and v0.3 will gradually take its place. Here we present a request for comments for the new v0.3 schema.

[View the full JSON schema](/openspecs/userschema_rfc.py).

### Sections

#### Basics

A user's basic information, including their name, location and bio.

#### Photos

A user's photos, including their avatar and cover photo.

#### Payments

A user's payment details for various payment methods, including Bitcoin and other cryptocurrencies. A user may provide proof of ownership by signing a message stating their blockchain handle and including it in their profile.

#### Profiles

A user's social network profiles. A user can provide the appropriate usernames or urls, as well as provide proof of ownership of their accounts by referencing posts that only they could have produced (tweets, gists, etc.).

#### Websites

A list of a user's websites. A user can establish proof of ownership outside of this schema by placing a file in their website's directory (potentially either the root directory or .well-known directory) that references them as an owner or team member of the organization that runs the site.

#### PGP

A user's PGP key. A user may provide proof of ownership by signing a message stating their blockchain handle and including it in their profile.

#### Email

A user's email addresses.

### Example
<pre><code>{
    "basics": {
        "bio": "Co-founder AngelList \\u2022 Founder Epinions, Vast \\u2022 Author Startupboy, Venture Hacks \\u2022 Investor Twitter, Uber, Yammer, Postmates", 
        "name": "Naval Ravikant", 
        "location": "San Francisco, CA"
    },
    "payments": [{
        "type": "bitcoin", "address": "1919UrhYyhs471ps8CFcJ3DRpWSda8qtSk"
    }],
    "profiles": [{
        "username": "naval", "type": "twitter"
    }],
    "photos": [{
        "type": "avatar",
        "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg"
    }, {
        "type": "cover",
        "url": "https://pbs.twimg.com/profile_banners/745273/1355705777/web_retina"
    }],
    "websites": [{
        "url": "https://angel.co/naval"
    }],
    "v": "0.3"
}</code></pre>

<a name="verification"/>
## Identity Verification

Users may verify their identities by providing links to and from accounts on social networks and other services.

### Linking an account on a social network or other service

For a profile to be verified by a given account, the profile must reference that account in it's data and the account must also have a post that references the profile. This shows that the owners of each account are in fact the same person.

For example, to prove that you own both your ONS profile and your twitter account, you would tweet out a reference to your ONS profile and then include the URL to that tweet in your ONS profile data.

#### Steps required

1. Create a post (tweet, gist, facebook post, etc.) with a message that explicitly states that you are the owner of your ONS username.
2. Reference the post in your profile data, providing either the post's URL or an identifier that is globally unique on that network.

#### Message format

All of the following are valid formats of identity verification messages:

    Verifying myself: My open username is +someuser
    Verifying myself: My Bitcoin username is +someuser
    Verifying myself: My blockchain handle is +someuser

*Messages are not case sensitive.*

<a name="usernames"/>
## Usernames

Usernames may be up to 60 characters long and contain lowercase letters, numbers, and underscores.

**Note:** usernames with ANY uppercase letters will be ignored by crawlers, so make sure to only use lowercase letters when you register a name.

Regex: ^[a-z0-9_]{1,60}$

<a name="explorers"/>
## Profile Explorers

Profile explorers are systems that read user data from the key-value store and provide an interface for viewing profiles. This is similar to how Bitcoin has block explorers that read data from the blockchain and provide an interface for viewing transaction data. As with bitcoin block explorers, developers are free to crawl the key-value store and set up their own profile explorers.

<a name="registration"/>
## Registering Users

To register a user:

1. choose an available username
2. construct a valid JSON object that adheres to the user schema specifications
3. register the username and profile as an entry in the key-value store

<a name="domains"/>
## Domains

#### Coming soon

As of yet, no work has been done on adding support for blockchain domains to ONS and the ONS command line tools. There have been a few interesting efforts within this vein, most notably the standards drafted up for namecoin's `d/` namespace. At some point it will be interesting to include support for blockchain domains, but we feel it is best for now to focus on providing specifications and tools for extending ICANN DNS to support users and user handles registered in an open way on the blockchain.

<a name="kvstores"/>
## Key-Value Stores

Users may be registered on any decentralized key-value store (DKVS). In this sense, the DKVS chosen is an implementation detail.

However, it is important to note that uniqueness and ownership of usernames is only enforced within a particular DKVS (or within a particular namespace on a particular DKVS if the DKVS has multiple namespaces).

We know that there are multiple IRC networks, but for getting usernames, the only one that matters is the one that everyone uses.

In the same way, the only user handle namespace that matters is the one that everyone uses. Right now that is the user namespace on the namecoin blockchain.

To learn how users are registered on the namecoin blockchain, you can [read more here](/NAMECOIN.md).
