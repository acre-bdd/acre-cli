import argparse

from pylogx import log
from acre.cli import registry, venv, args


@registry.command
def init(arguments):
    """ initialize acre virtual environment """

    parser = argparse.ArgumentParser(parents=[args.base], description="acre init", usage=__doc__)
    parser.add_argument('--docker', nargs=1, help='install acre-docker from the given url',
                        default=["git+https://github.com/acre-bdd/acre-docker.git"])
    parser.add_argument('init', nargs=1, help='initialize acre')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")
    log.info('installing acre-docker')
    venv.run(f"pip3 install {myargs.docker[0]}")
