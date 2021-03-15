# This example is mainly to demonstrate the implemented feature-based approach
# together with the reworked hierarchy and motors.

# Imports

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.MotorManager import MotorManager
from PyTrinamic.evalboards.TMC5072_eval import TMC5072_eval
from PyTrinamic.features.LinearRamp import LinearRamp
from PyTrinamic.features.MotorControl import MotorControl
import time
import logging

# Initialize logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

# Initialize connection and module

# Select first available USB port as connection port
con = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]
eval = TMC5072_eval(con)

# Check if eval has required feature
if(eval.hasFeature(LinearRamp)):
    logger.debug("Eval has feature LinearRamp")
    # Rotate motors with eval- and parameter-approach
    logger.info("Rotate motors with eval- and parameter-approach")
    eval.setMaxAcceleration(0, 10000)
    eval.setMaxAcceleration(1, 10000)
    eval.setTargetVelocity(0, 10000)
    eval.setTargetVelocity(1, -10000)
    # Motors 1 and 2 of TMC5072 should rotate in different directions
    logger.info("Motors 1 and 2 of TMC5072 should rotate in different directions")
    time.sleep(5)
    eval.setTargetVelocity(0, 0)
    eval.setTargetVelocity(1, 0)

# Check if eval has required feature
if(eval.hasFeature(MotorControl)):
    logger.debug("Eval has feature MotorControl")
    # Rotate motors with eval- and functional-approach
    logger.info("Rotate motors with eval- and functional-approach")
    eval.rotate(0, 10000)
    eval.rotate(1, -10000)
    # Motors 1 and 2 of TMC5072 should rotate in different directions
    logger.info("Motors 1 and 2 of TMC5072 should rotate in different directions")
    time.sleep(5)
    eval.stop(0)
    eval.stop(1)

# Collect all motors from given modules.
# Here we have just the module 'eval', in the general case multiple motors can be listed.
motors = MotorManager.motors(eval)

# Check if motor has required feature
if(motors[0].hasFeature(LinearRamp)):
    logger.debug("motors[0] has feature LinearRamp")
    # Rotate Motor 1 of TMC5072 with motor- and parameter-approach
    logger.info("Rotate Motor 1 of TMC5072 with motor- and parameter-approach")
    # Notice that indexing is done implicitly, no 'axis' argument is required for the functions.
    motors[0].setMaxAcceleration(10000)
    motors[0].setMaxAcceleration(10000)
    # Motor 1 of TMC5072 should rotate

# Check if motor has required feature
if(motors[1].hasFeature(MotorControl)):
    logger.debug("motors[1] has feature MotorControl")
    # Rotate Motor 2 of TMC5072 with motor- and functional-approach
    logger.info("Rotate Motor 2 of TMC5072 with motor- and functional-approach")
    # Notice that indexing is done implicitly, no 'axis' argument is required for the functions.
    # The rotate definition is in the corresponding module.
    motors[1].rotate(-10000)
    # Motor 2 of TMC5072 should rotate

# Motors 1 and 2 of TMC5072 should rotate in different directions
time.sleep(5)
motors[0].stop()
motors[1].stop()

# Now, handle the feature-parameters for the motor directly via registers instead of APs like previously.
# For this, set the handler of the motor to the IC.
logger.debug("Available handlers for motor 0: {}".format(motors[0].handlers))
motors[0].handler = motors[0].handlers[1]

# Check if motor has required feature
if(motors[0].hasFeature(MotorControl)):
    # Rotate Motor 1 of TMC5072 with motor- and functional-approach directly by IC register read/write implementation.
    logger.info("Rotate Motor 1 of TMC5072 with motor- and functional-approach directly by IC register read/write implementation")
    # The rotate definition is in the corresponding IC.
    motors[0].rotate(10000)
    # Motor 1 of TMC5072 should rotate
    time.sleep(5)
    motors[0].stop()

logger.info("Example finished successfully.")
