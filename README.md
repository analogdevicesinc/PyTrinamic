# PyTrinamic

PyTrinamic is a Python package to set up and control TRINAMIC modules, evaluation boards and ICs via serial, USB or CAN interfaces.

The package is intended to automate tasks that are typically done manually with TRINAMICs [TMCL-IDE](https://www.analog.com/en/resources/evaluation-hardware-and-software/motor-motion-control-software/tmcl-ide.html).

## Install

Use pip to install PyTrinamic.

```
pip install pytrinamic
```

## Getting Started

Please have a look at the [code examples on GitHub](https://github.com/analogdevicesinc/PyTrinamic/tree/master/examples).

## Migration Guide

Version 0.2.0 of PyTrinamic introduces several changes to the API. For those who want to convert code that uses an older version of PyTrinamic, we wrote a short [migration guide](https://github.com/analogdevicesinc/PyTrinamic/blob/master/docs/migration_guide.md).

All previous versions of PyTrinamic will still be available on PyPI and can be installed via: `pip install pytrinamic==0.1.27`.

## Contributing

We welcome pull requests! If you have major changes or questions about implementation, please open an issue first to discuss your ideas.

Please ensure contributed Python code adheres to the [PEP 8](https://peps.python.org/pep-0008/) Python code style guide and the [PEP 257](https://peps.python.org/pep-0257/) style guide for docstrings.
If you want to express details in docstrings using a markup language, please use [reStructuredText](reStructuredText) like proposed in [PEP 287](https://peps.python.org/pep-0287/) and when documenting parameters, variables, attributes, exceptions use the [Sphinx style](https://www.sphinx-doc.org/en/master/usage/domains/python.html#info-field-lists).

Additionally, please use double quotes (") for string constants.


## License

PyTrinamic is licensed under the MIT License.