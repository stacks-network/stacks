---
title: Command Line - Basic Usage
description: Explore Blockstack usage, including looking up & registering names.
image: /images/article-photos/programming.jpg
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
    "data_record": {
        "name": "Fred Wilson",
        "bio": "I am a VC",
        "website": "http://avc.com"
        ...
    }
}
```

### Price Estimations

Every name costs a certain amount of money to register, and each namespace has it's own name pricing rules.

As an example, in the `.id` namespace 6-letter alphabetic-only names cost 0.001 bitcoins, but with every additional letter the names get 4x cheaper and with every fewer letter the names get 4x more expensive. In addition, names without vowels and names with numbers and special characters get a special discount.

To determine how much a name will cost to order a name, use the `price` command:

```bash
$ blockstack price <YOUR NAME>.id
```

Example response:

```json
{
    "name_price": 0.064,
    "total_estimated_cost": 0.06416,
    "transaction_fee": 0.00016
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
    "success": true
}
```

After a few hours, your registration should go through and you'll be able to update your DNS records for the name.

### Updates

To update the data record associated with a name you own, run the `blockstack update` command:

```bash
$ blockstack update '{ "cname": [{"name": "@", "alias": "https://zk9.s3.amazonaws.com"}] }'
```

Expected response:

```json
{
    "success": true
}
```
