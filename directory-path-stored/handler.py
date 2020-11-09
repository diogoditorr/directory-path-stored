import argparse


def config_parser(parser: argparse.ArgumentParser):
    shortcut_name = parser.add_argument_group('Shortcut Name')
    shortcut_name.add_argument("-n", "--name", help="name of the directory as shortcut")

    options = parser.add_mutually_exclusive_group()
    options.add_argument("-l", "--list", help="list of shortcuts directories",
                    action="store_true")
    options.add_argument("-s", "--save", help="save directory with the PATH",
                    metavar="PATH")
    options.add_argument("-u", "--update", help="update shortcut directory PATH, if exists", 
                    action="store_true")
    options.add_argument("-d", "--delete", help="delete shortcut directory name", 
                    action="store_true")
    options.add_argument("-v", "--view", help="print shortcut directory by the '--name' argument", 
                    action="store_true")

    return parser

def get_exceptions(parser: argparse.ArgumentParser, args: argparse.Namespace):
    if args.name and args.list:
        parser.error("argument -n/--name: not allowed with argument -l/--list")

# print(args.name)
# parser.error('to use this option, the following argument is required: -n NAME')

def get_args(optional_args: list = None):
    parser = argparse.ArgumentParser(prog="dps")
    parser = config_parser(parser)
    
    if optional_args:
        args = parser.parse_args(optional_args)
    else:
        # Use args from terminal
        args = parser.parse_args()

    get_exceptions(parser, args)
    
    return args 


