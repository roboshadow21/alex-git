# Интерфейсы - встроенные методы
class Human:
    first_name: str
    last_name: str

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __str__(self):                  # Для строк
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):                # Для списков и других вложенных структур
        return "Human: " + self.__str__()


a = Human('John', 'Doe')
b = Human('Arthur', 'Doe')
humans = [a, b]
# b = float(10.5)
# print(a)
print(humans)

# Вычисляемые интерфейсы


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """ Оператор плюса """
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        """ Оператор минуса """
        return Point(
            self.x - other.x,
            self.y - other.y
        )

    def __truediv__(self, other):
        """ Оператор деления """
        return Point(
            self.x / other.x,
            self.y / other.y
        )

A = Point(3, 5)
B = Point(10, -4)
C = A + B
print(C)



