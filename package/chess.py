'''
Задание 2.
Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
'''

__all__ = ['check_queens_var_1', 'COUNT_OF_QUEENS', 'queens_location_2', 'check_queens_var_2', 'check_queens_var_3', 'check_success']

import random

def check_queens_var_1():
    COUNT_OF_QUEENS = 8
    queens_location = []
    for i in range(1, COUNT_OF_QUEENS+1):
        queens_location.append(tuple(map(int, input(f'Введите координаты расположения {i} ферзя (два целых числа через пробел): ').split())))
    for i in range(len(queens_location)-1):
        for j in range(i+1, len(queens_location)):
            if queens_location[i] == queens_location[j]:
                print(f'Координаты ферзей {i+1} и {j+1} совпадают, попробуйте ввести заново')
                return False
            elif queens_location[i][0] == queens_location[j][0] or queens_location[i][1] == queens_location[j][1] or (queens_location[i][0] == queens_location[i][1] and queens_location[j][0] == queens_location[j][1]) or (queens_location[i][0] - queens_location[j][0] == queens_location[i][1] - queens_location[j][1]):
                print(f'Ферзи {i+1} и {j+1} бьют друг друга')
                return False
    return True

COUNT_OF_QUEENS = 8
queens_location_2 = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(COUNT_OF_QUEENS)]

def check_queens_var_2(queens_location_2):
    for i in range(len(queens_location_2)-1):
        for j in range(i+1, len(queens_location_2)):
            if queens_location_2[i] == queens_location_2[j]:
                print(f'Координаты ферзей {i+1} и {j+1} совпадают, попробуйте заново')
                return False
            elif queens_location_2[i][0] == queens_location_2[j][0] or queens_location_2[i][1] == queens_location_2[j][1] or (queens_location_2[i][0] == queens_location_2[i][1] and queens_location_2[j][0] == queens_location_2[j][1]) or (queens_location_2[i][0] - queens_location_2[j][0] == queens_location_2[i][1] - queens_location_2[j][1]):
                print(f'Ферзи {i+1} и {j+1} бьют друг друга')
                return False
    return True

'''
Задание 3.
Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
'''


def check_queens_var_3():
    COUNT_OF_QUEENS = 8
    queens_location_3 = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(COUNT_OF_QUEENS)]
    for i in range(len(queens_location_3)-1):
        for j in range(i+1, len(queens_location_3)):
            if queens_location_3[i] == queens_location_3[j]:
                print(f'Координаты ферзей {i+1} и {j+1} совпадают, попробуйте заново')
                return False
    print(f'Успешная расстановка {queens_location_3}')
    return True

def check_success():
    count_of_success = 0
    count_of_try = 0
    while not count_of_success:
        count_of_try += 1
        res = check_queens_var_3()
        if res:
            count_of_success += 1
    print(f'Успешная попытка номер {count_of_try}')
    return True


if __name__ == '__main__':
    print(check_queens_var_1())
    print(check_queens_var_2(queens_location_2))
    print(queens_location_2)
    check_success()