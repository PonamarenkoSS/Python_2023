__all__ = ['csv_to_json']

import json
import csv 
from pathlib import Path

def csv_to_json(from_path: Path, to_path: Path):
    result = []
    with open(from_path, 'r', encoding='UTF-8', newline='') as file_csv:
        csv_read = csv.reader(file_csv, dialect='excel-tab')
        for i, row in enumerate(csv_read):
            if i != 0:
                level, id, name = row
                data = {
                    'level': int(level),
                    'id': f'i{int(id):010}',
                    'name': name.title(),
                    'hash': hash(f'{name.title()}{int(id):010}')
                }
                result.append(data)
    with open(to_path, 'w', encoding='UTF-8') as file_json:
        json.dump(result, file_json, indent=4, ensure_ascii=False)      

if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))

