# Add issue id hook [![Build Status](https://travis-ci.org/pbetkier/add-issue-id-hook.svg?branch=master)](https://travis-ci.org/pbetkier/add-issue-id-hook)

Git commit hook for adding related JIRA issue ids to commit messages.

## How does it work?
Issue id is parsed from the current branch name and prepended to your commit message.


    $ git checkout -b EXAMPLE-123-new-feature
    $ git add some_code.py
    $ git commit -m "Added some pretty code."
    $ git log
        ...
        EXAMPLE-123 Added some pretty code.

Here's the specification generated from ``spec.py`` tests:

#### AddIssueIdHook:
 - prepends issue id from branch name to commit message
 - prepends first matching issue id to commit message if multiple ids in branch name exist
 - doesnt modify commit message if issue id not in branch name
 - doesnt modify commit message if it already starts with issue id
 - doesnt modify commit message if in detached HEAD state
 - supports aborting a commit by providing an empty message
 - supports aborting a commit by exiting from editor without making changes

## Installation
1. Copy ``commit-msg`` file into ``.git/hooks/`` directory of your project's repository.
1. Open the newly created copy of ``commit-msg`` file and set ``project`` variable according to your project's name in JIRA.
1. Make sure the ``commit-msg`` file has execution mode flag set (``chmod +x commit-msg``).

This plugin requires having Python 2.7 installed (comes pre-installed on OS X and Ubuntu).

### Not a JIRA project?

This hook supports JIRA issue ids by default, but you can easily customize it to support any other issue id patterns. Simply change the ``issue_pattern`` variable to a regular expression that matches the issue ids from your ticket system.

## Known limitations
As this commit hook depends on parsing the current branch name, it won't work when committing in detached HEAD state, e.g. when doing a *reword* operation during ``git rebase --interactive``.
