# ************************
# Logger object
# ************************
# Loggers should NEVER be instantiated directly, but always through the module-level function logging.getLogger(name).
# Multiple calls to getLogger() with the same name will always return a reference to the same Logger object.
# https://docs.python.org/3.8/library/logging.html#logger-objects

import logging

# multiple Logger objects may be instantiated
url_info_logger = logging.getLogger('URL_Fetcher')
general_logger = logging.getLogger("GENERAL")
url_info_logger.setLevel(logging.ERROR)


def module1():
    general_logger.warning("General Logger Module1")
    url_info_logger.warning("New URL found")


def do_something():
    general_logger.warning("General Logger Module2")
    url_info_logger.error("Url parsed")


module1()
do_something()


# ************************
# LogRecord object
# ************************
# LogRecord instances are created automatically by the Logger every time something is logged,
# and can be created manually via makeLogRecord() (for example, from a pickled event received over the wire).
# https://docs.python.org/3.8/library/logging.html#logrecord-objects
record = logging.makeLogRecord(
        dict(
            msg="This is logging record1.",
            mylevel="INFO",
            ispbar=False,
        ))

print("Log record info:")
print(record.created)
print(record.getMessage())


# ************************
# Handler object
# ************************
# Handlers send the LogRecord to the required output destination, like the console or a file.
# Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more.
# These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.
logging.getLogger().addHandler(logging.StreamHandler())


# ************************
# Filter object
# ************************
# Starting from version 3.2 there is no need to create specialized Filter classes,
# or use other classes with a filter method: you can use a function (or other callable) as a filter.
# https://docs.python.org/3.8/library/logging.html#filter-objects
# 1. Derive from logging.Filter class and rewrite its filter method
class NoSensitiveDataFilter(logging.Filter):
    sensitive_word = "password"

    def filter(self, record):
        logging.warning(f"filter method record - {record.getMessage()}")
        return self.sensitive_word not in record.getMessage()


logger_filter_class = logging.getLogger("filter_as_class")
logger_filter_class.addFilter(NoSensitiveDataFilter())
logger_filter_class.warning("zzz")
logger_filter_class.warning("password: 00000000")


# 2. Add filter function
def filter_messages_with_sensitive_data(record):
    logging.warning(f"filter function record - {record.getMessage()}")
    if "password" in record.getMessage():
        return False
    return True


logger_filter_callable = logging.getLogger("filter_as_callable")
logger_filter_callable.addFilter(filter_messages_with_sensitive_data)
logger_filter_callable.warning("zzz")
logger_filter_callable.warning("password: 00000000")

# ************************
# Formatter object
# ************************
# Formatter objects are responsible for converting a LogRecord to (usually) a string which can be interpreted
# by either a human or an external system. The base Formatter allows a formatting string to be specified.
# If none is supplied, the default value of '%(message)s' is used, which just includes the message in the logging call.
# https://docs.python.org/3.8/library/logging.html#formatter-objects

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
