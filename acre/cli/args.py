import argparse

container = argparse.ArgumentParser(description="acre run <features>", usage=__doc__, add_help=False)
container.add_argument('--stop', help='stop container after testrun', action="store_true")
container.add_argument('--restart', help='restart container for this testrun', action="store_true")
container.add_argument('--rebuild', help='rebuild container for this testrun', action="store_true")
container.add_argument('--update', help='update acre requirements before run', action="store_true")
container.add_argument('--detach', help='run docker container in background and keep it running', action="store_true")

base = argparse.ArgumentParser(description="acre run <features>", usage=__doc__, add_help=False)
base.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
base.add_argument('--mount', nargs=1, help='mount additional directory into docker container',
                  action="append", default=[])
base.add_argument('--steps', nargs=1, help='mount <steps> directory to container and add it to the steps path',
                  action="append", default=[])
base.add_argument('--lib', nargs=1, help='mount <lib> directory to container and add it to the PYTHONPATH',
                  action="append", default=[])
