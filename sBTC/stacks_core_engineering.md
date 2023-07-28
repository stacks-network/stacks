# What is Stacks Core Eng?

**Stacks Core Eng** is a collective term that encompasses the vital participants for the Nakamoto Release, sBTC, Clarity VM, and Testing & Hardening initiatives. The contributors to these initiatives play a crucial role in designing, developing, supporting, and ensuring the security of the Stacks Blockchain and sBTC-related initiatives, and the associated infrastructure, programming and management that brings this technology to life.

## What is Stacks Core Eng North Star?

Stacks contributors are committed to propelling the Bitcoin economy forward. Currently, Stacks Core Eng is focused on reaching a TVL of 10,000 BTC within the sBTC protocol three months after the launch of The Nakamoto Release. This ambitious objective will strengthen the Bitcoin ecosystem and increase the utility of Bitcoin as an asset.

## Where can I learn more about active Stacks Core Eng initiatives?

- [Product Requirements Document for sBTC](sbtc-prd.md).
- [Product Requirements Document for sBTC Signer](sbtc-signer-prd.md).

| Initiative          | Engineering Lead                     | Technical Specification Document   | Repo                                                        |
| ------------------- | ------------------------------------ | ---------------------------------- | ----------------------------------------------------------- |
| Nakamoto Release    | [Jude](https://github.com/jcnelson)  | [link](./nakamoto.md)              | [link](https://github.com/stacks-network/stacks-blockchain) |
| sBTC                | [Mårten](https://github.com/netrome) | [link](./sbtc_technical.md)        | [link](https://github.com/stacks-network/sbtc)              |
| Clarity VM          | [Brice](https://github.com/obycode)  | [link](./clarity_vm.md)            | [link](https://github.com/stacks-network/clar2wasm)         |
| Testing & Hardening | [Aaron](https://github.com/kantai)   | [link](./testing_and_hardening.md) | -                                                           |

## Current Objectives and Key Results

### 3Q23 OKRs: Nakamoto Release

> Coming soon

### 3Q23 OKRs: sBTC

#### Objective 1: Deliver sBTC Mini

- **Key Result 1**: The design of sBTC Mini is completed
  - **Measure**: Percentage of open questions answered by docs
  - **Target**: 90%
- **Key Result 2**: The signer protocol is completed and documented
  - **Measure**: Percentage of open questions answered by docs
  - **Target**: 90%
- **Key Result 3**: The Clarity smart contracts of the sBTC design are deployed
  - **Measure**: Percentage of defined contracts deployed
  - **Target**: 100%
- **Key Result 4**: The reference implementation of the signer binary is implemented
  - **Measure**: Completion
  - **Target**: Yes

#### **Objective 2:** Create an sBTC SDK for developers

- **Key Result 1**: The sBTC operations are supported in the SDK
  - **Measure**: Percentage of ops supported for writing and parsing
  - **Target**: 100%
- **Key Result 2**: The SDK supports broadcasting sBTC operations to Bitcoin
  - **Measure**: Integration test coverage against Bitcoin regtest
  - **Target**: 100%
- **Key Result 3**: The SDK interface is exported to Python and JS
  - **Measure**: Percentage of public functions exposed to Python or JS
  - **Target**: 50%

#### Objective 3: Engage participation in early sBTC releases

- **Key Result 1**: sBTC is being explored on testnet.
  - **Measure**: Number of unique STX addresses holding an sBTC variant
  - **Target**: 50
- **Key Result 2**: Developers are building on sBTC.
  - **Measure**: Number of known repos on GitHub using the sBTC SDK
  - **Target**: 10
- **Key Result 3**: STX holders register as signers
  - **Measure**: Number of signers registered in sBTC Mini
  - **Target**: 10

### 3Q23 OKRs: Clarity VM

#### Objective 1: clar2wasm

- **Key Result 1**: Deliver a Clarity to Wasm compiler. This should be a Rust crate with an associated binary for easy testing.
  - **Measure**: Successfully compile all published Clarity contracts
  - **Target**: Fully functional library/command line tool

#### Objective 2: Stacks WebAssembly Runtime

- **Key Result 2**: Integrate a Wasm runtime into the Clarity VM.
  - **Measure**: Boot successfully from genesis using this new runtime.
  - **Target**: Complete the first pass of stacks-node’s Clarity VM integration with Wasm.
  - _Note_: All functionality is not expected to be complete and release-ready by end of Q3.

### 3Q23 OKRs: Testing & Hardening

#### Objective 1: Automated Testing for the Stacks Blockchain

- **Key Result 1**: Black-box tests which would have discovered each of the 2.2-2.4 bugs
  - **Measure**: How many of the now-known bugs are caught with automated black box testing.
  - **Target**: All three of the bugs are caught.

#### **Objective 2:** Fast test automation for the Stacks Blockchain

- **Key Result 1:** Time to run test suite before merging a PR is less than 1 hour
  - **Measure**: PR test execution times
  - **Target**: Mean time for a PR’s test suite is 1 hour
