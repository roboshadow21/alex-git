# import collections
import random


# d1 = {'a': 1}
# d2 = {'b': 2}
# c = d1 | d2
# # c = {**d1, **d2}
# print(c)
# s = 't_srteTY'
# li = s.removeprefix('t_')
# print(li)
# li = s.removesuffix('TY')
# print(li)
# l = [1, 2, 2 , 3, 4, 4, 4 ,5]
# c = collections.Counter(l)
# print(c)
# print(c.most_common(2))
# size = 4
# matrix = [[random.randint(0, 50) for _ in range(size)] for _ in range(size)]
# column_sum = [0] * len(matrix[0])
# for row in matrix:
#     row_sum = 0
#     for i, item in enumerate(row):
#         print(f'{item:>4}', end='')
#         row_sum += item
#         column_sum[i] += item
#     print(f'   | {row_sum:>4}', end='')
#     print()
#
# print('-' * 20)
# for s in column_sum:
#     print(f'{s:>4}', end='')
#
# print()
#
# print('*' * 20)
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             spam = matrix[i][j]
#             matrix[i][j] = matrix[i][size - 1 - j]
#             matrix[i][size - 1 - j] = spam
#
# column = [0] * size
# for row in matrix:
#     row_sum = 0
#     for i, item in enumerate(row):
#         print(f'{item:>4}', end='')
#         row_sum += item
#         column[i] += item
#     print(f'    |  {row_sum:>4}')
#     print()
#
# print('-' * 20)
# for el in column:
#     print(f'{el:>4}', end='')
# sort_list = [9, 9, 8, 4, 6, 2, 1]
# sort_len = len(sort_list)
# for _ in sort_list:
#     for i in range(sort_len - 1):
#         if sort_list[i] > sort_list[i + 1]:
#             sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
#
# print(sort_list)
#
# for i in range(sort_len):
#     minimum = i
#     for j in range(i+1, sort_len):
#         if sort_list[j] < sort_list[minimum]:
#             minimum = j
#         sort_list[i], sort_list[minimum] = sort_list[minimum], sort_list[i]
# print(sort_list)
#
#
# def quick_sort(seq):
#     if len(seq) < 2:
#         return seq
#     mid = random.choice(seq)
#     eq_nums = [mid] * seq.count(mid)
#     less = [n for n in seq if n < mid]
#     more = [n for n in seq if n > mid]
#     return quick_sort(less) + eq_nums + quick_sort(more)
#
#
# print(quick_sort(sort_list))

# st = 'qwerty'
# s = ''
# for i in st:
#     s = f'{i} {s}'
#     print(s)
# def acc(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return acc(m - 1, 1)
#     else:
#         return acc(m - 1, acc(m, n - 1))
#
# print(acc(3, 5))

# import os
# import sqlite3
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# path = r'C:\Users\Анна\PycharmProjects\pythonProject2'
# file = 'test.db'
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(path, file)
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# db.create_all()
# n = 9
# def prime(n):
#     upper = int(n ** 0.5)
#     for i in range(2, upper + 1):
#         if n % i == 0:
#             return False
#     return True
#
# print(prime(3))


def fib_loop(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]
    # if prod == 0:
    #     return [0, 1, True]
    # elif prod == 1:
    #     return [1, 1, True]
    # elif prod == 2:
    #     return [1, 2, True]
    # elif prod == 3:
    #     return [2, 3, False]
    # first, second = 0, 1
    # for i in range(2, prod + 1):
    #     first, second = second, first + second
    #     if first * second == prod:
    #         return [first, second, True]
    #     elif first * second > prod:
    #         return [first, second, False]


# print(fib_loop(4895))

# def fib_loop(n):
#     if n < 2:
#         return n
#     first, second = 0, 1
#     for i in range(2, n + 1):
#         first, second = second, first + second
#     return second
sort_list = [9, 7, 8, 13, 2, 5, 8, 6, 4, 1]
sort_len = len(sort_list)
for _ in sort_list:
    for i in range(sort_len - 1):
        if sort_list[i] > sort_list[i + 1]:
            sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]

# print(sort_list)
for i in range(sort_len):
    minimum = i
    for j in range(i + 1, sort_len):
        if sort_list[j] < sort_list[minimum]:
            minimum = j
    sort_list[i], sort_list[minimum] = sort_list[minimum], sort_list[i]


# print(sort_list)


def quick_sort(seq):
    if len(seq) < 2:
        return seq
    mid = random.choice(seq)
    less = [x for x in seq if x < mid]
    more = [x for x in seq if x > mid]
    e_num = [mid] * seq.count(mid)
    return quick_sort(less) + e_num + quick_sort(more)


# print(quick_sort(sort_list))


# def my_sum(*args):
#     txt = ['чисел', 'квадратов', 'кубов']
#
#     def calc(n):
#         s = 0
#         for m in range(len(args)):
#             s += args[m] ** n
#         return s
#
#     for k in range(len(txt)):
#         print('Сумма', txt[k] + ':', calc(k + 1))


# my_sum(1, 3, 5, 7)

# num = 10
# print('Нечетные числа')
# l = lambda n: n * 2 + 1
# for k in range(num):
#     print(l(k), end=' ')
# print('\nСтепени двойки')
# l = lambda n: 2 ** n
# for k in range(num):
#     print(l(k), end=' ')
#
# print('\nКвадраты чисел')
# for k in range(num):
#     print((lambda x: x * x)(k + 1), end=' ')
#
#
# def calc(x, y):
#     return x + y


# F = lambda x, y: calc(x, y)
# f = calc
# calc = lambda x, y: x * y
#
# print('\nВызов F(3, 5):', F(3, 5))
# print('\nВызов f(3, 5):', f(3, 5))
# print('\nВызов calc(3, 5):', calc(3, 5))
#
# s = 'abcdef'
# g = list(map(lambda x: x + x, s))
# print(g)
#
#
# def display(func, a, b):
#     for k in range(a, b + 1):
#         print('{0:4}'.format(func(k)), end='')
#
# display(lambda x: x, 1, 5)

# def display(f, a, b):
#     for k in range(a, b + 1):
#         print('{0:4}'.format(f(k)), end=' ')
#     print()
#
#
# def mypow(n):
#     return lambda x: x ** n
#
#
# def apply(f, h):
#     def calc(x):
#         return f(h(x))
#
#     return calc
#
#
# A = mypow(2)
# B = mypow(3)
# C = apply(lambda x: 2 * x + 1, lambda x: 2 * x)
# print('x  ', end='')
# display(lambda x: x, 1, 5)
# print('A(x)', end='')
# display(A, 1, 5)
# print('B(x)', end='')
# display(B, 1, 5)
# print('C(x)', end='')
# display(C, 1, 5)
# F = lambda f: lambda x: f(f(x))
# print('F(x->x * x) (5): ', F(lambda x: x * 5) (5))
#
# print(F(lambda x: 2 * x + 1) (5))
def my_sum(n):
    if n == 0:
        return 0
    else:
        return n + my_sum(n - 1)


def fib(n):
    if n <= 2:
        # if n == 1 or n ==2:
        return 1
    # else:
    return fib(n - 1) + fib(n - 2)


def show(txt):
    if len(txt) == 0:
        print('|')
    else:
        print('|', txt[-1], end='', sep='')
        show(txt[:-1])


# li = [1, 3, 5, 7, 11, 23, 34, 56, 78, 122]

# def bin_search(array, value):
#     left = 0
#     right = len(array) - 1
#     idx = len(array) // 2
#     while array[idx] != value and left <= right:
#         if value > array[idx]:
#             left = idx + 1
#         else:
#             right = idx - 1
#         idx = (left + right) // 2
#     return -1 if left > right else f'Элемент найден на позиции {idx}'


def my_sum(n):
    if n == 0:
        return n
    return n + my_sum(n - 1)


# print(my_sum(5))


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


for i in range(12):
    print(my_sum(i), end=' ')
print()
for j in range(15):
    print(fib(j + 1), end=' ')
print()


def show(txt):
    if len(txt) == 0:
        print('|')
    else:
        print("|", txt[-1], end='', sep='')
        show(txt[:-1])


show('hello')
show([1, 2, 3, 4, 5])
#
# import cProfile
#
# cProfile.run('fib(2)')

#n - размерность матрицы n x n
#mat - результирующая матрица
#st - текущее значение-счетчик для записи в матрицу
#m - коеффициент, используемый для заполнения верхней
#матрицы последующих витков, т.к. одномерные матрицы
#следующих витков имеют меньше значений

# n = int(input("Enter n: "))
# mat = [[0] * n for i in range(n)]
# st, m = 1, 0
# # Заранее присваиваю значение центральному элементу
# # матрицы
# mat[n // 2][n // 2] = n * n
# for v in range(n // 2):
#     # Заполнение верхней горизонтальной матрицы
#     for i in range(n - m):
#         mat[v][i + v] = st
#         st += 1
#         # i+=1
#     # Заполнение правой вертикальной матрицы
#     for i in range(v + 1, n - v):
#         mat[i][-v - 1] = st
#         st += 1
#         # i+=1
#     # Заполнение нижней горизонтальной матрицы
#     for i in range(v + 1, n - v):
#         mat[-v - 1][-i - 1] = st
#         st += 1
#         # i+=1
#     # Заполнение левой вертикальной матрицы
#     for i in range(v + 1, n - (v + 1)):
#         mat[-i - 1][v] = st
#         st += 1
#         # i+=1
#     # v+=1
#     m += 2
# # Вывод результата на экран
# for i in mat:
#     print(*i)
# text = 'Как важно знать в начале\nмножество вещей\nОднако же потом\nУзнаем еще больше'
# f = open('test.txt', 'w', encoding='utf-8')
# f.write(text)
# f.close()

# f = open('test.txt', 'r', encoding='utf-8')
# obj = f.readline()
# print(obj)
# k = 1
# while obj != '':
#     print(f'{k}) ', end='')
#     for symb in obj:
#         if symb == ' ':
#             symb = '_'
#         print(symb, end='')
#     k += 1
#     obj = f.readline()
# for line in obj:
#     print(f'[{k}]', line)
#     k += 1
# f.close()

matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for raw in matr:
    print()
    for col in raw:
        print(col, end=' ')

print()
print('*' * 20)

for i in matr:
    print(*i)