from .acrepath import AcrePath


def add_to(parser):
    """ add the common arguments to the argument parser """
    parser.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
    parser.add_argument('--acrepath', action=AcrePath,
                        help=f'set to acre virtual environment, default is {AcrePath.path}')
