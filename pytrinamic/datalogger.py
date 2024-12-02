"""Draft/Mockup for a new shiny RAMDebug implementation"""

from __future__ import annotations
from dataclasses import dataclass
import enum


class DataLogger:

    @dataclass
    class Info:
        base_frequency: int
        sample_limit: int
        number_of_channels: int

    class SignalType:
        pass

    class SignalTypeAp(SignalType):
        def __init__(self, index, axis=0):
            self.index = index
            self.axis = axis
    
    class SignalTypeRegister(SignalType):
        def __init__(self, address):
            self.address = address

    class TriggerType(enum.IntEnum):
        TRIGGER_UNCONDITIONAL         = 0
        TRIGGER_RISING_EDGE_SIGNED    = 1
        TRIGGER_FALLING_EDGE_SIGNED   = 2
        TRIGGER_DUAL_EDGE_SIGNED      = 3
        TRIGGER_RISING_EDGE_UNSIGNED  = 4
        TRIGGER_FALLING_EDGE_UNSIGNED = 5
        TRIGGER_DUAL_EDGE_UNSIGNED    = 6

    def __init__(self, connection):
        self._connection = connection
        self.signals = None
        self.prescaler = 0
        self.number_of_samples = None
        self.trigger_type = None
        self.result = {}

    def get_info(self) -> DataLogger.Info:
        pass

    def start(self) -> None:
        pass

    def has_stopped(self) -> bool:
        pass