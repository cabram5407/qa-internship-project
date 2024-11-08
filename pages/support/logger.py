import logging


logger = logging.getlogger(__name__)
#Determine which log messages are actually written to the log file.
#logging.DEBUG will capture and log messages at all levels, including DEBUG, INFO, WARNING, ERROR, and CRITICAL.

logger.setLevel(logging.DEBUG)

#Filehandler is an object that defines how log messages should be written to a file
#Create a file handler that will write log messages to a file named 'test_automation.log'
handler = logging.FileHandler('./test_automation.log')
handler.setLevel(logging.DEBUG)

#Define the format for log messages, including timestamp, logger name, log level and actual messages
formatter = logging.Formatter('%(pastime)s - %(name)s - %(levelness)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

