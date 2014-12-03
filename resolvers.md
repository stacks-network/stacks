# Resolvers (DRAFT)

Resolvers can return data via multiple channels. Currently two protocols are supported in the spec: __HTTP(S) RESTful API__ and __DNS__.

__Table of Contents__

- [HTTP RESTful API (Draft)](<#HTTP>)
    - [Guiding Principles for resolver API](<#Guiding>)
    - [Specifying what is being queried](<#Specifying>)
    - [Reading and writing to blockchains](<#Reading>)
        - [Reading from blockchains](<#Reading>)
        - [Writing from blockchains](<#Writing>)
    - [Resolver information](<#Resolver>)
- [DNS API (Draft)](<#DNS>)
    - [MetaTLDs](<#MetaTLDs>)
    - [Records for blockchains](<#Records>)

## HTTP RESTful API (Draft)<a name="HTTP"/>

Resolvers conform to a blockchain-agnostic RESTful API according the following __Guiding Principles:__

### Guiding Principles for resolver API<a name="Guiding"/>

1. __Agnosticism to maximum extent possible.__ For unique features found only in one blockchain, the API should be designed in a generic way that can be adaptable to other blockchains should they implement said feature.
2. __Maximize both simplicity and usability.__ Start with a simple, solid foundation and build off of it as necessary. Simple requests should have simple formats. Complicated requests should express that complexity in a way that builds off of the simple foundation. All design decisions must have justifications. [[1]](https://forum.namecoin.info/viewtopic.php?p=10750#p10750)
    - In cases where ambiguity exists about the right design decision, _both_ approaches should be implemented and tested in the real-world. Real-world feedback will determine how to proceed.
3. __Maximize security and privacy.__ The API must be queriable over a MITM-proof channel. It must be flexible enough to support arbitrary security protocols and cryptography. To the maximum extent possible, the API should be stateless, and must not leak any unnecessary information or metadata about the connection.

### Specifying what is being queried<a name="Specifying"/>

Resolvers can support multiple _functionalities_ and multiple _blockchains_.

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

#### Reading from blockchains<a name="Reading"/>

__Examples: Querying user profile information__

|                  Desired Data                  |         HTTP Header          |       Query       |
|------------------------------------------------|------------------------------|-------------------|
| XML representation of `/u/ryan` in Namecoin    | BLOCKCHAIN: api.namecoin.dns | GET /u/ryan.xml   |
| JSON representation of `/u/muneeb` in Namecoin | BLOCKCHAIN: api.namecoin.dns | GET /u/muneeb     |
| JSON representation of `/id/greg` in Namecoin  | BLOCKCHAIN: api.namecoin.dns | GET /id/greg.json |

_Note that JSON is the default when the extension isn't specified._

#### Writing from blockchains<a name="Writing"/>

_TBD: [copy from namecoin forum](https://forum.namecoin.info/viewtopic.php?p=10750#p10750)._

### Resolver information<a name="Resolver"/>

| `HOST` or `BLOCKCHAIN` Header Value | HTTP verb |         Query          |               Returns               |
|-------------------------------------|-----------|------------------------|-------------------------------------|
| fingerprint.api.namecoin.dns        | _ANY_     | /{. [json &#x7C; xml]} | _TBD: format of SHA256 fingerprint_ |

## DNS API (Draft)<a name="DNS"/>

#### MetaTLDs<a name="MetaTLDs"/>

MetaTLDs are TLDs that [resolve to the IP of the resolver itself](http://blog.okturtles.com/2014/02/introducing-the-dotdns-metatld/).

Resolvers conforming to this spec MUST support the `.dns` metaTLD, and return all queries to this TLD with an `A` record specifying the resolver's public facing IP address.

#### Records for blockchains<a name="Records"/>

| DNS Record |    Blockchain use   |
|------------|---------------------|
| TLSA       | _TBD: fill this in_ |
