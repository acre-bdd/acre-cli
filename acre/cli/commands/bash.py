import argparse

from acre.cli import log
from acre.cli import registry, args
from acre.cli.docker import Docker
from acre.cli.container import Container


@registry.command
def bash(arguments):
    """ run a bash inside the docker container """

    parser = argparse.ArgumentParser(parents=[args.base, args.container],
                                     description="acre bash",
                                     usage=__doc__)
    parser.add_argument('bash', nargs=1, help='run bash inside container')
    (myargs, options) = parser.parse_known_args()
    log.debug(f"arguments: {myargs}")

    cmd = f'{" ".join(options)}' if len(options) > 0 else 'bash'
    docker = Docker(name='acre')
    container = Container(docker, myargs)
    log.info(f"running: {cmd}")
    return container.exec(command=cmd, cwd="/acre", interactive=True)
