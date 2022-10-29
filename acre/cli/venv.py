import subprocess

from acrecli import log
from acrecli.acrepath import AcrePath


def run(command):
    cmd = f". {AcrePath.path}/bin/activate && {command}"
    cmd = f"{command}"
    log.debug(f"running: {command}")
    subprocess.run(cmd, shell=True)