import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, path):
        self.path = path
        try:
            self.connection = sqlite3.connect(path, check_same_thread=False)
            self.cursor = self.connection.cursor()
        except Error as e:
            raise Error(e)

    def select(self, table: str, id = None):
        query = f'SELECT * FROM \'{table}\''
        if id:
            query += f'WHERE id = {str(id)}'
        query += ';'

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, table, data):
        if not data:
            raise Error('Wrong data format')

        fields = ''
        values = '\''
        for key, value in data.items():
            fields += key + ','
            values += value + '\',\''

        fields = fields[:len(fields)-1]
        values = values[:len(values)-2]

        query = f'INSERT INTO {table}({fields}) VALUES({values})'
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, table, data):
        if not data or not data.id:
            raise Error('Wrong data format')
        query = f'UPDATE {str(table)} SET '
        
        for key, value in data.items():
            query += f'{str(key)} = {str(value)}'

        query += f'WHERE id = {str(data.id)};'
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def exec_query(self, query: str):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Error as e:
            raise Error('Query Error', e)
