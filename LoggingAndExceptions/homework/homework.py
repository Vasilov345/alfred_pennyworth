<<<<<<< HEAD
=======
import logging.handlers


>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2
class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
<<<<<<< HEAD

    # add 2 class attributes - max_visitors (200) and min_visitors (10)
=======
    # add 2 class attributes - max_visitors (200) and min_visitors (10)
    max_visitors = 200
    min_visitors = 10
>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2

    def __init__(self, visitors_num):
        """
        if visitors num is bigger than max_visitors - raise TooManyVisitors error
        if visitors num is less than min_visitors - raise TooFewVisitors error
        """
<<<<<<< HEAD
=======
        if visitors_num > self.max_visitors:
            raise TooManyVisitors
        elif visitors_num < self.min_visitors:
            raise TooFewVisitors
>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2


def make_concert(visitors_num):
    """
    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    in case if caught - log error to console and return False, in case of successful initialization - return True
    """
<<<<<<< HEAD

# create Logger object
# set level to debug
# add handler to write logs to file "test.log"
=======
    try:
        a = Concert(9)
    except TooManyVisitors as e:
        print(e)
        return False
    except TooFewVisitors as e:
        print(e)
        return False
    else:
        return True


logger_obj = logging.getLogger('test')
logger_obj.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler("test.log", mode='w')
logger_obj.addHandler(handler)
>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2


def log_message(message, level):
    """
    this function should use the logger defined above and log messages.
    level is the numeric representation of log level the message should refer to.
    :param message:
    :param level:
    """
<<<<<<< HEAD
=======
    if level == 10:
        logger_obj.debug(message)
    elif level == 20:
        logger_obj.info(message)
    elif level == 30:
        logger_obj.warning(message)
    elif level == 40:
        logger_obj.error(message)
    elif level == 50:
        logger_obj.critical(message)
>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2
