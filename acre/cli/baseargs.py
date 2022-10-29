def add_to(parser):
    """ add the common arguments to the argument parser """
    parser.add_argument('--debug', action='store_true', help='enable debug logging', default=False)
