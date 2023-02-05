# database
from src.modules.database.table import Table

class Bans(Table):

    def __init__(self, cursor):
        
        # private class variables
        _table = "bans"
        _schema = """(
            id integer PRIMARY KEY,
            addressId integer NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (addressId)
                REFERENCES addresses(id)
        )"""

        super().__init__(cursor, _table, _schema)

    def Insert(self, addressId):
        self._cursor.execute(f'INSERT INTO {self._table}(addressId) VALUES("{addressId}")')

    def SelectId(self, addressId):
        return self._cursor.execute(f'SELECT * FROM {self._table} WHERE addressId = "{addressId}"').fetchall()