import sys
from pylogx import log

_commands = {}


def invoke(command, *arg, **kwarg):
    log.debug(f"looking up {command} in {_commands}")
    if command not in _commands:
        log.error(f'unknown command: {command}')
        sys.exit(1)

    cmd = _commands[command]
    log.debug(f"command: {cmd}")
    return cmd['fn'](*arg, **kwarg)


def commands():
    return list(_commands.keys())


def help(command):
    usage = ''
    cmd = _commands[command]

    usage = _add(usage, cmd['fn'].__doc__)
    usage += "\n"
    usage = _add(usage, cmd['usage'])

    return usage


def command(usage=None):
    if callable(usage):
        _commands[usage.__name__] = {'fn': usage, 'usage': None}
        return

    def wrapper(wfn):
        _commands[wfn.__name__] = {'fn': wfn, 'usage': usage}
    return wrapper


def _add(to, what):
    if not what:
        return to
    return to + what
