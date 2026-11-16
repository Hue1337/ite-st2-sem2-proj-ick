from modules.crypto import operations
from modules.crypto.key import Key

class KeyManager:
    def __init__(self, dev_kek_path, dev_dek_path):
        self.dev_kek_path = dev_kek_path
        self.dev_dek_path = dev_dek_path

        self.kek = Key(self.dev_kek_path)
        self.dek = Key(self.dev_dek_path)

        self.dek.set_path(dev_dek_path)

        # Initialize kek and dek
        # self.dek.set_key(self.decrypt(self.dek.get_path(), self.dek.get_key()))
        self.load_dek()


    def __str__(self):
        return f"KEK: {self.kek}\n\nDEK: {self.dek}"

    def load_kek(self):
        self.kek.load_key()

    def load_dek(self):
        self.dek.load_key()

    def decrypt(self, path, key):
        """ Decrypt a key """
        with open(path, "rb") as f:
            ciphertext = f.read()
            bytestream = operations.decrypt(ciphertext, key)
            f.close()

        return bytestream

    def encrypt(self):
        """ Encrypt a key """
        pass

    """Getters and Setters"""
    def get_dek(self):
        return self.dek.get_key()

    def get_kek(self):
        return self.kek.get_key()
