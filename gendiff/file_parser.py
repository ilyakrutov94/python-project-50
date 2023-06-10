import json
import yaml


def parse_file(file_path: str) -> str | None:
    '''
    loads json and yaml files in Python
    If file doesn't exist returns - Can't find "file"
    '''
    try:
        if file_path.endswith('json'):
            with open(file_path) as file:
                return json.load(file)
        elif file_path.endswith('yml') or file_path.endswith('yaml'):
            with open(file_path) as file:
                return yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't find \"{file_path}\"")


def open_file(file_path: str) -> str | None:
    try:
        with open(file_path) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't find \"{file_path}\"")
