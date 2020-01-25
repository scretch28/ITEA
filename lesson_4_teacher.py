#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:57:24 2020

@author: nia
"""

# Конструктор класса
a = list()
print(type(a), str(a), repr(a))

<class 'list'> [] []

In [56]:

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

In [57]:

# Создание из итерируемого объекта
a = list('qwerty')
print(a)
b = ['qwerty']
print(b)
c = list(a)
print(c)
d = list(range(3, 10))
print(d)
c is a, c == a






['q', 'w', 'e', 'r', 't', 'y']
['qwerty']
['q', 'w', 'e', 'r', 't', 'y']
[3, 4, 5, 6, 7, 8, 9]



Out[57]:

(False, True)



Обращение по индексу¶


In [58]:



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




In [59]:



a = [
    [1,2,3],
    [4,5,6],
]
a[0][0]





Out[59]:

1



Срезы¶


In [60]:



a = list('qwerty')
print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')
print(a)
print("От позиции - до конца:")
print("a[2:] = ", a[2:])
print("a[-3:] = ", a[-3:])
aa = a[2:]
print(type(aa), id(a), id(aa))
print(aa)






[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w', 'e', 'r', 't', 'y']
От позиции - до конца:
a[2:] =  ['e', 'r', 't', 'y']
a[-3:] =  ['r', 't', 'y']
<class 'list'> 140349806226320 140349806626608
['e', 'r', 't', 'y']




In [61]:



a = list('qw')
aa = a[:]
b = a
id(a), id(aa), id(b), a == aa, b == a, b == aa





Out[61]:

(140349806281024, 140349806284624, 140349806281024, True, True, True)


In [62]:



print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')
print(a)
print("От позиции - до позиции:")
print("a[1:3] = ", a[1:3])
print("a[-3:-1] = ", a[-3:-1])






[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w']
От позиции - до позиции:
a[1:3] =  ['w']
a[-3:-1] =  ['q']




In [63]:



print('[' + ', '.join([f"-{i}-" for i in range(10)]) + ']')
print(a)
print("С шагом:")
print("a[1::1] = ", a[1::1])
print("a[1::2] = ", a[1::2])
print("a[::3] = ", a[::3])
print("a[-1::-2] = ", a[-1::-2])
print("a[-1::-1] = ", a[-1::-1])
print(a[::-1])






[-0-, -1-, -2-, -3-, -4-, -5-, -6-, -7-, -8-, -9-]
['q', 'w']
С шагом:
a[1::1] =  ['w']
a[1::2] =  ['w']
a[::3] =  ['q']
a[-1::-2] =  ['w']
a[-1::-1] =  ['w', 'q']
['w', 'q']





Списки - изменяемый тип данных¶


In [64]:



a = list('qw')
b = a  # list(a)
print(a, b, a is b, a==b)






['q', 'w'] ['q', 'w'] True True




In [65]:



a.append(['e'])
print(a, b, a is b, a==b)






['q', 'w', ['e']] ['q', 'w', ['e']] True True




In [66]:



b.extend(list('rt'))  # list('rt') == ['r', 't']
print(a, b, a is b, a==b)
print(type(a))
['q', 'w', ['e'], 'r', 't'] ['q', 'w', ['e'], 'r', 't'] True True

In [67]:

a = list('qw')
b = a
print(a, b, id(a), id(b), a is b, a==b)
a = a + ['y',]
print(a, b, id(a), id(b), a is b, a==b)

['q', 'w'] ['q', 'w'] 140349807024640 140349807024640 True True
['q', 'w', 'y'] ['q', 'w'] 140349806225120 140349807024640 False False

Методы списков¶

In [ ]:

help(list)

In [68]:

help(list.append)


Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.

In [69]:

help(list.extend)


Help on method_descriptor:

extend(self, iterable, /)
    Extend list by appending elements from the iterable.

In [ ]:

a = list(range(10))
a.extend('asd')
a


In [70]:

help(list.clear)

Help on method_descriptor:

clear(self, /)
    Remove all items from list.

In [71]:

help(list.copy)

Help on method_descriptor:

copy(self, /)
    Return a shallow copy of the list.

In [72]:

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

In [73]:

a = [list(range(5)), 5, 6, {1:2, 3:{4:[1,2,{5:6,7:8}]}}]
b = a.copy()
print(a)
print(b)
print(a is b, a==b)

[[0, 1, 2, 3, 4], 5, 6, {1: 2, 3: {4: [1, 2, {5: 6, 7: 8}]}}]
[[0, 1, 2, 3, 4], 5, 6, {1: 2, 3: {4: [1, 2, {5: 6, 7: 8}]}}]
False True

In [74]:

id(a[0]), id(b[0])


Out[74]:

(140349806651984, 140349806651984)


In [75]:

a[0][0] = 1024
b[0][0]

Out[75]:

1024


In [76]:

import copy

a = [list(range(5)), 5, 6, {1:2, 3:{4:[1,2,{5:6,7:8}]}}]
b = a.copy()
print(id(a[0]), id(b[0]))
b = copy.deepcopy(a)
print(id(a[0]), id(b[0]))


140349806648608 140349806648608
140349806648608 140349806232192


In [77]:

help(list.count)


Help on method_descriptor:

count(self, value, /)
    Return number of occurrences of value.

In [78]:

list('abracadabra').count('a')


Out[78]:

5
In [79]:

a = [[1,2], 3, 4, [3,4], [1,2]]
a.count([3,4])


Out[79]:

1


In [80]:

help(list.insert)

Help on method_descriptor:

insert(self, index, object, /)
    Insert object before index.

In [81]:

a = list('zaqwsx')
a.insert(3, ['1', '2'])
print(a, a[3])

['z', 'a', 'q', ['1', '2'], 'w', 's', 'x'] ['1', '2']


In [ ]:

help(list.pop)

In [ ]:

print(a)
x = a.pop()
print(a, repr(x))
print('a='+repr(a), 'x='+repr(x))

In [ ]:



help(list.index)#по умолчанию берется наибольшее число




In [ ]:

abracadabra = list('abracadabra')
p1 = abracadabra.index('a')
p2 = abracadabra.index('a', p1)
p3 = abracadabra.index('a', p1+1)#устанавливаем индекс, чтобьі искать дальше
print(p1, p2, p3)


In [ ]:

help(list.remove)#удаляет установленньій елемент. Если не найдет параметр вьізовет исключение



In [ ]:

abracadabra.remove('a')
abracadabra

In [ ]:

help(list.reverse)#печатает перевернутьій список, а в функции ничего не возвращают
# методі возвращают none
In [ ]:

a = list('qwerty')
print(a)
print(a.reverse(), a)

In [ ]:

# А это эквивалент, но с сохранением состояния и созданием нового списка
a = list('qwerty')
b = a[-1::-1]
print(a, b)
id(a), id(b)
копирует перевертьіш

In [ ]:

help(list.sort)

In [ ]:
    
    

a = list('qwerty')
print(a)
print(a.sort(), a)

a = list('АЕЯаея')
print(a)
for ch in a:
    print(ord(ch), end='')
print()
a.sort
for ch in a:
    print(ord(ch), end='')



Функции работы со списками¶


In [ ]:

help(len)# длинна списка
a = list(range(10))
len(a)

In [ ]:

help(min)
min(list('qwerty'))#определяется наименшее

a=[1, 2.0, 'a',True]
min(a)


In [ ]:

help(max)
max(list('qwerty'))

In [ ]:

help(sum)
sum(list(range(1, 1+4)))  # 1+2+3+4=10




In [ ]:



a = list('qwerty')
b = sorted(a)
print(a)
print(b)
print(id(a), a)
print(id(b), b)


a=list(range(10))+list(range(-9, 0))
print(a)
b=sorted(a, key=lambda x: abs(x))
print(b)

#lambda xпараметр может біть только один
#возвращает другой списокб еквивалент среза.

def key_func(x):
    return abs(x)
a=list(range(10))+list(range(-9, 0))
print(a)
b=sorted(a, key=lambda x: abs(x))
print(b)

key_func_lambda=lambda x:abs(x)
a=list(range(10))+list(range(-9, 0))
print(a)
b=sorted(a, key=key_func abs(x))
print(b)

#in проверяет внутри списка
'r' in list ('hrgfjf')



Расширенный материал¶



Распаковка и упаковка последовательностей¶

#логические операции
In [ ]:
[1,2,3]>[3,2,1,2]

[1,2,3]>[3,2,[1,2]]


a = [1, 2, 3]
a1, a2, a3 = a
print(a1, a2, a3)
print(id(a1), id(a2), id(a3))
print(id(a[0], id(a[1], id(a[2])



a=[1,2,3]
a1, a2, a3 =a
print(a1,a2,a3)

a=[1,2,3,4,5]
a1, a2, a3 =a
print(a1,a2,a3)

a=[1,2,3,4,5]
a1, a2, a3 *extra=a
print(a1,a2,a3, extra)
#распаковка и создание нового списка=1 2 3 [4,5]

a=[1,2,3,4,5]
a1, a2, *_ , a3=a
print(a1,a2,a3)
#=*_то что нам не нужно
In [ ]:
    
    
a=[1,2,3]
b=[4,5,6]
c=[*a, *b]
print(a,b,c)

a=[1,2,3]
b=[4,5,6]
c=[*a,*b]
print(a,b,c)

a = [1, 2, 3, 4, 5]
a1, a2, a3 = a
print(a1, a2, a3)


a={
   (1,[2,3]):40,
   }
a#в ключе не нужно использовать изменяемьіе обьекти

a={
   (1,(2,3):40,
   }
    

a#в ключе не нужно использовать изменяемьіе обьекти