# database
from src.modules.database.table import Table

class Users(Table):

    def __init__(self, cursor):
        
        # private class variables
        _table = "users"
        _schema = """(
            id integer PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            createdAt DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""

        super().__init__(cursor, _table, _schema)

    def Insert(self, username, password):
        self._cursor.execute(f'INSERT INTO {self._table}(username, password) VALUES("{username}", "{password}")')

    def SelectIdByCreds(self, username, password):
        _table = self.SelectTable()

        # slower but more secure way (doesn't require sanitization)
        for (_id, _username, _password, _createdAt) in _table:
            if (_username == username) and (_password == password):
                return _id

        return None