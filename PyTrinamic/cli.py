import PyTrinamic

def select_com_port_by_name(CAN=False, Serial=False, USB=False):
    PyTrinamic.showAvailableComPorts(CAN, Serial, USB)
    return input("Select COM port by name: ")

# TODO
def select_com_port_by_id(CAN=False, Serial=False, USB=False):
    pass
