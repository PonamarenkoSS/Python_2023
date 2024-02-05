'''
Задание 1.
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os

p = os.path.abspath('seminar_5.py')
'/Users/svetlanaponamarenko/Desktop/Python/seminar/seminar_5.py'

def os_func():
    text = input('Введите абсолютный путь до файла: ')
    input_way = list(p.split('/'))
    way = ''
    for i in range(len(input_way)-1):
        way += input_way[i] + '/'
    name = input_way[len(input_way)-1].split('.')[0]
    extension = input_way[len(input_way)-1].split('.')[-1]
    return way, name, extension

print(os_func())

'''
Задание 2.
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
'''

name = ['Bob', 'Ivan', 'Lola']
rate = [100000, 125000, 130000]
prize = ['15.3%', '20.0%', '17.9%']

res = {i[0]: i[1] * float(i[-1][:-1]) / 100 for i in zip(name, rate, prize)}
print(res)


'''
Задание 3.
Создайте функцию генератор чисел Фибоначчи
'''

n = int(input('Сколько чисел Фибоначчи хотите вывести? Введите целое число: '))

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, b+a

print(list(fibo(n)))