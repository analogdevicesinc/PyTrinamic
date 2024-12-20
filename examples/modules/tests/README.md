
The test scripts located in this directory dry test the example scripts.
The interface to the hardware is mocked away on the `tmcl_module_interface` level.
Also the `time.sleep()` function is mocked away with an empty implementation so the tests run faster.

To run the tests:

* Install PyTrinamic via `python -m pip install -e <path-to-the-pytrinamic-repo>`
* Install `pytest`
* Call `pytest` from the terminal within this directory or from within the above directories.