Print vs Logging
================

The logging package has a lot of useful features:

* See where and when a logging call is made
* Differentiate your logging based on severity
* Turn on or off logging at differentiate level of severity 
* Log to the terminal, files, pretty much anything, all at the same time

Print doesn't have any of these.

If your project is meant to be imported by other python tools, it's bad practice for your package to print things to stdout, 
since the user likely won't know where the print messages are coming from. With logging, users of your package can choose 
whether or not they want to propogate logging messages from your tool or not.

Example of logging:

.. code-block:: bash

    import logging

    ...

    if __name__ == "__main__":

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s | %(levelname)s  |%(process)d | %(name)s | %(message)s",
            datefmt='%d-%b-%y %H:%M:%S'
        )

        logging.info("...")

Where the output would look something like

.. code-block:: bash

    31-Oct-22 17:57:30 | INFO  | z:\trade\trade.py | trade_api | 34 | Using paper account

A full list of formatters can be found at

https://docs.python.org/3/library/logging.html#formatter-objects
