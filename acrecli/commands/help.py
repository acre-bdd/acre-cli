import sys
import argparse
from subprocess import run

from acrecli import log
from acrecli import registry


def _args():
    parser = argparse.ArgumentParser(description="acre help <command>", usage=registry.help('help'))
    parser.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
    parser.add_argument('help', nargs=1, help='show detailed information about command')
    parser.add_argument('command', nargs="?", help='command to show help for')
    return (parser, parser.parse_args())


@registry.command
def help(args):
    """ show help for the given command """
    (parser, myargs) = _args()
    if not myargs.command:
        log.info('usage: acre help <command>')
        log.info(f'available commands: {", ".join(registry.commands())}')
        return

    if myargs.command not in registry.commands():
        log.error("unknown command: {myargs.command}, use `acre help`")
        sys.exit(1)

    run(f"acre {myargs.command} -h", shell=True)
