import os
import logging
import cryptography

import cryptography.hazmat
from cryptography.hazmat.primitives import serialization, padding, hashes
import cryptography.hazmat.primitives
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

logging.basicConfig(level=logging.INFO)


def write_bytes(path: str, data: bytes) -> None:
    with open(path, 'wb') as file:
        file.write(data)


def read_bytes(path: str) -> bytes:
    with open(path, 'rb') as file:
        data = file.read()
    return data


def write_txt(path: str, data: str) -> None:
    with open(path, 'w') as file:
        data = file.write(data)


def read_txt(path: str) -> str:
    with open(path, 'r', encoding="utf_8_sig") as file:
        data = file.read()
    return data


class SymmetricCryptography:

    def __init__(self, key_path: str) -> None:
        self.key_path = key_path


    def generate_key(self, size: int) -> bytes:
        key = os.urandom(size)
        return key
    

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        padder = cryptography.hazmat.primitives.padding.ANSIX923(64).padder()
        padded_text = padder.update(data)+padder.finalize()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return c_text


    def decrypt(self, data: bytes, key: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_data = decryptor.update(data) + decryptor.finalize()
        unpadder = cryptography.hazmat.primitives.padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_data)# + unpadder.finalize()
        return unpadded_dc_text


class AsymmetricCryptography:

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path


    def generate_key(self, size: int) -> tuple:
        private_key = rsa.generate_private_key( 
                public_exponent=65537,
                key_size=2048
            )
        public_key = private_key.public_key()
        return private_key, public_key


    def serialize_key(self, key: tuple) -> None:
        private_key, public_key = key
        with open(self.private_key_path, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))
        with open(self.public_key_path, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
        

    def deserialize_key(self) -> tuple:
        with open(self.public_key_path, 'rb') as pem_in:
            public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
        with open(self.private_key_path, 'rb') as pem_in:
            private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes,password=None,)
        return d_private_key, d_public_key


    def encrypt(self, data: bytes, key: bytes) -> bytes:
        c_data = key.encrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return c_data


    def decrypt(self, data: bytes) -> bytes:
        private_key, public_key = self.deserialize_key()
        c_data = private_key.decrypt(data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return c_data


class HybridCryptography:

    def __init__(self, symmetric_key_path: str, private_key_path: str, public_key_path: str) -> None:
        #self.symmetric_key_path = symmetric_key_path
        #self.public_key_path = public_key_path
        #self.private_key_path = private_key_path
        self.symmetric = SymmetricCryptography(symmetric_key_path)
        self.asymmetric = AsymmetricCryptography(private_key_path, public_key_path)

    
    def generate_keys(self, size: int) -> None:
        print(size)
        symmetric_key = self.symmetric.generate_key(size)
        asymmetric_key = self.asymmetric.generate_key(size)
        self.asymmetric.serialize_key(asymmetric_key)
        private_key, public_key = asymmetric_key
        write_bytes(self.symmetric.key_path, public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None)))


    def encrypt(self, text_path: str, encrypted_text_path: str) -> None:
        text = bytes(read_txt(text_path), 'UTF-8')
        symmetric_key = self.asymmetric.decrypt(read_bytes(self.symmetric.key_path))
        c_text = self.symmetric.encrypt(text, symmetric_key)
        write_bytes(encrypted_text_path, c_text)


    def decrypt(self, text_path: str, decrypted_text_path: str) -> None:
        c_data = read_bytes(text_path)
        symmetric_key = self.asymmetric.decrypt(read_bytes(self.symmetric.key_path))
        dc_data = self.symmetric.decrypt(c_data, symmetric_key)
        write_bytes(decrypted_text_path, dc_data)