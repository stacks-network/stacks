# Blockchain Name System

The Blockchain Name System (BNS), formerly known as Openname, is very similar to the Domain Name System (DNS), but differs in that it gives stronger guarantees on ownership and security, has no trusted parties or "root servers", and is completely decentralized. For more information, visit the BNS wiki or continue reading below.

[![Read the Wiki](/images/read-the-wiki.png)](https://github.com/namesystem/namesystem/wiki)

### Protocol Layers

The Blockchain Name System is composed of several layers. At the bottom, raw data is stored in a decentralized (most likely blockchain-based) key-value store like Namecoin or Blockstore. In the middle layer, resolvers read, interpret, and verify the data from the datastore and make it readily accessible to services. In the top layer, services grab data from resolvers and present it to the end user.

![Blockchain Name System Layers](/images/blockchain-name-system-1.png)

### Entry Types

Entries in the Blockchain Name System each have:

1. a entry type
1. a globally unique identifier
1. a data container for storing descriptive information

Each entry type has it's own namespace in the key-value store and has its own set of specifications for how to format data. Some example entry types are people, businesses, artwork, websites, physical products, and places.

Each entry type may also have it's own terminology. For example, user identies on the system are called passcards. In addition, their unique identifiers are referred to as usernames and the data containers store descriptive information about the person (specifications for formatting this data can be found in the wiki).

If there's an identity type that you'd like to see added to the Blockchain Name System, simply propose it in the issues and start a discussion about it. Once the community approves it and there are specifications established for the type, it can be added to the wiki.
