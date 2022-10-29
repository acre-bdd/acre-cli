import argparse

from acre.cli import registry
from acre.cli.docker import Docker


@registry.command
def run(args):
    """ run feature testst """
    parser = argparse.ArgumentParser(description="acre run <features>", usage=__doc__)
    parser.add_argument('run', nargs=1, help='run a test')
    (myargs, options) = parser.parse_known_args()

    docker = Docker()
    docker.build()
    docker.run("acre invoke {options}", cwd="testproject/")
