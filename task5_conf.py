#!/home/student/Desktop/logger-lab/bin/python3
import logging
import logging.config
logging.config.fileConfig(fname='task5.conf',
disable_existing_loggers=False)
# Get the logger specified in the file
# logger = logging.getLogger(__name__)
logger = logging.getLogger('sampleLogger')
logger.debug('This is a debug message')
