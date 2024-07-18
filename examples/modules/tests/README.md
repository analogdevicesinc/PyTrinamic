
The test scripts located in this directory dry test the example scripts.
The interface to the hardware is mocked away on the `tmcl_module_interface` level.
Also the `time.sleep()` function is mocked away with an empty implementation so the tests run faster.

To run the tests:

* install PyTrinamic via `python -m pip install -e <path-to-the-pytrinamic-repo>`
* install `pytest`
* go into this directory and call `pytest` from the terminal