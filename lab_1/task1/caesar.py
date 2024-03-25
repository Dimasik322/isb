import logging

logging.basicConfig(level=logging.INFO)


def caesar_encrypt(path : str, shift : int) -> str:
    """Function encrypts original text file 
    using the Caesar method by specified shift.
    params:
        file_name: original file path
        shift: int number for the method
    return:
        str
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read().replace(' ', '')
        encrypted_text = ""
        for char in text:
            if ord('а') <= ord(char.lower()) <= ord('я'):
                encrypted_text += chr((ord(char.lower()) + shift - ord('а')) % 32 + ord('а'))
            else:
                encrypted_text += char
        return encrypted_text
    except Exception as exc:
        logging.error(f'Encrypting error: {exc}\n')

