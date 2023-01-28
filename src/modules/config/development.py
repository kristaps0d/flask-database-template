class DevelopmentConfig(object):

    SESSION_COOKIE_NAME = "SESSION"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_PERMANENT = False
    SESSION_TYPE = "Cookies"

    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'