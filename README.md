# Welcome to latit_space

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ash2d/latit_space/ci.yml?branch=main)](https://github.com/ash2d/latit_space/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/latit_space/badge/)](https://latit_space.readthedocs.io/)
[![codecov](https://codecov.io/gh/ash2d/latit_space/branch/main/graph/badge.svg)](https://codecov.io/gh/ash2d/latit_space)

## Installation

The Python package `latit_space` can be installed from PyPI:

```
python -m pip install latit_space
```

## Development installation

If you want to contribute to the development of `latit_space`, we recommend
the following editable installation from this repository:

```
git clone https://github.com/ash2d/latit_space
cd latit_space
python -m pip install --editable .[tests]
```

Having done so, the test suite can be run using `pytest`:

```
python -m pytest
```

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).
