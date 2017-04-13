<!--- -->
chapter: Blockchain
<!--- -->

#### Virtualchain

When a Blockstack node boots up, it derives a name database that matches the databases stored by all other nodes. It does this by connecting to a Bitcoin node that it trusts (ideally one that is local) and reading all of the transactions in the blockchain in sequence.

If a transaction has a sequence of data that identifies it as a Blockstack transaction, the node parses it, checks that it has both the proper form and it doesn't violate any authorization rules, and then adds it to the list of valid operations for that block.  Invalid transactions are ignored and discarded.  Once the sequence of operations for a block is validated, the Blockstack node executes them to update its name database.  Because each Blockstack node evaluates the same blockchain data, they will each calculate the same database.  For example, if a keypair issues an operation attempting to transfer a name that it doesn't own, the operation is flagged as invalid and discarded.  But if the keypair that actually owns the name issues a transfer operation, every Blockstack node processes the name transfer.

<img src="blockstack/images/virtual-blockchain.png" class="img-fluid" alt="Virtual Blockchains">

The embedded sequence of valid Blockstack operations make up what is referred to as a virtual blockchain. That is because the transactions of the underlying blockchain are filtered and interpreted in a context that the underlying blockchain is not aware of.   Blockstack gives the transactions extra meaning; they otherwise look like normal transactions to the underlying blockchain's nodes. For example, a Bitcoin node may look at a Blockstack transaction and only see that bitcoins are moving from one address to another and that an unintelligible sequence of data has been attached in a data field (e.g. a field identified by OP_RETURN). Meanwhile, a Blockstack node will look at that data and will know how to interpret it in a way that updates the name database.
