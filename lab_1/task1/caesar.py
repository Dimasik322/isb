import logging

from reader import txt_reader

logging.basicConfig(level=logging.INFO)


def caesar_encrypt(path : str, shift : int) -> str:
    """Encrypts text from file using Caesar method.
    :param path:
    "param shift:
    :return str:
    """
    try:
        text = txt_reader(path)
        encrypted_text = ""
        for char in text:
            if ord('а') <= ord(char.lower()) <= ord('я'):
                encrypted_text += chr((ord(char.lower()) + shift - ord('а')) % 32 + ord('а'))
            else:
                encrypted_text += char
        return encrypted_text
    except Exception as exc:
        logging.error(f'Encrypting error: {exc}\n')

