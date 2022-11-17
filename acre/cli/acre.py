#!/usr/bin/env python3
import sys
import logging
import argparse

from . import registry, args


def main():
    log = logging.getLogger()

    parser = argparse.ArgumentParser(parents=[args.base], description="acre", add_help=False)
    parser.add_argument('command', nargs=1, help='acre command to run')

    (myargs, options) = parser.parse_known_args()
    loglevel = logging.DEBUG if myargs.debug else logging.INFO
    logging.basicConfig(level=loglevel, format='%(message)s')
    log.debug(myargs)
    log.debug('loading commands...')
    from . import commands  # noqa: F401

    return registry.invoke(myargs.command[0], myargs)


if __name__ == "__main__":
    sys.exit(main())
