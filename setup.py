'''
Created on 30.12.2018

@author: ED
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTrinamic",
    version="0.1.3",
    author="ED, LK, LH, ..",
    author_email="tmc_info@trinamic.com",
    description="TRINAMIC's Python Technology Access Package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trinamic/PyTrinamic",
    packages=setuptools.find_packages(),
    py_modules=[
        "PyTrinamic/connections/connection_interface",
        "PyTrinamic/connections/serial_tmcl_interface",
        "PyTrinamic/connections/uart_ic_interface",
        "PyTrinamic/evalboards/eval_interface",
        "PyTrinamic/evalboards/TMC4671_eval",
        "PyTrinamic/evalboards/TMC4672_eval",
        "PyTrinamic/evalboards/TMC5041_eval",
        "PyTrinamic/evalboards/TMC5130_eval",
        "PyTrinamic/evalboards/TMC6200_eval",
        "PyTrinamic/ic/ic_interface",
        "PyTrinamic/ic/TMC4671/TMC4671_fields",
        "PyTrinamic/ic/TMC4671/TMC4671_register_variant",
        "PyTrinamic/ic/TMC4671/TMC4671_register",
        "PyTrinamic/ic/TMC4671/TMC4671",
        "PyTrinamic/ic/TMC4672/TMC4672_fields",
        "PyTrinamic/ic/TMC4672/TMC4672_register_variant",
        "PyTrinamic/ic/TMC4672/TMC4672_register",
        "PyTrinamic/ic/TMC4672/TMC4672",
        "PyTrinamic/ic/TMC5041/TMC5041_fields",
        "PyTrinamic/ic/TMC5041/TMC5041_register_variant",
        "PyTrinamic/ic/TMC5041/TMC5041_register",
        "PyTrinamic/ic/TMC5041/TMC5041",
        "PyTrinamic/ic/TMC5130/TMC5130_fields",
        "PyTrinamic/ic/TMC5130/TMC5130_register_variant",
        "PyTrinamic/ic/TMC5130/TMC5130_register",
        "PyTrinamic/ic/TMC5130/TMC5130",
        "PyTrinamic/ic/TMC6200/TMC6200_fields",
        "PyTrinamic/ic/TMC6200/TMC6200_register_variant",
        "PyTrinamic/ic/TMC6200/TMC6200_register",
        "PyTrinamic/ic/TMC6200/TMC6200",
        "PyTrinamic/modules/TMCM_0010_OPC",
        "PyTrinamic/modules/TMCM_1160",
        "PyTrinamic/modules/TMCM_1640",
        "PyTrinamic/helpers"
    ],
    scripts=[
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_ABN_encoder_offset_estimation.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6200_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6200_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC4672/TMC4672_eval_template.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_stallGuardDemo.py",
        "PyTrinamic/examples/evalboards/TMC5130/TMC5130_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5130/TMC5130_MicroStep.py",
        "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM-0010-OPC_config_check.py",
        "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM-0010-OPC_config_update.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_hall_positioning_test.py",
        "PyTrinamic/examples/tools/FirmwareUpdate.py",
        "PyTrinamic/examples/ShowAvailableCOMPorts.py"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    zip_safe=False,
)
