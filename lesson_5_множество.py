#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:25:06 2020

@author: nia
"""

#Коллекции в Python¶



#Множества - set¶
#Множества – это неупорядоченные коллекции уникальных и неизменяемых объектов.
# (М.Лутц)
#Создание множества
#Множества - изменяемый тип данных
#Операторы над множествами
#Методы множеств
#
#
#
#Создание множества¶

# Конструктор класса
a = set()
print(type(a), str(a), repr(a))
a = set([1,2,3])
print(type(a), str(a), repr(a))
a = set((1,2,3))
print(type(a), str(a), repr(a))


<class 'set'> set() set()
<class 'set'> {1, 2, 3} {1, 2, 3}
<class 'set'> {1, 2, 3} {1, 2, 3}

# Конструктор класса

a = set([1,2,3,1,2])
print(type(a), str(a), repr(a))
a = set((1,2,3,2,3))
print(type(a), str(a), repr(a))

<class 'set'> {1, 2, 3} {1, 2, 3}
<class 'set'> {1, 2, 3} {1, 2, 3}

# Литерал
a = {1, 2, 3}
print(type(a), str(a), repr(a))
a = {1, '2', 3.0, 'Three', (4, 5, 6)}
print(type(a), str(a), repr(a))
a = {1, '2', 3.0, 'Three', [4, 5, 6]}
print(type(a), str(a), repr(a))

<class 'set'> {1, 2, 3} {1, 2, 3}
<class 'set'> {1, 3.0, '2', 'Three', (4, 5, 6)} {1, 3.0, '2', 'Three', (4, 5, 6)}


---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-2c463dc14627> in <module>
      4 a = {1, '2', 3.0, 'Three', (4, 5, 6)}
      5 print(type(a), str(a), repr(a))
----> 6 a = {1, '2', 3.0, 'Three', [4, 5, 6]}
      7 print(type(a), str(a), repr(a))

TypeError: unhashable type: 'list'


# Создание из итерируемого объекта
a = set('qwerty')
b = set(['qwerty'*2])
c = set(a)
d = set(range(10))
print(a, b, c, d)

{'t', 'e', 'q', 'y', 'r', 'w'} {'qwertyqwerty'} {'y', 'r', 'w', 't', 'e', 'q'} {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}




Обращение по индексу¶

s = set(range(10))
s[1]

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-ec1c3703c84f> in <module>
      1 s = set(range(10))
----> 2 s[1]

TypeError: 'set' object is not subscriptable


Срезы¶

s = set(range(10))
s[1:5:2]

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-d74e171d717e> in <module>
      1 s = set(range(10))
----> 2 s[1:5:2]

TypeError: 'set' object is not subscriptable



Методы множества¶

help(set)

s = set(range(10))
print(s)
s.add(15)
print(s)

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15}


s + {15,}

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-da9cfebbf767> in <module>
----> 1 s + {15,}

TypeError: unsupported operand type(s) for +: 'set' and 'set'



Операторы над множествами¶

s = set(range(10))
print(s)

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

1 in s


True

s = set(range(10))
ss = set(range(10))
print('==', s == ss)
sss = set(range(11))
print(s, '>', sss, ':', s > sss)

== True
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} > {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} : False

s = set(range(10))
ss = set(range(10, 20))
print(s, '<', ss, ':', s < ss)
print(s, '>', ss, ':', s > ss)
print(s, '<=', ss, ':', s <= ss)
print(s, '>=', ss, ':', s >= ss)

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} < {10, 11, 12, 13, 14, 15, 16, 17, 18, 19} : False
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} > {10, 11, 12, 13, 14, 15, 16, 17, 18, 19} : False
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} <= {10, 11, 12, 13, 14, 15, 16, 17, 18, 19} : False
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} >= {10, 11, 12, 13, 14, 15, 16, 17, 18, 19} : False

s = set(range(0, 0+10))
ss = set(range(5, 5+10))
print(s, '&', ss, '=', s & ss)
print(s, '|', ss, '=', s | ss)
print(s, '-', ss, '=', s - ss)
print(s, '^', ss, '=', s ^ ss)


{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} & {5, 6, 7, 8, 9, 10, 11, 12, 13, 14} = {5, 6, 7, 8, 9}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} | {5, 6, 7, 8, 9, 10, 11, 12, 13, 14} = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - {5, 6, 7, 8, 9, 10, 11, 12, 13, 14} = {0, 1, 2, 3, 4}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} ^ {5, 6, 7, 8, 9, 10, 11, 12, 13, 14} = {0, 1, 2, 3, 4, 10, 11, 12, 13, 14}

Расширенный материал¶

Пример применения множеств¶


# Чтобы не перебирать два списка или кортежа, 
# можно использовать множества для поиска уникальных расхождений
# Например: 
# есть список терминов и список страниц книги, на которых дано их определение.
# Необходимо определить копии каких страниц необходимо сделать
termins = ['or', 'and', 'not', 'in', 'if', 'else', 'elif', 'for', 'while']
pages = [5, 5, 5, 6, 13, 13, 14, 17, 21]
need_copy = set(pages)
print('Для терминов', termins, 'необходимо скопировать страницы', need_copy)

Для терминов ['or', 'and', 'not', 'in', 'if', 'else', 'elif', 'for', 'while'] необходимо скопировать страницы {5, 6, 13, 14, 17, 21}

for i in sorted(list(need_copy)):
    print(i, '-', pages.count(i))

5 - 3
6 - 1
13 - 2
14 - 1
17 - 1
21 - 1
