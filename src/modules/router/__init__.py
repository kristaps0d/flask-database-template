# libs
from flask import render_template, request, make_response

# auth
from src.modules.auth.wrapper import AuthWrapper
from src.modules.auth.cookies import CookieHandler

# routing
from src.modules.router.posts import PostsHandler, AuthPostsHandler
from src.modules.router.gets import GetsHandler, AuthGetsHandler

class Router(object):
    """
        Handles routing by directing
        url and acces methods
    """

    def __new__(self, url, method, status, address):
        
        if (status == 'REJECTED'):
            return render_template('403.html', title='403')

        with AuthWrapper() as auth:

            with CookieHandler('COOKIE_NAME') as handle:
                _state = auth.checkSession(handle.getCookie(), address)

            # routing
            if (method == 'POST') and (_state):
                return AuthPostsHandler(url, address)

            if (method == 'GET') and (_state):
                return AuthGetsHandler(url, address)

            if (method == 'POST') and (not _state):
                return PostsHandler(url, address)
            
            if (method == 'GET') and (not _state):
                return GetsHandler(url, address)

        return render_template('500.html')