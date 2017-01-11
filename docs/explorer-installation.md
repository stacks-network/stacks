---
title: Explorer - Installation
description: Get started by installing the Blockstack Browser.
image: /images/article-photos/computer.jpg
---

### Installation Overview

Developers can run a copy of the Blockstack name explorer on Ubunto 16.04.1 LTS.

To do this, there are a few main phases:

1. Set up a bitcore node with the explorer frontend
1. Set up the blockstack explorer API
1. Point the bitcore node to the blockstack API

### Setting Up Bitcore

1. Make sure you have root privileges
1. Make sure apt-get is up to date: `apt-get update && apt-get dist-upgrade -y`
1. Install python: `apt-get install python-pip python-dev libzmq3-dev -y`
1. Get node: `curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -`
1. Install node: `apt-get install -y nodejs`
1. Create a directory for the installation: `mkdir /data`
1. Install the bitcore node creator: `npm install -g bitcore-node`
1. Create a bitcore node: `bitcore-node create /data/blockstack-bitcore`
1. Enter into the folder for the node: `cd /data/blockstack-bitcore/`
1. Install the insight API: `./node_modules/.bin/bitcore-node install insight-api`
1. Set up the explorer frontend: `./node_modules/.bin/bitcore-node install git+https://github.com/blockstack/blockstack-explorer.git#master`
1. Start bitcore: `./node_modules/.bin/bitcore-node start`
1. Wait many hours (approximately a day) for the bitcore node to index the blockchain

### Running the Blockstack Explorer API

1. Enter the data directory: `cd /data`
1. Clone the blockstack explorer repo: `git clone git@github.com:blockstack/blockstack-explorer.git`
1. Install flask dependencies: `pip install --upgrade Flask flask-crossdomain`
1. Run the explorer API on port 5000: `./tools/runserver.py`

### Connecting the Bitcore Node to the API

1. Enter the bitcore folder: `cd /data/blockstack-bitcore`
1. Stop the bitcore node: `./node_modules/.bin/bitcore-node stop`
1. Remove the existing insight API: `rm -Rf ./node_modules/insight-ui`
1. Link to the new API: `ln -s <path-to-checkout-out-blockstack-explore-repo> ./node_modules/insight-ui`
1. Go to edit `public/index.html`
1. Update the script that includes `blockstackApiPrefix` to the following: `<script language="javascript">window.blockstackApiPrefix = 'http://localhost:5000';</script>`
1. Restart the bitcore node: `./node_modules/.bin/bitcore-node start`