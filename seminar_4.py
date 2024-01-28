'''
Задание 1. Напишите функцию для транспонирования матрицы
'''

import random

SIZE_OF_MATRIX = 3
LOWER_LIMIT = 1
UPPER_LIMIT = 10

matrix = []
for i in range(SIZE_OF_MATRIX):
    matrix.append(list(random.randint(LOWER_LIMIT, UPPER_LIMIT) for _ in range(SIZE_OF_MATRIX)))

def matrix_transposition(lst):
    matrix_trnsp = []
    COUNT_OF_COLUMNS = len(matrix[0])
    for i in range(len(matrix)):
        res = []
        for j in range(COUNT_OF_COLUMNS):
            res.append(matrix[j][i])
        matrix_trnsp.append(res)
    return matrix_trnsp

print(f'\nЗадание 1:\nИсходная матрица - {matrix}\nТранспонированная матрица - {matrix_transposition(matrix)}\n')

'''
Задание 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''

def get_transp_dict(**kwargs):
    input_dict = kwargs
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        output_dict[value] = key
    return output_dict

print(f'\nЗадание 2:\n{get_transp_dict(one=1, two=2, seven=7, ten=10)}\n')

'''
Задание 3. Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.

Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
'''

print(f'\nЗадание 3:')

lst = []

def deposit(balance, amount):
    # Пополнение счета
    WEALTH_TAX = 0.10
    if amount % 50 != 0:
        print("Сумма пополнения должна быть кратной 50 у.е.")
        if balance > 5000000:
            balance -= amount * WEALTH_TAX
            lst.append(f'налог на богатство {amount * WEALTH_TAX} у.е.')
        lst.append(f'неудачное пополнение на {amount} у.е.')
        return balance  # Если сумма не кратна 50, возврат без изменения баланса
    balance += amount
    if balance > 5000000:
            balance -= amount * WEALTH_TAX
    print(f"Вы пополнили счет на {amount} у.е.")
    lst.append(f'пополнение на {amount} у.е.')
    return balance

def withdraw(balance, amount):
    # Снятие средств
    if amount % 50 != 0:
        print("Сумма снятия должна быть кратной 50 у.е.")
        lst.append(f'неудачное снятие {amount} у.е.')
        return balance  # Если сумма не кратна 50, возврат без изменения баланса

    if amount > balance:
        print("Недостаточно средств на счете.")
        lst.append(f'неудачное снятие {amount} у.е.')
        return balance  # Если недостаточно средств, возврат без изменения баланса

    PERCENT = 0.015
    if 30 < amount < 600:
        comission = amount * PERCENT
    elif amount < 30:
        comission = 30
    else: comission = 600
    lst.append(f'комиссия за снятие {comission} у.е.')

    WEALTH_TAX = 0.10 
    if balance > 5000000:
        res_amount = amount + comission + (amount * WEALTH_TAX)
        lst.append(f'налог на богатство {amount * WEALTH_TAX} у.е.')
    else:
        res_amount = amount + comission

    balance -= res_amount
    print(f"Вы сняли {amount} у.е.")
    lst.append(f'снятие {amount} у.е.')
    return balance

def apply_interest(balance, transactions):
    # Начисление процентов
    if transactions % 3 == 0:
        interest = round(0.03 * balance, 2)
        balance += interest
        print(f"Начислены проценты: {interest} у.е.")
        lst.append(f'начисление процентов {interest} у.е.')
    return balance

def check_balance(balance):
    # Проверка баланса
    print(f"Ваш баланс: {balance} у.е.")

def atm_menu():
    balance = 0
    transactions = 0

    while True:
        print("\nМеню банкомата:")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ")
        if choice == '1':
            amount = int(input("Введите сумму для пополнения: "))
            balance = deposit(balance, amount)
            check_balance(balance)
            transactions += 1
            balance = apply_interest(balance, transactions)
        elif choice == '2':
            amount = int(input("Введите сумму для снятия: "))
            balance = withdraw(balance, amount)
            check_balance(balance)
            transactions += 1
            balance = apply_interest(balance, transactions)
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

atm_menu()
print(lst)