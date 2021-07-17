import random
import timeit
import cProfile
# Алгоритмы и структуры данных

# class Stack:
#
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
#
# s = Stack()
#
# print(s.is_empty())
# s.push(4)
# s.push('name')
# s.push([1, 2])
# print(s.peek())
# print(s.size())
# s.pop()
# print(s.peek())
# print(s.size())

# Циклы, функции, рекурсия
# Рекурсия


# def func(a, b):
#     if a == b:
#         return f'{a}'
#     elif a < b:
#         return f'{a} {func(a + 1, b)}'
#
#
# print(func(1, 10))

# Функция Аккермана
# import sys
# sys.setrecursionlimit(3000)
#
#
# def akk(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return akk(m - 1, 1)
#     return akk(m - 1, akk(m, n - 1))  # m > 0 n > 0
#
#
# print(akk(2, 0))
# Алгоритм Евклида (наибольший общий делитель)
# Циклический вычитание
# def gcd(m, n):
#     while m != n:
#         if m > n:
#             m -= n
#         else:
#             n -= m
#     return m


# print(gcd(54, 24))


# Рекурсивный
# def gcd2(m, n):
#     if n == 0:
#         return m
#     return gcd2(n, m % n)


# print(gcd2(54, 24))

# Циклический остаток от деления


# def gcd3(m, n):
#     while n != 0:
#         m, n = n, m % n
#     return m

# Решето Эратосфена (отбираем простые числа)


# n = int(input('До какого числа получить список?: '))
# sieve = [i for i in range(n)]
# sieve[1] = 0
# print(sieve)
# for i in range(2, n):
#     if sieve[i] != 0:
#         j = i * 2
#         while j < n:
#             sieve[j] = 0
#             j += i
# result = [i for i in sieve if i != 0]
# print(result)

# Перевод десятичного числа в двоичный формат


# def binary(num):
#     s = ''
#     while num > 0:
#         s = f'{num % 2} {s}'
#         num //= 2
#     return s


# print(binary(25))


# while True:
#     n = int(input('Введите целое число: '))
#     if n != 0:
#         print(binary(n))
#     else:
#         break

# МАССИВЫ
# li = [1, 2, 3, 4]
# for i in li:
#     li.remove(i)
# print(li)

# for i in li[:]:
#     li.remove(i)
# print(li)

# for i in li2:
#     li2.pop(i)
# print(li2)

# Крестики-нолики
# row = [''] * 3
# print(row)
# board = [row] * 3
# print(board)
# board[0][0] = 'X'
# print(board)
# Лучше создавать списки генератором (создаются разные объекты, а не ссылки на один и тот же)
# board1 = [[''] * 3 for i in range(3)]
# board1[0][0] = 'X'
# print(board1)

# те же операнды, другая история
# a = [1, 2, 3, 4]
# b = a
# a = a + [5, 6, 7]
# print(a, b)

# a = [1, 2, 3, 4]
# b = a
# a += [5, 6, 7]
# print(a, b)

# Запятая в кортеже
# t = ('one', 'two')
# for i in t:
#     print(i)

# t = ('one',)
# for i in t:
#     print(i)

# Сохраним уникальные значения

# lst = [1, 2, 4, 6, 6, 6, 7, 8, 8]
# lst2 = list(set(lst))
# print(lst2)

# Ключ словаря - изменяемый объект

set_x = {1, 2, 3}
lst_x = [2, 4, 9]
# dict_x = {set_x: lst_x}  # ошибка, изменяемый объект
# print(dict_x)
# dict_x = {frozenset(set_x): lst_x}
# dict_x2 = {tuple(lst_x): set_x}
# print(dict_x)
# print(dict_x2)

# Бинарный поиск


# def bin_search(array, value):
#     left = 0
#     right = len(array) - 1
#     pos = len(array) // 2
#     while array[pos] != value and left <= right:
#         if value > array[pos]:
#             left = pos + 1
#         else:
#             right = pos - 1
#         pos = (left + right) // 2
#     return -1 if left > right else pos


# a = [random.randint(0, 1000) for _ in range(100)]
# a.sort()
# print(a, end=' ')
# print()
# n = int(input('Enter el to find: '))
# print(bin_search(a, n))

# Разложить положительные и отрицательные числа по разным массивам

# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
# arr_below = []
# arr_bigger = []
# for item in array:
#     if item > 0:
#         arr_bigger.append(item)
#     else:
#         arr_below.append(item)
# print(arr_below)
# print(arr_bigger)

# Вставка элемента в произвольное место массива
# (механизм работы метода insert())
# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
# num = int(input('Enter num: '))
# pos = int(input('Enter position: '))
# array.append(None)
# i = len(array) - 1
# while i > pos:
#     array[i], array[i-1] = array[i-1], array[i]
#     i -= 1
# array[pos] = num
# print(array)

# array2 = array[:pos] + num[pos] + array[pos+1:] - тратит больше памяти, т.к. создается новый список

# МАТРИЦА
size = 5
matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
#
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()
# print(len(matrix))

# Посчитать сумму строк и столбцов матрицы

# sum_column = [0] * len(matrix[0])

# for line in matrix:
#     sum_line = 0
#     for i, item in enumerate(line):
#         sum_line += item
#         sum_column[i] += item
#         print(f'{item:>5}', end='')
#
#     print(f'    |  {sum_line}')
# print('-' * len(matrix) * 5)
#
# for s in sum_column:
#     print(f'{s:>5}', end='')

# Обмен значений главной и побочной диагоналей
# квадратной матрицы

# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()
# print('-' * 20)
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             spam = matrix[i][j]
#             matrix[i][j] = matrix[i][size - 1 - j]
#             matrix[i][size - 1 - j] = spam
#
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()

# Ассоциативные массивы

# k = int(input('Enter number of enterprises: '))
# enterprises = {}
# for i in range(1, k + 1):
#     name = input('Enter name of enterprises: ')
#     enterprises[name] = [float(input('Plan: ')), float(input('Fact: '))]
#     enterprises[name].append(enterprises[name][1] / enterprises[name][0])
# print('Fact profit more then 10, but not plan (less then 100%)')
# for key, value in enterprises.items():
#     if value[1] > 10 and value[2] < 1:
#         print(f'Предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')

# Эмпирическая оценка алгоритмов
# x = 2 + 2
# print(timeit.timeit('x = 2 + 2'))
# print(timeit.timeit('x = sum(range(10))'))


# def get_len(array):
#     return len(array)


# def get_sum(array):
#     s = 0
#     for i in array:
#         s += i
#     return s


# def main():
#     lst = [i for i in range(1000000)]
#     a = get_len(lst)
#     b = get_sum(lst)
#
#
# cProfile.run("main()")


# Рекурсивный поиск чисел Фибоначчи
# def test_fib(func):
#     lst = [1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test {i} Ok')


# def fib(n):
#     if n < 2:
#         return 1
#     return fib(n-1) + fib(n-2)


# cProfile.run('fib(20)')
# print(test_fib(fib))
#fib(10) - 1000 loops, best of 5: 17.6 usec per loop
#fib(15) - 1000 loops, best of 5: 197 usec per loop
#fib(20) - 1000 loops, best of 5: 2.2 msec per loop

#cProfile
#fib(10) -  177/1    0.000    0.000    0.000    0.000 algstr.py:344(fib)
#fib(15) -  1973/1    0.001    0.000    0.001    0.001 algstr.py:344(fib)
#fib(20) -  21891/1    0.009    0.000    0.009    0.009 algstr.py:344(fib)

# Рекурсия + словарь
# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test {i} Ok')


# def fib_dict(n):
#     fib_d = {0: 0, 1: 1}
#
#     def _fib_dict(n):
#         if n in fib_d:
#             return fib_d[n]
#
#         fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
#         return fib_d[n]
#
#     return _fib_dict(n)


# test_fib(fib_dict)

# fib_dict(10) - 1000 loops, best of 5: 4.29 usec per loop
# fib_dict(15) - 1000 loops, best of 5: 5.94 usec per loop
# fib_dict(20) - 1000 loops, best of 5: 8 usec per loop
# fib_dict(100) - 1000 loops, best of 5: 47.7 usec per loop
# fib_dict(200) - 1000 loops, best of 5: 99.2 usec per loop
# fib_dict(500) - 1000 loops, best of 5: 278 usec per loop

# cProfile.run('fib_dict(500)')

#fib_dict(10) -  19/1    0.000    0.000    0.000    0.000 algstr.py:372(_fib_dict)
#fib_dict(20) -  39/1    0.000    0.000    0.000    0.000 algstr.py:372(_fib_dict)
#fib_dict(100) -  199/1    0.000    0.000    0.000    0.000 algstr.py:372(_fib_dict)
#fib_dict(500) -  999/1    0.000    0.000    0.000    0.000 algstr.py:372(_fib_dict)

# Рекурсия и список

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} Ok')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


# test_fib(fib_list)

# fib_list(10) - 1000 loops, best of 5: 11.4 usec per loop
# fib_list(20) - 1000 loops, best of 5: 16.7 usec per loop
# fib_list(100) - 1000 loops, best of 5: 43.1 usec per loop
# fib_list(200) - 1000 loops, best of 5: 93.2 usec per loop
# fib_list(500) - 1000 loops, best of 5: 218 usec per loop

cProfile.run('fib_list(500)')

#fib_list(10) - 19/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
#fib_list(20) - 39/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
#fib_list(100) - 199/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
#fib_list(500) - 999/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
