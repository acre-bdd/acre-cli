import subprocess

from acrelib import log


def run(command):
    log.trace(command)
    return subprocess.run(command, shell=True).returncode
