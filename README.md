# A cookiecutter for GitHub actions

Current version: 0.1.0

## Authors

* Giovanni Stracquadanio, info@stracquadaniolab.org

## Overview

### Step 1: Bootstrap an action

    cookiecutter git@github.com:stracquadaniolab/cookiecutter-github-action.git

### Step 3: Versioning
Packages should use the following semantic versioning scheme:
```
{MAJOR}.{MINOR}.{PATCH}-{RELEASE}
```
where:
- MAJOR: the version introduces incompatible changes with the previous one or new code/functioning structure.
- MINOR: the version introduces compatible changes with the previous one (e.g. new features).
- PATCH: bug fixes.

Version should be tracked using `bumpversion`. You can bump all parts of the version scheme as follows:

- MAJOR: `bumpversion major`
- MINOR: `bumpversion minor`
- PATCH: `bumpversion patch`
- RELEASE: `bumpversion release`

### Step 4: Sharing changes
Changes should be commited to GIT by running:
```
git push
git push --tags
```