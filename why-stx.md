Why is the STX token needed for Stacks?

With the Nakamoto upgrade and the rollout of sBTC, Stacks is evolving toward a Bitcoin-native application layer where users and applications primarily interact with BTC. In practice, this means users can hold BTC-denominated assets, use BTC inside apps via sBTC, and (in many cases) pay transaction fees using BTC.

Given this shift, a common question is:

If apps use BTC, why does STX still exist?

This document explains why STX is still necessary, what role it plays today, and what it does not try to be.

Short answer

STX exists to keep Stacks decentralized.

It is not designed to be the dominant user currency of the ecosystem. Instead, STX plays a protocol-level role by providing incentives that cannot be fulfilled by BTC alone.

Without STX, Stacks would have to rely on trusted federations — similar to Liquid — rather than operating as an open, permissionless network.

What STX does (today)

As of the Nakamoto era, STX is primarily used for:

Incentivizing decentralized block production (sequencers / miners)

Incentivizing decentralized sBTC peg security (signers)

Coordinating long-term network security via Stacking

These are infrastructure roles, not application-level currency roles.

Why BTC alone is not enough

Many Bitcoin community members are rightly skeptical of unnecessary tokens. In many projects, a token adds no real value.

Stacks is different.

Stacks was created by Bitcoin builders with a long history of building directly on Bitcoin L1 without tokens (e.g., BNS on Bitcoin in 2015 using OP_RETURN). The decision to introduce STX was not ideological — it was architectural.

The core problem

Bitcoin cannot mint new BTC to secure another chain.

But any decentralized network needs a way to:

Incentivize block production

Penalize misbehavior

Remain open and permissionless

Bitcoin solves this on L1 via block rewards.
Stacks must solve the same problem off L1, without modifying Bitcoin.

That requires a native asset.

STX and decentralized block production

Stacks uses Proof-of-Transfer (PoX), where miners commit BTC to Bitcoin L1 to participate in block production on Stacks.

However:

BTC cannot be minted by the Stacks protocol

BTC fees alone are insufficient to guarantee open participation

Using BTC directly would bias control toward large incumbents

STX is minted by the protocol and used to:

Reward sequencers

Keep block production permissionless

Avoid cartelization or federation control

This mirrors Bitcoin’s own design, where BTC issuance secures the network.

STX and sBTC security (peg-out signers)

sBTC is designed as a trust-minimized, open peg, not a federation.

Key properties:

Anyone can become a signer

Signers are economically incentivized to act honestly

Misbehavior is economically punishable

This requires:

A native asset to align incentives

A unit that the protocol can control

BTC cannot fulfill this role.
STX is used to secure the peg-out path and make sBTC non-custodial.

Without STX, sBTC would require a trusted federation — the exact outcome Stacks is designed to avoid.

STX is not meant to replace BTC in apps

An important clarification:

STX is not meant to be the primary currency users interact with in applications.

Post-sBTC:

BTC is the dominant unit of account

Users can hold BTC-backed assets

Apps can price in BTC

Fees can be paid in BTC via sBTC

STX operates below the application layer, similar to how:

ETH secures Ethereum but stablecoins dominate usage

BTC secures Bitcoin but users transact via layers and abstractions

Stacking: aligning long-term incentives

STX holders can participate in Stacking, where they:

Lock STX

Help secure the network

Earn BTC rewards

This mechanism:

Aligns STX holders with Bitcoin’s success

Converts protocol participation into BTC yield

Avoids inflation-only security models

Importantly, Stacking pays out in BTC, not STX — reinforcing Bitcoin as the economic center.

The alternative: federation

Removing STX would force Stacks into a federated model:

Fixed set of block producers

Trusted peg operators

Permissioned governance

Reduced censorship resistance

This is a valid design (e.g., Liquid), but not the design goal of Stacks.

Stacks aims to be:

Open

Permissionless

Bitcoin-aligned

Decentralized at the protocol layer

STX is the minimal mechanism required to achieve that.

Summary

BTC is the user-facing asset of Stacks

sBTC enables Bitcoin programmability

STX secures the network and peg

STX exists to prevent federation

Bitcoin remains the economic center

Stacks does not introduce a token to extract value —
it introduces STX to protect decentralization.

Further reading

Stacks whitepaper: https://stacks.co/stacks.pdf

sBTC design: https://stacks.co/sbtc

Bitcoin L2 trilemma: https://x.com/muneeb/status/1717542872545628394

Related FAQ: Why is Stacks a Bitcoin L2?
