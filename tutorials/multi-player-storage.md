---
title: Multi-player Storage Tutorial
description: Build a decentralized micro-blogging app using multi-player storage in Gaia.
image: /images/visuals/hello-blockstack-tutorial.png
---

In this tutorial, we're going to build a decentralized micro-blogging application using multi-player Gaia storage.

This app will be a React.js application that is completely decentralized and server-less. Identity and storage services will be provided by `blockstack.js`

The app will be able to do the following:

- Authenticate users using Blockstack
- Post new statuses
- Display statuses in the user profile
- Lookup other users and see their profile and statuses

We will be using the following tools:

- `npm` to manage dependencies and scripts
- `yo` to generate boilerplate for a Blockstack React app
- `blockstack.js` to authenticate the user and access Gaia storage

For experienced Blockstack developers, the TL;DR:

- Add the `publish_data` scope to sign in requests
- Use `getFile('filename.json', { username: 'username.id' })` to read a file from another user
- Use `lookupProfile('username.id')` to lookup user profiles
- Use `putFile('filename.json', file)` as before

### Installation & Generation

First, install Yeoman along with the Blockstack App Generator:

```bash
npm install -g yo generator-blockstack
```

Next, create a directory for our application. We will call our app Publik:

```bash
mkdir publik && cd publik
```

Then, use the Blockstack React App Generator to generate a simple Blockstack app:

```bash
yo blockstack:react
```

After you respond to the prompts, the app generator will create all of the app files and then install all dependencies.

To run the app locally:

```bash
npm start
```

And open your browser to `http://localhost:8080`. You should now see a simple React app that you can sign in to using your Blockstack ID. We covered how authentication works in depth in a previous tutorial. ([Blockstack Todos Tutorial](/tutorials/todo-list))

### Multi-player Storage Scope

In multi-player storage, user files stored on Gaia are made visible to others via the `apps` property in the user's `profile.json` file. Every app that uses multi-player storage must add itself to the user's `profile.json` file. The Blockstack Browser will handle this part automatically when the `publish_data` scope is requested during authentication. 

So the first thing we need to do is modify our authentication request to include the `publish_data` scope.

Open `src/components/App.jsx` and locate the sign in handler method:

```javascript
handleSignIn(e) {
  e.preventDefault();
  redirectToSignIn();
}
```

Modify the method to this:

```javascript
handleSignIn(e) {
  e.preventDefault();
  const origin = window.location.origin
  redirectToSignIn(origin, origin + '/manifest.json', ['store_write', 'publish_data'])
}
```

*Note that by default, authentication requests include the `store_write` scope which enables storage.*

If you log out and sign in again, the authentication request will now prompt the user for permission to publish data stored for our app.

![Multi-reader storage authentication](/images/tutorials/multi-player-storage-auth.png)

### Posting Statuses

In this step, we will add functionality to allow posting and displaying of "statuses".

Let's open `src/components/Profile.jsx` and import several methods that we'll be using from `blockstack.js`. These methods are `putFile()`, `getFile()` and `lookupProfile()`. Add them to the import statement for `blockstack` near the top of the file:

```javascript
import {
  isSignInPending,
  loadUserData,
  Person,
  getFile,
  putFile,
  lookupProfile
} from 'blockstack';
```

Then, we'll need to add a few properties to the the initial state in `constructor()`. Your constructor should look like this:

```javascript
constructor(props) {
  super(props);

  this.state = {
    person: {
      name() {
        return 'Anonymous';
      },
      avatarUrl() {
        return avatarFallbackImage;
      },
    },
    username: "",
    newStatus: "",
    statuses: [],
    statusIndex: 0, 
    isLoading: false    
  };
}
```


Now let's modify the `render()` method to add a text input and submit button so that we can post statuses. Replace the `render()` method with the following:

```javascript
render() {
  const { handleSignOut } = this.props;
  const { person } = this.state;
  const { username } = this.state;

  return (
    !isSignInPending() && person ?
    <div className="container">
      <div className="row">
        <div className="col-md-offset-3 col-md-6">
          <div className="col-md-12">
            <div className="avatar-section">
              <img 
                src={ person.avatarUrl() ? person.avatarUrl() : avatarFallbackImage } 
                className="img-rounded avatar" 
                id="avatar-image" 
              />
              <div className="username">
                <h1>
                  <span id="heading-name">{ person.name() ? person.name() 
                    : 'Nameless Person' }</span>
                  </h1>
                <span>{username}</span>
                <span>
                  &nbsp;|&nbsp;
                  <a onClick={ handleSignOut.bind(this) }>(Logout)</a>
                </span>
              </div>
            </div>
          </div>

          <div className="new-status">
            <div className="col-md-12">
              <textarea className="input-status" 
                value={this.state.newStatus} 
                onChange={e => this.handleNewStatusChange(e)} 
                placeholder="What's on your mind?"
              />
            </div>
            <div className="col-md-12">
              <button
                className="btn btn-primary btn-lg"
                onClick={e => this.handleNewStatusSubmit(e)}
              >
                Submit
              </button>
            </div>
          </div>

        </div>
      </div>
    </div> : null
  );
}
```

In the `render()` method above, we're also displaying the Blockstack ID of the user. We'll need to extract this from the user profile data. Locate the `componentWillMount()` method and add the username property below the person property:


```javascript
componentWillMount() {
  this.setState({
    person: new Person(loadUserData().profile),
    username: loadUserData().username
  });
}
```

Next, we'll add two methods to handle our input events:

```javascript
handleNewStatusChange(event) {
  this.setState({newStatus: event.target.value})
}

handleNewStatusSubmit(event) {
  this.saveNewStatus(this.state.newStatus)
  this.setState({
    newStatus: ""
  })
}
```

And a method to perform the required storage operations to save our new statuses:

```javascript
saveNewStatus(statusText) {
  let statuses = this.state.statuses

  let status = {
    id: this.state.statusIndex++, 
    text: statusText.trim(),
    created_at: Date.now()
  }

  statuses.unshift(status)

  putFile('statuses.json', JSON.stringify(statuses))
    .then(() => {
      this.setState({
        statuses: statuses
      })
    })
}
```

Now you should be able to type a status in the text box and save it by pressing the submit button.

You'll see that nothing happens when you press the submit button. Because we haven't added any code to display the statuses.

### Display Statuses

Go back to the `render()` method and add the following block right below the `div` element containing the text input and submit button.

```javascript
<div className="col-md-12 statuses">
  {this.state.isLoading && <span>Loading...</span>}
  {this.state.statuses.map((status) => (
      <div className="status" key={status.id}>
        {status.text}
      </div>
    )
  )}
</div>
```

We also need to fetch statuses on page load, so let's add a new method called `fetchData()` and call it from the `componentDidMount()` method

```javascript

componentDidMount() {
  this.fetchData()
}

fetchData() {
  this.setState({ isLoading: true })
  getFile('statuses.json')
    .then((file) => {
      var statuses = JSON.parse(file || '[]')
      this.setState({
        person: new Person(loadUserData().profile),
        username: loadUserData().username,
        statusIndex: statuses.length,
        statuses: statuses,
      })
    })
    .finally(() => {
      this.setState({ isLoading: false })
    })
}
```

At this point we have a basic micro-blogging app that we can use to post and view statuses. However, there's no way to view other users' statuses. We'll get to the multi-player part in the next steps. But first, let's take a moment to pretty up our app. 

Open `src/styles/style.css` and replace the existing styles with the following:


```css
/* Globals */
a,a:focus,a:hover{color:#fff;}
html,body{height:100%;text-align:center;background-color:#191b22;}
body{color:#fff}
.hide{display:none;}
.landing-heading{font-family:'Lato',Sans-Serif;font-weight:400;}

/* Buttons */
.btn{font-family:'Lato',Sans-Serif;padding:0.5625rem 2.5rem;font-size:0.8125rem;font-weight:400;line-height:1.75rem;border-radius:0!important;-webkit-transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-ms-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;transition:all .2s ease-in-out;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}
.btn-lg{font-size:1.5rem;padding:0.6875rem 3.4375rem;line-height:2.5rem;}
.btn:focus,.btn:active:focus,.btn.active:focus{outline:none;}
.btn-primary{color:#fff;border:1px solid #2C96FF;background-color:#2C96FF;}
.btn-primary:hover,.btn-primary:focus,.btn-primary:active{color:#fff;border:1px solid #1a6ec0;background-color:#1a6ec0;}

/* Avatar */
.avatar{width:100px;height:100px;}
.avatar-section{margin-bottom:25px;display:flex;text-align:left;}
.username{margin-left:20px;}

/* Scaffolding */
.site-wrapper{display:table;width:100%;height:100vh;min-height:100%;}
.site-wrapper-inner{display:flex;flex-direction:column;justify-content:center;margin-right:auto;margin-left:auto;width:100%;height:100vh;}
.panel-authed{padding:0 0 0 0;}

/* Home button */
.btn-home-hello{position:absolute;font-family:'Source Code Pro',monospace;font-size:11px;font-weight:400;color:rgba(255,255,255,0.85);top:15px;left:15px;padding:3px 20px;background-color:rgba(255,255,255,0.15);border-radius:6px;-webkit-box-shadow:0px 0px 20px 0px rgba(0,0,0,0.15);-moz-box-shadow:0px 0px 20px 0px rgba(0,0,0,0.15);box-shadow:0px 0px 20px 0px rgba(0,0,0,0.15);}

/* Input */
input, textarea{color:#000;padding:10px;}
.input-status{width:100%;height:70px;border-radius:6px;}
.new-status{text-align:right;}

/* Statuses */
.statuses{padding-top:30px;}
.status{margin:15px 0px;padding:20px;background-color:#2e2e2e;border-radius:6px}
```

If everything went well, we should end up with something like this:

![Multi-reader storage authentication](/images/tutorials/multi-player-storage-status.png)

### User Profile Lookup

Let's now modify our `Profile.jsx` to display profiles of other users. We'll be using the `lookupProfile()` method provided by `blockstack.js` which we added to our import statement earlier. `lookupProfile()` takes a single parameter that is the Blockstack ID of the profile you want to look up and returns a profile object.

First, we'll make some changes to the routing structure of our app so that we can view other users' profiles by visiting `http://localhost:8080/other_user.id`

Install `react-router`:

```bash
npm install --save react-router-dom
```

Open `src/index.js` and add to the top of the file:
```javascript
import { BrowserRouter } from 'react-router-dom'
```

Next, change the `ReactDOM.render()` method in `src/index.js` to:
```javascript
ReactDOM.render((
  <BrowserRouter>
    <App />
  </BrowserRouter>
), document.getElementById('root'));

```

Then we'll need to go back to `src/components/App.jsx` and add the new route.
Open `src/components/App.jsx` and import the `Switch` and `Route` components from `react-router-dom`:

```javascript
import { Switch, Route } from 'react-router-dom'
```

Next, locate the line below in the `render()` method:
```javascript
: <Profile handleSignOut={ this.handleSignOut } />
```

And replace it with the following:

```javascript
  : 
  <Switch>
    <Route 
      path='/:username?' 
      render={
        routeProps => <Profile handleSignOut={ this.handleSignOut } {...routeProps} />
      } 
    />
  </Switch>
```

This sets up a route and captures the route parameter to be used as the profile lookup username.

We'll also need to add a rule to our webpack config so that we can properly process URL paths that contain the `.` character. e.g. `http://localhost:8080/other_user.id` *Note: In a production app, the web server needs to be configured to handle this.*

Open `webpack.config.js` in the root project directory and locate the following line:
```javascript
historyApiFallback: true,
```

Change it to this:
```javascript
historyApiFallback: {
  disableDotRule: true
},
```
*Note: We'll need to run `npm start` again for this to take effect.*

Now we jump back to `src/components/Profile.jsx` and add a single method that will let us determine if we're viewing the local user's profile or another user's profile.

```javascript
isLocal() {
  return this.props.match.params.username ? false : true
}
```

Then we can modify our `fetchData()` method like so:

```javascript
fetchData() {
  this.setState({ isLoading: true })
  if (this.isLocal()) {
    getFile('statuses.json')
      .then((file) => {
        var statuses = JSON.parse(file || '[]')
        this.setState({
          person: new Person(loadUserData().profile),
          username: loadUserData().username,
          statusIndex: statuses.length,
          statuses: statuses,
        })
      })
      .finally(() => {
        this.setState({ isLoading: false })
      })
  } else {
    const username = this.props.match.params.username

    lookupProfile(username)
      .then((profile) => {
        this.setState({
          person: new Person(profile),
          username: username
        })
      })
      .catch((error) => {
        console.log('could not resolve profile')
      })
  }
}
```
We first use `isLocal()` to check if we're viewing the local user profile or another user's profile. If it's the local user profile, we will run the `getFile()` function we added earlier. Otherwise, we lookup the profile belonging to the username using the `lookupProfile()` method.

*Note: For `https` deployments, the default Blockstack Core API endpoint for name lookups should be changed to point to a core API served over `https`. Otherwise name lookups will fail due to browsers blocking mixed content. Refer to the [Blockstack.js documention](http://blockstack.github.io/blockstack.js/#getfile) for details. *

In order to fetch the user's statuses, we add the following block to `fetchData()` right after the call to `lookupProfile(username)... catch((error)=>{..}` block:


```javascript
const options = { username: username }
getFile('statuses.json', options)
  .then((file) => {
    var statuses = JSON.parse(file || '[]')
    this.setState({
      statusIndex: statuses.length,
      statuses: statuses
    })
  })
  .catch((error) => {
    console.log('could not fetch statuses')
  })
  .finally(() => {
    this.setState({ isLoading: false })
  })
```

And lastly, we need to conditionally render the logout button, status input textbox and submit button so they don't show up when viewing another user's profile. In the `render()` method, check to ensure that you are viewing your own profile, by wrapping the Logout button and inputs with the `{isLocal() && ...}` condition:

```javascript
{this.isLocal() &&
  <span>
    &nbsp;|&nbsp;
    <a onClick={ handleSignOut.bind(this) }>(Logout)</a>
  </span>
}

//...

{this.isLocal() && 
  <div className="new-status">
    <div className="col-md-12">
      <textarea className="input-status" 
        value={this.state.newStatus} 
        onChange={this.handleNewStatusChange} 
        placeholder="What's on your mind?"
      />
    </div>
    <div className="col-md-12 text-right">
      <button
        className="btn btn-primary btn-lg"
        onClick={this.handleNewStatusSubmit}
      >
        Submit
      </button>
    </div>
  </div>
}
```

And we're done! Point your browser to `http://localhost:8080/your_blockstack.id` to see the profile. Note: You will need to have a registered Blockstack ID to for this to work.

To see the complete source code of this tutorial visit: https://github.com/yknl/publik/tree/tutorial-demo

See a working version of the app [here](http://publik.ykliao.com).
