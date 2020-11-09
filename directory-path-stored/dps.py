import sys

import colorama
import pyperclip
from termcolor import colored, cprint

from handler import get_args
from database import JsonDatabase

colorama.init()


def main():
    args = get_args()

    db = JsonDatabase()
    # db.create()
    db.list_directories()
    db.update('MyProject', 'C:\\')
    print(args)

    pyperclip.copy("Hello World!")

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', )

if __name__ == '__main__':
    main()