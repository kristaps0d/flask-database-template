# libs
import datetime

# database
from src.modules.database.table import Table

class Sessions(Table):

    def __init__(self, cursor):
        
        # private class variables
        _table = "sessions"
        _schema = """(
            id integer PRIMARY KEY,
            userId integer NOT NULL,
            addressId integer NOT NULL,

            session TEXT NOT NULL UNIQUE,

            expiresAt DATETIME,
            lockedAt DATETIME,

            createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (userId)
                REFERENCES users(id),

            FOREIGN KEY (addressId)
                REFERENCES addresses(id)
            
        )"""

        super().__init__(cursor, _table, _schema)

    def Insert(self, userId, addressId, session):
        self._cursor.execute(f'INSERT INTO {self._table}(userId, addressId, session) VALUES("{userId}", "{addressId}", "{session}")')

    def FindSessionRow(self, session):
        # A slower approach, but no need for sanitization
        for _row in self.SelectTable():
            if session == _row[3]:
                return _row

    def checkSession(self, session):
        _row = self.FindSessionRow(session)

        # check if even exists
        if (_row == None):
            return False

        # unpack
        (pid, uid, aid, session, expireAt, lockedAt, createdAt) = _row

        # check if session is not expired
        if (expireAt) and (datetime.datetime.now() > datetime.datetime.strptime(expireAt, '%Y-%m-%d %H:%M:%S')):
            return False

        # check if session is locked
        if (lockedAt) and (datetime.datetime.now() > datetime.datetime.strptime(lockedAt, '%Y-%m-%d %H:%M:%S')):
            return False

        # if createdAt in future, (possibly mitigating bitflips)
        if (createdAt) and (datetime.datetime.now() < datetime.datetime.strptime(createdAt, '%Y-%m-%d %H:%M:%S')):
            return False

        return aid

    def LockSession(self, session):
        _res = self.FindSessionRow(session)

        if len(_res) < 1:
            return False

        (_id, _userid, _addressid, _session, _expiresAt, _lockedAt, _createdAt) = _res
        self._cursor.execute(f'UPDATE {self._table} SET lockedAt = CURRENT_TIMESTAMP WHERE id = {_id}')