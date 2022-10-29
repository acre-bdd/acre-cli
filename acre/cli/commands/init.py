import argparse

from acre.cli import log
from acre.cli import registry, venv, baseargs


@registry.command
def init(args):
    """ initialize acre virtual environment """

    parser = argparse.ArgumentParser(description="acre init", usage=__doc__)
    baseargs.add_to(parser)
    parser.add_argument('--docker', nargs=1, help='install acre-docker from the given url',
                        default=["git+https://github.com/realtimeprojects/acre-docker.git"])
    parser.add_argument('init', nargs=1, help='initialize acre')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")
    log.info('installing acre-docker')
    venv.run(f"pip3 install {myargs.docker[0]}")
