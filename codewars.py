# import math
#
#
# class PaginationHelper:
#
#     def __init__(self, arr, num):
#         self.arr = arr
#         self.num = num
#
#     def __str__(self):
#         return f'{self.arr}, {self.num}'
#
#     def page_count(self):
#         return math.ceil(len(self.arr) / self.num)
#
#     def item_count(self):
#         return len(self.arr)
#
#     def page_item_count(self, index):
#         page_nums = list(range(self.page_count()))
#         if index not in page_nums:
#             return -1
#         elif index == page_nums[-1]:
#             return self.num if len(self.arr) % self.num == 0 else len(self.arr) % self.num
#         else:
#             return self.num
#
#     def page_index(self, n):
#         if n not in range(len(self.arr)):
#             return -1
#         else:
#             k = 0
#             i = 0
#             page = 0
#             while k < len(self.arr[:n]):
#                 if i == self.num:
#                     page += 1
#                     i = 0
#                 i += 1
#                 k += 1
#         return page
#
#
# helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
# print(helper)
# print(helper.page_count())
# print(helper.item_count())
# print(helper.page_item_count(0))
# print(helper.page_index(5))
# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
#
#     def __str__(self):
#         return f'{self.left} {self.right} {self.value}'
# x = tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5),
#                    Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])


# tree = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5),
#                                                      Node(None, None, 6), 3), 1)
# print(tree)
# print(tree.right)
# print(tree.value)
# y = []
# y.append(tree.value)
# print(y)

# MORSE_CODE['.--']
# MORSE_CODE = {'....': 'H', '.': 'E', '-.--': 'Y', '.---': 'J', '..-': 'U', '-..': 'D', '..': 'I', '--': 'M'}
# 'HEY JUDE'
# s = '.... . -.--   .--- ..- -.. .'


# def decodeMorse(morse_code):
#     s1 = ''
#     s2 = morse_code.replace('   ', ' A ').strip()
#     for el in s2.split():
#         if el == 'A':
#             s1 += ' '
#         elif el in MORSE_CODE.keys():
#             s1 += MORSE_CODE[el]
#     return s1.strip()
#
# print(decodeMorse(s))
# bits = 1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
# bits = 11001100110011000000110000001111110011001111110011111100000000000000
# bits = 11101110101
# bits = 11111100111111
# bits = 1010001110111


# def decode_bits(bits):
#     s = str(bits)
#     if s.count('1') == 6 and s.count('0') == 1:
#         return '--'
#     elif s.count('1') == 12 and s.count('0') == 2:
#         return '--'
#     else:
#         test = s.split('0')
#         li = []
#         unit = 0
#         for el in test:
#             if el != '':
#                 li.append(len(el))
#                 unit = min(set(li))
#         s1 = s.replace('0' * (unit * 7), '   ').replace('0' * (unit * 3), ' ').replace('1' * (unit * 3), '-').replace(
#             '1' * unit, '.').replace('0' * unit, '').replace('0', '')
#         # print(s1)
#         return s1
#
# morseCode = decode_bits(bits)


# def decode_morse(morseCode):
#     s1 = ''
#     s2 = morseCode.replace('   ', ' A ').strip()
#     for el in s2.split():
#         if el == 'A':
#             s1 += ' '
#         elif el in MORSE_CODE.keys():
#             s1 += MORSE_CODE[el]
#     return s1.strip()

# print(decode_morse(morseCode))


# s2 = '00111100'
# s2 = s2.strip('0')
# print(s2)

# Sudoku

# puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#           [6, 0, 0, 1, 9, 5, 0, 0, 0],
#           [0, 9, 8, 0, 0, 0, 0, 6, 0],
#           [8, 0, 0, 0, 6, 0, 0, 0, 3],
#           [4, 0, 0, 8, 0, 3, 0, 0, 1],
#           [7, 0, 0, 0, 2, 0, 0, 0, 6],
#           [0, 6, 0, 0, 0, 0, 2, 8, 0],
#           [0, 0, 0, 4, 1, 9, 0, 0, 5],
#           [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# print(puzzle[0])
# print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# sample = list(range(1, 10))
# puzzle[0][2] = 9
# print(puzzle[0])

# for i, raw in enumerate(puzzle, start=1):
#     for j, el in enumerate(raw, start=1):
#         print(f'{j} : {el:<4}', end='')
#     print()
# for i in sample:
#     for j in range(len(puzzle[0])):
#         if i not in puzzle[0] and puzzle[0][j] == 0:
#             puzzle[0][j] = i
#
# print(puzzle[0])

# Sum of intervals
# l = [(1, 4), (7, 10), (3, 5)]
# l = [(1, 2), (6, 10), (11, 15)]
# l = [(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)]
# l = [(1, 5)]
# l = [(1, 5), (6, 10)]
# l = [(1, 5), (1, 5)]

# def sum_of_intervals(intervals):
#     lst = []
#     for el in intervals:
#         for j in range(len(el) - 1):
#             temp = list(range(el[j], el[j+1]))
#             lst.append(temp)
#     lst2 = []
#     for el in lst:
#         for j in el:
#             lst2.append(j)
#     return len(list(set(lst2)))
#
#
# print(sum_of_intervals(l))


# Validate Sudoku with size `NxN`

# matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
#           [2, 3, 1, 5, 6, 4, 8, 9, 7],
#           [3, 1, 2, 6, 4, 5, 9, 7, 8],
#           [4, 5, 6, 7, 8, 9, 1, 2, 3],
#           [5, 6, 4, 8, 9, 7, 2, 3, 1],
#           [6, 4, 5, 9, 7, 8, 3, 1, 2],
#           [7, 8, 9, 1, 2, 3, 4, 5, 6],
#           [8, 9, 7, 2, 3, 1, 5, 6, 4],
#           [9, 7, 8, 3, 1, 2, 6, 4, 5]]
# print(sum(matrix[0][:3]) == sum(matrix[1][0:3]))
# matrix = [
#   [7,8,4,  1,5,9,  3,2,6],
#   [5,3,9,  6,7,2,  8,4,1],
#   [6,1,2,  4,3,8,  7,5,9],
#
#   [9,2,8,  7,1,5,  4,6,3],
#   [3,5,7,  8,4,6,  1,9,2],
#   [4,6,1,  9,2,3,  5,8,7],

#   [8,7,6,  3,9,4,  2,1,5],
#   [2,4,3,  5,6,1,  9,7,8],
#   [1,9,5,  2,8,7,  6,3,4]
# ]

# matrix = [
#     [1, 4, 2, 3],
#     [3, 2, 4, 1],
#     [4, 1, 3, 2],
#     [2, 3, 1, 4]
# ]


# class Sudoku(object):
#
#     def __init__(self, data):
#         self.data = data
#
#     def is_valid(self):
#         if self.data[0][0] is True or sum(self.data[0][0:3]) == sum(self.data[1][0:3]):
#             return False
#         k = 0
#         lst = []
#         try:
#             while k <= len(self.data) - 1:
#                 for i in range(len(self.data)):
#                     if sum(self.data[i]) != sum(range(1, len(self.data) + 1)) or len(self.data[i]) != len(
#                             set(self.data[i])):
#                         return False
#                     lst.append(self.data[i][k])
#                 if sum(lst) != sum(range(1, len(self.data) + 1)) or len(lst) != len(set(lst)):
#                     return False
#                 else:
#                     lst = []
#                     k += 1
#         except TypeError:
#             return False
#         return True

# sudoku = Sudoku(matrix)
# print(sudoku.is_valid())

# Roman Numerals Helper
# def from_roman(roman_num):
#     roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     li = [roman_nums.get(x) for x in roman_num]
#     print(li)
#     for i in range(len(li) - 1):
#         if li[i] < li[i + 1]:
#             li[i], li[i + 1] = 0, abs(li[i] - li[i + 1])
#     print(li)
#     # print(sum(li))
#     return sum(li)
#
#
# def to_roman(val):
#     a = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
#     b = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
#     c = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
#     d = {1: 'M', 2: 'MM', 3: 'MMM'}
#     # val = 1
#     s = ''
#     lst = [el for el in str(val)]
#     print(lst)
#     if len(lst) == 1:
#         s += a.get(int(val))
#         return s
#     elif len(lst) == 2:
#         s += b.get(int(lst[0]))
#         s += a.get(int(lst[1]))
#         return s
#     elif len(lst) == 3:
#         s += c.get(int(lst[0]))
#         s += b.get(int(lst[1]))
#         s += a.get(int(lst[2]))
#         return s
#     elif len(lst) == 4:
#         s += d.get(int(lst[0]))
#         s += c.get(int(lst[1]))
#         s += b.get(int(lst[2]))
#         s += a.get(int(lst[3]))
#         return s

# print(from_roman('MCMXC'))
# print(to_roman(1990))

# Mix string

# s1 = "A aaaa bb cfff cc"
# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# s1 = "Are the kids at home? aaaaa fffff"
# s2 = "Yes they are here! aaaaa fffff"
# s1 = "Are they here"
# s2 = "yes, they are here"
# s1 = "Sadus:cpms>orqn3zecwGvnznSgacs"
# s2 = "MynwdKizfd$lvse+gnbaGydxyXzayp"
import random

# s1 = "looping is fun but dangerous"
# s2 = "less dangerous than coding"
# s1 = "codewars"
# s2 = "codewars"


def mix(s1, s2):
    li1 = [el for el in s1 if s1.count(el) > 1 if el.islower()]
    li2 = [el for el in s2 if s2.count(el) > 1 if el.islower()]
    li1.extend(li2)
    result = sorted(list(set(li1)))
    lst1 = ['1:' + (el * s1.count(el)) + '/' for el in result if s1.count(el) > s2.count(el)]
    lst2 = ['2:' + (el * s2.count(el)) + '/' for el in result if s2.count(el) > s1.count(el)]
    lst_eq = ['=:' + (el * s1.count(el)) + '/' for el in result if el in s1 and el in s2 and s1.count(el) == s2.count(el)]
    lst1.extend(lst2)
    lst1.extend(lst_eq)
    return ''.join(sorted(lst1, key=lambda x: len(x[2:-1]), reverse=True)).rstrip('/')


# print(mix(s1, s2))

# sample = "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
# sample = "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
# sample = "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
# sample = "2:eeeee/2:yy/=:hh/=:rr"
# sample = '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
# sample = "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

# Calculator
from collections import deque
# class Calculator(object):
#     plus = '+'
#     minus = '-'
#
#     def evaluate(self, string):
#         lst = string.split()
#         print(lst)
#
#     def my_list(self, s: str):
#         pass
# import re
# s = Calculator()
# s.evaluate("1 + 1")
# print(s.my_list('1 + 1'))
# s = '( 1 + 1 )'
# s = '( 4 + 2 + 1 )'
# s = "3 * ( 4 + 7 ) - 6"
# s = "2 / 2 + 3 * 4 - 6"
# s = '4 / 2 + 4 * 4 + 2'
# s = '3 * 4 - 2'
# s = '4 * ( 8 + 3 )'
s = "( ( ( ( 1 ) * 2 ) ) )"
# s = "( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"
# s = "2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"
# print(s[s.index(')') - 4])
# for el in s:
#     if el == ')':
#         s = s.replace(')', s[s.index(el) - 10:s.index(el) - 9] + ' ' + s[s.index(el) - 12:s.index(el) - 11])
#         s = s.replace('(', ' ')
# print(s[s.index(')') - 4])
for el in s:
    if el == ')' and s[s.index(')') - 4] != '*' and s[s.index(')') - 6].isdigit():
        s = s.replace(')', s[2:3] + ' ' + s[0:1])
        s = s.replace('(', ' ')
    # elif s.index(el) == 10:
    #     print(el)
    #     s = s.replace(el, ' ')

    else:
        s = s.replace('(', ' ')
        # s = s.replace(')', ' ')

# print(s)
# li = s.split()
# print(li)

# for el in li:
#     if el == '/':
#         res = int(li[li.index(el) - 1]) // int(li[li.index(el) + 1])
#         li = li[:li.index(el) - 1] + [str(res)] + li[li.index(el) + 2:]
# print(li)

# for el in li:
#     if el == '*':
#         #li.remove(')')    # adding
#         res = int(li[li.index(el) - 1]) * int(li[li.index(el) + 1])
#         li = li[:li.index(el) - 1] + [str(res)] + li[li.index(el) + 2:]
# print(li)
#
# for el in li:
#     if el == '+':
#         res = int(li[li.index(el) - 1]) + int(li[li.index(el) + 1])
#         li = li[:li.index(el) - 1] + [str(res)] + li[li.index(el) + 2:]
# print(li)
#
# for el in li:
#     if el == '-':
#         res = int(li[li.index(el) - 1]) - int(li[li.index(el) + 1])
#         li = li[:li.index(el) - 1] + [str(res)] + li[li.index(el) + 2:]
#
# print(int(li[0]) if li[0].isdigit() else int(li[1]))

# Text align justify
size = 7
# s = '123 45 6'
# s = '123 45 6'
# s = '123 56 7 890 45 1 34 56 786 12 19'
s = '1234567 8'
# print(len(s))
li = s.split()
print(li)
# print(len(li))
lst = []
for i in range(len(li)):
    lst.append(li[i])
    lst.append(' ')

lst.pop()
print(lst)
temp = [None] * len(lst)
print(temp)
summ = 0
lst2 = []
for i in range(len(lst)):
    summ += len(lst[i])
    temp[i] = len(lst[i])
    lst2.append(lst[i])
    # if summ == size - 1 or summ % size == 0:
    if summ == size - 1 or summ % size == 0:
        lst2.append('\n')
        summ = 0

# print(summ)
print(temp)
print(lst2)
print(''.join(lst2))







