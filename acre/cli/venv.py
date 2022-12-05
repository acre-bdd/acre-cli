import subprocess

from pylogx import log


def run(command):
    log.trace(command)
    return subprocess.run(command, shell=True).returncode
