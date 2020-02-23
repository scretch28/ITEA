#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:20:23 2020

@author: nia
"""

Строки как коллекции символов¶
Строки – это упорядоченные по местоположению коллекции символов.
● Методы строк
● Форматирование строк
● Функции работы со списками
● модeль string

Методы строк¶

In [ ]:

s = 'абракадабра abracadabra'
ss = ' |*****\n\tПростой текст с переносами строк и символами табуляции\n*****|\t| '

print(ss)
print(repr(ss))

In [ ]:

help(str)

In [ ]:

# help(str.isalpha)

In [ ]:

# help(str.startswith)

In [ ]:

# help(str.strip)
with_spaces = ' |---|\t'
print(repr(with_spaces.rstrip()))
print(repr(with_spaces.lstrip()))
print(repr(with_spaces.strip()))

In [ ]:

# help(str.count)
print(s.count('b'), s.count('д'), s.count('ц'))

In [ ]:

# help(str.find)
print(repr(s.find('ab')))
print(repr(s.find('AB')))

In [ ]:

# help(str.index)
print(repr(s.index('ab')))
print(repr(s.index('AB')))

In [ ]:

# help(str.split)
r = ss.split()
print(type(r))
print(r)
print(repr(r))

In [ ]:

r = ss.split()

rr = ss.split(' ')
print(r)
print('*'*30)
print(rr)

In [ ]:

# help(str.join)
empty = ', '
restored = empty.join(r)
print(id(empty), id(restored))
print(repr(empty))
print(repr(restored))

In [ ]:

# help(str.maketrans)
# help(str.translate)
tran_table = str.maketrans('abcd\t\n', 'АБЦД ')
print(repr(tran_table))
print(repr(s.translate(tran_table)))

Форматирование строк¶

In [ ]:

# Оператор % для форматирования строк
print('%s = %d' %('string', 7))

In [ ]:

# help(str.format)
print("{0} = {1} / {1}-{0}".format('string', 7))
print('{key} = {value}'.format(key='string', value=7), )

In [ ]:

# f""
p1 = 'string'
p2 = 7
print(f"{p1} = {p2}")