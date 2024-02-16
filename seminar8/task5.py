import json
import pickle
from pathlib import Path

def json_to_pickle(path: Path):
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with(
                open(obj, 'r', encoding='UTF-8') as f_read,
                open(obj.stem + '.pickle', 'wb') as f_write
            ):
                data = json.load(f_read)
                pickle.dump(data, f_write)

if __name__ == '__main__':
    json_to_pickle(Path(r'/Users/svetlanaponamarenko/Desktop/Python/seminar/Python_2023'))