import argparse

from acre.cli import registry, args
from acre.cli.docker import Docker
from acre.cli.container import Container


@registry.command
def build(arguments):
    """ build the docker containers required for the test run """
    parser = argparse.ArgumentParser(parents=[args.container, args.base],
                                     description="acre run <features>", usage=__doc__)
    parser.add_argument('build', nargs=1, help='build the container')
    (myargs, options) = parser.parse_known_args()

    docker = Docker(name="acre")
    container = Container(docker, myargs)
    return container.build(force=True)
