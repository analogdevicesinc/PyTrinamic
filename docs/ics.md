# ICs

## Structure

The following image shows a generalized UML diagram of a TMC IC.

![TMC IC structure](resources/ic.svg "TMC IC structure")

When using Trinamic ICs directly on the host platform, implementing scripts can
either use the IC object or the included motor objects of the IC, similar to
TMCL modules.  
In both cases, some kind of external implementation of the `read_register(...)`
and `write_register(...)` functions is required to read from / write to IC registers.
Typically, these boil down to read/write functions of chip-level communication,
like SPI or UART. Since this is highly platform dependent, it must be implemented
by the user in a `handler` object and used to construct the IC object.  
Every higher level register access function of the IC and its features will
use these functions to read and write registers.

Every IC consists of `REGISTERS`, `VARIANTS` and `FIELDS` classes.
These contain all the registers, register variants and bitfields of registers.
Registers are basically just 8-bit addresses. Variants are registers with changing
semantics, based on the selection in some other register.  
Fields are sub-values of registers. One register can consist of multiple fields,
or just one. Since registers are the smallest accessible unit, field access
involves reading a full register, masking and changing the value of the bitfield
and fully write the entire register back (*read-modify-write*).  
This is done by the `read_register_field(...)` and `write_register_field(...)` functions.
For this to work, the definition of register fields is a tuple consisting
of the corresponding register address, the mask of the field, and the shift value
for the LSB of the field.  
Additionally, ICs implement the `read_axis_field(...)` and `write_axis_field(...)` functions.
For multi-axis ICs these functions resolve axis-specific fields based on given
base field and axis number. For single-axis ICs, these functions just wrap
the normal register field access functions on the given field.

Every IC inherits the general `TMC_IC` class, providing general Trinamic IC functionality,
such as channel handling and field access as described above. The `channel` of an
IC is just an identifier used to differentiate between different ICs for handlers
in systems with multiple ICs. For this to work, the `channel` is also passed as
argument to the `handler.read_register(...)` and `handler.write_register(...)` functions,
which are implemented by the user. In single IC systems, this value can be ignored.

Similar to TMCL modules, ICs contain a list of motors, accessible via `MOTORS` attribute.
Additionally to working with the IC object directly, the motor object can be used
for axis-dependent parameter access and feature functions.
These motor objects are instances of internally defined motor classes, `MOTOR_0` and `MOTOR_1`
in the above example.
Each of these motor classes has its own set of features. The parameters and functions
for these features are implemented in and inherited from the corresponding feature classes,
i.e. `FeatureXIC`, `FeatureYIC`, `FeatureZIC`.
The features of a motor can be listed with the `motor.list_features(...)` function.
All feature functions and parameter accesses in IC features come down to
register field accesses in the given IC.

## Usage

### IC-level usage

The following code snipped shows the principle of using the IC object to
work with ICs on IC-level.  
Change used IC `TMC5130` to your preferences. `X` is just a placeholder field.
`handler` object is intended to have the platform-specific `read_register(...)`
and `write_register(...)` functions implemented.

```Python
from pytrinamic2.ic.TMC5130.TMC5130 import TMC5130

class Handler(object):
  def read_register(self, channel, address, signed=False):
    # Platform specific implementation (SPI, UART, ...)
    pass
  def write_register(self, channel, address, value):
    # Platform specific implementation (SPI, UART, ...)
    pass

handler = Handler()
channel = 0
ic = TMC5130(handler, channel)

ic.write_register_field(ic.FIELDS.X, 42)
ic.read_register_field(ic.FIELDS.X)
```

After importing the required Python module, and given that the `handler` is
correctly implemented, the IC object can be used to read or write to registers.

### Motor-level usage

The following code snipped shows the principle of using the motor object to
work with ICs on motor-level.  
Change used IC `TMC5130` to your preferences. `X` is just a placeholder field.
`handler` object is intended to have the platform-specific `read_register(...)`
and `write_register(...)` functions implemented.

```Python
from pytrinamic2.ic.TMC5130.TMC5130 import TMC5130

class Handler(object):
  def read_register(self, channel, address, signed=False):
    # Platform specific implementation (SPI, UART, ...)
    pass
  def write_register(self, channel, address, value):
    # Platform specific implementation (SPI, UART, ...)
    pass

handler = Handler()
channel = 0
ic = TMC5130(handler, channel)
motor = ic.MOTOR[0]

# Feature parameters
motor.set_axis_field(ic.FIELDS.X, 42)
motor.FeatureX.set_x(42)
motor.FeatureX.x = 42
```

After importing the required Python module, given that the `handler` is
correctly implemented, the motor object can be accessed from the instantiated IC object.

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
