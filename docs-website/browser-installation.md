---
title: Browser - Installation
description: Get started by installing the Blockstack Browser.
image: /images/article-photos/computer.jpg
---

### Developer Installation

Developers can install the experimental alpha of the Blockstack Browser and run it locally. Here's how:

1. Clone the repo at https://github.com/blockstack/blockstack-browser.git
1. Make sure you have gulp installed globally by running `npm install gulp -g`
1. Run `npm install` from the root directory
1. Run `gulp proxy` to start the CORS proxy on port 1337
1. In another terminal, run `gulp dev`

Your browser will automatically be opened you'll see the Blockstack dashboard via the browser-sync proxy address. Files are being served from the `/build` directory and any changes to files in the `/app` directory will trigger Gulp to rebundle the assets and reload the browser.

### Production Deployment

The Blockstack Browser can be packaged up and deployed for production distribution. Instructions for this are coming soon.