# A cookiecutter for GitHub actions

![](https://img.shields.io/badge/current_version-v0.2.0-blue)
[![build](https://github.com/stracquadaniolab/cookiecutter-github-action/actions/workflows/ci.yml/badge.svg)](https://github.com/stracquadaniolab/cookiecutter-github-action/actions/workflows/ci.yml)

## Overview

A cookiecutter to boostrap a GitHub action.

### Step 1: Bootstrap an action

    cookiecutter https://github.com/stracquadaniolab/cookiecutter-github-action

### Step 3: Versioning
Actions should use the following semantic versioning scheme:
```
{MAJOR}.{MINOR}.{PATCH}
```
where:
- MAJOR: the version introduces incompatible changes with the previous one or new code/functioning structure.
- MINOR: the version introduces compatible changes with the previous one (e.g. new features).
- PATCH: bug fixes.

Version should be tracked using `bumpversion`. You can bump all parts of the version scheme as follows:

- MAJOR: `bumpversion major`
- MINOR: `bumpversion minor`
- PATCH: `bumpversion patch`

### Step 4: Sharing changes
Changes should be commited to GIT by running:
```
git push
git push --tags
```

## Authors

* Giovanni Stracquadanio, @gstracquadanio