# EvalBoards

## Structure

The following image shows a generalized UML diagram of an EvalBoard.

![EvalBoard structure](resources/eval.svg "EvalBoard structure")

EvalBoards are special modules. Indirectly, all EvalBoards inherit from
the `tmcl_module` class via the `TMC_EvalBoard` class.  
For more information on the module interface of this library, look into the
[modules documentation](modules.md).

Additionally, in contrast to normal modules, EvalBoards provide direct access to the underlying
ICs and its registers. In this case, the EvalBoard serves as `handler` as
discussed in the [ICs documentation](ics.md).

All EvalBoards inherit the general `TMC_EvalBoard` class, which implements
the `read_register(...)` and `write_register(...)` fields, translating
register accesses to TMCL commands, which are used to communicate with the
evaluation platform.

## Usage

The EvalBoard can be used either as a module with its motors or using the IC
and its motors.

### Module-level usage

The following code snipped shows the principle of using the EvalBoard object to
work with EvalBoard on module-level.  
Change `TMC5130_eval` and `usb_tmcl_interface` to your preferences. `X` is just a placeholder axis parameter.

```Python
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface

con = usb_tmcl_interface()
eval = TMC5130_eval(con)
axis = 0

eval.set_axis_parameter(eval.MOTORS[axis].APs.X, axis, 42)
eval.rotate(axis, 1000)
eval.stop(axis)

con.close()
```

After importing the required Python modules, the connection needs to be
initialized first. This is highly interface-specific, some interfaces might
need additional arguments, such as `port`, `datarate` etc.

With an interface initialized, the EvalBoard object can be constructed.

Having the EvalBoard object, all general and specific module functions can be used
directly from the object, i.e. `set_axis_parameter(...)` and `rotate(...)`.
The axis parameter definitions are motor-specific and thus defined within the
motor object for the given axis.

### Module-motor-level usage

The following code snipped shows the principle of using the motors within the EvalBoard object to
work with EvalBoard on motor-level.  
Change `TMC5130_eval` and `usb_tmcl_interface` to your preferences. `X` is just a placeholder axis parameter.

```Python
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface

con = usb_tmcl_interface()
eval = TMC5130_eval(con)
motor = eval.MOTORS[0]

# Feature parameters
motor.set_axis_parameter(motor.APs.X, 42)
motor.FeatureX.set_x(42)
motor.FeatureX.x = 42

motor.rotate(1000)
motor.stop()
```

After importing the required Python modules, the connection needs to be
initialized first. This is highly interface-specific, some interfaces might
need additional arguments, such as `port`, `datarate` etc.

With an interface initialized, the EvalBoard object can be constructed.

To abstract away from the specific EvalBoard, the motor objects for the desired axes
can be accessed via the `MOTORS` list and its members can be used directly. In the general case,
motors of multiple EvalBoards can be collected in lists in the implementation script. In the above example,
just one axis is used. All the general motor and feature functions are available
from the motor object without handling axis numbers.  
The features of a motor can be listed with `list_features(...)` function.  
The features of a motor are grouped into feature blocks, with its functions accessible
by `motor.FeatureX.function(...)`, `featureX` being an example feature and `function`
the feature-specific function to be called.  
Parameters for features are additionally accessible by either the corresponding
setter/getter functions or its *property*. Properties behave like variables
in script level, but accessing them invokes the corresponding setter/getter
function implicitly. In both cases, it comes down to axis parameters being
set/get in the module. This way, the *feature parameters* statements in the above
example are completely equivalent.

### IC-level usage

The following code snipped shows the principle of using the IC within the EvalBoard object to
work with the IC on the EvalBoard directly.  
Change `TMC5130_eval` and `usb_tmcl_interface` to your preferences. `X` is just a placeholder field.

```Python
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface

con = usb_tmcl_interface()
eval = TMC5130_eval(con)
ic = eval.IC

ic.write_register_field(ic.FIELDS.X, 42)
ic.read_register_field(ic.FIELDS.X)
```

After construction of the EvalBoard object with the underlying connection,
the IC can be directly accessed.
As in the above example, in this level direct access to fields is possible.

### IC-motor-level usage

The following code snipped shows the principle of using the motor interfaces of the IC within the EvalBoard object to
work directly with the attached motors, abstracting from the individual IC.  
Change `TMC5130_eval` and `usb_tmcl_interface` to your preferences. `X` is just a placeholder field.

```Python
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.connections.usb_tmcl_interface import usb_tmcl_interface

con = usb_tmcl_interface()
eval = TMC5130_eval(con)
ic = eval.IC
motor = ic.MOTOR[0]

# Feature parameters
motor.set_axis_field(ic.FIELDS.X, 42)
motor.FeatureX.set_x(42)
motor.FeatureX.x = 42
```

After construction of the EvalBoard object with the underlying connection,
the motor to be used and its features can directly be accessed.

To abstract away from the specific IC, the motor objects for the desired axes
can be accessed via the `MOTORS` list and its members can be used directly. In the general case,
motors of multiple ICs can be collected in lists in the implementation script. In the above example,
just one axis is used. All the general motor and feature functions are available
from the motor object without handling axis numbers or register fields.  
The features of a motor can be listed with `list_features(...)` function.  
The features of a motor are grouped into feature blocks, with its functions accessible
by `motor.FeatureX.function(...)`, `featureX` being an example feature and `function`
the feature-specific function to be called.  
Parameters for features are additionally accessible by either the corresponding
setter/getter functions or its *property*. Properties behave like variables
in script level, but accessing them invokes the corresponding setter/getter
function implicitly. In both cases, it comes down to register fields being
read from / written to the IC. This way, the *feature parameters* statements in the above
example are completely equivalent.
