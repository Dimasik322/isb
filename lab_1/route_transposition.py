#encrtypting by route transposition method
def route_transposition(file_name : str, key : str):
    srt_key = sorted(key)
    route = [key.index(char) for char in sorted(key)]
    for i in range(len(route) - 1):
        if route[i] == route[i+1]:
            route[i + 1] = key.index(key[route[i]], route[i] + 1)
    #print(route)
    width = max(route) + 1
    with open(file_name, 'r', encoding='utf-8') as file:
        with open(f'lab_1/task1_encrypted.txt', 'w', encoding='utf-8') as new_file:
            text = file.read().replace(' ', '').replace('\n', '')
            height = int((len(text)) / (width + 1)) + 1
            matrix = [[text[((width * j) + i) % len(text)] for i in range(width)] for j in range(height)]
            #print(matrix)
            for i in route:
                for j in range(height):
                    new_file.write(matrix[j][i])
        new_file.close()
    file.close()
