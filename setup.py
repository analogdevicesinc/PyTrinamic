'''
Created on 30.12.2018

@author: ED
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTrinamic",
    version="0.0.15",
    author="ED, LK,..",
    author_email="tmc_info@trinamic.com",
    description="TRINAMIC's Python Technology Access Package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trinamic/PyTrinamic",
    packages=setuptools.find_packages(),
    py_modules=["PyTrinamic/connections/connection_interface",
                "PyTrinamic/connections/serial_tmcl_interface",
                "PyTrinamic/connections/uart_ic_interface",
                "PyTrinamic/evalboards/eval_interface",
                "PyTrinamic/evalboards/TMC4671_eval",
                "PyTrinamic/evalboards/TMC4672_eval",
                "PyTrinamic/evalboards/TMC5130_eval",
                "PyTrinamic/examples/evalboards/TMC4671_eval_BLDC_ABN_encoder_offset_estimation",
                "PyTrinamic/examples/evalboards/TMC4671_eval_BLDC_ABN_encoder",
                "PyTrinamic/examples/evalboards/TMC4671_eval_BLDC_open_loop",
                "PyTrinamic/examples/evalboards/TMC5130_eval_register_dump",
                "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM-0010-OPC_config_check",
                "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM-0010-OPC_config_update",
                "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_encoder_analog_input_test",
                "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_encoder_positioning_test",
                "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_hall_digital_input_test",
                "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_hall_positioning_test",
                "PyTrinamic/ic/ic_interface",                
                "PyTrinamic/ic/TMC4671/TMC4671_mask_shift",
                "PyTrinamic/ic/TMC4671/TMC4671_register_variant",
                "PyTrinamic/ic/TMC4671/TMC4671_register",
                "PyTrinamic/ic/TMC4671/TMC4671",
                "PyTrinamic/ic/TMC4672/TMC4672_mask_shift",
                "PyTrinamic/ic/TMC4672/TMC4672_register_variant",
                "PyTrinamic/ic/TMC4672/TMC4672_register",
                "PyTrinamic/ic/TMC4672/TMC4672",
                "PyTrinamic/ic/TMC5130/TMC5130_mask_shift",
                "PyTrinamic/ic/TMC5130/TMC5130_register_variant",
                "PyTrinamic/ic/TMC5130/TMC5130_register",
                "PyTrinamic/ic/TMC5130/TMC5130",
                "PyTrinamic/modules/TMCM_0010_OPC",
                "PyTrinamic/modules/TMCM_1640",
                "PyTrinamic/helpers"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)