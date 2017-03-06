# #DecentralizeTheWeb Challenge Winners
  On February 16th Blockstack announced the submissions and winners of the [#DecentralizeTheWeb](https://twitter.com/hashtag/DecentralizeTheWeb?src=hash) challenge. The goal of the event was to get the Blockstack community involved in the creation of serverless apps and concepts. With only a few weeks heads up, we received some great submissions. Check out the recap [here](https://forum.blockstack.org/t/the-decentralizetheweb-recap/746)! 

# Blockstack CLI Video Tutorial Series
  Like having your own personal instructor for every basic command for the Blockstack CLI. Learn how to install the CLI & use commands like $ renew, $ update, and $ register step by step with Blockstack core contributor, Jude Nelson! Get started today by clicking [here](https://www.youtube.com/playlist?list=PLXS8JJHIn4nGCU2uW85dHXpkQJ7QA5JkX).

# Release of the New Blockstack Explorer
  In case you missed our earlier announcement, we launched [Blockstack Explorer](https://explorer.blockstack.org/), a service for looking up info on Blockstack names and their associated addresses and transaction histories. Explorer gives a global view of all activity happening on the Blockstack network. It makes ownership of domains transparent and makes it easy for anyone to see the history of all domain name operations. Read the recent [announcement](http://blockstack.us14.list-manage1.com/track/click?u=394a2b5cfee9c4b0f7525b009&id=4c40716416&e=a5f3df994e) blog post and try it out yourself by looking up your registered name in the .id namespace.

# AWS & FastSync

@Muneeb A let me know whether we’ll have this

MA: This is TBD given Amazon’s turn around time. I can work on the blog post and use my contact at AWS to speed things up.

# Search Integration

@Muneeb A

MA: This is ready to be included. I can write a short description here.

# v0.14.1 Update
  Release 0.14.1 brings many incremental improvements over 0.14. 
- *Fast Sync* -  In its default setting, Blockstack needs to index the underlying blockchain in order to construct its name database and Atlas state. This can take days. To improve the user experience, 0.14.1 adds a fast_sync command that allows the user to fetch, verify, and bootstrap off of an existing node's recent state. Synchronizing with fast_sync takes only a few minutes.
- *Zone file wizard* - The CLI interface in 0.14.1 comes with an interactive zone file wizard that makes it easy to add, remove, and change the priority of URLs to off-chain data. Before, users were expected to craft new zone files by hand, which proved tedious and error-prone.
  
  For the full release notes, including *Upgrade Notes* and *Selected Bugfixes & Fixes* see the latest [release notes](https://github.com/blockstack/blockstack-core/blob/rc-0.14.1b/release_notes/changelog-0.14.1.md).
- ~~Premiere of FastSync (@Jude N can you add a sentence here?)~~
- ~~Premiere of RESTful API (@Jude N can you add a sentence here?)~~
- ~~Alpha of Storage API (@Muneeb A should this be included?)~~

_MA: Let’s take both the storage API and RESTful API out (RESTful can be separate release, it’s probably a blog post and the API is not defined/ready yet). We can give a summary of the v14.1 release notes and then link to the release notes on Github._

# Top Forum Posts
- [What's the Difference between Blockstack and Ethereum](https://forum.blockstack.org/t/what-is-the-difference-between-blockstack-and-ethereum/781/5)
- [How Blockstack Could Address Amazon S3 Outages](https://forum.blockstack.org/t/how-blockstack-could-address-amazon-s3-outages/773/6)
- [Cloudbleed: When Hidden Trust Parties Leak Your Data](https://forum.blockstack.org/t/cloudbleed-when-hidden-trusted-parties-leak-your-data/757)
- [PoS Blockchains Require Subjectivity to Reach Consensus](https://forum.blockstack.org/t/pos-blockchains-require-subjectivity-to-reach-consensus/762)
- [Getting High-Quality Engineers Interested in the Blockchain Space](https://forum.blockstack.org/t/getting-high-quality-engineers-interested-in-the-blockchain-space/749)
- [Update for OpenBazaar Users](https://forum.blockstack.org/t/update-for-openbazaar-users/688)
- [How Does Blockstack Scale for Replacing the Current DNS](https://forum.blockstack.org/t/how-does-blockstack-scale-for-things-like-replacing-the-current-dns-system-as-whole/533) 
- [Blockstack + Lightning](https://forum.blockstack.org/t/blockstack-lightning/689?u=larry)

# Press Coverage
- Mar 2, Harvard Business Review [How Blockchain Applications Will Move Beyond Finance](https://hbr.org/2017/03/how-blockchain-applications-will-move-beyond-finance)
- Feb 27, CampaignLive [Blockchain set to move intermediary brands that 'add no value'](http://www.campaignlive.co.uk/article/blockchain-set-remove-intermediary-brands-add-no-value/1425502#bgF4o1fOCacJEQuf.99)
- Feb 21, Coindesk [Coindesk: Decentralized Web Gets Visual Aid With New Blockstack Explorer](http://www.coindesk.com/decentralized-web-gets-visual-aid-new-blockstack-explorer/?utm_content=buffer7d93f&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)
- Feb 21, Data Center Journal [Data Center Journal: WWW Creator Calls for Internet Decentralizations & Encryption](https://www.datacenterjournal.com/world-wide-web-creator-calls-internet-decentralization-encryption/)
- Feb 17, Coindesk [3 Big Blockchain Ideas MIT is Working on Right Now](http://www.coindesk.com/3-big-blockchain-ideas-mit-working-right-now/)

