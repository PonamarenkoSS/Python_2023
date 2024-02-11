'''Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. 
    При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. 
    Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. 
    Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

from pathlib import Path
import os

def rename_files(directory: str | Path, ext_now: str, ext_future: str, finish_name: str = None, count_of_numbers: int = 2, range_of_origin_name: list = None):
    if not finish_name and not finish_name:
        print('Не указан один из основных параметров для переименования файлов, попробуйте заново')
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        print('Указанной директории не существует, попробуйте заново')
    os.chdir(directory)
    dir_list = os.listdir(directory)
    print(dir_list)
    counter = 1
    for file_in_dir in dir_list:
        new_file_name = ''
        if file_in_dir.endswith(ext_now):
            if range_of_origin_name:
                start, end, *other = range_of_origin_name
                new_file_name = file_in_dir[start-1, end-1] + finish_name
                if count_of_numbers == 1:
                    new_file_name += str(counter) + '.' + ext_future
                    counter += 1
                else:
                    new_file_name += str(counter).zfill(count_of_numbers) + '.' + ext_future
                    counter += 1
            else:
                if count_of_numbers == 1:
                    new_file_name = finish_name + str(counter) + '.' + ext_future
                    counter += 1
                else:
                    new_file_name = finish_name + str(counter).zfill(count_of_numbers) + '.' + ext_future
                    counter += 1
            print(new_file_name)
            Path(file_in_dir).rename(new_file_name)

if __name__ == '__main__':
    rename_files(r"/Users/svetlanaponamarenko/Desktop/Python/seminar/Python_2023/Python_2023/test/spam", 'txt', 'jpeg', 'new_name')