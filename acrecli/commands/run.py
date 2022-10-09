import os
import re
import argparse

from acrecli import log
from acrecli import registry, venv


@registry.command
def run(args):
    """ run feature testst """

    parser = argparse.ArgumentParser(description="acre run <features>", usage=__doc__)
    parser.add_argument('run', nargs=1, help='run a test')
    (myargs, options) = parser.parse_known_args()

    userdata = _read_userdata()

    cmd = f'radish -b steps {userdata} {" ".join(options)}'
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
