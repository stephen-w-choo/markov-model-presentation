#!/usr/bin/env python3

import lib.file_io as file_io
from lib.markov_class import NGramModel
import click

JSON_OUTPUT_PATH = "/data/model_json"
TXT_OUTPUT_PATH = "/data/output_txt"

@click.command()
@click.argument('file_path', type=click.Path(exists=True, readable=True))
@click.option('--order', default=2, type=int, help='Order for the n-gram model.')
def make_model(file_path: str, order: int = 2):
    text = file_io.read_text_file(file_path)
    model = NGramModel(text, order)
    file_io.write_dict_to_json_file(
        model.toJson(), 
        f"./{JSON_OUTPUT_PATH}/{file_io.file_name(file_path)}.json"
    )

@click.command()
@click.argument('file_path', type=click.Path(exists=True, readable=True))
@click.option('--num-sentences', default=20, type=int, help='Number of sentences to generate.')
def generate_text(file_path: str, num_sentences: int = 20):
    json = file_io.read_json_file(file_path)
    model = NGramModel.fromAdjList(json["model"], json["order"])
    output_file = open(f"./{TXT_OUTPUT_PATH}/{file_io.file_name(file_path)}_generated.txt", "w")
    for _ in range(int(num_sentences)):
        generated_text = model.generate_text()
        print(generated_text)
        output_file.write(generated_text + "\n\n")

@click.group()
def cli():
    pass

cli.add_command(make_model)
cli.add_command(generate_text)

if __name__ == '__main__':
    cli()