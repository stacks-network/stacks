---
title: Usage
nextUrl: /docs/advanced-usage
nextLabel: Advanced Usage
nextDescription: Dig deeper with Blockstack usage. Learn how to create new namespaces and more.
---

# Usage

## Lookups

Now, to perform a name lookup, run this command:

```bash
$ blockstack lookup yeezy.id
```

You should get a response like this:

```json
{
  "data": {
    "$origin": "yeezy.id",
    "$ttl": "3600",
    "txt": [{ "name": "@", "txt": "https://zk9.s3.amazonaws.com/yeezy.id" }]
  }
}
```

## Registrations

After you get comfortable with looking up names, take the next step and register and manage a name for yourself. Run the following command:

```bash
$ blockstack register yeezy.id '{"name": "Yeezy"}'
```

If the name hasn’t been registered yet, you’ll get a confirmation that your registration is pending:

```json
{
  "success": true
}
```

After a few hours, your registration should go through and you’ll be able to update your DNS records for the name.

## Updates

```bash
$ blockstack update '{ "cname": [{"name": "@"}] }'
```

## Transfers

```bash
$ blockstack transfer <name> <recipient>
```

## Renewals

```bash
$ blockstack renew <name>
```
