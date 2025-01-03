

Option A: Start the download when all data was logged.

```py
# Start the logging
dl.activate_trigger()
# Wait for the logging to finish
while not dl.is_done():
    pass
dl.download_data()
# Access the logged data
...
```

Option B: Start the download right after the logging was triggered. (What should be done if the product does not support this?)

```py
# Start the logging
dl.activate_trigger()
# Wait for the logging to start
while not dl.got_triggered():
    pass
dl.download_data()
# Access the logged data
...
```

Error

```py
# Start the logging
dl.activate_trigger()
# This will likely raise an exception because the download could not start.
dl.download_data()
```