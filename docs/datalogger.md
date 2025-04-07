
# Datalogger

## General Information

Some Trinamic products have a logging mechanism implemented into firmware, also called RAMDebug at some places.
This logging mechanism allows sampling of signals at a high rate, that would otherwise not be possible to achieve via the communication interface.

Also the TMC-EvalSystem supports the logging mechanism, allowing Eval-chip data to be logged.

The following two diagrams give an overview on concept of the Datalogger. 
![Datalogger Diagram](datalogger.drawio.svg)

## Usage

### Basic example

This example keeps all optional settings at default.
It uses no triggering, thus data will be logged immediately after `start_capture()` got called.

```py
    dl = tmc9660_eval.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
    ]

    dl.start_capture()

    dl.wait_for_completion()

    dl.download_logs()

    print(dl.log.data["ADC_I1_I0_SCALED.I0"])
```

Step by step details:

* We create reference to the Datalogger object as a short alias.
  ```py
    dl = tmc9660_eval.datalogger
  ```
* The number of samples to be logged is given.
  ```py
    dl.config.samples_per_channel = 10
  ```
* The data to be logged is listed.
  ```py
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
    ]
  ```
* With the minimal configuration done we can start the logging.
  ```py
    dl.start_capture()
  ```
* The firmware now does the logging and we need to wait till it is finished.
  ```py
    dl.wait_for_completion()
  ```
* With the logging done, we can download the logs.
  ```py
    dl.download_logs()
  ```
* Finally we can access the logged data via the `logs` dictionary.
  ```py
    print(dl.log.data["ADC_I1_I0_SCALED.I0"])
  ```
  The `dl.log.data["ADC_I1_I0_SCALED.I0"]` returns a `DataLogger.LogData` object and the print will look similar to this output:
  ```
    DataLogger.LogData(samples=[-9, -49, -65, -57, -81, -105, -25, -73, -105, -9], request_object=<pytrinamic.ic.TMC9660.MCCmap._ALL_REGISTERS._ADC_I1_I0_SCALED._I0 object at 0x00000274C1FBC2E0>)
  ```

## Reading out Information on a device's Logging Implementation

We can use `get_info()` to read out the logging information.

```py
    dl = tmc9660_eval.datalogger

    print(dl.get_info())
```

This prints the `DataLogger.Info` object returned by `get_info()`, which will look like this:

```
DataLogger.Info(base_frequency_hz=25000, sample_buffer_length=4096, number_of_channels=4)
```

## Change of the Sample/Logging Rate

### Using the `sample_rate` Config Attribute

```py
    dl.config.samples_per_channel = 10
    dl.config.sample_rate = 12500.0
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
       ...
```

### Using the `set_sample_rate()` Function

The sample rate can be specified using the `config.set_sample_rate()` function:

```py
    dl.config.samples_per_channel = 10
    dl.config.set_sample_rate(12500.0)
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
       ...
```

### Using the `down_sampling_factor`

The sample rate can be decrease using the `config.down_sampling_factor`:

```py
    dl.config.samples_per_channel = 10
    dl.config.down_sampling_factor = 2  # <--
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
       ...
```

This will be reflected in `dl.log.rate_hz` and `dl.log.period_s`.

A `down_sampling_factor` of 1 means no down sampling.
A value of 2 divides the base frequency by 2.
Note, ideally the `down_sampling_factor` is set to a power of two value.

## Doing a Logging Session with a Trigger Condition

```py
    dl = tmc9660_eval.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = [
       TMC9660.MCC.ADC_I1_I0_SCALED.I0,
    ]
    dl.config.trigger.on_data = TMC9660.MCC.ADC_I1_I0_SCALED.I0
    dl.config.trigger.threshold = 100
    dl.config.trigger.edge = dl.TriggerEdge.RISING

    dl.start_capture()

    dl.wait_for_completion()

    dl.download_logs()

    print(dl.log.data["ADC_I1_I0_SCALED.I0"])
```

This is almost identical to the above unconditional logging example, but we set trigger condition.
Note, for another unconditional logging to start, the `dl.config.trigger.on_data` must be set to `None`

## TODO - Continue with more details!

...