import openhtf as htf
from openhtf.output.callbacks import json_factory
from openhtf.plugs import user_input
from openhtf.util import conf

import logging
import argparse

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register

from PyTrinamic.tests.validators import ValuesEqualDict

class test_TMC5130_TMCL(object):
    __VERSION = "1.0.0"
    def __init__(self, cm):
        parser = argparse.ArgumentParser(description=self.__class__.__name__)
        parser.add_argument('--register-tests', dest='register_tests', action='store', nargs=1, type=int, default=[100],
                            help='Number of register stability tests to run (default: %(default)s)')

        args = parser.parse_known_args()[0]

        self.__test = htf.Test(self.connectivity.with_args(_self=self), self.registers.with_args(_self=self),
            test_name=self.__class__.__name__, test_description="TMC5130 IC general test", test_version=self.__VERSION)
        self.__test.add_output_callbacks(json_factory.OutputToJSON('./{dut_id}.{metadata[test_name]}.json', indent=2))
        self.__interface = None
        self.__cm = cm
        self.__register_tests = int(args.register_tests[0])
        self.__tmc5130 = None
        self.__register_repititions = 0
        self.__default_pins_repititions = 0
    def execute(self):
        self.__test.execute(test_start=user_input.prompt_for_test_start())
    @htf.measures(htf.Measurement('connectivity_measurement'))
    def connectivity(test, _self):
        test.logger.info("Instantiating interface")
        _self.__interface = _self.__cm.connect()
        test.logger.info("Instantiating chip")
        _self.__tmc5130 = TMC5130_eval(_self.__interface)
        test.measurements.connectivity_measurement = 'Connectivity measurement stub'
    @htf.measures(htf.Measurement('pin_default_states').ValuesEqualDict({
        
        TMC5130_register.IHOLD_IRUN  : 464643,
        TMC5130_register.MSLUT0      : 2863314260,
        TMC5130_register.MSLUT1      : 1251300522,
        TMC5130_register.MSLUT2      : 608774441,
        TMC5130_register.MSLUT3      : 269500962,
        TMC5130_register.MSLUT4      : 4227858431,
        TMC5130_register.MSLUT5      : 3048961917,
        TMC5130_register.MSLUT6      : 1227445590,
        TMC5130_register.MSLUT7      : 4211234,
        TMC5130_register.MSLUTSEL    : 4294934614,
        TMC5130_register.MSLUTSTART  : 1618739,
        TMC5130_register.MSCNT       : 0,
        TMC5130_register.MSCURACT    : 0
    }))
    def pin_state_default(test, _self):
        pin_states = {}

        _self.__interface.globalParameter()
    @htf.measures(htf.Measurement('registers').ValuesEqualDict({
        TMC5130_register.IHOLD_IRUN  : 464643,
        TMC5130_register.MSLUT0      : 2863314260,
        TMC5130_register.MSLUT1      : 1251300522,
        TMC5130_register.MSLUT2      : 608774441,
        TMC5130_register.MSLUT3      : 269500962,
        TMC5130_register.MSLUT4      : 4227858431,
        TMC5130_register.MSLUT5      : 3048961917,
        TMC5130_register.MSLUT6      : 1227445590,
        TMC5130_register.MSLUT7      : 4211234,
        TMC5130_register.MSLUTSEL    : 4294934614,
        TMC5130_register.MSLUTSTART  : 1618739,
        TMC5130_register.MSCNT       : 0,
        TMC5130_register.MSCURACT    : 0
    }))
    def registers(test, _self):
        values = {}
        test.logger.info(f"Register stability test #{_self.__register_repititions}")
        for register in _self.__tmc5130.registers.list:
            values[register] = _self.__tmc5130.readRegister(register)
            test.logger.debug("0x{:02X}: {}".format(register, values[register]))
        test.measurements.registers = values
        _self.__register_repititions = _self.__register_repititions + 1
        if(_self.__register_repititions < _self.__register_tests):
            return htf.PhaseResult.REPEAT

if __name__ == '__main__':
    test = test_TMC5130_TMCL(ConnectionManager())
    test.execute()
