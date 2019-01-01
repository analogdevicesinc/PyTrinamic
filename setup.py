'''
Created on 30.12.2018

@author: ED
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTrinamic",
    version="0.0.7",
    author="ED,..",
    author_email="tmc_info@trinamic.com",
    description="TRINAMIC's Python Technology Access Package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trinamic/PyTrinamic",
    packages=setuptools.find_packages(),
    py_modules=["PyTrinamic/connections/SerialInterface",
                "PyTrinamic/modules/TMCM_0010_OPC",
                "PyTrinamic/examples/TMCM-0010-OPC_config_check",
                "PyTrinamic/examples/TMCM-0010-OPC_config_update"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)