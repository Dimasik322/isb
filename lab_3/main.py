import json

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
    crypto_system = HybridCryptography(paths["sym_path"], paths["public_path"], paths["private_path"])
    crypto_system.generate_keys(128)