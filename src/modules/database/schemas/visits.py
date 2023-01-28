from ..table import Table

class Visits(Table):

    def __init__(self, cursor):
        
        # private class variables
        _table = "visits"
        _schema = """(
            id integer PRIMARY KEY,

            addressId integer NOT NULL,
            path TEXT NOT NULL,
            method TEXT NOT NULL,
            status TEXT NOT NULL,

            date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (addressId)
                REFERENCES addresses(id)
        )"""

        super().__init__(cursor, _table, _schema)

    def Insert(self, addressId, path, method, status):
        self._cursor.execute(f'INSERT INTO {self._table}(addressId, path, method, status) VALUES("{addressId}", "{path}", "{method}", "{status}")')