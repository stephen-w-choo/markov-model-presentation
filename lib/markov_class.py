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
        bigrams: list[NGram] = []
        """
        Split the text into sentences, then split each sentence into bigrams.
        """
        sentences = nltk.tokenize.sent_tokenize(text)

        for sentence in sentences:
            sentence = "///START " + sentence + " ///END"
            tokens = sentence.split(" ")
            for i in range(len(tokens) - 1):
                bigrams.append((tokens[i], tokens[i + 1]))
                
        return bigrams

    def generate_adj_list(self, bigrams: list[NGram]) -> dict[str, list[str]]:
        generated_adj_list: DefaultDict[str, list[str]] = DefaultDict(list)
        """
        Generate an adjacency list from the bigrams.
        """

        for bigram in bigrams:
            generated_adj_list[bigram[0]].append(bigram[1])
        print(generated_adj_list)
        return generated_adj_list

    def generate_text(self) -> str:
        sentence: list[str] = []
        """
        Do a random walk through the graph, starting at the start token.
        """
        current_token = "///START"

        while current_token != "///END":
            current_token = random.choice(self.adj_list[current_token])
            sentence.append(current_token)

        return ' '.join(sentence[:-1])
    
    def toJson(self):
        return {"model": self.adj_list, "order": self.order}

    @classmethod
    def fromAdjList(cls, adj_list: Dict[NGram, list[str]], order: int) -> 'NGramModel':
        instance = cls.__new__(cls)  # Create an "empty" instance
        instance.adj_list = adj_list
        instance.order = order
        return instance

    