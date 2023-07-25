# Clarity VM | Technical Specification Document

## Executive Summary:

> 👉 _At a high-level what is Clarity VM - its purpose, target audience, and benefits?_

</br>

The Clarity VM (Virtual Machine) is like the brain of the Stacks blockchain. It's responsible for understanding and executing special programs written in the smart contracting language, Clarity. These programs are like sets of instructions that tell the blockchain how to perform various tasks and transactions securely.

The current Clarity VM can sometimes be slow in processing these instructions, which can cause delays in transactions. To make the blockchain faster and more efficient, the Clarity VM Workstream is working on a solution. They plan to use a special technology called WASM (WebAssembly), which is known for its speed and safety, to make the Clarity VM work much faster.

By improving the Clarity VM, the blockchain will be able to handle more transactions quickly, making it easier for people to use and enjoy the benefits of the Stacks blockchain. This upgrade will help make the blockchain more reliable and user-friendly.

## Problem Statement:

> 👉 _What specific problem does Clarity VM initiative solve?_

</br>

The Clarity VM in the stacks-node faces inefficiencies in transaction processing, limiting the number of transactions that can be included in a block. This hampers user experience and transaction capacity. An improved VM is essential to address these limitations.

With an improved Clarity VM, transactions can be processed much faster. This enhancement will enable an increase in the number of transactions that can fit into each block and improve the overall user experience significantly.

## Solution:

> 👉 _How does the Clarity VM initiative provide a solution to the identified problem?_

</br>

The plan to speed up the Clarity VM is to compile Clarity contracts into [WebAssembly (Wasm)](https://webassembly.org/), and then integrate a Wasm runtime into the Clarity VM. Wasm has proven to be an effective tool for fast, safe, and portable code execution, and is being used in several other blockchain projects. Initial back-of-the-envelope testing shows that a Wasm runtime has the potential to be at least an order of magnitude faster, assuming we do not hit other bottlenecks, e.g. MARF reads/writes.

## Technical Requirements:

> 👉 _What technical requirements and criteria must the Clarity VM initiative meet to be fully functional and successfully implemented?_

</br>

The new compiler and runtime must execute all valid Clarity code, including the code currently supported by the existing runtime. If any changes are made to Clarity to simplify or improve the implementation, this runtime will be epoch gated, and the old runtime will be used before its activation height.

The stacks-node should efficiently store the compiled Wasm code alongside the Clarity source for all published contracts and retrieve it quickly when a contract is called. The saved Wasm should be accessible via RPC calls for verification and debugging purposes.

The runtime needs to establish a mechanism to interact with the MARF using Clarity's native functions for reading/writing data-vars and maps.

Furthermore, the runtime must ensure all the isolation, security, and predictability provided by the current runtime. Modifying state outside of well-defined interfaces should be impossible, and contract execution must be predictable and consistent in its execution time.

## Architectural Diagrams:

Clarity → clar2wasm (uses walrus to build Wasm) → Clarity VM (uses wasmtime)

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

## Testing Plan:

> 👉 _What is the comprehensive testing plan in place to ensure quality assurance?_

</br>

Testing of the Clarity to Wasm compiler and updated Clarity VM should include comprehensive unit tests with ~100% coverage. Fuzz testing will generate various Clarity code inputs to validate correct handling of both valid and invalid inputs. Random tests will compare results between the current VM and the new compiler->runtime process. The existing chainstate will be processed with the new implementation to verify consistent results.

Integration of the new stacks-node into Clarinet will enable testing with console and unit testing frameworks. An option to test the new runtime alongside the old one will report any discrepancies. A docker image will facilitate end-to-end testing using clarinet integrate and stacks-devnet-js.

For live testing, a testnet rollout with both runtimes executing transactions will allow comparison of results. If discrepancies arise, the old runtime will be used temporarily, while errors are reported.

Performance testing throughout development will ensure goals are met. We will prioritize safety over speed and carefully consider complexity to maintain simplicity while achieving performance targets.

## Deployment Plan:

> 👉 _What does the deployment plan entail, including infrastructure requirements, deployment processes, and monitoring strategies?_

Upon completion of testing and achieving an acceptable confidence level in the new system, the updated stacks-node will be deployed to the testnet. This phase serves as the final validation step before proceeding with the mainnet deployment. Thorough evaluation and assessment of the testnet rollout will confirm the effectiveness and reliability of the system under real-world conditions, ensuring a smooth and successful activation on the mainnet.
