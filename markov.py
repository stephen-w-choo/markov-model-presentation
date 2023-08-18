import nltk.tokenize
import random

def n_gram_tokeniser(text: str, n: int) -> list[list[str]]:
    ngrams: list[list[str]] = []
    sentences: list[str] = nltk.tokenize.sent_tokenize(text)

    for sentence in sentences:
        sentence = '///START' + sentence + 'END///'
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
    
    # depth first search through the model


    # def dfs(key: tuple[str]):
    #     if key not in model:
    #         return
    #     word = random.choice(model[key])
    #     sentence.append(word)
    #     dfs(key[1:] + (word,))

def get_random_key(model: dict[tuple[str], list[str]]) -> tuple[str]:
    return random.choice(list(model.keys()))


if __name__ == '__main__':
    text = 'This is a test sentence. This is another test sentence. This is a third test sentence.'
    print(n_gram_tokeniser(text, 3))