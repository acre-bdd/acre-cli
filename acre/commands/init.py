import os
import argparse
from subprocess import run

from acre import log, bailout
from acre import registry, venv
from acre.acrepath import AcrePath


@registry.command
def init(args):
    """ initialize acre virtual environment """

    parser = argparse.ArgumentParser(description="acre init", usage=__doc__)
    parser.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
    parser.add_argument('--acrepath', action=AcrePath,
                        help=f'set to acre virtual environment, default is {AcrePath.path}')
    parser.add_argument('init', nargs=1, help='show detailed information about command')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")

    log.info(f'initializing virtual environment in {AcrePath.path}')
    if os.path.exists(AcrePath.path):
        bailout(2, f"directory {AcrePath.path} already exists")
    run(f"virtualenv {AcrePath.path}", shell=True)
    log.info('installing acre-lib')
    venv.run("pip3 install git+https://github.com/realtimeprojects/acre-lib.git")



