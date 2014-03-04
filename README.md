OneName
=======

The decentralized identity system built on Bitcoin.

## Introduction

OneName is a decentralized identity system (DIS) with a user directory comprised of entries in a decentralized key-value store. OneName uses the Namecoin blockchain, but is compatible with any decentralized key-value store.

Users are added to the OneName directory via an entry into the key-value store, where the key is the username and the value is the profile.

The OneName protocol provides formatting specs for usernames and profiles and defines conventions for OneName crawlers/explorers (which read the profile data from the key-value store and display it online), as well as apps built on top of the network.

Nobody owns or controls OneName and users are in complete control of their data. OneName is open source, has a public design, and is for all to take part.

## Viewing Profiles

Profiles may be viewed on any OneName profile explorer.

The default explorer is hosted on onename.io, but developers may crawl the key-value store and set up their own explorer at any time.

URL pattern for viewing a profile on onename.io:

    https://www.onename.io/<username>

URL pattern for viewing a profile as raw JSON data on onename.io:

    https://www.onename.io/<username>.json

## Registering Users

To register a user on OneName:

1. choose an available OneName username
2. construct a valid JSON object that adheres to the OneName profile specifications
3. register the username and profile as an entry in the key-value store

## Usernames

Usernames may be up to 60 characters long and contain lowercase letters, numbers, and underscores.

**Note:** usernames with ANY uppercase letters will be ignored by OneName crawlers, so make sure to only use lowercase letters when you register a name.

Regex: ^/[a-z0-9_]{1,60}$

### Usernames in Namecoin

Namecoin's key-value store has several namespaces. Key entries that start with "d/" are interpreted as domain names. Likewise, those that start with "u/" are interpreted as OneName usernames.

To register a username on Namecoin, prepend "u/" to the username and use that as your key in the key-value entry.

Regex: ^u/[a-z0-9_]{1,60}$

Example:

    Username: someuser
    Key: u/someuser

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

### Sample profile

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

## Registering key-value entries in Namecoin

To register a key-value entry with Namecoin

1. issue a name new with the key (the username with "u/" prepended)
2. issue a name first update with the chunked profile

Key-value entries on Namecoin currently cost 0.01 NMC, which on the date of writing (Mar 3, 2014) is approximately 3.5 cents.

### Chunking profiles


