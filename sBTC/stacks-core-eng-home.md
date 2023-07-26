# What is Stacks Core Eng?

**Stacks Core Eng** is a collective term that encompasses the vital participants for the Nakamoto Release, sBTC, Clarity VM, and Testing & Hardening initiatives. The contributors to these initiatives play a crucial role in designing, developing, supporting, and ensuring the security of the Stacks Blockchain and sBTC-related initiatives, and the associated infrastructure, programming and management that brings this technology to life.

## What is Stacks Core Eng North Star?

Stacks contributors are committed to propelling the Bitcoin economy forward. Currently, Stacks Core Eng is focused on reaching a TVL of 10,000 BTC within the sBTC protocol three months after the launch of The Nakamoto Release. This ambitious objective will strengthen the Bitcoin ecosystem and increase the utility of Bitcoin as an asset.

## Where can I learn more about active Stacks Core Eng initiatives?

- [Product Requirements Document for sBTC](sbtc-prd.md).
- [Product Requirements Document for sBTC Signer](sbtc-signer-prd.md).

| Initiative          | Engineering Lead                     | Technical Specification Document       | Repo                                                        |
| ------------------- | ------------------------------------ | -------------------------------------- | ----------------------------------------------------------- |
| Nakamoto Release    | [Jude](https://github.com/jcnelson)  | [link](./nakamoto-release-tsd.md)      | [link](https://github.com/stacks-network/stacks-blockchain) |
| sBTC                | [Mårten](https://github.com/netrome) | [link](./sbtc-tsd.md)                  | [link](https://github.com/stacks-network/sbtc)              |
| Clarity VM          | [Brice](https://github.com/obycode)  | [link](./clarity-vm-tsd.md)            | [link](https://github.com/stacks-network/clar2wasm)         |
| Testing & Hardening | [Aaron](https://github.com/kantai)   | [link](./testing-and-hardening-tsd.md) | -                                                           |

## Current Objectives and Key Results

### 3Q23 OKRs: Nakamoto Release

> Coming soon

### 3Q23 OKRs: sBTC

#### **Objective 1:** Deliver sBTC Mini

| Key Result                                                       | Measure                                       | Target |
| ---------------------------------------------------------------- | --------------------------------------------- | ------ |
| The design of sBTC Mini is completed                             | Percentage of open questions answered by docs | 90%    |
| The signer protocol is completed and documented                  | Percentage of open questions answered by docs | 90%    |
| The Clarity smart contracts of the sBTC design are deployed      | Percentage of defined contracts deployed      | 100%   |
| The reference implementation of the signer binary is implemented |  Completion                                   | Yes    |

#### **Objective 2:** Create an sBTC SDK for developers

| Key Result                                               | Measure                                                | Target |
| -------------------------------------------------------- | ------------------------------------------------------ | ------ |
| The sBTC operations are supported in the SDK             | Percentage of ops supported for writing and parsing    | 100%   |
| The SDK supports broadcasting sBTC operations to Bitcoin | Integration test coverage against Bitcoin regtest      | 100%   |
| The SDK interface is exported to Python and JS           | Percentage of public functions exposed to Python or JS | 50%    |

#### **Objective 3:** Engage participation in early sBTC releases

| Key Result                        | Measure                                                | Target |
| --------------------------------- | ------------------------------------------------------ | ------ |
| sBTC is being explored on testnet | Number of unique STX addresses holding an sBTC variant | 50     |
| Developers are building on sBTC   |  Number of known repos on GitHub using the sBTC SDK    | 10     |
| STX holders register as signers   | Number of signers registered in sBTC Mini              | 10     |

### 3Q23 OKRs: Clarity VM

#### **Objective 1:** clar2wasm

| Key Result                                                                                                 | Measure                                              | Target                       |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------- |
| Deliver a Clarity to Wasm compiler. This should be a Rust crate with an associated binary for easy testing | Successfully compile all published Clarity contracts | Fully functional library/cli |

#### **Objective 2:** Stacks WebAssembly Runtime

**Note:** All functionality is not expected to be complete and release-ready by end of Q3.

| Key Result                                   | Measure                                               | Target                                                                    |
| -------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------- |
| Integrate a Wasm runtime into the Clarity VM | Boot successfully from genesis using this new runtime | Complete the first pass of stacks-node’s Clarity VM integration with Wasm |

### 3Q23 OKRs: Testing & Hardening

#### **Objective 1:** Automated Testing for the Stacks Blockchain

| Objective                                   | Key Result                                                                 | Measure                          | Target |
| ------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------- | ------ |
| Automated Testing for the Stacks Blockchain | How many of the now-known bugs are caught with automated black box testing | All three of the bugs are caught |

#### **Objective 2:** Fast test automation for the Stacks Blockchain

| Objective                                                      | Key Result              | Measure                          | Target                                    |
| -------------------------------------------------------------- | ----------------------- | -------------------------------- | ----------------------------------------- |
| Time to run test suite before merging a PR is less than 1 hour | PR test execution times | All three of the bugs are caught | Mean time for a PR’s test suite is 1 hour |
