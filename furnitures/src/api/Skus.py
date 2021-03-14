
from src.models import Sku
from src.api import Api

class Skus(Api):
    
    def __init__(self):
        super().__init__()

    def create_model(self):
        self.model = Sku()
    
    def get(self,product,id=None):
        data = self.model.get(product) if id is None else self.model.getone(product,id)
        return data , 200
