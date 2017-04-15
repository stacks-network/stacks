---
title: Hello, Blockstack Tutorial
description: Tutorial on building a hello world application.
image: /images/visuals/hello-blockstack-tutorial.png
youtube: https://www.youtube.com/embed/UbZ6PlX5rF8
---

Welcome!

In this tutorial, we're going to walk through building a simple application on Blockstack.

This app will be a single-page application (SPA) that runs completely client-side. It will have no backend API to talk to, other than the identity and storage API that the user provides. In this sense, it will be a completely decentralized, server-less application.

For this tutorial, we will use the following tools:

- `npm` to manage dependencies and scripts
- `browserify` to compile node code into browser-ready code
- `blockstack.js` to authenticate the user and work with the user's identity/profile information

### Part 1: Installation & Generation

First, install Yeoman (a popular app generation tool) along with the Blockstack App Generator:

```bash
npm install -g yo generator-blockstack
```

Next, create a directory for the application and enter into that directory:

```bash
mkdir hello-blockstack && cd hello-blockstack
```

Then, use the Blockstack App Generator to generate a simple Blockstack app:

```bash
yo blockstack
```

After you respond to the prompts, the app generator will create all of the app files and then install all dependencies.

### Part 2: Serving the App

Start the development static file server to serve the app locally

```bash
npm run start
```

The simple static file server can be found in `server.js`.

This server will serve all of the files in the `/public` directory, including `index.html`, `app.js`, `bootstrap.min.css` and `app.css`.

### Part 3: Main App Code

The main file of our app is called `app.js` (in the `/public` folder). This is where the majority of the logic is contained.

As you can see, all of the code in the file is wrapped in an event listener that waits until the DOM content has been loaded:

```js
document.addEventListener("DOMContentLoaded", function(event) { 
})
```

Inside of this, we have a sign in button handler that creates an auth request and redirects the user to sign in:

```js
document.getElementById('signin-button').addEventListener('click', function() {
  var authRequest = blockstack.makeAuthRequest(null, window.location.origin)
  blockstack.redirectUserToSignIn(authRequest)
})
```

We also have a sign out button handler that deletes the local user data and signs the user out:

```js
document.getElementById('signout-button').addEventListener('click', function() {
  blockstack.signUserOut(window.location.origin)
})
```

Next, we have a function for showing the user's profile:

```js
function showProfile(profile) {
  var person = new blockstack.Person(profile)
  document.getElementById('heading-name').innerHTML = person.name()
  document.getElementById('avatar-image').setAttribute('src', person.avatarUrl())
  document.getElementById('section-1').style.display = 'none'
  document.getElementById('section-2').style.display = 'block'
}
```

Then, we have logic for signing the user in and displaying the application.

Note that there are 3 main states the user can be in:

- The user is already signed in
- The user has a sign in request that is pending
- The user is signed out

We express that as follows:

```js
if (blockstack.isUserSignedIn()) {
  // Show the user's profile
} else if (blockstack.isSignInPending()) {
  // Sign the user in
} else {
  // Do nothing
}
```

With the first condition (when the user is signed in), we load the user data from local storage and then display the profile. With the second condition (when the user has a pending sign in request), we sign the user in and redirect the user back to the home page. 

```js
if (blockstack.isUserSignedIn()) {
  blockstack.loadUserData(function(userData) {
    showProfile(userData.profile)
  })
} else if (blockstack.isSignInPending()) {
  blockstack.signUserIn(function(userData) {
    window.location = window.location.origin
  })
}
```

### Part 4: App Manifest

The app manifest file (`/public/manifest.json`) contains configurations for your app that dictate how it will be displayed in auth views and on user home screens.

The `manifest.json` file should look like this:

```json
{
  "name": "Hello, Blockstack",
  "start_url": "localhost:5000",
  "description": "A simple demo of Blockstack Auth",
  "icons": [{
    "src": "https://helloblockstack.com/icon-192x192.png",
    "sizes": "192x192",
    "type": "image/png"
  }]
}
```

Keep it as is or fill it in with new information that describes your app.

### Part 5: Source Control

To complete the tutorial, save your app code by pushing it to GitHub.

First, create a simple git repo:

```bash
git init
```

Next, add and commit all of the files:

```bash
git add . && git commit -m "first commit"
```

Then, create a new repo on GitHub and name it "hello-blockstack":

> https://github.com/new

After that, add the remote repo to your local git repo. Make sure to fill in your username:

```bash
git remote add origin git@github.com:YOUR_USERNAME_HERE/hello-blockstack.git
```

Last, push all of the code to the master branch of the remote repo:

```
git push origin master
```

You're done! You just built your first Blockstack app and shipped the code.

You're well on your way to becoming a Blockstack app legend.
