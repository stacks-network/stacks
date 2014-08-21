## User Schema RFC (v0.3)

The ONS User Schema v0.2 is planned to be phased out and v0.3 will gradually take its place. Here we present a request for comments for the new v0.3 schema.

[View the full JSON schema](/openspecs/userschema_rfc/schema.py).

### Format

A user's ONS consists of lists of objects. In order to faciliate the greatest possible uses while retaining forward and backward compatibilty, objects and lists are as generic as possible. Objects may have <pre>types</pre> and <pre>attributes</pre> which explain their purpose.

Applications which parse ONS entries need not understand the semantic meaning of every type and attribute, and should display all data which is correctly specified.

Applications which require additional types or attributes for their functionality should use existing ones to the maximum extent possible, and where it is not possible they should add their new types and attributes to this specification.

#### Global Attributes

There are two global attributes which can be applied to any object, regardless of type:

* primary
* old

The <pre>primary<pre> attribute indicates the default object to be used when more then object of a given type or type/attribute exist. 

The <pre>old</pre> attributes that an object should no longer be used, and is only included in the entry for historical reasons.

### Sections

#### Names

A list of names associated with a user.

Each name must have one category, and zero or more attributes.

##### Suggested Types

* personal
* business

##### Suggested Attributes

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

##### Suggested Types

* website
* file

##### Suggested Attributes

* personal
* business
* blog
* wiki
* store
* *public key identifier*

#### Profiles

A list of site-specific username associated with a user on specific websites.

##### Suggested Types

* *canonical link to the site (example: https://www.facebook.com)*

##### Suggested Attributes

* *optional link to the user's profile page*

#### Images

A list of link to a user's images, including avatars and cover photos. Images can include Gravatar-compatible ratings as attributes.

##### Suggested Types

* avatar
* cover

##### Suggested Attributes

* personal
* business
* G
* PG
* R
* X

#### Mail

A list of asynchronous communication (email-like) addresses associated with a user.

##### Suggested Types

* email
* bitmessage
* freemail

##### Suggested Attributes

* personal
* business
* student
* official

#### IM

A list of synchronous communication (instant messaging) addresses associated with a user, including voice/video methods.

##### Suggested Types

* phone
* xmpp
* icq
* aim
* skype

##### Suggested Attributes

* personal
* business
* official
* land
* mobile
* fax

#### Fingerprints

A list of public key fingerprints associated with a user.

##### Suggested Types

* pgp
* otr
* ssl

##### Suggested Attributes

*none*

#### Payments

A list of the user's payment details for various payment methods, including Bitcoin and other cryptocurrencies.

##### Suggested Types

* bitcoin
* *any other cryptocyrrency name*

##### Suggested Attributes

* personal
* business
* tip
* donation

#### Locations

A list of the user's location details.

##### Suggested Types

* home
* business

##### Suggested Attributes

* country
* region
* locality
* street
* postal code
* permanent
* temporary

#### Text

A list of short text strings which a user can associate with their entry

##### Suggested Types

* bio
* tagline

##### Suggested Attributes

*none*

#### Proofs

This section contains a list of Namecoin identifiers where proof information is stored. Proofs allow for any identity to attest to the validity of any information claimed by any other user.

Users can split their proof information into two types of entries: attestations they've made about other users, and attestations they've received from other users.

##### Suggested Types:

* incoming
* outgoing

##### Suggested Attributes:

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
