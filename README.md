OneName
=======

The decentralized identity system built on Bitcoin.

##### Table of Contents  
[Introduction](#introduction)  
[Profile Explorers](#profile-explorers)  
[Viewing Profiles](#viewing-profiles)  
[Registering Users](#registering-users)  
[Usernames](#usernames)  
[Profiles](#profiles)  
[Verification](#verification)  
[Key-value Entries](#kv-entries)  

<a name="introduction"/>
## Introduction

OneName is a protocol for a decentralized identity system (DIS) with a user directory comprised of entries in a decentralized key-value store. OneName currently uses the Namecoin blockchain, but any decentralized key-value store may be used.

Users are added to the OneName directory via an entry into the key-value store, where the *key* is the username and the *value* is the profile data (in JSON format).

The OneName protocol provides formatting specifications for usernames and profiles and defines conventions for OneName profile crawlers/explorers (which read from the key-value store, digest profile data, and display profiles).

Nobody owns or controls OneName and users are in complete control of their data.

With Bitcoin, private keys provide us with complete control over our funds - nobody can move it without our permission. In the same way, OneName private keys provide us with complete control over our identities - no individual or entity can usurp our usernames or modify our public data or control the release of our private data without our permission. 

OneName is open source, has a public design, and is for all to take part.

<a name="profile-explorers"/>
## Profile Explorers

OneName profile explorers are systems that read OneName user data from the key-values store and provide an interface for viewing profiles. This is similar to how Bitcoin has block explorers that read data from the blockchain and provide an interface for viewing transaction data. As with bitcoin block explorers, developers are free to crawl the key-value store and set up their own OneName profile explorers.

<a name="viewing-profiles"/>
## Viewing Profiles

Profiles may be viewed on any OneName profile explorer.

### Viewing profiles on a profile explorer

The URL pattern for viewing a profile on a profile explorer:

    someonenameexplorer.com/<username>

The URL pattern for viewing a profile as raw JSON data:

    someonenameexplorer.com/<username>.json

### Current profile explorers

+ [onename.io](https://www.onename.io)

<a name="registering-users"/>
## Registering Users

To register a user on OneName:

1. choose an available OneName username
2. construct a valid JSON object that adheres to the OneName profile specifications
3. register the username and profile as an entry in the key-value store

<a name="usernames"/>
## Usernames

Usernames may be up to 60 characters long and contain lowercase letters, numbers, and underscores.

**Note:** usernames with ANY uppercase letters will be ignored by OneName crawlers, so make sure to only use lowercase letters when you register a name.

Regex: ^[a-z0-9_]{1,60}$

### Usernames on Namecoin

Namecoin's key-value store has several namespaces. By convention, key entries that start with "d/" are interpreted as domain names. Likewise, those that start with "u/" are interpreted as OneName usernames.

When registering a username on Namecoin, prepend "u/" to the username and use that as your key in the key-value entry.

Regex: ^u/[a-z0-9_]{1,60}$

Example:

    Username: someuser
    Key: u/someuser

Full instructions for registering usernames on Namecoin can be found below.

<a name="profiles"/>
## Profiles

User profiles in OneName are collections of attributes that are expressed as JSON objects.

For profiles to be properly read by OneName crawlers and displayed on OneName profile explorers, their fields must adhere to the conventions outlined below.

### Profile Format v0.2

<table class="table table-bordered">
<thead>
    <tr>
        <th>Field Name</th>
        <th>Description</th>
        <th>Example(s)</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>name</td>
        <td>The user's name, including his/her given name and family name.</td>
        <td>{ "formatted": "John Smith" }</td>
    </tr>
    <tr>
        <td>avatar</td>
        <td>A url to an image that serves as the user's avatar.</td>
        <td>{ "url": "http://example.com/avatar.jpg"}</td>
    </tr>
    <tr>
        <td>cover</td>
        <td>A url to an image that serves as the user's cover photo.</td>
        <td>{ "url": "http://example.com/cover.jpg" }</td>
    </tr>
    <tr>
        <td>location</td>
        <td>The user's current location.</td>
        <td>{ "formatted": "New York, NY" }</td>
    </tr>
    <tr>
        <td>website</td>
        <td>The user's website or blog.</td>
        <td>"http://example.com"</td>
    </tr>
    <tr>
        <td>bio</td>
        <td>The user's biography/self-summary.</td>
        <td>"Just a guy with his head in the cloud."</td>
    </tr>
    <tr>
        <td>bitcoin</td>
        <td>The user's bitcoin address.</td>
        <td>{ "address": "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T", "signature": "Gyk26Le4ER0...", "message": "This is a signed message." }</td>
    </tr>
    <tr>
        <td>pgp</td>
        <td>The user's PGP key and fingerprint.</td>
        <td>{ "fingerprint": "D34987E8FAD4AE18C8680B4604DE396333BDC0E1", "url": "https://s3.amazonaws.com/97p/pubkey.txt" }</td>
    </tr>
    <tr>
        <td>twitter</td>
        <td>The user's twitter account.</td>
        <td>{ "username": "someuser", "proof": { "url": "https://twitter.com/someuser/status/958360498327054801", "id": "958360498327054801" } }</td>
    </tr>
    <tr>
        <td>github</td>
        <td>The user's github account.</td>
        <td>{ "username": "someuser", "proof": { "url": "https://gist.github.com/someuser/e8dd382ccf7c19c2e041", "id": "afa72b13d6cd53dc61f5" } }</td>
    </tr>
    <tr>
        <td>facebook</td>
        <td>The user's facebook account.</td>
        <td>{ "username": "someuser", "proof": { "url": "https://www.facebook.com/someuser/posts/10152292145311923", "id": "10152292145311923" } }</td>
    </tr>
    <tr>
        <td>linkedin</td>
        <td>The user's linkedin account.</td>
        <td>{ "url": "http://www.linkedin.com/in/someuser" }</td>
    </tr>
    <tr>
        <td>bitmessage</td>
        <td>The user's message account.</td>
        <td>{ "address": "BM-orkCbppXWSqPpAxnz6jnfTZ2djb5pJKDb" }</td>
    </tr>
    <tr>
        <td>bitcointalk</td>
        <td>The user's account on bitcointalk.org (Bitcoin Forum).</td>
        <td>{ "url": "https://bitcointalk.org/index.php?action=profile;u=000000" }</td>
    </tr>
    <tr>
        <td>bitcoinotc</td>
        <td>The user's account on #bitcoin-otc.</td>
        <td>{ "username": "someuser" }</td>
    </tr>
    <tr>
        <td>[name of service or social network]</td>
        <td>The user's account on a given service or social network.</td>
        <td>{ "username": "someuser" }</td>
    </tr>
    <tr>
        <td>orgs</td>
        <td>A list of organizations the user belongs to.</td>
        <td>[{ "name": "Big Corp", "relationship": "Software Engineer", "url": "http://bigcorp.com" }, { "url": "http://mypersonalblog.com" }, ]</td>
    </tr>
    <tr>
        <td>v</td>
        <td>The version number of the profile data format.</td>
        <td>"0.2"</td>
    </tr>
</tbody>
</table>

#### Sample profile

<pre><code>{
    "name": { "formatted": "John Smith" },
    "avatar": { "url": "http://example.com/avatar.jpg" },
    "cover": { "url": "http://example.com/cover.jpg" },
    "location": { "formatted": "New York, NY" },
    "website": "http://example.com",
    "bio": "Just a guy with his head in the cloud.",
    "github": { "username": "someuser" },
    "facebook": { "username": "someuser" },
    "twitter": { "username": "someuser" },
    "linkedin": { "url": "http://www.linkedin.com/in/someuser" },
    "bitcoin": { "address": "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T" },
    "bitmessage": { "address": "BM-orkCbppXWSqPpAxnz6jnfTZ2djb5pJKDb" },
    "bitcoinotc": { "username": "someuser" },
    "pgp": {
        "fingerprint": "D34987E8FAD4AE18C8680B4604DE396333BDC0E1",
        "url": "https://s3.amazonaws.com/97p/pubkey.txt"
    },
    "orgs": [
        { "name": "Big Corp", "relationship": "Software Engineer", "url": "http://bigcorp.com" },
        { "url": "http://mypersonalblog.com" }
    ],
    "v": "0.2"
}</code></pre>

<a name="verification"/>
## Verification

OneName users may verify their identities by

1. Providing links to and from accounts on social networks and other services.
2. Providing links to and from websites/organizations.

### Linking an account on a social network or other service

For a OneName profile to be verified by a given account, the profile must reference that account in it's data and the account must also have a post that references the profile. This shows that the owners of each account are in fact the same person.

For example, to prove that you own both your OneName profile and your twitter account, you would tweet out a reference to your OneName profile and then include the URL to that tweet in your OneName profile data.

#### Steps required

1. Create a post (tweet, gist, facebook post, etc.) with a message that explicitly states that you are the owner of your OneName username.
2. Reference the post in your profile data, providing either the post's URL or an identifier that is globally unique on that website.

#### Message format

Messages must contain `#verifymyonename` and `+<username>`. Neither of these are case sensitive.

#### Sample posts:

1. `#verifymyonename +someuser`
2. `I am +someuser on OneName #verifymyonename`
3. `I am +someuser on OneName #VerifyMyOneName`

### Linking a website/organization

For a OneName profile to be verified by a given website/organization, the profile must reference that site in it's data and the site must also include the profile in the list of users that it vouches for. This shows that the owner of the website/organization professes that the OneName user is indeed a part of the organization.

#### Steps required

1. Create a JSON file called onename.json and place it in the root directory of your website. List all the users that you would like to have that domain vouch for.
2. Make sure all of the users reference the site in the "orgs" section of their profile data.

#### onename.json file format

<pre><code>{
    "users": [
        { "username": "user1" },
        { "username": "user2" },
        { "username": "user3" }
    ]
}</code></pre>

This file is the equivalent of the domain vouching for the users listed.

#### Notes

1. Using the root directory is necessary to prevent false ownership on websites that allow users to upload files to their servers. It also provides a standard location for OneName crawlers to look.
2. Any proof you provide must be publicly and perpetually available. If you ever delete a post that provides proof of ownership of your OneName profile, that account will lose it's verified status.
3. Verification is a two-way process. That is, in order to be verified by a particular domain or account on a social network, two things must happen: (1) the account/site must reference/vouch for your OneName account (2) your OneName account must reference the account/site.

### Services/Sites Currently Supported by Profile Explorers

+ github
+ facebook
+ twitter
+ linkedin
+ instagram
+ bitmessage
+ bitcointalk
+ bitcoinotc
+ dribbble
+ foursquare
+ pinterest
+ behance
+ skype
+ stackoverflow
+ stackexchange
+ googleplus
+ flickr
+ email

<a name="kv-entries"/>
## Key-value entries

### Registering username/profile pairs as key-value entries in Namecoin

You'll need either a desktop Namecoin client [(Namecoin-Qt)](http://namecoin.info/?p=download) or a UNIX Namecoin daemon. Instructions for building namecoind from source are [here](build-debian.md). Once you have a running version of either Namecoin-Qt or namecoind you will need to buy some namecoins (from exchanges like [Kraken](http://kraken.com) or [BTC-e](http://btc-e.com)) and send them to yourself. Now you're ready to register new names:

1. issue a "name new" with the key (the username with "u/" prepended)
2. issue a "name first update" with the chunked profile

### "Name new" operations

The "name new" operation is the first operation required to register a key-value pair on Namecoin (and by extension, a username/profile pair in accordance with the OneName protocol). This is the operation that communicates intent to register and use a given name. Without "name first update," however, the name registration is not complete.

Current cost: 0.01 NMC

### "Name first update" operations

After the "name new" operation is complete, the "name first update" operation completes the name registration.

Current cost: 0.00 NMC

### Chunking profiles

Key-value entries in Namecoin are limited to a maximum of 519 bytes.

As a result, profiles exceeding 519 bytes must be split into several linked components in order to be embedded in the blockchain.

To chunk a JSON object, simply do the following:

1. check if all the remaining data fits in one chunk
2. if not, choose an unregistered Namecoin key (e.g. "i/username-1" - this will be the key of the "next" chunk) and create an empty JSON object (the current chunk), then add a pointer from this chunk to the next one (e.g. "next": "i/username-1")
4. fill the JSON object with as many properties as possible
5. go back to 1

Note: we recommend not using the "u/" namespace for linked chunks.

#### Example:

The sample profile above could be chunked as follows:

`"u/username"`

<pre><code>{
    "next": "i/username-1"
    "name": { "formatted": "John Smith" },
    "location": { "formatted": "New York, NY" },
    "website": "http://example.com",
    "github": { "username": "someuser" },
    "facebook": { "username": "someuser" },
    "twitter": { "username": "someuser" },
    "bitcoin": { "address": "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T" },
    "bitmessage": { "address": "BM-orkCbppXWSqPpAxnz6jnfTZ2djb5pJKDb" },
    "pgp": {
        "fingerprint": "D34987E8FAD4AE18C8680B4604DE396333BDC0E1",
        "url": "https://s3.amazonaws.com/97p/pubkey.txt"
    },
    "v": "0.2",
}
</pre></code>

`"i/username-1"`

<pre><code>{
    "avatar": { "url": "http://example.com/avatar.jpg" },
    "cover": { "url": "http://example.com/cover.jpg" },
    "bio": "Just a guy with his head in the cloud.",
    "linkedin": { "url": "http://www.linkedin.com/in/someuser" },
    "bitcoinotc": { "username": "someuser" },
    "orgs": [
        { "name": "Big Corp", "relationship": "Software Engineer", "url": "http://bigcorp.com" },
        { "url": "http://mypersonalblog.com" }
    ]
}
</pre></code>
