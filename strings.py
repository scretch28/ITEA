#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:36:36 2020

@author: nia
"""

#Коллекции в Python¶
#
#
#
#Строки как коллекции символов¶
#Строки – это упорядоченные по местоположению коллекции символов.
#Методы строк
#Форматирование строк
#Функции работы со списками
#модeль string
#
#
#
#Методы строк¶
#
#
#In [ ]:



s = 'абракадабра abracadabra'
ss = ' |*****\n\tПростой текст с переносами строк и символами табуляции\n*****|\t| '
print(ss)
print(repr(ss))


help(str)



# help(str.isalpha)


# help(str.startswith)


# help(str.strip)
with_spaces = '    |---|\t'
print(repr(with_spaces.rstrip()))#прибрати пробели праворуч
print(repr(with_spaces.lstrip()))#прибрати пробели ліворуч
print(repr(with_spaces.strip()))#прибрати усі пробели, окрім середини 



# help(str.count)
print(s.count('b'), s.count('д'), s.count('ц'))



# help(str.find)
print(repr(s.find('ab')))#відображає на якій позиції знаходиться підстрока
print(repr(s.find('AB')))#якщо символ відсутній = (-1)



# help(str.index)
print(repr(s.index('ab')))#відображає індекс
print(repr(s.index('AB')))# теж і що find, але при відсутності символа - помилка


# help(str.split)
r = ss.split('о')#разделить по умолчанию = преобразует 
#строку в список, разделитель по умолчанию - пробели
print(type(r))
print(r)
print(repr(r))


r = ss.split()
rr = ss.split(' ')
print(r)
print('*'*30)
print(rr)


# help(str.join)
empty = ', '
restored = empty.join(r)#обєднання списка в строку, зібрану зі списка
print(id(empty), id(restored))
print(repr(empty))
print(repr(restored))



# help(str.maketrans)
# help(str.translate)
tran_table = str.maketrans('abcd\t\n', '*БЦД  ')
print(repr(tran_table))
print(repr(s.translate(tran_table)))


#Форматирование строк¶


# Оператор % для форматирования строк
print('%s = %d' %('string', 7))



# help(str.format)
print("{0} = {1} / {1}-{0}".format('string', 7))
print('{key} = {value}'.format(key='string', value=7), )

print('{key1} = {value}'.format(key1=s, value=7), )

# f""
p1 = 'string'
p2 = 7
print(f"{p1} = {p2}")



