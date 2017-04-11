---
title: Command Line - Basic Usage
description: Explore Blockstack usage, including looking up & registering names.
image: /images/article-photos/programming.jpg
next: cli-extended-usage
---

### Lookups

Now, to perform a name lookup, run this command:

```bash
$ blockstack lookup timblee.id
```

You should get a response like this:

```
{
    "profile": {
        "@type": "Person", 
        "account": [
            {
                "@type": "Account", 
                "identifier": "timbl", 
                "proofType": "http", 
                "proofUrl": "https://gist.github.com/timbl/04e8ac7c81cd2dee2f51a5e8c672188d", 
                "service": "github"
            }, 
            {
                "@type": "Account", 
                "identifier": "timberners_lee", 
                "proofType": "http", 
                "proofUrl": "https://twitter.com/timberners_lee/status/740677355950080001", 
                "service": "twitter"
            }
        ], 
        "image": [
            {
                "@type": "ImageObject", 
                "contentUrl": "https://s3.amazonaws.com/97p/lUU.jpeg", 
                "name": "cover"
            }
        ]
    }, 
    "zonefile": "$ORIGIN timblee.id\n$TTL 3600\n_http._tcp URI 10 1 \"https://blockstack.s3.amazonaws.com/timblee.id\"\n"
}
```

### Price Estimations

Every name costs a certain amount of money to register, and each namespace has it's own name pricing rules.

As an example, in the `.id` namespace 6-letter alphabetic-only names cost 0.001 bitcoins, but with every additional letter the names get 4x cheaper and with every fewer letter the names get 4x more expensive. In addition, names without vowels and names with numbers and special characters get a special discount.

To determine how much a name will cost to order a name (including all transaction fees), use the `price` command:

```bash
$ blockstack price <YOUR NAME>.id
```

Example response:

```json
{
    "name_price": {
        "btc": "0.00025", 
        "satoshis": "25000"
    }, 
    "preorder_tx_fee": {
        "btc": "0.00047406", 
        "satoshis": "47406"
    }, 
    "register_tx_fee": {
        "btc": "0.00046184", 
        "satoshis": "46184"
    }, 
    "total_estimated_cost": {
        "btc": "0.00188394", 
        "satoshis": "188394"
    }, 
    "update_tx_fee": {
        "btc": "0.00069804", 
        "satoshis": "69804"
    }
}
```

### Deposits

Name registrations and name management operations cost money, so before you can do these things, you'll need to deposit bitcoins in your account.

*Note that in some cases you'll need to wait for one or more confirmations (about 10-60 minutes) before the Blockstack CLI will register the funds as fully deposited and allow you to proceed with registering names.*

To get the Bitcoin address where you should deposit your bitcoins, run the `deposit` command:

```bash
$ blockstack deposit
```

Example response:

```json
{
    "address": "13aUoeUtQnHUTfRwbksKvyvMRMzN3Qf2iR",
    "message": "Send bitcoins to the address specified."
}
```

### Registrations

After you get comfortable with looking up names, take the next step and register and manage a name for yourself. Run the following command:

```bash
$ blockstack register <YOUR NAME>.id
```

If the name hasn't been registered yet, you'll get a confirmation that your registration is pending:

```json
{
    "success": true,
    "transaction_hash": "f576313b2ff4cc7cb0d25545e1e38e2d0d48a6ef486b7118e5ca0f8e8b98ae45",
    "message": "The name has been queued up for registration and will take a few hours to go through. You can check on the status at any time by running 'blockstack info'."
}
```

After a few hours, your registration should go through and you'll be able to update your DNS records for the name.

### Updates

To update the data record associated with a name you own, run the `blockstack update` command:

```bash
$ cat > new_zone_file.txt <<EOF
\$ORIGIN swiftonsecurity.id
\$TTL 3600
pubkey TXT "pubkey:data:04cabba0b5b9a871dbaa11c044066e281c5feb57243c7d2a452f06a0d708613a46ced59f9f806e601b3353931d1e4a98d7040127f31016311050bedc0d4f1f62ff"
_file IN URI 10 1 "file:///Users/TaylorSwift/.blockstack/storage-disk/mutable/swiftonsecurity.id"
_https._tcp IN URI 10 1 "https://blockstack.s3.amazonaws.com/swiftonsecurity.id"
_http._tcp IN URI 10 1 "http://node.blockstack.org:6264/RPC2#swiftonsecurity.id"
_dht._udp IN URI 10 1 "dht+udp://fc4d9c1481a6349fe99f0e3dd7261d67b23dadc5"
EOF

$ blockstack update swiftonsecurity.id new_zone_file.txt
```

Expected response:

```json
{
    "success": true,
    "transaction_hash": "4e1f292c09ad8e03a5f228b589d9a7dc3699b495862bee3b40f2432ac497b134",
    "message": "The name has been queued up for update and will take ~1 hour to process. You can check on the status at any time by running 'blockstack info'."
}
```
