import time, hashlib

class NewSessionToken(object):
    def __new__(self, address):
        _raw = f'{address}:{time.time()}'
        return hashlib.sha3_512(_raw.encode()).hexdigest()