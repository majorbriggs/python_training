Logging
===========================================

logging built-in module
--------------------------
:py:mod:`logging` module from the Standard Library allows for a flexible and consistent logging across different
modules of your application.

Apart from the examples presented below, see the `Python Logging Cookbook <https://docs.python.org/2/howto/logging-cookbook.html>`_
and the examples in :py:mod:`logging` documentation

Example configuration in a muli-module application
------------------------------------------------------------------------------

To start working with :py:mod:`logging`, import the module and create an instance of the logger:

.. code-block:: python

    import logging
    logger = logging.getLogger('my logger')

All calls to ``logging.getLogger('logger_name')`` within the same python interpeter process return
a reference to the same logger object. A good practice when dealing with multiple modules is to have one module with
a global log configuration file, and separate calls to ``logging.getLogger(__name__)`` in each modules.

The variable ``__name__`` contains the name of the current python module (with "." notation, e.g. ``some_package.some_module``)
So, by calling

.. code-block:: python

    logger = logging.getLogger(__name__)

we end up with separate log instances indicating exactly where does the logged information come from

A possible setup using this principle is presented below

.. code-block:: none

    my_package/                     Top-level package
          __init__.py               initialize the log
          logconf.py
          my_module.py
    main.py                         import my_package


Each module should have the following lines:

.. code-block:: python

    import logging

    LOGGER = logging.getLogger(__name__)


Sample configuration file

.. code-block:: python

    # logconf.py

    import logging
    # create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('logfile.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info('Logging configuration finished')

Other modules

.. code-block:: python

    # my_module.py

    import logging

    LOGGER = logging.getLogger(__name__)

    def some_function():
        LOGGER.info('some_function called')



.. code-block:: python

    # main.py

    from my_package import my_module
    import logging

    logger = logging.getLogger(__name__)

    logger.info('Main started')

    auxillary_module.some_function()

    logger.info('Main finished')


Log output

.. code-block:: none

    2016-10-03 15:54:03,497 - root - INFO - Logging configuration finished
    2016-10-03 15:54:03,498 - __main__ - INFO - Main started
    2016-10-03 15:54:03,498 - my_package.my_module - INFO - some_function called
    2016-10-03 15:54:03,498 - __main__ - INFO - Main finished


Log file rotation
----------------------------------------------------

To prevent log files from excessing a certain size or number of separate files, you may want to use a pattern called file rotation.
This means, that after reaching the maximum size, a new log file is opened with the original name, and the old one is archived, typically in a file renamed by appending "1" to the name
When the predefined maximum number of archived log files is reached, the oldest ones are deleted.

To implement the pattern with :py:mod:`logging`, use :py:class:`logging.handlers.RotatingFileHandler`

Example from `Python Logging Cookbook <https://docs.python.org/2/howto/logging-cookbook.html>`_:

.. code-block:: python

    import glob
    import logging
    import logging.handlers

    LOG_FILENAME = 'logging_rotatingfile_example.out'

    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(
                  LOG_FILENAME, maxBytes=20, backupCount=5)

    my_logger.addHandler(handler)

    # Log some messages
    for i in range(20):
        my_logger.debug('i = %d' % i)

    # See what files are created
    logfiles = glob.glob('%s*' % LOG_FILENAME)

    for filename in logfiles:
        print(filename)


See also :py:class:`logging.handlers.RotatingFileHandler` for file rotating based on time, the not size of the log.