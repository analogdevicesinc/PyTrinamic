
import time
import canopen


class TmcmNode(canopen.RemoteNode):
    class ModeOfOperation:
        NO_MODE = 0
        PROFILE_POSITION_MODE = 1
        PROFILE_VELOCITY_MODE = 3
        HOMING_MODE = 6
        CYCLIC_SYNCHRONOUS_POSITION_MODE = 8
        CYCLIC_SYNCHRONOUS_VELOCITY_MODE = 9
        CYCLIC_SYNCHRONOUS_TORQUE_MODE = 10

    class Cmd:
        SHUTDOWN = 6
        SWITCH_ON = 7
        ENABLE_OPERATION = 15
        NEW_SET_POINT = 16
        FAULT_RESET = 128

    class StateMachineFault(Exception):
        pass

    def __init__(self, *args, **kwargs):
        super(TmcmNode, self).__init__(*args, **kwargs)

    def go_to_operation_enabled(self):
        # clear an eventually present fault
        state = self.get_state()
        if state == 'Fault':
            self.sdo[0x6040].raw = self.Cmd.FAULT_RESET
            while 1:
                state = self.get_state()
                if state == 'Switch on disable':
                    break
                time.sleep(1)
        sequence_from_state = {
            'Switch on disable': [(self.Cmd.SHUTDOWN, 'Ready to switch on'),
                                  (self.Cmd.SWITCH_ON, 'Switched on'),
                                  (self.Cmd.ENABLE_OPERATION, 'Operation enabled')],
            'Ready to switch on': [(self.Cmd.SWITCH_ON, 'Switched on'),
                                   (self.Cmd.ENABLE_OPERATION, 'Operation enabled')],
            'Switched on': [(self.Cmd.ENABLE_OPERATION, 'Operation enabled')],
            'Operation enabled': [],
        }
        # go up the state machine states
        for cmd, expected_status in sequence_from_state[state]:
            self.sdo[0x6040].raw = cmd
            time.sleep(0.1)
            while 1:
                state = self.get_state()
                if state == 'Fault':
                    raise self.StateMachineFault(f'Fault when transitioning to {expected_status}')
                if state == expected_status:
                    break

    def shutdown(self):
        if self.get_state() != 'Switch on disable':
            self.sdo[0x6040].raw = 0
            time.sleep(0.1)

    def get_state(self):
        states = [
            ('Not ready to switch on', 0b0000_0000_0100_1111, 0b0000_0000_0000_0000),
            ('Switch on disable', 0b0000_0000_0100_1111, 0b0000_0000_0100_0000),
            ('Ready to switch on', 0b0000_0000_0110_1111, 0b0000_0000_0010_0001),
            ('Switched on', 0b0000_0000_0110_1111, 0b0000_0000_0010_0011),
            ('Operation enabled', 0b0000_0000_0110_1111, 0b0000_0000_0010_0111),
            ('Quick Stop active', 0b0000_0000_0110_1111, 0b0000_0000_0000_0111),
            ('Fault reaction active', 0b0000_0000_0100_1111, 0b0000_0000_0000_1111),
            ('Fault', 0b0000_0000_0100_1111, 0b0000_0000_0000_1000),
        ]
        statusword = self.sdo[0x6041].raw
        for name, mask, bits in states:
            if (statusword & mask) == bits:
                return name