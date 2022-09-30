#!/usr/bin/env python3

import os
import logging
import argparse

from . import commands  # noqa: F401
from . import registry


def main():
    log = logging.getLogger()
    _env = os.environ.get

    parser = argparse.ArgumentParser(description="acre", add_help=False)
    parser.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
    parser.add_argument('command', nargs=1, help='acre command to run')

    (myargs, options) = parser.parse_known_args()
    loglevel = logging.DEBUG if myargs.debug else logging.INFO
    logging.basicConfig(level=loglevel, format='%(message)s')
    log.debug(myargs)
    registry.invoke(myargs.command[0], myargs)


if __name__ == "__main__":
    main()
