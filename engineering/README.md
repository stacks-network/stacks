# Blockstack Engineering Handbook

Welcome to the Blockstack Engineering Handbook! This is our attempt at building an engineering process as we build a new internet for decentralized apps.

Here you'll find notes, checklists and knowledge that w

## Table of Contents

- [Sprints](#sprints)
- [Pull Requests](#pull-requests)
- [Repository Management](#repository-management)
- [Planning](#planning)
- [Meetings](#meetings)

## Sprints 
We operate with 2 week sprints. At the beginning of each two week sprint, we have a weekly meeting followed by breakout sessions for the product and engineering teams where user stories and sprint items are generated.

Mid-sprint, we have a weekly meeting and prune tasks from the sprint.

### Sprint management
We create a new Github organization kanban for each sprint with 5 columns: 
* User Stories
* To Do
* Doing
* Delivered
* Accepted.

#### User Stories

Create an issue for each user story in this column. The title  of the story should generally be in the format 'As a `<stakeholder>` I can `<do something>`.

Each user story is assigned to a team member who is the owner of that user story for the sprint. The owner of the user story is responsible for breaking the user story into discrete tasks. Each of these tasks should be linked from the user story. These tasks are added to the To Do column of the sprint board.

#### To Do

**Responsible party:** User story assignee

Tasks that need to be completed to satisfy the user stories belong here until someone starts working on them.

This column uses the "To Do" Github automation enabling the options to put newly opened issues and reopened into this column automatically.

#### Doing
**Responsible party:** Issue assignee
 
Move issues from the To Do to column into this column when you're working on them.

#### Delivered 
**Responsible party:** Issue assignee

When you believe you've completed an issue, mark it as closed and move it to this column. You should also send a pull request for the issue to `develop` or `master` as appropriate and place that pull request in this column.

#### Accepted
**Responsible party:** Pull request reviewer

The reviewer of a pull request is moves the pull request and any issues that it satisfies to the Accepted column when the pull request is approved.

Issues that don't pass review should be moved by the pull request reviewer back to the To Do column.


## Pull Requests
### Creating a pull request
**Responsible party:** Issue assignee

Pull requests are made from topic (feature, hotfix, etc) branches to `develop` or `master`. We never commit directly to these two branches.

#### Checklist
[ ] A description of what is included in the pull request
[ ] Links to any other pull requests in other repos that are required for this pull request
[ ] Instructions on how to test this pull request
[ ] Links to the github issue(s) this pull request addresses
[ ] Assigned to & review request from the person responsible for acceptance testing
[ ] Tests written for all new or modified functionality
[ ] Lint free
[ ] Type declarations written for all modified files (JavaScript)
[ ] Comments for any public functions

*After successful review, the assignee merges the PR.*

## Reviewing a pull request

**Responsible party:** Reviewer 

Pull request reviews are conducted when a pull request is made from a feature or hotfix branch to `develop` or `master`. We do a single code review by a colleague who also works on the same codebase for most things. For anything that involves cryptography, secrets or consensus, we require at least 2 reviews by different people.

#### Review checklist

Below is a basic checklist of items that should be checked during a pull request code review.

- [ ] Does the code work and does it perform its intended function?
- [ ] Is all the code easily understood? Do variable and function names clearly communicate their function?
- [ ] Is there properly formatted (eg. jsdoc for JavaScript) documentation for public and private API methods?
- [ ] Does any code duplicate functionality?
- [ ] Are there any global variables that can be removed?
- [ ] Is there any commented out code?
- [ ] Is there any logging or debugging code that isn't using a logger that can be removed?   
- [ ] Do tests exist and do they adequately cover the changed behavior?
- [ ] Is the code being tested by any linter or type checking tools and does it pass?


## Repository management
We generally use the [git flow](http://nvie.com/posts/a-successful-git-branching-model/) git repository workflow. 

The `develop` branch contains the latest delivered and accepted features. New features are generally developed against the `develop` branch unless they depend on the work done in another feature branch that has yet to be accepted and merged into `develop.

## Planning
[ ] Before Friday Engineering meeting: Each team member collects notes on their top priorities for the coming week, progress on existing items, concerns etc. and adds bullet list items to Friday engineering meeting agenda.
[ ] Friday Engineering meeting: team members discuss their priorities and concerns along with those of the community.
[ ] Meeting deliverable: consensus on a few bullet point priorities for the following week that will be presented to co-founders. These should be listed at the top of the agenda document and link to github issues if they exist.
[ ] Co-founders & team members consider these proposed engineering priorities before the weekly team meeting.
[ ] Co-founders present their priorities for the upcoming week having taken into account the engineering teams priorities & team discusses.

## Meetings

Meetings are expensive, especially for creative people like designers and engineers. A 15 minute meeting can mean an hour or more of lost productivity. Meetings are also synchronous and mean that only those that can be available at that certain time have a chance to give input into the discussion. As such, we prefer to default to conducting discussions on github issues or in the forum and to minimize meetings whenever possible.

### Meeting rules

[ ] Meetings always begin on time: starting late penalizes the punctual and rewards the tardy. You should connect to the meeting conference call or arrive in the conference room a few minutes before the start time.
[ ] Meetings always end on time: our team member and community member time is very valuable and they have other commitments. Disciplined meetings can cover the required topics within the allocated time.
[ ] No meeting shall proceed without a written agenda: if it's not important enough to create an agenda, it's not important enough to hold a meeting
[ ] Each meeting should have a stated goal, deliverable or outcome. This helps keep the meeting on track.

**Calling a meeting**
*Responsible person:* Person who called the meeting (or delegate)

[ ] Create an agenda and notes in a paper document
[ ] Create a zoom meeting link
[ ] Confirm attendee availability
[ ] Create a forum post in the meetings category with date, time, agenda & zoom meeting link*
[ ] Send a calendar invite that includes the zoom meeting link & link to agenda

** Public meetings only*

### Agenda contents
*Responsible person:* Person who called the meeting (or delegate)

[ ] Items to be dicussed
[ ] Desired outcome or deliverable
[ ] Links to any relevant previous meeting notes
[ ] Links to any github issues or other items that provide background info so that attendees can be up to speed

**Holding meetings**
*Responsible person:* Person who called the meeting (or delegate)

[ ] At meeting start, paste link to forum meeting post in slack #engineering channel*
[ ] Nominate a person to take notes
[ ] Quick intros: Name, affiliation, location, one interesting or relevant fact (2 sentences per person max)*
[ ] Record attendees
[ ] Discuss agenda items recording notes in paper document including:
[ ] Record key decisions
[ ] Record actions items & parties responsible for executing on each item
[ ] At conclusion of meeting, paste contents of paper doc into the forum meeting post
[ ] Create relevant github issues for action items and link them from the forum meeting post

** Public meetings only*