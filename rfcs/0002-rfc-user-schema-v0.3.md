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

The site-specific username associated with a user on specific websites.

##### Suggested Types for Profiles

* *canonical link to the site (example: https://www.facebook.com)*

##### Suggested Attributes for Profiles

* *optional link to the user's profile page*

#### Photos

A user's photos, including their avatar and cover photo.

#### Payments

A user's payment details for various payment methods, including Bitcoin and other cryptocurrencies. A user may provide proof of ownership by signing a message stating their blockchain handle and including it in their profile.

#### PGP

A user's PGP key. A user may provide proof of ownership by signing a message stating their blockchain handle and including it in their profile.

#### Email

A user's email addresses.

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
    "payments": [{
        "type": "bitcoin", "address": "1919UrhYyhs471ps8CFcJ3DRpWSda8qtSk"
    }],
    "photos": [{
        "type": "avatar",
        "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg"
    }, {
        "type": "cover",
        "url": "https://pbs.twimg.com/profile_banners/745273/1355705777/web_retina"
    }],
    "v": "0.3"
}</code></pre>
