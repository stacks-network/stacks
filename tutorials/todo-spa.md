# Single Page Applications on blockstack

What are we building today?

- A single page javascript application that runs locally
- The app stores data on repurposed cloud storage
- It also allows for sign in with your Blockstack ID

#### Requirements

- Downloaded blockstack and created an identity
- node.js LTS version - v6.11.2
- `yarn`
- `vue.js` 
- A local copy of the [`blockstack-todos`](https://github.com/blockstack/blockstack-todos) repository

#### Install Dependancies & run server

```
$ git clone git@github.com:blockstack/blockstack-todos.git
$ cd blockstack-todos
$ yarn install
$ npm run start
```
This is a single page javascript application, it runs directly in your browser. As you click the `Sign In With Blockstack` button an ephemeral key is generated within the application. This key which is just used for the particular instance of the application is just used to sign a signin request. It also generates a public key which is sent to the browser and used to encrypt data coming back to you. This will allow you to store data in your Blockstack storage.

This signed authentication request is sent to the 

