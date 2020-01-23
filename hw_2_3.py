#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:13:36 2020

@author: nia
"""

# Fibonacci

# Функція розрахунку та виводу на екран ряду чисел фібоначи    
       
def fib_v1(num):
    fib1=1
    fib2=1
    count=0
    print('Вивід наступних %s чисел фібоначи: '%num, end='')
    while count<num:
        fib=fib1+fib2;
        print(fib,' ',end='')
        fib1=fib2
        fib2=fib
        count+=1
    print()
       

# початкове значення n, 1, для того щоб цикль while відпрацював хоча б один раз
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
   
    # виклик функції 
    fib_v1(n)
   
  