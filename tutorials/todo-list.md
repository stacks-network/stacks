---
title: Blockstack Todos
description: Walk through creating a basic Todo application with Blockstack. Learn about Sign In flow and Gaia storage.
image: /images/article-photos/chalkboard.jpg
youtube: https://www.youtube.com/embed/oyvg-h0obFw
---

What are we learning today?

- How to build a Single Page Javascript application with Blockstack
- How to manage authentication using a Blockstack ID 
- How to use Blockstack Storage (Gaia) as an application backend.

#### Requirements

- Installed and running [Blockstack Browser](https://github.com/blockstack/blockstack-browser/releases)
- Have a registered Blockstack name in the Browser
- node.js LTS Version -> `v6.11.2`

#### Getting Started - Install Dependancies & run server

```
$ git clone git@github.com:blockstack/blockstack-todos.git
$ cd blockstack-todos
$ yarn install
$ npm run start
```

#### Sign In - How it works

As you click the `Sign In With Blockstack` button an ephemeral key is generated within the application. This key, which is just used for the particular instance of the application, is just used to sign a Sign In request. It also generates a public key which is sent to the browser and used to encrypt data coming back to your Blockstack node. This allows the application to store data in your Blockstack storage. The signed authentication request is sent to Blockstack through a JSON Web Token. The JWT is passed in via a query string in the parameter: `?authRequest=j902120cn829n1jnvoa...`. 

To decode the token and see what information it holds you can navigate to [jwt.io](http://jwt.io/) and paste the full token there. The output should look similar to below:

```json
{
  "jti":"bbf82977-cc3e-4593-bacc-33ff3b749790",
  "iat":1501784293,
  "exp":1501787893,
  "iss":"did:btc-addr:1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
  "public_keys":[
    "a09932dx081273xmreDII8yhjd0m8ioawfokljISHhejrnHG"
  ],
  "domain_name":"http://localhost:8080/",
  "manifest_uri":"http://localhost:8080/manifest.json",
  "redirect_uri":"http://localhost:8080/",
  "scopes":[
    "store-write"
  ]
}
```

Clicking the Sign In button brings up a modal. When you click `Approve` the following actions are taken:

- A request is sent from the browser to your local blockstack-core node. 
- The blockstack-core node generates a session token which is returned to the application. 
- This session token allows the application to read and write files to your personal Blockstack storage.
- An authentication response is then generated which is similar to the `authRequest` above.
- The `authResponse` also includes a private key intended only for the application. This allows the application to encrypt data on your storage. 
- You are now logged into the Todo application!

##### Notes

- `iss` is a decentralized identifier or `did`. This is used to identify you, along with your name to the application. As you see here the particular `did` we are using is a `btc-addr`.
- The JWT implementation we use is different from other implementations because of the underlying cryptography we employ. There are libraries in [Javascript](https://github.com/blockstack/jsontokens-js) and [Ruby](https://github.com/blockstack/ruby-jwt-blockstack) available on the Blockstack Github to allow you to work with these tokens.

#### Storage - How it works

To see the Gaia Storage in action add a couple of todos. Maybe a list of applications you want to see built on top of Blockstack. I added the following:

- [ ] Software package manager secured by the blockchain
- [ ] Mutable torrents with human readable names
- [ ] Decentralized twitter

These Todos have now been stored in your Dropbox account linked to your Blockstack ID. To view the files go to your [Dropbox account](https://dropbox.com) and open the `Apps` folder. Once inside you should see a folder called `Blockstack`. This is where all of the data stored via the Gaia storage layer lives.

You should see some files that were reciently added when you updated your todos. Download and open the file to see the created JSON. The todos above created the following json:

```json
[
  {
    "id":2,
    "text":"Software package manager secured by the blockchain",
    "completed":false
  },
  {
    "id":1,
    "text":"Mutable torrents with human readable names",
    "completed":false
  },
  {
    "id":0,
    "text":"Decentralized twitter",
    "completed":false
  }
]
```
Now add another todo and mark it completed:

- [x] Blockstack Todo
- [ ] Software package manager secured by the blockchain
- [ ] Mutable torrents with human readable names
- [ ] Decentralized twitter

When you download the newly generated file from your Dropbox it will reflect the change:

```json
[
  {
    "id":3,
    "text":"Blockstack Todo",
    "completed":true
  },
  {
    "id":2,
    "text":"Software package manager secured by the blockchain",
    "completed":false
  },
  {
    "id":1,
    "text":"Mutable torrents with human readable names",
    "completed":false
  },
  {
    "id":0,
    "text":"Decentralized twitter",
    "completed":false
  }
]
```

Now that you have seen the application in action lets dig into how it works. Open the `blockstack-todos` repository in a text editor.

#### Sign In - Implementation

Because this is a [Vue.js](https://vuejs.org/) application the Sign In code is in two locations. The first is a call in `src/components/Landing.vue`:

```js
signIn () {
  const blockstack = this.blockstack
  blockstack.redirectToSignIn()
}
```
When this button is clicked the authentication request described above is generated and the user is redirected to their `blockstack-browser` to approve the login. Once the user approves the login the application must handle the `authResponse`. This happens in `src/App.vue` which is the page at the application root, `/`:

```js
if (blockstack.isUserSignedIn()) {
  this.user = blockstack.loadUserData().profile
} else if (blockstack.isSignInPending()) {
  blockstack.handlePendingSignIn()
  .then((userData) => {
    window.location = window.location.origin
  })
}
```

First we check if the user is signed in with `blockstack.isUserSignedIn()`. If this is true then we can pull that data from the browser and use it in our application. 

If we aren't signed in we then need to check `blockstack.isSignInPending()`. This means that an `authResponse` has been sent back to the application but hasn't been processed yet. the `handlePendingSignIn` function takes care of processing that pending Sign In. 

Signout is handled in `src/components/Dashboard.js`. The method allows the application creator to decide where to redirect the user upon Sign Out:

```js
signOut () {
  this.blockstack.signUserOut(window.location.href)
}
```

#### Storage - Implementation

Next we are going to see how the application interacts with your Dropbox storage. This code lives in the `src/components/Dashboard.vue` file. First lets see where the changes to the Todos are processed:

```js
todos: {
  handler: function (todos) {
    const blockstack = this.blockstack
    return blockstack.putFile(STORAGE_FILE, JSON.stringify(todos))
  },
  deep: true
}
```

You can see that the `todos` JSON object is passed in. Then we use the `blockstack.putFile()` method to store it in our Dropbox. Quick and easy!

The other operation we need to perform is to read the Todos from the storage. This is accomplished with the `blockstack.getFile()` method which returns a promise:

```js
fetchData () {
  const blockstack = this.blockstack
  blockstack.getFile(STORAGE_FILE)
  .then((todosText) => {
    var todos = JSON.parse(todosText || '[]')
    todos.forEach(function (todo, index) {
      todo.id = index
    })
    this.uidCount = todos.length
    this.todos = todos
  })
},
```

The `todos` data is retrieved from the promise.

You now have everything you need to construct complex applications complete with Authentication and Storage on the Decentralized Internet. Go forth and build!
