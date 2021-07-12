# MotorControl feature

The MotorControl feature implements the basic functions to rotate and position
a motor.

This feature is inherited by all supported axes within modules and / or ICs.

## Axis parameters

There are no additional axis parameters for this feature.

## Register fields

There are no additional register fields for this feature.

## Feature parameters

There are no additional feature parameters for this feature.

## Feature functions

The MotorControl feature implements the basic functions to rotate and position
a motor.

### `rotate(self, velocity)`

#### Description

Rotates the motor with the given velocity.
Additional ramp parameters, such as acceleration, might have to be set using
the corresponding feature.

#### Parameters

| Parameter | Description |
| --- | --- |
| `self` | Motor object to be used with this function. |
| `velocity` | Velocity in module-specific units to rotate the motor with. |

#### Returns

`None`

### `stop(self)`

#### Description

Stops the current motion on the given motor.

#### Parameters

| Parameter | Description |
| --- | --- |
| `self` | Motor object to be used with this function. |

#### Returns

`None`

### `move_to(self, position, velocity=None)`

#### Description

Moves the motor with the given maximum velocity to the target position.
If no velocity is given, the currently externally configured velocity will be used.
Additional ramp parameters, such as acceleration, might have to be set using
the corresponding feature.

#### Parameters

| Parameter | Description |
| --- | --- |
| `self` | Motor object to be used with this function. |
| `position` | Target position in module-specific units to move to. |
| `velocity` | Maximum velocity in module-specific units to move the motor with. |

#### Returns

`None`

### `move_by(self, difference, velocity=None)`

#### Description

Moves the motor with the given maximum velocity by the given distance.
If no velocity is given, the currently externally configured velocity will be used.
Additional ramp parameters, such as acceleration, might have to be set using
the corresponding feature.

#### Parameters

| Parameter | Description |
| --- | --- |
| `self` | Motor object to be used with this function. |
| `difference` | Position difference in module-specific units to move the motor by. |
| `velocity` | Maximum velocity in module-specific units to move the motor with. |

#### Returns

`None`
