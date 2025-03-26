# Clarity VM | Technical Specification Document

## At a high-level, what is the Clarity VM?

The Clarity VM (Virtual Machine) works like the brain of the [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain). It is responsible for understanding and executing programs written in the smart contracting language, [Clarity](https://clarity-lang.org/), which are essentially just sets of instructions that tell the blockchain how to perform various tasks and transactions securely.

The current Clarity VM can sometimes be slow in processing these instructions, which can cause delays in transaction times. To make the blockchain faster and more efficient, the Clarity VM Workstream is working on a solution: the plan is to use a special technology called WASM ([WebAssembly](https://webassembly.org/)), which is known for its speed and safety, to address the current limitations.

By improving the Clarity VM, the [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain) will be able to process more transactions quickly, in turn making it easier for people to use and enjoy the benefits of the [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain), contributing to a more reliable and user-friendly experience.

### Architectural Diagram

`Clarity` → `clar2wasm` (using [walrus](https://github.com/rustwasm/walrus)) → `Clarity VM` (using [wasmtime](https://github.com/bytecodealliance/wasmtime))

```
               +--------+   clar2wasm    +-------------------+
               |        | -------------> |                   |
    Clarity →  |        |                |  Clarity VM       |
               |        | -------------> |                   |
               +--------+   walrus       +--------+----------+
                                               |
                                               v
                                          +----------------+
                                          |                |
                                          |   Wasmtime     |
                                          |                |
                                          +----------------+
```

## What specific problem does a new Clarity VM solve?

Currently, the Clarity VM implementation in the [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain) has some inefficiencies in transaction processing which limits the total number of transactions that can be included in a block.

With an improved Clarity VM, transactions can be processed much faster, and will enable an increase in the number of transactions that can fit into each block, improving the overall user experience significantly.

## How does a new Clarity VM provide a solution to the identified problem?

The plan to speed up the Clarity VM is to compile Clarity contracts into [WebAssembly (Wasm)](https://webassembly.org/), and then integrate a Wasm runtime into the Clarity VM. [Wasm](https://webassembly.org) has proven to be an effective tool for fast, safe, and portable code execution, and is being used in several other blockchain projects already. Initial proof of concept testing shows that a [Wasm](https://webassembly.org) runtime has the potential to be at least an order of magnitude faster, assuming we do not hit other bottlenecks, specifically I/O related bottlenecks (e.g. MARF database reads/writes).

## What technical requirements and criteria must the new Clarity VM meet to be fully functional and successfully implemented?

The new compiler and runtime must execute all valid [Clarity](https://clarity-lang.org/) code, including all contracts currently supported by the existing runtime. If any changes are made to [Clarity](https://clarity-lang.org/) to simplify or improve the implementation, this runtime will be epoch gated (versioned), and the old runtime will be used before activation at a future block height.

The [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain) will also need to efficiently store the compiled [Wasm](<(https://webassembly.org/)>) code alongside the [Clarity](https://clarity-lang.org/) source for all published contracts and will need to retrieve it quickly when a contract is called. The stored [Wasm](https://webassembly.org/) will also need to be accessible via RPC calls for verification and debugging purposes.

The runtime needs to establish a mechanism to interact with the MARF using Clarity's native functions for reading/writing data-vars and maps.

Furthermore, the runtime must ensure all the isolation, security, and predictability provided by the current runtime. Modifying state outside of well-defined interfaces should be impossible, and contract execution must be predictable and consistent in its execution time.

## What is the testing plan to ensure quality assurance?

Testing of the `Clarity` → `Wasm` compiler and updated Clarity VM should include comprehensive unit tests with **~100% coverage**. Fuzz testing will generate various [Clarity](https://clarity-lang.org/) code inputs to validate the correct handling of both valid and invalid inputs. Random tests will compare results between the current VM and the new `compiler` → `runtime` process, and the existing chainstate will be processed with the new implementation to verify consistent results.

Integration of the new [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain) into Clarinet will enable testing with console and unit testing frameworks, with an option to test the new runtime alongside the old one that will report any discrepancies. A docker image will be created to facilitate end-to-end testing using clarinet integrate and stacks-devnet-js.

For live testing, a testnet rollout with both runtimes executing transactions will allow comparison of results. If discrepancies arise, the old runtime will be used temporarily, while errors are logged and reported.

Performance testing throughout development will ensure goals are met. However, safety will be prioritized over speed and complexity shall be carefully considered to maintain simplicity while reaching defined performance targets.

## What does the deployment plan entail, including infrastructure requirements, deployment processes, and monitoring strategies?

Upon completion of testing and achieving an acceptable confidence level in the new system, the updated [Stacks Blockchain](https://github.com/stacks-network/stacks-blockchain) will be deployed to testnet. This phase serves as the final validation step before proceeding with the mainnet deployment. Thorough evaluation and assessment of the testnet rollout will confirm the effectiveness and reliability of the system under real-world conditions, ensuring a smooth and successful activation on the mainnet.
