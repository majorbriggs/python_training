from my_package import my_module
import logging

logger = logging.getLogger(__name__)
logger.info('Main started')

my_module.some_function()

logger.info('Main finished')