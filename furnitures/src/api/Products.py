
from src.models import Product
from src.api import Api

class Products(Api):
    
    def __init__(self):
        super().__init__()

    def create_model(self):
        self.model = Product()
    
    def get(self,node):
        data = self.model.getone(node)
        return data , 200
