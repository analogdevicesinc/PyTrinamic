################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic.evalboards as evalboards


def test_eval_creation():
    """Most basic test to check if the eval boards can be created."""
    evalboards.TMC2100_eval(None)
    evalboards.TMC2130_eval(None)
    evalboards.TMC2160_eval(None)

    evalboards.TMC2208_eval(None)
    evalboards.TMC2209_eval(None)
    evalboards.TMC2224_eval(None)
    evalboards.TMC2225_eval(None)
    evalboards.TMC2240_eval(None)

    evalboards.TMC2300_eval(None)

    evalboards.TMC2590_eval(None)

    evalboards.TMC2660_eval(None)

    evalboards.TMC4361_eval(None)

    evalboards.TMC4671_eval(None)

    evalboards.TMC5031_eval(None)
    evalboards.TMC5041_eval(None)
    evalboards.TMC5062_eval(None)
    evalboards.TMC5072_eval(None)

    evalboards.TMC5130_eval(None)
    evalboards.TMC5160_eval(None)
    evalboards.TMC5160_shield(None)

    evalboards.TMC5240_eval(None)
    evalboards.TMC5271_eval(None)
    evalboards.TMC5272_eval(None)

    evalboards.TMC6100_eval(None)
    evalboards.TMC6140_eval(None)

    evalboards.TMC6200_eval(None)

    evalboards.TMC6300_eval(None)

    evalboards.TMC7300_eval(None)

