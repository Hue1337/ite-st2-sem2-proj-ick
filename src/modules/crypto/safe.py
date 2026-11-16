import os

from modules.crypto import operations
from modules.crypto.key_manager import KeyManager

class Safe:
    def __init__(self, path, kek_path, dek_path):
        self.path = path
        self.files = []

        self.key_manager = KeyManager(kek_path, dek_path)

    def __str__(self):
        return "\n".join(self.files)

    def list_files(self, p):
        for file in os.listdir(p):
            if os.path.isdir(p + "/" + file):
                self.list_files(p + "/" + file)
            else:
                self.files.append(p + "/" + file)

    def encrypt_safe(self):
        """ Encrypting the entire safe """
        for file in self.files:
            with open(file, "rb") as f:
                bytestream = f.read()
                print(len(self.key_manager.get_dek()))
                ciphertext = operations.encrypt(bytestream, self.key_manager.get_dek())
            print("Encrypted:\n", ciphertext)

            with open(file, "wb") as f:
                f.write(ciphertext)
                f.close()


    def decrypt_safe(self):
        """ Decrypting the entire safe """
        for file in self.files:
            with open(file, "rb") as f:
                ciphertext = f.read()
                bytestream = operations.decrypt(ciphertext, self.key_manager.get_dek())
                print("Decrypted:\n", bytestream)

            with open(file, "wb") as f:
                f.write(bytestream)
                f.close()
