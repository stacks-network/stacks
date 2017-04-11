---
title: Explorer - Installation
description: Get started by installing the Blockstack Browser.
image: /images/article-photos/computer.jpg
---

### Developer Installation

Developers can run a copy of the Blockstack name explorer.

Note that installation requires Ubuntu 16.04.1 LTS and a user with root privileges.

To install the explorer, one must first set up a name explorer API and then set up a bitcore node, configured with the explorer frontend and a reference to the name explorer API.

<p><b>Setting Up the Name Explorer API</b></p>

1. Create and enter an installation directory: `mkdir /data && cd /data`
1. Clone the blockstack explorer repo: `git clone git@github.com:blockstack/blockstack-explorer.git`
1. Install flask and other dependencies: `pip install --upgrade Flask flask-crossdomain`
1. Run the explorer API on port 5000: `./tools/runserver.py`

<p><b>Setting Up Bitcore</p></b>

1. Make sure apt-get is up to date: `apt-get update && apt-get dist-upgrade -y`
1. Install python: `apt-get install python-pip python-dev libzmq3-dev -y`
1. Get node: `curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -`
1. Install node: `apt-get install -y nodejs`
1. Install the bitcore node creator: `npm install -g bitcore-node`
1. Create a bitcore node: `bitcore-node create /data/blockstack-bitcore`
1. Enter into the folder for the node: `cd /data/blockstack-bitcore/`
1. Install the insight API: `./node_modules/.bin/bitcore-node install insight-api`

<p><b>Set Up the Frontend</p></b>

The easiest way to set up the frontend is to install it as a node package: `./node_modules/.bin/bitcore-node install git+https://github.com/blockstack/blockstack-explorer.git#master`

If you want to develop on the explorer, though, you can install the frontend in a separate folder:

1. Remove the insight UI: `rm -Rf ./node_modules/insight-ui`
1. Link to the new insight UI: `ln -s /data/blockstack-explorer ./node_modules/insight-ui`

<p><b>Linking the Name Explorer API</p></b>

1. Open the index.html file: `nano public/index.html`
1. Update the script that includes `blockstackApiPrefix` to the following: `<script language="javascript">window.blockstackApiPrefix = 'http://localhost:5000';</script>`

<p><b>Starting Bitcore</p></b>

1. Start bitcore: `./node_modules/.bin/bitcore-node start`
1. Wait many hours (approximately a day) for the bitcore node to index the blockchain

### Production Deployment

Once you've installed everything and the bitcore node has fully indexed the blockchain, your explorer should be ready for use.

Next, you can update your OS settings to expose the frontend and the API, and then update your DNS settings to point to the IP address where its all running.

Now you have your very own Blockstack Explorer.
