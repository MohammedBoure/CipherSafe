from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


iv = b'\x10\x0c1\t\x9f\xb1\x10\x94D4\xcf\x99\x8en&\xbf'

def encrypt(plaintext, key, iv = iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key, iv = iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()


if __name__ == "__main__":
    import os

    key = os.urandom(32)
    
    plaintext = "test"
    ciphertext = encrypt(plaintext, key, iv)
    print(ciphertext)

    decrypted_text = decrypt(ciphertext, key, iv)
    print(decrypted_text)