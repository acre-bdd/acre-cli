import subprocess

from acre.cli import log


def run(command):
    cmd = f"{command}"
    log.debug(f"running: {command}")
    subprocess.run(cmd, shell=True)
