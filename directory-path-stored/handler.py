import os
import argparse
from os.path import join

import pyperclip
from termcolor import colored, cprint

from database import JsonDatabase

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', )

def handle_args(args: argparse.Namespace):
    if not os.path.isfile(JsonDatabase()._get_json_path()):
        print('creating...')
        JsonDatabase().create()

    if args.name:
        dir_name = args.name

        if args.save:
            path = _get_compatible_path(args.save)
            save_directory(dir_name, path)

        elif args.update:
            path = _get_compatible_path(args.update)
            update_directory(dir_name, path)

        elif args.view:
            view_directory(dir_name)

        elif args.delete:
            delete_directory(dir_name)

        else:
            copy_path(dir_name)

    elif args.list:
        display_directories()    
    

def save_directory(dir_name, path):
    cprint('saving', 'magenta')
    db = JsonDatabase()
    db.save(dir_name, path)


def update_directory(dir_name, path):
    cprint('updating', 'magenta')
    JsonDatabase().update(dir_name, path)

    
def view_directory(dir_name):
    cprint('viewing', 'magenta')
    print(f'{dir_name}: {repr(JsonDatabase().get_directory_path(dir_name))}')


def delete_directory(dir_name):
    cprint('deleting', 'magenta')
    JsonDatabase().delete(dir_name)


def copy_path(dir_name):
    cprint('copying', 'magenta')
    path = JsonDatabase().get_directory_path(dir_name)
    if path:
        pyperclip.copy(f'cd "{path}"')


def display_directories():
    cprint('displaying directories', 'magenta')


def _get_compatible_path(path: str):
    return os.path.normpath(path.replace('\ ', ' ').replace('\:', ':')).strip("\'\"")
