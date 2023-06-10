import json


def make_json(source: dict) -> str:
    '''Returns json from diffence_dict'''
    return json.dumps(source, indent=4)
