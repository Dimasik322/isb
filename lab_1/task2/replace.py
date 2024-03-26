import logging

from reader import txt_reader

logging.basicConfig(level=logging.INFO)


def replace_dict(path : str, key : dict) -> None:
    try:
        text = txt_reader(path)
        decrypted_text = ""
        for char in text:
            if (char in key):
                decrypted_text += key[char]
            else:
                decrypted_text += char
        return decrypted_text
    except Exception as exc:
        logging.error(f'Decrypting error: {exc}\n')