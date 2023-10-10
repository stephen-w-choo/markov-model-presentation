from typing import Dict, Tuple, List, DefaultDict
import random
import nltk.tokenize

# types
NGram = Tuple[str, ...]
NextWords = List[str]
NextWordFrequencies = Dict[str, int]

class NGramModel:
    def __init__(self, txt: str, order: int = 2):
        ngrams = self.ngram_tokenise(txt, order + 1)
        self.adj_list = self.generate_adj_list(ngrams)
        self.order = order

    def ngram_tokenise(self, text: str, n: int) -> list[NGram]:
        ngrams: list[NGram] = []
        
        sentences: list[str] = nltk.tokenize.sent_tokenize(text) 

        for sentence in sentences:
            sentence = '///START ' + sentence + ' END///' # add start and end tokens
            words = sentence.split()
            for i in range(len(words) - n + 1):
                ngrams.append(tuple(words[i:i+n]))

        return ngrams

    def generate_adj_list(self, ngrams: list[NGram]) -> dict[NGram, NextWords]:
        generated_adj_list: DefaultDict[NGram, NextWords] = DefaultDict(list)

        for ngram in ngrams:
            key = tuple(ngram[:-1])
            generated_adj_list[key].append(ngram[-1])

        return generated_adj_list

    def generate_text(self) -> str:
        sentence: list[str] = []

        # get all the tokens that begin with '///START'
        start_tokens = [token for token in self.adj_list.keys() if token[0] == '///START']

        current_token = random.choice(start_tokens)

        # add the first n-1 words to the sentence
        sentence.extend(current_token[1:-1])

        while current_token in self.adj_list:
            sentence.append(current_token[-1])
            current_token = current_token[1:] + (random.choice(self.adj_list[current_token]),)

        return ' '.join(sentence)
    
    def toJson(self):
        return {"model": self.adj_list, "order": self.order}

    @classmethod
    def fromAdjList(cls, adj_list: Dict[NGram, NextWords], order: int) -> 'NGramModel':
        instance = cls.__new__(cls)  # Create an "empty" instance
        instance.adj_list = adj_list
        instance.order = order
        return instance

    