import logging.handlers


class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
    max_visitors = 200
    min_visitors = 10

    def __init__(self, visitors_num):
        self.visitors_num = visitors_num


if self.visitors_num > self.max_visitors:
    raise TooManyVisitors
elif self.visitors_num < self.min_visitors:
    raise TooFewVisitors


    # add 2 class attributes - max_visitors (200) and min_visitors (10)

    def __init__(self, visitors_num, message="Count of visitors is not in (10 - 200 range."):
        self.visitors_num = visitors_num
        self.message = message
        super(Concert, self).__init__(self.message)


    def __str__(self):
        return f"(self.visitors_num) -> (self.message)"

visitors_num = int(input("Max visitors - 200"))
if 0 < visitors_num < 10
    raise TooFewVisitorsError(visitors_num)

if 200 > visitors_num
    raise TooManyVisitorsError(visitors_num)

    """
    if visitors num is bigger than max_visitors - raise TooManyVisitors error
    if visitors num is less than min_visitors - raise TooFewVisitors error
    """


def make_concert(visitors_num):
    """
    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    in case if caught - log error to console and return False, in case of successful initialization - return True
    """


# create Logger object
# set level to debug
# add handler to write logs to file "test.log"


def log_message(message, level):
    """
    this function should use the logger defined above and log messages.
    level is the numeric representation of log level the message should refer to.
    :param message:
    :param level:
    """
