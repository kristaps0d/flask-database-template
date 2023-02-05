# libs
from flask import request

# utils
from src.utils.environment import Environment

class CookieHandler(Environment):
    """
        Cookie handler, setter, getter
        to be used in "with" context

        (example):
        with CookieHandler(cookieNameEnv) as handle:
            handle.set(value)
            value = handle.get()
    """

    def __init__(self, cookieNameEnv):
        super().__init__()

        # class variables
        self._cookie_env_key = cookieNameEnv
        self._cookie_name = self.getenv(self._cookie_env_key)

        if not self._cookie_env_key:
            raise SystemError(f'Failed to get cookie name from .env: ({self._cookie_env_key})')

    def getCookieName(self):
        return self._cookie_name

    def getCookie(self):
        return request.cookies.get(self._cookie_name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return self