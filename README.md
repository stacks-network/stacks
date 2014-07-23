Open Name System Specifications
=============

##### Specifications, standards, and schema for the Open Name System.

### Table of Contents
[Overview](#overview)  
[Installation](#installation)  
[User Schema](#schema)  
[User Schema RFC](#schema-rfc)  
[Identity Verification](#verification)  

<a name="overview"/>
## Overview

The open name system (ONS) is a protocol that extends DNS by:

2. supporting the registration and resolution of domains on the blockchain
1. supporting the registration and resolution of user handles on the blockchain

### ONS = ICANN DNS + blockchain handles + blockchain domains


ONS is 100% backwards compatible with ICANN DNS and simply extends the functionality.

You can read more about ONS <a href="https://opennamesystem.org"> here</a>.

<a name="installation"/>
## Installation

    >>> pip install openspecs

<a name="schema"/>
## User Schema (v0.2)

On ONS, users may register a username and then have that name resolve to a description of their identity as a web user. This schema is a standard for such description/characterization.

### Notes

This standard specifies a way to publicly describe a user. All data on a user is public, and all fields are optional. If there are any fields that you would prefer to keep private (your email address, for example), then it is advised that you do not include that information in your profile.

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
  "bitcoin": {
    "address": "1N9rsxZimC8z8SRfocEh9pAa5RweBa76st"
  }, 
  "avatar": {
    "url": "https://pbs.twimg.com/profile_images/2597394462/32b6p3stu0g09zwy8rq5.jpeg"
  }, 
  "twitter": {
    "proof": {
      "url": "https://twitter.com/barrysilbert/status/486629628618891264"
    }, 
    "username": "barrysilbert"
  }, 
  "v": "0.2", 
  "cover": {
    "url": "https://s3.amazonaws.com/97p/orange-sky.jpg"
  }, 
  "website": "https://www.bitcointrust.co", 
  "name": {
    "formatted": "Barry Silbert"
  }, 
  "location": {
    "formatted": "New York"
  }, 
  "bio": "Founder/CEO @SecondMarket, Founder @BitcoinTrust; investor in Bitcoin companies, entrepreneur advocate", 
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
    "name": "Ryan Shea",
    "location": "New York, NY",
    "bio": "Co-founder of @OneNameio with @Muneeb. Bitcoin, identity, the blockchain, and decentralization."
},
"photos": [
    { "type": "avatar", "url": "https://s3.amazonaws.com/97p/tux.jpg" },
    { "type": "cover", "url": "https://s3.amazonaws.com/dx3/ryanshea" },
],
"payments": [
    { "type": "bitcoin", "address": "14eautXfJT7EZsKfm1eHSAPnHkn3w1XF9R" },
],
"profiles": [
    { "type": "twitter", "username": "ryaneshea", "proof": "https://twitter.com/ryaneshea/status/486057647808868352" },
    { "type": "github", "username": "rxl", "proof": "https://gist.github.com/rxl/9799732" },
],
"websites": [
    { "label": "Blog", "url": "http://shea.io" },
],
"pgp": {
    "url": "https://s3.amazonaws.com/97p/pubkey.asc",
    "fingerprint": "DDA1CF3D659064044EC99354429E1A42A93EA312",
},
"email": [
    { "address": "ryan@shea.io" }
],
"v": "0.3",
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
