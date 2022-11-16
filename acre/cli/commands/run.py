import argparse

from acre.cli import registry, args
from acre.cli.docker import Docker
from acre.cli.container import Container


@registry.command
def run(arguments):
    """ run feature testst """
    parser = argparse.ArgumentParser(parents=[args.container, args.base],
                                     description="acre run <features>", usage=__doc__)
    parser.add_argument('--update', help='update acre requirements before run', action="store_true")
    parser.add_argument('--upgrade',
                        help='force radish-run to update dependencies before testrun',
                        action="store_const", const="--upgrade", default="")
    parser.add_argument('--noterm', help='do not acquire a terminal for testrun', action="store_true")
    parser.add_argument('run', nargs=1, help='run a test')
    (myargs, options) = parser.parse_known_args()

    docker = Docker(name="acre")
    container = Container(docker, myargs)
    return container.exec(command=f'run-radish {myargs.upgrade} {" ".join(options)}',
                          cwd="/acre/testproject/",
                          interactive=not myargs.noterm)
