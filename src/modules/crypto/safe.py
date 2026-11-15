import os

class Safe:
    def __init__(self, path):
        self.path = path
        self.files = []

    def __str__(self):
        return "\n".join(self.files)

    def list_files(self, p):
        for file in os.listdir(p):
            if os.path.isdir(p + "/" + file):
                self.list_files(p + "/" + file)
            else:
                self.files.append(file)

    def decrypt_safe(self):
        """ Encrypting the entire safe """
        pass

    def encrypt_safe(self):
        """ Decrypting the entire safe """
        pass
