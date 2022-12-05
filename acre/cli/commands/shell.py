import argparse

from pylogx import log
from acre.cli import registry, args
from acre.cli.docker import Docker
from acre.cli.container import Container


@registry.command
def shell(arguments):
    """ run a shell inside the docker container """

    parser = argparse.ArgumentParser(parents=[args.base, args.container],
                                     description="acre bash",
                                     usage=__doc__)
    parser.add_argument('bash', nargs=1, help='run bash inside container')
    (myargs, options) = parser.parse_known_args()
    log.debug(f"arguments: {myargs}")

    cmd = f'{" ".join(options)}' if len(options) > 0 else 'sh'
    docker = Docker(name='acre')
    myargs.nowait = True
    container = Container(docker, myargs)
    return container.do(command=cmd, cwd="/acre/testproject", interactive=True)
