import json
import logging


logging.basicConfig(level=logging.INFO)


class ReadWrite:
    """Class that contains additional functions
    for reading and writing files.
    """

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
 