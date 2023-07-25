# sBTC Signer | Product Requirements Document

>Detailed Technical Specifications Document can be found [here](sbtc-tsd.md).

>Detailed Product Requirements Document for sBTC can be found [here](sbtc-prd.md).

# Introduction

This document outlines the requirements for the development of the sBTC Signer, providing guidance and allowing for potential refinements based on continuous feedback and project progress. The requirements are derived from the Signer user stories, which serve as a foundational reference.

## Requirement 1: Integration with Transaction Monitoring API

**Description:**

The system must enable seamless integration with the Chainalysis API to facilitate blockchain transaction analysis, enhancing security and compliance. The product will offer the necessary tools and configuration options to facilitate API calls by third-party applications.

**Requirements:**

| No. | Task |
| --- | --- |
| 1 | Support third-party applications to make Chainalysis API calls. |
| 2 | Provide minimal configuration control for secure and flexible API calls, including a list of auto-deny addresses for flagged transactions. |
| 3 | Implement auto-deny capability for transactions based on Chainalysis API analysis results. |

## Requirement 2: Trigger Manual Review for Transactions Above Certain Threshold

**Description:**

The system should automatically initiate a manual review process for specific transactions based on predefined conditions to ensure compliance and prevent suspicious activities.

**Requirements:**

| No. | Task |
| --- | --- |
| 1 | Allow setting a maximum auto-approve transaction amount. Transactions exceeding this amount will trigger a manual review for approval. |
| 2 | Implement a default time limit for the manual review process (e.g., 24 hours) to ensure timely action on flagged transactions. |

## Requirement 3: Auto Deny Configuration After X Blocks

**Description:**

The system must automatically deny transactions after a specified number of blocks if the signer is unable to sign within the timeframe.

**Requirements:**

| No. | Task |
| --- | --- |
| 1 | Allow configuration of the number of blocks after which a transaction is automatically denied. |
| 2 | Determine and specify the penalty mechanism for cases where a user does not sign a transaction during the manual review process (e.g., freezing or slashing rewards). |

## Requirement 4: Delegated Signing (Mini v2 Feature)

**Description:**

Delegated signing enables designated signers to perform transactions on behalf of users, improving the efficiency and scalability of the signing process.

**Requirements:**

| No. | Task |
| --- | --- |
| 1 | Implement delegated signing in V2 of the product. |
| 2 | Conduct further analysis of delegated signing product requirements. |

## Requirement 5: Signer Dashboard

**Description:**

The Signer Dashboard provides signers with an overview of their responsibilities and transaction history.

**Requirements:**

| No. | Task |
| --- | --- |
| 1 | Display a list of all signers in the network on the Signer Dashboard, including their voting power and public key. |
| 2 | Provide signers with analytics related to their activities, including the number of transactions signed and a history of past transactions. |

## Explicit Non-Requirements for Mini

1. **Vote Obfuscation:** Vote choices will not be hidden prior to consensus being reached or a vote deadline passed to minimize on-chain collusion. The option of switching to a commit-reveal system to obfuscate vote choices is not included in V1 of the product, but it will be considered for the final release to prevent collusion between signers.
2. **Signer Abstention:** The protocol will not provide signers with the ability to abstain from signing transactions due to the technical complexity involved.

## Open Questions:

1. How to attribute votes correctly during delegated signing, considering multiple layers of delegation?
2. What are the downstream requirements of delegated signing?
3. How will signers be motivated or penalized? What happens if a signer fails to vote? Are rewards frozen or slashed? Will they miss the entire POX cycle?
4. What is the maximum time allowed for manual review of transactions?

## Action Items:

1. Comprehensive documentation will be provided to guide users on API usage, configuration setup, and performing manual approvals.

## Assumptions:

**Institutional Partner Requirements:**

1. Signer Binary and Configuration: High-reputation signers will download the signer binary and receive comprehensive documentation on configuration and operation. The configuration process will involve setting up necessary parameters, with the public key as the minimum requirement.
2. API Usage for Configuration: Larger companies may prefer automated processes, so high-reputation signers are expected to utilize API calls for automated configuration. They will programmatically configure the signer and update the config file accordingly.
3. Reduced Manual Intervention: High-reputation signers expect minimal manual intervention and will rely on automated processes and API calls for most interactions with the product.
4. Auto Approval Logic: Institutional signers may implement logic for automating the approval process for specific transaction types, but it should minimize the risk of erroneous approvals.