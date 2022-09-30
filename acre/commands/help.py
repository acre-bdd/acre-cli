from acre import log
from acre.registry import command


@command
def help(args):
    log.info("hello world")
