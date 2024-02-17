__all__ = ['pickle_to_csv']


import csv
import pickle
from pathlib import Path

def pickle_to_csv(path: Path):
    with open(path, 'rb') as f_read:
        data = pickle.load(f_read)
    headers = list(data[0].keys())
    with open(path.stem + '.csv', 'w', encoding='UTF-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)

if __name__ == '__main__':
    pickle_to_csv(Path('new_users.pickle'))