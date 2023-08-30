import json
from typing import Any, Dict


def read_text_file(relative_path: str) -> str:
    with open(relative_path, 'r') as f:
        return f.read()
    
def write_text_file(text: str, relative_path: str):
    with open(relative_path, 'w') as f:
        f.write(text)
    
# write a function that takes a dictionary and writes it to a json file
def write_dict_to_json_file(dictionary: Dict[Any, Any], relative_path: str):
    with open(relative_path, 'w') as f:
        json.dump(dictionary, f)

# write a function that takes a relative path to a json file and returns a dictionary
def read_json_file(relative_path: str):
    with open(relative_path, 'r') as f:
        return json.load(f)
    
