---
title: Identity Attestation
description: Explore about identity attestations on Blockstack.
image: /images/article-photos/cup.jpg
next: light-clients
date: March 28, 2016
---

Identities on Blockstack can be bare or they can be verified. Verification is done through the combination of both verifiable proofs and third party attestations.

#### Verified Profiles

User-attested information in profiles can also be verified and become trusted information.

This allows users to provide evidence of who they are in other contexts, on the Internet or in real life.

For users to present their information as verified information, they must include a proof along with it.

Proofs can either be references to data on other social networks and software systems or they can be references to signed attestations by trusted authorities or peers.

#### Verifiable Proofs

Here are a few types of verifiable proofs that are supported:

- **social network proofs** - users can show that they are a given user on Twitter, Facebook, or GitHub
- **domain name proofs** - users can show that they own a given domain name or have admin access to the domain of a given organization
- **key proofs** - users can show that they have control over certain PGP keys or ECDSA keys
- **facial recognition proofs** - users can show that they look like a certain person in real life

Here's an example of a social network proof:

```json
{
  "@type": "Account",
  "service": "twitter",
  "identifier": "naval",
  "proofType": "http",
  "proofUrl": "https://twitter.com/naval/status/486609266212499456"
}
```

#### Attestations

- **peer attestations** - users can have multiple peers attest to information and then aggregate the attestations
- **authority attestations** - users can have trusted authorities attest to information and reference the attestations

#### Authority Attestations

Authorities may be primary sources or secondary sources. If a senior official of your univerity attests to your status at that university, then the university/official is considered a primary source. If your local DMV (Department of Motor Vehicles) attests to your birth date, that is considered a secondary source.

Here's an example of a claim made by Naval about himself:

```json
{
  "issuer": {
    "@id": "naval.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "subject": {
    "@id": "naval.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "claim": {
    "name": "Naval Ravikant"
  }, 
  "issuedAt": "2016-03-02T18:59:29.043Z", 
  "expiresAt": "2017-03-02T18:59:29.043Z"
}
```

And here is an example of an attestation made by the DMV of the state of California:

```json
{
  "issuer": {
    "@id": "california-dmv.id",
    "publicKey": "03a59dbfd9612e4088818c90e19afcf8d1793b38a5c040c38d7d07bb7d39d86d72"
  },
  "subject": {
    "@id": "naval.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "claim": {
    "name": "Naval Ravikant"
  }, 
  "issuedAt": "2016-03-10T17:01:32.879Z",
  "expiresAt": "2017-03-10T17:01:32.879Z"
}
```

#### Peer Attestations

Peer attestations can include references to any type of information. However, they are most commonly made about relationships between the peers.

For example, Alice can attest that she knows Bob and Bob can attest that he knows Alice. With this, we can be confident that Alice and Bob know one another.

Here Alice is claiming that the list of people she knows includes Bob:

```json
{
  "issuer": {
    "@id": "alice.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "subject": {
    "@id": "alice.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "claim": {
    "knows": [
      {
        "@type": "Person",
        "@id": "bob.id"
      }
    ]
  }, 
  "issuedAt": "2016-03-02T18:59:29.043Z", 
  "expiresAt": "2017-03-02T18:59:29.043Z"
}
```

Here Bob is claiming that the list of people he knows includes Alice:

```json
{
  "issuer": {
    "@id": "bob.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "subject": {
    "@id": "bob.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "claim": {
    "knows": [
      {
        "@type": "Person",
        "@id": "alice.id"
      }
    ]
  }, 
  "issuedAt": "2016-03-02T18:59:29.043Z", 
  "expiresAt": "2017-03-02T18:59:29.043Z"
}
```

In another example, we can show how an employee-employer relationship would be expressed.

Here Naval is claiming he works for a company called AngelList:

```json
{
  "issuer": {
    "@id": "naval.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "subject": {
    "@id": "naval.id",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "claim": {
    "worksFor": [
      {
        "@type": "Organization",
        "@id": "angellist.corp",
        "name": "AngelList"
      }
    ],
  }, 
  "issuedAt": "2016-03-02T18:59:29.043Z", 
  "expiresAt": "2017-03-02T18:59:29.043Z"
}
```

Here AngelList is claiming that it has an employee known as Naval:

```json
{
  "issuer": {
    "@id": "angellist.corp",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "subject": {
    "@id": "angellist.corp",
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  },
  "claim": {
    "employee": [
      {
        "@type": "Person",
        "@id": "naval.id"
      }
    ]
  }, 
  "issuedAt": "2016-03-02T18:59:29.043Z", 
  "expiresAt": "2017-03-02T18:59:29.043Z"
}
```
