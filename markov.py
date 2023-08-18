import nltk.tokenize
nltk.download('punkt')
import random

def n_gram_tokeniser(text: str, n: int) -> list[list[str]]:
    ngrams: list[list[str]] = []
    sentences: list[str] = nltk.tokenize.sent_tokenize(text)

    for sentence in sentences:
        sentence = '///START ' + sentence + ' END///'
        words = nltk.tokenize.word_tokenize(sentence)
        for i in range(len(words) - n + 1):
            ngrams.append(words[i:i+n])

    return ngrams

def generate_markov_model(ngrams: list[list[str]]) -> dict[str, list[str]]:
    markov_model: dict[str, list[str]] = {}

    for ngram in ngrams:
        key = ' '.join(ngram[:-1]) # joins all but the last word
        if key in markov_model:
            markov_model[key].append(ngram[-1])
        else:
            markov_model[key] = [ngram[-1]]

    return markov_model

def generate_sentence(model: dict[tuple[str], list[str]], n: int) -> str:
    sentence: list[str] = []
    
    current_token = get_random_key(model)

    while current_token in model:
        sentence.append(current_token[-1])
        current_token = current_token[1:] + (get_random_word(model[current_token]),)

    return ' '.join(sentence)

def get_random_key(model: dict[tuple[str], list[str]]) -> tuple[str]:
    return random.choice(list(model.keys()))

def get_random_word(words: list[str]) -> str:
    return random.choice(words)


if __name__ == '__main__':
    text = 'This is a test sentence. This is another test sentence. This is a third test sentence.'
    ngrams = n_gram_tokeniser(text, 3)
    print(ngrams)
    model = generate_markov_model(ngrams)
    print(model)