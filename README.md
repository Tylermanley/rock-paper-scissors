# library-template

## What is this repo?
A template for creating Python libraries which includes linting and pytest


## Installation
If just trying to run the code in this repo, the following should suffice:

```bash
pip install -r requirements.txt
```

If you need to make code changes, the following will work:

```bash
pip install -r requirements-dev.txt
```

## Development

Make whatever changes you want.
Note: If you make changes to requirements.in or requirements-dev.in, you need to recompile the requirements:

```bash
pip-compile --no-emit-index-url
pip-compile --no-emit-index-url requirements-dev.in
```

### Unit Tests
Linting and unit tests in this repo can be run using:

```bash
flake8 library_template tests
pytest -v
```
