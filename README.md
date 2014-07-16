OpenName
=============

## Installation

    >>> pip install onsuserschema

#### Example User JSON
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