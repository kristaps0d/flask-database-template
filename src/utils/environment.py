import os, dotenv

class Environment(object):
    def __init__(self):
        dotenv.load_dotenv()

    def getenv(self, key):
        return os.getenv(key)

    def __enter__(self, key):
        dotenv.load_dotenv()
        return os.getenv(key)

    def __exit__(self, type, value, traceback):
        return

class EnvironmentWrapper(object):
    def __init__(self, key):
        dotenv.load_dotenv()
        self._key = key

    def __enter__(self):
        return os.getenv(self._key)

    def __exit__(self, type, value, traceback):
        return