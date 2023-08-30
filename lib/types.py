from typing import TypedDict

class MarkovModel(TypedDict):
    n: int
    adj_list: dict[tuple[str], list[str]]

