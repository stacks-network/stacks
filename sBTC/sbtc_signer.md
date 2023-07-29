# sBTC Signer | Product Requirements Document

- [Technical Specifications Document](./sbtc_technical.md).
- [Product Requirements Document](./sbtc_product.md).

# Introduction

This document outlines the requirements for the development of the sBTC Signer, providing guidance and allowing for potential refinements based on continuous feedback and project progress. The requirements are derived from the Signer user stories, which serve as a foundational reference.

## Requirement 1: Enable Third-party API Integrations

**Description:**

The system must enable optional integration with third-party APIs for compliance purposes. The product will provide the necessary tools and configuration options for third-party applications to make local API calls. 

**Requirements:**

| No. | Task                                                                                                                                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Enable third-party applications to make local API calls.                                                                            |
| 2   | Develop an SDK to provide enough control for a user to integrate whichever API or tooling they wish into the signer's deny or approve logic. |
| 3   | Implement auto-sign capability for transactions based on the API results.                                                 |

## Requirement 2: Delegated Signing 

**Description:**

Delegated signing enables designated signers to perform transactions on behalf of users, improving the efficiency and scalability of the signing process. This is a requirement for custodians if the institution chooses not to self-stack. 


**Requirements:**

| No. | Task                                                                |
| --- | ------------------------------------------------------------------- |
| 1   | Implement delegated signing in V0.2 of the Signer product.                   |
| 2   | Conduct further analysis of delegated signing product requirements. |

## Requirement 3: Implement an Auto-Deny Configuration For Transactions That Require a Manual Review 

**Description:**

The system must be able to automatically deny transactions after a protocol-defined number of blocks if the Signer is unable to manually sign within the timeframe. The purpose of this requirement is to accommodate a Signer who has logic that triggers a manual review but is unable to perform the action in the defined timeframe. By default, signers will Deny a transaction rather than allow them to pass the vote deadline and potentially fail to sign.

**Requirements:**

| No. | Task                                                                                                                                   |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Enable an auto deny configuration for transactions that require manual review, and the signer is unable to perform the action within a protocol-defined timeframe. |


## Requirement 4: Signer Dashboard

**Description:**

The Signer Dashboard provides signers with an overview of their responsibilities and transaction history.

**Requirements:**

| No. | Task                                                                                                                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Display a list of all signers in the network on the Signer Dashboard, including their voting power and public key.                          |
| 2   | Provide signers with analytics related to their activities, including the number of transactions signed and a history of past transactions. |

## Explicit Non-Requirements for Mini

1. **Vote Obfuscation:** Vote choices will not be hidden prior to consensus being reached or a vote deadline passed to minimize on-chain collusion. The option of switching to a commit-reveal system to obfuscate vote choices is not included in V1 of the product, but it will be considered for the final release to prevent collusion between signers.
2. **Signer Abstention:** The protocol will not provide signers with the ability to abstain from signing transactions due to the technical complexity involved.



## Action Items:

1. Comprehensive documentation will be provided to guide users on API usage, configuration setup, and performing manual approvals.

## Assumptions:

**Institutional Partner Requirements:**

1. Signer Binary and Configuration: Sophisticated signers will download the signer binary and receive comprehensive documentation on its operation. The configuration process will involve setting up necessary parameters, with the public key as the minimum requirement.
2. API Usage for Configuration: Larger companies may prefer automated processes, so signers are expected to utilize API calls for automated configuration. They will programmatically configure the signer and update the config file accordingly.
3. Reduced Manual Intervention: Signers expect minimal manual intervention and will rely on automated processes and API calls for most interactions with the product.
4. Auto Approval Logic: The signer binary will automatically sign peg-in and peg-out transactions unless explicitly instructed not to. Institutional signers may implement logic for automating the approval process for specific transaction types.
