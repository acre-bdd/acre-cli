import argparse

from acre.cli import log, bailout
from acre.cli import registry, baseargs
from acre.cli.docker import Docker


@registry.command
def bash(args):
    """ run a bash inside the docker container """

    parser = argparse.ArgumentParser(description="acre bash", usage=__doc__)
    baseargs.add_to(parser)

    parser.add_argument('bash', nargs=1, help='run bash inside container')
    (myargs, options) = parser.parse_known_args()
    log.debug(f"arguments: {myargs}")

    cmd = f'/usr/local/bin/shell {" ".join(options)}'
    docker = Docker()
    if docker.build():
        bailout("docker build failed")
    return docker.run(cmd, mounts=myargs.mount, interactive=True)
