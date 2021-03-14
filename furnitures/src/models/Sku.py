
from src.models import Database

class Sku(Database):
    
    def __init__(self):
        super().__init__()

    def get(self,product):
        sql = 'select s.id as "id", s.name as "name", s.quantity as "quantity", round(s.price,2) as "original", round(s.price*s.promotion,2) as "price", s.image as "image" from skus s inner join products p on s.product_id = p.id where p.id = %s;'
        try:
            self.cursor.execute(sql,[product,])
            data = self.cursor.fetchall()
            return self.formatall(data)
        except:
            return {}

    def getone(self,product,id):
        sql = 'select s.id as "id", s.name as "name", s.quantity as "quantity", round(s.price,2) as "original", round(s.price*s.promotion,2) as "price", s.image as "image" from skus s inner join products p on s.product_id = p.id where p.id = %s and s.id = %s;'
        try:
            self.cursor.execute(sql,[product,id])
            data = self.cursor.fetchone()
            return self.formatone(data)
        except:
            return {}
