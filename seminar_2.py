'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
'''

DIV_HEX = 16
num_original = int(input('Введите целое число для перевода в шестнадцатеричную систему: '))
num = num_original
num_hex = hex(num)[2:]
result = ''
dict_of_some_div = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
while num>0:
    div = num % DIV_HEX
    if div > 9:
        div = dict_of_some_div.get(div)
    result = str(div) + result
    num //= DIV_HEX

print(f'Число {num} в шестнадцатеричной системе - {result}')
if result == num_hex:
    print('Результат перевода соотвествует функции hex')
else: print('Результат перевода не соотвествует функции hex')


'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions
'''

import fractions
from math import gcd

while True:
    n = input('Введите первую дробь в формате a/b: ')
    separator = '/'
    if separator in n:
        a1, b1 = map(int, n.split('/'))
        break
while True:
    m = input('Введите вторую дробь в формате a/b: ')
    separator = '/'
    if separator in n:
        a2, b2 = map(int, n.split('/'))
        break

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)

a3_p, b3_p = a1 * a2, b1 * b2
max_divisor_of_a3_b3 = gcd(a3_p, b3_p)
if max_divisor_of_a3_b3 > 1:
    a3_p, b3_p = a3_p / max_divisor_of_a3_b3, b3_p / max_divisor_of_a3_b3
product = str(a3_p) + '/' + str(b3_p)
print(f'Результат умножения {n} на {m} составляет {product}')
if product == str(f1 * f2):
    print('Результат умножения совпадает с модулем fraction')
else: print('Результат умножения не совпадает с модулем fraction')

a3_s, b3_s = a1 * b2 + a2 * b1, b1 * b2
max_divisor = gcd(a3_s, b3_s)
if max_divisor > 1:
    a3_s, b3_s = int(a3_s / max_divisor), int(b3_s / max_divisor)
summa = str(a3_s) + '/' + str(b3_s)
print(f'Результат сложения {n} и {m} составляет {summa}')
if summa == str(f1 + f2):
    print('Результат сложения совпадает с модулем fraction')
else: print('Результат сложения не совпадает с модулем fraction')
