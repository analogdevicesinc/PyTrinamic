# PyTrinamic

PyTrinamic is a Python package to set up and control ADI Trinamic modules, evaluation boards and ICs via serial, USB or CAN interfaces.

The package is intended to automate tasks that are typically first done manually with ADI Trinamic's [TMCL-IDE](https://www.analog.com/en/resources/evaluation-hardware-and-software/motor-motion-control-software/tmcl-ide.html).

## Install

Use pip to install PyTrinamic.

```
pip install pytrinamic
```

## Getting Started

Please have a look at the [code examples on GitHub](https://github.com/analogdevicesinc/PyTrinamic/tree/master/examples).

## Contributing

We welcome pull requests! If you plan major changes or you have questions about a planned implementation, please first open a [GitHub issue](https://github.com/analogdevicesinc/PyTrinamic/issues) to discuss your ideas.

Please ensure contributed Python code adheres to the [PEP 8](https://peps.python.org/pep-0008/) Python code style guide and the [PEP 257](https://peps.python.org/pep-0257/) style guide for docstrings.
If you want to express details in docstrings using a markup language, please use [reStructuredText](reStructuredText) like proposed in [PEP 287](https://peps.python.org/pep-0287/) and when documenting parameters, variables, attributes, exceptions use the [Sphinx style](https://www.sphinx-doc.org/en/master/usage/domains/python.html#info-field-lists).
Additionally, please use double quotes (") for string literals and triple double quotes (""") for multiline strings.
Prefer f-strings over `str.format()` and `%` string interpolation.
For logging statements, use the logging module's argument-based formatting: `logger.info("Port %s opened", port)`

PyTrinamic uses [Ruff](https://docs.astral.sh/ruff/) for formatting and linting. Its configuration is in [pyproject.toml](pyproject.toml).

* For formatting, follow the [Ruff Formatter](https://docs.astral.sh/ruff/formatter/) instructions.
* For linting, follow the [Ruff Linter](https://docs.astral.sh/ruff/linter/) instructions.

## License

PyTrinamic is licensed under the MIT License.