from typing import Dict, Tuple, DefaultDict
import random
import nltk.tokenize

# types
NGram = Tuple[str, ...]

class NGramModel:
    def __init__(self, txt: str, order: int = 2):
        ngrams = self.ngram_tokenise(txt)
        self.adj_list = self.generate_adj_list(ngrams)
        self.order = order

    def ngram_tokenise(self, text: str) -> list[NGram]:
        """
        Split the text into sentences, then split each sentence into bigrams.
        """
        bigrams: list[NGram] = []
        # 

        return bigrams

    def generate_adj_list(self, bigrams: list[NGram]) -> dict[str, list[str]]:
        """
        Generate an adjacency list from the bigrams.
        """
        generated_adj_list: DefaultDict[str, list[str]] = DefaultDict(list)
        # enter your code here

        return generated_adj_list

    def generate_text(self) -> str:
        """
        Do a random walk through the graph, starting at the start token.
        """
        sentence: list[str] = []
        # enter your code here

        return ' '.join(sentence[:-1])
    
    def toJson(self):
        return {"model": self.adj_list, "order": self.order}

    @classmethod
    def fromAdjList(cls, adj_list: Dict[NGram, list[str]], order: int) -> 'NGramModel':
        instance = cls.__new__(cls)  # Create an "empty" instance
        instance.adj_list = adj_list
        instance.order = order
        return instance

    