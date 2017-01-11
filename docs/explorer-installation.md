---
title: Explorer - Installation
description: Get started by installing the Blockstack Browser.
image: /images/article-photos/computer.jpg
---

### Installation

Developers can run a copy of the Blockstack name explorer.

Note that installation requires Ubunto 16.04.1 LTS and a user with root privileges.

To install the explorer, one must first set up a name explorer API and then set up a bitcore node, configured with the explorer frontend and a reference to the name explorer API.

#### Setting Up the Name Explorer API

1. Create and enter an installation directory: `mkdir /data && cd /data`
1. Clone the blockstack explorer repo: `git clone git@github.com:blockstack/blockstack-explorer.git`
1. Install flask and other dependencies: `pip install --upgrade Flask flask-crossdomain`
1. Run the explorer API on port 5000: `./tools/runserver.py`

#### Setting Up Bitcore

1. Make sure apt-get is up to date: `apt-get update && apt-get dist-upgrade -y`
1. Install python: `apt-get install python-pip python-dev libzmq3-dev -y`
1. Get node: `curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -`
1. Install node: `apt-get install -y nodejs`
1. Install the bitcore node creator: `npm install -g bitcore-node`
1. Create a bitcore node: `bitcore-node create /data/blockstack-bitcore`
1. Enter into the folder for the node: `cd /data/blockstack-bitcore/`
1. Install the insight API: `./node_modules/.bin/bitcore-node install insight-api`

#### Set Up the Frontend

The easiest way to set up the frontend is to install it as a node package: `./node_modules/.bin/bitcore-node install git+https://github.com/blockstack/blockstack-explorer.git#master`

If you want to develop on the explorer, though, you can install the frontend in a separate folder:

1. Remove the insight UI: `rm -Rf ./node_modules/insight-ui`
1. Link to the new insight UI: `ln -s /data/blockstack-explorer ./node_modules/insight-ui`

#### Linking the Name Explorer API

1. Open the index.html file: `nano public/index.html`
1. Update the script that includes `blockstackApiPrefix` to the following: `<script language="javascript">window.blockstackApiPrefix = 'http://localhost:5000';</script>`

#### Starting Bitcore

1. Start bitcore: `./node_modules/.bin/bitcore-node start`
1. Wait many hours (approximately a day) for the bitcore node to index the blockchain
