# libs
from flask import render_template, request, make_response, redirect
import time

# auth
from src.modules.auth.cookies import CookieHandler

# database
from src.modules.database.connection import DbConnection
from src.modules.database.cursor import DbCursor

from src.modules.database.schemas.site.sessions import Sessions

class GetsHandler(object):
    def __new__(self, url, address):

        if (url == '/'):
            return render_template('index.html')

        return redirect('/')

class AuthGetsHandler(object):
    def __new__(self, url, address):

        if (url == '/logout'):
            with CookieHandler('COOKIE_NAME') as handle:
                _session = handle.getCookie()

                with DbConnection('DB_URI') as con:
                    with DbCursor(con) as cur:
                        SessionsTable = Sessions(cur)
                        SessionsTable.LockSession(_session)
                
                _res = make_response(redirect('/'))
                _res.delete_cookie(handle.getCookieName())
                return _res
        
        if (url == '/'):
            return render_template('auth/index.html')

        return redirect('/')