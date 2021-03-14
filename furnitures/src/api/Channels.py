
from src.models import Channel
from src.api import Api

class Channels(Api):
    
    def __init__(self):
        super().__init__()

    def create_model(self):
        self.model = Channel()
    
    def get(self):
        data = self.model.get() 
        return data , 200
