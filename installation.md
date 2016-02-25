---
title: Installation
description: Get started by installing and configuring Blockstack.
image: /images/article-photos/computer.jpg
next: basic-usage
---

The quickest way to get started with Blockstack and get a glimpse of what it can do is to install the command line interface and start performing name lookups.

Installing the Blockstack command line interface is simple if you already pip installed on your computer (it often comes packaged with python). Just run the following command in your console:

```bash
$ sudo pip install blockstack
```

### OS X Users

If you're running OS X, you should already have an installation of pip and the command shown above should be all you need.

Otherwise, you can install pip along with python using the following command:

```
$ brew install python
```

Then continue with the installation using `sudo pip install blockstack`.

### Debian + Ubuntu Users

If you're on Debian or Ubuntu, you may have to run another command before you perform the installation shown above. To prevent any installation issues, run the following first:

```bash
$ sudo apt-get update && sudo apt-get install -y python-pip python-dev libssl-dev
```

Then continue with the installation using `sudo pip install blockstack`.