import os
import argparse
from subprocess import run

from acrecli import log, bailout
from acrecli import registry, venv, baseargs
from acrecli.acrepath import AcrePath


@registry.command
def init(args):
    """ initialize acre virtual environment """

    parser = argparse.ArgumentParser(description="acre init", usage=__doc__)
    baseargs.add_to(parser)
    parser.add_argument('init', nargs=1, help='show detailed information about command')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")

    log.info(f'initializing virtual environment in {AcrePath.path}')
    if os.path.exists(AcrePath.path):
        bailout(2, f"directory {AcrePath.path} already exists")
    run(f"virtualenv {AcrePath.path}", shell=True)
    log.info('installing acre-lib')
    venv.run("pip3 install git+https://github.com/realtimeprojects/acre-lib.git")
