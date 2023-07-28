# Extension: Fixed Transaction Orders

> An extension is proposed to manage fixed transaction orders in the Stacks blockchain. Its primary goal is to handle potential inconsistencies caused by short-lived Bitcoin forks. The extension introduces speculative execution for Bitcoin-dependent transactions, enabling processing with the understanding that there might be a risk of invalidation during a fork event. In case of a Bitcoin fork, the Stacks blockchain ensures that Stacks transactions are reprocessed in the same order as initially accepted, and any invalid transactions are treated as runtime errors. Additionally, the proposal addresses sBTC wallet operations and indicates potential future work on taint tracking for confirming volatile state.

This document proposes that Stacks continue to support on-Bitcoin transactions for `stack-stx`, `transfer-stx`, and `delegate-stx`. However, the absence of Stacks forks makes it possible for non-finalized Stacks chain state to become inconsistent with the Bitcoin chain. For example, if Alice sends 10 STX to Bob via a `stack-stx`, but the `stack-stx` is mined in a Bitcoin block that later gets orphaned, then Alice's and Bob's new balances are inconsistent with Bitcoin -- a node attempting to bootstrap from the Bitcoin and Stacks chains would not process the now-missing `stack-stx` transaction, and would be unable to authenticate the Stacks blocks against subsequent state snapshots (and thus be unable to finish booting).

Bitcoin forks are rare events, and forks lasting longer than six blocks are extremely unlikely. This document proposes that a Bitcoin transaction which receives at least one tenure of Bitcoin confirmations (i.e. at least 10 Bitcoin confirmations) is sufficiently confirmed that it can be assumed that it will remain confirmed forever.

Nevertheless, short-lived Bitcoin forks arise often. A naive stawman way of dealing with Stacks chain state inconsistency created by these short-lived forks is presented below for illustrative purposes:

- Process all on-Bitcoin transactions at the end of the block, instead of the beginning (as it is done today). Then, the transactions in the block that are not on-Bitcoin are at least not causally-dependent on the on-Bitcoin transactions.
- Do not process on-Bitcoin transactions that arise in tenure N until the state snapshot for tenure N is mined. This all but guarantees that these on-Bitcoin transactions will never be orphaned.
- Report only Bitcoin data as of the last state snapshot via Clarity functions. For example, `get-burn-block-info?` would only report Bitcoin state up to the Bitcoin block which contained the last state snapshot.

While this naive approach would work, the problem is that the second and third requirements introduce a very high transaction confirmation latency for Bitcoin-dependent transactions -- users would need to wait for over two tenures (over 20 Bitcoin blocks) before their Bitcoin-dependent transactions could be processed.

Because Bitcoin forks are rare, this document proposes a form of speculative execution whereby Bitcoin-dependent transactions are processed as soon as they are available (and Bitcoin-dependent information exposed to Clarity as soon as available), but with the caveat that unfinalized transactions may be discarded if a fork arises.

<!-- To minimize the disruption this would cause, stackers require that producers -->

## Recovery from Bitcoin Forks

In the event that a Bitcoin fork arises and invalidates transactions, the Stacks blockchain would guarantee that all Stacks transactions (but not on-Bitcoin transactions) are reprocessed in the same order that they were initially accepted. Stackers will only sign produced blocks that contain the same Stacks transactions as before. However, it is possible that not all Stacks transactions will be valid, since they may be causally dependent on Bitcoin state that is no longer canonical. For this reason, transactions no longer invalidate Stacks blocks; the inclusion of an invalid transaction is treated as a runtime error in all cases.

Old Stacks blocks that contain potentially-invalid state are discarded.

## Bitcoin Forks and sBTC

The sBTC wallet operations already require sufficient Bitcoin confirmations that it is effectively guaranteed that they will never be orphaned by the time the producer set processes them. As such, sBTC by itself is not speculatively instantiated or destroyed -- it can only materialize or dematerialize once its deposit and withdraw transactions are sufficiently confirmed. Consequently, sBTC transfers will remain valid even when Stacks transactions are replayed to recover from Bitcoin forks.

## Future Work: Taint Tracking

A future SIP may propose that the Clarity VM performs taint-tracking on state that may still be volatile. This information is not consensus-critical. However, this information would be useful to off-chain services who need to determine whether or not state they intend to act upon is sufficiently confirmed by Bitcoin.
