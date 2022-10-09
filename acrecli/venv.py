import subprocess
from acrecli.acrepath import AcrePath


def run(cmd):
    subprocess.run(f". {AcrePath.path}/bin/activate && {cmd}", shell=True)
