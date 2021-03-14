
from src.models import Node
from src.api import Api

class Nodes(Api):
    
    def __init__(self):
        super().__init__()

    def create_model(self):
        self.model = Node()
    
    def get(self,channel):
        data = self.model.getone(channel)
        return data , 200
