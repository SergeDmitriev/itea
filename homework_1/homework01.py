# Задание 1. Встроенные типы данных, операторы, функции и генераторы
#
# Напишите реализации объявленных ниже функций. Для проверки
# корректности реализации ваших функций, запустите тесты:
#
# pytest test_homework01.py
#
# Если написанный вами код не содержит синтаксических ошибок,
# вы увидите результаты тестов ваших решений.
import itertools
from collections import Iterable
from functools import reduce
from operator import mul
from timeit import timeit


def fac(n):
    """
    Факториал

    Факториал числа N - произведение всех целых чисел от 1 до N
    включительно. Например, факториал числа 5 - произведение
    чисел 1, 2, 3, 4, 5.

    Функция должна вернуть факториал аргумента, числа n.
    """
    # assert n >= 0, f'Входящее исло должно быть положтельным!'
    # result = 1
    # for j in {i for i in range(1, n+1)}:
    #     result = result*j
    # return result

    # Вариант более компактный:
    for i in range(1, n):
        n *= i
    return n


def factr(n):
    if n == 1:
        return 1
    else:
        return n * factr(n - 1)
    # поламается на ~ 1000 итерации


def facrr(n):
    # reduce(lambda x, y: x * y, range(1, n), n)
    return reduce(mul, range(1, n), n)


def gcd(a, b):
    """
    Наибольший общий делитель (НОД) для двух целых чисел.

    Предполагаем, что оба аргумента - положительные числа
    Один из самых простых способов вычесления НОД - метод Эвклида,
    согласно которому

    1. НОД(a, 0) = a
    2. НОД(a, b) = НОД(b, a mod b)

    (mod - операция взятия остатка от деления, в python - оператор '%')
    """
    while True:
        if a < b:
            a, b = b, a

        if a % b == 0:
            return b
        else:
            a = a % b


def fib():
    """
    Генератор для ряда Фибоначчи

    Вам необходимо сгенерировать бесконечный ряд чисел Фибоначчи,
    в котором каждый последующий элемент ряда является суммой двух
    предыдущих. Начало последовательности: 1, 1, 2, 3, 5, 8, 13, ..

    Подсказка по реализации: для бесконечного цикла используйте идиому

    while True:
      ..

    """

    # start = [1, 1, 2, 3, 5, 8, 13]
    # f = start[0]
    # s = start[1]
    # yield f  # ряд начинается не с 0 и ждет первое значение равное 1
    #
    # while True:
    #     yield f
    #     s = f + s
    #     yield s
    #     f = f + s
    #
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


def flatten(seq):
    """
    Функция, преобразующая вложенные последовательности любого уровня
    вложенности в плоские, одноуровневые.

    >>> flatten([])
    []
    >>> flatten([1, 2])
    [1, 2]
    >>> flatten([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten([(1, 2), (3, 4)])
    [1, 2, 3, 4]
    """

    acc = []
    for i in seq:
        if isinstance(i, Iterable):
            acc.extend(flatten(i))
        else:
            acc.append(i)
    return acc


def flat(seq):
    for i in seq:
        if type(i) in {list, tuple}:
            yield from flat(i)
        else:
            yield i


if __name__ == '__main__':
    pass
