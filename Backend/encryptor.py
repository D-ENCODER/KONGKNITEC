# Date    : 24/09/22 11:47 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import hashlib
import os


def encrypt(plain_text):
    """
    Encrypts the plain text using SHA256 algorithm
    arguments include plain text and returns list containing key and plain text
    """
    # Generate a random key
    key = os.urandom(32)
    # Encrypt the plain text using SHA256 algorithm
    encrypted_text = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        plain_text.encode('utf-8'),  # Convert the password to bytes
        key,  # Provide the key
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
        dklen=128  # Get a 128 byte key
    )
    # Return the encrypted text and key
    return encrypted_text, key
