---
title: Basic Usage
description: Explore Blockstack usage, including looking up & registering names.
image: https://images.unsplash.com/photo-1454165205744-3b78555e5572
next: extended-usage
---

### Lookups

Now, to perform a name lookup, run this command:

```bash
$ blockstack lookup fredwilson.id
```

You should get a response like this:

```json
{
  "data": {
    "$origin": "fredwilson.id",
    "$ttl": "3600",
    "cname": [{ "name": "@", "alias": "https://zk9.s3.amazonaws.com" }]
  }
}
```

### Cost Estimations

```bash
$ blockstack fee $(whoami).id
```

Example response:

```json
{
  "fee": 0.01624,
  "registration_fee": 0.016,
  "transaction_fee": 0.00024
}
```

### Registrations

After you get comfortable with looking up names, take the next step and register and manage a name for yourself. Run the following command:

```bash
$ blockstack register <YOUR FULL NAME>.id
```

If the name hasn’t been registered yet, you’ll get a confirmation that your registration is pending:

```json
{
  "message": "Name queued up for registration. Please expect a few hours for this process to be completed.",
  "error": false
}
```

After a few hours, your registration should go through and you’ll be able to update your DNS records for the name.

### Updates

To update the data record associated with a name you own, run the `blockstack update` command:

```bash
$ blockstack update '{ "cname": [{"name": "@", "alias": "https://zk9.s3.amazonaws.com/yeezy.id"}] }'
```

Expected response:

```json
{
  "message": "Data record updated.",
  "error": false
}
```