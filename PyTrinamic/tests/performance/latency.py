'''
Test TMCL latency.

Created on 19.12.2020

@author: LK
'''

from PyTrinamic.TMCL import TMCL_Request, TMCL_Reply
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
import logging
import math
import time

MODULE_ID = 1
N_SAMPLES = 10000

results = []

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

logger.info("Latency test")

logger.info("Initializing interface.")
interface = ConnectionManagerPC.interactive().connect()[0]

logger.info("Performing test.")
while(len(results) < N_SAMPLES):
    t = time.time()
    # send invalid (for all modules) TMCL Request
    reply = interface.send_request(TMCL_Request(MODULE_ID, 1, 2, 3, 4, 5))
    delta = (time.time() - t) * 1000
    if(delta < 5):
        logger.debug("Measured delta time: {} ms".format(delta))
        results.append(delta)

logger.info("Calculating statistical values.")
min_time = min(results)
max_time = max(results)
avg_time = (sum(results)) / len(results)
std_dev_time = math.sqrt(sum([((i - avg_time)**2) for i in results]) / (len(results) - 1))

logger.info("Minimum: {} ms, Maximum: {} ms, Mean: {} ms, Standard deviation: {} ms".format(min_time, max_time, avg_time, std_dev_time))
