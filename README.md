# python_test<a name="python_test"></a>

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [python_test](#python_test)
  - [Setup Local Dev Environment](#setup-local-dev-environment)
  - [Usefull tools](#usefull-tools)
    - [Autoupdate version of the tools in .pre-commit-config.yaml](#autoupdate-version-of-the-tools-in-pre-commit-configyaml)
    - [Run pre-commit check for all files](#run-pre-commit-check-for-all-files)

<!-- mdformat-toc end -->

## Setup Local Dev Environment<a name="setup-local-dev-environment"></a>

- Install `pre-commit` hook

```bash
pip3 install --upgrade pip
pip install -r requirements.txt
pre-commit install
```

## Usefull tools<a name="usefull-tools"></a>

### Autoupdate version of the tools in .pre-commit-config.yaml<a name="autoupdate-version-of-the-tools-in-pre-commit-configyaml"></a>

```bash
pre-commit autoupdate

```

### Run pre-commit check for all files<a name="run-pre-commit-check-for-all-files"></a>

```bash
pre-commit run --all-files

```
