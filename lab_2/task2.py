import logging
import json
import math
import os

from mpmath import gammainc

ROW_SIZE = 128
PATHS = "paths.json"
PI = [0.2148, 0.3672, 0.2305, 0.1875]

logging.basicConfig(level=logging.INFO)

def json_reader(path: str) -> dict:
    """Reads json file into dict.
    :param path: path to json file
    :return: dict which contains keys and values from file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            paths = json.load(file)
        return paths
    except Exception as exc:
        logging.error(f'Cannot find the path or read: {exc}\n')

def txt_reader(path: str) -> str:
    """Reads txt file into str.
    :param path: path to txt file
    :return: str of text from file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as exc:
        logging.error(f'Cannot find the path or read: {exc}\n')

def bit_frequncy_test(row: str) -> float:
    try:
        s = (row.count("1") - row.count("0")) / pow(ROW_SIZE, 0.5)
        p = math.erfc(s / pow(2, 0.5))
        return p
    except Exception as exc:
        logging.error(f"bit frequncy test error: {exc}")

def bit_row_test(row: str) -> float:
    try:
        s = row.count("1") / ROW_SIZE
        if abs(s - 0.5) >= (2 / pow(ROW_SIZE, 0.5)):
            return 0
        else:
            v = 0
            for i in range(0, ROW_SIZE - 1):
                if row[i] != row[i+1]:
                    v += 1
        p = math.erfc(abs(v - 2 * ROW_SIZE * s * (1 - s)) / (2 * pow(2 * ROW_SIZE, 0.5) * s * (1 - s)))
        return p
    except Exception as exc:
        logging.error(f"bit row test error: {exc}")

def longest_bit_row_test(row: str) -> float:
    try:
        block_max_lenghts = {i: 0 for i in range(0, 8)}
        for step in range(0, ROW_SIZE, 8):
            block = row[step:step+8]
            lenght = 0
            max_lenght = 0
            for bit in block:
                if bit == "1":
                    lenght += 1
                else:
                    lenght = 0
                if max_lenght < lenght:
                    max_lenght = lenght
            block_max_lenghts[max_lenght] +=1
        v = {i: 0 for i in range(1, 5)}
        for i in block_max_lenghts:
            if i <= 1:
                v[1] += block_max_lenghts[i]
            if i == 2:
                v[2] += block_max_lenghts[i]
            if i == 3:
                v[3] += block_max_lenghts[i]
            if i >= 4:
                v[4] += block_max_lenghts[i]
        xi = 0
        for i in range(0, 4):
            xi += (pow((v[i+1] - 16 * PI[i]), 2) / (16 * PI[i]))
        p = gammainc(3/2, xi/2)
        return p    
    except Exception as exc:
        logging.error(f"longest bit row test error: {exc}")

if __name__ == "__main__":
    paths = json_reader(PATHS)

    print(longest_bit_row_test(txt_reader(paths["cpp_row"])))
