import openhtf as htf
from openhtf.output.callbacks import json_factory
from openhtf.plugs import user_input
from openhtf.util import conf

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.cli import select_com_port_by_name

@htf.measures(htf.Measurement('connectivity_measurement'))
def connectivity(test):
    myInterface = serial_tmcl_interface(PyTrinamic.getComPort(name=select_com_port_by_name(USB=True), USB=True))
    test.measurements.connectivity_measurement = 'Connectivity measurement stub'

if __name__ == '__main__':
    test = htf.Test(connectivity)
    test.add_output_callbacks(json_factory.OutputToJSON('./{dut_id}.TMC5130.json', indent=2))
    test.execute(test_start=user_input.prompt_for_test_start())
