# PyTrinamic

PyTrinamic is a Python package to set up and control TRINAMIC modules, evaluation boards and ICs via serial, USB or CAN interfaces.

The package is intended to automate tasks that are typically done manually with TRINAMICs [TMCL-IDE](https://www.trinamic.com/support/software/tmcl-ide/).

| ⚠️ Note that we changed the way PyTrinamic is used, please check out the [Migration Guide](#migration-guide)|
|------------------------------------------------------------------------------------------------------------|

## Install

Use pip to install PyTrinamic.

```
pip install pytrinamic
```

## Getting Started

Please have a look at the [code examples on GitHub](https://github.com/trinamic/PyTrinamic/tree/master/examples).

## Migration Guide<a id="migration-guide"></a>

Version 0.2.0 of PyTrinamic introduces several changes to the API. For those who want to convert code that uses an older version of PyTrinamic, we wrote a short [migration guide](https://github.com/trinamic/PyTrinamic/blob/master/docs/migration_guide.md).

All previous versions of PyTrinamic will still be available on PyPI and can be installed via: `pip install pytrinamic==0.1.27`.

## Contributing

Pull requests are welcome. For any major changes or questions regarding implementation, please open an issue to ask or discuss first.

## License

PyTrinamic is licensed under the MIT License.