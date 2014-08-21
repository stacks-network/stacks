## User Schema RFC (v0.3)

The ONS User Schema v0.2 is planned to be phased out and v0.3 will gradually take its place. Here we present a request for comments for the new v0.3 schema.

[View the full JSON schema](/openspecs/userschema_rfc/schema.py).


### Sections

#### Basics

A user's basic information, including their location and bio.

#### Names

A list of names associated with a user.

Each name must have one category, and zero or more attributes.

##### Suggested Types for Names

* personal
* business

##### Suggested Attributes for Names

* legal
* nick
* married
* maiden
* stage
* pen

#### URLs

A list of URLs associated with a user, which may include websites, public keys, or another link they may which to associate with their identity. Links to avatar images should not be added to this section as they as handled in their own section.

Each url must have one category, and zero or more attributes.

A user can establish proof of ownership outside of this schema by placing a file in their website's directory (potentially either the root directory or .well-known directory) that references them as an owner or team member of the organization that runs the site.

##### Suggested Types for URLs

* website
* file

##### Suggested Attributes for URLs

* personal
* business
* blog
* wiki
* store
* *public key identifier*

#### Profiles

A list of site-specific username associated with a user on specific websites.

##### Suggested Types for Profiles

* *canonical link to the site (example: https://www.facebook.com)*

##### Suggested Attributes for Profiles

* *optional link to the user's profile page*

#### Images

A list of link to a user's images, including avatars and cover photos. Images can include Gravatar-compatible ratings as attributes.

##### Suggested Types for Images

* avatar
* cover

##### Suggested Attributes for Images

* personal
* business
* G
* PG
* R
* X

#### Mail

A list of asynchronous communication (email-like) addresses associated with a user.

##### Suggested Types for Mail

* email
* bitmessage
* freemail

##### Suggested Attributes for Mail

* personal
* business
* student
* official

#### IM

A list of synchronous communication (instant messaging) addresses associated with a user, including voice/video methods.

##### Suggested Types for IM

* phone
* xmpp
* icq
* aim
* skype

##### Suggested Attributes for IM

* personal
* business
* official
* land
* mobile
* fax

#### Fingerprints

A list of public key fingerprints associated with a user.

##### Suggested Types for Fingerprints

* pgp
* otr
* ssl

##### Suggested Attributes for Fingerints

*none*

#### Payments

A list of the user's payment details for various payment methods, including Bitcoin and other cryptocurrencies.

##### Suggested Types for Payments

* bitcoin
* *any other cryptocyrrency name*

##### Suggested Attributes for Payments

*none*

### Example
<pre><code>{
    "basics": {
        "bio": "Co-founder AngelList \\u2022 Founder Epinions, Vast \\u2022 Author Startupboy, Venture Hacks \\u2022 Investor Twitter, Uber, Yammer, Postmates", 
        "location": "San Francisco, CA"
    },
    "names": [{
        "type": "personal",
        "attributes": [{ "legal" }],
        "name": "Naval Ravikant"
    }],
    "urls": [{
        "type": "website",
        "url": "https://angel.co/naval"
    }],
    "profiles": [{
        "type": "https://twitter.com"
        "username": "naval"
    }],
    "images": [{
        "type": "avatar",
        "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg"
    }, {
        "type": "cover",
        "url": "https://pbs.twimg.com/profile_banners/745273/1355705777/web_retina"
    }],
    "payments": [{
        "type": "bitcoin",
        "address": "1919UrhYyhs471ps8CFcJ3DRpWSda8qtSk"
    }],
    "v": "0.3"
}</code></pre>
