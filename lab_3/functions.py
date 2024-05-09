import json
import logging
import argparse

from constants import PATHS


logging.basicConfig(level=logging.INFO)


class Functions:
    """Class that contains additional functions
    for reading and writing files and parsing arguments.

    """

    def write_bytes(path: str, data: bytes) -> None:
        """Writes bytes into txt file.
        :param path: path to txt file.
        :param data: bytes object that is needed to write.
        :return: None.
        """
        try:
            with open(path, "wb") as file:
                file.write(data)
        except Exception as exc:
            logging.error(f"Writing binary data to file error: {exc}\n")

    def read_bytes(path: str) -> bytes:
        """Reads bytes from txt file.
        :param path: path to txt file.
        :return: bytes.
        """
        try:
            with open(path, "rb") as file:
                data = file.read()
            return data
        except Exception as exc:
            logging.error(f"Reading binary data from file error: {exc}\n")

    def write_txt(path: str, data: str) -> None:
        """Writes string into txt file.
        :param path: path to txt file.
        :param data: string object that is needed to write.
        :return: None.
        """
        try:
            with open(path, "w") as file:
                data = file.write(data)
        except Exception as exc:
            logging.error(f"Writing string data to file error: {exc}\n")

    def read_txt(path: str) -> str:
        """Reads srting from txt file.
        :param path: path to txt file.
        :return: string.
        """
        try:
            with open(path, "r", encoding="utf_8_sig") as file:
                data = file.read()
            return data
        except Exception as exc:
            logging.error(f"Reading string data from file error: {exc}\n")

    def json_reader(path: str) -> dict:
        """Reads json file into dict.
        :param path: path to json file.
        :return: dict which contains keys and values from file.
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                paths = json.load(file)
            return paths
        except Exception as exc:
            logging.error(f"Reading json file error: {exc}\n")

    def parse() -> argparse.Namespace:
        """Parses arguments.
        :return: Namespace object with parsed arguments.
        """
        try:
            paths = Functions.json_reader(PATHS)
            parser = argparse.ArgumentParser()
            group = parser.add_argument_group()
            group.add_argument(
                "-gen",
                "--generation",
                action="store_true",
                help="Sets key generation mode",
            )
            group.add_argument(
                "-enc",
                "--encryption",
                action="store_true",
                help="Sets encryption mode",
            )
            group.add_argument(
                "-dec",
                "--decryption",
                action="store_true",
                help="Sets decryption mode",
            )
            group.add_argument(
                "-len", type=int, default=256, help="Sets key len(128|192|256)"
            )
            group.add_argument(
                "-key", action="store_true", help="Sets custom paths to keys mode"
            )
            group.add_argument(
                "-sym_pth",
                type=str,
                default=paths["sym_path"],
                help="Sets path to symmetric key",
            )
            group.add_argument(
                "-private_pth",
                type=str,
                default=paths["private_path"],
                help="Sets path to private key",
            )
            group.add_argument(
                "-public_pth",
                type=str,
                default=paths["public_path"],
                help="Sets path to public key",
            )
            group.add_argument(
                "-pth",
                type=str,
                default=paths["text"],
                help="Sets path to text to encypt",
            )
            group.add_argument(
                "-cpt",
                type=str,
                default=paths["encrypted_text"],
                help="Sets path to encrypted text",
            )
            args = parser.parse_args()
            return args
        except Exception as exc:
            logging.error(f"Parsing error: {exc}\n")
