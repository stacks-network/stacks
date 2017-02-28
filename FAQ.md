#General	-	What is Blockstack?
Blockstack is a new decentralized internet.

With Blockstack, users control their data and apps run on their devices. There are no middlemen, no passwords, no massive data silos to breach, and no services tracking us around the internet.

The applications on blockstack are server-less and decentralized. Developers start by building a single-page application in Javascript, Then, instead of plugging the frontend into a centralized API, they plug into an API run by the user. Developers install a library called 'blockstack.js' and don't have to worry about running servers, maintaining databases, or building out user management systems.

Personal user APIs ship with the Blockstack app and handle everything from identity and authentication to data storage. Applications can request permissions from users and then gain read and write access to user resources.

Data storage is simple and reliable and uses existing cloud infrastructure. Users connect with their Dropbox, Google Drive, etc and data is synced from their local device up to the cloud.

Identity is user-controlled and utilizes the blockchain for secure management of keys, devices and usernames. When users login with apps, they are anonymous by default and use an app-specific key, but their full identity can be revealed and proven at any time. Keys are for signing and encryption and can be changed as devices need to be added or removed.

Under the hood, Blockstack provides a decentralized domain name system (DNS), decentralized public key distribution system, and registry for apps and user identities.


#General	-	What is a Blockstack ID?
These are the names & identities registered in the .id namespace on Blockstack. 

#General	-	What is a decentralized internet?

#General	-	What problems does Blockstack solve?
Users can now use Web applications where:

you own your data, not the application;
you control where your data is stored;
you control who can access your data

Developers can now build Web applications where:

you don't have to deal with passwords;
you don't have to host everyone's data;
you don't have to run app-specific servers
Right now, Web application users are "digital serfs" and applications are the "digital landlords." Users don't own their data; the app owns it. Users don't control where data gets stored; they can only store it on the application. Users don't control access to it; they only advise the application on how to control access (which the application can ignore).

Blockstack applications solve both sets of problems. Users pick and choose highly-available storage providers like Dropbox or BitTorrent to host their data, and applications read it with the user's consent. Blockstack ensures that all data is signed and verified and (optionally) encrypted end-to-end, so users can treat storage providers like dumb hard drives: if you don't like yours, you can swap it out with a better one. Users can take their data with them if they leave the application, since it was never the application's in the first place.

At the same time, developers are no longer on the hook for hosting user data. Since users bring their own storage and use public-key cryptography for authentication, applications don't have to store anything--there's nothing to steal when they get hacked. Moreover, many Web applications today can be re-factored so that everything happens client-side, obviating the need for running dedicated application servers.

#General	-	What opportunities does Blockstack enable?

#General	-	What is a "serverless" app?
The application itself should not run application-specific functionality on a server. All of its functionality should run on end-points. However, the application may use non-app-specific servers with the caveat that they must not be part of the trusted computing base. This is the case with storage systems like Amazon S3 and Dropbox, for example, because Blockstack's data is signed and verified end-to-end (so the storage systems are not trusted to serve data). Serverless can also mean applications where some amount of server-side logic is still written by the application developer but unlike traditional architectures is run in stateless compute containers that are event-triggered, ephemeral (may only last for one invocation)

#General	-	What is a "decentralized" app?

#General	-	Who should build on Blockstack?

#General	-	How are Blockstack domains different from normal DNS domains? 

#General	-	What is Blockstack Core and who is working on it?

#General	-	What is a virtual chain?

#General	-	What's the difference between Onename and Blockstack?

#General	-	How is Blockstack different from Namecoin?

#General	-	How is Blockstack different from Ethereum for building decentralized apps? 

#General	-	I heard you guys were on Namecoin, what blockchain do you use now?

#General	-	Can Blockstack only run on Bitcoin?

#General	-	I heard Blockstack uses a DHT. How does that work?

#General	-	Can the Blockstack network fork? 

#General	-	How is the Blockstack network upgraded over time? What parties need to agree on an upgrade?

#General	-	Can miners take down Blockstack?

#General	-	Who gets the registration fees for name registrations?

#General	-	How long has the project been around? What does the current development roadmap look like?

#General	-	Who started the project? Who maintains it?

#General	-	Where are the current developers based out of? What are the requirements for being a core developer?

#General	-	I heard some companies working on Blockstack have raised venture capital, how does that impact the project?

#Using	-	Can Blockstack control my data or ID when I use it?

#Using	-	How long can I own my ID on Blockstack?

#Using	-	Where is my data stored and how do I control who access it?

#Using	-	Why should I trust the information, like name ownership or public key mappings, read from Blockstack?

#Using	-	Can anyone register a TLD?

#Using	-	Do apps using Blockstack work with a regular browser?

#Using	-	Where can I discover apps using Blockstack?

#Using	-	What programming language can I use to build these apps?

#Using	-	What is the Blockstack Portal?

#Using	-	How can I use the Blockstack CLI?

#Using	-	How do I get started using Blockstack to build apps?

#Using	-	Do I need to run a full Blockstack node to use Blockstack?

#Using	-	What language is the Blockstack software written in?

#Using	-	What incentives are there to run a Blockstack node?

#Using	-	How does Blockstack perform against building apps on Heroku or AWS?

#Using	-	Can Blockstack apps scale, given that Blockstack uses blockchains which don't scale that well?

#Using	-	What if the current companies and developers working on Blockstack disappear, would the network keep running?

#Using	-	What are the business models for companies working on Blockstack?
