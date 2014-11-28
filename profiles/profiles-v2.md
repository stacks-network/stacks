# Profile Schema v2

### Fields

|Name      |Type    |Properties         |Description                           |
|----------|--------|-------------------|--------------------------------------|
|name      |object  |"formatted"        |the user's name                       |
|bio       |string  |                   |a short summary of the user           |
|location  |object  |"formatted"        |the user's location                   |
|website   |string  |                   |the user's website                    |
|bitcoin   |object  |"address"          |the user's bitcoin payment details    |
|avatar    |object  |"url"              |a photo that represents the user's appearance|
|cover     |object  |"url"              |a background photo that adds a personal touch|
|pgp       |object  |"url","fingerprint"|the user's pgp public key information |
|email     |string  |                   |the user's email address              |
|twitter   |object  |"username","proof" |the user's twitter account info       |
|facebook  |object  |"username","proof" |the user's facebook account info      |
|github    |object  |"username","proof" |the user's github account info        |
|v         |string  |                   |the version number of the specs being used |

### Identity Verification Proofs

Each social media account that a user specifies must include both a username and a verification proof.

The data is structured like so:

<pre>"twitter": {
  "username": "fredwilson", 
  "proof": {
    "url": "https://twitter.com/fredwilson/status/533040726146162689"
  }
}</pre>

Note that in the case of this twitter proof, the proof object includes a url to a tweet that only the user could have produced

In that tweet is a verification message that shows the user publicly proclaiming ownership of their openname username.

From this, we can conclude that the person in possession of the twitter account is in fact the same person as the person in possession of the openname username.

#### Verification Proof Messages

<pre>Verifying that +fredwilson is my openname</pre>

### Examples

#### +satoshi

<pre>{
  "name": {
    "formatted": "Satoshi Nakamoto"
  },
  "bio": "Creator of Bitcoin",
  "location": {
    "formatted": "Somewhere on planet Earth"
  },
  "website": "https://bitcoin.org",
  "bitcoin": {
    "address": "1HLoD9E4SDFFPDiYfNYnkBLQ85Y51J3Zb1"
  }, 
  "avatar": {
    "url": "https://s3.amazonaws.com/97p/satoshi"
  },
  "cover": {
    "url": "https://s3.amazonaws.com/dx3/fredwilson"
  },
  "pgp": {
    "fingerprint": "DE4E FCA3 E1AB 9E41 CE96 CECB 18C0 9E86 5EC9 48A1",
    "url": "https://pgp.mit.edu/pks/lookup?op=vindex&search=0x18C09E865EC948A1"
  },
  "twitter": {
    "username": "satoshinakamoto", 
    "proof": {
      "url": "https://twitter.com/satoshinakamoto/status/0123456789"
    }
  },
  "facebook": {
    "username": "satoshinakamoto", 
    "proof": {
      "url": "https://facebook.com/satoshinakamoto/posts/0123456789"
    }
  },
  "github": {
    "username": "satoshinakamoto", 
    "proof": {
      "url": "https://gist.github.com/satoshinakamoto/0123456789"
    }
  },
  "v": "0.2"
}</pre>

#### +fredwilson

<pre>{
  "name": {
    "formatted": "Fred Wilson"
  },
  "bio": "I am a VC",
  "location": {
    "formatted": "New York City"
  }, 
  "website": "http://avc.com",
  "bitcoin": {
    "address": "1Fbi3WDPEK6FxKppCXReCPFTgr9KhWhNB7"
  },
  "avatar": {
    "url": "https://s3.amazonaws.com/kd4/fredwilson1"
  },
  "cover": {
    "url": "https://s3.amazonaws.com/dx3/fredwilson"
  },
  "twitter": {
    "username": "fredwilson", 
    "proof": {
      "url": "https://twitter.com/fredwilson/status/533040726146162689"
    }
  },
  "facebook": {
    "username": "fred.wilson.963871", 
    "proof": {
      "url": "https://facebook.com/fred.wilson.963871/posts/10100401430876108"
    }
  },
  "v": "0.2"
}</pre>
