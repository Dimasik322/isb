import os
import logging
import cryptography.hazmat.primitives

from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)

from functions import write_bytes, read_bytes, read_txt


logging.basicConfig(level=logging.INFO)


class SymmetricCryptography:
    """
    Class that contains methods for generating key,
    encryption and decryption by symmetrical method.
    Methods:
    generate_key(self, size: int) -> bytes,
    encrypt(self, data: bytes, key: bytes) -> bytes,
    decrypt(self, data: bytes, key: bytes) -> bytes.
    """

    def __init__(self, key_path: str) -> None:
        """Initialises SymmetricCryptography class object.
        :param key_path: path for saving key.
        :return: None.
        """
        self.key_path = key_path

    def generate_key(self, size: int) -> bytes:
        """Generates key for symmetrical method.
        :param size: size of key in bits.
        :return: key as bytes object.
        """
        try:
            key = os.urandom(size)
            return key
        except Exception as exc:
            logging.error(f"Generating symmetrical key error: {exc}\n")

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """Does symmetrical encryption of data using key.
        :param data: bytes object that is needed to encrypt.
        :param key: bytes object key for encryption.
        :return: bytes of encrypted data.
        """
        try:
            padder = cryptography.hazmat.primitives.padding.ANSIX923(
                algorithms.Camellia.block_size
            ).padder()
            padded_text = padder.update(data) + padder.finalize()

            iv = os.urandom(16)
            cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            c_text = encryptor.update(padded_text) + encryptor.finalize()
            return c_text
        except Exception as exc:
            logging.error(f"Symmetrical encryption error: {exc}\n")

    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """Does symmetrical decryption of encrypted data using key.
        :param data: bytes object that is needed to decrypt.
        :param key: bytes object key for decryption.
        :return: bytes of decrypted data.
        """
        try:
            iv = os.urandom(16)
            cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            dc_data = decryptor.update(data) + decryptor.finalize()

            unpadder = cryptography.hazmat.primitives.padding.ANSIX923(
                algorithms.Camellia.block_size
            ).unpadder()
            unpadded_dc_data = unpadder.update(dc_data) + unpadder.finalize()

            return unpadded_dc_data
        except Exception as exc:
            logging.error(f"Symmetrical decryption error: {exc}\n")


class AsymmetricCryptography:
    """
    Class that contains methods for generating key,
    encryption and decryption by asymmetrical method.
    Methods:
    generate_key(self, size: int) -> tuple,
    serialize_key(self, key: tuple) -> None,
    deserialize_key(self) -> tuple,
    encrypt(self, data: bytes, key: bytes) -> bytes,
    decrypt(self, data: bytes, key: bytes) -> bytes.
    """

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """Initializes AsymmetricCryptography class object.
        :param private_key_path: path for saving private key.
        :param public_key_path: path for saving public key.
        :return: None.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    def generate_key(self, size: int) -> tuple:
        """Generates key for asymmetrical method.
        :param size: size of keys in bits.
        :return: tuple of private and public keys.
        """
        try:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            public_key = private_key.public_key()
            return private_key, public_key
        except Exception as exc:
            logging.error(f"Generating asymmetrical keys error: {exc}\n")

    def serialize_key(self, key: tuple) -> None:
        """Serializes keys for asymmetrical method.
        :param key: tuple of private and public keys.
        :return: None.
        """
        try:
            private_key, public_key = key
            with open(self.private_key_path, "wb") as private_out:
                private_out.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
            with open(self.public_key_path, "wb") as public_out:
                public_out.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except Exception as exc:
            logging.error(f"Asymmetrical keys serialization error: {exc}\n")

    def deserialize_key(self) -> tuple:
        """Deserializes keys for asymmetrical method.
        :return: tuple of private and public keys.
        """
        try:
            with open(self.public_key_path, "rb") as pem_in:
                public_bytes = pem_in.read()
                d_public_key = load_pem_public_key(public_bytes)
            with open(self.private_key_path, "rb") as pem_in:
                private_bytes = pem_in.read()
                d_private_key = load_pem_private_key(
                    private_bytes,
                    password=None,
                )
            return d_private_key, d_public_key
        except Exception as exc:
            logging.error(f"Asymmetrical keys deserialization error: {exc}\n")

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """Does asymmetrical encryption of data using key.
        :param data: bytes object that is needed to encrypt.
        :param key: bytes object key for encryption.
        :return: bytes of encrypted data.
        """
        try:
            c_data = key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return c_data
        except Exception as exc:
            logging.error(f"Asymmetrical encryption error: {exc}\n")

    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """Does asymmetrical decryption of encrypted data using key.
        :param data: bytes object that is needed to decrypt.
        :param key: bytes object key for decryption.
        :return: bytes of decrypted data.
        """
        try:
            c_data = key.decrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return c_data
        except Exception as exc:
            logging.error(f"Asymmetrical decryption error: {exc}\n")


class HybridCryptography:
    """Class that contains methods for generating key,
    encryption and decryption by hybrid method(symmetrical and asymmetrical).
    Methods:
    generate_key(self, size: int) -> bytes,
    encrypt(self, text_path: str, encrypted_text_path: str) -> None,
    decrypt(self, text_path: str, decrypted_text_path: str) -> None.
    """

    def __init__(
        self, symmetric_key_path: str, private_key_path: str, public_key_path: str
    ) -> None:
        """Initializes HybridCryprography class object.
        :param symmetric_key_path: path for saving symmetrical key.
        :param private_key_path: path for saving private key.
        :param public_key_path: path for saving public key.
        :return: None.
        """
        self.symmetric = SymmetricCryptography(symmetric_key_path)
        self.asymmetric = AsymmetricCryptography(private_key_path, public_key_path)

    def generate_keys(self, size: int) -> None:
        """Generates key for hybrid method.
        :param size: size of keys in bits.
        :return: tuple of private and public keys.
        """
        try:
            if size != 16 and size != 24 and size != 32:
                raise ValueError("Size of keys must be 128, 192 or 256")
            symmetric_key = self.symmetric.generate_key(size)
            asymmetric_key = self.asymmetric.generate_key(size)
            self.asymmetric.serialize_key(asymmetric_key)
            private_key, public_key = asymmetric_key
            write_bytes(
                self.symmetric.key_path,
                public_key.encrypt(
                    symmetric_key,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None,
                    ),
                ),
            )
        except Exception as exc:
            logging.error(f"Genereting keys for HybridCryptography error: {exc}\n")

    def encrypt(self, text_path: str, encrypted_text_path: str) -> None:
        """Does hybrid encryption of data.
        :param text_path: path to file with data that is needed to encrypt.
        :param encrypted_text_path: path to file for saving encrypted data.
        :return: None.
        """
        try:
            text = bytes(read_txt(text_path), "UTF-8")
            key = self.asymmetric.deserialize_key()[0]
            symmetric_key = self.asymmetric.decrypt(
                read_bytes(self.symmetric.key_path), key
            )
            c_text = self.symmetric.encrypt(text, symmetric_key)
            write_bytes(encrypted_text_path, c_text)
        except Exception as exc:
            logging.error(f"Hybrid encryption error: {exc}\n")

    def decrypt(self, text_path: str, decrypted_text_path: str) -> None:
        """Does hybrid dencryption of data.
        :param text_path: path to file with data that is needed to decrypt.
        :param decrypted_text_path: path to file for saving decrypted data.
        :return: None.
        """
        try:
            c_data = read_bytes(text_path)
            key = self.asymmetric.deserialize_key()[0]
            symmetric_key = self.asymmetric.decrypt(
                read_bytes(self.symmetric.key_path), key
            )
            dc_data = self.symmetric.decrypt(c_data, symmetric_key)
            write_bytes(decrypted_text_path, dc_data)
        except Exception as exc:
            logging.error(f"Hybrid decryption error: {exc}\n")
