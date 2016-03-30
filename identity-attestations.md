---
title: Identity Attestations
description: Explore about identity attestations on Blockstack.
image: /images/article-photos/persona.jpg
next: light-clients
---

Every identity on blockstack has a profile, which can contains a series of attributes, each of which can be either public or private and either user-attested or authority-attested.

### Public Profiles

Public profiles are constructed through the compilation of public statements, signed by the user that owns the profile.

### Extended Profiles

Extended profiles are public profiles, extended with other information that has not been made publicly accessible.

This information is privately released by the user to selected parties.

When a user authorizes another party to access information, the user encrypts the information with the party's key and hosts it in a publicly-accessible location.

The authorized party is sent the link to the information and is able to decrypt it and extend the public profile with the private information.

The user is free to update the private information, such as an address, and the authorized party will be able to continually grab the updated information and keep everything in sync.

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

### Verified Profiles

User-attested information in profiles can also be attested to by various authorities.

Authorities may be primary sources or secondary sources. If a senior official of your univerity attests to your status at that university, then the university/official is considered a primary source. If your local DMV (Department of Motor Vehicles) attests to your birth date, that is considered a secondary source.

```json
{
  "birthDate": "1973-01-01"
}
```

Signed statements from a variety of authorities can be combined in order to construct a verified profile.