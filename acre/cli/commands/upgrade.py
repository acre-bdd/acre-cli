import argparse

from acre.cli import log
from acre.cli import registry, venv, baseargs

cli_url = "git+https://github.com/realtimeprojects/acre-cli.git"
docker_url = "git+https://github.com/realtimeprojects/acre-docker.git"


@registry.command
def upgrade(args):
    """ upgrade acre """

    parser = argparse.ArgumentParser(description="acre init", usage=__doc__)
    baseargs.add_to(parser)

    parser.add_argument('--cli', nargs="*", help='use given url for updating the acre cli')
    parser.add_argument('--docker', nargs="*", help='use given url for updating the acre docker base image')
    parser.add_argument('upgrade', nargs=1, help='upgrade acre')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")

    log.info('upgrading acre-lib')
    if myargs.cli:
        url = myargs.cli[0] if len(myargs.cli) > 0 else cli_url
        venv.run(f"pip3 install --upgrade {url}")
    if myargs.docker:
        url = myargs.docker[0] if len(myargs.docker) > 0 else docker_url
        venv.run(f"pip3 install --upgrade {url}")
