import sys
import logging

log = logging.getLogger()


def bailout(message, ec=1):
    log.critical(message)
    sys.exit(ec)
