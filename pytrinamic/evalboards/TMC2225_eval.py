from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC2225
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC2225_eval(TMCLEval):
    """
    This class represents a TMC2225 Evaluation board.

    Communication is done over the TMCL commands writeDRV and readDRV. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """
    
    def __init__(self, connection, module_id=1):
        """
        Parameters:
            connection:
                Type: class
                A class that provides the necessary functions for communicating
                with a TMC2225. The required functions are
                    connection.writeDRV(registerAddress, value, moduleID)
                    connection.readDRV(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC2225.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2225. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC2225()]

    # Use the driver controller channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_drv(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_drv(register_address, self._module_id, signed)

    # Motion control functions

    def rotate(self, motor, value):
        self._connection.rotate(motor, value)

    def stop(self, motor):
        self._connection.stop(motor)

    def move_to(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.motors[motor].set_axis_parameter(self.motors[motor].AP.MaxVelocity, velocity)
        self._connection.move(motor, position, self._module_id)

#    def moveBy(self, motor, distance, velocity):
#        if not(0 <= motor < self.MOTORS):
#            raise ValueError

#        position = self.readRegister(self.registers.XACTUAL, self.__channel, signed=True)

#        self.moveTo(motor, position + distance, velocity)

#        return position + distance

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        class AP:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            MaxCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            InternalRsense                 = 28
            MeasuredSpeed                  = 29
            StepDirSource                  = 50
            StepDirFrequency               = 51
            MicrostepResolution            = 140
            ChopperBlankTime               = 162
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            VSense                         = 179
            smartEnergyActualCurrent       = 180
            smartEnergyStallVelocity       = 181
            PWMThresholdSpeed              = 186
            PWMGrad                        = 187
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            FreewheelingMode               = 204
