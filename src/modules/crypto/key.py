import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Key:
    key: bytes = b''
    def __init__(self, path):
        self.key_path = path

    def __str__(self):
        return str(self.key)

    def load_key(self):
        with open(self.key_path, "rb") as f:
            self.key = f.read()
            f.close()


    @staticmethod
    def gen_key(bytes: int = 256):
        return os.urandom(bytes)
