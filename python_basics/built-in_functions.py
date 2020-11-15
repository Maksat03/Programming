# https://www.programiz.com/python-programming/methods/built-in





#################################################### abs(x) ####################################################
# Возвращает абсолютную величину (модуль числа).
print(abs(-1)) # Выводится 1



input("Continue? (yes/no): ")



############################################### sum(iterable, start) ####################################################
# Функция sum() добавляет элементы повторяемого элемента и возвращает сумму.
# Функция sum() добавляет начало и элементы заданной итерации слева направо.
# Параметры sum ():
# iterable/Итерируемый - итерируемый (список, кортеж, dict и т. д.). Элементы итерируемого должны быть числами.
# start (необязательно) - это значение добавляется к сумме элементов итерируемого. Значение по умолчанию для start равно 0 (если не указано)
# Возвращаемое значение из суммы ():
# sum () возвращает сумму начала и элементов заданной итерации.
numbers = [2.5, 3, 4, -5]
# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum) # 4.5
# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum) # 14.5
# Если вам нужно добавить числа с плавающей точкой с точной точностью, вам следует использовать вместо этого math.fsum (итерируемый).
# Если вам нужно объединить элементы данной итерируемой (элементы должны быть строками), то вы можете использовать метод join (). 'string'.join(sequence)



input("Continue? (yes/no): ")



################################################ round(number, ndigits) ####################################################
# Функция round() возвращает число с плавающей точкой, округленное до указанного числа десятичных дробей.
# Функция round () принимает два параметра:
# number/число - число, которое будет округлено
# ndigits (необязательно) - число, до которого округляется данное число; по умолчанию 0
# Возвращаемое значение от round ():
# Если ndigits не указан, round () возвращает ближайшее целое число к указанному числу.
# Если дано ndigits, round () возвращает число, округленное до цифр ndigits.
# for integers
print(round(10)) # 10
# for floating point
print(round(10.7)) # 11
# even choice
print(round(5.5)) # 6
# Пример 2: округление числа до заданного числа десятичных знаков
print(round(2.665, 2)) # 2.67
print(round(2.675, 2)) # 2.67
# используя decimal.Decimal (передал float как строку для точности)
from decimal import Decimal
num = Decimal('2.675')
print(round(num, 2)) # 2.68



input("Continue? (yes/no): ")



################################################## pow(x, y, z) ####################################################
# Функция pow () возвращает мощность числа.
# Функция pow () принимает три параметра:
# х - число, основание
# у - число, показатель степени
# z (необязательно) - число, используемое для модуля
# Следовательно,
# pow (x, y) равен x**y
# pow (x, y, z) равно (x**y) % z
# positive x, positive y (x**y)
print(pow(2, 2)) # 4
# negative x, positive y
print(pow(-2, 2)) # 4  
# positive x, negative y
print(pow(2, -2)) # 0.25
# negative x, negative y
print(pow(-2, -2)) # 0.25
# Пример 2: pow () с тремя аргументами (x ** y) % z
x = 7
y = 2
z = 5
print(pow(x, y, z)) # OUTPUT:4. Here, 7 powered by 2 equals 49. Then, 49 modulus 5 equals 4.
# Здесь 7, приводимое в действие 2, равно 49. Тогда 49 модуль 5 равен 4.



input("Continue? (yes/no): ")



#################################################### divmod(x, y) ####################################################
# Метод divmod () принимает два числа и возвращает пару чисел (кортеж), состоящую из их частного и остатка.
# divmod () принимает два параметра:
# х - некомплексное число (числитель)
# у - некомплексное число (знаменатель)
# divmod () возвращает:
# (q, r) - пара чисел (кортеж), состоящая из частного q и остатка r
# Если x и y являются целыми числами, возвращаемое значение из divmod () совпадает с (a // b, x% y).
# Если x или y является плавающим числом, результат равен (q, x% y). Здесь q - целая часть частного.
print('divmod(8, 3) = ', divmod(8, 3)) # divmod(8, 3) =  (2, 2)
print('divmod(3, 8) = ', divmod(3, 8)) # divmod(3, 8) =  (0, 3)
print('divmod(5, 5) = ', divmod(5, 5)) # divmod(5, 5) =  (1, 0)
# divmod() with Floats
print('divmod(8.0, 3) = ', divmod(8.0, 3)) # divmod(8.0, 3) =  (2.0, 2.0)
print('divmod(3, 8.0) = ', divmod(3, 8.0)) # divmod(3, 8.0) =  (0.0, 3.0)
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5)) # divmod(7.5, 2.5) =  (3.0, 0.0)
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5)) # divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)



input("Continue? (yes/no): ")



########################################### map(function, iterable, ...) ###########################################
# Функция map() применяет данную функцию к каждому элементу итерируемого (список, кортеж и т. Д.) И возвращает список результатов.
# map() Параметр
# function/Функция - map() передает каждый элемент итерируемой этой функции.
# iterable - итерируемый, который должен быть отображен
# Вы можете передать более одной итерации в функцию map().
# Возвращаемое значение из карты ()
# Функция map () применяет данную функцию к каждому элементу итерируемого и возвращает список результатов.
# Возвращенное значение из map () (объект карты) затем может быть передано в функции, такие как list () (для создания списка), set () (для создания набора) и так далее.
def calculateSquare(n):
    return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result) # <map object at 0x7f722da129e8>
# converting map object to set
numbersSquare = set(result)
print(numbersSquare) # {16, 1, 4, 9}
# В приведенном выше примере каждый элемент кортежа возводится в квадрат.
# Поскольку map () ожидает передачи функции, лямбда-функции обычно используются при работе с функциями map ().
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result) # <map 0x7fafc21ccb00>
# converting map object to set
numbersSquare = set(result)
print(numbersSquare) # {16, 1, 4, 9}
# Нет различий в функциональности этого примера и примера приведенном выше.
# Пример 3: Передача нескольких итераторов в map () с использованием лямбды
# В этом примере добавлены соответствующие элементы двух списков.
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result)) # [9, 11, 13]



input("Continue? (yes/no): ")



#################################################### dict() ####################################################
# Создаёт новый словарь. Объект dict является классом словаря.
print(dict([(1, 10), ("asd", "qwe")])) # {1: 10, "asd": "qwe"}
print(dict(first=10, asd='qwe')) # {'first': 10, 'asd': 'qwe'}
print(dict({'x': 4, 'y': 5}, z=8)) # {'x': 4, 'y': 5, z=8}



input("Continue? (yes/no): ")



################################################ list([iterable]) ####################################################
# Конструктор list () возвращает список в Python.
# Конструктор list () принимает один аргумент:
# iterable (необязательно) - объект, который может быть последовательностью (строка, кортежи) или коллекцией (набор, словарь) или любым объектом итератора
# Конструктор list () возвращает список.
# Если параметры не переданы, возвращается пустой список
# Если в качестве параметра передается итерируемое, создается список, состоящий из элементов итерируемого.
# Пример 1. Создание списков из string, tuple, and list
# empty list
print(list()) # []
# vowel string
vowel_string = 'aeiou'
print(list(vowel_string)) # ['a', 'e', 'i', 'o', 'u']
# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple)) # ['a', 'e', 'i', 'o', 'u']
# vowel list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list)) # ['a', 'e', 'i', 'o', 'u']
# Пример 2. Создание списков из set and dictionary
# vowel set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set)) # ['e', 'u', 'a', 'i', 'o']
# vowel dictionary
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
print(list(vowel_dictionary)) # ['a', 'e', 'i', 'o', 'u']
# Примечание. В случае словарей ключами словаря будут элементы списка. Также порядок элементов будет случайным.
# Пример 3: создание списка из объекта итератора
# объекты этого класса являются итераторами
class PowTwo:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result
pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)
print(list(pow_two_iter)) # [1, 2, 4, 8, 16]



input("Continue? (yes/no): ")



################################################ tuple(iterable) ####################################################
# Встроенный tuple () может быть использован для создания кортежей в Python
# Параметры tuple ()
# iterable/итерация (optional/необязательно) - итерация (list/список, range/диапазон и т. д.) или объект итератора
# Если итерация не передается в tuple (), функция возвращает пустой кортеж.
t = tuple()
print('t =', t) # t = ()

# creating a tuple from a list
t = tuple([1, 4, 6])
print('t =', t) # t = (1, 4, 6)

# creating a tuple from a string
t = tuple('Python')
print('t =',t) # t = ('P', 'y', 't', 'h', 'o', 'n')

# creating a tuple from a dictionary
t = tuple({1: 'one', 2: 'two'})
print('t =',t) # t = (1, 2)



input("Continue? (yes/no): ")



################################################ set(iterable) ####################################################
# Встроенная функция set () создает set/набор в Python
# Параметры set()
# iterable/итерируемый (optional/необязательно) - последовательность (string/строка, tuple/кортеж и т. д.) или коллекция (set/набор, dictionary/словарь и т. д.) или объект итератора для преобразования в набор
# Возвращаемое значение из set ()
# пустой набор, если параметры не переданы
# множество, построенное из заданного итерируемого параметра
# empty set
print(set()) # set()

# from string
print(set('Python')) # {'o', 'y', 'P', 'n', 't', 'h'}

# from tuple
print(set(('a', 'e', 'i', 'o', 'u'))) # {'o', 'e', 'a', 'i', 'u'}

# from list
print(set(['a', 'e', 'i', 'o', 'u'])) # {'o', 'e', 'a', 'i', 'u'}

# from range
print(set(range(5))) # {0, 1, 2, 3, 4}

# from set
print(set({'a', 'e', 'i', 'o', 'u'})) # {'o', 'u', 'e', 'a', 'i'}

# from dictionary
print(set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5})) # {'o', 'u', 'e', 'a', 'i'}

# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set)) # {'o', 'u', 'e', 'a', 'i'}
# Примечание. Мы не можем создавать пустые наборы с использованием синтаксиса {}, поскольку он создает пустой словарь. Чтобы создать пустой набор, мы используем set ()
# Example: Create set() for a custom iterable object / Создание set () для настраиваемого итерируемого объекта.
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

# print_num is an iterable / print_num является итерируемый
print_num = PrintNumber(5)

# creating a set / создание набора
print(set(print_num)) # {1, 2, 3, 4, 5}



input("Continue? (yes/no): ")



#################################################### any(iterable) ####################################################
# Функция any() возвращает True, если любой элемент итерируемого равен True. Если нет, any() возвращает False.
# any() возвращает логическое значение:
# True, если хотя бы один элемент итерируемого равен true
# Ложь, если все элементы ложны или если итерация пуста
# True since 1,3 and 4 (at least one) is true
print(any([1, 3, 4, 0])) # True
print(any([0, False])) # False
print(any([0, False, 5])) # True
print(any([])) # False
print(any("0")) # True
print(any('')) # False
print(any({0: 'asd'})) # False потому что ключ словаря ложный
print(any({0: 'qwe', 1: 'zxc'})) # True потому что один ключ(элемент) не ложный
print(any({0: 'False', False: 0})) # False
print(any({})) # False
print(any({'0': 'False'})) # True



input("Continue? (yes/no): ")



#################################################### all(iterable) ####################################################
# Метод all () возвращает:
# True - если все элементы в итерируемом являются истинными
# False - если какой-либо элемент в итерируемом является ложным
print(all([1, 3, 4, 5])) # True
print(all([0, False])) # False
print(all([1, 3, 4, 0])) # False
print(all([0, False, 5])) # False
print(all([])) # True
print(all("This is good")) # True
print(all('0')) # True
print(all('')) # True
print(all({0: 'False', 1: 'False'})) # False потому что один ключ(элемент) является ложным
print(all({1: 'True', 2: 'True'})) # True потому что все ключи(элементы) являются не ложный
print(all({1: 'True', False: 0})) # False потому что один ключ(элемент) является ложным
print(all({})) # True
print(all({'0': 'True'})) # True



input("Continue? (yes/no): ")



################################################### bool([value]) ####################################################
# Метод bool() преобразует значение в логическое (True или False), используя стандартную процедуру проверки истинности.
print(bool([])) # False
print(bool([0])) # True
print(bool(0.0)) # False
print(bool(None)) # False
print(bool(True)) # True
print(bool('Easy string')) # True



input("Continue? (yes/no): ")



############################################# iter(object, sentinel) ###################################################
# Функция Python iter () возвращает итератор для данного объекта.
# Функция iter () создает объект, который может повторяться по одному элементу за раз.
# Эти объекты полезны, когда связаны с циклами, такими как цикл for, while.
# Функция iter () принимает два параметра:
# object - объект, чей итератор должен быть создан (может быть наборами, кортежами и т. д.)
# sentinel (необязательно) - специальное значение, которое используется для представления конца последовательности
# Возвращаемое значение из iter ()
# Функция iter () возвращает объект итератора для данного объекта.
# Если определенный пользователем объект не реализует __iter __ () и __next __ () или __getitem () __, возникает исключение TypeError.
# Если также указан параметр sentinel, iter () возвращает итератор, пока символ стража не будет найден.
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)
print(next(vowels_iter)) # 'a'
print(next(vowels_iter)) # 'e'
print(next(vowels_iter)) # 'i'
print(next(vowels_iter)) # 'o'
print(next(vowels_iter)) # 'u'
# Пример 2: iter () для пользовательских объектов
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num
print_num = PrintNumber(3)
print_num_iter = iter(print_num)
print(next(print_num_iter)) # 1
print(next(print_num_iter)) # 2
print(next(print_num_iter)) # 3
try: print(next(print_num_iter)) # Код вызовет исключение # raises StopIteration
except: print("StopIteration")
# print(next(print_num_iter, "None")) # None, второй аргумент является default-ным, если итератор закончился то выводится "None"
# Пример 3: iter () с параметром sentinel
with open('test.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line)
# Когда вы запустите программу, она откроет файл test.txt в режиме чтения.
# Затем iter (fp.readline, '') в цикле for вызывает readline (который читает каждую строку в текстовом файле) до тех пор, пока не будет достигнут часовой символ '' (пустая строка).



input("Continue? (yes/no): ")



############################################## range(start, stop[, step]) ####################################################
# Функция range () возвращает неизменную последовательность чисел от заданного начального целого до конечного целого.
# range () принимает в основном три аргумента, одинаково используемых в обоих определениях:
# start - целое число, начиная с которого должна быть возвращена последовательность целых чисел.
# stop - целое число, перед которым должна быть возвращена последовательность целых чисел. Диапазон целых чисел заканчивается на стопе - 1.
# step (Optional/Необязательно) - целочисленное значение, которое определяет приращение между каждым целым числом в последовательности
# empty range
print(list(range(0))) # []
# using range(stop)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# using range(start, stop)
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Примечание. Мы преобразовали диапазон в список Python, поскольку range () возвращает объект, подобный генератору, который печатает выходные данные только по требованию.
# Вы также можете получить доступ к объекту диапазона по индексу как: rangeObject[index]
# Пример 2: Создайте список четных чисел между заданными числами, используя range ()
start = 2
stop = 14
step = 2
print(list(range(start, stop, step))) # [2, 4, 6, 8, 10, 12]
# Пример 3: как range () работает с отрицательным шагом?
start = 2
stop = -14
step = -2
print(list(range(start, stop, step))) # [2, 0, -2, -4, -6, -8, -10, -12]
# value constraint not met
print(list(range(start, 14, step))) # []



input("Continue? (yes/no): ")



############################################## enumerate(iterable, start=0) ####################################################
# Метод enumerate() добавляет счетчик к итерируемому и возвращает его (объект перечисления).
print(list(enumerate(['bread', 'milk']))) # [(0, 'bread'), (1, 'milk')]
print(list(enumerate(['bread', 'milk'], 10))) # [(10, 'bread'), (11, 'milk')]
for item in enumerate(['bread', 'milk']):
  print(item) # (0, 'bread')\n(1, 'milk')
for count, item in enumerate(['bread', 'milk']):
  print(str(count) + "_" + item) # 0_bread\n1_milk
for count, item in enumerate(['bread', 'milk'], 100):
  print(str(count) + "_" + item) # 100_bread\n101_milk



input("Continue? (yes/no): ")



#################################################### float([x]) ####################################################
# Метод float () возвращает число с плавающей запятой из числа или строки.
# Метод float () принимает один параметр: 
# x (необязательно) - число или строка, которые необходимо преобразовать в число с плавающей запятой
# Если это строка, строка должна содержать десятичные точки
# Метод float () возвращает:
# Эквивалентное число с плавающей запятой, если передан аргумент
# 0.0 если аргументы не переданы
# Исключение OverflowError, если аргумент находится за пределами диапазона с плавающей точкой Python
# for integers
print(float(10)) # 10.0
# for floats
print(float(11.22)) # 11.22
# for string floats
print(float("-13.33")) # -13.33
# for string floats with whitespaces
print(float("     -24.45\n")) # -24.45
# string float error
try: print(float("abc")) # Код вызовет исключение
except Exception as e: print(repr(e))



input("Continue? (yes/no): ")



#################################################### int(x=0, base=10) ####################################################
# Метод int () возвращает целочисленный объект из любого числа или строки.
print(int(12)) # 12
print(int(12.0)) # 12
print(int('12')) # 12
# Внутренне метод int () вызывает метод объекта __int __ ().
# Таким образом, даже если объект не является числом, вы можете преобразовать объект в целочисленный объект.
# Вы можете сделать это, переопределив методы класса __int __ () для возврата числа.
class Person:
    age = 23
    
    def __int__(self):
        return self.age
person = Person()
print('int(person) is:', int(person)) # int(person) is: 23



input("Continue? (yes/no): ")



###################################### getattr(object, name[, default]) == object.name #####################################
# Параметры getattr ()
# Метод getattr () принимает несколько параметров:
# object - объект, чье значение именованного атрибута должно быть возвращено
# name - строка, содержащая имя атрибута
# default (необязательно) - значение, которое возвращается, когда указанный атрибут не найден
# Возвращаемое значение из getattr ()
# Метод getattr () возвращает:
# значение именованного атрибута данного объекта
# по умолчанию, если именованный атрибут не найден
# Исключение AttributeError, если именованный атрибут не найден и значение по умолчанию не определено

# Example #1
class Person:
    age = 23
    name = "Adam"
person = Person()
print('The age is:', getattr(person, "age")) # The age is: 23
print('The age is:', person.age) # The age is: 23

# Example #2 (когда именованный атрибут не найден)
class Person:
    age = 23
    name = "Adam"
person = Person()
# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male')) # The sex is: Male
# when no default value is provided
try: print('The sex is:', getattr(person, 'sex')) # Код вызовет исключение
except AttributeError: print("AttributeError: 'Person' object has no attribute 'sex'")



input("Continue? (yes/no): ")



################################################ hasattr(object, name) ###############################################
# Метод hasattr () возвращает true, если объект имеет заданный именованный атрибут, и false, если его нет.
# Метод hasattr () принимает два параметра:
# object - объект, чей названный атрибут должен быть проверен
# name - имя атрибута для поиска
class Person:
    age = 23
    name = 'Adam'
person = Person()
print('Person has age?:', hasattr(person, 'age')) # True
print('Person has salary?:', hasattr(person, 'salary')) # False



input("Continue? (yes/no): ")



############################################ setattr(object, name, value) ###############################################
# Функция setattr () устанавливает значение атрибута объекта.
# Функция setattr () принимает три параметра:
# object/объект - объект, атрибут которого должен быть установлен
# name - имя атрибута
# value/значение - значение, данное атрибуту
# Возвращаемое значение из setattr ():
# Метод setattr () ничего не возвращает; Возвращает None.
# Example #1
class Person:
    name = 'Adam'

p = Person()
print('Before modification:', p.name) # Before modification: Adam

# setting name to 'John' / установив имя на 'Джон'
setattr(p, 'name', 'John')

print('After modification:', p.name) # After modification: John

# Example #2 When the attribute is not found in setattr() / Когда атрибут не найден в setattr ()
# Если атрибут не найден, setattr () создает новый атрибут и присваивает ему значение. Однако это возможно только в том случае, если объект реализует метод __dict __ ().
# Вы можете проверить все атрибуты объекта с помощью функции dir ().
class Person:
    name = 'Adam'

p = Person()

# setting attribute name to John / установка имени атрибута для Джона
setattr(p, 'name', 'John')
print('Name is:', p.name) # Name is: John

# setting an attribute not present in Person / установка атрибута, отсутствующего в Person
setattr(p, 'age', 23)
print('Age is:', p.age) # Age is: 23



input("Continue? (yes/no): ")



################################################ delattr(object, name) ###############################################
# delattr () удаляет атрибут из объекта (если объект позволяет это).
# delattr () принимает два параметра:
# object/объект - объект, из которого атрибут имени должен быть удален
# name - строка, которая должна быть именем атрибута, который будет удален из объекта
# Возвращаемое значение из delattr ()
# delattr () не возвращает никакого значения (возвращает None). Это только удаляет атрибут (если объект позволяет это).
class Coordinate:
  x = 10
  y = -5
  z = 0

point1 = Coordinate() 

print('x = ',point1.x) # x =  10
print('y = ',point1.y) # y =  -5
print('z = ',point1.z) # z =  0

delattr(Coordinate, 'z') # Здесь атрибут z удаляется из класса Coordinate с помощью delattr (Coordinate, 'z')
# del Coordinate.z # Вы также можете удалить атрибут объекта, используя оператор del

print('--After deleting z attribute--') # --After deleting z attribute--
print('x = ',point1.x) # x =  10
print('y = ',point1.y) # y =  -5

# Raises Error
try: print('z = ',point1.z)
except AttributeError: print("'Coordinate' object has no attribute 'z'")



input("Continue? (yes/no): ")




############################################# isinstance(object, classinfo) #############################################
# Функция isinstance () проверяет, является ли объект (первый аргумент) экземпляром или подклассом класса classinfo (второй аргумент).
# Функция isinstance () принимает два параметра:
# object - объект для проверки
# classinfo - класс, тип или кортеж классов и типов
# isinstance () возвращает:
# True, если объект является экземпляром или подклассом класса, или любым элементом кортежа
# False, в противном случае
# Если classinfo не является типом или кортежем типов, возникает исключение TypeError.
class Foo: pass
fooInstance = Foo()
print(isinstance(fooInstance, Foo)) # True
print(isinstance(fooInstance, (list, tuple))) # False
print(isinstance(fooInstance, (list, tuple, Foo))) # True
# More examples
numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result) # [1, 2, 3] instance of list? True

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result) # [1, 2, 3] instance of dict? False

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result) # [1, 2, 3] instance of dict or list? True

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result) # 5 instance of list? False

result = isinstance(number, int)
print(number,'instance of int?', result) # 5 instance of int? True



input("Continue? (yes/no): ")



############################################# issubclass(object, classinfo) #############################################
# Функция issubclass () проверяет, является ли аргумент объекта (первый аргумент) подклассом класса classinfo (второй аргумент).
# issubclass () принимает два параметра:
# object - класс для проверки
# classinfo - класс, тип или кортеж классов и типов
# issubclass () возвращает:
# True, если объект является подклассом класса или любого элемента кортежа
# False, B противном случае
class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon)) # True
print(issubclass(Triangle, list)) # False
print(issubclass(Triangle, (list, Polygon))) # True
print(issubclass(Polygon, (list, Polygon))) # True
# Важно отметить, что класс считается подклассом сам по себе.



input("Continue? (yes/no): ")



############################### max(iterable, *iterables, key, default) or max(arg1, arg2, *args, key) #################
# Функция Python max () возвращает самый большой элемент в итерации. Его также можно использовать для поиска наибольшего элемента между двумя или более параметрами.
# The max() function has two forms:
# // to find the largest item in an iterable
# max(iterable, *iterables, key, default)
# // to find the largest item between two or more objects
# max(arg1, arg2, *args, key)
# max () Параметры // to find the largest item in an iterable
# iterable - итеративный, такой как список, кортеж, набор, словарь и т. д.
# * iterables (необязательно) - любое количество итераций; может быть более одного
# key (необязательно) - ключевая функция, в которой передаются итерации и сравнение выполняется на основе их возвращаемого значения
# default (необязательно) - значение по умолчанию, если данная итерация пуста
# Get the largest item in a list/set/tuple/string/dict
print(max([1, 3, 2])) # 3
print(max({1, 3, 2})) # 3
print(max((1, 3, 2))) # 3
print(max(["Python", "C Programming", "Java", "JavaScript"])) # Python
# Если элементы в итерируемом являются строками, возвращается самый большой элемент (упорядоченный по алфавиту).
# В случае словарей max () возвращает самый большой ключ. 
square = {2: 4, -3: 9, -1: 1, -2: 4}
# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2
# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])
print("The key with the largest value:", key2)    # -3
# getting the largest value
print("The largest value:", square[key2])    # 9
# Во второй функции max () мы передали лямбда-функцию ключевому параметру. key = lambda k: square[k]
# Несколько заметок:
# Если мы пропустим пустой итератор, возникает исключение ValueError. Чтобы избежать этого, мы можем передать параметр по умолчанию.
# Если мы передаем более одного итератора, возвращается самый большой элемент из заданных итераторов.
# max () параметры // to find the largest item between two or more objects
# arg1 - объект; могут быть числа, строки и т. д.
# arg2 - объект; могут быть числа, строки и т. д.
# * args (необязательно) - любое количество объектов
# key (необязательно) - ключевая функция, в которой передается каждый аргумент, и сравнение выполняется на основе его возвращаемого значения
# По сути, функция max () находит самый большой элемент между двумя или более объектами.
print(max(4, -5, 23, 5)) # 23



input("Continue? (yes/no): ")



############################### min(iterable, *iterables, key, default) or min(arg1, arg2, *args, key) #################
# Функция Python min () возвращает наименьший элемент в итерации. Его также можно использовать для поиска наименьшего элемента между двумя или более параметрами.
# The min() function has two forms:
# // to find the smallest item in an iterable
# min(iterable, *iterables, key, default)
# // to find the smallest item between two or more objects
# min(arg1, arg2, *args, key)
# min () Параметры // to find the smallest item in an iterable
# iterable - итеративный, такой как список, кортеж, набор, словарь и т. д.
# * iterables (необязательно) - любое количество итераций; может быть более одного
# key (необязательно) - ключевая функция, в которой передаются итерации и сравнение выполняется на основе их возвращаемого значения
# default (необязательно) - значение по умолчанию, если данная итерация пуста
# Get the smallest item in a list/set/tuple/string/dict
print(min([1, 3, 2])) # 1
print(min({1, 3, 2})) # 1
print(min((1, 3, 2))) # 1
print(min(["Python", "C Programming", "Java", "JavaScript"])) # C Programming
# Если элементы в итерируемом являются строками, возвращается наименьший элемент (упорядоченный по алфавиту).
# В случае словарей min () возвращает наименьший ключ. 
square = {2: 4, -3: 9, -1: 1, -2: 4}
# the smallest key
key1 = min(square)
print("The smallest key:", key1)  # -3
# the key whose value is the smallest
key2 = min(square, key = lambda k: square[k])
print("The key with the smallest value:", key2)  # -1
# getting the smallest value
print("The smallest value:", square[key2]) # 1
# Во второй функции min () мы передали лямбда-функцию ключевому параметру. key = lambda k: square[k]
# Несколько заметок:
# Если мы пропустим пустой итератор, возникает исключение ValueError. Чтобы избежать этого, мы можем передать параметр по умолчанию.
# Если мы передаем более одного итератора, возвращается наименьший элемент из заданных итераторов.
# min () параметры // to find the smallest item between two or more objects
# arg1 - объект; могут быть числа, строки и т. д.
# arg2 - объект; могут быть числа, строки и т. д.
# * args (необязательно) - любое количество объектов
# key (необязательно) - ключевая функция, в которой передается каждый аргумент, и сравнение выполняется на основе его возвращаемого значения
# По сути, функция min () находит наименьший элемент между двумя или более объектами.
print(min(4, -5, 23, 5)) # -5



input("Continue? (yes/no): ")



############################################# eval, exec, compile ###########################################################
############################### eval(expression, globals=None, locals=None) ###############################
# Метод eval() анализирует выражение, переданное этому методу, и выполняет выражение (код) Python в программе.
# Функция eval() принимает три параметра:
# expression - строка, проанализированная и оцененная как выражение Python
# globals (необязательно) - словарь
# locals (необязательно) - объект сопоставления. Словарь - это стандартный и часто используемый тип отображения в Python.
# Возвращаемое значение из eval()
# Метод eval() возвращает результат, полученный из выражения.
x = 1
print(eval('x + 1')) # 2

# Практический пример для демонстрации использования eval()
def calculate_perimeter(i):
    return 4*i

def calculate_area(i):
    return i*i

expression = input("Type a function: ")

for i in range(1, 5):
  if expression in ('area', 'perimeter'):
    code = 'calculate_expression(i)'
    print("If length is", i, ",", expression, "=", eval(code.replace('expression', expression)))
  else:
    break
# Bыводится:
# Type a function: perimeter
# If length is  1 , Perimeter =  4
# If length is  2 , Perimeter =  8
# If length is  3 , Perimeter =  12
# If length is  4 , Perimeter =  16

# Возможно, вам придется ограничить использование доступных методов и переменных для eval ().
# Вы можете сделать это, передавая необязательные globals и locals параметры (словари) в функцию eval ().
# Если оба параметра опущены, выражение выполняется в текущей области видимости. 
# Глобальные и локальные параметры (словари) используются для глобальных и локальных переменных соответственно. 
# Если словарь locals пропущен, по умолчанию используется словарь globals. 
# Это означает, что глобальные переменные будут использоваться как для глобальных, так и для локальных переменных.

# передача пустого словаря в качестве параметра globals
from math import *
print(eval('dir()', {})) # ['__builtins__']
try: print(eval('sqrt(25)', {})) # Код вызовет исключение
except NameError: print("[log] ERROR: name 'sqrt' is not defined")

# Обеспечение доступности некоторых методов
from math import *
print(eval('dir()', {'sqrt': sqrt, 'a': 25})) # ['__builtins__', 'sqrt', 'a']
print(eval('sqrt(a)', {'sqrt': sqrt, 'a': 25})) # 5.0

# Oграничение использования встроенных модулей
# Вы можете ограничить использование __builtins__ в выражении следующим образом:
try: eval('print("Hello world")', {'__builtins__': None}) # Код вызовет исключение
except TypeError: print("[log] ERROR: 'NoneType' object is not subscriptable")

# Вы также можете использовать некоторых встроенных модулей передавая в globals/locals
eval('print("Hello world")', {'__builtins__': None, 'print': print}) # Hello world

# Вы можете сделать необходимые функции и переменные доступными для использования, передав словарь locals. Например:
from math import *
print(eval('sqrt(a)', {'__builtins__': None}, {'a': 169, 'sqrt': sqrt})) # 13.0



input("Continue? (yes/no): ")



######################################### exec(object, globals, locals) ###############################
# Метод exec () выполняет динамически созданную программу, которая является либо строкой, либо объектом кода.
# Параметры exec ()
# exec () принимает три параметра:
# object - либо строка, либо объект кода
# globals (необязательно) - словарь
# locals (необязательно) - объект сопоставления.
# Возвращаемое значение из exec ()
# Exec () не возвращает никакого значения, он возвращает None.
# Example #1
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program) # Sum = 15
program = "[print(item) for item in [1, 2, 3]]"
exec(program) # 1\n2\n3
# Возможно, вам придется ограничить использование доступных методов и переменных для exec ().
# Вы можете сделать это, передавая необязательные globals и locals параметры (словари) в функцию exec ().
# Если оба параметра опущены, выражение выполняется в текущей области видимости. 
# Глобальные и локальные параметры (словари) используются для глобальных и локальных переменных соответственно. 
# Если словарь locals пропущен, по умолчанию используется словарь globals. 
# Это означает, что глобальные переменные будут использоваться как для глобальных, так и для локальных переменных.

# передача пустого словаря в качестве параметра globals
from math import *
exec('print(dir())', {}) # ['__builtins__']
try: exec('print(sqrt(25))', {}) # Код вызовет исключение
except NameError: print("[log] ERROR: name 'sqrt' is not defined")

# Обеспечение доступности некоторых методов
from math import *
exec('print(dir())', {'sqrt': sqrt, 'a': 25}) # ['__builtins__', 'sqrt', 'a']
exec('print(sqrt(a))', {'sqrt': sqrt, 'a': 25}) # 5.0

# Oграничение использования встроенных модулей
# Вы можете ограничить использование __builtins__ в выражении следующим образом:
try: exec('print("Hello world")', {'__builtins__': None}) # Код вызовет исключение
except TypeError: print("[log] ERROR: 'NoneType' object is not subscriptable")

# Вы также можете использовать некоторых встроенных модулей передавая в globals/locals
exec('print("Hello world")', {'__builtins__': None, 'print': print}) # Hello world

# Вы можете сделать необходимые функции и переменные доступными для использования, передав словарь locals. Например:
from math import *
def Sqrt(a):
  print(sqrt(a))
exec('Sqrt(a)', {'__builtins__': None}, {'a': 169, 'Sqrt': Sqrt}) # 13.0
# Вы можете сохранить глобальных и локальных переменных в словарь, передав в object необходимый код
g = dict()
l = dict()
exec('global a; a, b = 123, 42', g, l)
print(g['a']) # 123
print(l) # {'b': 42}

# Будьте осторожны при использовании exec()/eval() 
# Рассмотрим ситуацию: вы используете систему Unix (macOS, Linux и т. Д.) И импортировали модуль os. Модуль os предоставляет переносимый способ использования функций операционной системы, таких как: чтение или запись файла.
# Если вы разрешаете пользователям вводить значение с помощью exec(input())/eval(input()), пользователь может вводить команды для изменения файла или даже удалять все файлы с помощью команды os.system ('rm -rf *').
# Если вы используете exec(input())/eval(input()) в своем коде, рекомендуется проверить, какие переменные и методы может использовать пользователь. Вы можете увидеть, какие переменные и методы доступны, используя метод dir ().

# В чем разница между eval, exec?
# По сути, eval используется для оценки одного динамически генерируемого выражения Python, а exec используется для выполнения динамически генерируемого кода Python только для его побочных эффектов.
# Eval и Exec имеют эти два различия:
# eval принимает только одно выражение, exec может принимать блок кода, который имеет операторы Python: loops, try: exception :, определения классов и функций / методов и так далее.
# Выражение в Python - это то, что вы можете иметь в качестве значения в присваивании переменной:
# a_variable = (все, что вы можете поместить в эти скобки, является выражением)
# eval возвращает значение данного выражения, тогда как exec игнорирует возвращаемое значение из своего кода и всегда возвращает None
# В Python 3 exec является функцией; его использование не влияет на скомпилированный байт-код функции, в которой он используется.
a = 5
a = eval('37 + a') # Это выражение
print(a) # 42

a = exec('37 + a') # Значение игнорируется (None возвращается)
print(a) # None

exec('a = 5') # Изменить глобальную переменную как побочный эффект
print(a) # 5

exec('a = 37 + a')
print(a) # 42

try : eval('a = 47') # Код вызовет исключение. Вы не можете оценить утверждение
except: 
  print("""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    a = 47
      ^
SyntaxError: invalid syntax""")



input("Continue? (yes/no): ")



############################ compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) #####################
# Метод compile () возвращает объект кода Python из источника (обычная строка, строка байтов или объект AST).
# Метод compile () используется, если код Python находится в строковой форме или является объектом AST, и вы хотите изменить его на объект кода.
# Объект кода, возвращаемый методом compile (), позже может быть вызван с использованием таких методов, как: exec () и eval (), которые будут выполнять динамически генерируемый код Python.
# Параметры compile ():
# source - нормальная строка, байтовая строка или объект AST
# filename - файл, из которого был прочитан код. Если он не был прочитан из файла, вы можете дать имя себе
# mode - либо exec, либо eval, либо single.
# eval - принимает только одно выражение.
# exec - может принимать блок кода, содержащий операторы Python, класс и функции и т. д.
# single - если он состоит из одного интерактивного оператора
# flags (необязательно) и dont_inherit (необязательно) - определяет, какие будущие операторы будут влиять на компиляцию источника. Значение по умолчанию: 0
# optimize (необязательно) - уровень оптимизации компилятора. Значение по умолчанию -1.
# Возвращаемое значение из compile ():
# Метод compile () возвращает объект кода Python.
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')
exec(codeObject)
# OUTPUT: sum = 11
# Здесь источник находится в обычной строковой форме. Имя файла - sumstring. Кроме того, режим exec позже позволяет использовать метод exec ().
# Метод compile () преобразует строку в объект кода Python. Затем объект кода выполняется с использованием метода exec ().



input("Continue? (yes/no): ")


################################################ globals, locals ################################################
# Таблица символов - это структура данных, поддерживаемая компилятором, которая содержит всю необходимую информацию о программе.
# К ним относятся имена переменных, методы, классы и т. Д.
# Существует в основном два вида таблицы символов.
# Глобальная таблица символов
# Таблица локальных символов
# Глобальная таблица символов хранит всю информацию, относящуюся к глобальной области видимости программы, и доступна в Python с помощью метода globals ().
# Глобальная область действия содержит все функции, переменные, которые не связаны ни с одним классом или функцией.
# Аналогично, в таблице локальных символов хранится вся информация, относящаяся к локальной области программы, и доступ к ней осуществляется в Python с помощью метода locals ().
# Локальная область видимости может быть внутри функции, внутри класса и т. Д.

##################################### globals() [method doesn't take any parameters] #####################################
# Метод globals () возвращает словарь текущей таблицы глобальных символов.
# Таблица символов - это структура данных, поддерживаемая компилятором, которая содержит всю необходимую информацию о программе.
# К ним относятся имена переменных, методы, классы и т. Д.
# Существует в основном два вида таблицы символов.
# Таблица локальных символов
# Глобальная таблица символов
# Локальная таблица символов хранит всю информацию, относящуюся к локальной области видимости программы, и доступна в Python с помощью метода locals ().
# Локальная область видимости может быть внутри функции, внутри класса и т. Д.
# Аналогично, таблица глобальных символов хранит всю информацию, относящуюся к глобальной области действия программы, и доступна в Python с помощью метода globals ().
# Глобальная область действия содержит все функции, переменные, которые не связаны ни с одним классом или функцией.
# Example #1 (Выходные данные показывают все глобальные переменные и другие символы для текущей программы.)
print(globals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
# Example #2 (Изменить глобальную переменную с помощью globals ())
age = 23
globals()['age'] = 25
print('The age is:', age) # The age is: 25


input("Continue? (yes/no): ")


################################################### locals() ##############################################
# Метод locals () обновляет и возвращает словарь текущей таблицы локальных символов.
# Example 1
print(locals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
# Примечание: таблица символов globals () и locals () для глобальной среды одинакова.
# Пример 2: как locals () работает внутри локальной области видимости?
def localsNotPresent():
    return locals()
def localsPresent():
    present = True
    return locals()
print('localsNotPresent:', localsNotPresent()) # localsNotPresent: {}
print('localsPresent:', localsPresent()) # localsPresent: {'present': True}
# Пример 3: Обновление значений словаря locals ()
def localsPresent():
    present = True
    print(present)
    locals()['present'] = False;
    print(present)
localsPresent() #True\nTrue
# В отличие от словаря globals (), который отражает изменение фактической глобальной таблицы, словарь locals () может не изменять информацию внутри таблицы locals.



input("Continue? (yes/no): ")



####################################################### len(s) ##############################################################
# Функция len () возвращает количество элементов (длину) в объекте.
# len () Параметры:
# s - последовательность (строка, байты, кортеж, список или диапазон) или коллекция (словарь, набор или замороженный набор)
# Функция len () возвращает количество элементов объекта.
# Если не передать аргумент или передать неверный аргумент, возникнет исключение TypeError.
print(len([1, 2, 3])) # 3
print(len((1, 2, 3))) # 3
print(len({1, 2, 3})) # 3
print(len(set({1, 2, 3}))) # 3
print(len({1: 1, 2: 2, 3: 3})) # 3
print(len(range(1, 10))) # 9
print(len("Hello world")) # 11
print(len(b"Hello world")) # 11
print(len(bytes([1, 2, 3]))) # 3
# Внутренне len () вызывает метод __len__ объекта. Вы можете думать о len () как:
def len(s):
    return s.__len__()
# Таким образом, вы можете назначить объекту произвольную длину (при необходимости)
# Пример 4: Как len () работает для пользовательских объектов?
class Session:
    def __init__(self, number = 0):
      self.number = number
    def __len__(self):
      return self.number
# default length is 0
s1 = Session()
print(len(s1)) # 0
# giving custom length
s2 = Session(6)
print(len(s2)) # 6



input("Continue? (yes/no): ")



##################################################### reversed(seq) #######################################################
# Функция reversed () возвращает реверсированный итератор данной последовательности.
# Функция reversed () принимает один параметр:
# seq - последовательность, подлежащая обращению
# Последовательность - это объект, который поддерживает протоколы последовательности: методы __len __ () и __getitem __ (). Например, кортеж, строка, список, диапазон и т. Д.
# Мы также можем использовать reversed () в любом объекте, который реализует __reverse __ ().
# Возвращаемое значение из reversed ()
# Функция reversed () возвращает итератор, который обращается к данной последовательности в обратном порядке.
# for string
seq_string = 'Python'
print(list(reversed(seq_string))) # ['n', 'o', 'h', 't', 'y', 'P']
# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple))) # ['n', 'o', 'h', 't', 'y', 'P']
# for range
seq_range = range(5, 9)
print(list(reversed(seq_range))) # [8, 7, 6, 5]
# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list))) # [5, 3, 4, 2, 1]
# В нашем примере мы преобразовали итераторы, возвращаемые функцией reversed (), в список с помощью функции list ().
# Пример 2: reversed () в пользовательских объектах
class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v))) # ['u', 'o', 'i', 'e', 'a']



input("Continue? (yes/no): ")



############################################### slice(start, stop, step) #################################################
# Функция slice () возвращает объект слайса, который можно использовать для нарезки строк, списков, кортежей и т. Д.
# Объект слайса используется для вырезания заданной последовательности (строки, байтов, кортежа, списка или диапазона) или любого объекта, который поддерживает протокол последовательности (реализует методы __getitem __ () и __len __ ()).
# slice () может принимать три параметра:
# start (необязательно) - начальное целое число, с которого начинается разрезание объекта. По умолчанию None, если не указано.
# stop - целое число, до которого происходит нарезка. Нарезка останавливается на индексе стоп-1 (последний элемент).
# step (необязательно) - целочисленное значение, которое определяет приращение между каждым индексом для нарезки. По умолчанию Нет, если не указано иное.
# Пример 1. Создание объекта среза для нарезки
# contains indices (0, 1, 2)
result1 = slice(3)
print(result1) # slice(None, 3, None)
# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2)) # slice(1, 5, 2)
# Здесь result1 и result2 являются объектами среза.
# Теперь мы знаем об объектах среза, давайте посмотрим, как мы можем получить подстроку, подсписок, поднабор и т. Д. Из объектов среза.
# Пример 2: Получить подстроку, используя объект среза
# Program to get a substring from the given string 
py_string = 'Python'
# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3) 
print(py_string[slice_object]) # Pyt
# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object]) # yhn

# Пример 3: Получить подстроку с использованием отрицательного индекса
py_string = 'Python'
# start = -1, stop = -4, step = -1
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)
print(py_string[slice_object]) # noh

# Пример 4: Получить подсписок и поднабор
py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']
# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h')  

# Пример 5: Получить подсписок и поднабор, используя отрицательный индекс
py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1) 
print(py_list[slice_object])  # ['n', 'o', 'h']
# contains indices -1 and -3
slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object]) # ('n', 'h')

# Пример 6: Использование синтаксиса индексации для нарезки
# Объект slice может быть заменен синтаксисом индексации в Python.
# Вы можете поочередно использовать следующий синтаксис для нарезки: obj[start:stop:step]
py_string = 'Python'
# contains indices 0, 1 and 2
print(py_string[0:3])  # Pyt
# contains indices 1 and 3
print(py_string[1:5:2]) # yh



input("Continue? (yes/no): ")



##################################################### vars(object) #######################################################
# Функция vars () возвращает атрибут __dict__ данного объекта.
# vars () принимает максимум один параметр:
# object/объект - это может быть модуль, класс, экземпляр или любой объект, имеющий атрибут __dict__.
# Возвращаемое значение из vars ()
# vars () возвращает атрибут __dict__ данного объекта.
# Если объект, переданный vars (), не имеет атрибута __dict__, он вызывает исключение TypeError.
# Если аргумент vars () не передается, эта функция действует как функция locals ().
# Примечание: __dict__ - это словарь или объект отображения. Он хранит (доступные для записи) атрибуты объекта.
class Foo:
  def __init__(self, a = 5, b = 10):
    self.a = a
    self.b = b
object = Foo()
print(vars(object)) # {'a': 5, 'b': 10}
# Также запустите эти операторы на оболочке Python:
# >>> vars(list)
# >>> vars(str)
# >>> vars(dict)



input("Continue? (yes/no): ")



############################# __import__(name, globals=None, locals=None, fromlist=(), level=0) ############################
# __import__() - это функция, которая вызывается оператором import.
# __import __ () Параметры
# name - название модуля, который вы хотите импортировать
# globals и locals - определяет, как интерпретировать имя
# fromlist - объекты или подмодули, которые должны быть импортированы по имени
# level - указывает, использовать ли абсолютный или относительный импорт
# Использование __import __ () не рекомендуется
# Эта функция __import __ () не нужна для повседневной программы на Python. Это редко используется и часто не рекомендуется.
# Эта функция может использоваться для изменения семантики оператора импорта, так как оператор вызывает эту функцию. Вместо этого лучше использовать импортные хуки.
# И, если вы хотите импортировать модуль по имени, используйте importlib.import_module ().
mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5)) # 2.5
# Метод fabs () определен в математическом модуле. Вы можете вызвать эту функцию, используя следующий синтаксис:
import math
print(math.fabs(-2.5)) # 2.5
# Однако в приведенной выше программе мы изменили способ работы fabs (). Теперь мы также можем получить доступ к fabs (), используя следующий синтаксис:
print(mathematics.fabs(-2.5)) # 2.5



input("Continue? (yes/no): ")



################################################# callable(object) ###################################################
# Метод callable () возвращает True, если переданный объект кажется вызываемым. Если нет, возвращается False.
# Метод callable () принимает объект с одним аргументом.
# Метод callable () возвращает:
# True - если объект кажется вызываемым
# False - если объект не подлежит вызову.
# Важно помнить, что даже если callable () имеет значение True, вызов объекта все равно может завершиться ошибкой.
# Однако, если callable () возвращает False, вызов объекта обязательно завершится неудачей.
x = 5
print(callable(x)) # False
def testFunction():
  print("Test")
y = testFunction
print(callable(y)) # True
# Здесь объект x не может быть вызван. И объект у кажется вызываемым (но не вызываемым).
# Пример 2: вызываемый объект
class Foo:
  def __call__(self):
    print('Print Something')
print(callable(Foo)) # True
# Экземпляр класса Foo представляется вызываемым (и в этом случае вызываемым).
# Пример 3: Объект кажется вызываемым, но не вызываемым.
class Foo:
  def printLine(self):
    print('Print Something')
print(callable(Foo)) # True
# Экземпляр класса Foo кажется вызываемым, но не вызываемым. Следующий код вызовет ошибку
class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo)) # True

InstanceOfFoo = Foo()
# Raises an Error
# 'Foo' object is not callable
try: InstanceOfFoo()
except TypeError: print("'Foo' object is not callable")



input("Continue? (yes/no): ")



########################################## bytes([source[, encoding[, errors]]]) ########################################
# Метод bytes () возвращает неизменный байтовый объект, инициализированный с заданным размером и данными.
# Метод bytes () возвращает объект bytes, который является неизменной (не может быть изменена) последовательностью целых чисел в диапазоне 0 <= x <256.
# Если вы хотите использовать изменяемую версию, используйте метод bytearray ().
# bytes () принимает три необязательных параметра:
# source (необязательно) - источник для инициализации массива байтов.
# encoding/кодировка (необязательно) - если источником является строка, кодировка строки.
# errors/ошибки (необязательно) - если источником является строка, действие, выполняемое при сбое преобразования кодировки
# Возвращаемое значение из байтов ()
# Метод bytes () возвращает байтовый объект заданного размера и значений инициализации.

# Исходный параметр можно использовать для инициализации байтового массива следующими способами: / The source parameter can be used to initialize the byte array in the following ways:
                                    # Различные параметры источника / Different source parameters
# +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
# | Тип                   | Описание                                                                                                                                                       |
# +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
# | String                | Преобразует строку в байты с помощью str.encode (). Должен также обеспечивать кодирование и необязательные ошибки.                                             |
# | Integer               | Создает массив заданного размера, все инициализируются как ноль                                                                                                |
# | Object                | Доступный только для чтения буфер объекта будет использоваться для инициализации массива байтов.                                                               |
# | Iterable              | Создает массив размером, равным итерируемому числу и инициализируемый итерируемым элементам. Должен быть итерируемым из целых чисел в диапазоне от 0 <= x <256 |
# | No source (arguments) | Создает массив размером 0                                                                                                                                      |
# +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

# Пример 1: преобразование строки в байты
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr) # b'Python is interesting.'

# Пример 2. Создание байта с заданным целочисленным размером
size = 5
arr = bytes(size)
print(arr) # b'\x00\x00\x00\x00\x00'

# Пример 3: преобразовать итеративный список в байты
rList = [1, 2, 3, 4, 5]
arr = bytes(rList)
print(arr) # b'\x01\x02\x03\x04\x05'



input("Continue? (yes/no): ")



################################################ zip(*iterables) #####################################################
# Функция zip () принимает итераторы (может быть нулем или более), объединяет их в кортеж и возвращает его.
# Параметры zip ():
# iterables - могут быть встроенными итерациями (например: list, string, dict) или пользовательскими итерациями
# Возвращаемое значение из zip ()
# Функция zip () возвращает итератор кортежей на основе итерируемых объектов.
# Если мы не передадим какой-либо параметр, zip () вернет пустой итератор
# Если передается одна итерация, zip () возвращает итератор кортежей, каждый из которых имеет только один элемент.
# Если передано несколько итераций, zip () возвращает итератор кортежей, каждый из которых имеет элементы из всех итераций.
# Предположим, две итерации передаются в zip (); один повторяемый, содержащий три, а другой содержащий пять элементов. Затем возвращенный итератор будет содержать три кортежа. Это потому, что итератор останавливается, когда самая короткая итерация исчерпана.
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
# No iterables are passed
result = zip()
# Converting itertor to list
result_list = list(result)
print(result_list) # []
# Two iterables are passed
result = zip(number_list, str_list)
# Converting itertor to set
result_set = set(result)
print(result_set) # {(2, 'two'), (3, 'three'), (1, 'one')}

# Пример 2: Разное количество повторяемых элементов
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)
# Converting to set
result_set = set(result)
print(result_set) # {(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}
result = zip(numbersList, str_list, numbers_tuple)
# Converting to set
result_set = set(result)
print(result_set) # {(2, 'two', 'TWO'), (1, 'one', 'ONE')}

# Пример 3: Распаковка значения с помощью zip ()
# Оператор * может использоваться вместе с zip () для распаковки списка. zip(*zippedList)
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
print(result_list) # [('x', 3), ('y', 4), ('z', 5)]
c, v =  zip(*result_list)
print('c =', c) # c = ('x', 'y', 'z')
print('v =', v) # v = (3, 4, 5)



input("Continue? (yes/no): ")



######################################## str(object, encoding='utf-8', errors='strict') #####################################
# Функция str () возвращает строковую версию данного объекта.
# Метод str () принимает три параметра:
# object - объект, чье строковое представление должно быть возвращено Если не указан, возвращает пустую строку
# encoding/кодировка - кодировка данного объекта. Значения по умолчанию UTF-8, если не указано.
# errors/ошибки - ответ при сбое декодирования. По умолчанию «строгий»/«strict».
# Существует шесть типов ошибок:
# strict/строгий - ответ по умолчанию, который вызывает исключение UnicodeDecodeError в случае сбоя
# ignore - игнорирует не кодируемый Unicode из результата
# replace/заменить - заменяет не кодируемый Unicode на знак вопроса
# xmlcharrefreplace - вставляет ссылку на символ XML вместо Unicodable Unicode
# backslashreplace - вставляет последовательность пробелов \ uNNNN вместо не кодируемого Unicode
# namereplace - вставляет escape-последовательность \ N {...} вместо не кодируемого Unicode
# Возвращаемое значение из str ()
# Метод str () возвращает строку, которая считается неформальным или красиво печатаемым представлением данного объекта.
# Пример 1: преобразовать в строку
# Если параметр кодирования и ошибок не указан, str () внутренне вызывает метод __str __ () объекта.
# Если он не может найти метод __str __ (), он вместо этого вызывает repr (obj).
result = str(10)
print(result) # 10
# Примечание: переменная результата будет содержать строку.

# Пример 2: Как работает str () для байтов?
# Если указан параметр кодирования и ошибок, первый параметр, object, должен быть похожим на байты объектом (bytes или bytearray).
# Если объект является байтами или bytearray, str () внутренне вызывает bytes.decode (кодировка, ошибки).
# В противном случае он получает байтовый объект в буфере перед вызовом метода decode ().
# bytes
b = bytes('pythön', encoding='utf-8')
print(str(b, encoding='ascii', errors='ignore')) # pythn
# Здесь символ 'ö' не может быть декодирован ASCII. Следовательно, это должно дать ошибку. Однако мы установили ошибки = «игнорировать/ignore». Следовательно, Python игнорирует символ, который не может быть декодирован str ().



input("Continue? (yes/no): ")



############################################## filter(function, iterable) ####################################################
# Метод filter() создает итератор из элементов итерируемого объекта, для которого функция возвращает true.
# Проще говоря, метод filter () фильтрует заданную итерацию с помощью функции, которая проверяет, является ли каждый элемент в итерируемом истинным или нет.
# Метод filter() принимает два параметра:
# function - функция, которая проверяет, возвращает ли элемент итерируемого значение true или false
# Если None, функция по умолчанию имеет функцию Identity - которая возвращает false, если какие-либо элементы имеют значение false
# iterable - итерируемый, который должен фильтроваться, может быть множествами, списками, кортежами или контейнерами любых итераторов.
# Возвращаемое значение из фильтра ()
# Метод filter() возвращает итератор, который прошел проверку функции для каждого элемента итерируемого.
# Метод filter () эквивалентен:
# # когда функция определена
# (element for element in iterable if function(element))
# # когда функция отсутствует
# (element for element in iterable if element)

# filter() method with filter function
def get_upper_letters(letter):
  upper_letters = ["A", "B", "C"]

  if letter in upper_letters:
    return True
  else:
    return False

filtered_list = filter(get_upper_letters, ['a', 'b', 'C', 'D', 'g', 'A', 'f', 'B'])

for i in filtered_list:
  print(i) # C\nA\nB

# filter() method without filter function
filter_type = None # or bool
filtered_list = filter(filter_type, [1, 'a', 0, False, True, '0'])
for i in filtered_list:
  print(i) # 1\n'a'\nTrue\n'0'



input("Continue? (yes/no): ")



####################################### sorted(iterable, key=None, reverse=False) #########################################
# Функция sorted() возвращает отсортированный список из элементов в итерируемой.
# Функция sorted() сортирует элементы заданной итерации в определенном порядке (по возрастанию или по убыванию) и возвращает отсортированную итерацию в виде списка.
# sorted() может принимать максимум три параметра:
# iterable/Итерируемый - последовательность (строка, кортеж, список) или коллекция (набор, словарь, замороженный набор) или любой другой итератор.
# reverse (Необязательно) - если True, отсортированный список переворачивается (или сортируется в порядке убывания). По умолчанию False, если не указано иное.
# key/ключ (необязательно) - функция, которая служит ключом для сравнения сортировки. По умолчанию Нет.
# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list)) # ['a', 'e', 'i', 'o', 'u']
# string
py_string = 'Python'
print(sorted(py_string)) # ['P', 'h', 'n', 'o', 't', 'y']
# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple)) # ['a', 'e', 'i', 'o', 'u']
# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True)) # ['u', 'o', 'i', 'e', 'a']
# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True)) # ['u', 'o', 'i', 'e', 'a']
# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True)) # ['u', 'o', 'i', 'e', 'a']
# Если вам нужна собственная реализация для сортировки, sorted () также принимает ключевую функцию в качестве необязательного параметра.
# Основываясь на возвращенном значении ключевой функции, вы можете отсортировать данную итерацию.
# Пример 3: сортировка списка с использованием функции sorted (), имеющей функцию ключа
# take the second element for sort
def take_second(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list) # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

# Пример 4: сортировка по нескольким ключам
# Предположим, что у нас есть следующий список:
# Вложенный список информации о студентах в олимпиаде по науке
# Элементы списка: (Имя ученика, Оценки из 100, Возраст)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]
# Мы хотим отсортировать список таким образом, чтобы ученик с самыми высокими оценками находился в самом начале. В случае, если студенты имеют равные оценки, они должны быть отсортированы таким образом, чтобы младший участник пришел первым.
# Мы можем достичь такого типа сортировки с несколькими ключами, возвращая кортеж вместо числа.

# Два кортежа можно сравнить, сравнивая их элементы, начиная с первого. Если есть связь (элементы равны), то сравнивается второй элемент и так далее.
# >>> (1,3) > (1, 4)
# False
# >>> (1, 4) < (2,2)
# True
# >>> (1, 4, 1) < (2, 1)
# True

# Давайте используем эту логику для построения нашей логики сортировки.
def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list) # [('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]

# Приведенная выше программа может быть написана с помощью lambdaфункции следующим образом:
sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list) # [('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]





# Python classmethod(), property(), staticmethod(), super() later
# unnecessary built-in functions: ascii(), bin(), chr(), complex(), frozenset(), hash(), help(), hex(), id(), memoryview(), object(), oct(), ord(), format(), type(), repr(), open().
