# Profile Schema v0.3

### Fields

|Name       |Type    |Properties                   |Description                           |
|-----------|--------|-----------------------------|--------------------------------------|
|name       |object  |"formatted"                  |the user's name                       |
|location   |object  |"formatted"                  |the user's location                   |
|summary    |string  |                             |a short summary of the user           |
|websites   |list    |"url"                        |                                      |
|contact    |list    |"type","identifier"          |                                      |
|photos     |list    |"type","url"                 |                                      |
|pubkeys    |list    |"type","fingerprint","url","value"|                                      |
|payments   |list    |"type","identifier"          |                                      |
|profiles   |list    |"type","username","proofUrl" |                                      |
|connections|list    |"type","username"            |                                      |
|statements |list    |"message","signature"        |                                      |
|auth       |object  |"method", "url"              |                                      |
|v          |string  |                             |the version number of the specs being used |

### Identity Verification Proofs

Each social media account that a user specifies must include both a username and a verification proof.

The data is structured like so:

<pre>{
    "type": "twitter",
    "username": "fredwilson",
    "proofUrl": "https://twitter.com/fredwilson/status/533040726146162689"
}</pre>

Note that in the case of this twitter proof, the proof object includes a url to a tweet that only the user could have produced

In that tweet is a verification message that shows the user publicly proclaiming ownership of their openname username.

From this, we can conclude that the person in possession of the twitter account is in fact the same person as the person in possession of the openname username.

#### Verification Proof Messages

<pre>Verifying that +fredwilson is my openname</pre>

### Examples

#### +ryanshea

<pre><code>{
    "name": {
        "formatted": "Ryan Shea"
    },
    "location": {
        "formatted": "New York, NY"
    },
    "summary": "Co-founder of Onename",
    "websites": [
        { "url": "http://shea.io" },
        { "url": "https://onename.io" }
    ],
    "contact": [
        { "type": "skype",
          "identifier": "ryaneshea" },
        { "type": "bitmessage",
          "identifier": "BM-2cSqtKVx27J8FZunKqjcsbfKQAhbgWnLdg" },
        { "type": "xmpp",
          "identifier": "ryan@shea.io" },
        { "type": "email",
          "url": "https://onename.io/ryanshea/email" },
    ],
    "photos": [
        { "type": "headshot",
          "url": "https://s3.amazonaws.com/97p/tux.jpg" },
        { "type": "background",
          "url": "https://s3.amazonaws.com/dx3/ryanshea" }
    ],
    "pubkeys": [
      { "type": "pgp",
        "fingerprint": "DDA1CF3D659064044EC99354429E1A42A93EA312",
        "url": "https://s3.amazonaws.com/97p/pubkey.asc#000000000000000000" },
      { "type": "otr",
        "fingerprint": "756CE84F 90ABDE84 0555F4E2 E0B2ACB1 297F9E65" },
      { "type": "bitcoin",
        "fingerprint": "1FbynFXB1C6jSAQZivucAnzAm9N7GxURYa",
        "value": "083a0518062cc3c5ad48501c60aa06059785449f579a256ed2f1a5e781a109d978e54b20fb43b6e90dc91d8f9898665b969e122df6e1d1e5ce06c790f618a2c4"},
    ],
    "payments": [
        { "type": "bitcoin",
          "identifier": "1EEwLZVZMc2EhMf3LXDARbp4mA3qAwhBxu" },
        { "type": "namecoin",
          "identifier": "N4izoiyX9XKapXqsts7bSN7c3Bcgnr9aeo" },
        { "type": "dogecoin",
          "identifier": "DMHjRxrKN48EQZQDmmoghxZPRRZrvDJeVh" },
        { "type": "quarkcoin",
          "identifier": "" },
        { "type": "bitcoin",
          "subtype": "stealth",
          "identifier": "vJmtrr3cRiWJ9dLqov7nDBZKCGDPP88chGfDRmcQ71jiUE2xMh7GqXe7eGVZcLj7SVQiPJAxXvfdAdyD2RW8re8J7pGanvSUk3k3KW" }
    ],
    "profiles": [
        { "type": "twitter",
          "username": "ryaneshea",
          "proofUrl": "https://twitter.com/ryaneshea/status/486057647808868352" },
        { "type": "facebook",
          "username": "ryaneshea",
          "proofUrl": "https://facebook.com/ryaneshea/posts/10152385985597713" },
        { "type": "github",
          "username": "rxl",
          "proofUrl": "https://gist.github.com/rxl/9799732" },
        { "type": "linkedin",
          "username": "ryaneshea",
          "proofUrl": "https://www.linkedin.com" },
        { "type": "instagram",
          "username": "ryaneshea",
          "proofUrl": "http://instagram.com/ryaneshea" },
        { "type": "reddit",
          "username": "ryaneshea",
          "proofUrl": "http://www.reddit.com/user/ryaneshea/" },
        { "type": "hackernews",
          "username": "rxl",
          "proofUrl": "https://news.ycombinator.com/user?id=rxl" },
        { "type": "stackoverflow",
          "username": "/users/1530754/ryan",
          "proofUrl": "http://stackoverflow.com/users/1530754/ryan" },
        { "type": "angellist",
          "username": "ryanshea",
          "proofUrl": "https://angel.co/ryanshea" },
        { "type": "googleplus",
          "username": "Ryan Shea",
          "proofUrl": "https://plus.google.com/110166845166458482181/posts" }
    ],
    "connections": [
        { "type": "followee", "username": "albertwenger" },
        { "type": "followee", "username": "fredwilson" },
    ],
    "statements": [
        { "message": "I hereby cast my vote for Bitdevs to be held at USV on Tue Dec 16",
          "signature": "HIFDEkiBuJK8MwAJV57L/jLUlTdhwhcIPWCAHJ7Rz58lRTxJfGTKAVxcN6zCtgX4bWlWVEb/qr5oI1AIqVXgUbA=" }
    ],
    "auth": {
        "method": "push",
        "url": "https://onename.io/ryanshea/auth"
    },
    "v": "0.3"
}
</code></pre>

### Sections

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

