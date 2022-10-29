import sys
import logging

log = logging.getLogger()


def bailout(ec, message):
    log.critical(message)
    sys.exit(ec)
