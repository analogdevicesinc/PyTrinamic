import math
import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM2611
from pytrinamic.tmcl import TMCLCommand


class AgvControl:
    """
    Instantiating this class connects to the AGV Board via USB.
    It then initializes encoders, motors, and goes to closed loop velocity mode.

    Attributes:
    - interface: USB interface instance to AGV board
    - module: AGV Board instance
    - motor_left, motor_right: Main instances for motor control. Left motor is also known as Axis 0 or Motor 1, Right motor is Axis 1 or Motor 2
    """

    # AGV Mechanical parameters
    AGV_WHEEL_DIAMETER = 14.0  # cm, diameter of one wheel
    AGV_WHEEL_PERIMETER = math.pi * AGV_WHEEL_DIAMETER
    AGV_WHEEL_WIDTH = 50.0  # cm, width of one wheel
    AGV_WHEEL_SPACING = 38.0  # cm, distance between center of the two wheels
    AGV_WHEEL_REDUCTION = 1.0 / 11.0  # ratio, input to output speed
    AGV_INVERT = True  # Set to true if AgvControl.driver_motors(speed, speed) results in rotation

    # AGV PID parameters, the velocity I parameter is bit shifted right by 8 by default
    AGV_TORQUE_P = 3200
    AGV_TORQUE_I = 200
    AGV_SPEED_P = 6500
    AGV_SPEED_I = 6000

    # AGV Motor parameters
    AGV_POLE_PAIRS = 3
    AGV_PEAK_CURRENT = 10000  # mA
    AGV_ABN_PPR = 16384  # Steps per turn
    AGV_MAX_SPEED = 5000  # rpm/s^2
    AGV_MAX_ACCEL = 1500  # rpm/s^2

    def __init__(self) -> None:
        # Connect to board and get left/right motor instances
        connection_manager = ConnectionManager()
        self.interface = connection_manager.connect()
        self.module = TMCM2611(self.interface)
        self.motor_left = self.module.motors[0]
        self.motor_right = self.module.motors[1]

        # Reverse one of the two motors direction
        if self.AGV_INVERT:
            self.motor_right.set_axis_parameter(
                self.motor_right.AP.MotorDirection, False
            )

        # Config motors using functions defined lower in this class
        self.__config_pid(
            self.motor_left,
            self.AGV_TORQUE_P,
            self.AGV_TORQUE_I,
            self.AGV_SPEED_P,
            self.AGV_SPEED_I,
        )
        self.__config_pid(
            self.motor_right,
            self.AGV_TORQUE_P,
            self.AGV_TORQUE_I,
            self.AGV_SPEED_P,
            self.AGV_SPEED_I,
        )
        self.__config_drive(self.motor_left)
        self.__config_drive(self.motor_right)

    def drive_motors(self, left_rpm, right_rpm):
        """
        Drive both agv motors with specified RPM.
        """
        self.motor_left.rotate(left_rpm)
        self.motor_right.rotate(right_rpm)

    def stop(self):
        """
        Set speed to 0 for both motors, which also disables the regulation.
        """
        self.drive_motors(0, 0)

    def translate(self, cm_per_s):
        """
        Translate robot at specified speed in centimeter per second
        """
        rpm = int(
            (cm_per_s * 60.0) / (self.AGV_WHEEL_PERIMETER * self.AGV_WHEEL_REDUCTION)
        )
        self.drive_motors(rpm, rpm)

    def rotate(self, rad_per_s):
        """
        Rotate robot at specified speed in radians per second
        """
        rpm = int(
            ((rad_per_s * self.AGV_WHEEL_SPACING / 2) * 60.0)
            / (self.AGV_WHEEL_PERIMETER * self.AGV_WHEEL_REDUCTION)
        )
        self.drive_motors(rpm, -rpm)

    def __config_drive(self, motor):
        """
        Configure drive settings, abn decoder unit, velocity calculation tweaks and velocity ramper.
        Then executes encoder initialization before going to closed loop velocity mode.
        When going to closed loop velocity mode, default PI values are used, but those are low and safe.
        Configure PI to achieve accurate positioning.
        """

        # Set general drive settings
        motor.drive_settings.pole_pairs = self.AGV_POLE_PAIRS
        motor.drive_settings.max_current = self.AGV_PEAK_CURRENT  # mA
        motor.drive_settings.open_loop_current = int(self.AGV_PEAK_CURRENT / 4)  # mA
        motor.drive_settings.target_reached_distance = 5
        motor.drive_settings.target_reached_velocity = 500  # RPM
        motor.drive_settings.motor_halted_velocity = 250  # RPM

        # Set encoder settings
        motor.abn_encoder.resolution = self.AGV_ABN_PPR
        motor.abn_encoder.direction = 1
        motor.abn_encoder.init_mode = motor.ENUM.ENCODER_INIT_MODE_0

        # Velocity:
        # Set scaler to shift I velocity coef by 8, this gives better resolution for setting the I parameter
        self.module.connection.write_register(
            0x61, TMCLCommand.WRITE_MC, motor._axis, 0x08
        )

        # Enable default biquad filter on speed, this does not appear to do much, probably improves the filtering a bit
        self.module.connection.write_register(
            0x24, TMCLCommand.WRITE_MC, motor._axis, True
        )

        # Set the minimum deviation register, this stops velocity calculation when the AGV is at standstill
        # Heavily reduces vibrations at standstill caused by high PI parameters.
        self.module.connection.write_register(
            0x2D, TMCLCommand.WRITE_MC, motor._axis, (0x000CBFFD)
        )

        # Configure ramp settings
        motor.linear_ramp.max_velocity = self.AGV_MAX_SPEED
        motor.linear_ramp.max_acceleration = self.AGV_MAX_ACCEL
        motor.linear_ramp.enabled = 1
        print(motor.linear_ramp)

        # Do encoder initialization
        motor.rotate(1)
        motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_OPENLOOP
        time.sleep(1)
        motor.rotate(0)
        motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_ABN_ENCODER
        time.sleep(1)

    def __config_pid(self, motor, torque_p, torque_i, velocity_p, velocity_i):
        """
        User settable PID configuration. Simply sets value of all controllers.
        """

        motor.pid.torque_p = torque_p
        motor.pid.torque_i = torque_i
        motor.pid.velocity_p = velocity_p
        motor.pid.velocity_i = velocity_i
        motor.pid.position_p = 0
        print(motor.pid)


if __name__ == "__main__":
    # Enable and init robot
    agv_robot = AgvControl()

    # Wait 1 second before starting canned routine
    time.sleep(1)

    # Driver forward and backwards at 10cm/s for 2 seconds forever
    while True:
        agv_robot.translate(10)
        time.sleep(2)
        agv_robot.translate(-10)
        time.sleep(2)
