## Key-value Entries

### Registering username/profile pairs as key-value entries in Namecoin

You'll need either a desktop Namecoin client [(Namecoin-Qt)](http://namecoin.info/?p=download) or a UNIX Namecoin daemon. Instructions for building namecoind from source are [here](build-debian.md). Once you have a running version of either Namecoin-Qt or namecoind you will need to buy some namecoins (from exchanges like [Kraken](http://kraken.com) or [BTC-e](http://btc-e.com)) and send them to yourself. Now you're ready to register new names.

1. issue a "name new" with the key (the username with "u/" prepended)
2. issue a "name first update" with the chunked profile

### "Name new" operations

The "name new" operation is the first operation required to register a key-value pair on Namecoin (and by extension, a username/profile pair in accordance with the ONS protocol). This is the operation that communicates intent to register and use a given name. Without "name first update," however, the name registration is not complete.

Current cost: 0.01 NMC

### "Name first update" operations

After the "name new" operation is complete, the "name first update" operation completes the name registration.

Current cost: 0.00 NMC

## Profile Chunking

Key-value entries in Namecoin are limited to a maximum of 519 bytes.

As a result, profiles exceeding 519 bytes must be split into several linked components in order to be embedded in the blockchain.

To chunk a JSON object, simply do the following:

1. check if all the remaining data fits in one chunk
2. if not, choose an unregistered Namecoin key (e.g. "i/username-1" - this will be the key of the "next" chunk) and create an empty JSON object (the current chunk), then add a pointer from this chunk to the next one (e.g. "next": "i/username-1")
4. fill the JSON object with as many properties as possible
5. go back to 1

Note: we recommend not using the "u/" namespace for linked chunks.
