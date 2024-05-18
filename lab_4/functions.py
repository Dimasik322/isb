import json
import logging

from matplotlib import pyplot as plt


logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """Reads json file into dict.
    :param path: path to json file.
    :return: dict which contains keys and values from file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            paths = json.load(file)
        return paths
    except Exception as exc:
        logging.error(f"Reading json file error: {exc}\n")


def write_txt(path: str, data: str) -> None:
    """Writes string into txt file.
    :param path: path to txt file.
    :param data: string object that is needed to write.
    :return: None.
    """
    try:
        with open(path, "w") as file:
            data = file.write(data)
    except Exception as exc:
        logging.error(f"Writing string data to file error: {exc}\n")


def draw_dependence(data: tuple, path: str) -> None:
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
