#!/usr/bin/env python3

import lib.file_io as file_io
from lib.model_class import NGramModel
import click
import sys

JSON_OUTPUT_PATH = "data/model_json"
TXT_OUTPUT_PATH = "/data/output_txt"

def main():
    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        order = int(sys.argv[2])
    else:
        order = 1
    generate_text(make_model(file_path, order), 20)

def make_model(file_path: str, order: int = 1):
    text = file_io.read_text_file(file_path)
    model = NGramModel(text, order)
    output_path = f"./{JSON_OUTPUT_PATH}/{file_io.file_name(file_path)}.json"
    file_io.write_dict_to_json_file(
        model.toJson(), 
        f"./{JSON_OUTPUT_PATH}/{file_io.file_name(file_path)}.json"
    )
    return output_path

def generate_text(file_path: str, num_sentences: int = 20):
    json = file_io.read_json_file(file_path)
    model = NGramModel.fromAdjList(json["model"], json["order"])
    output_file = open(f"./{TXT_OUTPUT_PATH}/{file_io.file_name(file_path)}_generated.txt", "w")

    for _ in range(int(num_sentences)):
        generated_text = model.generate_text()
        output_file.write(generated_text + "\n\n")
        formatted_print(generated_text + "\n\n")

def formatted_print(text: str):
    # limit chars per line to 80, while preserving words
    words = text.split(" ")
    line = ""
    for word in words:
        if len(line + word) > 80:
            print(line)
            line = ""
        line += word + " "


if __name__ == '__main__':
    main()