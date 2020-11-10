import sys
import os
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

import colorama

import handler
from dps_parser import get_args

colorama.init()


def main():
    # ['-n', 'git', '-u', 'D\:/Diego\ Oliveira\ Silva/Documents/GitHub/']
    args = get_args()

    handler.handle_args(args)
    

if __name__ == '__main__':
    main()