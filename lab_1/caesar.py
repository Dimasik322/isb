#encrtypting by caesar method
def caesar_encrypt(file_name : str, shift : int) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(f'lab_1/task1_encrypted.txt', 'w', encoding='utf-8') as new_file:
            for char in file.read():
                if ord('а') <= ord(char.lower()) <= ord('я'):
                    new_file.write(chr((ord(char.lower()) + shift - ord('а')) % 32 + ord('а')))
                else:
                    new_file.write(char)
            new_file.close()
        file.close()
