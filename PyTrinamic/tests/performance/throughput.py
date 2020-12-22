'''
Test TMCL throughput.

Created on 19.12.2020

@author: LK
'''

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.TMCL import TMCL_Request, TMCL_Reply
import logging
import math
import time

MODULE_ID = 1
N_SAMPLES = 10000
PAYLOAD = 1
WORST_CASE_LATENCY = 50 # ms

min_time = 0
max_time = 0
avg_time = 0
std_dev_time = 0
n = 0

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

logger.info("Throughput test")

logger.info("Initializing interface.")
interface = ConnectionManagerPC.interactive().connect()[0]

logger.info("Performing test.")
while(n < N_SAMPLES):
    t = time.time()
    for i in range(0, PAYLOAD):
        interface.send_request_only(TMCL_Request(MODULE_ID, 1, 2, 3, 4, 5))
    try:
        for i in range(0, PAYLOAD):
            interface.receive_reply()
    except:
        pass
    delta = time.time() - t
    if(delta < (5 * PAYLOAD)):
        logger.debug("Measured delta time: {} s".format(delta))
        value = (2 * PAYLOAD) / delta
        if(n == 0):
            min_time = value
            max_time = value
            avg_time = value
            std_dev_time = 0
        else:
            min_time = min(min_time, value)
            max_time = max(max_time, value)
            avg_time_new = avg_time + ((value - avg_time) / (n + 1))
            std_dev_time = (((n - 1) * std_dev_time) + ((value - avg_time_new) * (value - avg_time))) / n
            avg_time = avg_time_new
        n += 1
    else:
        logger.debug("Timeout, not counting")

logger.info("Calculating statistical values.")
std_dev_time = math.sqrt(std_dev_time)

logger.info("Minimum: {} commands/s, Maximum: {} commands/s, Mean: {} commands/s, Standard deviation: {} commands/s".format(min_time, max_time, avg_time, std_dev_time))
