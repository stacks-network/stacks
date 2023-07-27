# Testing and Hardening | Technical Specification Document

## At a high-level what is Testing & Hardening - its purpose, target audience, and benefits?

### Definition

The Testing & Hardening initiative aims to enhance the functionality and user experience of interacting with the Stacks blockchain and its codebase. It focuses on improving the testing framework to prevent frequent bugs during protocol updates and non-consensus changes to the stacks-node, ultimately leading to a more secure and reliable blockchain ecosystem.

### Purpose

The initiative seeks to address the high occurrence of bugs discovered during Stacks releases, as witnessed in the recent `2.1`, `2.2`, `2.3`, and `2.4` updates. By enhancing the testing framework, the goal is to:

- detect bugs early
- reduce critical issues during updates
- create a secure and stable blockchain ecosystem

### Target Audience

The Testing & Hardening initiative targets developers, maintainers, and contributors of the Stacks blockchain and its codebase. Additionally, it benefits end-users by providing a more stable and robust blockchain system.

### Benefits

The proposed improvements in the testing framework offer several benefits:

1. **Bug Detection**: The introduction of new black-box testing methodologies will help identify bugs, including those not impossibly complex, thereby minimizing the likelihood of critical issues
2. **Enhanced PR Evaluation**: The initiative aims to improve the current state of automatic test execution on the stacks-blockchain repository, making it easier to evaluate whether a given PR has sufficient test coverage
3. **Faster Test Execution**: Reducing the overhead of running a full suite of tests on pull requests will speed up test execution and streamline the development process

## What specific problem does The Testing & Hardening initiative solve?

The Testing & Hardening initiative aims to address the significant problem of the current testing for the Stacks blockchain being inadequate in detecting and preventing numerous critical bugs that surfaced during the release of Stacks 2.1 and subsequent versions (`2.1.0.0.0` -> `2.4.0.0.0`).

The rapid discovery of these bugs and the subsequent need for critical updates highlight the urgency to enhance the testing framework. By implementing new black-box testing methodologies and optimizing test execution on pull requests, the initiative seeks to fortify the blockchain's reliability, thereby reducing bugs and ensuring a more stable and secure ecosystem.

## How does the Testing & Hardening initiative provide a solution to the identified problem?

The Testing & Hardening initiative proposes a multi-pronged solution:

- Implement effective black-box testing to detect bugs
- Improve test execution for pull requests

First, it is important to note that these bugs weren’t missed for lack of trying — some bugs are unavoidable, but these bugs are mostly not impossibly complex, and so its reasonable to think that some kind of testing would have caught them. For these kinds of bugs, black-box testing is very well suited to uncovering them. So, the first prong of this work is to implement sufficient black-box testing that these bugs would have been discovered (this is a kind of meta-regression testing).

Second, for PRs, it is currently very difficult to evaluate whether or not a given PR has sufficient testing coverage. The current state of automatic test execution in the stacks-blockchain repository is such that test runs take a long time (if they complete at all), and provides unclear test coverage as a result. This framework must be improved if PR reviews are expected to uncover code that is lacking in test coverage.

## What technical requirements and criteria must the Testing & Hardening initiative meet to be fully functional and successfully implemented?

This workstream must produce source code and documentation for executing black box testing on the stacks-blockchain which would catch each of the aforementioned bugs.

### Architectural Diagrams:

A detailed discussion outlining various black-box testing methods and their potential application to the stacks-blockchain can be found in a [GitHub Discussion](https://github.com/stacks-network/stacks-blockchain/discussions/3732).

## What is the comprehensive testing plan in place to ensure quality assurance?

The Testing & Hardening initiative itself serves as a comprehensive testing plan.

## What does the deployment plan entail, including infrastructure requirements, deployment processes, and monitoring strategies?

Improvements to the stacks-blockchain testing architecture may involve moving from Github actions or Github action’s default runners. However, initially, this testing workstream should focus on continued usage of Github actions for automated tests.

For non-CI tests (i.e., black-box testing like fuzz testing), these tests should run on long-standing executors (because they may need to run for longer), and should be triggered for runs before releases.
