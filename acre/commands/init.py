import os
import argparse
from subprocess import run

from acre import log, bailout
from acre import registry


@registry.command
def init(args):
    """ initialize acre virtual environment """

    parser = argparse.ArgumentParser(description="acre init", usage=__doc__)
    parser.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
    parser.add_argument('--acrepath',
                        default=os.environ.get('ACREPATH', "~/.acre"),
                        help='path to acre virtual environment')
    parser.add_argument('init', nargs=1, help='show detailed information about command')
    myargs = parser.parse_args()
    acrepath = os.path.expanduser(myargs.acrepath)

    log.info(f'initializing virtual environment in {myargs.acrepath}')
    if os.path.exists(acrepath):
        bailout(2, f"directory {acrepath} already exists")

    run(f"virtualenv {acrepath}", shell=True)
