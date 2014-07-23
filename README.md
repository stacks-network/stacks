Open Name System Specifications
=============

### Table of Contents
[Overview](#overview)  
[Installation](#installation)  
[User Schema](#schema)  
[User Schema RFC](#schema-rfc)  
[Identity Verification](#verification)  

<a name="overview"/>
## Overview

### The Open Name System

The Open Name System (ONS) is a protocol that extends DNS by supporting the registration and resolution of:

1. domains on the blockchain
1. user handles on the blockchain

#### ONS = ICANN DNS + blockchain handles + blockchain domains

ONS is 100% backwards compatible with ICANN DNS and simply extends the functionality.

### ONS Specifications

This repository includes the specifications, standards, and schema for the Open Name System.

All the schemas are in JSON format and the python packages provided allow you to start inspecting and playing around with them. Meanwhile, this README simply contains an overview of the specifications.

### Getting Started

Here are a few ways to get started:

+ <a href="https://opennamesystem.org">Read the overview</a>
+ <a href="https://github.com/opennamesystem/openspecs">Download and fork opendig</a>  (the ONS equivalent of dig)
+ <a href="/openspecs/userschema_rfc.py">Explore and comment on the RFC specifications in this repo</a>

<a name="installation"/>
## Installation

    >>> pip install openspecs

<a name="schema"/>
## User Schema (v0.2)

On ONS, users may register a username and then have that name resolve to a description of their identity as a user on the web. This schema is a standardization of user descriptions.

### Notes

This schema specifies a way to publicly describe a user. All data contained describing a user is public, and all fields are optional. If there are any fields that you would prefer to keep private (your email address, for example), then it is advised that you do not include that information in your profile.

Further, at some point the specifications may support other measures to enable the inclusion of private data, potentially with URI's to encrypted data containers.

[View the full JSON schema](/openspecs/userschema.py).

### Fields

+ name
+ avatar
+ cover
+ location
+ bio
+ github
+ twitter
+ bitcoin
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

A user's payment details, including their bitcoin addresses.

#### Profiles

A user's social network profiles.

#### Websites

A user's websites.

#### PGP

A user's PGP key.

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
    Verifying myself: My Blockchain username is +someuser

*Messages are not case sensitive.*
