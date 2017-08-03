---
title: Command Line - Installation
description: Get started by installing and configuring Blockstack.
image: /images/article-photos/computer.jpg
next: cli-basic-usage
---

### Installation

The quickest way to experience the power of Blockstack first hand is to install the command line interface and play around with looking up names and registering names.

Below you'll find the installation instructions for both OS X and Linux (Debian and Ubuntu).

#### OS X Users

Installation on OS X requires `pip`. If you're running OS X, you should already have `pip` installed (it comes with Python), but if not make sure to install it using the following command:

```bash
$ brew install python
```

Next, use `pip2` (or `pip`) to install blockstack:

```bash
$ sudo pip2 install blockstack   # some systems use `pip` only; make sure it's the Python 2.x pip
```

#### Debian + Ubuntu Users

Installation on Debian + Ubuntu requires `pip` and `libssl`. First, make sure you have both:

```bash
$ sudo apt-get update && sudo apt-get install -y python-pip python-dev libssl-dev libffi-dev rng-tools
```

Next, use `pip2` to install pyparsing and then blockstack:

```bash
$ sudo pip2 install pyparsing
$ sudo pip2 install blockstack
```

#### Windows Subsystem for Linux

Installation requires `pip` and `libssl`. First, make sure you have both:

```bash
$ sudo apt-get update && sudo apt-get install -y python-pip python-dev libssl-dev libffi-dev
```

Next, use `pip` to install functools32 and pyparsing modules, and then blockstack:

```bash
$ sudo pip install functools32 pyparsing
$ sudo pip install blockstack
```
