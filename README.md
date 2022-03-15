# Add issue id hook

Git commit hook for adding related JIRA issue ids to commit messages, packaged for [pre-commit-hooks](https://pre-commit.com/).

# Why this fork?

In this fork of the [original add-issue-id-hook repo](https://github.com/pbetkier/add-issue-id-hook), I packaged the python script and make the hook installable via [pre-commit-hooks](https://pre-commit.com/)

# Installation

In your repository, add following block to your `.pre-commit-config.yaml`.

``` yaml
  - repo: https://github.com/kaamos1/add-issue-id-hook.git
    rev: ccbc68f5cc2efd1410c65462ded4830099dc9d71
    hooks:
      - id: add-issue-id
        name: Prepend issue ID to commit message
        language: python
        stages: [commit-msg]
```

Dont forget to install the stage hooks:

``` bash
pre-commit install -f --hook-type commit-msg
```

# Contributions

Feel free to create an issue or open a PR in case you want to further extend this tool.

# Acknowledge

Many, many thanks to the original Author [Piotr Betkier](https://github.com/pbetkier)
