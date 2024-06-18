################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""Testing the ramp module

Run this test using ether the command-line of the unittest framework [1] or simply call the script directly

[1]: https://docs.python.org/3/library/unittest.html#command-line-interface
"""

import time
import unittest
from unittest.mock import Mock, call

from pytrinamic.tools import VelocityRampRunner


class TestVelocityRampRunner(unittest.TestCase):
    """Contains the tests for the VelocityRampRunner"""

    def test_fixed_cycle_time(self):
        """Run a linear ramp and see if the velocity is updated as expected."""
        update_mock = Mock()
        ramp_runner = VelocityRampRunner(update_mock, update_cycle_time_ms=10)

        # call the method under test
        ramp_runner.run_linear_ramp(0, 100, 40)

        expected_velocity_update_calls = [call(0), call(25), call(50), call(75), call(100)]
        update_mock.assert_has_calls(expected_velocity_update_calls)

    def test_fixed_cycle_time_delay_time(self):
        """Run a linear ramp and see if the delay is plausible"""
        update_mock = Mock()
        ramp_runner = VelocityRampRunner(update_mock, update_cycle_time_ms=100)

        # call the method under test
        start_time = time.perf_counter()
        ramp_runner.run_linear_ramp(0, 100, 400)
        stop_time = time.perf_counter()

        delay_s = stop_time-start_time
        assert 0.35 < delay_s < 0.45

    def test_fixed_cycle_time_imprecise_25(self):
        """Run a linear ramp with an interval that is not a multiple of update_cycle_time_ms"""
        update_mock = Mock()
        ramp_runner = VelocityRampRunner(update_mock, update_cycle_time_ms=10)

        # call the method under test
        ramp_runner.run_linear_ramp(0, 100, 25)

        expected_velocity_update_calls = [call(0), call(40), call(80), call(100)]
        update_mock.assert_has_calls(expected_velocity_update_calls)

    def test_fixed_cycle_time_imprecise_35(self):
        """Run a linear ramp with an interval that is not a multiple of update_cycle_time_ms"""
        update_mock = Mock()
        ramp_runner = VelocityRampRunner(update_mock, update_cycle_time_ms=10)

        # call the method under test
        ramp_runner.run_linear_ramp(0, 100, 35)

        expected_velocity_update_calls = [call(0), call(28), call(57), call(85), call(100)]
        update_mock.assert_has_calls(expected_velocity_update_calls)

    def test_without_given_cycle_time(self):
        """Run a linear ramp and see if the velocity is updated as expected."""
        update_mock = Mock()
        ramp_runner = VelocityRampRunner(update_mock)

        # we mock the internal time method to emulate calls to time.time
        ramp_runner._time_ms = Mock()
        # the _time_ms method is about to return thees values
        ramp_runner._time_ms.side_effect = [10, 30, 50]

        # call the method under test
        ramp_runner.run_linear_ramp(0, 100, 40)

        expected_velocity_update_calls = [call(0), call(50), call(100)]
        update_mock.assert_has_calls(expected_velocity_update_calls)


if __name__ == "__main__":
    unittest.main()
