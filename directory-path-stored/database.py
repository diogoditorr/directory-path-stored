import os
from os.path import join
import json

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
        pass
    
    def update(self, name, path):
        with open(self._get_json_path()) as file:
            data = json.load(file)

            # Update value
            data['directories'].append({'name': '123', 'path': 'd:/aa'})

            # Transform in json content
            new_json_content = json.dumps(data, indent=2, sort_keys=True)
            print(new_json_content)

        with open(self._get_json_path(), 'w') as file:
            json.dump(data, file, indent=2)

    def delete(self):
        pass

    def list_directories(self) -> list:
        with open(self._get_json_path()) as file:
            data = json.load(file)
            print(data)

    def _get_json_path(self):
        return join(PWD, 'paths.json')

# def _get_json_content(self, file):
#     return file.read().replace('\n', '')

# Loads the file content
# data = json.loads(self._get_json_content(file))
# print(data)

# Load file
# with open('file') as file:
#   data = json load(file)
#   print(data)