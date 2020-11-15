# https://www.programiz.com/python-programming/methods/dictionary
# https://www.programiz.com/python-programming/methods/list
# https://www.programiz.com/python-programming/methods/set
# https://www.programiz.com/python-programming/methods/tuple
# https://www.programiz.com/python-programming/methods/string





############################################### Dictionary Methods ###############################################
################################################## dict.clear() ##################################################
# Метод clear() удаляет все элементы из словаря.
# Mетод clear() не принимает никаких параметров.
# Mетод clear() не возвращает никакого значения (returns None).
d = {1: "one", 2: "two"}
d.clear()
print('d =', d) # d = {}





################################################### dict.copy() ###################################################
# Метод copy() возвращает неглубокую копию словаря. Он не изменяет исходный словарь.
# Метод copy() не принимает никаких параметров.
original = {1:'one', 2:'two'}
new = original.copy()
print('Orignal: ', original) # Orignal:  {1: 'one', 2: 'two'}
print('New: ', new) # New:  {1: 'one', 2: 'two'}
# !!!!!!!!!!!!!! Разница в использовании метода copy() и оператора = для копирования словарей !!!!!!!!!!!!!!
# При copy() использовании метода создается новый словарь, который заполняется копией ссылок из исходного словаря.
# При = использовании оператора создается новая ссылка на исходный словарь.
# Пример 2: использование оператора = для копирования словарей
original = {1:'one', 2:'two'}
new = original
# removing all elements from the list
new.clear()
print('new: ', new) # new:  {}
print('original: ', original) # original:  {}
# Здесь, когда 'new' словарь очищается, 'original' словарь также очищается.
# Пример 3: Использование функции copy() для копирования словарей
original = {1:'one', 2:'two'}
new = original.copy()
# removing all elements from the list
new.clear()
print('new: ', new) # new:  {}
print('original: ', original) # original:  {1: 'one', 2: 'two'}
# Здесь, когда 'new' словарь очищается, 'original' словарь остается неизменным.





########################################### dictionary.fromkeys(sequence[, value]) ###########################################
# Метод fromkeys () создает новый словарь из заданной последовательности элементов со значением, предоставленным пользователем.
# fromkeys () принимает два параметра:
# sequence/последовательность - последовательность элементов, которая будет использоваться в качестве ключей для нового словаря
# value (Необязательно) - значение, которое устанавливается для каждого элемента словаря
# Возвращаемое значение из fromkeys ()
# fromkeys () метод возвращает новый словарь с заданной последовательностью элементов в качестве ключей словаря.
# Если аргумент значения установлен, каждый элемент вновь созданного словаря устанавливается на предоставленное значение.
# Пример 1. Создайте словарь из последовательности ключей.
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(keys)
print(vowels) # {'a': None, 'u': None, 'o': None, 'e': None, 'i': None}
# Пример 2: Создать словарь из последовательности ключей со значением
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels) # {'a': 'vowel', 'u': 'vowel', 'o': 'vowel', 'e': 'vowel', 'i': 'vowel'}
# Пример 3: Создать словарь из списка изменяемых объектов
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels) # {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}
# updating the value
value.append(2)
print(vowels) # {'a': [1, 2], 'u': [1, 2], 'o': [1, 2], 'e': [1, 2], 'i': [1, 2]}
# Если value является изменяемым объектом (значение которого может быть изменено), таким как список, словарь и т. Д., При изменении изменяемого объекта каждый элемент последовательности также обновляется.
# Это потому, что каждому элементу назначается ссылка на один и тот же объект (указывает на один и тот же объект в памяти).
# Чтобы избежать этой проблемы, мы используем понимание словаря.
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels) # {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}
# updating the value
value.append(2)
print(vowels) # {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}
# Здесь для каждого ключа в ключах создается и назначается новый список из значения.
# По сути, значение не присваивается элементу, но из него создается новый список, который затем присваивается каждому элементу в словаре.





################################################# dict.get(key[, value]) #################################################
# Метод get() возвращает значение для указанного ключа, если ключ находится в словаре.
# Метод get() принимает максимум два параметра:
# key - ключ для поиска в словаре
# value (необязательно) - значение, которое будет возвращено, если ключ не найден. Значение по умолчанию - None.
# get() метод возвращает:
# значение для указанного key, если key находится в словаре.
# None если key не найден и value не указан.
# value если key не найден и value указан.
person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name')) # Name:  Phill
print('Age: ', person.get('age')) # Age:  22
# value is not provided
print('Salary: ', person.get('salary')) # Salary:  None
# value is provided
print('Salary: ', person.get('salary', 0.0)) # Salary:  0.0

# Метод get() VS dict[key] для доступа к элементам
# get() метод возвращает значение по умолчанию, если key оно отсутствует.
# Однако , если key не найден при использовании dict[key], KeyError возникает исключение.
person = {}
# Using get() results in None
print('Salary:', person.get('salary')) # Salary: None
# Using [] results in KeyError
try: print(person['salary'])
except KeyError: print("""
Traceback (most recent call last):
  File "data_types_methods.py", line 126, in 
    print(person['salary'])
KeyError: 'salary'""")





################################################## dictionary.items() ##################################################
# Метод items() возвращает объект view/представления, который отображает список пар кортежей данного словаря (ключ, значение).
# Метод items() не принимает никаких параметров.
# Пример 1: получить все элементы словаря с элементами()
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items()) # dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
# Пример 2: Как работает функция items() при изменении словаря?
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
items = sales.items()
print('Original items:', items) # Original items: dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items) # Updated items: dict_items([('orange', 3), ('grapes', 4)])
# Элементы объекта представления сами по себе не возвращают список товаров для продажи, но возвращают представление пары продаж (ключ, значение).
# Если список обновляется в любое время, изменения отражаются на самом объекте view/представления, как показано в приведенной выше программе.





##################################################### dict.keys() #####################################################
# Метод keys() возвращает объект view/представления, который отображает список всех ключей в словаре.
# При изменении словаря объект представления также отражает эти изменения.
# Метод keys() не принимает никаких параметров.
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys()) # dict_keys(['name', 'salary', 'age'])
empty_dict = {}
print(empty_dict.keys()) # dict_keys([])
# Пример 2: Как работает keys() при обновлении словаря?
person = {'name': 'Phill', 'age': 22, }
print('Before dictionary is updated') # Before dictionary is updated
keys = person.keys()
print(keys) # dict_keys(['name', 'age'])
# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated') # After dictionary is updated
print(keys) # dict_keys(['name', 'age', 'salary'])
# Здесь, когда словарь обновляется, keys он также автоматически обновляется, чтобы отразить изменения.





################################################## dictionary.values() ##################################################
# Метод values() возвращает объект view/представления, который отображает список всех значений в словаре.
# Метод values() не принимает никаких параметров.
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.values()) # dict_values([2, 4, 3])

# Пример 2: Как работает функция values() при изменении словаря?
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
values = sales.values()
print('Original items:', values) # Original items: dict_values([2, 4, 3])
# delete an item from dictionary
del[sales['apple']]
print('Updated items:', values) # Updated items: dict_values([4, 3])
# Значения объекта view/представления сами по себе не возвращают список значений предметов продажи, но возвращают представление всех значений словаря.
# Если список обновляется в любое время, изменения отражаются на самом объекте view/представления, как показано в приведенной выше программе.





############################################# dictionary.pop(key[, default]) #############################################
# Метод pop() удаляет и возвращает элемент из словаря, имеющего заданный ключ.
# Метод pop() принимает два параметра:
# key - ключ, который нужно искать для удаления
# default/по умолчанию - значение, которое должно быть возвращено, если ключа нет в словаре
# Метод pop() возвращает:
# Если ключ найден - удален / выскочил элемент из словаря
# Если ключ не найден - значение указано как второй аргумент (default/по умолчанию)
# Если ключ не найден и аргумент по умолчанию не указан - возникает исключение KeyError

# Пример 1: извлеките элемент из словаря
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('apple')
print('The popped element is:', element) # The popped element is: 2
print('The dictionary is:', sales) # The dictionary is: {'orange': 3, 'grapes': 4}

# Пример 2: извлечь элемент, которого нет в словаре
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
try: element = sales.pop('guava') # KeyError: 'guava'
except KeyError: print("KeyError: 'guava'")

# Пример 3: Извлечь элемент, отсутствующий в словаре, при условии, что он имеет значение default/по умолчанию
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('guava', 'banana')
print('The popped element is:', element) # The popped element is: banana
print('The dictionary is:', sales) # The dictionary is: {'orange': 3, 'apple': 2, 'grapes': 4}





################################################## dict.popitem() ##################################################
# Метод popitem() удаляет и возвращает последнюю пару элементов (ключ, значение), вставленную в словарь.
# Метод popitem() не принимает никаких параметров.
# Возвращаемое значение из метода popitem ()
# Метод popitem () удаляет и возвращает пару (ключ, значение) из словаря в порядке «последний пришел - первый ушел» (LIFO).
# Возвращает последнюю вставленную пару элементов (ключ, значение) из словаря.
# Удаляет возвращенную пару элементов из словаря.
# Примечание. До Python 3.7 метод popitem () возвращал и удалял произвольную пару элементов (ключ, значение) из словаря.
# Примечание. Метод popitem() вызывает ошибку KeyError, если словарь пуст.
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()
print('Return Value = ', result) # Return Value =  ('salary', 3500.0)
print('person = ', person) # person =  {'name': 'Phill', 'age': 22}
# inserting a new element pair
person['profession'] = 'Plumber'
# now ('profession', 'Plumber') is the latest element
result = person.popitem()
print('Return Value = ', result) # Return Value =  ('profession', 'Plumber')
print('person = ', person) # person =  {'name': 'Phill', 'age': 22}





########################################### dict.setdefault(key[, default_value]) ###########################################
# Метод setdefault() возвращает значение ключа (если ключ находится в словаре). Если нет, он вставляет ключ со значением в словарь.
# setdefault () принимает максимум два параметра:
# key - ключ для поиска в словаре
# default_value (необязательно) - ключ со значением default_value вставляется в словарь, если ключа нет в словаре.
# Если не указан, default_value будет None.
# setdefault () возвращает:
# значение ключа, если оно есть в словаре
# None, если ключа нет в словаре и значение default_value не указано
# default_value, если ключ отсутствует в словаре и указано default_value

# Пример 1: Как работает setdefault (), когда ключ находится в словаре?
person = {'name': 'Phill', 'age': 22}
age = person.setdefault('age')
print('person = ',person) # person =  {'name': 'Phill', 'age': 22}
print('Age = ',age) # Age =  22

# Пример 2: Как работает setdefault (), когда ключа нет в словаре?
person = {'name': 'Phill'}
# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person) # person =  {'name': 'Phill', 'salary': None}
print('salary = ',salary) # salary =  None
# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person) # person =  {'name': 'Phill', 'age': 22, 'salary': None}
print('age = ',age) # age =  22





################################################## dict.update([other]) ##################################################
# Метод update() обновляет словарь элементами из другого объекта словаря или из итерируемых пар ключ / значение.
# Метод update() добавляет элемент (ы) в словарь, если ключ отсутствует в словаре. Если ключ находится в словаре, он обновляет ключ с новым значением.
# Параметры update()
# Метод update() принимает либо словарь, либо итерационный объект пар ключ/значение (обычно кортежи).
# Если update() вызывается без передачи параметров, то словарь остается неизменным.
# Возвращаемое значение из update ()
# update () обновляет словарь элементами из объекта словаря или повторяемого/итерационного объекта пар ключ / значение.
# Он не возвращает никакого значения (возвращает None).
d = {1: "one", 2: "three"}
d1 = {2: "two"}
# updates the value of key 2
d.update(d1)
print(d) # {1: 'one', 2: 'two'}
d1 = {3: "three"}
# adds element with key 3
d.update(d1)
print(d) # {1: 'one', 2: 'two', 3: 'three'}

# Пример 2: update () при передаче кортежа
d = {'x': 2}
d.update(y = 3, z = 0)
print(d) # {'x': 2, 'y': 3, 'z': 0}





##############################################################################################################################
##############################################################################################################################





###################################################### List Methods ######################################################
#################################################### list.append(item) ###################################################
# Метод append() добавляет элемент в конец списка.
# Метод append() не возвращает никакого значения (returns None).
# Метод append() принимает единственный аргумент:
# item - элемент, который нужно добавить в конец списка. Элементом могут быть числа, строки, словари, другой список и т.д.
# animals list
animals = ['cat', 'dog', 'rabbit']
# 'guinea pig' is appended to the animals list
animals.append('guinea pig')
# Updated animals list
print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'rabbit', 'guinea pig']

# Пример 2: Добавление списка в список
# animals list
animals = ['cat', 'dog', 'rabbit']
# list of wild animals
wild_animals = ['tiger', 'fox']
# appending wild_animals list to the animals list
animals.append(wild_animals)
print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'rabbit', ['tiger', 'fox']]
# Важно отметить, что в список animals/животных в приведенной выше программе добавляется один элемент (список wild_animals).
# Если вам нужно добавить элементы списка в другой список (а не в сам список), используйте метод extend().





###################################################### list.clear() #####################################################
# Метод clear() удаляет все элементы из списка.
# Метод clear() не принимает никаких параметров.
# Метод clear() не возвращает никакого значения.
# Defining a list
List = [{1, 2}, ('a'), ['1.1', '2.2']]
# clearing the list
List.clear()
print('List:', List) # List: []

# Пример 2: Очистка списка с помощью del
# Defining a list
List = [{1, 2}, ('a'), ['1.1', '2.2']]
# clearing the list
del List[:]
print('List:', List) # List: []





###################################################### list.copy() #####################################################
# Метод copy() возвращает неглубокую копию списка.
# Метод copy() не принимает никаких параметров.
# Метод copy() возвращает новый список. Он не изменяет исходный список.
# Список можно скопировать с помощью '=' оператора. Например,
old_list = [1, 2, 3]
new_list = old_list
# Проблема с копированием списков таким образом заключается в том , что если вы изменяете new_list, old_list то также изменяетесь.
# add an element to list
new_list.append('a')
print('New List:', new_list) # New List: [1, 2, 3, 'a']
print('Old List:', old_list) # Old List: [1, 2, 3, 'a']
# Однако если вам нужно, чтобы исходный список оставался неизменным при изменении нового списка, вы можете использовать этот copy() метод.
# mixed list
my_list = ['cat', 0, 6.7]
# copying a list
new_list = my_list.copy()
print('Copied List:', new_list) # Copied List: ['cat', 0, 6.7]
# Если вы измените new_list его в приведенном выше примере, my_list он не будет изменен.
# Пример 2: Копирование Списка С Использованием Синтаксиса Среза
# shallow copy using the slicing syntax
# mixed list
List = ['cat', 0, 6.7]
# copying a list using slicing
new_list = List[:]
# Adding an element to the new list
new_list.append('dog')
# Printing new and old list
print('Old List:', List) # Old List: ['cat', 0, 6.7]
print('New List:', new_list) # New List: ['cat', 0, 6.7, 'dog']





#################################################### list.count(element) ###################################################
# Метод count() возвращает количество раз, когда указанный элемент появляется в списке.
# Метод count() принимает один аргумент:
# element-элемент, подлежащий подсчету
# Метод count() возвращает количество раз element, появившихся в списке.
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count) # The count of i is: 2
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count) # The count of p is: 0

# Пример 2: подсчет элементов кортежа и списка внутри списка
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count) # The count of ('a', 'b') is: 2
# count element [3, 4]
count = random.count([3, 4])
# print count
print("The count of [3, 4] is:", count) # The count of [3, 4] is: 1





#################################################### list.extend(iterable) ###################################################
# Метод extend() добавляет все элементы итерируемого объекта (список, кортеж, строка и т.д.) в конец списка.
# Метод extend() изменяет исходный список. Он не возвращает никакого значения.
# Параметры extend():
# Как уже упоминалось, метод extend () принимает итерацию, такую как список, кортеж, строка и т.д.
# language list
language = ['French', 'English']
# another list of language
language1 = ['Spanish', 'Portuguese']
# appending language1 elements to language
language.extend(language1)
print('Language List:', language) # Language List: ['French', 'English', 'Spanish', 'Portuguese']

# Пример 2: добавить элементы кортежа и установить их в список
# language list
language = ['French']
# language tuple
language_tuple = ('Spanish', 'Portuguese')
# language set
language_set = {'Chinese', 'Japanese'}
# appending language_tuple elements to language
language.extend(language_tuple)
print('New Language List:', language) # New Language List: ['French', 'Spanish', 'Portuguese']
# appending language_set elements to language
language.extend(language_set)
print('Newer Language List:', language) # Newer Language List: ['French', 'Spanish', 'Portuguese', 'Japanese', 'Chinese']

# Другие способы расширения списка
# Вы также можете добавить в список все элементы итерации, используя:
# 1. the + operator
a = [1, 2]
b = [3, 4]
a += b # a = a + b
print('a =', a) # a = [1, 2, 3, 4]
# 2. the list slicing syntax
a = [1, 2]
b = [3, 4]
a[len(a):] = b
print('a =', a) # a = [1, 2, 3, 4]

# list.extend() VS list.append()
# Если вам нужно добавить элемент в конец списка, вы можете использовать метод append().
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)
# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1) # [1, 2, 3, 4]
# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2) # [1, 2, (3, 4)]





############################################## list.index(element, start, end) #############################################
# Метод index() возвращает индекс указанного элемента в списке.
# Если элемент не найден, возникает исключение ValueError.
# Примечание. Метод index() возвращает только первое вхождение соответствующего элемента.
# Метод index() может принимать не более трех аргументов:
# element - элемент для поиска
# start (необязательно) - начать поиск с этого индекса
# end (необязательно) - искать элемент до этого индекса
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index) # The index of e: 1
# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')
print('The index of i:', index) # The index of i: 2

# Пример 2: индекс элемента, отсутствующего в списке
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']
# index of'p' is vowels
try:
	index = vowels.index('p')
	print('The index of p:', index) # ValueError: 'p' is not in list
except ValueError: print("ValueError: 'p' is not in list")

# Пример 3: Работа index () с параметрами start и end
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index) # The index of e: 1
# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index) # The index of i: 6
# 'i' between 3rd and 5th index is searched
try:
	index = alphabets.index('i', 3, 5)   # Error!
	print('The index of i:', index) # ValueError: 'i' is not in list
except ValueError: print("ValueError: 'i' is not in list")





#################################################### list.insert(index, element) ###################################################
# Метод insert() вставляет элемент в список по указанному индексу.
# list.insert(index, element): Здесь element вставляется в список по index-у индексу. Все элементы после element смещены вправо.
# Метод insert() ничего не возвращает; возвращает None. Он только обновляет текущий список.
# Метод insert() принимает два параметра:
# index - индекс, в который нужно вставить элемент
# element - это элемент, который нужно вставить в список
# Notes:
# Если index равен 0, элемент вставляется в начало списка.
# Если индекс равен 3, элемент вставляется после 3-го элемента. Его позиция будет 4-й.
# vowel list
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')
print('Updated List:', vowel) # Updated List: ['a', 'e', 'i', 'o', 'u']

# Пример 2: вставка кортежа (как элемента) в список
mixed_list = [{1, 2}, [5, 6, 7]]
# number tuple
number_tuple = (3, 4)
# inserting a tuple to the list
mixed_list.insert(1, number_tuple)
print('Updated List:', mixed_list) # Updated List: [{1, 2}, (3, 4), [5, 6, 7]]





###################################################### list.pop(index) #####################################################
# Метод pop() удаляет элемент по данному индексу из списка и возвращает удаленный элемент.
# Метод pop () принимает единственный аргумент (index).
# Аргумент, передаваемый методу, не является обязательным. Если не передан, в качестве аргумента передается индекс по умолчанию -1 (индекс последнего элемента).
# Если индекс, переданный методу, находится за пределами диапазона, он выдает исключение IndexError: pop index out of range.
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value) # Return Value: French
# Updated List
print('Updated List:', languages) # Updated List: ['Python', 'Java', 'C++', 'C']

# Пример 2: pop () без индекса и для отрицательных индексов
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# remove and return the last item
print('When index is not passed:') # When index is not passed:
print('Return Value:', languages.pop()) # Return Value: C
print('Updated List:', languages) # Updated List: ['Python', 'Java', 'C++', 'Ruby']
# remove and return the last item
print('\nWhen -1 is passed:') # When -1 is passed:
print('Return Value:', languages.pop(-1)) # Return Value: Ruby
print('Updated List:', languages) # Updated List: ['Python', 'Java', 'C++']
# remove and return the third last item
print('\nWhen -3 is passed:') # When -3 is passed:
print('Return Value:', languages.pop(-3)) # Return Value: Python
print('Updated List:', languages) # Updated List: ['Java', 'C++']

# Если вам нужно удалить данный элемент из списка, вы можете использовать метод remove ().
# Кроме того, вы можете использовать delоператор для удаления элемента или фрагментов из списка .





################################################### list.remove(element) ##################################################
# Метод remove() удаляет первый совпадающий элемент (который передается в качестве аргумента) из списка.
# Метод remove () принимает один элемент в качестве аргумента и удаляет его из списка.
# Если элемент не существует, он выдает ValueError: list.remove (x): x not in list exception.
# Метод remove () не возвращает никакого значения (возвращает None).
# Если вам нужно удалить элементы на основе индекса (например, четвертый элемент), вы можете использовать метод pop().
# Кроме того, вы можете использовать оператор Python del для удаления элементов из списка.
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# 'rabbit' is removed
animals.remove('rabbit')
# Updated animals List
print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'guinea pig']

# Пример 2: Метод remove() в списке с повторяющимися элементами
# Если список содержит повторяющиеся элементы, remove()метод удаляет только первый совпадающий элемент.
# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
# 'dog' is removed
animals.remove('dog')
# Updated animals list
print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'guinea pig', 'dog']

# Пример 3: Удаление несуществующего элемента
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# Deleting 'fish' element
try:
	animals.remove('fish')
	# Updated animals List
	print('Updated animals list: ', animals)
except ValueError: 
	print("ValueError: animals.remove('fish'): 'fish' not in list exception.") # OUTPUT





###################################################### list.reverse() #####################################################
# Метод reverse() переворачивает элементы списка.
# Метод reverse() не принимает никаких аргументов.
# Метод reverse() не возвращает никакого значения. Он обновляет существующий список.
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems) # Original List: ['Windows', 'macOS', 'Linux']
# List Reverse
systems.reverse()
# updated list
print('Updated List:', systems) # Updated List: ['Linux', 'macOS', 'Windows']

# Пример 2: реверсирование списка с помощью оператора Slicing/Cреза
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems) # Original List: ['Windows', 'macOS', 'Linux']
# Reversing a list	
#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]
# updated list
print('Updated List:', reversed_list) # Updated List: ['Linux', 'macOS', 'Windows']

# Пример 3: доступ к элементам в обратном порядке
# Если вам нужно получить доступ к отдельным элементам списка в обратном порядке, лучше использовать встроенную функцию reversed().
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o) # Linux\nmacOS\nWindows





############################################## list.sort(key=..., reverse=...) #############################################
# Метод sort() сортирует элементы данного списка в определенном порядке возрастания или убывания.
# Метод sort() по умолчанию не требует дополнительных параметров. Однако у него есть два необязательных параметра:
# reverse - Если True, отсортированный список переворачивается (или сортируется в порядке убывания)
# key - функция, которая служит ключом для сравнения сортировок
# В качестве альтернативы вы также можете использовать встроенную функцию sorted() для той же цели.
# Примечание. Простейшее различие между sort () и sorted () заключается в следующем: sort () изменяет список напрямую и не возвращает никакого значения, тогда как sorted () не изменяет список и возвращает отсортированный список.
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort()
# print vowels
print('Sorted list:', vowels) # Sorted list: ['a', 'e', 'i', 'o', 'u']

# Пример 2: отсортировать список по убыванию
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort(reverse=True)
# print vowels
print('Sorted list (in Descending):', vowels) # Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']

# Пример 3: сортировка списка с помощью ключа
# take second element for sort
def takeSecond(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key=takeSecond)
# print list
print('Sorted list:', random) # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

# Возьмем другой пример (Пример 4). Предположим, у нас есть список информации о сотрудниках офиса, где каждый элемент является словарем.
# Мы можем отсортировать список следующим образом:
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')
def get_age(employee):
    return employee.get('age')
def get_salary(employee):
    return employee.get('salary')
# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n') # [{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]
# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n') # [{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]
# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n') # [{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]

# Здесь, в первом случае, наша пользовательская функция возвращает имя каждого сотрудника. Поскольку имя string, Python по умолчанию сортирует его в алфавитном порядке.
# Во втором случае возвращается функция age (int), которая сортируется в порядке возрастания.
# В третьем случае функция возвращает зарплату (int) и сортируется в порядке убывания с помощью reverse = True.
# Хорошей практикой является использование лямбда-функции, когда она может быть суммирована в одной строке. Таким образом, мы также можем написать приведенную выше программу следующим образом:
# sort by name (Ascending order)
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n') # [{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]
# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n') # [{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]
# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n') # [{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]





##############################################################################################################################
##############################################################################################################################





####################################################### Set Methods ##########################################################
##################################################### set.add(element) #######################################################
# Метод add() добавляет заданный элемент в набор. Если элемент уже присутствует, он не добавляет никаких элементов.
# Метод add() не возвращает никакого значения и возвращает None.
# Метод add() принимает один параметр:
# element-элемент, который добавляется в набор
# set of vowels
vowels = {'a', 'e', 'i', 'u'}
# adding 'o'
vowels.add('o')
print('Vowels are:', vowels) # Vowels are: {'a', 'i', 'o', 'u', 'e'}
# adding 'a' again
vowels.add('a')
print('Vowels are:', vowels) # Vowels are: {'a', 'i', 'o', 'u', 'e'}
# Примечание. Порядок гласных может быть разным.

# Пример 2: Добавить tuple/кортеж в set/набор
# Вы также можете добавить кортежи в набор. И как обычные элементы, вы можете добавить один и тот же кортеж только один раз.
# set of vowels
vowels = {'a', 'e', 'u'}
# a tuple ('i', 'o')
tup = ('i', 'o')
# adding tuple
vowels.add(tup)
print('Vowels are:', vowels) # Vowels are: {('i', 'o'), 'e', 'u', 'a'}
# adding same tuple again
vowels.add(tup)
print('Vowels are:', vowels) # Vowels are: {('i', 'o'), 'e', 'u', 'a'}





####################################################### set.clear() ######################################################### 
# Метод clear() удаляет все элементы из набора.
# Метод clear() не принимает никаких параметров.
# Метод clear() не возвращает никакого значения и возвращает None.
# set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
print('Vowels (before clear):', vowels) # Vowels (before clear): {'e', 'a', 'o', 'u', 'i'}
# clearing vowels
vowels.clear()
print('Vowels (after clear):', vowels) # Vowels (after clear): set()





####################################################### set.copy() #########################################################
# Метод copy() возвращает неглубокую копию набора.
# Метод copy() не принимает никаких параметров.
numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()
new_numbers.add(5)
print('numbers: ', numbers) # numbers:  {1, 2, 3, 4}
print('new_numbers: ', new_numbers) # new_numbers:  {1, 2, 3, 4, 5}

# Набор также может быть скопирован с помощью '=' оператора. Например:
numbers = {1, 2, 3, 4}
new_numbers = numbers
# Проблема с копированием набора таким образом заключается в том, что если вы изменяете numbers набор, new_numbers то он также изменяется.
numbers = {1, 2, 3, 4}
new_numbers = numbers
new_numbers.add(5)
print('numbers: ', numbers) # numbers:  {1, 2, 3, 4, 5}
print('new_numbers: ', new_numbers) # new_numbers:  {1, 2, 3, 4, 5}
# Однако если вам нужно, чтобы исходный набор оставался неизменным при изменении нового набора, вы можете использовать метод copy().





################################################### set1.difference(set2) ######################################################
# Метод difference () возвращает разницу между двумя наборами, которая также является набором. Не изменяет оригинальные наборы.
set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'f', 'g'}
# Equivalent to A-B
print(set1.difference(set2)) # {'b', 'a', 'd'}
# Equivalent to B-A
print(set2.difference(set1)) # {'g', 'f'}

# Вы также можете найти разницу набора с помощью '-' оператора.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}
print(A-B) # {'b', 'd', 'a'} 
print(B-A) # {'f', 'g'}





############################################### set1.difference_update(set2) #################################################
# Функция difference_update() обновляет набор, вызывающий метод difference_update(), с помощью разности наборов.
# Предположим,
# result = set1.difference_update(set2)
# Когда вы запускаете код,
# result будет None
# set1 будет равно set1-set2
# set2 будет без изменений
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
result = A.difference_update(B)
print('A = ', A) # A =  {'d', 'a'}
print('B = ', B) # B =  {'c', 'g', 'f'}
print('result = ', result) # result =  None





######################################################## set.discard(x) #######################################################
# Метод discard() принимает единственный элемент 'x' и удаляет его из набора (если он присутствует). Mетод возвращает None
numbers = {2, 3, 4, 5}
numbers.discard(3)
print('numbers = ', numbers) # numbers =  {2, 4, 5}
numbers.discard(10)
print('numbers = ', numbers) # numbers =  {2, 4, 5}
print(numbers.discard(3)) # None





################################################ set1.intersection(*other_sets) ###############################################
# Метод intersection() возвращает новый набор с элементами, общими для всех наборов.
# Метод intersection() допускает произвольное количество аргументов (наборов).
# Метод intersection() возвращает пересечение множества set1 со всеми множествами (передается в качестве аргумента).
# Если аргумент не передается в intersection(), он возвращает неглубокую копию set(set1).
A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}
print(B.intersection(A)) # {2, 5}
print(B.intersection(C)) # {2}
print(A.intersection(C)) # {2, 3}
print(C.intersection(A, B)) # {2}
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}
print(A.intersection(D)) # {100}
print(B.intersection(D)) # {200}
print(C.intersection(D)) # {300}
print(A.intersection(B, C, D)) # set()

# Вы также можете найти пересечение множеств с помощью '&' оператора.
# Пример 3: Установите пересечение с помощью оператора '&' 
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3, 7}
D = {100, 200, 300}
print(A & C) # {7}
print(A & D) # {100}
print(A & C & D) # set()
print(A & B & C & D) # set()





############################################## set1.intersection_update(*other_sets) ##############################################
# Метод intersection_update() обновляет набор, вызывающий метод intersection_update(), с пересечением наборов. Этот метод возвращает None
# Метод intersection_update() допускает произвольное количество аргументов (множеств).
# Например:
# result = A.intersection_update(B, C)
# Когда вы запускаете код,
# result будет None
# A будет равно пересечению A, B, и C
# B оставаться прежней
# C оставаться прежней
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
result = A.intersection_update(B)
print('result =', result) # result = None
print('A =', A) # A = {2, 3, 4}
print('B =', B) # B = {2, 3, 4, 5}

# Пример 2: intersection_update() с двумя параметрами
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}
result = C.intersection_update(B, A)
print('result =', result) # result = None
print('C =', C) # C = {4}
print('B =', B) # B = {2, 3, 4, 5, 6}
print('A =', A) # A = {1, 2, 3, 4}





####################################################### set1.isdisjoint(set2) #######################################################
# Метод isdisjoint() возвращает True, если два набора не пересекаются. Если нет, возвращается False.
# Метод isdisjoint() принимает единственный аргумент (set/набор).
# Вы также можете передать итерацию (список, кортеж, словарь и строку) в disjoint (). isdisjoint () автоматически преобразует итерируемые объекты в набор и проверяет, являются ли наборы непересекающимися.
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
print('Are A and B disjoint?', A.isdisjoint(B)) # Are A and B disjoint? True
print('Are A and C disjoint?', A.isdisjoint(C)) # Are A and C disjoint? False
A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D ={1 : 'a', 2 : 'b'}
E ={'a' : 1, 'b' : 2}
print('Are A and B disjoint?', A.isdisjoint(B)) # Are A and B disjoint? False
print('Are A and C disjoint?', A.isdisjoint(C)) # Are A and C disjoint? False
print('Are A and D disjoint?', A.isdisjoint(D)) # Are A and D disjoint? True
print('Are A and E disjoint?', A.isdisjoint(E)) # Are A and E disjoint? False





######################################################## set1.issubset(set2) ########################################################
# Метод issubset() возвращает True, если все элементы набора присутствуют в другом наборе (переданном в качестве аргумента). Если нет, возвращается False.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B)) # True
# B не является подмножеством A
print(B.issubset(A)) # False
print(A.issubset(C)) # False
print(C.issubset(B)) # True
# Если вам нужно проверить, является ли набор надмножеством другого набора, вы можете использовать issueperset().





####################################################### set1.issuperset(set2) #######################################################
# Метод Issueperset() возвращает True, если набор содержит все элементы другого набора (переданного в качестве аргумента). Если нет, возвращается False.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
print(A.issuperset(B)) # True
print(B.issuperset(A)) # False
print(C.issuperset(B)) # True
# Если вам нужно проверить, является ли набор подмножеством другого набора, вы можете использовать issubset() в Python.





############################################################# set.pop() #############################################################
# Метод pop() удаляет произвольный(случайный) элемент из набора и возвращает удаленный элемент. Если набор пуст, возникает исключение TypeError.
# Метод pop() не принимает аргументов.
A ={'a', 'b', 'c', 'd'}
print('Return Value is', A.pop()) # Return Value is d
print('A = ', A) # A =  {'a', 'b', 'c'}
# Примечание. Вы можете получить другой результат, так как pop() возвращает и удаляет случайный элемент.





######################################################## set.remove(element) ########################################################
# Метод remove() принимает один элемент в качестве аргумента и удаляет его из набора и обновляет набор. Он не возвращает никакого значения.
# Если элемент, переданный в remove(), не существует, создается исключение KeyError.
# language set
language = {'English', 'French', 'German'}
# removing 'German' from language
language.remove('German')
# Updated language set
print('Updated language set:', language) # Updated language set: {'English', 'French'}

# Пример 2: Удаление несуществующего элемента
# animal set
animal = {'cat', 'dog', 'rabbit', 'guinea pig'}
# Deleting 'fish' element
try:
	animal.remove('fish')
	# Updated animal
	print('Updated animal set:', animal)
except KeyError:
	print("KeyError: 'fish'")
# Вы можете использовать метод discard(), если вам не нужна эта ошибка.
# Метод discard() удаляет указанный элемент из набора. Однако, если элемент не существует, набор остается неизменным; вы не получите ошибки.





################################################## set1.symmetric_difference(set2) ##################################################
# Метод symric_difference() возвращает симметричную разность двух наборов.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}
print(A.symmetric_difference(B)) # {'b', 'a', 'e'}
print(B.symmetric_difference(A)) # {'b', 'e', 'a'}
print(A.symmetric_difference(C)) # {'b', 'd', 'c', 'a'}
print(B.symmetric_difference(C)) # {'d', 'e', 'c'}

# Mы также можем найти симметричную разницу с помощью оператора '^'.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
print(A ^ B) # {'e', 'a', 'b'}
print(B ^ A) # {'e', 'a', 'b'}
print(A ^ A) # set()
print(B ^ B) # set()





############################################## set1.symmetric_difference_update(set2) ##############################################
# Метод symmetric_difference_update() находит симметричную разность двух наборов и обновляет набор, вызывающий его.
# Метод symmetric_difference_update() возвращает None (ничего не возвращает). Скорее, он обновляет вызывающий его набор.
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }
result = A.symmetric_difference_update(B)
print('A =', A) # A = {'a', 'e'}
print('B =', B) # B = {'d', 'c', 'e'}
print('result =', result) # result = None
# Здесь набор A обновляется с симметричной разностью наборов A и B. Однако набор B не изменяется.





##################################################### set1.union(*other_sets) #####################################################
# Метод union() возвращает новый набор с различными элементами из этого набора и всех других наборов (передаваемых в качестве аргумента).
# Если аргумент не передается union(), он возвращает неглубокую копию набора.
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}
print('A U B =', A.union(B)) # A U B = {2, 'a', 'd', 'c'}
print('B U C =', B.union(C)) # B U C = {1, 2, 3, 'd', 'c'}
print('A U B U C =', A.union(B, C)) # A U B U C = {1, 2, 3, 'a', 'd', 'c'}
print('A.union() =', A.union()) # A.union() = {'a', 'd', 'c'}

# Вы также можете найти объединение множеств с помощью '|' оператора.
# Пример 2: установите объединение с помощью оператора '|'
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}
print('A U B =', A | B) # A U B = {2, 'a', 'c', 'd'}
print('B U C =', B | C) # B U C = {1, 2, 3, 'c', 'd'}
print('A U B U C =', A | B | C) # A U B U C = {1, 2, 3, 'a', 'c', 'd'}





###################################### set.update(iterable)/set.update(iter1, iter2, iter3) ######################################
# Метод update() обновляет набор, добавляя элементы из других итераций.
# Метод update() возвращает None (ничего не возвращает).
A = {'a', 'b'}
B = {1, 2, 3}
result = A.update(B)
print('A =', A) # A = {'a', 1, 2, 3, 'b'}
print('result =', result) # result = None

# Пример 2: Добавить элементы строки и словаря в set
string_alphabet = 'abc'
numbers_set = {1, 2}
# add elements of the string to the set
numbers_set.update(string_alphabet)
print('numbers_set =', numbers_set) # numbers_set = {'c', 1, 2, 'b', 'a'}
info_dictionary = {'key': 1, 'lock' : 2}
numbers_set = {'a', 'b'}
# add keys of dictionary to the set
numbers_set.update(info_dictionary)
print('numbers_set =', numbers_set) # numbers_set = {'key', 'b', 'lock', 'a'}
# Примечание. Если словари передаются в метод update(), ключи словарей добавляются в набор.





##################################################################################################################################
##################################################################################################################################





########################################################## Tuple Methods ##########################################################
####################################################### tuple.count(element) ######################################################
# Метод count() возвращает количество раз, когда указанный элемент встречается в кортеже.
# Метод count() принимает единственный аргумент: element - элемент для подсчета
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count) # The count of i is: 2
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count) # The count of p is: 0

# Пример 2: подсчет списка и элементов кортежа внутри кортежа
# random tuple
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count) # The count of ('a', 'b') is: 2
# count element [3, 4]
count = random.count([3, 4])
# print count
print("The count of [3, 4] is:", count) # The count of [3, 4] is: 1





################################################# tuple.index(element, start, end) #################################################
# Метод index() возвращает индекс указанного элемента в кортеже.
# Метод index() может принимать не более трех аргументов:
# element - элемент для поиска
# start (необязательно) - начать поиск с этого индекса
# end (необязательно) - искать элемент до этого индекса
# Метод index() возвращает индекс данного элемента в кортеже.
# Если элемент не найден, возникает исключение ValueError.
# Примечание. Метод index() возвращает только первое вхождение соответствующего элемента.
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index) # The index of e: 1
# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')
print('The index of i:', index) # The index of e: 2

# Пример 2: индекс элемента, отсутствующего в кортеже
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'u')
try:
	# index of 'p' in vowels
	index = vowels.index('p')
	print('The index of p:', index)
except ValueError: 
	print("ValueError: vowels.index('p'): 'p' not in tuple")

# Пример 3: index() с параметрами start и end
# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')
# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index) # The index of e: 1
# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index) # The index of i: 6
try:
	# 'i' between 3rd and 5th index is searched
	index = alphabets.index('i', 3, 5) # Error!
	print('The index of i:', index)
except ValueError:
	print("ValueError: alphabets.index('i', 3, 5): 'i' not in tuple")





##################################################################################################################################
##################################################################################################################################





######################################################### String Methods #########################################################
# unnecessary string methods: maketrans(), translate()
# necessary string methods: encode, format, format_map, join
def func0():
	########################################## str.encode(encoding='UTF-8',errors='strict') ##########################################
	# Метод encode() возвращает закодированную версию данной строки.
	# По умолчанию метод encode() не требует никаких параметров.
	# Он возвращает версию строки в кодировке utf-8. В случае сбоя возникает исключение UnicodeDecodeError.
	# Однако он принимает два параметра:
	# encoding/кодировка - тип кодировки, в который должна быть закодирована строка
	# errors/ошибки - ответ при сбое кодирования. Есть шесть типов реакции на ошибку
	# strict - ответ по умолчанию, который вызывает исключение UnicodeDecodeError при сбое
	# ignore - игнорирует некодируемый юникод из результата
	# replace - заменяет некодируемый юникод на вопросительный знак?
	# xmlcharrefreplace - вставляет ссылку на символ XML вместо некодируемого юникода
	# backslashreplace - вставляет escape-последовательность \ uNNNN вместо некодируемого юникода
	# namereplace - вставляет escape-последовательность \ N {...} вместо некодируемого юникода
	# Пример 1: кодирование в кодировку Utf-8 по умолчанию
	# unicode string
	string = 'pythön!'
	# print string
	print('The string is:', string) # The string is: pythön!
	# default encoding to utf-8
	string_utf = string.encode()
	# print result
	print('The encoded version is:', string_utf) # The encoded version is: b'pyth\xc3\xb6n!'

	# Пример 2: Кодирование с параметром errors/ошибки
	# unicode string
	string = 'pythön!'
	# print string
	print('The string is:', string) # The string is: pythön!
	# ignore error
	print('The encoded version (with ignore) is:', string.encode("ascii", "ignore")) # The encoded version (with ignore) is: b'pythn!'
	# replace error
	print('The encoded version (with replace) is:', string.encode("ascii", "replace")) # The encoded version (with replace) is: b'pyth?n!'
	# xmlcharrefreplace error
	print('The encoded version (with xmlcharrefreplace) is:', string.encode("ascii", "xmlcharrefreplace")) # The encoded version (with xmlcharrefreplace) is: b'pyth&#246;n!'
	# backslashreplace error
	print('The encoded version (with backslashreplace) is:', string.encode("ascii", "backslashreplace")) # The encoded version (with backslashreplace) is: b'pyth\\xf6n!'
	# namereplace error
	print('The encoded version (with namereplace) is:', string.encode("ascii", "namereplace")) # The encoded version (with namereplace) is: b'pyth\\N{LATIN SMALL LETTER O WITH DIAERESIS}n!'





	################################################### Python String format() ###################################################
	# default arguments
	print("Hello {}, your balance is {}.".format("Adam", 230.2346)) # Hello Adam, your balance is 230.2346.
	# positional arguments
	print("Hello {0}, your balance is {1}.".format("Adam", 230.2346)) # Hello Adam, your balance is 230.2346.
	# keyword arguments
	print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346)) # Hello Adam, your balance is 230.2346.
	# mixed arguments
	print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346)) # Hello Adam, your balance is 230.2346.

	# define Person class
	class Person:
	    age = 23
	    name = "Adam"
	print("{p.name}'s age is: {p.age}".format(p=Person())) # Adam's age is: 23

	# define Person dictionary
	person = {'age': 23, 'name': 'Adam'}
	print("{p[name]}'s age is: {p[age]}".format(p=person)) # Adam's age is: 23

	# define Person dictionary
	person = {'age': 23, 'name': 'Adam'}
	print("{name}'s age is: {age}".format(**person)) # Adam's age is: 23

	# datetime formatting
	import datetime
	date = datetime.datetime.now()
	print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date)) # It's now: 2016/12/02 04:16:28

	# custom __format__() method
	class Person:
		def __format__(self, format):
			if(format == 'age'):
				return '23'
			return 'None'
	print("Adam's age is: {:age}".format(Person())) # Adam's age is: 23

	# __str__() and __repr__() shorthand !r and !s
	print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat")) # Quotes: 'cat', Without Quotes: cat
	# __str__() and __repr__() implementation for class
	class Person:
		def __str__(self):
			return "STR"
		def __repr__(self):
			return "REPR"
	print("repr: {p!r}, str: {p!s}".format(p=Person())) # repr: REPR, str: STR





	################################################## str.format_map(mapping) ##################################################
	# Метод format_map() похож на str.format(**mapping), за исключением того, что str.format(**mapping) создает новый словарь, а str.format_map(mapping) - нет.
	# Метод format_map() более гибкий, чем str.format(**mapping), так как у вас могут отсутствовать ключи.
	# Метод format_map() принимает один аргумент mapping(dictionary).
	# Метод format_map() форматирует данную строку и возвращает ее.
	# Example #1 str.format(**mapping)
	point = {'x':4,'y':-5}
	print('{x} {y}'.format(**point)) # 4 -5

	# Example #2 str.format_map(mapping)
	point = {'x':4,'y':-5}
	print('{x} {y}'.format_map(point)) # 4 -5
	point = {'x':4,'y':-5, 'z': 0}
	print('{x} {y} {z}'.format_map(point)) # 4 -5 0

	# Пример 2: Как format_map () работает с подклассом dict?
	class Coordinate(dict):
	    def __missing__(self, key):
	      return key
	print('({x}, {y})'.format_map(Coordinate(x='6'))) # (6, y)
	print('({x}, {y})'.format_map(Coordinate(y='5'))) # (x, 5)
	print('({x}, {y})'.format_map(Coordinate(x='6', y='5'))) # (6, 5)





	############################################### str.join(iterable) 3##############################################
	# Метод join() возвращает строку, соединяя все элементы итератора, разделенные строковым разделителем.
	# Метод join() предоставляет гибкий способ создания строк из повторяемых объектов. Он объединяет каждый элемент итерации (например, список, строку и кортеж) с помощью разделителя строк (строки, для которой вызывается метод join()) и возвращает объединенную строку.
	# Метод join () принимает в качестве параметра итерацию (объекты, способные возвращать свои члены по одному).
	# Вот некоторые из примеров итераций:
	# Собственные типы данных - список, кортеж, строка, словарь и набор.
	# Файловые объекты и объекты, которые вы определяете с помощью метода __iter __ () или __getitem () __.
	# Если итерируемый объект содержит какие-либо не строковые значения, он вызывает исключение TypeError.
	# .join() with lists
	numList = ['1', '2', '3', '4']
	separator = ', '
	print(separator.join(numList)) # 1, 2, 3, 4
	# .join() with tuples
	numTuple = ('1', '2', '3', '4')
	print(separator.join(numTuple)) # 1, 2, 3, 4
	s1 = 'abc'
	s2 = '123'
	# each element of s2 is separated by s1
	# '1'+ 'abc'+ '2'+ 'abc'+ '3'
	print('s1.join(s2):', s1.join(s2)) # s1.join(s2): 1abc2abc3
	# each element of s1 is separated by s2
	# 'a'+ '123'+ 'b'+ '123'+ 'b'
	print('s2.join(s1):', s2.join(s1)) # s2.join(s1): a123b123c

	# Пример 2: метод join() с множествами/sets
	# .join() with sets
	test = {'2', '1', '3'}
	s = ', '
	print(s.join(test)) # 2, 3, 1
	test = {'Python', 'Java', 'Ruby'}
	s = '->->'
	print(s.join(test)) # Python->->Ruby->->Java
	# Примечание. Набор/Set - это неупорядоченный набор элементов, поэтому вы можете получить другой результат (порядок случайный).

	# Пример 3: метод join() со словарями/dict
	# .join() with dictionaries
	test = {'mat': 1, 'that': 2}
	s = '->'
	# joins the keys only
	print(s.join(test)) # mat->that
	test = {1: 'mat', 2: 'that'}
	s = ', '
	# this gives error since key isn't string
	try: print(s.join(test)) # ERROR!!!
	except TypeError: print("TypeError: sequence item 0: expected str instance, int found")
	# Метод join() пытается соединить ключи (не значения) словаря с помощью разделителя строк.
	# Примечание. Если ключ строки не является строкой, возникает исключение TypeError.

# String find, rfind, index, rindex, ljust, rjust, partition, rpartition, strip, rstrip methods
def func1():
	############################################### str.find(sub[, start[, end]] ) ###############################################
	# Метод find() возвращает наименьший индекс подстроки внутри строки.
	# Метод find() принимает максимум три параметра:
	# sub - это подстрока, которую нужно искать в строке str.
	# start и end (необязательно) - диапазон str [start: end], в котором ищется подстрока.
	# Метод find() возвращает целочисленное значение:
	# Если подстрока существует внутри строки, она возвращает наименьший индекс первого появления подстроки.
	# Если подстроки не существует внутри строки, возвращается -1.
	quote = 'Let it be, let it be, let it be'
	# first occurance of 'let it'(case sensitive)
	result = quote.find('let it')
	print("Substring 'let it':", result) # Substring 'let it': 11
	# find returns -1 if substring not found
	result = quote.find('small')
	print("Substring 'small ':", result) # Substring 'small ': -1
	# How to use find()
	if (quote.find('be,') != -1):
		print("Contains substring 'be,'") # Contains substring 'be,'
	else:
		print("Doesn't contain substring")

	# Пример 2: find() с аргументами start и end
	quote = 'Do small things with great love'
	# Substring is searched in 'hings with great love'
	print(quote.find('small things', 10)) # -1
	# Substring is searched in ' small things with great love' 
	print(quote.find('small things', 2)) # 3
	# Substring is searched in 'hings with great lov'
	print(quote.find('o small ', 10, -1)) # -1
	# Substring is searched in 'll things with'
	print(quote.find('things ', 6, 20)) # 9





	########################################## str.rfind(sub[, start[, end]] ) ##########################################
	# Метод rfind() точно похож на метода find().
	# Единственное отличие состоит в том, что find() возвращает наименьший индекс подстроки внутри строки. А rfind() возвращает наивысший индекс подстроки внутри строки
	# Если подстрока не найдена, обе метода возвращает -1
	# Метод rfind() принимает те же три параметра метода find()
	# Example #1: rfind() With No start and end Argument
	quote = 'Let it be, let it be, let it be'
	result = quote.rfind('let it')
	print("Substring 'let it':", result) # Substring 'let it': 22
	result = quote.rfind('small')
	print("Substring 'small ':", result) # Substring 'small ': -1
	result = quote.rfind('be,')
	# returns "Contains substring 'be,'"
	if (result != -1):
		print("Highest index where 'be,' occurs:", result)
	else:
		print("Doesn't contain substring")

	# Example #2: rfind() With start and end Arguments
	quote = 'Do small things with great love'
	# Substring is searched in 'hings with great love'
	print(quote.rfind('things', 10)) # -1
	# Substring is searched in ' small things with great love' 
	print(quote.rfind('t', 2)) # 25
	# Substring is searched in 'hings with great lov'
	print(quote.rfind('o small ', 10, -1)) # -1
	# Substring is searched in 'll things with'
	print(quote.rfind('th', 6, 20)) # 18





	############################################## str.index(sub[, start[, end]] ) ##############################################
	# Метод index() возвращает наименьший индекс подстроки внутри строки (если она найдена). Если подстрока не найдена, возникает исключение ValueError.
	# Метод index() принимает три параметра:
	# sub - подстрока для поиска в строке str.
	# start и end (необязательно) - поиск подстроки выполняется в str[start: end]
	# Метод index() похож на метод find() для строк.
	# Единственное отличие состоит в том, что метод find() возвращает -1, если подстрока не найдена, тогда как index() выдает исключение.
	sentence = 'Python programming is fun.'
	result = sentence.index('is fun')
	print("Substring 'is fun':", result) # Substring 'is fun': 19
	try:
		result = sentence.index('Java')
		print("Substring 'Java':", result) # Error!
	except ValueError: print("ValueError: substring not found")

	# Пример 2: index() с аргументами start и end
	sentence = 'Python programming is fun.'
	# Substring is searched in 'gramming is fun.'
	print(sentence.index('ing', 10)) # 15
	# Substring is searched in 'gramming is '
	print(sentence.index('g is', 10, -4)) # 17
	# Substring is searched in 'programming'
	try: print(sentence.index('fun', 7, 18)) # Error!
	except ValueError: print("ValueError: substring not found")





	############################################### str.rindex(sub[, start[, end]] ) ##############################################
	# Метод rindex() точно похож на метода index().
	# Единственное отличие состоит в том, что index() возвращает наименьший индекс подстроки внутри строки. А rindex() возвращает наивысший индекс подстроки внутри строки
	# Если подстрока не найдена, возникает исключение ValueError как в методе index() и также в методе rindex()
	# Метод rindex() принимает те же три параметра метода index()
	# Метод rindex() похож на метод rfind() для строк.
	# Единственное отличие состоит в том, что метод rfind() возвращает -1, если подстрока не найдена, тогда как rindex() выдает исключение.

	# Example #1:
	quote = 'Let it be, let it be, let it be'
	result = quote.rindex('let it')
	print("Substring 'let it':", result) # Substring 'let it': 22
	try:
		result = quote.rindex('small') # ERROR!!!
		print("Substring 'small ':", result)
	except ValueError: print("ValueError: substring not found")

	# Example #2
	quote = 'Do small things with great love'
	# Substring is searched in ' small things with great love' 
	print(quote.rindex('t', 2)) # 25
	# Substring is searched in 'll things with'
	print(quote.rindex('th', 6, 20)) # 18
	# Substring is searched in 'hings with great lov'
	try: print(quote.rindex('o small ', 10, -1)) # ERROR!!!
	except ValueError: print("ValueError: substring not found")




	########################################### str.ljust(width[, fillchar]) ###########################################
	# Метод ljust() возвращает строку с выравниванием по левому краю заданной минимальной ширины.
	# Метод ljust() принимает два параметра:
	# width - ширина данной строки. Если ширина меньше или равна длине строки, возвращается исходная строка.
	# fillchar(Необязательно) - символ для заполнения оставшегося места по ширине
	# example string
	string = 'cat'
	width = 5
	# print left justified string
	print(string.ljust(width)) # cat  
	# Здесь задана минимальная ширина 5. Итак, результирующая строка имеет минимальную длину 5.
	# Строка cat выровнена по левому краю, что оставляет два пробела справа от слова.
	# example string
	string = 'cat'
	width = 5
	fillchar = '*'
	# print left justified string
	print(string.ljust(width, fillchar)) # cat**
	# Здесь строка cat выровнена по левому краю, а оставшиеся два пробела справа заполнены символом '*'.





	########################################### string.rjust(width[, fillchar]) ###########################################
	# Метод rjust() точно похож на метода ljust().
	# Единственное отличие состоит в том, что метод ljust() возвращает строку с выравниванием по левому краю(l-left, ljust=left+just) заданной минимальной ширины. А rjust() возвращает строку с выравниванием по правому краю(r-right, rjust=right+just) заданной минимальной ширины
	# Метод rjust() принимает те же три параметра метода ljust()
	# Объяснение того, как работают эти два метода, одинаково
	# example string
	string = 'cat'
	width = 5
	# print right justified string
	print(string.rjust(width)) #   cat
	# example string
	string = 'cat'
	width = 5
	fillchar = '*'
	# print right justified string
	print(string.rjust(width, fillchar)) # **cat





	################################################ str.lstrip([chars]) ################################################
	# Метод lstrip() возвращает копию строки с удаленными ведущими символами (на основе переданного строкового аргумента).
	# Метод lstrip() удаляет символы слева на основе аргумента (строка, определяющая набор символов, которые необходимо удалить).
	# lstrip() Параметры:
	# chars (необязательно) - строка, определяющая набор символов, которые нужно удалить.
	# Если аргумент chars не указан, все начальные пробелы удаляются из строки.
	# Возвращаемое значение из lstrip():
	# lstrip() возвращает копию строки с удаленными начальными символами.
	# Все комбинации символов в аргументе chars удаляются из левой части строки до первого несоответствия.
	random_string = '   this is good '
	# Leading whitepsace are removed
	print(random_string.lstrip()) # this is good 
	# Argument doesn't contain space
	# No characters are removed.
	print(random_string.lstrip('sti')) #    this is good 
	print(random_string.lstrip('s ti')) # his is good 
	website = 'https://www.programiz.com/'
	print(website.lstrip('htps:/.')) # www.programiz.com/





	################################################ str.rstrip([chars]) ################################################





	############################################# str.partition(separator) ##############################################
	# Метод partition() разбивает строку при первом вхождении строки аргумента и возвращает кортеж, содержащий часть перед разделителем, строку аргумента и часть после разделителя.
	# Метод partition() принимает строковый параметр separator, который разделяет строку при первом ее появлении.
	string = "Python is fun"
	# 'is' separator is found
	print(string.partition('is ')) # ('Python ', 'is ', 'fun')
	# 'not' separator is not found
	print(string.partition('not ')) # ('Python is fun', '', '')
	string = "Python is fun, isn't it"
	# splits at first occurence of 'is'
	print(string.partition('is')) # ('Python ', 'is', " fun, isn't it")





	############################################# str.rpartition(separator) #############################################
	# Метод rpartition() разбивает строку в последнем вхождении строки аргумента и возвращает кортеж, содержащий часть перед разделителем, строку аргумента и часть после разделителя.
	# Метод rpartition() принимает строковый параметр separator, который разделяет строку при первом ее появлении.
	string = "Python is fun"
	# 'is' separator is found
	print(string.rpartition('is ')) # ('Python ', 'is ', 'fun')
	# 'not' separator is not found
	print(string.rpartition('not ')) # ('', '', 'Python is fun')
	string = "Python is fun, isn't it"
	# splits at last occurence of 'is'
	print(string.rpartition('is')) # ('Python is fun, ', 'is', "n't it")

# String lower, upper, swapcase methods
def func2():
	#################################################### str.lower() ####################################################
	# Метод lower() преобразует все символы верхнего регистра в строке в символы нижнего регистра и возвращает их. Если символы верхнего регистра отсутствуют, возвращается исходная строка.
	# Метод lower() не принимает никаких параметров.
	# example string
	string = "THIS SHOULD BE LOWERCASE!"
	print(string.lower()) # this should be lowercase!
	# string with numbers
	# all alphabets whould be lowercase
	string = "Th!s Sh0uLd B3 L0w3rCas3!"
	print(string.lower()) # th!s sh0uld b3 l0w3rcas3!

	# MORE EXAMPLES
	# first string
	firstString = "PYTHON IS AWESOME!"
	# second string
	secondString = "PyThOn Is AwEsOmE!"
	# returns 'The strings are same.'
	if(firstString.lower() == secondString.lower()):
		print("The strings are same.")
	else:
		print("The strings are not same.")





	#################################################### str.upper() ####################################################

# String isalnum, isalpha, isdecimal, isdigit, isnumeric, islower, isupper, isprintable, isspace, istitle, isidentifier methods
def func3():
	####################################################### str.isalnum() #######################################################
	# Метод isalnum() возвращает True, если все символы в строке являются буквенно-цифровыми (либо алфавитами, либо цифрами). Если нет, возвращается False.
	# Метод isalnum() не принимает никаких параметров.
	# Метод isalnum() возвращает:
	# True, если все символы в строке буквенно-цифровые
	# False, если хотя бы один символ не является буквенно-цифровым
	name = "M234onica"
	print(name.isalnum()) # True
	# contains whitespace
	name = "M3onica Gell22er "
	print(name.isalnum()) # False
	name = "Mo3nicaGell22er"
	print(name.isalnum()) # True
	name = "133"
	print(name.isalnum()) # True
	name = "M0n1caG3ll3r"
	# returns 'All characters of string (name) are alphanumeric.'
	if name.isalnum() == True:
		print("All characters of string (name) are alphanumeric.")
	else:
		print("All characters are not alphanumeric.")





	####################################################### str.isalpha() #######################################################
	# Метод isalpha() возвращает True, если все символы в строке являются алфавитными. Если нет, возвращается False.
	# Метод isalpha() не принимает никаких параметров.
	# Метод isalpha() возвращает:
	# True, если все символы в строке являются алфавитными (могут быть как строчными, так и прописными).
	# False, если хотя бы один символ не является алфавитом.
	name = "Monica"
	print(name.isalpha()) # True
	# contains whitespace
	name = "Monica Geller"
	print(name.isalpha()) # False
	# contains number
	name = "Mo3nicaGell22er"
	print(name.isalpha()) # False
	name = "MonicaGeller"
	# returns 'All characters are alphabets'
	if name.isalpha() == True:
		print("All characters are alphabets")
	else:
		print("All characters are not alphabets.")





	###################################################### str.isdecimal() ######################################################
	# Метод isdecimal() возвращает True, если все символы в строке являются десятичными. Если нет, возвращается False.
	# Метод isdecimal() не принимает никаких параметров.
	# Метод isdecimal() возвращает:
	# True, если все символы в строке являются десятичными.
	# False, если хотя бы один символ не является десятичным.
	# Верхний и нижний индексы считаются цифрами, но не десятичными знаками. Если строка содержит эти символы (обычно написанные с использованием юникода), isdecimal() возвращает False.
	# Точно так же римские цифры, числители валют и дроби считаются числовыми числами (обычно записанными с использованием Unicode), но не десятичными. В этом случае isdecimal() также возвращает False.
	# Существует два метода: isdigit() и isnumeric(), которые проверяют, содержит ли строка символы цифр и числовые символы соответственно.
	# Узнайте больше о методах isdigit() и isnumeric().
	s = "28212"
	print(s.isdecimal()) # True
	# contains alphabets
	s = "32ladk3"
	print(s.isdecimal()) # False
	# contains alphabets and spaces
	s = "Mo3 nicaG el l22er"
	print(s.isdecimal()) # False

	# Пример 2: строка, содержащая цифры и числовые символы
	s = '23455'
	print(s.isdecimal()) # True
	#s = '²3455'
	s = '\u00B23455'
	print(s.isdecimal()) # False
	# s = '½'
	s = '\u00BD'
	print(s.isdecimal()) # False





	####################################################### str.isdigit() #######################################################
	# Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.
	# Метод isdigit() не принимает никаких параметров.
	# Метод isdigit() возвращает:
	# True, если все символы в строке являются цифрами.
	# False, если хотя бы один символ не является цифрой.
	s = "28212"
	print(s.isdigit()) # True
	# contains alphabets and spaces
	s = "Mo3 nicaG el l22er"
	print(s.isdigit()) # False
	# Цифра - это символ, имеющий значение свойства:
	# Numeric_Type = Цифра/digit
	# Numeric_Type = десятичный/decimal
	# В Python надстрочные и подстрочные индексы (обычно записываемые с использованием Unicode) также считаются цифровыми символами. Следовательно, если строка содержит эти символы вместе с десятичными символами, isdigit() возвращает True.
	# Римские цифры, числители валют и дроби (обычно записываемые в кодировке Unicode) считаются числовыми символами, но не цифрами. isdigit() возвращает False, если строка содержит эти символы.
	s = '23455'
	print(s.isdigit()) # True
	#s = '²3455'
	# subscript is a digit
	s = '\u00B23455'
	print(s.isdigit()) # True
	# s = '½'
	# fraction is not a digit
	s = '\u00BD'
	print(s.isdigit()) # False





	#################################################### str.isnumeric() ####################################################
	# Метод isnumeric() возвращает True, если все символы в строке являются числовыми. Если нет, возвращается False.
	# Числовой символ имеет следующие свойства:
	# Numeric_Type=Десятичное Число
	# Numeric_Type=Цифра
	# Numeric_Type=Числовой
	# В Python десятичные символы (например: 0, 1, 2, ...), цифры (например, нижний индекс, верхний индекс) и символы, имеющие свойство числового значения Unicode (например, дробь, римские цифры, числители валют), все они считаются числовыми символами.
	# Метод isnumeric() не принимает никаких параметров.
	# Метод isnumeric() возвращает:
	# True, если все символы в строке являются числовыми.
	# False, если хотя бы один символ не является числовым.
	s = '1242323'
	print(s.isnumeric()) # True
	#s = '²3455'
	s = '\u00B23455'
	print(s.isnumeric()) # True
	# s = '½'
	s = '\u00BD'
	print(s.isnumeric()) # True
	s = '1242323'
	s='python12'
	print(s.isnumeric()) # False

	# MORE EXAMPLES
	#s = '²3455'
	s = '\u00B23455'
	# returns 'All characters are numeric.'
	if s.isnumeric() == True:
		print('All characters are numeric.')
	else:
		print('All characters are not numeric.')





	###################################################### str.islower() ######################################################
	# Метод islower() возвращает True, если все алфавиты в строке являются строчными. Если строка содержит хотя бы один алфавит в верхнем регистре, возвращается значение False.
	# Метод islower() не принимает никаких параметров.
	# Метод islower() возвращает:
	# True, если все алфавиты, существующие в строке, являются строчными.
	# False, если строка содержит хотя бы один алфавит в верхнем регистре.
	s = 'this is good'
	print(s.islower()) # True
	s = 'th!s is a1so g00d'
	print(s.islower()) # True
	s = 'this is Not good'
	print(s.islower()) # False

	# MORE EXAMPLES
	s = 'this is good'
	# returns 'Does not contain uppercase letter.'
	if s.islower() == True:
		print('Does not contain uppercase letter.')
	else:
		print('Contains uppercase letter.')
	s = 'this is Good'
	# returns 'Contains uppercase letter.'
	if s.islower() == True:
		print('Does not contain uppercase letter.')
	else:
		print('Contains uppercase letter.')






	################################################## str.isupper() ##################################################
	# Метод isupper() возвращает, являются ли все символы в строке верхнoм регистoрe или нет.
	# Метод isupper() не принимает никаких параметров.
	# Метод isupper() возвращает:
	# True, если все символы в строке являются прописными/верхнoм регистoрe
	# False, если какие-либо символы в строке являются строчными
	# example string
	string = "THIS IS GOOD!"
	print(string.isupper()) # True
	# numbers in place of alphabets
	string = "THIS IS ALSO G00D!"
	print(string.isupper()) # True
	# lowercase string
	string = "THIS IS not GOOD!"
	print(string.isupper()) # False

	# MORE EXAMPLES
	string = 'THIS IS GOOD'
	# returns 'Does not contain lowercase letter.'
	if string.isupper() == True:
		print('Does not contain lowercase letter.')
	else:
		print('Contains lowercase letter.')
	string = 'THIS IS gOOD'
	# returns 'Contains lowercase letter.'
	if string.isupper() == True:
		print('Does not contain lowercase letter.')
	else:
		print('Contains lowercase letter.')





	################################################## str.isprintable() ##################################################
	# Метод isprintable() возвращают True, если все символы в строке печатаются или строка пуста. Если нет, возвращается False.
	# Метод isprintable() не принимает никаких параметров.
	# Символы, занимающие место для печати на экране, известны как символы для печати. Например:
	# буквы и символы
	# цифры
	# пунктуация
	# пробельные
	# Метод isprintable() возвращает:
	# True, если строка пуста или все символы в строке печатаются
	# False, если строка содержит хотя бы один непечатаемый символ
	s = 'Space is a printable'
	print(s) # Space is a printable
	print(s.isprintable()) # True
	s = '\nNew Line is printable'
	print(s) # New Line is printable
	print(s.isprintable()) # False
	s = ''
	print('\nEmpty string printable?', s.isprintable()) # Empty string printable? True

	# MORE EXAMPLES
	# written using ASCII
	# chr(27) is escape character
	# char(97) is letter 'a'
	s = chr(27) + chr(97)
	# returns 'Not Printable'
	if s.isprintable() == True:
		print('Printable')
	else:
		print('Not Printable')
	s = '2+2 = 4'
	# returns 'Printable'
	if s.isprintable() == True:
		print('Printable')
	else:
		print('Not Printable')





	################################################### str.isspace() ###################################################
	# Метод isspace() возвращает True, если в строке есть только пробельные символы. Если нет, возвращается False.
	# Метод isspace() не принимает никаких параметров.
	# Символы, используемые для пробелов, называются пробелами. Например: табуляция, пробелы, новая строка и т.д.
	# Метод isspace() возвращает:
	# True, если все символы в строке являются пробельными символами
	# False, если строка пуста или содержит хотя бы один непечатаемый символ
	s = '   \t'
	print(s.isspace()) # True
	s = ' a '
	print(s.isspace()) # False
	s = ''
	print(s.isspace()) # False

	# MORE EXAMPLES
	s = '\t  \n'
	# returns 'All whitespace characters'
	if s.isspace() == True:
	  print('All whitespace characters')
	else:
	  print('Contains non-whitespace characters')
	s = '2+2 = 4'
	# returns 'Contains non-whitespace characters'
	if s.isspace() == True:
	  print('All whitespace characters')
	else:
	  print('Contains non-whitespace characters.')





	################################################### str.istitle() ###################################################
	# Метод istitle() возвращает True, если строка является строкой с заголовком. Если нет, возвращается False.
	# Метод istitle() не принимает никаких параметров.
	# Метод istitle() возвращает:
	# True, если строка представляет собой строку с заголовком
	# False, если строка не является строкой с заголовком или пустой строкой
	s = 'Python Is Good.'
	print(s.istitle()) # True
	s = 'Python is good'
	print(s.istitle()) # False
	s = 'This Is @ Symbol.'
	print(s.istitle()) # True
	s = '99 Is A Number'
	print(s.istitle()) # True
	s = 'PYTHON'
	print(s.istitle()) # False

	# MORE EXAMPLES
	s = 'I Love Python.'
	# returns 'Titlecased String'
	if s.istitle() == True:
		print('Titlecased String')
	else:
		print('Not a Titlecased String')
	s = 'PYthon'
	# returns 'Not a Titlecased String'
	if s.istitle() == True:
		print('Titlecased String')
	else:
		print('Not a Titlecased String')





	#################################################### str.isidentifier() ####################################################
	# Метод isidentifier() возвращает True, если строка является допустимым идентификатором в Python. Если нет, возвращается False.
	# Метод isidentifier() не принимает никаких параметров.
	# Метод isidentifier() возвращает:
	# True, если строка является допустимым идентификатором
	# False, если строка не является недопустимым идентификатором
	string = 'Python'
	print(string.isidentifier()) # True
	string = 'Py thon'
	print(string.isidentifier()) # False
	string = '22Python'
	print(string.isidentifier()) # False
	string = ''
	print(string.isidentifier()) # False

	# MORE EXAMPLES
	string = 'root33'
	# returns 'root33 is a valid identifier.'
	if string.isidentifier() == True:
		print(string, 'is a valid identifier.')
	else:
		print(string, 'is not a valid identifier.')
	  
	string = '33root'
	# returns '33root is not a valid identifier.'
	if string.isidentifier() == True:
		print(string, 'is a valid identifier.')
	else:
		print(string, 'is not a valid identifier.')
	  
	string = 'root 33'
	# returns 'root 33 is not a valid identifier.'
	if string.isidentifier() == True:
		print(string, 'is a valid identifier.')
	else:
		print(string, 'is not a valid identifier.')

# String endswith, startswith methods
def func4():
	############################################## str.endswith(suffix[, start[, end]]) ##############################################
	# Метод endwith() возвращает True, если строка заканчивается указанным суффиксом. Если нет, возвращается False.
	# Метод endwith() принимает три параметра:
	# suffix - строка или кортеж суффиксов для проверки
	# start (необязательно) - начальная позиция, в которой следует проверить суффикс в строке.
	# end (необязательно) - конечная позиция, в которой следует проверить суффикс в строке.
	text = "Python is easy to learn."
	result = text.endswith('to learn')
	print(result) # False
	result = text.endswith('to learn.')
	print(result) # True
	result = text.endswith('Python is easy to learn.')
	print(result) # True

	# Пример 2: endwith() с параметрами start и end
	text = "Python programming is easy to learn."
	# start parameter: 7
	# "programming is easy to learn." string is searched
	result = text.endswith('learn.', 7)
	print(result) # True
	# Both start and end is provided
	# start: 7, end: 26
	# "programming is easy" string is searched
	result = text.endswith('is', 7, 26)
	print(result) # False
	result = text.endswith('easy', 7, 26)
	print(result) # True

	# Также можно передать суффиксы кортежа методу endwith().
	# Если строка заканчивается каким-либо элементом кортежа, endwith() возвращает True. Если нет, возвращается False.
	text = "programming is easy"
	result = text.endswith(('programming', 'python'))
	print(result) # False
	result = text.endswith(('python', 'easy', 'java'))
	print(result) # True
	# With start and end parameter
	# 'programming is' string is checked
	result = text.endswith(('is', 'an'), 0, 14)
	print(result) # True





	############################################# str.startswith(suffix[, start[, end]]) #############################################

# Строковые методы, которые могут вам понадобиться: capitalize, casefold, center, count, expandtabs
def func5():
	######################################################## str.capitalize() ########################################################
	# Метод capitalize() преобразует первый символ строки в верхний регистр и переводит в нижний регистр все остальные символы, если они есть.
	# Метод capitalize() не принимает никаких параметров.
	string = "python is AWesome."
	capitalized_string = string.capitalize()
	print('Old String: ', string) # Old String: python is AWesome
	print('Capitalized String:', capitalized_string) # Capitalized String: Python is awesome
	string = "+ is an operator."
	new_string = string.capitalize()
	print('Old String:', string) # Old String: + is an operator.
	print('New String:', new_string) # New String: + is an operator.





	######################################################### str.casefold() #########################################################
	# Метод casefold() - это агрессивный метод lower(), который преобразует строки в строки, свернутые по регистру, для сопоставления без регистра.
	# Метод casefold() удаляет все различия в регистре, присутствующие в строке. Он используется для сопоставления без регистра, т.е. игнорирует регистры при сравнении.
	# Например, немецкая строчная буква ß эквивалентна ss. Однако, поскольку ß уже имеет нижний регистр, метод lower () ничего с ним не делает. Но casefold () преобразует его в ss.
	# Метод casefold() не принимает никаких параметров.
	string = "PYTHON IS AWESOME"
	# print lowercase string
	print("Lowercase string:", string.casefold()) # Lowercase string: python is awesome
	firstString = "der Fluß"
	secondString = "der Fluss"
	print(firstString.casefold()) # der Fluss
	print(secondString.casefold()) # der Fluss





	################################################# str.center(width[, fillchar]) #################################################
	# Метод center() возвращает строку, которая дополняется указанным символом.
	# Метод center() принимает два аргумента:
	# width - длина строки с заполненными символами
	# fillchar(необязательно) - символ заполнения
	# Аргумент fillchar является необязательным. Если он не указан, по умолчанию используется пробел.
	string = "Python is awesome"
	new_string = string.center(24)
	print("Centered String: ", new_string) # Centered String:     Python is awesome   
	string = "Python is awesome"
	new_string = string.center(24, '*')
	print("Centered String: ", new_string) # Centered String:  ***Python is awesome****





	############################################ str.count(substring, start=..., end=...) ############################################
	# Метод count() ищет подстроку в заданной строке и возвращает, сколько раз подстрока присутствует в ней.
	# Метод count() требует для выполнения только одного параметра. Однако у него также есть два необязательных параметра:
	# substring - строка, количество которой необходимо найти.
	# start (Необязательно) - начальный индекс в строке, с которой начинается поиск.
	# end (Необязательно) - конечный индекс в строке, где заканчивается поиск.
	# define string
	string = "Python is awesome, isn't it?"
	substring = "is"
	count = string.count(substring)
	# print count
	print("The count is:", count) # The count is: 2

	# Пример 2: Подсчитайте количество вхождений данной подстроки, используя start и end
	# define string
	string = "Python is awesome, isn't it?"
	substring = "i"
	# count after first 'i' and before the last 'i'
	count = string.count(substring, 8, 25)
	# print count
	print("The count is:", count) # The count is: 1





	################################################### str.expandtabs(tabsize) ###################################################
	# Метод expandtabs() возвращает копию строки, в которой все символы табуляции '\t' заменены символами пробела до следующего кратного значения параметра tabsize.
	# Метод expandtabs() принимает целочисленный аргумент размера табуляции. Размер табуляции по умолчанию - 8.
	# Пример 1: expandtabs() без аргумента
	string = 'xyz\t12345\tabc'
	result = string.expandtabs()
	print(result) # xyz     12345   abc

	# Пример 2: expandtabs() с другим аргументом
	string = "xyz\t12345\tabc"
	print('Original String:', string) # Original String: xyz	12345	abc
	# tabsize is set to 2
	print('Tabsize 2:', string.expandtabs(2)) # Tabsize 2: xyz 12345 abc
	# tabsize is set to 3
	print('Tabsize 3:', string.expandtabs(3)) # Tabsize 3: xyz   12345 abc
	# tabsize is set to 4
	print('Tabsize 4:', string.expandtabs(4)) # Tabsize 4: xyz 12345   abc
	# tabsize is set to 5
	print('Tabsize 5:', string.expandtabs(5)) # Tabsize 5: xyz  12345     abc
	# tabsize is set to 6
	print('Tabsize 6:', string.expandtabs(6)) # Tabsize 6: xyz   12345 abc






########################################## str.replace(old, new [, count]) ##########################################
# Метод replace() возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.
# Метод replace() может принимать максимум 3 параметра:
# old - старая подстрока, которую нужно заменить
# new - новая подстрока, которая заменит старую подстроку
# count (необязательно) - сколько раз вы хотите заменить старую подстроку новой подстрокой
# Примечание. Если число не указано, метод replace() заменяет все вхождения старой подстроки на новую подстроку.
# Если старая подстрока не найдена, возвращается копия исходной строки.
song = 'cold, cold heart'
# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt')) # hurt, hurt heart
song = 'Let it be, let it be, let it be, let it be'
# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2)) # Let it be, don't let it be, don't let it be, let it be

# MORE EXAMPLES
song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')
# The original string is unchanged
print('Original string:', song) # Original string: cold, cold heart
print('Replaced string:', replaced_song) # Replaced string: celd, celd heart
song = 'let it be, let it be, let it be'
# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0)) # let it be, let it be, let it be