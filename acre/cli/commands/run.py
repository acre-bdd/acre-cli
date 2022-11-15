import logging
import argparse

from acre.cli import registry, baseargs, bailout
from acre.cli.docker import Docker


@registry.command
def run(args):
    """ run feature testst """
    parser = argparse.ArgumentParser(description="acre run <features>", usage=__doc__)
    baseargs.add_to(parser)
    parser.add_argument('--stop', help='stop container after testrun', action="store_true")
    parser.add_argument('--restart', help='restart container for this testrun', action="store_true")
    parser.add_argument('--rebuild', help='rebuild container for this testrun', action="store_true")
    parser.add_argument('--update', help='update acre requirements before run', action="store_true")
    parser.add_argument('--upgrade',
                        help='force radish-run to update dependencies before testrun',
                        action="store_const", const="--upgrade", default="")
    parser.add_argument('--noterm', help='do not acquire a terminal for testrun', action="store_true")
    parser.add_argument('run', nargs=1, help='run a test')
    (myargs, options) = parser.parse_known_args()

    docker = Docker(name="acre")

    if myargs.rebuild:
        if docker.is_running():
            logging.warning("stopping running container")
            docker.stop()
        ec = docker.build(update=myargs.update)
        if ec:
            bailout("docker build failed")

    if docker.is_running():
        if myargs.restart:
            docker.stop()
            docker.run(mounts=myargs.mount)
    else:
        docker.run(mounts=myargs.mount)

    ec = docker.exec(f'run-radish {myargs.upgrade} {" ".join(options)}',
                     cwd="/acre/testproject/",
                     interactive=not myargs.noterm)

    if myargs.stop:
        docker.stop()
    return ec
