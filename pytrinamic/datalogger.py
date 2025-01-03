"""Draft/Mockup for a new shiny RAMDebug implementation"""

from __future__ import annotations
from dataclasses import dataclass
import enum


class DataLogger:

    @dataclass
    class Info:
        base_frequency_hz: int
        sample_limit: int
        number_of_channels: int

    class SignalType:
        pass

    class SignalTypeAp(SignalType):
        def __init__(self, index, axis=0):
            self.index = index
            self.axis = axis
    
    class SignalTypeRegister(SignalType):
        def __init__(self, channel, address):
            self.channel = channel
            self.address = address

    @dataclass
    class Data:
        rate_hz: float
        samples: list

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
        self.data = None
        self.down_sampling_factor = 0
        self.samples_per_channel = None
        self.trigger_type = None
        self.data = {}

    def get_info(self) -> DataLogger.Info:
        pass

    def log_data(self, data: dict) -> None:
        pass

    def activate_trigger(self) -> None:
        pass

    def got_triggered(self) -> bool:
        pass

    def is_done(self) -> bool:
        pass

    def download_data(self) -> None:
        pass