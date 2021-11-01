import random
import sys
import timeit
import cProfile
import functools
import ctypes
import struct

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

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

# print(fact(5))


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# print(fib(10))

# Функция Аккермана
# import sys
# sys.setrecursionlimit(3000)


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))  # m > 0 n > 0


# print(akk(2, 0))

# Алгоритм Евклида (наибольший общий делитель)
# Циклический вычитание
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


# print(gcd(54, 24))


# Рекурсивный
def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


# print(gcd2(54, 24))

# Циклический остаток от деления


def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


# print(gcd3(54, 24))

# Решето Эратосфена (отбираем простые числа)


n = int(input('До какого числа получить список?: '))
sieve = [i for i in range(n)]
sieve[1] = 0
print(sieve)
for i in range(2, n):
    if sieve[i] != 0:
        j = i * 2
        while j < n:
            sieve[j] = 0
            j += i
            print(i)
            print(f'J - {j}')
result = [i for i in sieve if i != 0]
print(result)

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

# Ключ словаря - не изменяемый объект

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

# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test {i} Ok')


# def fib_list(n):
#     fib_l = [None] * 1000
#     fib_l[:2] = [0, 1]
#
#     def _fib_list(n):
#         if fib_l[n] is None:
#             fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
#         return fib_l[n]
#
#     return _fib_list(n)


# test_fib(fib_list)

# fib_list(10) - 1000 loops, best of 5: 11.4 usec per loop
# fib_list(20) - 1000 loops, best of 5: 16.7 usec per loop
# fib_list(100) - 1000 loops, best of 5: 43.1 usec per loop
# fib_list(200) - 1000 loops, best of 5: 93.2 usec per loop
# fib_list(500) - 1000 loops, best of 5: 218 usec per loop

# cProfile.run('fib_list(500)')

#fib_list(10) - 19/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
#fib_list(20) - 39/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
#fib_list(100) - 199/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)
#fib_list(500) - 999/1    0.000    0.000    0.000    0.000 algstr.py:411(_fib_list)

# Фибоначчи через цикл
# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test {i} Ok')


# def fib_loop(n):
#     if n < 2:
#         return n
#     first, second = 0, 1
#     for i in range(2, n + 1):
#         first, second = second, first + second
#     return second

# print(test_fib(fib_loop))

#python -m timeit -n 1000 -a "import algstr" "algstr.fib_loop(10)"
#fib_loop(10) - 1000 loops, best of 5: 756 nsec per loop
#fib_loop(100) - 1000 loops, best of 5: 5.13 usec per loop
#fib_loop(500) - 1000 loops, best of 5: 32.2 usec per loop
#fib_loop(50000) - 1000 loops, best of 5: 29.9 msec per loop

# cProfile.run('fib_loop(1000)')


# @functools.lru_cache()
# def fib(n):
#     if n < 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# fib(10) - 1000 loops, best of 5: 101 nsec per loop
# fib(100) - 1000 loops, best of 5: 91.6 nsec per loop
# fib(200) - 1000 loops, best of 5: 83.7 nsec per loop
# UserWarning: The test results are likely unreliable.
# The worst time (1.02 usec) was more than four times slower than the best time (83.7 nsec).

# cProfile.run('fib(200)')
#fib(10) - 11/1    0.000
# 0.000    0.000    0.000 algstr.py:462(fib)
#fib(100) - 101/1    0.000    0.000    0.000    0.000 algstr.py:462(fib)
#fib(200) - 201/1    0.000    0.000    0.000    0.000 algstr.py:462(fib)

# Модуль Collections
from collections import Counter, deque, defaultdict, OrderedDict, namedtuple, ChainMap

# a = Counter()
# b = Counter('abrakadabra')
# c = Counter({'red': 2, 'blue': 4})
# d = Counter(cat=4, dog=5)
# print(a, b, c, d, sep='\n')
# print(b['z'])
# b['z'] = 0
# print(b)
# print(list(b.elements()))
# print(b.most_common(2))
# q = Counter(a=4, b=6, c=-2, d=0)
# f= Counter(a=1, b=2, c=3, d=-2)
# q.subtract(f)
# print(q)
# print('*' * 50)
# print(set(q))
# print(dict(q))
# q.clear()
# print(q)
# print('*' * 50)
# x = Counter(a=3, b=1)
# y = Counter(a=1, b=2)
# print(x + y)
# print(x - y)
# print(x & y)
# print(x | y)
# print('*' * 50)
# z = Counter(a=2, b=-4)
# print(+z)
# print(-z)

# Deque
# a = deque()
# b = deque('abcdef')
# c = deque([1, 2, 3, 4, 5])
# print(a, b, c, sep='\n')
# b = deque('abcdef', maxlen=3)
# c = deque([1, 2, 3, 4, 5], maxlen=4)
# c.clear()
# print(b, c, sep='\n')
# Добавление в очередь
# print('*' * 50)
# d = deque([i for i in range(5)], maxlen=7)
# d.append(5)
# d.appendleft(6)
# print(d)
# d.extend([7, 8, 9])
# print(d)
# d.extendleft([10, 11, 12])
# print(d)
# Забрать элементы из очереди
# print('*' * 50)
# f = deque([i for i in range(5)], maxlen=7)
# x = f.pop()
# y = f.popleft()
# print(f, x, y, sep='\n')
# # Другие методы
# print('*' * 50)
# g = deque([i for i in range(5)], maxlen=7)
# print(g.count(2))
# print(g.index(3))
# g.insert(2, 6)
# print(g)
# g.reverse()
# print(g)
# g.rotate(3)
# print(g)
# Пример использования
# array = [random.randint(-100, 100) for _ in range(10)]
# print(array)
# deq = deque()
# for item in array:
#     if item > 0:
#         deq.append(item)
#     elif item < 0:
#         deq.appendleft(item)
# print(deq)

# DefaultDict

# a = defaultdict()
# print(a)
# s = 'ssdeegrhcxdceutigakqdkdgjxdce'
# b = defaultdict(int)
# for i in s:
#     b[i] += 1
# print(b)
#
# list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
# c = defaultdict(list)
# for k, v in list_1:
#     c[k].append(v)
# print(c)
#
# list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('dog', 5)]
# d = defaultdict(set)
# for k, v in list_1:
#     d[k].add(v)
# print(d)
#
# f = defaultdict(lambda: 'unknown')
# f.update(rex='dog', thomas='cat')
# print(f)
# print(f['rex'])
# print(f['jerry'])
# print(f.get('thomas'))

# OrderedDict
# Сортируем по ключам
# a = {'cat': 5, 'mouse': 4, 'dog': 2}
# new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
# print(new_a)
# # Сортируем по значениям
# b = {'cat': 5, 'mouse': 4, 'dog': 2}
# new_b = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
# print(new_b)
# print(new_a == new_b)
#
# new_b.move_to_end('mouse')
# print(new_b)
#
# new_b.move_to_end('mouse', last=False)
# print(new_b)

# Удаляем последний элемент
# new_b.popitem()
# print(new_b)

# # Удаляем первый элемент
# new_b.popitem(last=False)
# print(new_b)
#
# new_b['cow'] = 1
# print(new_b)
# new_b['dog'] = 8
# print(new_b)
# print('*' * 50)
#
# new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
# print(new_c)
#
# for key in reversed(new_c):
#     print(key, new_c[key])
#
# # Работа с файлом big_log.txt
# N = 3000
# with open('big_log.txt', 'r', encoding='utf-8') as f:
#     log = deque(f, N)
# print(log)
#
# data = OrderedDict()
# spam = defaultdict(int)
#
# for item in log:
#     ip = item[:-1]
#     if not ip.startswith('192.168'):
#         spam[ip] += 1
#         data[ip] = 1
# print(spam)
# print(data)
# data.update(spam)
# print(data)
# with open('data.txt', 'w', encoding='utf-8') as f:
#     for key, value in data.items():
#         f.write(f'{key} - {value}\n')

# namedtuple

# hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
# print(hero_1[4])


# class Person:
#
#     def __init__(self, name, race, health, mana, strength):
#         self.name = name
#         self.race = race
#         self.health = health
#         self.mana = mana
#         self.strength = strength


# hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
# print(hero_2.mana)
#
# New_Person = namedtuple('New_Person', 'name, race, health, mana, strength')
# hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
# print(hero_3)
# print(hero_3.race)
#
# prop = ['name', '3race', 'health', '_mana', 'strength']
# New_Person_1 = namedtuple('New_Person_1', prop, rename=True) # переименование недопустимых имен (цифры и т.п)
# hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
# print(hero_4)
#
# print('*' * 50)
# Point = namedtuple('Point', 'x, y, z')
# p1 = Point(2, z=3, y=4)
# print(p1)
#
# t = [5, 10, 15]
# p2 = Point._make(t)
# print(p2)
# d2 = p2._asdict()
# print(d2)
#
# p3 = p2._replace(x=6)
# print(p3)
#
# print(p3._fields)
#
# print('*' * 50)
#
# New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
# p4 = New_Point(5)
# print(p4)
#
# print(p4._field_defaults)
#
# dct = {'x': 10, 'y': 20, 'z': 30}
# p5 = New_Point(**dct)
# print(p5)

# ChainMap

# d_1 = {'a': 2, 'b': 4, 'c': 6}
# d_2 = {'a': 10, 'b': 20, 'd': 40}
# d_map = ChainMap(d_1, d_2)
# print(d_map)
# d_2['a'] = 100
# print(d_map)
# print(d_map['a'])
# print(d_map['d'])
# print('*' * 50)
# x = d_map.new_child({'a': 111, 'b': 222, 'c': 333, 'd': 444})
# print(x)
# print(x.maps[0])
# print(x.maps[-1])
# print(x.parents)
# print('*' * 50)
# y = d_map.new_child()
# print(y)
# print(y['a'])
# y['a'] = 1
# print(y)
# print(list(y))
# print(list(y.values()))
#
# import argparse
# defaults = {'ip': 'localhost', 'port': 7777}
# parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--ip')
# parser.add_argument('-p', '--port')
#
# args = parser.parse_args()
# new_dict = {key: value for key, value in vars(args).items() if value}
# settings = ChainMap(new_dict, defaults)
# print(settings['ip'])
# print(settings['port'])

# b = 0b100110
# print(b)
# c = int('2cd50', base=24)
# z = int('z', base=36)
# print(z)

# Работа списка
# allocated = 0
# for newsize in range(100):
#     if allocated < newsize:
#         new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
#         allocated = newsize + new_allocated
#
#         print(newsize, allocated)

# Объекты в памяти

# print(sys.version, sys.platform)
#
# a = 5
# b = 125.54
# c = 'Hello world'
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# lst = [i for i in range(10)]
# print(sys.getsizeof(lst))
#
#
# def show_size(x, level=0):
#     print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
#
#     if hasattr(x, '__iter__'):
#         if hasattr(x, 'items'):
#             for xx in x.items():
#                 show_size(xx, level + 1)
#         elif not isinstance(x, str):
#             for xx in x:
#                 show_size(xx, level + 1)
#
# show_size(a)
# show_size(b)
# show_size(c)
# show_size(lst)
#
# print('*' * 50)
# t = tuple(lst)
# show_size(t)
# print('*' * 50)
# s = set(lst)
# show_size(s)
# print('*' * 50)
# d = {str(i): i for i in range(10)}
# show_size(d)

a = 59
x = y = a
b = 125.54
# c = 'hello worldsssss'

# print(id(str))
# print(hash(c))
# print(id(a))
# print(id(type(a)))
# print(sys.getsizeof(a))
# print(ctypes.string_at(id(a), sys.getsizeof(a)))
# print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
# print(id(int))

# print('*' * 50)
# print(id(b))
# print(sys.getsizeof(b))
# z = b
# b = 122.99
# print(ctypes.string_at(id(b), sys.getsizeof(b)))
# print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))
# print(id(float))
# print('*' * 50)
# print(id(c))
# print(sys.getsizeof(c))
# print(ctypes.string_at(id(c), sys.getsizeof(c)))
# print(struct.unpack('LLLLLLLLLLLii' + 'c' * 13, ctypes.string_at(id(c), sys.getsizeof(c))))
# print(len(c))
# print('*' * 50)
# lst = [1, 2, 3, 4]
# print(sys.getsizeof(lst))
# print(struct.unpack('LLLLLLLLLi' + 'L' * 5 * 4, ctypes.string_at(id(lst), sys.getsizeof(lst))))

# c = 'hello world'
# print(id(c))
# print(sys.getsizeof(c))
# print(struct.unpack('LLLLLLLLLLLLc' + 'c' * len(c), ctypes.string_at(id(c), sys.getsizeof(c))))

# СОРТИРОВКА
# Пузырьком
size = 10
array = [i for i in range(size)]
random.shuffle(array)
# print(array)

# n = 1
# while n < len(array):
#     for i in range(len(array) - n):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
# print(array)

# for _ in array:
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]

# print(array)

# Выбором


# def selection_sort(array):
#     for i in range(len(array)):
#         idx_min = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[idx_min]:
#                 idx_min = j
#         array[idx_min], array[i] = array[i], array[idx_min]
#
#
# selection_sort(array)
# print(array)

# Сортировка вставками


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
            # print(j)
        array[j] = spam
        # print(array)

# insertion_sort(array)
# print(array)

# Сортировка Шелла


def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой'
    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()
    count = 0
    for increment in new_increment(array):
        # print(increment)
        for i in range(increment, len(array)):
            # print(i)
            for j in range(i, increment - 1, -increment):
                # print(j)
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                # print(array)
                count += 1
    # print(count)

shell_sort(array)
# print(array)

# Быстрая сортировка Хоара


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []
    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

array_new = quick_sort(array)
# print(array_new)

# То же, без использования дополнительной памяти


def quick_sort_no_memory(array, fst, lst):
    if fst >= lst:
        return
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)


quick_sort_no_memory(array, 0, len(array) - 1)
# print(array)

# Разворот массива

def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
revers(array)
# print(array)
#
# array.reverse()
# print(array)
# array.sort()
# print(array)

# print('*' * 50)
# t = tuple(random.randint(0, 100) for _ in range(size))
# print(t)
# t = tuple(sorted(t))
# print(t)

# Сортировка с использованием ключа

Person = namedtuple('Person', 'name, age')
p1 = Person('Vasya', 25)
p2 = Person('Kolya', 30)
p3 = Person('Olya', 23)
people = [p1, p2, p3]
# print(people)


def by_age(person):
    return person.age


# result = sorted(people, key=by_age)
# print(result)

from operator import attrgetter
result2 = sorted(people, key=attrgetter('age'))
# print(result2)

# Графы

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

# print(*graph, sep='\n')

# print('*' * 50)
# Ориентированный граф
# graph = [
#     [0, 1, 1, 0],
#     [0, 0, 1, 1],
#     [0, 1, 0, 0],
#     [0, 0, 0, 0]
# ]

# print(*graph, sep='\n')

print('*' * 50)
# Взвешенный граф

graph[0][1:3] = [2, 3]
graph[1][2] = 2
graph[2][1] = 2

# print(*graph, sep='\n')

# Списки смежности
# print('*' * 50)
# graph1 = []
# graph1.append([1, 2])
# graph1.append([0, 2, 3])
# graph1.append([0, 1])
# graph1.append([1])
# print(*graph1, sep='\n')

# print('*' * 50)
#
# graph2 = {
#     0: {1, 2},
#     1: {0, 2, 3},
#     2: {0, 1},
#     3: {1}
# }
# print(graph2)
#
# if 3 in graph2[1]:
#     print(True)

# print('*' * 50)
# Vertex = namedtuple('Vertex', ['vertex', 'edge'])
# graph3 = []
# graph3.append([Vertex(1, 2), Vertex(1, 3)])
# graph3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
# graph3.append([Vertex(0, 3), Vertex(1, 2)])
# graph3.append([Vertex(1, 1)])
# print(*graph3, sep='\n')

# for v in graph3[1]:
    # print(graph3[1])
    # if v.vertex == 3:
        # print(True)

class Graph:

    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge


# Список ребер

# print('*' * 50)
graph4 = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3)]

# print(*graph4, sep='\n')

# Поиск кратчайшего пути в ширину

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    deq = deque([start])
    is_visited[start] = True
    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            # return parent
            break
        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(vertex)
    else:
      return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
    cost += 1
    way.appendleft(start)
    return f'Кратчайший путь {list(way)} длиною {cost} условных единиц'

# s = int(input('От какой вершины идти: '))
# s = int(input('От какой вершины идти: '))
# f = int(input('До какой вершины идти: '))
# print(bfs(g, s, f))

# Алгоритм Дейкстры

g1 = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[start] = 0
    # print(cost)
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    # print(parent)
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost


# s = int(input('От какой вершины идти: '))
# print(dijkstra(g1, s))

# Деревья
# Создание
from binarytree import tree, bst, Node, build

# class MyNode:
#     def __init__(self, data, right=None, left=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
a = tree(height=4, is_perfect=False)
# print(a)
# b = bst(height=3, is_perfect=True)
# # print(b)
# c = Node(7)
# c.left = Node(3)
# c.right = Node(11)
# c.left.left = Node(1)
# c.left.right = Node(5)
# c.right.left = Node(9)
# c.right.right = Node(13)
# # print(c)
#
# d = build([7, 3, 11, 1, 5, 9, 13, None, 2, None, 6])
# print(d)

# Бинарный поиск. Алгоритм Хаффмана

def search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по следующему пути:\nКорень{path}'
    if number < bin_search_tree.value and bin_search_tree.left is not None:
        return search(bin_search_tree.left, number, path=f'{path}\nШаг влево')
    if number > bin_search_tree.value and bin_search_tree.right is not None:
        return search(bin_search_tree.right, number, path=f'{path}\nШаг вправо')
    return f'Число {number} отсутствует в дереве'


bt = bst(height=5, is_perfect=False)
# print(bt)
# print(bt.value)
# num = int(input('Введите число для поиска:'))
# print(search(bt, num))

# Хэш-функция

h_list = [None] * 26


def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    # print(h_list)

a = 'apricot'
my_append(a)
b = 'banana'
my_append(b)
c = 'apple'
my_append(c)

def my_index(value):
    letter = 26
    index = 0
    size = 10000
    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i
    return index % size

# print(my_index(a))
# print(my_index(b))
# print(my_index(c))

# Контроль целостности данных при их передаче
import hashlib
#
# print(hashlib.sha1(b'Hello world!').hexdigest())
# print(hashlib.sha1(b'Hello world.').hexdigest())
# print(hashlib.sha1(b'qwetfghjj' + b'Hello world.').hexdigest())
#
# s = hashlib.sha1(b'Hello world!').hexdigest()
# print(s.encode('utf-8'))
#
# print(hashlib.sha1(b'dffetgf' + s.encode('utf-8')).hexdigest())

# SHA-1 алгоритм
# Сравнение строк


def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')
    return ha == hb


# s1 = input('Введите строку 1: ')
# s2 = input('Введите строку 2: ')
# print('Строки одинаковые' if is_eq_str(s1, s2, True) else 'Строки разные')

# Поиск подстроки в строке. Алгоритм Рабина-Карпа

def Rabin_Karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                return i
    return -1


# s_1 = input('Введите строку: ')
# s_2 = input('Введите подстроку для поиска: ')

# pos = Rabin_Karp(s_1, s_2)
# print(pos)


# Закодировать любую строку по методу Хаффмана

import collections


class Leaf:
    """ вспомогательный класс Лист для создания дерева Хаффмана
        key - буква из кодируемой строки
        value - частота буквы в строке
    """
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value


class Node:
    """ вспомогательный класс Узел для построения дерева Хаффмана """

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Haffman:
    """ Класс, реализующий сжатие и восстановление строки по методу Хаффмана """
    _data: list

    def __init__(self):
        """ _code_table - таблица кодирования: key - буква, value - двоичный код
            _data - список для преобразования из строки в дерево
            _real_str - строка для кодирования
        """
        self._code_table = dict()
        self._data = []
        self._real_str = ''

    def _make_list(self, real_str):
        """ формируем упорядоченный по убыванию список объектов класса Leaf """
        counter = dict(collections.Counter(real_str))
        counter = collections.OrderedDict(sorted(counter.items(), key=lambda k: k[1], reverse=True))
        for key, value in counter.items():
            self._data.append(Leaf(key, value))
        return True

    def _haffmans_tree(self):
        """ функция формирует из списка объектов класса Leaf бинарное дерево по алгоритму Хаффмана """
        while len(self._data) > 2:
            b, a = self._data.pop(), self._data.pop()
            spam = Node(a.value + b.value, a, b)
            if spam.value > self._data[0].value:
                self._data.insert(0, spam)
            elif spam.value < self._data[-1].value:
                self._data.append(spam)
            else:
                for i in range(1, len(self._data)):
                    if self._data[i - 1].value >= spam.value > self._data[i].value:
                        self._data.insert(i, spam)
                        break
        self._data = Node(self._data[0].value + self._data[1].value, self._data[0], self._data[1])

    def _haffman_recursion(self, data: Node, code=''):
        """ рекурсивный обход дерева и построение таблицы кодирования """
        if isinstance(data, Node):
            self._haffman_recursion(data.left, code=code + '0')
            self._haffman_recursion(data.right, code=code + '1')
        elif isinstance(data, Leaf):
            self._code_table[data.key] = code

    def _encode(self):
        """ преобразование из строки в двоичный код
            имитация со строковым '0' и '1' для демонстрации работы
        """
        result = []
        for char in self._real_str:
            result.append(self._code_table[char])
        return ''.join(result)

    def encode(self, real_str):
        """ основной метод преобразования строки в код по алгоритму Хаффмана
            на вход подается строка real_str: str
            создается таблица для кодировки _code_table: dict
            На выходе закодированная строка code_str: str
        """
        self.__init__()
        self._real_str = real_str
        self._make_list(real_str)
        self._haffmans_tree()
        self._haffman_recursion(self._data)
        code_str = self._encode()
        return code_str


    def decode(self, code_str, code_table=None):
        """ декодирование строки из '0' и '1' на основе таблицы кодирования code_table
            если code_table не передан, используется полученная ранее таблица
        """
        if code_table:
            self._code_table = code_table
        decode_table = {value: key for key, value in self._code_table.items()}
        result = []
        i = 0
        while i < len(code_str):
            j = i + 1
            while code_str[i:j] not in decode_table.keys():
                j += 1
            result.append(decode_table[code_str[i:j]])
            i = j
        real_str = ''.join(result)
        return real_str

    def get_table_code(self):
        """ возвращает таблицу кодирования в виде словаря (буква: код)"""
        if self._code_table:
            return self._code_table
        return False

    def get_real_string_code(self):
        """ возвращает строку из '0' и '1' - реальный код строки для кодирования """
        if self._real_str:
            result = []
            for char in self._real_str:
                result.append(bin(ord(char))[2:].zfill(8))
            return ''.join(result)
        return False


# if __name__ == '__main__':
#     my_str = input('Введите строку для кодирования: ')
#     haf = Haffman()
#     code_s = haf.encode(my_str)
#     print(haf.get_real_string_code())
#     print(code_s)
#     table = haf.get_table_code()
#     print(table)
#     real_1 = haf.decode(code_s, table)
#     real_2 = haf.decode(code_s)
#     print(real_1)
#     print(real_2)