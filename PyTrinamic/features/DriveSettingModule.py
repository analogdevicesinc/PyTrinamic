'''
Created on 19.10.2021

@author:JH
'''

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.DriveSetting import DriveSetting

class DriveSettingModule(DriveSetting,FeatureProvider):

    class __GROUPING(DriveSetting,FeatureProvider):
        def __init__(self, parent):
            self.parent = parent
    
            self._hasCommutationMode = False 
            self._hasMotorType = False
            self._hasMotorPolePairs = False
            self._hasOpenLoopCurrent = False
            self._hasMaxCurrent = False
            self._hasVelocitySensorSelection = False 
            self._hasPositionSensor = False 
            self._hasMotorHaltedVelocity = False
            self._hasTargetReachedDistance = False
            self._hasTargetReachedVelocity = False

            if hasattr(parent.APs, "CommutationMode"):
                self._hasCommutationMode = True
            if hasattr(parent.APs, "MotorType"):
                self._hasMotorType = True
            if hasattr(parent.APs, "MotorPolePairs"):
                self._hasMotorPolePairs = True
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
            
        def set_commutation_mode(self, mode):
            """
            Sets commutation mode current that is used for this axis.
            This value is stored as CommutationMode axis parameter.

            Parameters:
            mode: commutation mode
            """
            if self._hasCommutationMode:
                return self.parent.set_axis_parameter(self.parent.APs.CommutationMode,mode)
            else:
                return "Not supported"
        def get_commutation_mode(self):
            """
            Gets commutation mode current that is used for this axis.
            This value is stored in the  CommutationMode axis parameter.

            Returns: commutation mode
            """
            if self._hasCommutationMode:
                return self.parent.get_axis_parameter(self.parent.APs.CommutationMode)
            else:
                return "Not supported"
        
        def set_motor_type(self, type):
            """
            Sets motor type that is used for this axis.
            This value is stored as MotorType axis parameter.

            Parameters:
            type: motor type
            """
            if self._hasMotorType:
                return self.parent.set_axis_parameter(self.parent.APs.MotorType,type)
            else:
                return "Not supported"
        def get_motor_type(self):
            """
            Gets motor type that is used for this axis.
            This value is stored in the  MotorType axis parameter.

            Returns: motor type
            """
            if self._hasMotorType:
                return self.parent.get_axis_parameter(self.parent.APs.MotorType)
            else:
                return "Not supported"

        def set_pole_pairs(self, number):
            """
            Sets pole pairs that is used for this axis.
            This value is stored as MotorPolePairs axis parameter.

            Parameters:
            number:  pole pairs
            """
            if self._hasMotorPolePairs:
                return self.parent.set_axis_parameter(self.parent.APs.MotorPolePairs,number)
            else:
                return "Not supported"
        def get_pole_pairs(self):
            """
            Gets pole pairs that is used for this axis.
            This value is stored in the  MotorPolePairs axis parameter.

            Returns: pole pairs
            """
            if self._hasMotorPolePairs:
                return self.parent.get_axis_parameter(self.parent.APs.MotorPolePairs)
            else:
                return "Not supported"

        def set_open_loop_current(self, current):
            """
            Sets  open loop current that is used for this axis.
            This value is stored as OpenLoopCurrent axis parameter.

            Parameters:
            current:  open loop current
            """
            if self._hasOpenLoopCurrent:
                return self.parent.set_axis_parameter(self.parent.APs.OpenLoopCurrent, current)
            else:
                return "Not supported"
        def get_open_loop_current(self):
            """
            Gets open loop current that is used for this axis.
            This value is stored in the  OpenLoopCurrent axis parameter.

            Returns: open loop current
            """
            if self._hasOpenLoopCurrent:
                return self.parent.get_axis_parameter(self.parent.APs.OpenLoopCurrent)
            else:
                return "Not supported"

        def set_max_current(self, current):
            """
            Sets maximum current that is used for this axis.
            This value is stored as MaxCurrent axis parameter.

            Parameters:
            current: maximum current
            """
            if self._hasMaxCurrent:
                return self.parent.set_axis_parameter(self.parent.APs.MaxCurrent,current)
            else:
                return "Not supported"
        def get_max_current(self):
            """
            Gets maximum current that is used for this axis.
            This value is stored in the  MaxCurrent axis parameter.

            Returns: maximum current
            """
            if self._hasMaxCurrent:
                return self.parent.get_axis_parameter(self.parent.APs.MaxCurrent)
            else:
                return "Not supported"      

        def set_velocity_sensor(self, sensor):
            """
            Sets velocity sensor velocity for this axis.
            This value is stored as VelocitySensorSelection axis parameter.

            Parameters: 
            sensor: velocity sensor 
            """
            if self._hasVelocitySensorSelection:
                return self.parent.set_axis_parameter(self.parent.APs.VelocitySensorSelection,sensor)
            else:
                return "Not supported"
        def get_velocity_sensor(self):
            """
            Gets velocity sensor for this axis.
            This value is stored as VelocitySensorSelection axis parameter.

            Returns: velocity sensor
            """
            if self._hasVelocitySensorSelection:
                return self.parent.get_axis_parameter(self.parent.APs.VelocitySensorSelection)
            else:
                return "Not supported"

        def set_position_sensor(self, sensor):
            """
            Sets position sensor velocity for this axis.
            This value is stored as PositionSensorSelection axis parameter.

            Parameters: 
            sensor: position sensor 
            """
            if self._hasPositionSensorSelection:
                return self.parent.set_axis_parameter(self.parent.APs.PositionSensorSelection,sensor)
            else:
                return "Not supported"
        def get_position_sensor(self):
            """
            Gets position sensor for this axis.
            This value is stored as PositionSensorSelection axis parameter.

            Returns: position sensor
            """
            if self._hasPositionSensorSelection:
                return self.parent.get_axis_parameter(self.parent.APs.PositionSensorSelection)
            else:
                return "Not supported"
        
        def set_motor_halted_velocity(self, velocity): 
            """
            Sets motor halted velocity for this axis.
            This value is stored as MotorHaltedVelocity axis parameter.

            Parameters:
            velocity:  motor halted velocity
            """
            if self._hasPositionSensorSelection:
                return self.parent.set_axis_parameter(self.parent.APs.MotorHaltedVelocity, velocity)
            else:
                return "Not supported"
        def get_motor_halted_velocity(self): 
            """
            Gets motor halted velocity for this axis.
            This value is stored as MotorHaltedVelocity axis parameter.

            Returns: motor halted velocity
            """
            if self._hasMotorHaltedVelocity:
                return self.parent.get_axis_parameter(self.parent.APs.MotorHaltedVelocity)
            else:
                return "Not supported"

        def set_target_reached_distance(self, distance): 
            """
            Sets target reached distance for this axis.
            This value is stored as TargetReachedDistance axis parameter.

            Parameters: 
            distance: target reached distance
            """
            if self._hasTargetReachedDistance:
                self.parent.set_axis_parameter(self.parent.APs.TargetReachedDistance, distance)
            else:
                return "Not supported"
        def get_target_reached_distance(self): 
            """
            Gets target reached distance for this axis.
            This value is stored as TargetReachedDistance axis parameter.

            Returns: target reached distance
            """
            if self._hasTargetReachedDistance:
                return self.parent.get_axis_parameter(self.parent.APs.TargetReachedDistance)
            else:
                return "Not supported"

        def set_target_reached_velocity(self, velocity): 
            """
            Sets target reached velocity for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Parameters:
            velocity:  target reached velocity
            """
            if self._hasTargetReachedVelocity:
                self.parent.set_axis_parameter(self.parent.APs.TargetReachedVelocity, velocity)
            else:
                return "Not supported"
        def get_target_reached_velocity(self): 
            """
            Gets target reached velocity for this axis.
            This value is stored as TargetReachedVelocity axis parameter.

            Returns: target reached velocity
            """
            if self._hasTargetReachedVelocity:
                return self.parent.get_axis_parameter(self.parent.APs.TargetReachedVelocity)
            else:
                return "Not supported"

        commutation_mode = property(get_commutation_mode,set_commutation_mode)
        motor_type = property(get_motor_type,set_motor_type)
        pole_pairs = property(get_pole_pairs,set_pole_pairs)
        open_loop_current = property(get_open_loop_current,set_open_loop_current)
        max_current = property(get_max_current,set_max_current)
        motor_halted_velocity = property(get_motor_halted_velocity,set_motor_halted_velocity)
        target_reached_distance = property(get_target_reached_distance,set_target_reached_distance)
        target_reached_velocity = property(get_target_reached_velocity,set_target_reached_velocity)
        velocity_sensor = property(get_velocity_sensor,set_velocity_sensor)
        position_sensor = property(get_position_sensor,set_position_sensor)
        
    # Feature initialization
    def __init__(self):
        self.DriveSetting = self.__GROUPING(self)
