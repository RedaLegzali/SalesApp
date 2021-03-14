import mysql.connector as mysql
import os

class Database:

    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def connect(self):
        connection = mysql.connect(
            host = os.getenv('HOST','localhost'),
            user = 'furnitures',
            password = 'furnitures',
            database = 'furnitures',
            port = 3306
        )
        return connection

    def formatall(self,rows):
        array = []
        for row in rows:
            data = {}
            names = list(map(lambda x: x[0], self.cursor.description))
            for name in names:
                data[name] = row[name]
            array.append(data)

        return array
    
    def formatone(self,row):
        data = {}
        names = list(map(lambda x: x[0], self.cursor.description))
        for name in names:
            data[name] = row[name]

        return data

