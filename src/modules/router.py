# libs
from flask import render_template

class Router(object):
    """
        Handles routing by directing
        url and acces methods
    """

    def __new__(self, url, method, status):
        
        if (status == 'REJECTED'):
            return render_template('403.html', title='403')

        if (method == 'POST'):
            return render_template('403.html', title='403')

        if (url == '/'):
            return render_template('index.html', title='Home page')

        return render_template('404.html', title='404')