# sBTC Concerns

> Notable changes are proposed for the sBTC system (**SIP-021**) in the Stacks blockchain. These changes include delaying sBTC materialization until Bitcoin transactions receive at least one tenure of confirmations, simplifying sBTC transfers as regular SIP-010 token transfers without requiring materialization on the Bitcoin chain, and eliminating the need for unconfirmed or frozen blocks and stacker blessings since Stacks no longer experiences forks. These modifications effectively address concerns related to sBTC operations and consensus rules in the Stacks blockchain.

This SIP proposes incorporating the sBTC system described in **SIP-021**, but with the following changes.

## sBTC Wallet Operations

The act of sending BTC to the stacker-controlled Bitcoin wallet would not materialize sBTC until the Bitcoin transaction had received at least one tenure of Bitcoin confirmations. Similarly, withdrawing BTC for sBTC would require at least one tenure of Bitcoin confirmations before its effects materialized on Stacks, as would transferring the wallet's BTC from one set of stackers to the next. Because there are no longer any Stacks forks, a BTC withdrawal would no longer require 150 Bitcoin confirmations.

## sBTC Transfers

Because Stacks no longer forks, sBTC transfers would be treated as any other SIP-010 token transfer. They can be mined as quickly as any other Stacks transaction, and do not need to be materialized on the Bitcoin chain.

## sBTC Consensus Rules

Because Stacks no longer forks, there is no longer a need for the system to identify blocks as unconfirmed or frozen. Also, there is no longer a need for stacker blessings. Instead, this document makes it so that the concerns these protocols were meant to address no longer arise.
