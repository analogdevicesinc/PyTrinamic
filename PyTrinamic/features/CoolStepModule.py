from PyTrinamic.features.feature import Feature, FeatureProvider
from PyTrinamic.features.CoolStep import CoolStep
import time


class CoolStepModule(CoolStep, FeatureProvider):
    """
    StallGuard2 feature implementation for modules
    """
    class __GROUPING(CoolStep, FeatureProvider):

        def __init__(self, parent):
            """
            Constructor for the feature grouping instance.

            Parameters:
            parent: Parent instance. This is the Feature itself aswell as its
            descendants.
            """
            self.parent = parent

        def set_current_minimum(self, current):
            """
            Sets the smartEnergy current minimum.
            Stored in axesparameter SEIMIN 
            Parameters:
            axis: Axis index.
            current: smartEnergy current minimum.
            """
            self.parent.set_axis_parameter(self.parent.AP.SEIMIN, current)

        def set_current_down_step(self, step):
            """
            Sets the smartEnergy current down step.

            Parameters:
            axis: Axis index.
            step: smartEnergy current down step.
            """
            self.parent.set_axis_parameter(self.parent.AP.SECDS, step)

        def set_current_up_step(self, step):
            """
            Sets the smartEnergy current up step.

            Parameters:
            axis: Axis index.
            step: smartEnergy current up step.
            """
            self.parent.set_axis_parameter(self.parent.AP.SECUS, step)

        def set_hysteresis(self, hysteresis):
            """
            Sets the smartEnergy hysteresis.

            Parameters:
            axis: Axis index.
            hysteresis: smartEnergy hysteresis.
            """
            self.parent.set_axis_parameter(self.parent.AP.SmartEnergyHysteresis, hysteresis)

        def set_hysteresis_start(self, hysteresis_start):
            """
            Sets the smartEnergy hysteresis start.

            Parameters:
            axis: Axis index.
            hysteresis_start: smartEnergy hysteresis start .
            """
            self.parent.set_axis_parameter(self.parent.AP.SmartEnergyHysteresisStart, hysteresis_start)

        def set_threshold_speed(self, speed):
            """
            Sets the smartEnergy speed threshold.

            Parameters:
            axis: Axis index.
            speed: smartEnergy threshold speed.
            """
            self.parent.set_axis_parameter(self.parent.AP.SmartEnergyThresholdSpeed, speed)

        def set_slow_run_current(self, current):
            """
            Sets the smartEnergy slow run current.

            Parameters:
            axis: Axis index.
            current: smartEnergy slow run current
            """
            self.parent.set_axis_parameter(self.parent.AP.SmartEnergySlowRunCurrent, current)
        
        def get_current_minimum(self):
            """
            Gets the smartEnergy current minimum.
            Stored in axesparameter SEIMIN 

            Returns: 
            smartEnergy current minimum.
            """
            return self.parent.get_axis_parameter(self.parent.AP.SEIMIN)

        def get_current_down_step(self):
            """
            Gets the smartEnergy current down step.

            Returns: 
            smartEnergy current down step.
            """
            return self.parent.get_axis_parameter(self.parent.AP.SECDS)

        def get_current_up_step(self):
            """
            Gets the smartEnergy current up step.

            Returns:
            smartEnergy current up step.
            """
            return self.parent.get_axis_parameter(self.parent.AP.SECUS)

        def get_hysteresis(self):
            """
            Gets the smartEnergy hysteresis.

            Returns:
            smartEnergy hysteresis.
            """
            return self.parent.get_axis_parameter(self.parent.AP.SmartEnergyHysteresis)

        def get_hysteresis_start(self):
            """
            Gets the smartEnergy hysteresis start.

            Returns:
            smartEnergy hysteresis start .
            """
            return self.parent.get_axis_parameter(self.parent.AP.SmartEnergyHysteresisStart)

        def get_threshold_speed(self):
            """
            Gets the smartEnergy speed threshold.

            Returns:
            smartEnergy threshold speed.
            """
            return self.parent.get_axis_parameter(self.parent.AP.SmartEnergyThresholdSpeed)

        def get_slow_run_current(self):
            """
            Gets the smartEnergy slow run current.
            
            Returns:
            smartEnergy slow run current
            """
            return self.parent.get_axis_parameter(self.parent.AP.SmartEnergySlowRunCurrent)
        
        def calibrate(self, threshold = 0):
            """
            Interactive calibration function. 
            Takes threshold as optional input. 
            Sets parameter automatically 

            """
            self.parent.StallGuard2.calibrate_middle()

            print("Now, apply some load to the motor, at which you want the current to increase automatically.")
            input("Press enter to continue ...")

            for i in range(3):
                print("Starting calibration in "+ str(3-i) + "seconds.")
                time.sleep(1.0)
            
            hstart = int(round((self.parent.StallGuard2.get_load_value() / 1023) * 15, 0))
            print("Hysteresis start:"+ str(hstart))

            print("Now, release the load. Let the motor run freely.")
            input("Press enter to continue ...")

            hend = int(round((self.parent.StallGuard2.get_load_value() / 1023) * 15, 0))
            print("Hysteresis end: " + str(hend))

            hwidth = hend - hstart
            print("Hysteresis window width: " + str(hwidth))

            self.parent.CoolStep.hysteresis = hwidth
            self.parent.CoolStep.hysteresisStart = hstart
            self.parent.CoolStep.threshold_speed = threshold

        def __str__(self):
            return "{} {}".format(
                "CoolStep",
                {
                    "current minimum": self.current_minimum,
                    "current down step": self.current_down_step,
                    "current up step": self.current_up_step,
                    "hysteresis": self.hysteresis,
                    "hysteresis_start": self.hysteresis_start,
                    "threshold_speed": self.threshold_speed,
                    "slow_run_current": self.slow_run_current,
                }
            )
        
        current_minimum = property(get_current_minimum, set_current_minimum)
        current_down_step = property(get_current_down_step, set_current_down_step)
        current_up_step = property(get_current_up_step, set_current_up_step)
        hysteresis = property(get_hysteresis, set_hysteresis)
        hysteresis_start = property(get_hysteresis_start, set_hysteresis_start)
        threshold_speed = property(get_threshold_speed, set_threshold_speed)
        slow_run_current = property(get_slow_run_current, set_slow_run_current)

    # Feature initialization
    def __init__(self):
        self.CoolStep = self.__GROUPING(self)
