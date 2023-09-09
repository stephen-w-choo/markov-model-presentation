import lib.file_io as file_io
from lib.markovclass import NGramModel
from os.path import basename
import sys

JSON_OUTPUT_PATH = "/data/model_json"

def make_model(file_path: str, order: int = 2):
    text = file_io.read_text_file(file_path)
    model = NGramModel(text, order)
    file_io.write_dict_to_json_file(
        model.toJson(), 
        f"./{JSON_OUTPUT_PATH}/{basename(file_path)}.json"
    )

def generate_text(file_path: str):
    json = file_io.read_json_file(f"{JSON_OUTPUT_PATH}/{file_path}.json")
    model = NGramModel.fromAdjList(json["model"], json["order"])
    generated_text = model.generate_text()
    print(generated_text)


if __name__ == '__main__':
    ERROR_MESSAGE = f"Usage: python3 main.py <command> <file_path> <order/sentence no>. Valid commands are {', '.join(commands.keys())}."

    COMMANDS = {
        "makemodel": make_model,
        "generatetext": generate_text
    }
    
    if len(sys.argv) < 3:
        print(ERROR_MESSAGE)
        sys.exit(1)

    command, file_path, num = sys.argv[1], sys.argv[2], sys.argv[3]

    if command not in COMMANDS: # check if command is valid
        print(ERROR_MESSAGE)
        sys.exit(1)
    
    COMMANDS[command](file_path)
    sys.exit(0)
        