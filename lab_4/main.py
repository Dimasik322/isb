
from functions import json_reader, write_txt
from task import HashOperating
from constants import PATHS, DATA

if __name__ == "__main__":
    data = json_reader(DATA)
    paths = json_reader(PATHS)
    write_txt(paths["card_id_path"], HashOperating.get_id_by_hash(data["hash"], data["last_digits"], data["bin"]))
 
