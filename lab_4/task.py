import hashlib
import logging
import time
import multiprocessing as mp

from functions import draw_dependence


logging.basicConfig(level=logging.INFO)


class HashOperating:
    """ 
    """

    def card_id_operate(
        hash: str, last_digits: str, bin: tuple, middle_digits: int
    ) -> str:
        try:
            for first_digits in bin:
                card_id = f"{first_digits}{middle_digits:06d}{last_digits}"
                if hashlib.sha512(card_id.encode()).hexdigest() == hash:
                    return card_id
        except Exception as exc:
            logging.error(f"Hash comparison error: {exc}\n")

    def get_id_by_hash(hash: str, last_digits: str, bin: tuple) -> str:
        """Calculates card id number by hash, last_digits and bin-number."""
        try:
            with mp.Pool(processes=mp.cpu_count()) as p:
                for result in p.starmap(
                    HashOperating.card_id_operate,
                    (
                        (hash, last_digits, bin, middle_digits)
                        for middle_digits in range(0, 1000000)
                    ),
                ):
                    if result:
                        p.terminate()
                        break
            return result
        except Exception as exc:
            logging.error(f"Calculating card id error: {exc}\n")

    def luhn_alg(card_id: str) -> bool:
        try:
            sum = 0
            for digit in card_id[:-1:2]:
                print((int(digit) * 2 % 10) + (int(digit) * 2 // 10))
                sum += (int(digit) * 2 % 10) + (int(digit) * 2 // 10)
            for digit in card_id[1:-1:2]:
                print(digit)
                sum += int(digit)
            return (10 - sum % 10) == int(card_id[-1])
        except Exception as exc:
            logging.error(f"Luhn algorithm card id check error: {exc}\n")

    def collision_time(hash: str, last_digits: str, bin: tuple, path: str) -> None:
        try:
            collision_time_by_cores = [[], []]
            for cores in range(1, int(mp.cpu_count() * 1.5) + 1):
                start = time.time()
                with mp.Pool(processes=cores) as p:
                    for result in p.starmap(
                        HashOperating.card_id_operate,
                        (
                            (hash, last_digits, bin, middle_digits)
                            for middle_digits in range(0, 1000000)
                        ),
                    ):
                        if result:
                            p.terminate()
                            break
                delta = time.time() - start
                collision_time_by_cores[0].append(cores)
                collision_time_by_cores[1].append(delta)
            draw_dependence(collision_time_by_cores, path)
        except Exception as exc:
            logging.error(f"Collision time comparison error: {exc}\n")
