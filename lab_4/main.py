from functions import json_reader, write_txt
from task import HashOperating
from constants import PATHS, DATA


if __name__ == "__main__":
    data = json_reader(DATA)
    paths = json_reader(PATHS)
    card_id = HashOperating.get_id_by_hash(
        data["hash"], data["last_digits"], data["bin"]
    )
    if HashOperating.luhn_alg(card_id):
        write_txt(paths["card_id_path"], card_id)
    HashOperating.collision_time(
        data["hash"], data["last_digits"], data["bin"], paths["picture_path"]
    )
