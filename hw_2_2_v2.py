#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:12:37 2020

@author: nia
"""

#filename: hw_2_2.py
#Пользователь вводит два числа a и b. Тип чисел может быть как int(),
# так и float()
#Выведите сумму всех натуральных чисел от меньшего до большего (включительно).
#Рекомендую строго соблюдать определние "натуральное число"
#Требования к реализации¶
#Функция sum_of_natural_numbers(a, b)¶
#Функция sum_of_natural_numbers должна принимать два параметра с числовыми значениями.
#Значения параметров могут быть:
#равны между собой
#первый больше второго
#первый меньше второго
#Функция должна вернуть натуральное число (в Python это можно выразить типом int), которое является суммой натуральных числел, находящихся в заданном параметрами диапазоне (включительно).
#Простой пример¶
#sum_of_natural_numbers(3, 7) должна вернуть 25
#Программа¶
#Запрашивает у пользователя два числа.
#Вызывает функцию.
#Печатает на экране вразумительное сообщение и результат функции.
#Запрашивает у пользователя вариант продолжения:
# повторить заново (y/Y/Д/д) или выйти (n/N/Н/н) из программы.


def sum_of_natural_numbers (a, b):
  
    r=0
    if a>b:
        r=range(b, a+1)
        list(range(b, a+1))
    elif a<b:
        r=range(a, b+1)
        list(range(a, b+1))    
    else:
       return a
    

    gather=0
    for i in r:
        gather+=i
    return gather
        
p='w'
#while p!='n' and p!='N' and p!='Н' and p!='н':
while p not in 'nNНн':

    a=float(input('Enter the number a: '))
    b=float(input('Enter the number b: '))
#    a=int(a)
#    b=int(b)
    if a<0:
        a=0
    if a<b:
        a=a+1
    if b<0:
        b=0
    if b<a:
        b=b+1
    else:

    return a, b
        
    
        
    summ=sum_of_natural_numbers(a,b)
        
    print('summ= ',summ)
   
    p='w'
    #while p!='n' and p!='N' and p!='Н' and p!='н' and p!='y' and p!='Y' and p!='Д' and p!='д':       
    while p not in 'nNНнyYДд':      
        p=input('Для продовження введіть - y/Y/Д/д, для виходу - n/N/Н/н): ')
