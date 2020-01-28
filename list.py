#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:38:26 2020

@author: nia
"""

#Списки - list¶
#Списки – это упорядоченные по местоположению коллекции объектов произвольных типов, размер которых не ограничен. (М.Лутц)
#Создание списка
#Обращение по индексу
#Срезы
#Списки - изменяемый тип данных
#Методы списков
#Функции работы со списками
#
#
#
#Создание списка¶


# Конструктор класса
a = list()
print(type(a), str(a), repr(a))

<class 'list'> [] []

# Литерал
a = []
print(type(a), str(a), repr(a))
a = [1, 2, 3]
print(type(a), str(a), repr(a))
a = [1, '2', 3.0, 'Three', [4, 5, 6]]
print(type(a), str(a), repr(a))

<class 'list'> [] []
<class 'list'> [1, 2, 3] [1, 2, 3]
<class 'list'> [1, '2', 3.0, 'Three', [4, 5, 6]] [1, '2', 3.0, 'Three', [4, 5, 6]]

# Создание из итерируемого объекта
a = list('qwerty')
print(a)
b = ['qwerty']
print(b)
c = list(a)
print(c)
d = list(range(3, 10))
print(d)
d=a
print(d)
d[0]=99
c is a, c == a
d is a, d == a

['q', 'w', 'e', 'r', 't', 'y']
['qwerty']
['q', 'w', 'e', 'r', 't', 'y']
[3, 4, 5, 6, 7, 8, 9]

(False, True)



#Обращение по индексу¶


a = list('qwerty')
print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')  # Используем генератор списка из курса Advance
print(a)
a.append('u')
print(a)
# Отсчёт начинается с 0, а не с 1
print("a[1] = ", a[1], ", a[0] = ", a[0])
# Можно вести отсчёт с конца
print("a[-2] = ", a[-2])
print("a[6] = ", a[6])

[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w', 'e', 'r', 't', 'y']
['q', 'w', 'e', 'r', 't', 'y', 'u']
a[1] =  w , a[0] =  q
a[-2] =  y
a[6] =  u

a = [
    [1,2,3],
    [4,5,6],
]
a[1][1]

1

#Срезы¶


a = list('qwerty')
print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')
print(a)
print("От позиции - до конца:")
print("a[2:] = ", a[2:])
print("a[-3:] = ", a[-3:])
aa = a[2:]# срез створює копію, що дає можливість змінити копію масива,
            # основний залишається незмінним, id - різні
aa[0]=999
print(type(aa), id(a), id(aa))
print(aa)

[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w', 'e', 'r', 't', 'y']
От позиции - до конца:
a[2:] =  ['e', 'r', 't', 'y']# від позиції і до кінця
a[-3:] =  ['r', 't', 'y']# три останні символи
<class 'list'> 140349806226320 140349806626608
['e', 'r', 't', 'y']


a = list('qw')
aa = a[:]
b = a
id(a), id(aa), id(b), a == aa, b == a, b == aa


(140349806281024, 140349806284624, 140349806281024, True, True, True)


print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')
print(a)
print("От позиции - до позиции:")
print("a[1:3] = ", a[1:3])# виводиться елемент між позиціями, 
#                            останній не включається 
print("a[-3:-1] = ", a[-3:-1])


[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w']
От позиции - до позиции:
a[1:3] =  ['w']
a[-3:-1] =  ['q']

print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')
print(a)
print("С шагом:")
print("a[1::1] = ", a[1::1])#с 1-го елемента з шагом 1
a.append(4)
a.append(6)
a.append(5)
print(a)
print("a[1::2] = ", a[1::2])#вибирає елементи 1-й з шагом 2
print("a[::3] = ", a[::3])#вибирає кожен 3-й елемент
print("a[-1::-2] = ", a[-1::-2])
print("a[-1::-1] = ", a[-1::-1])#друкує навпаки
print(a[::-1])#від останнього елементу і до кінця


[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w']
С шагом:
a[1::1] =  ['w']
a[1::2] =  ['w']
a[::3] =  ['q']
a[-1::-2] =  ['w']
a[-1::-1] =  ['w', 'q']
['w', 'q']

#Списки - изменяемый тип данных¶

a = list('qw')
b = a  # list(a)
print(a, b, a is b, a==b)


['q', 'w'] ['q', 'w'] True True


a.append(['e'])
print(a, b, a is b, a==b)


['q', 'w', ['e']] ['q', 'w', ['e']] True True


b.extend(list('rt'))  # list('rt') == ['r', 't']
print(a, b, a is b, a==b)#об*єднання списків


['q', 'w', ['e'], 'r', 't'] ['q', 'w', ['e'], 'r', 't'] True True


a = list('qw')
b = a
print(a, b, id(a), id(b), a is b, a==b)
a = a + ['y','2']
print(a, b, id(a), id(b), a is b, a==b)


['q', 'w'] ['q', 'w'] 140349807024640 140349807024640 True True
['q', 'w', 'y'] ['q', 'w'] 140349806225120 140349807024640 False False


#Методы списков¶


help(list)


help(list.append)


Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.


help(list.extend)


Help on method_descriptor:

extend(self, iterable, /)
    Extend list by appending elements from the iterable.



a = list(range(10))
a.extend('asd')
a


help(list.clear)


Help on method_descriptor:

clear(self, /)
    Remove all items from list.


help(list.copy)


Help on method_descriptor:

copy(self, /)
    Return a shallow copy of the list.



a = list('qw')
b = list(a)
c = a[:]
d = a.copy()
print(id(a), a)
print(id(b), b)
print(id(c), c)
print(id(d), d)



140349806598496 ['q', 'w']
140349806597696 ['q', 'w']
140349806225120 ['q', 'w']
140349807024640 ['q', 'w']


a = [list(range(5)), 5, 6, {1:2, 3:{4:[1,2,{5:6,7:8}]}}]
b = a.copy()
print(a)
print(b)
print(a is b, a==b)



[[0, 1, 2, 3, 4], 5, 6, {1: 2, 3: {4: [1, 2, {5: 6, 7: 8}]}}]
[[0, 1, 2, 3, 4], 5, 6, {1: 2, 3: {4: [1, 2, {5: 6, 7: 8}]}}]
False True


id(a[0]), id(b[0])



(140349806651984, 140349806651984)


a[0][0] = 1024
b[0][0]



1024


import copy

a = [list(range(5)), 5, 6, {1:2, 3:{4:[1,2,{5:6,7:8}]}}]
b = a.copy()
print(id(a[0]), id(b[0]))
b = copy.deepcopy(a)
print(id(a[0]), id(b[0]))



140349806648608 140349806648608
140349806648608 140349806232192

help(list.count)


Help on method_descriptor:

count(self, value, /)
    Return number of occurrences of value.

list('abracadabra').count('a')#рахує кількість зазначених символів

5

a = [[1,2], 3, 4, [3,4], [1,2]]
a.count([3,4])

1


help(list.insert)


Help on method_descriptor:

insert(self, index, object, /)
    Insert object before index.


a = list('zaqwsx')
print(a)
l = ['1', '2']
a.insert(3, l)
print(a, a[3])#розширити список списком на 3-му ел-ті поставити 1,2
print(id(a[3]), id(l))






['z', 'a', 'q', 'w', 's', 'x']
['z', 'a', 'q', ['1', '2'], 'w', 's', 'x'] ['1', '2']
140349806311936 140349806311936


help(list.pop)


Help on method_descriptor:

pop(self, index=-1, /)
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

print(a)
x = a.pop(-2)
print('a=' + repr(a), 'x=' + repr(x))


['z', 'a', 'q', ['1', '2'], 's']
a=['z', 'a', 'q', 's'] x=['1', '2']


help(list.index)


Help on method_descriptor:

index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.


abracadabra = list('abracadabra')
p1 = abracadabra.index('a')
p2 = abracadabra.index('a', p1)
p3 = abracadabra.index('a', p1+1)
print(p1, p2, p3)


0 0 3


help(list.remove)


Help on method_descriptor:

remove(self, value, /)
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.



abracadabra.remove('a')
abracadabra






---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-98-d39fec810e62> in <module>
----> 1 abracadabra.remove('a')
      2 abracadabra

ValueError: list.remove(x): x not in list


In [99]:



help(list.reverse)






Help on method_descriptor:

reverse(self, /)
    Reverse *IN PLACE*.



a = list('qwerty')
print(a)
a.reverse()
print(a)
print(a.reverse(), a)



['q', 'w', 'e', 'r', 't', 'y']
['y', 't', 'r', 'e', 'w', 'q']
None ['q', 'w', 'e', 'r', 't', 'y']



a = list('qwerty')
anti_a = a.reverse()
a, anti_a



(['y', 't', 'r', 'e', 'w', 'q'], None)



# А это эквивалент, но с сохранением состояния и созданием нового списка
a = list('qwerty')
b = a[-1::-1]
print(a, b)
id(a), id(b)






['q', 'w', 'e', 'r', 't', 'y'] ['y', 't', 'r', 'e', 'w', 'q']


(140349806233472, 140349806281904)



help(list.sort)




Help on method_descriptor:

sort(self, /, *, key=None, reverse=False)
    Stable sort *IN PLACE*.



a = list('qwerty')
print(a)
print(a.sort(), a)



['q', 'w', 'e', 'r', 't', 'y']
None ['e', 'q', 'r', 't', 'w', 'y']



a = list('АЁЯаёя')
print(a)
for ch in a:
    print(ord(ch), end=' ')
print()
a.sort()
print(a)
for ch in a:
    print(ord(ch), end=' ')



['А', 'Ё', 'Я', 'а', 'ё', 'я']
1040 1025 1071 1072 1105 1103 
['Ё', 'А', 'Я', 'а', 'я', 'ё']
1025 1040 1071 1072 1103 1105 


#Функции работы со списками¶



help(len)
a = list(range(10))
len(a)  # length



Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.


10




help(min)
min(list('qwerty'))


Help on built-in function min in module builtins:

min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.






'e'

a = [1, 2.0, 'a', True]
min(a)



---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-116-52e50e1fbe0f> in <module>
      1 a = [1, 2.0, 'a', True]
----> 2 min(a)

TypeError: '<' not supported between instances of 'str' and 'int'


help(max)
max(list('qwerty'))






Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.


'y'


help(sum)
sum(list(range(1, 1+4)))  # 1+2+3+4=10






Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.


10



help(sorted)



Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.



a = list('qwerty')
b = sorted(a)
print(id(a), a)
print(id(b), b)


140349807112096 ['q', 'w', 'e', 'r', 't', 'y']
140349806359488 ['e', 'q', 'r', 't', 'w', 'y']


a = list(range(10)) + list(range(-9, 0))
print(a)
b = sorted(a, key=lambda x: abs(x))
print(b)


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6, -5, -4, -3, -2, -1]
[0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]



def key_func(x):
    """ Реализация lambda x: abs(x) """
    return abs(x)

a = list(range(10)) + list(range(-9, 0))
print(a)
b = sorted(a, key=key_func)
print(b)






[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6, -5, -4, -3, -2, -1]
[0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]




In [125]:



key_func_lambda = lambda x: abs(x)

a = list(range(10)) + list(range(-9, 0))
print(a)
b = sorted(a, key=key_func_lambda)
print(b)






[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6, -5, -4, -3, -2, -1]
[0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]





Расширенный материал¶



Распаковка и упаковка последовательностей¶

a = [1, 2, 3]
a1, a2, a3 = a
print(a1, a2, a3)
print(id(a1), id(a2), id(a3))
print(id(a[0]), id(a[1]), id(a[2]))






1 2 3
140350146966464 140350146966496 140350146966528
140350146966464 140350146966496 140350146966528



a = [1, 2, 3, 4, 5]
a1, a2, a3 = a
print(a1, a2, a3)



---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-136-2f0fa2b7fcc6> in <module>
      1 a = [1, 2, 3, 4, 5]
----> 2 a1, a2, a3 = a
      3 print(a1, a2, a3)

ValueError: too many values to unpack (expected 3)


a = [1, 2, 3, 4, 5]
a1, a2, a3, *extra = a
print(a1, a2, a3, extra)


1 2 3 [4, 5]


a = [1, 2, 3, 4, 5]
a1, a2, *extra, a3 = a
print(a1, a2, a3, extra)


1 2 5 [3, 4]




In [140]:



a = [1, 2, 3, 4, 5]
*extra, a1, a2, a3 = a
print(a1, a2, a3, extra)



3 4 5 [1, 2]


a = [1, 2, 3, 4, 5]
a1, a2, *_, a3 = a
print(a1, a2, a3)


1 2 5



a = [1,2,3]
b = [4,5,6]
c = a + b
print(a, b, c)


[1, 2, 3] [4, 5, 6] [1, 2, 3, 4, 5, 6]



a = [1,2,3]
b = [4,5,6]
c = [*a, *b]
print(a, b, c)



[1, 2, 3] [4, 5, 6] [1, 2, 3, 4, 5, 6]



a = [1,2,3]
b = [4,5,6]
c = [a, b]
print(a, b, c)


[1, 2, 3] [4, 5, 6] [[1, 2, 3], [4, 5, 6]]


Логические операции¶

'r' in list('abracadabra')


True

[1,2,3] < [1, 2, 1, 2]



False


[1,2,3] < [2, 2, [1, 2]]


[1,2,3] < [[2, 1]]






---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-144-55fb6b5b6d59> in <module>
----> 1 [1,2,3] < [[2, 1]]

TypeError: '<' not supported between instances of 'int' and 'list'