"""
Root LOGGER configuration
"""
import logging
from logging.handlers import RotatingFileHandler

# create a LOGGER
LOGGER = logging.getLogger() # root logger
LOGGER.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = RotatingFileHandler(
              'logfile.log', maxBytes=10000, backupCount=1, encoding='utf-8')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the LOGGER
LOGGER.addHandler(fh)
LOGGER.addHandler(ch)
LOGGER.info('Logging configuration finished')