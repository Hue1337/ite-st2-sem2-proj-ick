import os

from modules.crypto import operations

class Safe:
    def __init__(self, path, kek, dek):
        self.path = path
        self.files = []
        self.kek = kek
        self.dek = dek

        self.iv = b"1234567890123456" # 16 bytes the way of holding the value will change in future

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
                print(len(self.dek.get_key()))
            print("Encrypted:\n", operations.encrypt(self.dek.get_key(), self.iv, bytestream))


    def decrypt_safe(self):
        """ Decrypting the entire safe """
        for file in self.files:
            with open(file, "rb") as f:
                ciphertext = f.read()

                bytestream = operations.decrypt(self.dek.get_key(), self.iv, ciphertext)
                print("Decrypted:\n", bytestream)
