import os
import argparse

from acre.cli import log


class AcrePath(argparse.Action):
    path = os.path.expanduser(os.environ.get('ACREPATH', "~/.acre"))

    def __call__(self, parser, namespace, values, option_string=None):
        log.debug(f"setting ACREPATH to {values}")
        AcrePath.path = values
