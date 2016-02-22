---
title: Extended Usage
description: Dig deeper with Blockstack usage, including name transfers and more.
image: https://images.unsplash.com/photo-1447433865958-f402f562b843?crop=entropy&dpr=2&fit=crop&fm=jpg&h=1100&ixjsv=2.1.0&ixlib=rb-0.3.5&q=50&w=1500
next: blockstack-vs-dns
---

### Transfers

To transfer a name that you own to another address, run the `blockstack transfer` command:

```bash
$ blockstack transfer <NAME YOU OWN> <RECIPIENT ADDRESS>
```

Expected response:

```json
{
  "message": "Name queued up for transfer.",
  "error": false
}
```

### Renewals

To renew a name that you own, run the `blockstack renew` command:

```bash
$ blockstack renew <NAME YOU OWN>
```

Expected response:

```json
{
  "message": "Name queued up for renewal.",
  "error": false
}
```

### Your Names

To get a list of the names you own, run the `blockstack names` command:

```bash
$ blockstack names
```

Expected response:

```json
{
  "names_owned": [],
  "addresses": [
    { "address": "1Jbcrh9Lkwm73jXyxramFukViEtktwq8gt", "names": [] }
  ]
}
```

### Your Balance

To get your Bitcoin balance that can be used for name registrations, run the `blockstack balance` command:


```bash
$ blockstack balance
```

Expected response:

```json
{
  "balance": 0.05,
  "addresses": [
    { "address": "1EHgqHVpA1tjn6RhaVj8bx6y5NGvBwoMNS", "balance": 0.05 }
  ]
}
```

### Importing

To import a name into your local name wallet or receive it from another sender, get your address with the `blockstack import` command:

```bash
$ blockstack import
```

Expected response:

```json
{
  "address": "1Jbcrh9Lkwm73jXyxramFukViEtktwq8gt"
}
```

### Whois Information

To get various information on a given name, including when it was registered and the address it is owned by, run the `blockstack whois` command:

```bash
$ blockstack whois fredwilson.id
```

Example response:

```json
{
  "block_preordered_at": 374084,
  "block_renewed_at": 374084,
  "owner_address": "1F2nHEDLRJ39XxAvSxwQhJsaVzvS5RHDRM",
  "owner_public_keys": ["0411d88aa37a0eea476a5b63ca4b1cd392ded830865824c27dacef6bde9f9bc53fa13a0926533ef4d20397207e212c2086cbe13db5470fd29616abd35326d33090"],
  "owner_script": "76a91499e7f97f5d2c77b4f32b4ed9ae0f0385c45aa5c788ac",
  "preorder_transaction_id": "2986ec31ec957692d7f5bc58a3b02d2ac2d1a60039e9163365fc954ff51aeb5a",
  "registered": true
}
```

### Blockstack Server Updates

To update the blockstack server that your command line is connecting to, use the `blockstack config` command:

```bash
$ blockstack config --server=server.blockstack.org --port=6264 --advanced=off
```

Expected response:

```json
{
  "message": "Configuration settings updated.",
  "error": false
}
```