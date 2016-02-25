---
title: Extended Usage
description: Dig deeper with Blockstack usage, including name transfers and more.
image: /images/article-photos/astronaut.jpg
next: blockstack-vs-dns
---

### Transfers

To transfer a name you own to another address, run the `blockstack transfer` command:

```bash
$ blockstack transfer <NAME YOU OWN> <RECIPIENT ADDRESS>
```

Expected response:

```json
{
    "success": true
}
```

### Names You Own

To get a list of the names you own, run the `blockstack names` command:

```bash
$ blockstack names
```

Expected response:

```json
{
    "addresses": [
        {
            "address": "1KBUsvXmSRMUTxp1GhftnbvDeRaEM2D6MX",
            "names_owned": []
        }
    ],
    "names_owned": []
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
            "address": "13aUoeUtQnHUTfRwbksKvyvMRMzN3Qf2iR",
            "balance": 0.05
        }
    ],
    "total_balance": 0.05
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
    "owner_address": "1F2nHEDLRJ39XxAvSxwQhJsaVzvS5RHDRM",
    "owner_public_key": "0411d88aa37a0eea476a5b63ca4b1cd392ded830865824c27dacef6bde9f9bc53fa13a0926533ef4d20397207e212c2086cbe13db5470fd29616abd35326d33090",
    "owner_script": "76a91499e7f97f5d2c77b4f32b4ed9ae0f0385c45aa5c788ac",
    "preorder_transaction_id": "2986ec31ec957692d7f5bc58a3b02d2ac2d1a60039e9163365fc954ff51aeb5a",
    "registered": true
}
```

### Blockstack Server Updates

To update the blockstack server that your command line client is connecting to, use the `blockstack config` command:

```bash
$ blockstack config --server=server.blockstack.org --port=6264 --advanced=off
```

Expected response:

```json
{
    "message": "Updated settings for advanced"
}
```