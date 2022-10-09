import argparse

from acrecli import log
from acrecli import registry, venv


@registry.command
def run(args):
    """ run feature testst """

    parser = argparse.ArgumentParser(description="acre run <features>", usage=__doc__)
    parser.add_argument('run', nargs=1, help='run a test')
    (myargs, options) = parser.parse_known_args()

    cmd = f'radish -b steps {" ".join(options)}'
    log.info(cmd)
    venv.run(cmd)
