import logging

from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)


logging.basicConfig(level=logging.INFO)


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

    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """Serializes private key for asymmetrical method.
        :param private_key: private key object.
        :return: None.
        """
        try:
            with open(self.private_key_path, "wb") as private_out:
                private_out.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
        except Exception as exc:
            logging.error(f"Asymmetrical private key serialization error: {exc}\n")

    def serialize_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        """Serializes public key for asymmetrical method.
        :param public_key: public key object.
        :return: None.
        """
        try:
            with open(self.public_key_path, "wb") as public_out:
                public_out.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except Exception as exc:
            logging.error(f"Asymmetrical public key serialization error: {exc}\n")

    def deserialize_private_key(self) -> rsa.RSAPrivateKey:
        """Deserializes private key for asymmetrical method.
        :return: private key.
        """
        try:
            with open(self.private_key_path, "rb") as pem_in:
                private_bytes = pem_in.read()
                d_private_key = load_pem_private_key(
                    private_bytes,
                    password=None,
                )
            return d_private_key
        except Exception as exc:
            logging.error(f"Asymmetrical private key deserialization error: {exc}\n")

    def deserialize_public_key(self) -> rsa.RSAPublicKey:
        """Deserializes public key for asymmetrical method.
        :return: public key.
        """
        try:
            with open(self.public_key_path, "rb") as pem_in:
                public_bytes = pem_in.read()
                d_public_key = load_pem_public_key(public_bytes)
            return d_public_key
        except Exception as exc:
            logging.error(f"Asymmetrical public key deserialization error: {exc}\n")

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
