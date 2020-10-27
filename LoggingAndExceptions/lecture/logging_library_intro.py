# Python provides logging system as a part of its standard library, so you can quickly add logging to your application.

import logging
logging.warning('This is some warning')

# ********************
# Logging level
# ********************
#
# DEBUG -> Detailed information, typically of interest only when diagnosing problems.
# INFO -> Confirmation that things are working as expected.
# WARNING -> An indication that something unexpected happened,
# or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR -> Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL -> A serious error, indicating that the program itself may be unable to continue running.


# ***********************
# Basic configuration
# ***********************

# Some of the commonly used parameters for basicConfig() are the following:
# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.
# More parameters: https://docs.python.org/3/library/logging.html#logging.basicConfig

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


# ***********************
# Formatting the output
# ***********************
# there are some basic elements that are already a part of the LogRecord and can be easily added to the output format
# format can take a string with LogRecord attributes in any arrangement you like.
# More attributes: https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

# Add datetime to output:
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
# Customize datetime format:
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

# The arguments passed to the method would be included as variable data in the message.
name = 'John'
logging.error('%s raised an error', name)
# or with f-strings
logging.error(f'{name} raised an error')

# **************************
# Capturing Stack Traces
# **************************
# The logging module also allows you to capture the full stack traces in an application.
# Exception information can be captured if the exc_info parameter is passed as True,
# and the logging functions are called like this:
a = 5
b = 0

try:
    c = a / b
except Exception as e:
    # the same as logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
