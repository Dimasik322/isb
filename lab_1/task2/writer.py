import logging

from replace import replace_dict
from frequency import char_frequency

logging.basicConfig(level=logging.INFO)


def write_decrypted(path : str, key : dict, path_encrypt: str, path_key: str) -> None:
    """Decrypts and writes str and key into files.
    :param path:
    :param key:
    :param path_decrypted:
    :param path_key:
    :return:
    """
    try:
        with open(path_encrypt, 'w', encoding='utf-8') as decrypted_file:
            decrypted_file.write(replace_dict(path, key))
        with open(path_key, 'w', encoding='utf-8') as key_file:
            key_file.write("Замены:")
            for char_before, char_after in key.items():
                key_file.write(f"'{char_before}' -> '{char_after}'\n")
        logging.info(f"Successfully dencrypted and saved")
    except Exception as exc:
        logging.error(f'Saving error: {exc}\n')

def write_frequency(path : str, path_frequency : str) -> None:
    """Does freaquency analysis and writes it into file.
    :param path:
    :param path_frequency:
    :return:
    """
    try:
        with open(path_frequency, 'w', encoding='utf-8') as key_file:
            key_file.write("Частотный анализ:\n")
            for char, count in char_frequency(path):
                key_file.write(f"'{char}' : '{count}'\n")
    except Exception as exc:
        logging.error(f'Frequency saving error: {exc}\n')