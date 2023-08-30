import lib.file_io as file_io
import lib.markov_utils as markov_utils
from lib.markovclass import MarkovModel
import sys

JSON_OUTPUT_PATH = "/data/model_json"

def make_model(file_path: str):
    ngrams = markov_utils.ngram_tokenise(file_io.read_text_file(file_path), 3)
    model = markov_utils.generate_adj_list(ngrams)
    file_io.write_dict_to_json_file(model.toJson(), f"{JSON_OUTPUT_PATH}/{file_path}.json")

def generate_text(file_path: str):
    model = file_io.read_json_file(f"{file_path}.json")
    generated_text = markov_utils.generate_text(MarkovModel.fromJson(model), 3)
    print(generated_text)

commands = {
    "makemodel": make_model,
    "generatetext": generate_text
}

error_message = f"Usage: python3 main.py <command> <file_path>. Valid commands are {', '.join(commands.keys())}."

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(error_message)
        sys.exit(1)

    command = sys.argv[1]
    file_path = sys.argv[2]

    # check if command is valid
    if command not in commands:
        print(error_message)
        sys.exit(1)
    
    # run the command
    commands[command](file_path)
        