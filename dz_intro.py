# ДЗ к семинару № 3
# Пузырьковая сортировка


li = [9, 1, 8, 3, 2, 6]

for _ in li:
    for j in range(len(li) - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

# print(li)

# i = 0
# while i <= len(li):
#     j = 0
#     while j < len(li) - 1:
#         if li[j] > li[j + 1]:
#             li[j], li[j + 1] = li[j + 1], li[j]
#         j += 1
#     i += 1
# print(li)

# Сортировка выбором
li = [77, 5, 9, 2, 1, 8, 4]
for i in range(len(li) - 1):
    minimum = i
    for j in range(i + 1, len(li)):
        if li[j] < li[minimum]:
            minimum = j
    li[i], li[minimum] = li[minimum], li[i]

# print(li)


# Разворот массива
i = 0
j = len(li) - 1
while i < len(li) // 2:
    li[i], li[j] = li[j], li[i]
    i += 1
    j -= 1
# print(li)


# Сумма между макс и мин значениями массива
arr = [4, 1, 6, 5, 8, 3, 9, 2, 5, 16, 7]
min_idx = 0
max_idx = 0
SIZE = len(arr)
for i in range(1, SIZE):
    if arr[i] < arr[min_idx]:
        min_idx = i
    elif arr[i] > arr[max_idx]:
        max_idx = i

# print(min_idx, max_idx)
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
summ = 0
for i in range(min_idx + 1, max_idx):
    summ += arr[i]
# print(summ)

first = arr[0]
second = arr[1]
for i in range(2, len(arr)):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second:
        second = arr[i]

# print(first, second)


def my_fact(n):
    if n <= 1:
        return 1
    return n * my_fact(n - 1)


# print(my_fact(5))
#
# print(int('1101101', base=2))
#
# d = {'a': 2}
# print(d['a'])
# print(d.get('a'))
# print(d.keys())
# print(d.values())

# a = {4, 5, 6, 7, 8}
# b = {5, 6, 7, 8}
# c = {3, 4, 5, 6, 7, 8}
# print(a | b)
# print(a & b)
# print(a.difference(b))
# print(b | c)
# print(b.intersection(c))
# print(b.difference(c))
# print(a.union(c))
# print(a.intersection(c))
# print(a.difference(c))

arr = [1, 3, 4, 5, 7, 8, 11, 15, 22]


def bin_search(array, value):
    left = 0
    right = len(array) - 1
    middle = len(array) // 2
    while array[middle] != value and left < right:
        if array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right) // 2
    return -1 if left > right else middle

# print(bin_search(arr, 22))


# n = 2
# m = 9

# spam = m // 2
# eggs = m % 2
# result = 1
# temp = 1
# while spam > 0:
#     temp = n ** 2
#     result *= temp
#     spam -= 1

# print(result * n if eggs != 0 else result)


def exponent(n, m):
    spam = m // 2
    rmd = m % 2
    result = 1
    while spam > 0:
        temp = n ** 2
        result *= temp
        spam -= 1
        print(spam)
    return result * n if rmd != 0 else result


print(exponent(3, 5))


