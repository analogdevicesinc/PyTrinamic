# Current feature

The Current feature implements all functions and parameters required to
set up the current settings for the corresponding motor.

This feature is inherited by all supported axes within modules and / or ICs.

## Axis parameters

The Current feature requires the following axis parameters to be defined
in motors within modules as part of the `APs` class.

| Identifier | Description |
| --- | --- |
| `RunCurrent` | Motor current used when motor is running. The maximum value is 255 which means 100% of the maximum current of the module. |
| `StandbyCurrent` | The current used when the motor is not running. The maximum value is 255 which means 100% of the maximum current of the module. This value should be as low as possible so that the motor can cool down when it is not moving. |

## Register fields

The Current feature requires the following register fields to be defined
in motors within ICs as part of the `FIELDS` class.

| Identifier | Description |
| --- | --- |
| `IRUN` | Motor run current (0=1/32...31=32/32) |
| `IHOLD` | Standstill current (0=1/32...31=32/32) In combination with stealthChop mode, setting IHOLD=0 allows to choose freewheeling or coil short circuit (passive braking) for motor stand still. |

## Feature parameters

The parameters for this feature can be accessed either by using the corresponding
setter / getter function or by reading from / writing to the property value `property` using
`motor.Current.property`.

| Property identifier | Axis parameter | Register field |
| --- | --- | --- |
| `run` | `RunCurrent` | `IRUN` |
| `standby` | `StandbyCurrent` | `IHOLD` |

| Property identifier | Setter function | Getter function |
| --- | --- | --- |
| `run` | `set_current_run(current)` | `get_current_run()` |
| `standby` | `set_current_standby(current)` | `get_current_standby()` |

## Feature functions

There are no additional feature functions for this feature.
