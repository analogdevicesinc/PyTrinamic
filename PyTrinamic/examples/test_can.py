import can

# Candlelight firmware on Linux
#bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

# Stock slcan firmware on Linux
# Stock slcan firmware on Windows
bus = can.interface.Bus(bustype='slcan', channel='COM8', bitrate=1000000)

msg = can.Message(arbitration_id=0xc0ffee,
                  data=[0, 25, 0, 1, 3, 1, 4, 1],
                  is_extended_id=True)

try:
    bus.send(msg, 100)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")