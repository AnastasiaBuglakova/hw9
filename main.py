# Решить задания, которые не успели решить на семинаре.
# Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.
import csv
import json
import os
import random
from typing import Callable
from functools import wraps


#
# def json_safe(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if not os.path.exists(f'result.json'):
#             print(result)
#             with open(f'result.json', 'w', encoding='utf-8') as f:
#                 atr = ','.join(list(map(str, args))) + '|' + ','.join(
#                     list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
#                 json.dump({atr: result}, f, indent=4, ensure_ascii=False)
#
#         else:
#             with open(f'result.json', 'r', encoding='utf-8') as f_read:
#                 json_data = json.load(f_read)
#                 print(json_data)
#             with open(f'result.json', 'w', encoding='utf-8') as f_write:
#                 atr = ','.join(list(map(str, args))) + '|' + ','.join(
#                     list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
#                 json_data[atr] = result
#                 json.dump(json_data, f_write, indent=4, ensure_ascii=False)
#
#         return result
#
#     return wrapper
#
#
# def decor(loop: int):
#     def inner(func):
#         result = []
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(loop):
#                 result.append(func(*args, **kwargs))
#             return result
#
#         return wrapper
#
#     return inner
#
#
# def check_nums(func: Callable):
#     @wraps(func)
#     def wrapper(l_lim: int, h_lim: int, tries_: int):
#         if l_lim > h_lim or l_lim < 0 or h_lim > 100:
#             l_lim = 1
#             h_lim = 100
#         if tries_ not in range(1, 2):
#             tries_ = random.randint(1, 2)
#
#         result = func(l_lim, h_lim, tries_)
#         return result
#
#     return wrapper
#
#
# @decor(3)
# @json_safe
# @check_nums
# def guess_number(low: int = 10, high: int = 100, tries: int = 1) -> str:
#     count = 1
#     number = random.randint(low, high)
#     while count <= tries:
#         my_num = int(input(f'{count} из {tries} попытка. Введите число от {low} до {high}: '))
#         if my_num > number:
#             print('Я загадал меньше')
#         elif my_num < number:
#             print('Я загадал больше')
#         else:
#             result = f'Да ты победил c {count} попытки, я загадал {number}'
#             break
#         count += 1
#     else:
#         result = 'Извини, но ты проиграл, все попытки закончились'
#     print(result)
#     return result
#
#
# guess_number(-1, 1000, 15)
# print(f'{guess_number.__name__=}')


def json_safe(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not os.path.exists(f'solve_q_equation.json'):
            with open(f'solve_q_equation.json', 'w', encoding='utf-8') as f:
                atr = ','.join(list(map(str, args))) + ','.join(
                    list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                json.dump({atr: result}, f, indent=4, ensure_ascii=False)

        else:
            with open(f'solve_q_equation.json', 'r', encoding='utf-8') as f_read:
                json_data = json.load(f_read)
            with open(f'solve_q_equation.json', 'w', encoding='utf-8') as f_write:
                atr = ','.join(list(map(str, args))) + ','.join(
                    list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                json_data[atr] = result
                json.dump(json_data, f_write, indent=4, ensure_ascii=False)

        return result

    return wrapper


def data_from_csv(num: int = 100):
    def deco(func: Callable):
        res = []

        def wrapper(*args, **kwargs):
            if args or kwargs:
                print(func(*args, **kwargs))
            else:
                with open("numbers in csv.csv", 'r', encoding='utf-8') as f:
                    csv_data = csv.reader(f)
                    for i in csv_data:
                        res.append(func(float(i[0]), float(i[1]), float(i[2])))

            return res

        return wrapper

    return deco

    # Напишите следующие функции:
    # Нахождение корней квадратного уравнения


@data_from_csv(4)
@json_safe
def solve_q_equation(a: int, b: int, c: int) -> str:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0 or a == 0:
        return 'Корней нет'
    elif discriminant == 0:
        x = round(-b / (2 * a), 2)
        return f'{x = }'
    else:
        x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
        x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
        return f'{x1 = }, {x2 = }'


print(f'{solve_q_equation() = }')


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

def gen_csv():
    numbers_for_csv = [[random.randint(0, 99) for _ in range(3)] for _ in range(random.randint(100, 1001))]
    with open('numbers in csv.csv', 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f)

        csv_write.writerows(numbers_for_csv)


gen_csv()

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
