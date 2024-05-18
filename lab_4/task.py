import hashlib
import logging
import multiprocessing as mp
import numpy as np

from random import randint
from matplotlib import pyplot as plt


logging.basicConfig(level=logging.INFO)


class HashOperating:
    """
    """

    def card_id_operate(hash: str, last_digits: str, bin: tuple, middle_digits: int) -> str:
        for first_digits in bin:
            card_id = f"{first_digits}{middle_digits:06d}{last_digits}"
            if hashlib.sha512(card_id.encode()).hexdigest() == hash:
                return card_id

    def get_id_by_hash(hash: str, last_digits: str, bin: tuple) -> str:
        """Calculates card id number by hash, last_digits and bin-number.
        [BBBBBB][MMMMMM][LLLL]
        """
        with mp.Pool(processes=mp.cpu_count()) as p:
            for result in p.starmap(HashOperating.card_id_operate, ((hash, last_digits, bin, middle_digits) for middle_digits in range(0, 1000000))):
                if result:
                    p.terminate()
                    break
        return result
            
    def luhn_alg(card_id: str) -> bool:
        sum = 0
        for digit in card_id[:-1:2]:
            print((int(digit) * 2 % 10) + (int(digit) * 2 // 10))
            sum += (int(digit) * 2 % 10) + (int(digit) * 2 // 10)
        for digit in card_id[1:-1:2]:
            print(digit)
            sum += int(digit)
        return (10 - sum % 10) == int(card_id[-1])
    
    #def collision_time():

 