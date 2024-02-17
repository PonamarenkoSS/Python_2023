__all__ = ['dir_walker']

import json
import csv 
from pathlib import Path

def json_to_csv(path: Path):
    with open(path, 'r', encoding='UTF-8') as file_read:
        data = json.load(file_read)
    
    result = []
    for level, id_name in data.items():
        for id, name in id_name.items():
            result.append({'level': int(level), 'id': int(id), 'name': name})
    with open(path.stem + '.csv', 'w', encoding='UTF-8', newline='') as file_write:
        csv_write = csv.DictWriter(file_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(result)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))
