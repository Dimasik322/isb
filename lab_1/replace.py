#replacing one char
def replace_char(file_name : str, change : list) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(f'lab_1/text_{change[0]}->{change[1]}.txt', 'w', encoding='utf-8') as new_file:
            for i in file.read():
                if i == change[0]:
                    new_file.write(change[1])
                else:
                    new_file.write(i)

#replacing by dictionary
def replace_dict(file_name : str, dict : dict) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(f'lab_1/task2_decrypted.txt', 'w', encoding='utf-8') as new_file:
            for i in file.read():
                if (i in dict):
                    new_file.write(dict[i])
                else:
                    new_file.write(i)