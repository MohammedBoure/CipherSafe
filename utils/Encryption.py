from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import base64

iv = b'\x10\x0c1\t\x9f\xb1\x10\x94D4\xcf\x99\x8en&\xbf'

def encrypt(plaintext, key, iv=iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode()  # تحويل إلى base64

def decrypt(ciphertext, key, iv=iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

def simple_hash_256(input_string):
    if not input_string:
        raise ValueError("Input string for hashing cannot be empty!")
    return hashlib.sha256(input_string.encode()).digest()[:32]


if __name__ == "__main__":
    key = simple_hash_256("password") 
    plaintext = ""
    
    encrypted = encrypt(plaintext, key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted:", decrypted)
