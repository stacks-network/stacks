---
title: Blockstack Profiles - Javascript
description: A Javascript library for creating, signing, and verifying Blockstack profiles
image: /images/article-photos/computer-3.jpg
next: blockstack-profiles-py
---

*Note: this document features the latest version of Javascript (ES6) in its examples, so you may see an unfamiliar syntax for imports and use of the newly supported "let" in place of "var". Don't worry, though, if you're using ES5, an older version of Javascript, as this library is completely compatible with both.*

#### Installation

```bash
$ npm install blockstack-profiles
```

#### Package Importing

```javascript
import { signTokenRecords, getProfileFromTokens, Person } from 'blockstack-profiles'
import { PrivateKeychain, PublicKeychain } from 'elliptic-keychain'
```

#### Defining Keys

```javascript
let privateKeychain = new PrivateKeychain()
let publicKeychain = privateKeychain.publicKeychain()
```

#### Creating Profiles

```javascript
let balloonDog = {
  "@context": "http://schema.org/",
  "@type": "CreativeWork",
  "name": "Balloon Dog",
  "creator": [
    {
      "@type": "Person",
      "@id": "therealjeffkoons.id",
      "name": "Jeff Koons"
    }
  ],
  "dateCreated": "1994-05-09T00:00:00-0400",
  "datePublished": "2015-12-10T14:44:26-0500"
}
let profileComponents = [balloonDog]
```

#### Signing Token Records

```javascript
let tokenRecords = signTokenRecords(profileComponents, privateKeychain)
```

##### Example output:

```json
[
  {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJjbGFpbSI6eyJAY29udGV4dCI6Imh0dHA6Ly9zY2hlbWEub3JnLyIsIkB0eXBlIjoiQ3JlYXRpdmVXb3JrIiwibmFtZSI6IkJhbGxvb24gRG9nIiwiY3JlYXRvciI6W3siQHR5cGUiOiJQZXJzb24iLCJAaWQiOiJ0aGVyZWFsamVmZmtvb25zLmlkIiwibmFtZSI6IkplZmYgS29vbnMifV0sImRhdGVDcmVhdGVkIjoiMTk5NC0wNS0wOVQwMDowMDowMC0wNDAwIiwiZGF0ZVB1Ymxpc2hlZCI6IjIwMTUtMTItMTBUMTQ6NDQ6MjYtMDUwMCJ9LCJzdWJqZWN0Ijp7InB1YmxpY0tleSI6IjAzYTU5ZGJmZDk2MTJlNDA4ODgxOGM5MGUxOWFmY2Y4ZDE3OTNiMzhhNWMwNDBjMzhkN2QwN2JiN2QzOWQ4NmQ3MiJ9LCJpc3N1ZWRBdCI6IjIwMTYtMDMtMTBUMTc6MDE6MzIuODc5WiIsImV4cGlyZXNBdCI6IjIwMTctMDMtMTBUMTc6MDE6MzIuODc5WiJ9.vEUJzl713FApgDNYzbUue5SDOdeElxEaAnMbmT-A6ihfrnzhOd5WvzlGJwTiz1LbeTruhQgbh_XyCJ6aLxfu6A",
    "data": {
      "header": {
        "typ": "JWT",
        "alg": "ES256K"
      },
      "payload": {
        "claim": {
          "@context": "http://schema.org/",
          "@type": "CreativeWork",
          "name": "Balloon Dog",
          "creator": [
            {
              "@type": "Person",
              "@id": "therealjeffkoons.id",
              "name": "Jeff Koons"
            }
          ],
          "dateCreated": "1994-05-09T00:00:00-0400",
          "datePublished": "2015-12-10T14:44:26-0500"
        },
        "subject": {
          "publicKey": "03a59dbfd9612e4088818c90e19afcf8d1793b38a5c040c38d7d07bb7d39d86d72"
        },
        "issuedAt": "2016-03-10T17:01:32.879Z",
        "expiresAt": "2017-03-10T17:01:32.879Z"
      },
      "signature": "vEUJzl713FApgDNYzbUue5SDOdeElxEaAnMbmT-A6ihfrnzhOd5WvzlGJwTiz1LbeTruhQgbh_XyCJ6aLxfu6A"
    },
    "publicKey": "03a59dbfd9612e4088818c90e19afcf8d1793b38a5c040c38d7d07bb7d39d86d72",
    "encrypted": false,
    "parentPublicKey": "03be573c8dbdd74bbc457f530c4f5898f7147f105af57c1aee20127f981697b884",
    "derivationEntropy": "35d0d4e73780d7e47b404a961c9005f415db76ae88c1bcd4bdcd742d68670f26"
  }
]
```

#### Recovering Profiles

```javascript
let validationResults = Person.validate(recoveredProfile)
console.log(validationResults.valid)
```

#### Creating Zone Files

*Coming soon*
