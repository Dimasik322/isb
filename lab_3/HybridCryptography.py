import os
import logging

from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.algorithms import Camellia
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

logging.basicConfig(level=logging.INFO)
     

class SymmetricCryptography:

    def __init__(self, key_path: str) -> None:
        self.key_path = key_path


    def generate_key(self, size: int) -> bytes:
        key = os.urandom(size)
        return key
    

    def serialize_key(self, key: bytes) -> None:
        with open(self.key_path, 'wb') as key_file:
            key_file.write(key)


    def deserialize_key(self) -> bytes:
        with open(self.key_path, mode='rb') as key_file: 
            content = key_file.read()


class AsymmetricCryptography:

    def __init__(self, public_key_path: str, private_key_path: str) -> None:
        self.public_key_path = public_key_path
        self.private_key_path = private_key_path


    def generate_key(self, size: int) -> tuple:
        private_key = rsa.generate_private_key( 
                public_exponent=65537,
                key_size=size
            )
        public_key = private_key.public_key()
        return (private_key, public_key)


    def serialize_key(self, key: tuple) -> None:
        private_key = key[0]
        public_key = key[1]
        with open(self.public_key_path, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))
        with open(self.private_key_path, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
        

    def deserialize_key(self) -> tuple:
        with open(self.public_key_path, 'rb') as pem_in:
            public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
        with open(self.private_key_path, 'rb') as pem_in:
            private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes,password=None,)


class HybridCryptography:

    def __init__(self, symmetric_key_path: str, public_key_path: str, private_key_path: str) -> None:
        self.symmetric_key_path = symmetric_key_path
        self.public_key_path = public_key_path
        self.private_key_path = private_key_path
        self.symmetric = SymmetricCryptography
        self.asmmetric = AsymmetricCryptography
