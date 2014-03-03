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

## Usernames in Namecoin

Namecoin's key-value store has several namespaces. Key entries that start with "d/" are interpreted as domain names. Likewise, those that start with "u/" are interpreted as OneName usernames.

To register a username on Namecoin, prepend "u/" to the username and use that as your key in the key-value entry.

Regex: ^u/[a-z0-9_]{1,60}$

Example:

    Username: someuser
    Key: u/someuser

## Profiles




