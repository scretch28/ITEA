#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:57:31 2020

@author: nia
"""
#явное и неявное преобразование чисел
int(17.99999)//6==17.99999//6

s=''
while not s.isdigit():
    s=input('введите полож число: ')
s=int(s)
print('дальше будет работать с  x='+s)

#виражение возвращает 
s=''
while not s.isalpha():
    s=input('введите строку из букв: ')
print('дальше будет работать s=', str(s))


help(str)

s=input(':')
print(repr(s))#видеть управляющий символ

#числа Фибоначи - числа натурального ряда без 0
# 1,1,3, 5, 8
#print('вичисление соседних чисел Фибоначи)
fib1=1
fib2=1
 

i=0
while i<10:
    i+=1
    print(i)
s=''
while not s.isdigit():
    s=input('введите полож число: ')
s=int(s)
print('дальше будет работать с  x='+s)
list
list(range(1,5,6))
list(range(6,10,6))

i=0
while i in (0,1,2,3,4,5,6,7,8,9):
    i+=1
    print(i)


while not s.isdigit():
    s=input('введите полож число: ')
s=int(s)

#0!=1, 

for char in 'Spam':
    print(char)

x=123.6544

for ch in str(x):
    if ch.isdigit():
        print(ch)
        
#функции
        
def f1(val):
    print('val=', val)

f1(25)
