---
title: Blockstack Profiles
description: Explore about identity attestations on Blockstack.
image: /images/article-photos/persona.jpg
next: identity-attestation
---

When you set up a blockstack identity, you can associate as much or as little information with it as you want. This is referred to as your profile. More information means people can find you more easily and trust that you are who you say you are. Less information means being able to retain more privacy.

Further, every identity on blockstack contains a series of attributes, each of which can be either public or private and either user-attested or authority-attested.

### Public Profiles

Public profiles are constructed through the compilation of public statements, signed by the user that owns the profile.

Here's an example of a blockstack profile:

![Naval's Profile](/images/article-diagrams/naval-card.png)

Here, Naval chose to publicly display his name, bio, and accounts across various social networks.

### Extended Profiles

Extended profiles are public profiles, extended with other information that has not been made publicly accessible.

This information is privately released by the user to selected parties.

When a user authorizes another party to access information, the user encrypts the information with the party's key and hosts it in a publicly-accessible location.

The authorized party is sent the link to the information and is able to decrypt it and extend the public profile with the private information.

The user is free to update the private information, such as an address, and the authorized party will be able to continually grab the updated information and keep everything in sync.

Here's an example of some address information that might be seen in an extended profile, but not publicly accessible:

```json
{
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "16 Maiden Ln",
    "addressLocality": "San Francisco, CA",
    "postalCode": "94108",
    "addressCountry": "United States"
  }
}
```

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
      "service": "facebook",
      "identifier": "navalr",
      "proofType": "http",
      "proofUrl": "https://facebook.com/navalr/posts/10152190734077261"
    },
    {
      "@type": "Account",
      "service": "twitter",
      "identifier": "naval",
      "proofType": "http",
      "proofUrl": "https://twitter.com/naval/status/486609266212499456"
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

Continue to the next article to learn about verified profiles and identity attestations.