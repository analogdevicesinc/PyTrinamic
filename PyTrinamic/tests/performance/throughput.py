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
N_SAMPLES = 1000
PAYLOAD = 2
WORST_CASE_LATENCY = 50 # ms

results = []

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
while(len(results) < N_SAMPLES):
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
        results.append((2 * PAYLOAD) / delta)
    else:
        logger.debug("Timeout, not counting")

logger.info("Calculating statistical values.")
min_time = min(results)
max_time = max(results)
avg_time = sum(results) / len(results)
std_dev_time = math.sqrt(sum([((i - avg_time)**2) for i in results]) / (len(results) - 1))

logger.info("Minimum: {} commands/s, Maximum: {} commands/s, Mean: {} commands/s, Standard deviation: {} commands/s".format(min_time, max_time, avg_time, std_dev_time))
