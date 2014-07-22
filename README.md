User Schema for the Open Name System
=============

Standard, specification, schema for characterizing a person's online identity on the open name system.

##### Table of Contents
[Introduction](#introduction)  
[Installation](#installation)  
[User Schema](#schema)  
[User Schema RFC](#schema-rfc)  
[Examples](#examples)  

<a name="introduction"/>
## Introduction

The open name system (ONS) is a protocol for registering unique names in a decentralized database (you can find more info about ONS here).

On ONS, users may register a username and then have that name resolve to a description of their identity as a web user.

This schema is a proposed standard for said description/characterization.

### Notes

This standard specifies a way to publicly describe a user. All data on a user is public, and all fields are optional. If there are any fields that you would prefer to keep private (your email address, for example), then it is advised that you do not include that information in your profile.

<a name="installation"/>
## Installation

    >>> pip install onsuserschema

<a name="schema"/>
## User Schema (v0.2)

[View the full JSON schema](https://github.com/opennamesystem/user-schema/blob/master/onsuserschema/schema.py).

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
  "bio": "Co-founder of @OneNameio with @Muneeb. Bitcoin, identity, the blockchain, and decentralization.", 
  "location": {
    "formatted": "New York, NY"
  }, 
  "twitter": {
    "username": "ryaneshea", 
    "proof": {
      "url": "https://twitter.com/ryaneshea/status/486057647808868352"
    }
  }, 
  "avatar": {
    "url": "https://s3.amazonaws.com/97p/tux.jpg"
  }, 
  "cover": {
    "url": "https://s3.amazonaws.com/dx3/ryanshea"
  }, 
  "github": {
    "username": "rxl", 
    "proof": {
      "url": "https://gist.github.com/rxl/9799732"
    }
  }, 
  "website": "http://shea.io", 
  "pgp": {
    "url": "https://s3.amazonaws.com/97p/pubkey.asc", 
    "fingerprint": "DDA1CF3D659064044EC99354429E1A42A93EA312"
  }, 
  "v": "0.2", 
  "name": {
    "formatted": "Ryan Shea"
  }, 
  "bitcoin": {
    "address": "14eautXfJT7EZsKfm1eHSAPnHkn3w1XF9R"
  }
}</code></pre>

<a name="schema-rfc"/>
## User Schema RFC (v0.3)

[View the full JSON schema](https://github.com/opennamesystem/user-schema/blob/master/onsuserschema/schema_rfc.py).

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
