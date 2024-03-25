import logging

from caesar import caesar_encrypt
from route import route_transposition

logging.basicConfig(level=logging.INFO)


def write_caesar(path : str, key : int, path_encrypt: str, path_key: str) -> None:
    try:
        with open(path_encrypt, 'w', encoding='utf-8') as encrypt_file:
            encrypt_file.write(caesar_encrypt(path, key))
        with open(path_key, 'w', encoding='utf-8') as key_file:
            key_file.write(f'KEY: {key}')
        logging.info(f"Successfully encrypted and saved")
    except Exception as exc:
        logging.error(f'Saving error: {exc}\n')

def write_route(path : str, keyword : str, path_encrypt: str, path_key: str) -> None:
    try:
        with open(path_encrypt, 'w', encoding='utf-8') as encrypt_file:
            encrypt_file.write(route_transposition(path, keyword))
        with open(path_key, 'w', encoding='utf-8') as key_file:
            key_file.write(f'KEY: {keyword}')
        logging.info(f"Successfully encrypted and saved")
    except Exception as exc:
        logging.error(f'Saving error: {exc}\n')