import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM2611


class AgvBrakeDemo:
    """
    Instantiating this class connects to the AGV Board via USB.
    It then initializes brakes only, to test that functionality on its own

    Attributes:
    - interface: USB interface instance to AGV board
    - module: AGV Board instance
    - motor_left, motor_right: Main instances for motor control. Left motor is also known as Axis 0 or Motor 1, Right motor is Axis 1 or Motor 2
    """

    AGV_BRAKE_RELEASE_DUTY_CYCLE = 80  # % PWM
    AGV_BRAKE_HOLD_DUTY_CYCLE = 30  # % PWM
    AGV_BRAKE_RELEASE_DURATION = 150  # ms

    def __init__(self) -> None:
        # Connect to board and get left/right motor instances
        connection_manager = ConnectionManager()
        self.interface = connection_manager.connect()
        self.module = TMCM2611(self.interface)
        self.motor_left = self.module.motors[0]
        self.motor_right = self.module.motors[1]

        # Set brake parameters
        self.motor_right.set_axis_parameter(
            self.motor_right.AP.BrakeReleaseDuty, self.AGV_BRAKE_RELEASE_DUTY_CYCLE
        )
        self.motor_left.set_axis_parameter(
            self.motor_right.AP.BrakeReleaseDuty, self.AGV_BRAKE_RELEASE_DUTY_CYCLE
        )
        self.motor_right.set_axis_parameter(
            self.motor_right.AP.BrakeHoldDuty, self.AGV_BRAKE_HOLD_DUTY_CYCLE
        )
        self.motor_left.set_axis_parameter(
            self.motor_right.AP.BrakeHoldDuty, self.AGV_BRAKE_HOLD_DUTY_CYCLE
        )
        self.motor_right.set_axis_parameter(
            self.motor_right.AP.BrakeReleaseDuration, self.AGV_BRAKE_RELEASE_DURATION
        )
        self.motor_left.set_axis_parameter(
            self.motor_right.AP.BrakeReleaseDuration, self.AGV_BRAKE_RELEASE_DURATION
        )

    def brake(self, release_brakes: bool):
        """
        True to brake, false to drive
        """
        self.motor_right.set_axis_parameter(
            self.motor_right.AP.BrakeRelease, release_brakes
        )
        self.motor_left.set_axis_parameter(
            self.motor_right.AP.BrakeRelease, release_brakes
        )

    def brakes_check_state(self):
        """
        Returns a tuple of motor right, motor left brake states.
        Numbers to enum can be found in self.motor_right.ENUM.BRAKE_

        0 : Faulty
        1 : Ready
        2 : Applying max PWM
        3 : Applying hold PWM
        """
        return (
            self.motor_right.get_axis_parameter(self.motor_right.AP.BrakeState),
            self.motor_left.get_axis_parameter(self.motor_right.AP.BrakeState),
        )


if __name__ == "__main__":
    # Enable and init robot
    brake_demo = AgvBrakeDemo()

    # Wait 1 second before starting the demo
    time.sleep(1)

    # Print brake status
    print(brake_demo.brakes_check_state())

    # Release brakes and print status
    brake_demo.brake(True)
    print(brake_demo.brakes_check_state())

    # Wait 0.5s and print status again
    time.sleep(0.5)
    print(brake_demo.brakes_check_state())

    # Wait 5 more seconds and brake
    time.sleep(2)
    brake_demo.brake(False)
    print(brake_demo.brakes_check_state())
