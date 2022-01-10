# {{cookiecutter.artifact_name}}

![](https://img.shields.io/badge/current_version-v0.0.0-blue)

## Overview
{{cookiecutter.artifact_description}}

## Inputs

### `my_param`

**Required** My important param. Default: `.`.

## Example usage

``` 
uses: {{ cookiecutter.artifact_org}}/{{cookiecutter.artifact_id}}
with:
  root_dir: '.'
```