"""
Script that Implements AES encryption and decryption using Python's cryptography library
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import base64
import os

# Message and byte conversion
message = input("What would u like to say? ")


#Generate key
key = os.urandom(16)
print(f"AES Key: {key}")


# Function for encryption 
def encrypted_message(message, key):
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), 
    backend = default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode()

def decrypted_message(encrypted_text, key) -> str:
    encrypted_data = base64.b64decode(encrypted_text)
    iv, ciphertext = encrypted_data[:16], encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),
    backend = default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_message = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted_message.decode()


encrypted_text = encrypted_message(message, key)
print(f"encrypted message: {encrypted_text}")
decrypted_text = decrypted_message(encrypted_text, key)
print(f"Decrypted Message: {decrypted_text}")


"""
padder = padding.PKCS7(128).padder()
padded_message = padder.update(message.encode()) + padder.finalize()

print(f"Padded Message: {padded_message}")

# Random Vector

iv = os.urandom(16)

# CBC Block

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), 
backend = default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

print(f"Encrypted Message: {b64encode(ciphertext).decode()}")



encrypted_text = encrypted_message(message, key)
print(f"encrypted message: {encrypted_text}")
decrypted_text = decrypted_message(encrypted_text, key)
print(f"Decrypted Message: {decrypted_text}")


# Decryption and Unpadding
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
decrypted_message = unpadder.update(decrypted_padded) + unpadder.finalize()

print(f"Decrypted Message: {decrypted_message.decode()}")
"""