import json
import logging

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """
    json file reader by path,
    returns dict.
    :param path: path to the file.
    :type path: string
    :return: dict.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            paths = json.load(file)
        return paths
    except Exception as exc:
        logging.error(f'Cannot find the path or read: {exc}\n')

def txt_reader(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as exc:
        logging.error(f'Cannot find the path or read: {exc}\n')