# Simple Markov Text Model Generator

This repository is used for a presentation I've given on simple Markov models, and predictive language models in general.

In this repository - I've implemented a simple Markov Model (with options for higher order models) from scratch in plain Python. I've tried to do it with as minimal abstractions as possible - just to illustrate what I think is both a really simple, and elegant concept. The one exception is using NLTK for tokenisation - because tokenisation itself is very much a non-trivial task to implement from scratch.

For more detailed information and a guided walkthrough, refer to the presentation available at this link:
[Markov Models Presentation Link](https://1drv.ms/p/s!AoWkMbbsIE9RiDGFlIlBdx7g0mHC?e=dbtPgQ)

This project is designed to illustrate and teach the concepts of simple Markov text models. It includes a set of literature text files sourced from Project Gutenberg and provides a hands-on approach to understanding and generating text with Markov models.

## Usage

### Generating a Markov Model

Use the following command to generate a simple Markov model:
`python3 main.py make-model --order 3 data/input_txt/homer_iliad.txt`
--order is an optional argument that specifies the order of the Markov model. The default value is 3.

### Generating Text from a Model
To generate sentences from the Markov model, use:
`python3 main.py generate-text data/model_json/dracula.json`
You can use the optional argument --sentences to specify the number of sentences to generate. The default value is 20
Sentences will be generated under output_data

### Adding Your Own Text Files
You can also add your own text files to the data/input_txt/ directory to generate your own models.

### Starter Branch
A starter branch is available where some of the method code is left unfinished. You can find this branch in the repository and fill in the code as per the instructions provided, if you'd like to try applying the concepts yourself.
