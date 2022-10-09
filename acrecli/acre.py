#!/usr/bin/env python3

import logging
import argparse

from . import registry
from . import baseargs


def main():
    log = logging.getLogger()

    parser = argparse.ArgumentParser(description="acre", add_help=False)
    baseargs.add_to(parser)
    parser.add_argument('command', nargs=1, help='acre command to run')

    (myargs, options) = parser.parse_known_args()
    loglevel = logging.DEBUG if myargs.debug else logging.INFO
    logging.basicConfig(level=loglevel, format='%(message)s')
    log.debug(myargs)
    log.debug('loading commands...')
    from . import commands  # noqa: F401

    registry.invoke(myargs.command[0], myargs)


if __name__ == "__main__":
    main()
