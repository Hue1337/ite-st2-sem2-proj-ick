import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Key:
    def __init__(self, path):
        self.key = b''
        self.key_path = path
        self.load_key()

    def __str__(self):
        return str(self.key)

    def load_key(self):
        with open(self.key_path, "rb") as f:
            self.key = f.read()
            f.close()

    @staticmethod
    def gen_key(bytes = 32):
        return os.urandom(bytes)

    """Getters and Setters"""

    def get_key(self):
        return self.key

    def get_path(self):
        return self.key_path

    def set_key(self, bytestream):
        self.key = bytestream

    def set_path(self, path):
        self.key_path = path
