import os
import sys
import json
from typing import Union
from os.path import join

from .directory import Directory
from ..exceptions import OverwriteError


PWD = os.path.dirname(sys.argv[0])


class Database():
    def __init__(self):
        self.directories = []

    def create(self):
        with open(self.database_path(), 'w') as file:
            json.dump(
                {
                    "directories": []
                },
                file,
                indent=2
            )

    def save(self, name: str, path: str):
        self.get_data()

        # Check if exits
        if not self._directory_exists(name):
            self.directories.append(Directory(name, path))
        else:
            raise OverwriteError

        self._commit_data()

    def update(self, dir_name: str, path: str):
        self.get_data()

        # Update value
        directory = self.get_directory(dir_name)
        if directory:
            directory.path = path
        else:
            raise ValueError

        # Transform in json content
        # new_json_content = json.dumps(data, indent=2, sort_keys=True)
        # print(new_json_content)

        self._commit_data()

    def delete(self, dir_name: str):
        self.get_data()

        directory = self.get_directory(dir_name)
        if directory:
            self.directories.remove(directory)
        else:
            raise ValueError

        self._commit_data()

    def get_data(self):
        with open(self.database_path()) as file:
            self.directories = [
                Directory(direc['name'], direc['path'])
                for direc in json.load(file)['directories']
            ]

    def get_directory(self, dir_name: str) -> Union[Directory, None]:
        for directory in self.directories:
            if dir_name.lower() == directory.name.lower():
                return directory

        return None

    def database_path(self):
        return join(PWD, 'paths.json')

    def _directory_exists(self, dir_name: str):
        for directory in self.directories:
            if dir_name.lower() == directory.name.lower():
                return True

        return False

    def _commit_data(self):
        if self.directories:
            with open(self.database_path(), 'w') as file:
                data = dict()
                data['directories'] = []

                for directory in self.directories:
                    data['directories'].append(
                        {'name': directory.name, 'path': directory.path})

                json.dump(data, file, indent=2)
        else:
            raise Exception()

# def _get_data(self, file):
#     return file.read().replace('\n', '')

# Loads the file content
# data = json.loads(self._get_data(file))
# print(data)

# Load file
# with open('file') as file:
#   data = json load(file)
#   print(data)
