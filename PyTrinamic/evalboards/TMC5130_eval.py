'''
Created on 09.01.2019

@author: LK, ED, LH
'''

from PyTrinamic.evalboards.TMC_EvalBoard import TMC_EvalBoard
from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130

class TMC5130_eval(TMC_EvalBoard):
    """
    This class represents a TMC5130 Evaluation board.

    Communication is done over the TMCL commands writeMC and readMC. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """

    __PIN_MAP = [
        # (pin_ic, pin_board)
        (2, 15),
        (3, 22),
        (4, 23),
        (5, 24),
        (7, 25),
        (8, 9),
        (9, 10),
        (23, 4),
        (24, 6),
        (25, 5),
        (26, 30),
        (27, 29),
        (28, 28)
    ]

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id, TMC5130(self, 0), self.EVAL_TYPES.MOTION_CONTROLLER)
