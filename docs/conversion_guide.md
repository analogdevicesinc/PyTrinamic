# Conversion guide

## Introduction

This guide outlines how to convert existing code based on legacy versions of this
library to be compatible to current versions.  
Whenever a new breaking change in the library is introduced, a new section
will be added here, explaining how to convert existing code using this library
to overcome these breaking changes.  
Each section gives the involved (master-)commit, so it is up to the user to identify
the commit range used in their local copy, and apply each conversion from bottom to top
subsequently, to update to the newest version.  
This is not intended to be used as a guide for entirely new code.

## Conversions

### Feature Hierarchy Rework

Commit: TBD

#### Involved parts

- ICs
- Modules
- EvalBoards

#### Outline

Entire mapping of hardware hierarchy has been reworked. The way of accessing parameters
has been unified and simplified for most use cases. Feature implementations have
been introduced via inheritance.

#### Conversion

##### Accessing registers

Previously, accessing registers of ICs was an exclusive feature of EvalBoards.
Now, registers can be accessed directly with the IC implementation, as long as
a handler is given. EvalBoards are just examples of such handlers. Users wanting
to directly communicate with the chip, have to implement this handler for their
platform and hand it over to the IC.

Previous:

```Python
eval.readRegister(0, eval.registers.X)
eval.writeRegister(0, eval.registers.X, 42)
```

Current:

```Python
# Communicating with IC directly, given that ic.handler is set
ic.read_register(0, ic.REGISTERS.X)
ic.write_register(0, ic.REGISTERS.X, 42)
```

```Python
# Communicating via EvalBoard
eval.read_register(0, eval.IC.REGISTERS.X)
eval.write_register(0, eval.IC.REGISTERS.X, 42)
```

##### Accessing axis parameters

Previous:

```Python
module.axisParameter(axis, module.AP.X)
module.setAxisParameter(axis, module.AP.X, 42)
```

Now there are several ways of accessing axis parameters, each for a specific use case.
It is up to the user to choose the best fitting.  
All of the below statements for setting/getting axis parameters are equivalent.

```Python
# Getting axis parameter directly from module
module.get_axis_parameter(module.MOTORS[axis].AP.X, axis)

# Getting axis parameter from the specific axis/motor
# motor = module.MOTORS[0]
motor.get_axis_parameter(motor.AP.X)

# Getting the axis parameter as grouped feature property
# motor = module.MOTORS[0]
motor.feature.X

# Getting the axis parameter as ungrouped feature property
# motor = module.MOTORS[0]
motor.X
```

```Python
# Setting axis parameter directly on module
module.set_axis_parameter(module.MOTORS[axis].AP.X, axis, 42)

# Setting axis parameter for the specific axis/motor
# motor = module.MOTORS[0]
motor.set_axis_parameter(motor.AP.X, 42)

# Setting the axis parameter as grouped feature property
# motor = module.MOTORS[0]
motor.feature.X = 42

# Setting the axis parameter as ungrouped feature property
# motor = module.MOTORS[0]
motor.X = 42
```
