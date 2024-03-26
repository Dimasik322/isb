import json
import logging

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """Reads json file into dict.
    :param path:
    :return dict:
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            paths = json.load(file)
        return paths
    except Exception as exc:
        logging.error(f'Cannot find the path: {exc}\n')

def txt_reader(path: str) -> str:
    """Reads txt file into str.
    :param path:
    :return str:
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read().replace(' ', '').replace('\n', '')
        return text
    except Exception as exc:
        logging.error(f'Cannot find the path: {exc}\n')