import re
import os
import argparse

from acre.cli import log, bailout
from acre.cli import registry, venv, baseargs


@registry.command
def invoke(args):
    """ invoke a test run """

    from acre.cli import AcrePath

    parser = argparse.ArgumentParser(description="acre invoke", usage=__doc__)
    baseargs.add_to(parser)

    parser.add_argument('invoke', nargs=1, help='invoke an acre run')
    (myargs, options) = parser.parse_known_args()
    log.debug(f"arguments: {myargs}")

    userdata = _read_userdata()

    cmd = f'radish -b ./steps -b {AcrePath.steps()} {userdata} {" ".join(options)}'
#   cmd = f'radish -b steps {userdata} {" ".join(options)}'
    log.info(cmd)
    venv.run(cmd)


def _read_userdata():
    if not os.path.exists("etc/user.data"):
        return ""

    userdata = []
    for line in open("etc/user.data", "r").readlines():
        if not re.match(r"\w+=.*", line):
            log.bailout(3, f'invalid user data: {line}')
        userdata.append(f'-u "{line.strip()}"')
    return " ".join(userdata)
