
from src.models import Database

class Product(Database):
    
    def __init__(self):
        super().__init__()

    def getone(self,node):
        sql = 'select p.id as "id", p.name as "name", p.image as "image" from products p inner join nodes n on p.node_id = n.id where n.id = %s;'
        try:
            self.cursor.execute(sql,[node,])
            data = self.cursor.fetchall()
            return self.formatall(data)
        except:
            return {}
