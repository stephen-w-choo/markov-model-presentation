class MarkovModel:
    def __init__(self, adj_list: dict[tuple[str], list[str]], order: int = 2):
        self.adj_list = adj_list
        self.order = order


    @classmethod
    def fromJson(cls, jsonModel):
        return MarkovModel(jsonModel["model"], jsonModel["order"])
    
    def toJson(self):
        return {"model": self.adj_list, "order": self.order}