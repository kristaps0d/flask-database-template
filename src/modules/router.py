# libs
from flask import render_template

# auth
from src.modules.auth.wrapper import AuthWrapper

class Router(object):
    """
        Handles routing by directing
        url and acces methods
    """

    def __new__(self, url, method, status, address):
        
        if (status == 'REJECTED'):
            return render_template('403.html', title='403')

        if (method == 'POST'):
            return render_template('403.html', title='403')

        if (url == '/'):
            return render_template('index.html', title='Home page')

        if (url == '/auth'):
            with AuthWrapper() as auth:
                
                ###
                # implement browser cookies
                # currently hardcoded session "example"
                _ret = auth.checkSession('example', address)

                if (_ret):
                    return render_template('auth/index.html', title='Success!')

                if (not _ret):
                    return render_template('403.html')

        return render_template('404.html', title='404')