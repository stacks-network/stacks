OneName
=======

The decentralized identity system built on Bitcoin.

##### Table of Contents  
[Introduction](#introduction)  
[Viewing Profiles](#viewing-profiles)  
[Registering Users](#registering-users)  
[Usernames](#usernames)  
[Profiles](#profiles)  
[Key-value Entries](#kv-entries)  

<a name="introduction"/>
## Introduction

OneName is a decentralized identity system (DIS) with a user directory comprised of entries in a decentralized key-value store. The OneName protocol can use any decentralized key-value store for storing data. OneName currently uses the Namecoin blockchain as a key-value store, but any blockchain can be used.

Users are added to the OneName directory via an entry into the key-value store, where the *key* is the username and the *value* is the profile data (in JSON format). The OneName protocol provides formatting specs for usernames and profiles and defines conventions for OneName crawlers/explorers (which read the profile data from the key-value store and display it online). There can be many apps built on top of OneName and the protocol provides specs and conventions for application developers. 

Nobody owns or controls OneName and users are in complete control of their data. Just like with Bitcoin a private key gives access to the Bitcoin account, with OneName a private key gives access to the OneName username and data. No one can modify user data without the private key for that specific username. OneName is open source, has a public design, and is for all to take part.

<a name="viewing-profiles"/>
## Viewing Profiles

Profiles may be viewed on any OneName profile explorer. Just like Bitcoin has many block explorers (like blockexplorer.com), developers may crawl the key-value store and set up their own OneName explorers.

A default explorer is hosted on http://onename.io

URL pattern for viewing a profile on onename.io:

    https://www.onename.io/<username>

URL pattern for viewing a profile as raw JSON data on onename.io:

    https://www.onename.io/<username>.json

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

Regex: ^/[a-z0-9_]{1,60}$

### Namespaces in Namecoin

Namecoin's key-value store has several namespaces. By convention, key entries that start with "d/" are interpreted as domain names. Likewise, those that start with "u/" are interpreted as OneName usernames.

To register a username on Namecoin, prepend "u/" to the username and use that as your key in the key-value entry.

Regex: ^u/[a-z0-9_]{1,60}$

Example:

    Username: someuser
    Key: u/someuser

<a name="profiles"/>
## Profiles

User profiles in OneName are collections of attributes that are expressed as JSON objects.

For profiles to be properly read by OneName crawlers and displayed on OneName profile explorers, their fields must adhere to the conventions outlined below.

### Profile Format v0.1

All fields are strings unless otherwise noted.

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
		<td>"John Smith"</td>
	</tr>
	<tr>
		<td>avatar</td>
		<td>A url to an image that serves as the user's avatar.</td>
		<td>"http://example.com/avatar.jpg"</td>
	</tr>
	<tr>
		<td>cover</td>
		<td>A url to an image that serves as the user's cover photo.</td>
		<td>"http://example.com/cover.jpg"</td>
	</tr>
	<tr>
		<td>location</td>
		<td>The user's current location.</td>
		<td>"New York, NY"</td>
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
		<td>"1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T"</td>
		</td>
	</tr>
	<tr>
		<td>[name of service or social network]</td>
		<td>A unique identifier of the user on the given social network. By default, crawlers will read this field as a username, unless the string is deciphered as a URL.</td>
		<td>
		 <div>1. "sometwitterhandle"</div>
		 <div>2. "http://www.linkedin.com/in/someuser"</div>
		</td>
	</tr>
</tbody>
</table>

#### Sample profile

<pre><code>{
"name": "John Smith",
"avatar": "http://example.com/avatar.jpg",
"cover": "http://example.com/cover.jpg",
"location": "New York, NY",
"website": "http://example.com",
"bio": "Just a guy with his head in the cloud.",
"github": "someuser",,
"facebook": "someuser",
"twitter": "someuser",
"linkedin": "http://www.linkedin.com/in/someuser",
"bitcoin": "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T",
"bitmessage": "BM-orkCbppXWSqPpAxnz6jnfTZ2djb5pJKDb",
"email": "someuser@emailhost.com",
"pgp": {
    "fingerprint": "D34987E8FAD4AE18C8680B4604DE396333BDC0E1",
    "url": "https://s3.amazonaws.com/97p/pubkey.txt"
}
}
</pre></code>

### Profile format v0.2

#### Sample profile

<pre><code>{
    "name": {
        "full": "John Smith"
    },
	"avatar": "http://example.com/avatar.jpg",
	"cover": "http://example.com/cover.jpg",
	"location": "New York, NY",
	"website": "http://example.com",
	"bio": "Just a guy with his head in the cloud.",
	"github": {
    	"username": "someuser"
	},
	"facebook": {
    	"username": "someuser"
	},
	"twitter": {
    	"username": "someuser"
	},
	"linkedin": {
    	"url": "http://www.linkedin.com/in/someuser"
	},
	"bitcoin": {
    	"address": "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T"
	},
	"bitmessage": {
    	"address": "BM-orkCbppXWSqPpAxnz6jnfTZ2djb5pJKDb"
	},
	"email": "someuser@emailhost.com",
	"pgp": {
    	"fingerprint": "D34987E8FAD4AE18C8680B4604DE396333BDC0E1",
    	"url": "https://s3.amazonaws.com/97p/pubkey.txt"
	}
}
</pre></code>

### Services/Sites Currently Supported by Profile Explorers

+ github
+ facebook
+ twitter
+ linkedin
+ instagram
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
+ bitmessage

<a name="kv-entries"/>
## Key-value entries

### Registering username/profile pairs as key-value entries in Namecoin

1. issue a "name new" with the key (the username with "u/" prepended)
2. issue a "name first update" with the chunked profile

### "Name new" operations

Current cost: 0.01 NMC

### "Name first update" operations

Current cost: 0.00 NMC

### Chunking profiles

Key-value entries in Namecoin are limited to a maximum of 519 bytes.

As a result, profiles exceeding 519 bytes must be split into several linked components in order to be embedded in the blockchain.

To chunk a JSON object, simply do the following:

1. check if all the remaining data fits in one chunk
2. if not, choose an unregistered Namecoin key (e.g. "i/username-1" or "i/username-b5sX6gkMp8" - this will be the key of the "next" chunk) and create an empty JSON object (the current chunk), then add a pointer from this chunk to the next one (e.g. "next": "i/username")
4. fill the JSON object with as many properties as possible
5. go back to 1

Note: we recommend not using the "u/" namespace for linked chunks.

#### Example:

The sample profile above could be chunked as follows:

`"u/username"`

<pre><code>{
"name": "John Smith",
"location": "New York, NY",
"website": "http://example.com",
"github": "someuser",
"facebook": "someuser",
"twitter": "someuser",
"linkedin": "http://www.linkedin.com/in/someuser",
"bitcoin": "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T",
"bitmessage": "BM-orkCbppXWSqPpAxnz6jnfTZ2djb5pJKDb",
"email": "someuser@emailhost.com",
"pgp": {
    "fingerprint": "D34987E8FAD4AE18C8680B4604DE396333BDC0E1",
    "url": "https://s3.amazonaws.com/97p/pubkey.txt"
},
"next": "i/username-1"
}
</pre></code>

`"i/username-1"`

<pre><code>{
"avatar": "http://example.com/avatar.jpg",
"cover": "http://example.com/cover.jpg",
"bio": "Just a guy with his head in the cloud.",
}
</pre></code>


