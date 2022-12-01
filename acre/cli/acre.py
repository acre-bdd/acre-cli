#!/usr/bin/env python3
import sys
import argparse

from acrelib import log

from . import registry, args


def main():
    parser = argparse.ArgumentParser(parents=[args.base], description="acre", add_help=False)
    parser.add_argument('command', nargs=1, help='acre command to run')

    (myargs, options) = parser.parse_known_args()
    if myargs.debug:
        log.setLevel(log.DEBUG)
    log.debug(myargs)
    log.debug('loading commands...')
    from . import commands  # noqa: F401

    return registry.invoke(myargs.command[0], myargs)


if __name__ == "__main__":
    sys.exit(main())
