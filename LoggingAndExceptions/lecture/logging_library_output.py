import logging.handlers

# ************************
# Output to stdout
# ************************
logging.getLogger("Console logger").addHandler(logging.StreamHandler())

# ************************
# Output to file - rotate
# ************************

# 1. rotate by log file size
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

# add a rotating handler
handler = logging.handlers.RotatingFileHandler("test.log", maxBytes=200, backupCount=5)
logger.addHandler(handler)
for i in range(10):
    logger.info("This is test log line %s" % i)

# 2. rotate by log file age
import time

logger = logging.getLogger("Rotating by age Log")
logger.setLevel(logging.INFO)

# add a rotating handler
handler = logging.handlers.TimedRotatingFileHandler("test.log",
                                                    when="s",
                                                    interval=1,
                                                    backupCount=5)
logger.addHandler(handler)
for i in range(10):
    logger.info("This is test log line %s" % i)
    print(1)
    time.sleep(1)


# ************************
# Alternative channel
# ************************

# 1. slack - https://gist.github.com/blakev/2d74a738a2770eeb06b1f5b2353ebe38
# https://github.com/slackapi/python-slackclient slack-client should be used.

# 2. sentry (https://sentry.io/for/python)
# https://docs.sentry.io/platforms/python/guides/logging/
