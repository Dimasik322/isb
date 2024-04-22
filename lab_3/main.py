import json
import argparse

from HybridCryptography import HybridCryptography

PATHS = "paths.json"


def json_reader(path: str) -> dict:
    """Reads json file into dict.
    :param path: path to json file
    :return: dict which contains keys and values from file
    """
    with open(path, 'r', encoding='utf-8') as file:
        paths = json.load(file)
    return paths


if __name__ == '__main__':
    paths = json_reader(PATHS)
    crypto_system = HybridCryptography(paths["sym_path"], paths["private_path"], paths["public_path"])
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group()
    #group = parser.add_mutually_exclusive_group(required = False)
    group.add_argument('-gen', '--generation', action='store_true', help='Запускает режим генерации ключей по заданному ключу(128/192/256)')
    group.add_argument('-enc', '--encryption', action='store_true', help='Запускает режим шифрования файла по заданному пути')
    group.add_argument('-dec', '--decryption', action='store_true', help='Запускает режим дешифрования файла по заданному пути')
    group.add_argument('-len', type=int, default=256, help='Задает длину ключа для генерации')
    group.add_argument('-pth', type=str, default=paths["text"], help='Задает путь файля для шифрования')
    group.add_argument('-cpt', type=str, default=paths["encrypted_text"], help='Задает путь файля для дешифрования')
    args = parser.parse_args()
    print(args)
    if args.generation:
        crypto_system.generate_keys(int(args.len / 8))
    elif args.encryption:
        crypto_system.encrypt(args.pth, paths["encrypted_text"])
    else:
        crypto_system.decrypt(args.cpt, paths["decrypted_text"])
