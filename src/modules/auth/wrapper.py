
# database
from src.modules.database.connection import DbConnection
from src.modules.database.cursor import DbCursor

from src.modules.database.schemas.addresses import Addresses
from src.modules.database.schemas.sessions import Sessions
from src.modules.database.schemas.users import Users

class AuthWrapper(object):
    """
        Authentication wrappec object
        ment to be used with __enter__
        functionality (example 1):

        with AuthWrapper(..) as auth:
            if auth.isAuth(session):
                ..

            if not auth.isAuth(session):
                ..
    """

    def __init__(self):
        pass

    def newSession(self):
        return False

    def checkSession(self, session, address):
        
        with DbConnection('DB_URI') as con:
            with DbCursor(con) as cur:
            
                # get and check session
                SessionsTable = Sessions(cur)
                _aid = SessionsTable.checkSession(session)

                # no session exists with that key
                if (not _aid):
                    return False

                # check if ip is correct
                AddressesTable = Addresses(cur)
                _address = AddressesTable.SelectAddressById(_aid)

                if (not _address):
                    return False

                if (address != _address):
                    return False

                return True

        return False

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return self