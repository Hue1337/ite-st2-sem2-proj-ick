from modules.crypto.key import Key

class KeyManager:
    def __init__(self, dev_kek_path, dev_dek_path):
        self.dev_kek_path = dev_kek_path
        self.dev_dek_path = dev_dek_path

        self.kek = Key(self.dev_kek_path)
        self.dek = Key(self.dev_dek_path)

    def __str__(self):
        return f"KEK: {self.kek}\n\nDEK: {self.dek}"

    def load_kek(self):
        self.kek.load_key()

    def load_dek(self):
        self.dek.load_key()

    def decrypt():
        """ Decrypt a key """
        pass

    def encrypt():
        """ Encrypt a key """
        pass
