
from src.models import Database

class Channel(Database):
    
    def __init__(self):
        super().__init__()

    def get(self):
        sql = 'select * from channels order by id;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return self.formatall(data)
