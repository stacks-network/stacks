---
title: Blockchain IDs
description: Learn about what Blockchain IDs are and what they can be used for.
image: /images/article-photos/passport.jpg
next: identity-attestations
---

A blockchain ID is an identity on the blockchain.

You can have one blockchain ID or many and you can register them just like you would register domain names or accounts on Facebook or Twitter.

The main difference between a blockchain ID and an account on any other service is that you own your blockchain ID completely. It can't be taken away from you by any service at all because the system defines ownership according to ownership of public-private keypairs, just like ownership of coins on Bitcoin. This is in direct contrast to Twitter or Facebook usernames, which could be confiscated or censored at any time by the respective companies that they belong to.

### Names

Blockchain IDs are registered using the blockstack naming system, on the `.id` namespace.

A blockchain ID is a complete user identity, so it includes the name that is registered on the namespace, as well as the profile that the user fills out and associates with the name.

The name for a blockchain ID, like "alice", is unique within the namespace. Meanwhile, the fully-qualified name of the blockchain ID, "alice.id", is globally unique across all of the blockstack naming universe because it includes the global top-level domain "id".

### Profiles

When you set up your blockchain ID, you can associate as much or as little information with it as you want. This is referred to as your profile.

More information means people can find you more easily and trust that you are who you say you are. Less information means being able to retain more privacy.

Here's an example of a blockchain ID profile:

![Naval's Profile](/images/article-diagrams/naval-card.png)

Here, Naval chose to publicly display his name, bio, and accounts across various social networks.

### Identity Proofs

Identity proofs allow the holders of blockchain IDs to provide evidence of who they are in other contexts, on the Internet or in real life.

Here are a few types of proofs that are supported:

- **social network proofs** - users can show that they are a given user on Twitter, Facebook, or GitHub
- **domain name proofs** - users can show that they own a given domain name or have admin access to the domain of a given organization
- **key proofs** - users can show that they have control over certain PGP keys or ECDSA keys
- **facial recognition proofs** - users can show that they look like a certain person in real life

### Profile Data

Profiles are encoded in a format known as JSON, with a specific JSON schema that is derived from schema.org.

Let's return to the example above of Naval's profile, and see what it might look like when it's shown as raw data:

```json
{
  "@context": "http://schema.org/",
  "@type": "Person",
  "givenName": "Naval",
  "familyName": "Ravikant",
  "description": "Co-founder of AngelList",
  "image": [
    {
      "@type": "ImageObject",
      "name": "avatar",
      "contentUrl": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg"
    }
  ],
  "website": [
    {
      "@type": "WebSite",
      "url": "angel.co"
    }
  ],
  "account": [
    {
      "@type": "Account",
      "service": "twitter",
      "identifier": "naval",
      "proofType": "http",
      "proofUrl": "https://twitter.com/naval/status/486609266212499456"
    },
    {
      "@type": "Account",
      "service": "facebook",
      "identifier": "navalr",
      "proofType": "http",
      "proofUrl": "https://facebook.com/navalr/posts/10152190734077261"
    }
  ],
  "worksFor": [
    {
      "@type": "Organization",
      "@id": "angellist.corp"
    }
  ],
  "knows": [
    {
      "@type": "Person",
      "@id": "jack.id"
    },
    {
      "@type": "Person",
      "@id": "travisk.id"
    }
  ]
}
```

Here we can see Naval's name, picture, and bio. We can also see proofs of a website he owns (angel.co), an organization he controls (angellist.corp), and his accounts on Twitter and Facebook. Last, we can see that he knows two users with the usernames "jack.id" and "travisk.id".