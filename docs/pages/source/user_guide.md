# User Guide

## Eval System

Trinamic EVAL-boards are usually used together with a Trinamic Landungsbruecke interface board (or just Landungsbruecke) which implements a virtual serial TMCL protocol based communication on top of USB.

For every EVAL-board there is an EVAL-board class.
When an object of this class is created a TMCL interface object is required as first argument.

```py
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5240_eval

with ConnectionManager().connect() as lb_tmcl_iface:
    tmc5240_eval = TMC5240_eval(lb_tmcl_iface)
```

The Landungsbruecke firmware implements specific logic for each EVAL-board.
TMCL commands are used to interact with the Landungsbruecke and to make use of the EVAL-board specific logic.

Some TMCL commands are equal across many EVAL-boards.
For example the `ROR` command implements motor rotation for many stepper EVAL-boards. 
As in the above example code, instead of using the `lb_tmcl_iface` to send the `TMCLCommand.ROR` like this:
```py
    lb_tmcl_iface.send(TMCLCommand.ROR, ...)
```
The `TMC5240_eval` object provides a convenient alternative way of sending the `ROR` command:
```py
    tmc5240_eval.rotate(motor=0, value=51200)
```

## Module

Trinamic modules that implement TMCL can also be operated using PyTrinamic.
For every supported module there is module class.

Here we connect a TMCM-1636 using a Kvaser USB to CAN adapter.
```py
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636

with ConnectionManager("--interface kvaser_tmcl").connect() as my_interface:
    module = TMCM1636(my_interface)
```

The module object provides some convenient functions to make use of the module level functionality.
For example the function `get_analog_input()` can be used to read analog input values.
```py
    module.get_analog_input(0)
```
Under the hood the `get_analog_input()` send and receives the `GIO` TMCL command.

Further, the module object provides a list called `motor` to make use of axis level functionality.
```py
    motor0 = module.motors[0]
    max_current = motor0.get_axis_parameter(motor0.AP.MaxCurrent)
```
Under the hood the `get_axis_parameter()` send and receives the `GAP` TMCL command.

## IC

Work in progress ...

