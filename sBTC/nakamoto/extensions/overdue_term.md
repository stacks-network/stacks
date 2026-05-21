# Extension: Overdue Term

> This extension suggests the implementation of a replicated verifiable delay function (VDF) to manage variations in tenure length within the Stacks blockchain. Block producers execute the VDF and submit proofs to increase their tenure's execution budget in case it takes longer than anticipated. VDF calibration adjusts the required ticks for a valid proof based on historical tenure data. Checkpoint blocks report the adjusted tick count, which is then recorded on-chain for reference by Clarity contracts. The primary objective is to eliminate idle time and enhance overall efficiency within the Stacks network.

Naively, the execution budget available to block producers can be treated as equal to the number of Stacks blocks' budgets today, multiplied by the tenure length. Ideally, block producers would produce blocks at a rate such that under network congestion, the tenure budget is completely consumed just as the tenure ends.

It is very difficult in practice to realize this idealized block production schedule, because the length of a tenure has very high variance and is not known in advance. If the block producers reach their tenure budget before the tenure is over, then the Stacks network stalls, which significantly increases transaction latency and degrades the user experience.

To eliminate these periods of idle time, this document proposes implementing a replicated verifiable delay function (VDF) which block producers individually run in order to prove that a tenure is taking too long. If enough block producers can submit VDF proofs that indicate that they have waited for the expected tenure length, then if the tenure is still ongoing, their tenure's execution budget is increased for an additional tenure. The process repeats indefinitely -- as long as block producers can submit VDF proofs, they earn more execution budget until their tenure is terminated by the arrival of the first Bitcoin block of the next tenure.

## VDF Execution

Concurrent with producing blocks, members of the producer set continuously evaluate a VDF for a protocol-defined number of "ticks" (i.e. one pass of the VDF's sequential proof-generation algorithm). The VDF proof must show that the producer evaluated the VDF for at least as many ticks.

Producers are incentivized to evaluate their local VDFs as quickly as possible, because gaining additional tenure execution budget means more transaction fees are available to them. Each time they can create a VDF proof, they submit it as a transaction to the mempool. Because the tenure execution budget grows only once at least 67% of producers (weighted by BTC spend) submit a VDF proof, each producer is incentivized to confirm a new VDF proof transaction as soon as possible by including it in the next block they propose.

Once enough valid VDF proofs have materialized in the blockchain, the tenure's budget expands.

## VDF Calibration

The consensus rules for checkpoint blocks require that the first checkpoint block in a tenure reports an adjusted number of ticks required to produce a valid VDF proof in this tenure. The tick count is adjusted over many tenures such that a producer running the VDF as fast as they can in the current tenure would complete a VDF proof in the expected duration of the tenure (i.e. 100 minutes). The number of ticks can be adjusted up or down, depending on historical tenure data.

To calculate the minimum number of ticks for tenure N, a node will load the following data for the past 15 tenures (about 25 hours of data):

- The wall-clock time of the tenure, calculated as the difference in the UNIX epoch timestamps between the last and first Bitcoin blocks in the tenure (as an array `TIMES`).
  - The consumed execution budget for the tenure (as an array `EXECUTION`).
  - The minimum number of ticks for the tenure (as an array `TICKS`).
  - The integer number of times the execution budget was increased in the tenure (as an array `EXCEEDED`).

The node then calculates the scaled average number of times the tenure budget was exceeded as: `s = (sum(TIMES) / 1500) \* (sum(EXCEEDED) / 15)`

If `s >= 0.5`, then it means that in the average tenure in this sample, producers were able to earn expanded tenures with over 50% probability. This indicates that the tick count needs to be increased, because producers were able to regularly evaluate the VDF faster than the tenures completed. In this case, it is multiplicatively increased by a factor of `min(2.0, s / 0.5)`, and rounded down to the nearest integer.

If `s < 0.5`, then in the average tenure, producers did not expand the budget over 50% of the time. This could be due to any of three reasons:

- The average tenure length was less than 10 minutes, so the budget was never exceeded and no VDF proofs were produced
- There was no network congestion, so producers simply didn't need to submit any VDF proofs
- There was network congestion, but the minimum tick count was so high that producers were unable to earn more budget to address it

We are interested in distinguishing that last case from the others, which do not warrant a minimum tick decrease. To do so, the node examines each consumed budget in `EXECUTION[i]` where `TIMES[i] > 6000`. If the majority of each such `EXECUTION[i]` contains a cost parameter that is over 95% of the allotted budget, we can infer that the network was congested but producers were unable to ask for more budget (i.e. Bitcoin didn't terminate their tenure early). In this case, the minimum tick count is multiplicatively decreased by a factor of `min(2.0, a)` where `a` is an adjusted scale factor, calculated to only consider tenures where producers really did need to increase the budget:

```
n = len(EXCEEDED[i] where TIMES[i] > 6000 and EXECUTION[i] has a near-full cost parameter)
a = (sum(TIMES) / 1500) \* (sum(EXCEEDED) / n)
```

The final tick count reported in the checkpoint block can be as low as 1, or as high as `u128::MAX`. The initial tick count will be calculated once a VDF implementation is written and tested.

The initial tick count is unconditionally used for the first 15 tenures.

## VDF On-Chain State

Each checkpoint block will contain a special-purpose transaction from the producers which contains the new tick count. Each Stacks node independently performs the VDF calibration above; the VDF calibration transaction merely announces it.

The VDF tick counts are recorded to a boot code contract `SP000000000000000000002Q6VF78.vdf`, and exposed via read-only functions so that Clarity contracts can act on them.
