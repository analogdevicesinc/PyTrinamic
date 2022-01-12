'''
Created on 19.10.2021

@author:JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.DriveSetting import DriveSetting


class DriveSettingModule(DriveSetting, FeatureProvider):

    class __GROUPING(DriveSetting, FeatureProvider):
        def __init__(self, parent):
            self.parent = parent
    
            self._hasCommutationMode = False 
            self._hasMotorType = False
            self._hasMotorPolePairs = False
            self._hasMotorPoles = False
            self._hasOpenLoopCurrent = False
            self._hasMaxCurrent = False
            self._hasVelocitySensorSelection = False 
            self._hasPositionSensorSelection = False 
            self._hasMotorHaltedVelocity = False
            self._hasTargetReachedDistance = False
            self._hasTargetReachedVelocity = False
            self._hasMicrostepResolution = False 
            self._hasReferenceSwitchTolerance = False 
            self._hasStandbyCurrent = False 
            self._hasBoostCurrent = False 

            if hasattr(parent.APs, "CommutationMode"):
                self._hasCommutationMode = True
            if hasattr(parent.APs, "MotorType"):
                self._hasMotorType = True
            if hasattr(parent.APs, "MotorPolePairs"):
                self._hasMotorPolePairs = True
            if hasattr(parent.APs, "MotorPoles"):
                self._hasMotorPoles = True
            if hasattr(parent.APs, "OpenLoopCurrent"):
                self._hasOpenLoopCurrent = True
            if hasattr(parent.APs, "MaxCurrent"):
                self._hasMaxCurrent = True
            if hasattr(parent.APs, "VelocitySensorSelection"):
                self._hasVelocitySensorSelection = True
            if hasattr(parent.APs, "PositionSensorSelection"):
                self._hasPositionSensorSelection = True
            if hasattr(parent.APs, "TargetReachedVelocity"):
                self._hasTargetReachedVelocity = True
            if hasattr(parent.APs, "TargetReachedDistance"):
                self._hasTargetReachedDistance = True
            if hasattr(parent.APs, "MotorHaltedVelocity"):
                self._hasMotorHaltedVelocity = True
            if hasattr(parent.APs, "MicrostepResolution"):
                self._hasMicrostepResolution = True
            if hasattr(parent.APs, "ReferenceSwitchTolerance"):
                self._hasReferenceSwitchTolerance = True
            if hasattr(parent.APs, "StandbyCurrent"):
                self._hasStandbyCurrent = True
            if hasattr(parent.APs, "BoostCurrent"):
                self._hasBoostCurrent = True
            
        def set_commutation_mode(self, mode):
            """
            Sets commutation mode that is used for this axis.
            This value is stored as CommutationMode axis parameter.

            Parameters:
            mode: commutation mode
            """
            if self._hasCommutationMode:
                self.parent.set_axis_parameter(self.parent.APs.CommutationMode, mode)

        def get_commutation_mode(self):
            """
            Gets commutation mode that is used for this axis.
            This value is stored in the  CommutationMode axis parameter.

            Returns: commutation mode
            """
            if self._hasCommutationMode:
                return self.parent.get_axis_parameter(self.parent.APs.CommutationMode)
            else:
                return None
        
        def set_motor_type(self, motor_type):
            """
            Sets motor type that is used for this axis.
            This value is stored as MotorType axis parameter.

            Parameters:
            type: motor type
            """
            if self._hasMotorType:
                self.parent.set_axis_parameter(self.parent.APs.MotorType, motor_type)

        def get_motor_type(self):
            """
            Gets motor type that is used for this axis.
            This value is stored in the  MotorType axis parameter.

            Returns: motor type
            """
            if self._hasMotorType:
                return self.parent.get_axis_parameter(self.parent.APs.MotorType)
            else:
                return None

        def set_pole_pairs(self, number):
            """
            Sets pole pairs that is used for this axis.
            This value is stored as MotorPolePairs axis parameter.

            Parameters:
            number:  pole pairs
            """
            if self._hasMotorPolePairs:
                self.parent.set_axis_parameter(self.parent.APs.MotorPolePairs, number)

        def get_pole_pairs(self):
            """
            Gets pole pairs that is used for this axis.
            This value is stored in the MotorPolePairs axis parameter.

            Returns: pole pairs
            """
            if self._hasMotorPolePairs:
                return self.parent.get_axis_parameter(self.parent.APs.MotorPolePairs)
            else:
                return None

        def set_poles(self, number):
            """
            Sets motor poles that are used for this axis.
            This value is stored as MotorPoles axis parameter.

            Parameters:
            number:  poles
            """
            if self._hasMotorPoles:
                self.parent.set_axis_parameter(self.parent.APs.MotorPoles, number)

        def get_poles(self):
            """
            Gets motor poles that are used for this axis.
            This value is stored in the MotorPoles axis parameter.

            Returns: poless
            """
            if self._hasMotorPoles:
                return self.parent.get_axis_parameter(self.parent.APs.MotorPoles)
            else:
                return None

        def set_open_loop_current(self, current):
            """
            Sets  open loop current that is used for this axis.
            This value is stored as OpenLoopCurrent axis parameter.

            Parameters:
            current:  open loop current
            """
            if self._hasOpenLoopCurrent:
                self.parent.set_axis_parameter(self.parent.APs.OpenLoopCurrent, current)

        def get_open_loop_current(self):
            """
            Gets open loop current that is used for this axis.
            This value is stored in the  OpenLoopCurrent axis parameter.

            Returns: open loop current
            """
            if self._hasOpenLoopCurrent:
                return self.parent.get_axis_parameter(self.parent.APs.OpenLoopCurrent)
            else:
                return None

        def set_max_current(self, current):
            """
            Sets maximum current that is used for this axis.
            This value is stored as MaxCurrent axis parameter.

            Parameters:
            current: maximum current
            """
            if self._hasMaxCurrent:
                self.parent.set_axis_parameter(self.parent.APs.MaxCurrent, current)

        def get_max_current(self):
            """
            Gets maximum current that is used for this axis.
            This value is stored in the  MaxCurrent axis parameter.

            Returns: maximum current
            """
            if self._hasMaxCurrent:
                return self.parent.get_axis_parameter(self.parent.APs.MaxCurrent)
            else:
                return None

        def set_standby_current(self, current):
            """
            Sets standby current that is used for this axis.
            This value is stored as StandbyCurrent axis parameter.

            Parameters:
            current: standby current
            """
            if self._hasStandbyCurrent:
                self.parent.set_axis_parameter(self.parent.APs.StandbyCurrent, current)

        def get_standby_current(self):
            """
            Gets standby current that is used for this axis.
            This value is stored in the StandbyCurrent axis parameter.

            Returns: standby current
            """
            if self._hasMaxCurrent:
                return self.parent.get_axis_parameter(self.parent.APs.StandbyCurrent)
            else:
                return None

        def set_boost_current(self, current):
            """
            Sets boost current that is used for this axis.
            This value is stored as BoostCurrent axis parameter.

            Parameters:
            current: boost current
            """
            if self._hasBoostCurrent:
                self.parent.set_axis_parameter(self.parent.APs.BoostCurrent, current)

        def get_boost_current(self):
            """
            Gets boost current that is used for this axis.
            This value is stored in the BoostCurrent axis parameter.

            Returns: boost current
            """
            if self._hasBoostCurrent:
                return self.parent.get_axis_parameter(self.parent.APs.BoostCurrent)
            else:
                return None

        def set_velocity_sensor(self, sensor):
            """
            Sets velocity sensor velocity for this axis.
            This value is stored as VelocitySensorSelection axis parameter.

            Parameters: 
            sensor: velocity sensor 
            """
            if self._hasVelocitySensorSelection:
                self.parent.set_axis_parameter(self.parent.APs.VelocitySensorSelection, sensor)

        def get_velocity_sensor(self):
            """
            Gets velocity sensor for this axis.
            This value is stored as VelocitySensorSelection axis parameter.

            Returns: velocity sensor
            """
            if self._hasVelocitySensorSelection:
                return self.parent.get_axis_parameter(self.parent.APs.VelocitySensorSelection)
            else:
                return None

        def set_position_sensor(self, sensor):
            """
            Sets position sensor velocity for this axis.
            This value is stored as PositionSensorSelection axis parameter.

            Parameters: 
            sensor: position sensor 
            """
            if self._hasPositionSensorSelection:
                self.parent.set_axis_parameter(self.parent.APs.PositionSensorSelection, sensor)

        def get_position_sensor(self):
            """
            Gets position sensor for this axis.
            This value is stored as PositionSensorSelection axis parameter.

            Returns: position sensor
            """
            if self._hasPositionSensorSelection:
                return self.parent.get_axis_parameter(self.parent.APs.PositionSensorSelection)
            else:
                return None
        
        def set_motor_halted_velocity(self, velocity): 
            """
            Sets motor halted velocity for this axis.
            This value is stored as MotorHaltedVelocity axis parameter.

            Parameters:
            velocity:  motor halted velocity
            """
            if self._hasMotorHaltedVelocity:
                self.parent.set_axis_parameter(self.parent.APs.MotorHaltedVelocity, velocity)

        def get_motor_halted_velocity(self): 
            """
            Gets motor halted velocity for this axis.
            This value is stored as MotorHaltedVelocity axis parameter.

            Returns: motor halted velocity
            """
            if self._hasMotorHaltedVelocity:
                return self.parent.get_axis_parameter(self.parent.APs.MotorHaltedVelocity)
            else:
                return None

        def set_target_reached_distance(self, distance): 
            """
            Sets target reached distance for this axis.
            This value is stored as TargetReachedDistance axis parameter.

            Parameters: 
            distance: target reached distance
            """
            if self._hasTargetReachedDistance:
                self.parent.set_axis_parameter(self.parent.APs.TargetReachedDistance, distance)

        def get_target_reached_distance(self): 
            """
            Gets target reached distance for this axis.
            This value is stored as TargetReachedDistance axis parameter.

            Returns: target reached distance
            """
            if self._hasTargetReachedDistance:
                return self.parent.get_axis_parameter(self.parent.APs.TargetReachedDistance)
            else:
                return None

        def set_target_reached_velocity(self, velocity): 
            """
            Sets target reached velocity for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Parameters:
            velocity:  target reached velocity
            """
            if self._hasTargetReachedVelocity:
                self.parent.set_axis_parameter(self.parent.APs.TargetReachedVelocity, velocity)

        def get_target_reached_velocity(self): 
            """
            Gets target reached velocity for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Returns: target reached velocity
            """
            if self._hasTargetReachedVelocity:
                return self.parent.get_axis_parameter(self.parent.APs.TargetReachedVelocity)
            else:
                return None

        def set_microstep_resolution(self, resolution): 
            """
            Sets microstep resolution for this axis.
            This value is stored as MicrostepResolution axis parameter.

            Parameters:
            resolution: microstep resolution
            """
            if self._hasMicrostepResolution:
                self.parent.set_axis_parameter(self.parent.APs.MicrostepResolution, resolution)

        def get_microstep_resolution(self): 
            """
            Gets microstep resolution for this axis.
            This value is stored as MicrostepResolution axis parameter.

            Returns: microstep resolution
            """
            if self._hasMicrostepResolution:
                return self.parent.get_axis_parameter(self.parent.APs.MicrostepResolution)
            else:
                return None
            
        def set_reference_switch_tolerance(self, tolerance): 
            """
            Sets reference switch tolerance for this axis.
            This value is stored as ReferenceSwitchTolerance axis parameter.

            Parameters:
            tolerance: reference switch tolerance 
            """
            if self._hasReferenceSwitchTolerance:
                self.parent.set_axis_parameter(self.parent.APs.ReferenceSwitchTolerance, tolerance)

        def get_reference_switch_tolerance(self): 
            """
            Gets reference switch tolerance for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Returns: reference switch tolerance 
            """
            if self._hasReferenceSwitchTolerance:
                return self.parent.get_axis_parameter(self.parent.APs.ReferenceSwitchTolerance)
            else:
                return None
        
        def __str__(self):
            values = "DriveSettings {"
            if self._hasCommutationMode: 
                values += "'commutation_mode': " + str(self.commutation_mode) + ", "

            if self._hasMotorType:
                values += "'motor_type': " + str(self.motor_type) + ", "

            if self._hasMotorPolePairs:
                values += "'pole_pairs': " + str(self.pole_pairs) + ", "

            if self._hasMotorPoles:
                values += "'poles': " + str(self.poles) + ", "

            if self._hasOpenLoopCurrent:
                values += "'open_loop_current': " + str(self.open_loop_current) + ", "

            if self._hasMaxCurrent:
                values += "'max_current': " + str(self.max_current)+", "

            if self._hasPositionSensorSelection:  
                values += "'position_sensor': " + str(self.position_sensor) + ", "

            if self._hasVelocitySensorSelection:
                values += "'velocity_sensor': " + str(self.velocity_sensor) + ", "

            if self._hasTargetReachedVelocity:
                values += "'target_reached_velocity': " + str(self.target_reached_velocity) + ", "

            if self._hasTargetReachedDistance:
                values += "'target_reached_distance': " + str(self.target_reached_distance) + ", "

            if self._hasMotorHaltedVelocity:
                values += "'motor_halted_velocity': " + str(self.motor_halted_velocity) + ", "

            if self._hasMicrostepResolution:
                values += "'microstep_resolution': " + str(self.microstep_resolution) + ", "

            if self._hasReferenceSwitchTolerance:
                values += "'reference_switch_tolerance': " + str(self.reference_switch_tolerance) + ", "
            
            if self._hasStandbyCurrent:
                values += "'standby_current': " + str(self.standby_current) + ", "
            
            if self._hasBoostCurrent:
                values += "'boost_current': " + str(self.boost_current) + ", "

            values = values[:-2]
            values += "}"
            return values

        commutation_mode = property(get_commutation_mode, set_commutation_mode)
        motor_type = property(get_motor_type, set_motor_type)
        pole_pairs = property(get_pole_pairs, set_pole_pairs)
        poles = property(get_poles, set_poles)
        open_loop_current = property(get_open_loop_current, set_open_loop_current)
        max_current = property(get_max_current, set_max_current)
        motor_halted_velocity = property(get_motor_halted_velocity, set_motor_halted_velocity)
        target_reached_distance = property(get_target_reached_distance, set_target_reached_distance)
        target_reached_velocity = property(get_target_reached_velocity, set_target_reached_velocity)
        velocity_sensor = property(get_velocity_sensor, set_velocity_sensor)
        position_sensor = property(get_position_sensor, set_position_sensor)
        microstep_resolution = property(get_microstep_resolution, set_microstep_resolution)
        reference_switch_tolerance = property(get_reference_switch_tolerance, set_reference_switch_tolerance)
        standby_current = property(get_standby_current, set_standby_current)
        boost_current = property(get_boost_current, set_boost_current)

    # Feature initialization
    def __init__(self):
        self.DriveSetting = self.__GROUPING(self)
