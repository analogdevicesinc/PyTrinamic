# StallGuard2 feature

The StallGuard2 feature implements all functions and parameters required to
set up StallGuard2 for the corresponding motor.

This feature is inherited by all supported axes within modules and / or ICs.

## Axis parameters

The StallGuard2 feature requires the following axis parameters to be defined
in motors within modules as part of the `APs` class.

| Identifier | Description |
| --- | --- |
| `SG2FilterEnable` | Enables the stallGuard2 filter for more precision of the movement. If set, reduces the measurement frequency to one measurement per four fullsteps. In most cases it is expedient to set the filtered mode before using coolStep. Use the standard mode for step loss detection. |
| `SG2Threshold` | This signed value controls stallGuard2 threshold level for stall output and sets the optimum measurement range for readout. A lower value gives a higher sensitivity. Zero is the starting value. A higher value makes stallGuard2 less sensitive and requires more torque to indicate a stall. |
| `SmartEnergyStallVelocity` | Velocity from which stop on stall feature is active. |

## Register fields

The StallGuard2 feature requires the following register fields to be defined
in motors within ICs as part of the `FIELDS` class.

| Identifier | Description |
| --- | --- |
| `SFILT` | Enables the stallGuard2 filter for more precision of the movement. If set, reduces the measurement frequency to one measurement per four fullsteps. In most cases it is expedient to set the filtered mode before using coolStep. Use the standard mode for step loss detection. |
| `SGT` | This signed value controls stallGuard2 level for stall output and sets the optimum measurement range for readout. A lower value gives a higher sensitivity. Zero is the starting value working with most motors. A higher value makes stallGuard2 less sensitive and requires more torque to indicate a stall. |
| `SG_STOP` | Enable stop by stallGuard2 (also available in dcStep mode). Disable to release motor after stop event. Attention: Do not enable during motor spin-up, wait until the motor velocity exceeds a certain value, where stallGuard2 delivers a stable result. This velocity threshold should be programmed using TCOOLTHRS. |
| `TCOOLTHRS` | This is the lower threshold velocity for switching on smart energy coolStep and stallGuard feature. (unsigned) Set this parameter to disable coolStep at low speeds, where it cannot work reliably. The stop on stall function (enable with sg_stop when using internal motion controller) and the stall output signal become enabled when exceeding this velocity. In non-dcStep mode, it becomes disabled again once the velocity falls below this threshold. TCOOLTHRS = TSTEP = THIGH: - coolStep is enabled, if configured - stealthChop voltage PWM mode is disabled TCOOLTHRS = TSTEP - Stop on stall and stall output signal is enabled, if configured. |

## Feature parameters

The parameters for this feature can be accessed either by using the corresponding
setter / getter function or by reading from / writing to the property value `property` using
`motor.StallGuard2.property`.

| Property identifier | Axis parameter | Register fields |
| --- | --- | --- |
| `filter` | `SG2FilterEnable` | `SFILT` |
| `threshold` | `SG2Threshold` | `SGT` |
| `stop_velocity` | `SmartEnergyStallVelocity` | `SG_STOP`, `TCOOLTHRS` |

| Property identifier | Setter function | Getter function |
| --- | --- | --- |
| `filter` | `set_filter(filter_enable)` | `get_filter()` |
| `threshold` | `set_threshold(threshold)` | `get_threshold()` |
| `stop_velocity` | `set_stop_velocity(velocity)` | `get_stop_velocity()` |

## Feature functions

There are no additional feature functions for this feature.
