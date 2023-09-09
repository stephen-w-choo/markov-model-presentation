import json
import ast
from typing import Any, Dict, DefaultDict

def read_text_file(relative_path: str) -> str:
    with open(relative_path, 'r') as f:
        return f.read()
    
def write_text_file(text: str, relative_path: str):
    with open(relative_path, 'w') as f:
        f.write(text)    

def write_dict_to_json_file(dictionary: Dict[Any, Any], relative_path: str):
    converted_dict = {"model": tuple_keys_to_str(dictionary["model"]), "order": dictionary["order"]}
    with open(relative_path, 'w') as f:
        json.dump(converted_dict, f)

def read_json_file(relative_path: str) -> Dict[Any, Any]:
    with open(relative_path, 'r') as f:
        data = json.load(f)
    data["model"] = DefaultDict(list, str_keys_to_tuple(data["model"]))
    return data

def tuple_keys_to_str(dictionary: Dict[Any, Any]) -> Dict[str, Any]:
    return {str(k): v for k, v in dictionary.items()}

def str_keys_to_tuple(dictionary: Dict[str, Any]) -> Dict[Any, Any]:
    return {ast.literal_eval(k): v for k, v in dictionary.items() if k.startswith('(') and k.endswith(')')}