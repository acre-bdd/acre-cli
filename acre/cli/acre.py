#!/usr/bin/env python3
import sys
import argparse

from pylogx import log, enable_colors, Level

from . import registry, args

enable_colors(ups=[Level.NOTE])


def main():
    parser = argparse.ArgumentParser(parents=[args.base], description="acre", add_help=False)
    parser.add_argument('command', nargs=1, help='acre command to run')

    (myargs, options) = parser.parse_known_args()
    level = Level.DEBUG if myargs.debug else Level.NOTE
    log.setLevel(level)
    log.debug(myargs)
    log.note('loading commands...')
    from . import commands  # noqa: F401

    return registry.invoke(myargs.command[0], myargs)


if __name__ == "__main__":
    sys.exit(main())
