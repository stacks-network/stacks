---
title: Command Line - Extended Usage
description: Dig deeper with Blockstack usage, including name transfers and more.
image: /images/article-photos/astronaut.jpg
---

### Transfers

To transfer a name you own to another address, run the `blockstack transfer` command:

```bash
$ blockstack transfer <NAME YOU OWN> <RECIPIENT ADDRESS>
```

Expected response:

```json
{
    "success": true,
    "transaction_hash": "8a68d52d70cf06d819eb72a9a58f4dceda942db792ceb35dd333f43f55fa8713",
    "message": "The name has been queued up for transfer and will take ~1 hour to process. You can check on the status at any time by running 'blockstack info'."
}
```

### Names You Own

To get a list of the names you own, run the `blockstack names` command:

```bash
$ blockstack names
```

Example response:

```json
{
    "addresses": [
        {
            "address": "16EMaNw3pkn3v6f2BgnSSs53zAKH4Q8YJg", 
            "names_owned": [
                "judecn.id"
            ]
        }
    ], 
    "names_owned": [
        "judecn.id"
    ]
}
```

### Bitcoin Balance

To get your Bitcoin balance that can be used for name registrations, run the `blockstack balance` command:


```bash
$ blockstack balance
```

Expected response:

```json
{
    "addresses": [
        {
            "address": "1FWWR679EQ1h3v8RjegcvCDsvWqTVZKxe2", 
            "bitcoin": 0.000959454, 
            "satoshis": 959454
        }
    ], 
    "total_balance": {
        "bitcoin": 0.000959454, 
        "satoshis": 959454
    }
}
```

### Imports

To import a name into your local name wallet or receive it from another sender, use the `blockstack import` command to get an address to have the name sent to:

```bash
$ blockstack import
```

Expected response:

```json
{
    "address": "1KBUsvXmSRMUTxp1GhftnbvDeRaEM2D6MX",
    "message": "Send the name you want to receive to the address specified."
}
```

### Whois Info

To get various info on a given name, including when it was registered and the address it is owned by, run the `blockstack whois` command:

```bash
$ blockstack whois fredwilson.id
```

Example response:

```json
{
    "block_preordered_at": 374084, 
    "block_renewed_at": 374084, 
    "expire_block": 489247, 
    "has_zonefile": true, 
    "last_transaction_height": 374084, 
    "last_transaction_id": "2986ec31ec957692d7f5bc58a3b02d2ac2d1a60039e9163365fc954ff51aeb5a", 
    "owner_address": "1F2nHEDLRJ39XxAvSxwQhJsaVzvS5RHDRM", 
    "owner_script": "76a91499e7f97f5d2c77b4f32b4ed9ae0f0385c45aa5c788ac", 
    "zonefile_hash": "1a587366368aaf8477d5ddcea2557dcbcc67073e"
}
```

### Blockstack Server Updates

To update your settings interactively, use the `blockstack configure` command.  Hit [Enter] to select defaults.

Example trace setting the blockstack server to `127.0.0.1` and the port to `8080`:

```bash
# blockstack configure

Your client does not have enough information to connect
to a Blockstack server.  Please supply the following
parameters, or press [ENTER] to select the default value.

blockchain_headers (default: '/Users/johnsmith/.blockstack/blockchain-headers.dat'): 
blockchain_writer (default: 'blockcypher'): 
api_endpoint_port (default: '6270'): 
poll_interval (default: '300'): 
metadata (default: '/Users/johnsmith/.blockstack/metadata'): 
server (default: 'node.blockstack.org'): 127.0.0.1
blockchain_reader (default: 'blockcypher'): 
email (default: ''): 
storage_drivers_required_write (default: 'disk,blockstack_server'): 
port (default: '6264'): 8080
queue_path (default: '/Users/johnsmith/.blockstack/queues.db'): 
storage_drivers (default: 'disk,blockstack_resolver,blockstack_server,http,dht'): 
client_version (default: '0.14.0'): 
rpc_detach (default: 'True'): 
advanced_mode (default: 'True'): 
anonymous_statistics (default: 'False'): 

Blockstack does not have enough information to connect
to bitcoind.  Please supply the following parameters, or
press [ENTER] to select the default value.

passwd (default: 'blockstacksystem'): 
regtest (default: 'False'): 
server (default: 'bitcoin.blockstack.com'): 
user (default: 'blockstack'): 
timeout (default: '300.0'): 
port (default: '8332'): 

Blockchain reader configuration

Please enter your Blockcypher API token.

api_token (default: ''): 

Blockchain writer configuration

Please enter your Blockcypher API token.

api_token (default: ''): 
Saving configuration to /Users/johnsmith/.blockstack/client.ini
{
    "path": "/Users/johnsmith/.blockstack/client.ini"
}
```
