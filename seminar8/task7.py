import csv
import pickle
from pathlib import Path

def csv_to_pickles(path: Path):
    with open(path, 'r', encoding='UTF-8', newline='') as f_read:
        data = csv.reader(f_read, dialect='excel')
        result = []
        for i, row in enumerate(data):
            if i != 0:
                result.append(dict(zip(headers, row)))
            else:
                headers = row

    print(pickle.dumps(result))


if __name__ == '__main__':
    csv_to_pickles(Path('new_users.csv'))