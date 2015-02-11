# Resolvers (DRAFT)

***Warning: This document is currently in DRAFT status and therefore may change rapidly and significantly. Do not build production-ready apps based on it yet!***

Resolvers return blockchain data via multiple protocols. Currently, two protocols are defined the spec: __HTTP(S)__ (as a RESTful API), and __DNS__.

The spec adheres to the [Guiding Principles](<#Guiding>) outlined in the [Appendix](<#Appendix>).

__Table of Contents__

- [HTTP RESTful API (Draft)](<#HTTP>)
    - [Reading and writing to blockchains](<#Reading>)
    - [Resolver information](<#Resolver>)
- [DNS API (Draft)](<#DNS>)
    - [TLDs for existing blockchain](<#TLDs>)
    - [Records for blockchains](<#Records>)
    - [metaTLDs (optional)](<#MetaTLDs>)
- [Appendix](<#Appendix>)
    - [Guiding Principles for resolver API](<#Guiding>)

## HTTP RESTful API<a name="HTTP"/>

All operations are performed via the URL [path and query string](https://en.wikipedia.org/wiki/Uniform_resource_locator#Syntax).

All possible queries that can be performed on a blockchain (both read, write, and delete operations) conform to the following structure:

    /{version}/[{chain}|resolver]/{resource}/{property}/{operation}{resp_format}?{args}

Examples:

    https://api.example.com/v1/namecoin/key/id%2Fbob
    https://api.example.com/v1/bitcoin/addr/MywyjpyBbFTsHkevcoYnSaifShG2Et8R3S
    https://api.example.com/v1/namecoin/key/id%2Fclinton/transfer?to_addr=ea3df...
    http://api.example.com/v1/resolver/fingerprint

Unless marked __Optional__, all parts are required:

- `{version}`: Specifies the API version. This value should be `v1` for now.
- `[{chain}|resolver]`: Specifies the full name of the blockchain, or request [resolver-specific information](<#ResolverInfo>).
- `{resource}`: Blockchains can support different resources that can be queried, but most support the same types of resources. For example, all blockchains (by definition) have a `blocks` resource. Examples: `blocks`, `txn`, `txns`, `addr`, `key`, `accounts`, `contracts`.
- `{property}` __(Optional):__ Specifies a property of a `{resource}`. Depending on the resource being queried, this can be used to refer to different things. Properties MUST be [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding)! Example queries:
    + `/v1/namecoin/blocks/height` - The height of the blockchain (positive integer).
    + `/v1/namecoin/addr/MywyjpyBbFTsHkevcoYnSaifShG2Et8R3S` - Return information about this address.
- `{operation}` __(Optional):__ Perform some action on a `{resource}` or a `{property}` of a resource. Example queries:
    + `/v1/namecoin/key/d%2Fgreatwebsite/transfer` - Transfer the key (in this case the domain `greatwebsite.bit`) to a new owner (specified by `{args}`).
    + `/v1/namecoin/key/u%2Fryan` - Return the JSON stored in the Namecoin blockchain for `/u/ryan`.
- `{resp_format}` __(Optional):__ The response format. __Default__ response format is JSON. Resolvers MUST support `.json` and MAY support other formats. Examples:
    + `/v1/namecoin/blocks/height.xml` - Return response in XML instead of JSON.
- `{args}` __(Optional):__ The URL-encoded arguments to some `{operation}`. Examples:
    + `/v1/namecoin/key/d%2Fgreatwebsite/transfer?to_addr=MywyjpyBbFTsHkevcoYnSaifShG2Et8R3S` - Transfers `greatwebsite.bit` to the owner at the specified address on the Namecoin blockchain.

<a name="Reading"/>
### Typical resources and operations across blockchains

__TBD: actual specs. Can infer from examples.__

Data being written SHOULD be placed into the body of the request, following standard `POST` semantics.

<a name="ResolverInfo"/>
### Resolver-specific information

Resolver-specific functionality MAY be provided should resolvers choose to provide resolver-specific information.

For example, a resolver can provide its TLS fingerprint like so:

- `/v1/resolver/fingerprint`

__TBD: Specify possible resources and their response format.__

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

Resolvers conforming to this spec MAY support the `.dns` metaTLD, and return all queries to this TLD with an `A` record specifying the resolver's public facing IP address.

#### Records for blockchains<a name="Records"/>

| DNS Record |    Blockchain use   |
|------------|---------------------|
| TLSA       | _TBD: fill this in_ |

#### metaTLDs<a name="MetaTLDs"/>

metaTLDs are TLDs that [resolve to the IP of the resolver itself](http://blog.okturtles.com/2014/02/introducing-the-dotdns-metatld/).

<a name="Appendix"/>
## Appendix

<a name="Guiding"/>
#### Guiding Principles for resolver API

1. __Agnosticism to maximum extent possible.__ It would be a detriment to blockchain innovation for us to assume there is a "best" blockchain for doing key/value mappings. That is why this spec supports key/value lookups in a blockchain-agnostic manner. For unique features found only in one blockchain, the API should be designed in a generic way that can be adaptable to other blockchains should they implement said feature.
2. __Maximize both simplicity and usability.__ Start with a simple, solid foundation and build off of it as necessary. Simple requests should have simple formats. Complicated requests should express that complexity in a way that builds off of the simple foundation.
    - In cases where ambiguity exists about the right design decision, _both_ approaches should be implemented and tested in the real-world. Real-world feedback will determine how to proceed.
3. __Maximize security and privacy.__ The API must be queriable over a MITM-proof channel. It must be flexible enough to support arbitrary security protocols and cryptography. To the maximum extent possible, the API should be stateless, and must not leak any unnecessary information or metadata about the connection.
4. __All design decisions must have justifications.__ This improves the quality of the spec by encouraging discussion, and promotes transparency. [[1]](https://forum.namecoin.info/viewtopic.php?p=10750#p10750)
