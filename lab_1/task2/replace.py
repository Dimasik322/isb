def replace_char(file_name : str, change : list) -> None:
    """Function that makes a replacement in a given text file 
    and writes converted text into new file.
    params:
        file_name: original file path
        change: list object that contains a pair of chars that need to replace
    return:
        None
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(f'lab_1/text_{change[0]}->{change[1]}.txt', 'w', encoding='utf-8') as new_file:
            for i in file.read():
                if i == change[0]:
                    new_file.write(change[1])
                else:
                    new_file.write(i)

def replace_dict(file_name : str, char_dict : dict) -> None:
    """Function that makes a replacement in a given text file 
    and writes converted text into new file.
    params:
        file_name: original file path
        dict: dictionary that contains pair of chars that need to replace
    return:
        None
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(f'lab_1/task2_decrypted.txt', 'w', encoding='utf-8') as new_file:
            for i in file.read():
                if (i in char_dict):
                    new_file.write(char_dict[i])
                else:
                    new_file.write(i)