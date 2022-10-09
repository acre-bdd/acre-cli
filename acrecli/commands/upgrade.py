import os
import argparse

from acrecli import log, bailout
from acrecli import registry, venv, baseargs
from acrecli.acrepath import AcrePath


@registry.command
def upgrade(args):
    """ upgrade acre """

    parser = argparse.ArgumentParser(description="acre init", usage=__doc__)
    baseargs.add_to(parser)

    parser.add_argument('upgrade', nargs=1, help='upgrade acre')
    myargs = parser.parse_args()
    log.debug(f"arguments: {myargs}")

    if not os.path.exists(AcrePath.path):
        bailout(2, "acre not initialized. Run `acre init`.")
    log.info('upgrading acre-lib')
    venv.run("pip3 install --upgrade git+https://github.com/realtimeprojects/acre-lib.git")
