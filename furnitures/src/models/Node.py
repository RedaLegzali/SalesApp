
from src.models import Database

class Node(Database):
    
    def __init__(self):
        super().__init__()

    def getone(self,channel):
        sql = 'select n.id as "id", n.name as "name" from nodes n inner join channels_nodes cn on n.id = cn.node_id inner join channels c on cn.channel_id = c.id where c.id = %s;'
        try:
            self.cursor.execute(sql,[channel,])
            data = self.cursor.fetchall()
            return self.formatall(data)
        except:
            return {}
