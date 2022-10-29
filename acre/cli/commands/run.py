import argparse

from acre.cli import registry, baseargs, bailout
from acre.cli.docker import Docker


@registry.command
def run(args):
    """ run feature testst """
    parser = argparse.ArgumentParser(description="acre run <features>", usage=__doc__)
    baseargs.add_to(parser)
    parser.add_argument('--update', help='update acre requirements before run', action="store_true")
    parser.add_argument('--noterm', help='do not acquire a terminal for testrun', action="store_true")
    parser.add_argument('run', nargs=1, help='run a test')
    (myargs, options) = parser.parse_known_args()

    docker = Docker()
    ec = docker.build(update=myargs.update)
    if ec:
        bailout("docker build failed")
    return docker.run(f'acre invoke {" ".join(options)}', cwd="testproject/", interactive=not myargs.noterm)
