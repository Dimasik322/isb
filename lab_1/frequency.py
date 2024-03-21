#frequency analysis
def char_frequency(file_name : str) -> None:
    file = open(file_name, 'r', encoding='utf-8')
    str = file.read()
    frequency = {}
    count = 0

    for i in str:
        count += 1
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    frequency = sorted(frequency.items(), key=lambda item : item[1], reverse=True)

    for item in frequency:
        print(f"{item[0]} : {item[1]/count}")
    print(count)