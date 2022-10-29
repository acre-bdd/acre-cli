import argparse

from acre.cli import log
from acre.cli import registry, baseargs
from acre.cli.docker import Docker

cli_url = "git+https://github.com/realtimeprojects/acre-cli.git"
lib_url = "git+https://github.com/realtimeprojects/acre-lib.git"


@registry.command
def update(args):
    """ update acre inside docker """

    parser = argparse.ArgumentParser(description="acre update", usage=__doc__)
    baseargs.add_to(parser)

    parser.add_argument('--cli', nargs="*", help='use given url for updating the acre cli')
    parser.add_argument('--lib', nargs="*", help='use given url for updating the acre docker base image')
    parser.add_argument('upgrade', nargs=1, help='upgrade acre')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")

    log.info('upgrading acre-lib')
    docker = Docker()
    if myargs.cli:
        url = myargs.cli[0] if len(myargs.cli) > 0 else cli_url
        docker.run("pip3 install --upgrade {url}")
    if myargs.lib:
        url = myargs.lib[0] if len(myargs.lib) > 0 else lib_url
        docker.run(f"pip3 install --upgrade {url}")
