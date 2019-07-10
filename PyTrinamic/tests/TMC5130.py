import openhtf as htf
from openhtf.output.callbacks import json_factory
from openhtf.plugs import user_input
from openhtf.util import conf

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.cli import select_com_port_by_name

class test_TMC5130(object):
    __VERSION = "1.0.0"
    def __init__(self):
        self.test = htf.Test(self.connectivity.with_args(_self=self), self.registers.with_args(_self=self),
            test_name="TMC5130 IC test", test_description="TMC5130 IC general test", test_version=self.__VERSION)
        self.test.add_output_callbacks(json_factory.OutputToJSON('./{dut_id}.TMC5130.json', indent=2))
        self.interface = None
        self.tmc5130 = None
        self.register_repititions = 0
    def execute(self):
        self.test.execute(test_start=user_input.prompt_for_test_start())
    @htf.measures(htf.Measurement('connectivity_measurement'))
    def connectivity(test, _self):
        test.logger.info("Instantiating interface")
        _self.interface = serial_tmcl_interface(PyTrinamic.getComPort(name=select_com_port_by_name(USB=True), return_default=False, USB=True))
        test.logger.info("Instantiating chip")
        _self.tmc5130 = TMC5130_eval(_self.interface)
        test.measurements.connectivity_measurement = 'Connectivity measurement stub'
    @htf.measures(htf.Measurement('registers_measurement'))
    def registers(test, _self):
        values = []
        test.logger.info(f"Register stability test #{_self.register_repititions}")
        for register in _self.tmc5130.registers.list:
            values.append(_self.tmc5130.readRegister(register))
            test.logger.debug("0x{:08X}: {}".format(register, values[-1]))
        test.measurements.registers_measurement = values
        _self.register_repititions = _self.register_repititions + 1

if __name__ == '__main__':
    test = test_TMC5130()
    test.execute()
