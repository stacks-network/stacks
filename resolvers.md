# Resolvers (DRAFT)

Resolvers can return data via multiple protocols Currently two protocols are defined by this spec: __HTTP(S)__ (as a RESTful API), and __DNS__.

__Table of Contents__

- [HTTP RESTful API (Draft)](<#HTTP>)
    - [Guiding Principles for resolver API](<#Guiding>)
    - [Summary of querying mechanisms employed](<#Mechanisms>)
    - [Specifying what is being queried](<#Specifying>)
    - [Reading and writing to blockchains](<#Reading>)
        - [Reading from blockchains](<#Reading>)
        - [Writing from blockchains](<#Writing>)
    - [Resolver information](<#Resolver>)
- [DNS API (Draft)](<#DNS>)
    - [TLDs for existing blockchain](<#TLDs>)
    - [MetaTLDs](<#MetaTLDs>)
    - [Records for blockchains](<#Records>)

## HTTP RESTful API (Draft)<a name="HTTP"/>

Resolvers conform to a blockchain-agnostic RESTful API according the following __Guiding Principles:__

### Guiding Principles for resolver API<a name="Guiding"/>

1. __Agnosticism to maximum extent possible.__ It would be a detriment to blockchain innovation for us to assume there is a "best" blockchain for doing key/value mappings. That is why this spec supports key/value lookups in a blockchain-agnostic manner. For unique features found only in one blockchain, the API should be designed in a generic way that can be adaptable to other blockchains should they implement said feature.
2. __Maximize both simplicity and usability.__ Start with a simple, solid foundation and build off of it as necessary. Simple requests should have simple formats. Complicated requests should express that complexity in a way that builds off of the simple foundation.
    - In cases where ambiguity exists about the right design decision, _both_ approaches should be implemented and tested in the real-world. Real-world feedback will determine how to proceed.
3. __Maximize security and privacy.__ The API must be queriable over a MITM-proof channel. It must be flexible enough to support arbitrary security protocols and cryptography. To the maximum extent possible, the API should be stateless, and must not leak any unnecessary information or metadata about the connection.
4. __All design decisions must have justifications.__ This improves the quality of the spec by encouraging discussion, and promotes transparency. [[1]](https://forum.namecoin.info/viewtopic.php?p=10750#p10750)

<a name="Mechanisms"/>
### Summary of querying mechanisms employed

- HTTP headers are used alongside metaTLDs to specify which blockchain is being queried.
- Subdomains are used (per metaTLD) to specify what functionality is being requested for that blockchain.
- HTTP verbs `GET` and `POST` are used to read and write data from blockchain RESTful APIs (respectively).
- The query path is used to specify first the __action__, and then the resource (key) that is being acted upon.
- The query string is used to pass parameters to actions that accept them.
- A path extension (like `.json`) may be appended to specify the format of the response.

This specification intentionally does not make full use of all possible HTTP verbs. If one of these verbs is necessary (such as writing) to blockchains, `POST` can be used.
The reasoning for this decision is multifold:

- The API can function perfectly well with just `GET`. Therefore, relying too much on verbs violates Guideline #2 (maximize simplicity).
- Requiring clients to deal with which verb to use violates Guideline #2 (maximize usability).
- The verbs do not capture all of the actions a resolver might perform.
- The verbs can be easily expressed as actions via the query path of the URL.

### Specifying what is being queried<a name="Specifying"/>

Resolvers CAN support multiple _functionalities_ and multiple _blockchains_. They MUST support: at least one blockchain metaTLD, at least one blockchain TLD, and the corresponding `api.` subdomain functionality.

To specify the blockchain being queried, two HTTP headers are supported: `HOST` and `BLOCKCHAIN`. The `HOST` header is used as convenience when using a resolver for DNS via the [`.dns` metaTLD](<#metatlds>).

__Examples: Specifying the desired blockchain via HTTP headers__

| Desired blockchain |       HTTP header        |
|--------------------|--------------------------|
| Namecoin           | HOST: namecoin.dns       |
| KeyID              | HOST: bitshares.dns      |
| Ethereum           | HOST: ethereum.dns       |
| Namecoin           | BLOCKCHAIN: namecoin.dns |

To specify the desired functionality, the first-level subdomain is used.

__Examples: Specifying the desired functionality via HTTP headers__

|     Desired Feature      |            HTTP header            |
|--------------------------|-----------------------------------|
| RESTful API for Namecoin | HOST: api.namecoin.dns            |
| RESTful API for Ethereum | BLOCKCHAIN: api.ethereum.dns      |
| Blockchain explorer      | HOST: explorer.namecoin.dns       |
| Blockchain explorer      | BLOCKCHAIN: explorer.namecoin.dns |

- Note: if clients are using the resolver for DNS, most programs will automatically set the `HOST` header when a request is made to the metaTLD.

### Reading and writing to blockchains<a name="Reading"/>

_TBD: actual specs. Can infer from examples._

The RESTful API is accessed through the `api.` subdomain.

#### Reading from blockchains<a name="Reading"/>

Resolvers MUST support the `GET` verb for all read actions, and MAY support other verbs for this function at their discretion.
Changing the verb MUST NOT impact the response the resolver sends.

The format of the query path is: `/read/{key}[.{extension}]` where:

- `{key}` is the key being looked up in the blockchain
- `{extension}` is an optional data format for the response

__Examples: Querying user profile information__

|           Desired Data           |         HTTP Header          |         Query          |
|----------------------------------|------------------------------|------------------------|
| XML for `/u/ryan` in Namecoin    | BLOCKCHAIN: api.namecoin.dns | GET /read/u/ryan.xml   |
| JSON for `/u/muneeb` in Namecoin | HOST: api.namecoin.dns       | GET /read/u/muneeb     |
| JSON for `/id/greg` in Namecoin  | BLOCKCHAIN: api.namecoin.dns | GET /read/id/greg.json |

_Note that JSON is the default when the extension isn't specified._

#### Writing to blockchains<a name="Writing"/>

_TBD: [copy from namecoin forum](https://forum.namecoin.info/viewtopic.php?p=10750#p10750)._

These will probably take the form of: `POST /write/{key}`

The data being written SHOULD be placed into the body of the request, following standard `POST` semantics.

### Resolver information<a name="Resolver"/>

| `HOST` or `BLOCKCHAIN` Header | HTTP verb |               Query                |               Returns               |
|-------------------------------|-----------|------------------------------------|-------------------------------------|
| api.namecoin.dns              | _ANY_     | /fingerprint{. [json &#x7C; xml]} | _TBD: format of SHA256 fingerprint_ |

## DNS API (Draft)<a name="DNS"/>

#### TLDs for existing blockchain<a name="TLDs"/>

If a blockchain has a specification for supporting domain resolution, resolvers MUST support resolving `A` records
for blockchain-associated TLDs if the blockchain has one. Resolvers SHOULD support all of the DNS record types of
the blockchain that it supports.

Existing blockchain TLDs are listed below:

|  TLD   |                                           Blockchain                                           |
|--------|------------------------------------------------------------------------------------------------|
| `.bit` | Namecoin ([spec](https://wiki.namecoin.info/index.php?title=Domain_Name_Specification))        |
| `.p2p` | KeyID aka BitShares DNS ([spec](http://wiki.bitshares.org/index.php/.p2p_%28BitShares_DNS%29)) |
| `.eth` | Ethereum (spec doesn't exist yet, probably will follow Namecoin)                               |

_Note: blockchains should choose TLDs that do not conflict with any existing ICANN TLDs (and ICANN should do the same)._ 

#### MetaTLDs<a name="MetaTLDs"/>

MetaTLDs are TLDs that [resolve to the IP of the resolver itself](http://blog.okturtles.com/2014/02/introducing-the-dotdns-metatld/).

Resolvers conforming to this spec MUST support the `.dns` metaTLD, and return all queries to this TLD with an `A` record specifying the resolver's public facing IP address.

#### Records for blockchains<a name="Records"/>

| DNS Record |    Blockchain use   |
|------------|---------------------|
| TLSA       | _TBD: fill this in_ |
