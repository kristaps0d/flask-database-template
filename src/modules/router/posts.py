# libs
from flask import render_template, request, make_response, redirect
import time

# auth
from src.modules.auth.cookies import CookieHandler
from src.modules.auth.sessions import NewSessionToken

# database
from src.modules.database.connection import DbConnection
from src.modules.database.cursor import DbCursor

from src.modules.database.schemas.site.users import Users
from src.modules.database.schemas.site.addresses import Addresses
from src.modules.database.schemas.site.sessions import Sessions

from src.modules.database.schemas.products import Products

class PostsHandler(object):
    def __new__(self, url, address):

        if (url == '/auth/create-session'):
            _json = request.json
            _username, _password = _json['username'], _json['password']

            # create session
            with DbConnection('DB_URI') as con:
                with DbCursor(con) as cur:
                    # get user id
                    UsersTable = Users(cur)
                    _uid = UsersTable.SelectIdByCreds(_username, _password)

                    if (not _uid):
                        return '404'

                    # get address id
                    AddressesTable = Addresses(cur)
                    (_aid, _address) = AddressesTable.SelectAddress(address)[0]

                    # create session
                    _session = NewSessionToken(address)
                    SessionsTable = Sessions(cur)
                    SessionsTable.Insert(_uid, _aid, _session)
            
            with CookieHandler('COOKIE_NAME') as handle:
                _res = make_response('200')
                _res.set_cookie(handle.getCookieName(), _session)
                return _res

        return render_template('403.html')

class AuthPostsHandler(object):
    def __new__(self, url, address):

        if (url == '/table/products'):
            
            with DbConnection('DB_URI') as con:
                with DbCursor(con) as cur:
                    ProductsTable = Products(cur)
                    _table = ProductsTable.SelectTable()

            return _table

        return render_template('403.html')