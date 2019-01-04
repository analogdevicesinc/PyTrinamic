'''
Created on 30.12.2018

@author: ED
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTrinamic",
    version="0.0.9",
    author="ED,..",
    author_email="tmc_info@trinamic.com",
    description="TRINAMIC's Python Technology Access Package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trinamic/PyTrinamic",
    packages=setuptools.find_packages(),
    py_modules=["PyTrinamic/connections/serial_tmcl_interface",
                "PyTrinamic/connections/uart_ic_interface",
                "PyTrinamic/evalboards/TMC4671_eval",
                "PyTrinamic/examples/evalboards/TMC4671_eval_BLDC_ABN_encoder",
                "PyTrinamic/examples/evalboards/TMC4671_eval_BLDC_open_loop",
                "PyTrinamic/examples/ic/TMC4671_BLDC_ABN_encoder",
                "PyTrinamic/examples/modules/TMCM-0010-OPC_config_check",
                "PyTrinamic/examples/modules/TMCM-0010-OPC_config_update",
                "PyTrinamic/ic/TMC4671/TMC4671_mask_shift",
                "PyTrinamic/ic/TMC4671/TMC4671_register",
                "PyTrinamic/modules/TMCM_0010_OPC"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)