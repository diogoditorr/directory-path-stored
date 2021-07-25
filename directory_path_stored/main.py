import os
import sys

import colorama

import dps

# os.chdir(os.path.dirname(__file__))


def main():
    # ['-n', 'git', '-u', 'D\:/Diego\ Oliveira\ Silva/Documents/GitHub/']
    colorama.init()
    args = dps.parse_args()

    dps.Handler(args).execute()


if __name__ == '__main__':
    main()
