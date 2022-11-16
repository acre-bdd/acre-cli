import argparse

container = argparse.ArgumentParser(description="acre run <features>", usage=__doc__, add_help=False)
container.add_argument('--stop', help='stop container after testrun', action="store_true")
container.add_argument('--restart', help='restart container for this testrun', action="store_true")
container.add_argument('--rebuild', help='rebuild container for this testrun', action="store_true")

base = argparse.ArgumentParser(description="acre run <features>", usage=__doc__, add_help=False)
base.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
base.add_argument('--mount', nargs="*", help='mount additional directory into docker container', default=[])
