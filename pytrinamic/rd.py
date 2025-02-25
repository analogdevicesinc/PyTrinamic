################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from enum import IntEnum

from pytrinamic.tmcl import TMCLCommand


class Rd:

    class Channel(IntEnum):
        CAPTURE_DISABLED   = 0
        AXIS_PARAMETER     = 1
        REGISTER           = 2
        STACKED_REGISTER   = 3
        SYSTICK            = 4
        RAMDEBUG_PARAMETER = 5
        ANALOG_INPUT       = 6
        GLOBAL_PARAMETER   = 8

    class Info(IntEnum):
        MAX_CHANNELS       = 0
        BUFFER_ELEMENTS    = 1
        SAMPLING_FREQUENCY = 2
        CAPTURED_SAMPLES   = 3    

    class Trigger(IntEnum):
        UNCONDITIONAL         = 0
        RISING_EDGE_SIGNED    = 1
        FALLING_EDGE_SIGNED   = 2
        DUAL_EDGE_SIGNED      = 3
        RISING_EDGE_UNSIGNED  = 4
        FALLING_EDGE_UNSIGNED = 5
        DUAL_EDGE_UNSIGNED    = 6
        
    class TriggerType(IntEnum):
        UNCONDITIONAL         = 0
        RISING_EDGE_SIGNED    = 1
        FALLING_EDGE_SIGNED   = 2
        DUAL_EDGE_SIGNED      = 3
        RISING_EDGE_UNSIGNED  = 4
        FALLING_EDGE_UNSIGNED = 5
        DUAL_EDGE_UNSIGNED    = 6
    
    class _Command(IntEnum):
        INIT                        =  0
        SET_SAMPLE_COUNT            =  1
        SET_SAMPLING_SOURCE         =  2 # Placeholder
        SET_PRESCALER               =  3
        SET_CHANNEL                 =  4
        SET_TRIGGER_CHANNEL         =  5
        SET_SHIFT_MASK              =  6
        ENABLE_TRIGGER              =  7
        GET_STATE                   =  8
        GET_SAMPLE                  =  9
        GET_INFO                    = 10
        GET_CHANNEL_TYPE            = 11
        GET_CHANNEL_ADDRESS         = 12
        SET_PRETRIGGER_SAMPLE_COUNT = 13
        GET_PRETRIGGER_SAMPLE_COUNT = 14
        SET_PROCESS_FREQUENCY       = 15
        SET_TYPE                    = 16
        SET_EVAL_CHANNEL            = 17
        SET_ADDRESS                 = 18
        SET_TRIGGER_TYPE            = 19
        SET_TRIGGER_EVAL_CHANNEL    = 20
        SET_TRIGGER_ADDRESS         = 21

    class State(IntEnum):
        IDLE           = 0
        TRIGGER        = 1
        CAPTURE        = 2
        COMPLETE       = 3
        PRETRIGGER     = 4
    
    def __init__(self, connection, module_id):
        self._connection = connection
        self._module_id = module_id

    def _command(self, cmd_type: _Command, index: int, value: int) -> int:
        return self._connection.send(TMCLCommand.RAMDEBUG, cmd_type, index, value, self._module_id).value
    
    def get_state(self) -> int:
        return self._command(self._Command.GET_STATE, 0, 0)

    def get_info(self, info: Info) -> int:
        return self._command(self._Command.GET_INFO, 0, info)
    
    def get_sample(self, offset: int) -> int:
        return self._command(self._Command.GET_SAMPLE, 0, offset)
    
    def init(self) -> int:
        return self._command(self._Command.INIT, 0, 0)
    
    def set_sample_count(self, count: int) -> int:
        return self._command(self._Command.SET_SAMPLE_COUNT, 0, count)
    
    def set_prescaler(self, prescaler: int) -> int:
        return self._command(self._Command.SET_PRESCALER, 0, prescaler)
    
    def set_process_frequency(self, frequency: int) -> int:
        return self._command(self._Command.SET_PROCESS_FREQUENCY, 0, frequency)
    
    def set_channel(self, channel_type: Channel, select: int) -> int:
        return self._command(self._Command.SET_CHANNEL, channel_type, select)
    
    def set_shift_mask(self, shift: int, mask: int) -> int:
        return self._command(self._Command.SET_SHIFT_MASK, shift, mask)
    
    def set_pretrigger_sample_count(self, count: int) -> int:
        return self._command(self._Command.SET_PRETRIGGER_SAMPLE_COUNT, 0, count)
    
    def set_trigger_channel(self, channel_type: Channel, select: int) -> int:
        # The signal used for triggering does not need to be a signal sampled!
        return self._command(self._Command.SET_TRIGGER_CHANNEL, channel_type, select)

    def enable_trigger(self, trigger_type: Trigger, threshold: int) -> int:
        return self._command(self._Command.ENABLE_TRIGGER, trigger_type, threshold)