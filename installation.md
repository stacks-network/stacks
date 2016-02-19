---
title: Installation
description: Get started by installing and configuring Blockstack.
image: https://images.unsplash.com/photo-1454165205744-3b78555e5572
next: basic-usage
---

# Installation

The quickest way to get started with Blockstack and get a glimpse of what it can do is to download the command line interface and perform a name lookup.

Installing the Blockstack command line interface is simple if you have pip. Just run the following command in your console:

```bash
$ pip install blockstack
```

### Alternative Installations

#### Mac Users

If you're a mac user and would like an alternative to installing through pip, you can also install Blockstack with brew, as seen below.

```bash
$ brew install blockstack
```

#### Linux Users

If you're a linux user and would like an alternative to installing through pip, you can also install via apt-get.

First, though, you'll need to add packages.blockstack.org to your sources list to tell apt-get where to get the blockstack package:

```bash
$ wget -O - http://packages.blockstack.org/jude@onename.com.gpg.key | sudo apt-key add -
$ sudo -- sh -c 'echo "deb http://packages.blockstack.org jessie main" >> /etc/hosts'
```

Now, you may move on to installing blockstack via apt-get:

```
$ sudo apt-get update && sudo apt-get install blockstack
```

After your done installing blockstack, you should be ready to check out the usage section and give it a spin.
