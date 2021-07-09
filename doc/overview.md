# Overview

## Structure

The following table summarizes the different parts of this library.

| Part | Description |
| --- | --- |
| `doc` | Project documentation. Folder containing this file. |
| `PyTrinamic` | Library folder. This should be used in implementation projects. |
| `PyTrinamic/connections` | Connection interfaces and ConnectionManager. TMCL-compatible interfaces derive from `tmcl\_interface`. Specific implementations are intended to be used with standard computers only. |
| `PyTrinamic/evalboards` | EvalBoard modules. They provide direct register access to the used ICs. |
| `PyTrinamic/examples` | Example scripts utilizing this library. They are intended to be used with standard computers only. |
| `PyTrinamic/features` | Implementations for different feature blocks of axes for modules and ICs. |
| `PyTrinamic/ic` | ICs with registers and register fields. |
| `PyTrinamic/modules` | Modules with global and axis parameters. |
| `PyTrinamic/referencedesigns` | Module reference designs. Also using global and axis parameters. |
| `PyTrinamic/tests` | Tests. |

## Intended use

This library is intended to be used with Trinamic hardware. The target platform to use this
library directly is a standard computer running CPython. This is mainly due to
required drivers for several connection interfaces and platform-dependend example scripts.  
However, all other parts of this library are designed to be platform independend.
The library can be used with and integrated into other projects, as long as
suitable connection interfaces are provided. Then, all modules and ICs can be accessed as intended.

## Supported hardware

For Trinamic hardware, we differentiate between ICs, modules and EvalBoards.  

ICs are the lowest level of hardware abstraction and are generally included into bigger hardware,
but can also be used directly with this library, if the required functions are provided.
They can be accessed via specific interface types, such as SPI and UART. As these are highly platform
dependend, they need to be implemented externally. To use the IC implementations of this library,
a `handler` is required as constructor parameter, providing `read_register(...)` and `write_register(...)` functions.  
For more information on how to use the ICs part of this library, take a look into [IC documentation](ic.md).

Modules are complete hardware solutions using Trinamic ICs. They provide hardware abstraction
to the extend that they provide access to the individual axes, while hiding the
used specific ICs. The axis parameters for the individual axes can be accessed with
`get_axis_parameter(...)` and `set_axis_parameter(...)` either from the module object
or the motor object.  
Most of Trinamic's modules also support TMCL, the *Trinamic Motion Control Language*.
TMCL provides access to all of those parameters aswell as motion control (e.g. `ROL` - *Rotate left*, `ROR` - *Rotate right*)
and control flow.  
For more details on how to use the module part of this library, take a look into [module documentation](module.md).  
For more details on TMCL and the module you are using, look into the TMCL firmware documentation of your module.
It can be downloaded from the [Trinamic website](https://www.trinamic.com/products/modules/).

EvalBoards are special modules. They provide the same functionality as normal modules.
Additionally, they make the used ICs and its registers visible and accessible to external hosts.
This way, the IC can be evaluated directly without embedding it into complex hardware.
Multiple EvalBoards can be aggregated together on an evaluation platform, like *Landungsbruecke*,
which provides the required interfaces to the host, which uses this library.
The ICs within EvalBoards can be accessed as described above, with the corresponding
EvalBoard being the `handler`, providing the register access via TMCL.
