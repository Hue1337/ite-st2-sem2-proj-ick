import os

from modules.crypto.key import Key

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

PADDING = 128

def encrypt(bytestream, key, iv = b"1234567890123456"):
    cipher = Cipher(algorithms.AES256(key), mode=modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(PADDING).padder()
    padded = padder.update(bytestream) + padder.finalize()

    return encryptor.update(padded) + encryptor.finalize()

def decrypt(ciphertext,key, iv = b"1234567890123456"):
    cipher = Cipher(algorithms.AES256(key), mode=modes.CBC(iv))
    decryptor = cipher.decryptor()

    data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(PADDING).unpadder()
    return unpadder.update(data) + unpadder.finalize()
