# Stacks Ecosystem Testing Standards

Pre-Release Testing and Documentation Standard Reference

## 1. Introduction

### 1.1 Purpose

**This document aims to formalize three aspects of stacks ecosystem projects:**

1. **The minimum expectations of repository infrastructure**
2. **The burden of testing and documentation on feature developers**
3. **The quality assurance steps between feature development and release**

It should serve as a reference when writing or reviewing PRs to ensure that incremental changes meet the bar for testing and documentation, and referenced when scoping the testing that needs to happen before rollout.

### 1.2 Scope

**This document outlines the lower threshold for quality assurance requirements across stacks ecosystem repositories.** This document is not intended to exhaustively list all types of testing nor limit the testing and documentation of features to what is outlined in the document.

### 1.3 Glossary

#### 1.3.1 Testing & Development

| Term                 | Definition                                                                                                                                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Feature**          | A unit of functionality that is designed to meet a specific client need or requirement. A feature extends or improves client facing functionality.                                                        |
| **Static Analysis**  | A type of software check that verifies aspects of how the code is written without running the software. Typical examples are formatting checks, security checks, and functional correctness checks.       |
| **Unit Test**        | A type of software test that focuses on a singular unit of code. Generally, this is self contained and does not include outside infrastructure.                                                           |
| **Fuzz Test**        | A type of software test that “fuzzes” a unit of code by placing in randomly generated malformed input into the code and verifying that the behavior is reasonable.                                        |
| **Property Test**    | A type of software test that inputs randomly generated valid values into a unit of code according to a defined set of properties and tests the output according to specified invariants.                  |
| **Integration Test** | A type of gray-box software testing in which the different units, modules or components of a software application are tested as a combined entity.                                                        |
| **Functional Test**  | A type of black-box software test meant to resemble an entire production system. In a sense, functional tests are a specific type of integration test that integrate the entire system.                   |
| **Stress Test**      | A type of software test aimed at pushing the full system to the breaking point. This ensures it can handle the expected levels of stress and isolate the points of failure.                               |
| **Hotfix**           | An emergency software release that needs to be published to resolve an immediate issue. By definition a hotfix is unplanned and is generally not beholden to the regular standard of QA before a release. |

#### 1.3.2 Environments & Networks

| Term        | Definition                                                                                                                                                                                                                                               |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mocknet** | A locally runnable network that mocks the ins and outs of the system outside of the blockchain under test. This is the kind of network used for functional testing.                                                                                      |
| **Devnet**  | A development network that is used by developers to test new features and code before they are deployed to the testnet or mainnet. This is typically a private network that is not accessible to the public.                                             |
| **Testnet** | A blockchain network used for testing new features and code that is nearly identical to the mainnet in terms of consensus mechanism. This network is used by outside developers to begin writing code that interfaces with the eventual mainnet release. |
| **Mainnet** | The blockchain network where the tokens have actual monetary value. Mainnet is the production environment of the blockchain world.                                                                                                                       |

#### 1.3.3 Documentation

| Term                  | Definition                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inline comment**    | A comment loosely attributed to an informally defined section of code.                                                                                                                                                                                                    |
| **Function Document** | A comment formally tied to a function documents aspects of the function.                                                                                                                                                                                                  |
| **Function Contract** | A comment formally tied to a function that defines a “contract” or a set of rules that the function will follow depending on the inputs and outputs. This term refers to the information of the contract itself, but typically this is included in the function document. |
| **README.md**         | A markdown file with documentation that is tied to a repo or sub-directory that contains information about the directory as a whole.                                                                                                                                      |

---

## 2. Repository Standards

### 2.1 Testing

**Each repository should have the following testing components defined within the continuous integration pipeline.**

1. **Static analysis**
2. **Unit / Property Tests with explicit coverage minimum**
3. **Integration Tests**
4. **Functional Tests (Provided there’s a runnable asset)**

#### 2.1.1 Justification

These requirements are fairly standard across all ecosystems. Including these steps within a CI catches issues early and with minimal required infrastructure.

### 2.2 Documentation

**Each repository should have a README.md with**:

1. **A repository summary**
2. **Instructions on how to contribute**
3. **Instructions on how to run continuous integration steps locally**
4. **A link to the License**
5. **A clear description of the pathway to release for the repository code**

#### 2.2.1 Justification

- A repository summary helps users to quickly understand what the project is about and whether it is relevant to them.
- Instructions on how to contribute will help ICs get involved in the project.
- Instructions on how to run continuous integration steps locally will significantly decrease the number of iterations a PR will need to go through before being accepted.
- A link to the License is standard practice and avoids legal complications.
- A written description of the pathway to release will ensure that releases are well-managed and standardized.

### 2.3 Issue Templates

**Each repository should enforce an issue template that includes, at a minimum:**

1. **Full context why the ticket exists**
2. **Success criteria of the ticket with an expected verifiable artifact**

For tickets that are about ideas that don't have a clear deliverable, the verifiable artifact would be some form of documentation that captures the outcome of the discussions.

#### 2.3.1 Justification

Explaining the problem in the ticket helps everyone understand what needs to be fixed, and setting clear goals helps us make sure the ticket is completed to the satisfaction of the project. Additionally, providing context helps individual contributors come up with new and better solutions than the original ticket creator may have thought of. Good engineering rarely happens when engineers don’t know the full situation.

---

## 3. Separation of Feature and QA Development

Below is a diagram of the tests and the burden of maintenance for each step defined above. This is expanded on in the feature and QA developer responsibilities sections below.
![standards-1-test_burden](https://github.com/stacks-network/stacks/assets/2847772/8835b56d-ba77-470a-99f7-0eeb98d7942b)

---


## 4. Feature Developer Responsibilities

_A developer who is coding a feature is a feature developer. This does not exempt the feature developer from contributing to the QA development process - this description is here to codify the responsibilities that can be separated when feature developers are tight or parts of the development process can be separated._

### 4.1 Testing

It is the feature developer’s responsibility to:

1. cover new feature code with an explicit minimum coverage percent defined by the repository
1. resolve any static analysis issues prior to a pull request

Long term, we want to move in the direction of property testing for every feature with optional unit testing for specific edge cases. In situations where minimum coverage does not make sense (e.g. a pure logging function) the PR should include a reason why this bar wasn’t met. See [Pull Request Description](#44-pull-request-description).

#### 4.1.1 Justification

Unit tests and property tests are easiest to write for the developers, who theoretically understand the code they wrote the best. Offloading the writing of tests to either another developer or your future self increases the chance of missing an edge case, or simply increasing coverage without testing the nature and intent of the code under test. Additionally, unit tests and property tests for complicated code can serve as functional documentation of how the code is intended to function - which makes it easier for other developers to contribute by reading the tests.

Switching primarily to property tests will not only reach edge cases in ways that a normal eye might miss, but it also improves the “documentation” piece of the tests. By specifying the nature of the inputs and outputs we make the intent behind the code itself clearer.

### 4.2 Comments and Documentation

**All functions and classes, unless overwhelmingly self-explanatory, must have documentation fit for a reputable and standard open source library written in that language.**

- **Python:** [Numpy](https://numpydoc.readthedocs.io/en/latest/format.html)
- **Rust:** [Standard library](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
- **Java:** [Google/Spring](https://google.github.io/styleguide/javaguide.html#s7-javadoc)
- **Typescript:** [Google](https://google.github.io/styleguide/tsguide.html#comments-documentation)

#### 4.2.1 Justification

We are working on an open source library with high standards, and we expect real people to put their faith in the robustness of our development when they put money into our system. If we expect people to put their faith in our code then we should handle it with the same grace that trusted open source libraries do.

### 4.3 Future Work Identified in Pull Requests

**All merged TODO comments should have a link to a ticket to execute that task**. In cases where the PR might not get merged it’s fair to hold off on creating the ticket until the PR is in a more final state, but at the moment the ticket is merged all TODO comments should have the work tracked in a github issue.

#### 4.3.1 Justification

Without a ticket, future work often gets lost or loses context when it’s rediscovered well after the original TODO was written. By including a ticket for each TODO we ensure the work keeps its context without cluttering the comment itself. Additionally, if we decide not to do the ticket the corresponding TODO can be removed with a PR and linked to the associated ticket so that stray TODOs don’t stay in the code.

### 4.4 Pull Request Description

**All pull requests, without exception, must include a “testing verification” section that both:**

1. **Describes how the PR was tested.**
2. **Outlines additional testing that must take place outside the PR and link to a ticket to execute those tests if they are substantial.**

#### 4.4.1 Justification

Explaining how these features have been tested within the PR helps reviewers pinpoint the areas of the PR to scrutinize.

Describing any additional testing that needs to be done outside of the PR and creating tickets for those tests helps to ensure that we don't forget about any areas of risk, even if we can't test them in the PR itself. For example, if a PR could cause a hard fork, the "additional testing" section might say "sync from genesis and run on a segregated testnet" and then list some specific events that should be tested.

While some pull requests (e.g. updates to CI or documentation) may not need testing of any kind, outlining why a feature is not tested allows reviewers to explicitly confirm that justification. Sometimes a reviewer may assume a feature was tested prior to PR when the developer believed the feature did not need testing. This is the case with some CI changes that can be verified on a separate branch prior to PR, or rust tests within a README.md that the developer was not aware of.

---

## QA Developer Responsibilities

### 5.1 Primary QA Developer Responsibilities

**Ultimately, it is the QA developer responsibility to:**

1. **Execute the testing tickets within the pull request descriptions.**
2. **Ensure the repository meets the minimum requirements above.**
3. **Follow the same development responsibilities of the feature developer.**

### 5.2 Testing Consensus Critical Code

Consensus critical code must have functional tests written by a developer who did not write the code prior to its release. Writing the functional tests for a feature should not block merging of a new feature into the repository, but it must block the release of the feature onto a main net.

#### 5.2.1 Justification

Functional tests are like putting on a blindfold and using the system. The developer who wrote the code knows what the system is supposed to do, but another engineer can see the system objectively and write tests that better simulate how the system will be used by real users.

Consensus critical code is some of the most critical code of the entire system and should be tested sufficiently and adversarially before release.

---

## Pathway to Code Release

### 6.1 Hotfixes

**Hotfixes are a special case that are not beholden to the following standards and require the best judgment of the engineers.**

### 6.2 Standard Software Releases

Standard software libraries and CLIs should follow the standard CI steps and then follow pre-release steps written in the repo’s README.md.
![standards-1-software_release](https://github.com/stacks-network/stacks/assets/2847772/f2cac62b-34fc-4305-8692-9fdd17d71834)

### 6.3 Blockchain Releases

#### 6.3.1 Soft Fork Release

**Patch and minor version releases should include a devnet test in addition to a soak period in testnet where developers can view the health of the environment in a dashboard.** By allowing the changes to soak before a rollout we mitigate any obvious issues in production.

Explicitly, the pathway to release will include the following:

1. Standard pipeline steps outlined above
2. Infrastructure steps prior to mainnet release
   1. Devnet test
   2. Testnet soak (2 PoX cycles)
   3. Begin deployment to mainnet
   
![standards-1-soft_fork](https://github.com/stacks-network/stacks/assets/2847772/99ae48cd-51f6-4aaa-9c08-2b916d4cbbd7)


#### 6.3.2 Hard Fork Release

**Hard fork releases extend the soft fork release procedure with stress testing on a segregated testnet, an internal security review, an outside security audit, and further stress testing on the public testnet.** The local and CI testing steps remain the same.

Below is the path to a major version release for a stacks blockchain change with the changes from the minor version release steps highlighted in yellow.

![standards-1-hard_fork](https://github.com/stacks-network/stacks/assets/2847772/c7ad725b-6387-4cb8-bb60-e4ef76ba019a)

In preparation for a hard fork feature release, we should execute stress tests on the deployed infrastructure and manually verify that the networks remain healthy by monitoring a metrics dashboard over the course of at least 2 PoX cycles. A stress test should first happen concurrently with the internal security review on a segregated testnet, and then should happen again after the security audit by an outside party.

---

## Appendix

### 7.1 Pull Requests

#### 7.1.1 Example Pull Request Template

_Note that this template is not meant to be prescriptive, but is instead an example of a template that meets the lower bar requirements specified above in section [4.4 Pull Request Description](#44-pull-request-description)._

```
# (Title)

## Summary of Changes

Please include the following information:

1. Summary of the changes
2. The related issue
3. Relevant context
4. Any PRs that need to be merged before this one

## Testing

### Risks

Please list, loosely, the risks that are associated with this PR. This can be very short. Even a documentation update would have the risk that the added information misleads a user to do or think XYZ.

### How were these changes tested?

Please describe the following:

1. What tests you ran to verify your changes
2. How to replicate these tests
3. Any relevant details for your test configuration

### What future testing should occur?

Please list known edge cases or tests that need further testing that don't make sense to add in this PR (integration tests and the like). **Once this PR is approved create an issue for each item and update the following section in the PR description so each bullet has an associated ticket next to it.**

## Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
```

#### 7.1.2 Actual Pull Request Description for ([SBTC #108](https://github.com/stacks-network/sbtc/pull/108))

_This is not meant to call out this PR specifically, but it’s a good example of our typical loose PR documentation standard. It was chosen at random with 1 retry._

```
Addresses #79, but the exact purpose of the requirement remains unclear. Since only the contract owner can mint! and burn!, and these functions will not be part of the API, why is the check truly needed here?
Think this is enough @friedger @FriendsFerdinand? I'll add tests if you agree with the approach.
```

#### 7.1.3 Pull Request Updated to use Example Template ([SBTC #108](https://github.com/stacks-network/sbtc/pull/108))

```
# Verify if Passed txid is Mined for Mint! and Burn! (#79)

## Summary of Changes

This PR addresses (#79): enforce the rule that all mints and burns should refer to an existing bitcoin transation. This verification is needed so that we know that sBTC is minted on the stacks chain using the same bitcoin fork as the bitcoin node.

To enforce this rule we've created two new errors that can be thrown from the `asset.clar` clarity contract:

1. `err-invalid-caller` - thrown when the contract caller is not the contract owner in functions that need both to be the same
2. `err-not-token-owner` - thrown during a transfer attempt when neither the token sender nor the contract caller is the sender

Additionally, we've created a new contract, `clarity-bitcoin-mini.clar`, which does `XYZ`.

## Testing

### Risks

Following this change there are a few risks:

1. A valid `asset.clar` clarity contract could be deemed invalid
2. Merkle proof verification in `clarity-bitcoin-mini.clar` could be incorrect, resulting in **XYZ..**
3. etc.

### How were these changes tested?

> **Note**
> this section is innacurate for the actual PR, which does not include testing when it was released. This is not meant to call out this PR; it is representative of the current testing and verification standard.
> Tests were later added in https://github.com/stacks-network/sbtc/pull/115.

These contracts were tested locally using clarinet unit testing. These can be replicated locally using the [Clarinet](https://github.com/hirosystems/clarinet) testing tool. You can follow the instructions on the github page's README to replicate the tests.

Additionally, I ran `clarinet integrate` and and triggered some events that would represent the actions relevant to this PR:

1. `Action 1` - description
2. `Action 2` - description
3. `Action 3` - description

### What future testing should occur?

1. Functional tests that run a bitcoin node and attempt to mint / burn should be shown to fail when not linked to an existing bitcoin transation: https://github.com/stacks-network/sbtc/issues/(issue #)

## Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
```

### 7.2 Issues (Document Amendment)

This was added after gaining consensus from the engineers and team leads, but does not change any of the content of the standards.

#### 7.2.1 Example Issue Template (New Task / Feature)

_Note that this template is not meant to be prescriptive, but is instead an example of a template that meets the lower bar requirements specified above in section [2.3 Issue Templates](#23-issue-templates)._

```
# Title:
[Short, descriptive title of the task/feature]

## Description

Explain the feature with full context

[Detailed explanation of the task or feature, including its context and purpose]

## Technical Details:

[Technical requirements or specifications]

## Acceptance Criteria:

- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

## Associated Milestone: (optional):

[Link to related Milestone, if any]

## Related Issues and Pull Requests (optional):

[Link to related issues or pull requests, if any]

## Dependencies:

[List any dependencies or related tasks]
```

#### 7.1.2 Example Issue Template (Reported Problem or Requested Feature)

```
# Title:
[Short, descriptive title of the issue]

## Description of the Task/Feature:

[Detailed description of the problem or feature request]

## Environment Details: (if applicable)

example:

- OS: [Your OS]
- Browser: [Your Browser]
- Version: [Your Project Version]

## Screenshots (if applicable):

![Screenshot](url)

## Steps to Reproduce (if applicable):

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior (if applicable):

[Description of what you expected to happen]

## Actual Behavior (if applicable):

[Description of what actually happened]

## Additional Information (if applicable):

[Additional details or information]
```
