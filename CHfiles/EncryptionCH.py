from cryptography.fernet import Fernet

def generate_key(key=None):
    if not key:
        key = str(Fernet.generate_key())
    with open("secret.key", "w") as key_file:
        key_file.write(key)
    print("the key in secret.key")

def load_key():
    with open("secret.key", "r") as key_file:
        return key_file.read()

def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text






if __name__ == "__main__":
    try:
        key = load_key()
    except FileNotFoundError:
        generate_key()
        key = load_key()
    
    text = input()
    encrypted = encrypt_text(text, key)
    print(encrypted.decode())
    
    decrypted = decrypt_text(encrypted, key)
    print(decrypted)
