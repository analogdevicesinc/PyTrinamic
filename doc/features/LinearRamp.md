# LinearRamp feature

The LinearRamp feature implements all functions and parameters required to
set up the linear ramp for the corresponding motor.

This feature is inherited by all supported axes within modules and / or ICs.

## Axis parameters

The LinearRamp feature requires the following axis parameters to be defined
in motors within modules as part of the `APs` class.

| Identifier | Description |
| --- | --- |
| `TargetPosition` | The desired target position in position mode. |
| `ActualPosition` | The actual position of the motor. Stop the motor before overwriting it. Should normally only be overwritten for reference position setting. |
| `TargetVelocity` | The desired speed in velocity mode. Not valid in position mode. |
| `ActualVelocity` | The actual speed of the motor. |
| `MaxVelocity` | The maximum speed used for positioning ramps. |
| `MaxAcceleration` | Maximum acceleration in positioning ramps. Acceleration and deceleration value in velocity mode. |

## Register fields

The LinearRamp feature requires the following register fields to be defined
in motors within ICs as part of the `FIELDS` class.

| Identifier | Description |
| --- | --- |
| `XTARGET` | Target position for ramp mode (signed). Write a new target position to this register in order to activate the ramp generator positioning in RAMPMODE=0. Initialize all velocity, acceleration and deceleration parameters before. |
| `XACTUAL` | Actual motor position (signed) Hint: This value normally should only be modified, when homing the drive. In positioning mode, modifying the register content will start a motion. |
| `VMAX` | Motion ramp target velocity (for positioning ensure VMAX = VSTART) (unsigned) This is the target velocity in velocity mode. It can be changed any time during a motion. |
| `VACTUAL` | Actual motor velocity from ramp generator (signed) The sign matches the motion direction. A negative sign means motion to lower XACTUAL. |
| `AMAX` | Second acceleration between V1 and VMAX (unsigned) This is the acceleration and deceleration value for velocity mode. |

## Feature parameters

The parameters for this feature can be accessed either by using the corresponding
setter / getter function or by reading from / writing to the property value `property` using
`motor.LinearRamp.property`.

| Property identifier | Axis parameter | Register field |
| --- | --- | --- |
| `target_position` | `TargetPosition` | `XTARGET` |
| `actual_position` | `ActualPosition` | `XACTUAL` |
| `target_velocity` | `TargetVelocity` | `VMAX` |
| `actual_velocity` | `ActualVelocity` | `VACTUAL` |
| `max_velocity` | `MaxVelocity` | `VMAX` |
| `max_acceleration` | `MaxAcceleration` | `AMAX` |

| Property identifier | Setter function | Getter function |
| --- | --- | --- |
| `target_position` | `set_target_position(position)` | `get_target_position()` |
| `actual_position` | `set_actual_position(position)` | `get_actual_position()` |
| `target_velocity` | `set_target_velocity(velocity)` | `get_target_velocity()` |
| `actual_velocity` | - | `get_actual_velocity()` |
| `max_velocity` | `set_max_velocity(velocity)` | `get_max_velocity()` |
| `max_acceleration` | `set_max_acceleration(acceleration)` | `get_max_acceleration()` |

## Feature functions

There are no additional feature functions for this feature.
