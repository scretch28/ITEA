#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 05:49:57 2020

@author: nia
"""

# Fibonacci

# Функція розрахунку та виводу на екран ряду чисел фібоначи    

def fib_v2(num,fib1,fib2):
    global fib1
    global fib2
    count=0
    print('Вивід наступних %s чисел фібоначи: '%num, end='')
    while count<num:
        fib=fib1+fib2;
        print(fib,' ',end='')
        fib1=fib2
        fib2=fib
        count+=1
    print()
       

# стартове значення n, 1, для того щоб цикль while відпрацював хочаб один раз
n=1
while n>0:
    # вивід перших двох чисел фібоначи
    fib1=1
    fib2=1
    print('Вивід перших двох чисел фібоначи ', fib1,' ',fib2, end='')
   
    num=input('Input the number: ')
   
    # користувач має ввести ціле додатньє, більше за нуль число,
    # в іншому випадку програма має завершитись (вихід по break)
    if not num.isdigit() or int(num)==0:
        break;
       
    n=int(num)
   
    # виклик функції версії 2, що використовує глобальні змінні
    fib_v2(n)