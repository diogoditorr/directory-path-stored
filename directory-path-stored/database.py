import os
import json
from typing import Union
from os.path import join

PWD = os.path.dirname(__file__)

class JsonDatabase():
    def __init__(self):
        pass

    def create(self):
        with open(self._get_json_path(), 'w') as file:
            json.dump(
                {
                    "directories": []
                }, 
                file, 
                indent=2
            )

    def save(self, name, path):
        data = self._get_json_content()

        # Check if exits
        index = self._get_directory_index(data, name)
        if index is None:
            data['directories'].append({
                'name': name,
                'path': path
            })
        else:
            print(f"Directory shortcut '{name}' already exists")
            return

        self._commit_data(data)
    
    def update(self, dir_name, path):
        data = self._get_json_content()

        # Update value
        index = self._get_directory_index(data, dir_name)
        if index is not None:
            data['directories'][index]['path'] = path
        else:
            print(f"Directory shortcut '{dir_name}' does not exist")
            return

        # Transform in json content
        new_json_content = json.dumps(data, indent=2, sort_keys=True)
        print(new_json_content)

        self._commit_data(data)

    def delete(self, dir_name: str):
        data = self._get_json_content()

        index = self._get_directory_index(data, dir_name)
        if index is not None:
            del data['directories'][index]
        else:
            print(f"Directory shortcut '{dir_name}' does not exist")
            return

        self._commit_data(data)        

    def list_directories(self) -> list:
        print(self._get_json_content()['directories'])

    def get_directory_path(self, dir_name) -> Union[str, None]:
        data: dict = self._get_json_content()

        index = self._get_directory_index(data, dir_name)
        if index is not None:
            return data['directories'][index]['path']
        else:
            print(f"Directory shortcut '{dir_name}' does not exist")
            return None

    def _get_json_content(self):
        with open(self._get_json_path()) as file:
            return json.load(file)

    def _get_json_path(self):
        return join(PWD, 'paths.json')

    def _get_directory_index(self, data: dict, indentifier: str) -> Union[int, None]:
        try:
            first_ocorrency = [directory for directory in data['directories'] if directory['name'] == indentifier]
            if first_ocorrency:
                first_ocorrency = first_ocorrency[0]
            else:
                raise ValueError
            return data['directories'].index(first_ocorrency)

        except ValueError:
            return None

    def _commit_data(self, data: dict):
        with open(self._get_json_path(), 'w') as file:
            json.dump(data, file, indent=2)

# def _get_json_content(self, file):
#     return file.read().replace('\n', '')

# Loads the file content
# data = json.loads(self._get_json_content(file))
# print(data)

# Load file
# with open('file') as file:
#   data = json load(file)
#   print(data)