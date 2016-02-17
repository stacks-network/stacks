---
title: Basic Usage
nextUrl: /docs/extended-usage
nextLabel: Advanced Usage
nextDescription: Dig deeper with Blockstack usage. Learn how to create new namespaces and more.
---

# Basic Usage

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
$ blockstack register $(whoami)_$RANDOM.id
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