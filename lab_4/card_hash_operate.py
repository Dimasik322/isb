import hashlib
import logging
import time
import multiprocessing as mp

from matplotlib import pyplot as plt


logging.basicConfig(level=logging.INFO)


class HashOperating:
    """Class that contains functions for calculating card id,
    luhn algorithm card id checking and hash function
    collision time dependence graph drawing."""

    def card_id_operate(
        hash: str, last_digits: str, bin: tuple, middle_digits: int
    ) -> str:
        """Calculates card id by known hash, last digits and bank bin-numbers.
        :param hash: hash string value of searched id.
        :param last_digits: string with last digits of id.
        :param bin: tuple of bin-numbers.
        :param middle_digits: string of middle digits of id.
        :return: string of calculated card id.
        """
        try:
            for first_digits in bin:
                card_id = f"{first_digits}{middle_digits:06d}{last_digits}"
                if hashlib.sha512(card_id.encode()).hexdigest() == hash:
                    return card_id
        except Exception as exc:
            logging.error(f"Hash comparison error: {exc}\n")

    def get_id_by_hash(hash: str, last_digits: str, bin: tuple) -> str:
        """Calculates card id number by hash, last_digits and
        bin-number by multiprocess alorithm.
        :param hash: hash string value of searched id.
        :param last_digits: string with last digits of id.
        :param bin: tuple of bin-numbers.
        :return: string of calculated card id.
        """
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
        """Checks card id validity by luhn algorithm.
        :param card_id: string of checkable card id.
        :return: bool value of card id validity.
        """
        try:
            sum = 0
            for digit in card_id[:-1:2]:
                sum += (int(digit) * 2 % 10) + (int(digit) * 2 // 10)
            for digit in card_id[1:-1:2]:
                sum += int(digit)
            return (10 - sum % 10) == int(card_id[-1])
        except Exception as exc:
            logging.error(f"Luhn algorithm card id check error: {exc}\n")

    def collision_time(hash: str, last_digits: str, bin: tuple, path: str) -> None:
        """Measures hash function collision time for different
        cores number and draws picture of dependence.
        :param hash: hash string value of searched id
        :param last_digits: string with last digits of id.
        :param bin: tuple of bin numbers.
        :param path: path to picture to save it.
        :return: None.
        """
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
            HashOperating.draw_dependence(collision_time_by_cores, path)
        except Exception as exc:
            logging.error(f"Collision time comparison error: {exc}\n")

    def draw_dependence(data: tuple, path: str) -> None:
        """Draws picture of dependence of data in tuple.
        :param data: tuple that contains x and y axis.
        :param path: path to picture to save it.
        :return: None.
        """
        try:
            fig = plt.figure(figsize=(15, 5))
            plt.ylabel("Time, s")
            plt.xlabel("Cores number")
            plt.title("Hash collision time dependence by cores number")
            plt.plot(
                data[0],
                data[1],
                color="navy",
                linestyle="--",
                marker="o",
                linewidth=2,
                markersize=5,
            )
            min_point_index = data[1].index(min(data[1]))
            min_x = data[0][min_point_index]
            min_y = data[1][min_point_index]
            plt.plot(
                min_x,
                min_y,
                color="red",
                marker="*",
                markersize=9,
                label="Minimum time value",
            )
            plt.plot(
                [min_x, min_x], [0, min_y], color="red", linestyle="dotted", linewidth=2
            )
            plt.plot(
                [0, min_x], [min_y, min_y], color="red", linestyle="dotted", linewidth=2
            )
            plt.legend()
            plt.savefig(path)
        except Exception as exc:
            logging.error(f"Plot drawing error: {exc}\n")
 