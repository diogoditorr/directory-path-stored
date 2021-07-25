import argparse
import os
from os.path import join
from pathlib import Path

import pyperclip
from termcolor import colored, cprint

from .database.database import Database
from .exceptions import OverwriteError
from .utils import calculate_max_width

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', )


class Handler():
    def __init__(self, args: argparse.Namespace):
        if not isinstance(args, argparse.Namespace):
            raise TypeError

        self.db = Database()
        self.args = args

        if not os.path.isfile(self.db.database_path()):
            print('Creating database...')
            self.db.create()

        self.db.get_data()

    def execute(self):
        if self.args.name:
            dir_name = self.args.name

            if self.args.save:
                path = self._get_compatible_path(self.args.save)
                self._save_directory(dir_name, path)

            elif self.args.update:
                path = self._get_compatible_path(self.args.update)
                self._update_directory(dir_name, path)

            elif self.args.delete:
                self._delete_directory(dir_name)

            elif self.args.view:
                self._view_directory(dir_name)

            else:
                self._copy_path(dir_name)

        elif self.args.list:
            self._display_directories()

    def _save_directory(self, dir_name, path):
        try:
            self.db.save(dir_name, path)
        except OverwriteError:
            print(
                f"Directory shortcut '{self.db.get_directory(dir_name).name}' already exists")
        else:
            cprint(f'Directory shortcut \'{dir_name}\' saved!' +
                   f'\nPath: "{path}"', 'magenta')

    def _update_directory(self, dir_name, path):
        try:
            self.db.update(dir_name, path)
        except ValueError:
            print(f"Directory shortcut '{dir_name}' does not exist!")
        else:
            cprint(f'Directory shortcut \'{self.db.get_directory(dir_name).name}\' updated successfully!' +
                   f'\nPath: "{path}"', 'magenta')

    def _delete_directory(self, dir_name):
        try:
            self.db.delete(dir_name)
        except ValueError:
            print(f"Directory shortcut '{dir_name}' does not exist!")
        else:
            cprint(
                f'Directory shortcut \'{self.db.get_directory(dir_name).name}\' deleted!', 'magenta')

    def _view_directory(self, dir_name):
        # prettytable
        directory = self.db.get_directory(dir_name)
        if directory:
            cprint(f'|=> Showing shortcut directory:' +
                   f'\n| Name: \"{directory.name}\" \n| Path: "{directory.path}"', 'magenta')
        else:
            cprint(f'Directory shortcut \'{dir_name}\' does not exist!\n' +
                   f'\nUse "dps -n NAME -s PATH" to create one', 'magenta')

    def _copy_path(self, dir_name):
        directory = self.db.get_directory(dir_name)
        if directory:
            cprint(f'Copying {repr(directory.name)} shortcut', 'magenta')
            pyperclip.copy(f'cd "{directory.path}"')
        else:
            cprint(f'Directory shortcut \'{dir_name}\' does not exist!\n' +
                   f'\nUse "dps -n NAME -s PATH" to create one', 'magenta')

    def _display_directories(self):
        self.column_name_max_width = calculate_max_width(
            list(map(lambda directory: directory.name, self.db.directories))
        )

        cprint(
            f'|=> Displaying directories:\n' +
            '\n'.join(map(self._create_row, self.db.directories)),
            color='magenta'
        )

    def _create_row(self, directory) -> str:
        return f'| * {directory.name:<{self.column_name_max_width}}: {repr(directory.path):<20}'

    def _get_compatible_path(self, path: str):
        # return os.path.normpath(path.replace('\ ', ' ').replace('\:', ':')).strip("\'\"")
        return Path(path).resolve()
