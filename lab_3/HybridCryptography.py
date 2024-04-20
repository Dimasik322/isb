import os
import logging

from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.algorithms import Camellia

logging.basicConfig(level=logging.INFO)
     

class HybridCryptography:

    def __init__(self, symmetric_key_path: str, public_key_path: str, private_key_path: str) -> None:
        self.symmetric_key_path = symmetric_key_path
        self.public_key_path = public_key_path
        self.private_key_path = private_key_path

    def generate_key(self, size: int) -> tuple:
        try:
            symmetric_key = os.urandom(size)
            private_key = rsa.generate_private_key( 
                public_exponent=65537,
                key_size=size
            )
            public_key = private_key.public_key()
            return (symmetric_key, private_key, public_key)
        except Exception as exc:
            logging.error(f'Keys generation error: {exc}\n')
    

