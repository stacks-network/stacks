# Profile Schema v3

### Sections

#### Basics

A user's basic information, including their name, location and bio.

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

#### Email

A user's email addresses.

### Example
<pre><code>{
    "basics": {
        "bio": "Co-founder AngelList \\u2022 Founder Epinions, Vast \\u2022 Author Startupboy, Venture Hacks \\u2022 Investor Twitter, Uber, Yammer, Postmates", 
        "name": "Naval Ravikant", 
        "location": "San Francisco, CA"
    },
    "payments": [{
        "type": "bitcoin", "address": "1919UrhYyhs471ps8CFcJ3DRpWSda8qtSk"
    }],
    "profiles": [{
        "username": "naval", "type": "twitter"
    }],
    "photos": [{
        "type": "avatar",
        "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg"
    }, {
        "type": "cover",
        "url": "https://pbs.twimg.com/profile_banners/745273/1355705777/web_retina"
    }],
    "websites": [{
        "url": "https://angel.co/naval"
    }],
    "v": "0.3"
}</code></pre>
