from ..table import Table

class Addresses(Table):

    def __init__(self, cursor):
        
        # private class variables
        _table = "addresses"
        _schema = """(
            id integer PRIMARY KEY,
            address text NOT NULL UNIQUE
        )"""

        super().__init__(cursor, _table, _schema)

    def Insert(self, address):
        self._cursor.execute(f'INSERT INTO {self._table}(address) VALUES("{address}")')

    def SelectAddress(self, address):
        return self._cursor.execute(f'SELECT * FROM {self._table} WHERE address = "{address}"').fetchall()