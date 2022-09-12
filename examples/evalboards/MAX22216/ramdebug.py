import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.RAMDebug import Channel, RAMDebug, RAMDebug_Trigger

pytrinamic.show_info()

with ConnectionManager(debug=True).connect() as my_interface:
    print(my_interface)

    ch = Channel.field(0, MAX22216.FIELD.ADC_VM_RAW, signed=True, eval_channel=1)
    trigger = Channel.field(0, MAX22216.FIELD.ADC_VM_RAW, signed=True, eval_channel=1)

    debug = RAMDebug(my_interface)
    debug.set_channel(ch)
    debug.set_trigger_type(RAMDebug_Trigger.TRIGGER_UNCONDITIONAL)
    debug.set_trigger_threshold(50)
    debug.start_measurement()

    while(not debug.is_measurement_done()):
        pass

    samples = debug.get_samples()

print("\nDone.")
