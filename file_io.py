import os.path
import json

# write a function that takes a relative path and returns the absolute path
def get_absolute_path(relative_path: str) -> str:
    return os.path.abspath(relative_path)


# write a function that takes a relative path to a text file and returns a string
def read_text_file(relative_path: str) -> str:
    with open(relative_path, 'r') as f:
        return f.read()
    
# write a function that takes a dictionary and writes it to a json file
def write_dict_to_json_file(dictionary: dict, relative_path):
    with open(relative_path, 'w') as f:
        json.dump(dictionary, f)

# write a function that takes a relative path to a json file and returns a dictionary
def read_json_file(relative_path: str) -> dict:
    with open(relative_path, 'r') as f:
        return json.load(f)