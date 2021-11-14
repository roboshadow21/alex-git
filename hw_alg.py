import timeit
import cProfile
import functools
import sys
import ctypes
import struct
import collections
import random
from binarytree import tree, bst, Node, build

# Сумму между макс и мин значениями массива
arr = [9, 8, 6, 5, 1, 3, 5, 2, 4]
min_idx = 0
max_idx = 0
SIZE = len(arr)
for i in range(1, SIZE):
    if arr[i] < arr[min_idx]:
        min_idx = i
    elif arr[i] > arr[max_idx]:
        max_idx = i

print(min_idx, max_idx)
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
summ = 0
for i in range(min_idx + 1, max_idx):
    summ += arr[i]
# print(summ)

# ДЗ к уроку эмпирическая оценка алгоритмов
# python -m timeit -n 1000 -s "import hw_alg" "hw_alg.div()"
# Вариант 1


# @functools.lru_cache()
# def div(n):
#     a = [0] * 8
#     for i in range(2, n):
#         for j in range(2, 10):
#             if i % j == 0:
#                 a[j - 2] += 1
#     return a


# n = 8, range = 100 - 1000 loops, best of 5: 68 usec per loop
# С декоратором:
# n = 8, range = 100 - 1000 loops, best of 5: 88.4 nsec per loop

# n = 8, range = 500 - 1000 loops, best of 5: 351 usec per loop
# С декоратором:
# n = 8, range = 500 - 1000 loops, best of 5: 89.6 nsec per loop

# n = 8, range = 1000 - 1000 loops, best of 5: 716 usec per loop
# С декоратором:
# n = 8, range = 1000 - 1000 loops, best of 5: 86.1 nsec per loop

# cProfile.run('div(1000)')

# Вариант 2


# @functools.lru_cache()
# def div1(n):
#     k = 2
#     lst = []
#     while k < 10:
#         num = [i for i in range(2, n) if i % k == 0]
#         lst.append(len(num))
#         k += 1
#     return lst


# range 100 - 1000 loops, best of 5: 40.7 usec per loop
# С декоратором:
# range 100 - 1000 loops, best of 5: 88.4 nsec per loop

# range 500 -1000 loops, best of 5: 211 usec per loop
# С декоратором:
# range 500 -1000 loops, best of 5: 107 nsec per loop

# range 1000 -1000 loops, best of 5: 437 usec per loop
# С декоратором:
# range 1000 -1000 loops, best of 5: 89.6 nsec per loop

# cProfile.run('div1(1000)')


# @functools.lru_cache()
# def div2(n):
#     lst = []
#     a = len([i for i in range(2, n) if i % 2 == 0])
#     lst.append(a)
#     b = len([i for i in range(2, n) if i % 3 == 0])
#     lst.append(b)
#     c = len([i for i in range(2, n) if i % 4 == 0])
#     lst.append(c)
#     d = len([i for i in range(2, n) if i % 5 == 0])
#     lst.append(d)
#     e = len([i for i in range(2, n) if i % 6 == 0])
#     lst.append(e)
#     f = len([i for i in range(2, n) if i % 7 == 0])
#     lst.append(f)
#     g = len([i for i in range(2, n) if i % 8 == 0])
#     lst.append(g)
#     h = len([i for i in range(2, n) if i % 9 == 0])
#     lst.append(h)
#     return lst


# range 100 - 1000 loops, best of 5: 38.6 usec per loop
# С декоратором:
# range 100 - 1000 loops, best of 5: 80.9 nsec per loop

# range 500 - 1000 loops, best of 5: 203 usec per loop
# С декоратором:
# range 500 - 1000 loops, best of 5: 80.9 nsec per loop

# range 1000 - 1000 loops, best of 5: 429 usec per loop
# С декоратором:
# range 1000 - 1000 loops, best of 5: 79.3 nsec per loop


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
#             # print(j, end=' ')
#         # print()
# result = [i for i in sieve if i != 0]
# print(result)


# @functools.lru_cache()
# def primary_num(n):
#     num = n + 1
#     while True:
#         if num != 2 and num % 2 == 0:
#             num += 1
#             continue
#         elif num != 3 and num % 3 == 0:
#             num += 1
#             continue
#         elif num != 5 and num % 5 == 0:
#             num += 1
#             continue
#         elif num != 7 and num % 7 == 0:
#             num += 1
#             continue
#         else:
#             return num

# print(primary_num(43))

# primary_num(1000) - 1000 loops, best of 5: 659 nsec per loop
# primary_num(1000) - 1000 loops, best of 5: 114 nsec per loop
# primary_num(10000) - 1000 loops, best of 5: 348 nsec per loop
# primary_num(10000) - 10000 loops, best of 5: 101 nsec per loop
# primary_num(1000000) - 10000 loops, best of 5: 332 nsec per loop
# primary_num(1000000) - 10000 loops, best of 5: 84.5 nsec per loop

# cProfile.run('primary_num(100000)')


# @functools.lru_cache()
# def sieve2(num):
#     n = num + 10
#     sieve = [i for i in range(n)]
#     sieve[1] = 0
#     for i in range(2, n):
#         if sieve[i] != 0:
#             j = i * 2
#             while j < n:
#                 sieve[j] = 0
#                 j += i
#     result = [i for i in sieve if i != 0]
#     for i in result:
#         if i > num:
#             return i

# print(sieve2(23))

# sieve2(1000) - 1000 loops, best of 5: 275 usec per loop
# sieve2(1000) - 1000 loops, best of 5: 80.1 nsec per loop
# sieve2(10000) - 1000 loops, best of 5: 2.89 msec per loop
# sieve2(10000) - 1000 loops, best of 5: 94.7 nsec per loop
# sieve2(100000) - 1000 loops, best of 5: 34.8 msec per loop
# sieve2(100000) - 1000 loops, best of 5: 171 nsec per loop

# cProfile.run('sieve2(1000)')

from collections import namedtuple, deque
# nums = int(input('Enter nums of enterprises: '))
# Enterprise = namedtuple('Enterprise', 'name, profit')
# li = []
# x = []
# for _ in range(nums):
#     info = input('Enter name, profit: ').split()
#     result = Enterprise._make(info)
#     x.append(int(result.profit))
#     li.append(result)
# print(li)
# average = sum(x) / 4
# print(average)
# lst = []
# lst1 = []
# for i in range(len(li)):
#     if int(li[i][1]) < average:
#         lst.append(li[i])
#     else:
#         lst1.append(li[i])
# print(f'More averege {lst1}\nLess average {lst}')

# x = deque()
# y = deque()
# x1 = deque()
# y1 = deque()
# num = input('Enter num: ')
# num1 = input('Enter num: ')
# nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
#         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
#         }
# for el in num:
#     if el in nums.keys():
#         x.appendleft(nums[el])
#     else:
#         x.appendleft(int(el))
# print(x)
# for el in num1:
#     if el in nums.keys():
#         x1.appendleft(nums[el])
#     else:
#         x1.appendleft(int(el))
# print(x1)
#
# summa = 0
# for el in x:
#     temp = el * (16 ** x.index(el))
#     summa += temp
# print(summa)
# y.append(summa)
# summa1 = 0
# for el in x1:
#     temp = el * (16 ** x1.index(el))
#     summa1 += temp
# print(summa1)
# y.append(summa1)
# res = sum(y)
# print(res)
#
# while res > 16:
#     temp = res % 16
#     if temp in nums.keys():
#         y1.appendleft(nums[temp])
#     else:
#         y1.appendleft(temp)
#     res //= 16
#     if res in nums.keys():
#         y1.appendleft(nums[res])
# print(y1)

# Работа с памятью


def func(a, b):
    if a == b:
        return f'{a}'
    elif a < b:
        return f'{a} {func(a + 1, b)}'

# print(func(1, 10))
# f = func(1, 10)
# print(id(f))
# size = sys.getsizeof(f)
# print(size)
# st = ctypes.string_at(id(f), size)
# print(st)
# print(struct.unpack('LLLLLLLLLLLLLLLLLc', st))

# t = (1, 2, 3)
# print(id(t))
#
# size = sys.getsizeof(t)
# print(size)
# st = ctypes.string_at(id(t), size)
# print(st)
# print(struct.unpack('LLLLLLLLLLLLLLLl', st))
# print(id(type(int)))

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 2500}
# print(id(d))
# size = sys.getsizeof(d)
# print(size)
# st = ctypes.string_at(id(d), size)
# print(st)
# print(struct.unpack('L' * 57 + 'l', st))

# ДЗ Сортировка


array = [random.randint(-100, 100) for _ in range(20)]
# print(array)
for _ in array:
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

# print(array)
# import math
#
# li = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
# print(sum(li))
# print(math.ceil(sum(li) / len(li)))

# ДЗ Графы
# N 1

def handshake(n):
    g = [[x * 1 for x in range(n)] for x in range(n)]
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] = 1 if i != j else 0
    print(*g, sep='\n')
    count = 0
    for el in g:
        for vertex in range(len(el)):
            if vertex != 0:
                count += 1
    return count


# print(handshake(3))

# N 2

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
    vertex_list = []
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                vertex_list.append(i)
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    print(parent)
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, vertex_list


# s = int(input('От какой вершины идти: '))
# print(dijkstra(g1, s))

# N 3
# N = 6
# g = [[x * 1 for x in range(N)] for x in range(N)]
# for i in range(len(g)):
#     for j in range(len(g[i])):
#         g[i][j] = 1 if i != j else 0
# print(*g, sep='\n')


def dfs(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    def _dfs(vertex):
        is_visited[vertex] = True
        path.append(vertex)
        for item in graph[vertex]:
            if not is_visited[item]:
                parent[item] = vertex
                _dfs(item)
                path.append(vertex)
        else:
            path.append(-vertex)
    _dfs(start)

    return parent, path

# print(dfs(g, 2))


import hashlib

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

# Подсчет количества подстрок в сроке
s = 'hello world!'
h_s = hashlib.sha1(s.encode('utf-8')).hexdigest()
h_s1 = hashlib.sha1(s[0].encode('utf-8')).hexdigest()
# print(h_s)
# print(h_s1)


def find_substring(s: str):
    assert len(s) > 0, 'Строка не может быть пустой!'
    symb = ''
    li = []
    idx = 0
    while idx < len(s):
        for i in range(len(s) - idx):
            symb += s[i + idx]
            space = ' '
            h_symb = hashlib.sha1(symb.encode('utf-8')).hexdigest()
            h_space = hashlib.sha1(space.encode('utf-8')).hexdigest()
            if h_symb == hashlib.sha1(s.encode('utf-8')).hexdigest() or h_symb == h_space or h_symb in li:
                continue
            else:
                li.append(symb)
            # print(symb)
        idx += 1
        symb = ''
    # print(li)
    return f'Количество подстрок в сроке: {len(set(li))}'


# print(find_substring(s))

# Закодировать любую строку по методу Хаффмана
# Бинарный поиск. Алгоритм Хаффмана

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


if __name__ == '__main__':
    my_str = input('Введите строку для кодирования: ')
    haf = Haffman()
    code_s = haf.encode(my_str)
    print(haf.get_real_string_code())
    print(code_s)
    table = haf.get_table_code()
    print(table)
    real_1 = haf.decode(code_s, table)
    real_2 = haf.decode(code_s)
    print(real_1)
    print(real_2)

# def search(bin_search_tree, number, path=''):
#     if bin_search_tree.value == number:
#         return f'Число {number} обнаружено по следующему пути:\nКорень{path}'
#     if number < bin_search_tree.value and bin_search_tree.left is not None:
#         return search(bin_search_tree.left, number, path=f'{path}\nШаг влево')
#     if number > bin_search_tree.value and bin_search_tree.right is not None:
#         return search(bin_search_tree.right, number, path=f'{path}\nШаг вправо')
#     return f'Число {number} отсутствует в дереве'


# bt = bst(height=4, is_perfect=True)
# print(bt)
# print(bt.value)
# num = int(input('Введите число для поиска:'))
# print(search(bt, num))


class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#     @property
#     def my_print(self):
#         return 2 + 98
# c = MyNode(111)
# print(c.my_print)

bt = bst(height=3, is_perfect=False)
# print(bt)
# print(bt.left.value)
# print(bt.right.right.value)
s = 'abc'
li = []
for el in s:
    li.append(ord(el))
# print(li)


def encode_string(bst, li):
    bst = Node(36)
    for i in range(len(li)):
        if li[i] > bst.value:
            bst.right = Node(int(li[i]))
        return encode_string(bst.right, li)

# print(encode_string(bt, li))

# bt = Node(44)
# bt.right = Node(97)
# print(bt)
# bt.right.right = Node(98)
# print(bt)
# bt.left = Node(36)
# bt.left.left = Node(39)
# print(bt)

# new = build(li)
# print(new)
# print(new.value)
# new.right.right = Node(117)
# print(new)

