import nltk.tokenize
from lib.markovclass import MarkovModel
import random

def ngram_tokenise(text: str, n: int) -> list[list[str]]:
        """
        Tokenises a passage into ngrams.
        
        Takes a passage as a string and returns a list of ngrams for a given order.
        """

        ngrams: list[list[str]] = []

        sentences: list[str] = nltk.tokenize.sent_tokenize(text) # split into sentences

        for sentence in sentences:
            sentence = '///START ' + sentence + ' END///' # add start and end tokens
            words = nltk.tokenize.word_tokenize(sentence) # split into list of words
            for i in range(len(words) - n + 1): # build ngrams
                ngrams.append(words[i:i+n])

        return ngrams

def generate_adj_list(ngrams: list[list[str]]) -> MarkovModel:
        """
        Takes a list of ngrams and builds an adjacency list, which will act as a predictive
        model for words.

        The adjacency list will represent a directed graph where each node is a word 
        and each edge is a transition between words. The ngrams are split such that
        the first n-1 words are the key and the last word is the value.
        """
        adj_list: dict[tuple[str], list[str]] = {}
        model_order = len(ngrams[0]) - 1

        for ngram in ngrams:
            key = tuple(ngram[:-1]) # joins all but the last word as a tuple
            if key in adj_list:
                adj_list[key].append(ngram[-1])
            else:
                adj_list[key] = [ngram[-1]]

        return MarkovModel(adj_list=adj_list, order=model_order)

def generate_text(model: MarkovModel, n: int) -> str:
    sentence: list[str] = []
    
    def get_random_start_key(model: dict[tuple[str], list[str]]) -> tuple[str]:
        return random.choice(list(model.keys()))

    def get_random_word(words: list[str]) -> str:
        return random.choice(words)

    current_token = get_random_start_key(model.adj_list)

    while current_token in model.adj_list:
        sentence.append(current_token[-1])
        current_token = current_token[1:] + (get_random_word(model.adj_list[current_token]),)

    return ' '.join(sentence)

if __name__ == '__main__':
    text = 'This is a test sentence. This is another test sentence. This is a third test sentence.'
    ngrams = ngram_tokenise(text, 3)
    print(ngrams)
    model = generate_adj_list(ngrams)
    print(model)