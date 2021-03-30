# Пример неудачного кода
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'hair_color': 'Green',
    'eyes_color': 'Brown',
    'weight': 95.4
}

person2 = {
    'first_name': 'Arthur',
    'last_name': 'Doe',
    'age': 45,
    'hair_color': 'Green',
    'eyes_color': 'Brown',
    'weight': 75.4
}


def get_full_name(person: dict):
    return person['first_name'], person['last_name']


def show_info(person: dict):
    print('Person:', get_full_name(person))


def show_all_persons_info(persons: list):
    for x in persons:
        show_info(x)

show_info(person1)
show_info(person2)

person_list = [person1, person2]
show_all_persons_info(person_list)
# print('Person:', person1['first_name'], person1['last_name'])

# Создание класса


class Human:
    first_name: str
    last_name: str     # = 'Undefined' - если значение не определено
    hair_color: str
    eyes_color: str
    age: int
    weigth: float


person1 = Human()  # конструктор объекта
person2 = Human()

person1.last_name = 'Doe'
person1.age = 30
person1.weigth = 40.5
# person1.lasts_name = 'Doe (Error)'

print(person1)
print(f'{person1.last_name}')
# print(person2.last_name)

#--------------------------------
# Работа с get/set, encapsulation


class Human:
    first_name: str = 'John'
    last_name: str = 'Doe'
    hair_color: str
    eyes_color: str
    __age: int = 200  # private
    weigth: float

    @property   # декоратор, (getter) --> fullname() --> fullname
    def fulname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self.__age

    @ age.setter
    def age(self, value):
        if 0 < value < 120:
            self.__age = value
        else:
            print('Invalid age value')



    # def set_age(self, new_age):     # setter, задает значение
    #     if new_age > 0:
    #         self.__age = new_age
    #     else:
    #         print('Invalid age value')
    #     return self.__age

person1 = Human()
# print(person1.fulname)
person1.age = -100
print(person1.age)
person1.age = 100
# print(person1.set_age(200))
print(person1.age)
# print(person1.__age) --> ошибка
# print(person1._Human__age) --> работает (обращение через класс)

#--------------------------------------------------
# Создание методов


class Human:
    first_name: str = 'John'
    last_name: str = 'Doe'
    hair_color: str
    eyes_color: str
    __age: int = 200  # private
    weigth: float

    @property   # декоратор, (getter) --> fullname() --> fullname
    def fulname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self.__age

    @ age.setter
    def age(self, value):
        if 0 < value < 120:
            self.__age = value
        else:
            print('Invalid age value')

    def walk(self, steps: int) -> None:
        for x in range(steps):
            print(f'Person {self.first_name} walking ...{x}...')

    def sleep(self, seconds: int) -> None:
        pass

    def say(self, message: str) -> None:
        print(f'{self.first_name}: {message}')


person1 = Human()
person2 = Human()
person1.walk(10)
person2.walk(5)
person2.say('Hello, world!')

# -------------------------------------
# Наследование


class Animal:
    name: str

    def __init__(self, animal_name: str):
        self.name = animal_name

    def move(self):
        pass


class Bird(Animal):
    def fly(self):
        pass

    def move(self):
        self.fly()


class Cat(Animal):
    def walk(self):
        pass

    def __init__(self):
        super().__init__('Cat')
        # self.name = 'Cat'

    def move(self):
        self.walk()

cat = Cat()
birdy = Cat()
print(cat.name)
# Полиморфизм
cat.move()
birdy.move()
cat.walk()
