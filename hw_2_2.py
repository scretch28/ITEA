#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:44:03 2020

@author: nia
"""
import math

# функція, що виконує запит числа у користувача
def get_number(text):
    num=-1
    while(num<0):
        num=float(input(text))        
    return num
  
    

# функція, що виконує розрахунок суми
# для float використовується скруглення меньшого числа до більшого цілого
def sum_of_natural_numbers(a,b):
 
    r=0
    if a<b:        
        a=math.ceil(a)
        b=int(b)
        r=range(a,b+1)
    elif a>b:
        b=math.ceil(b)
        a=int(a)
        r=range(b,a+1)
    else:
       return int(a)
   
    summ=0   
    for i in r:
        summ+=i
   
    return summ

resp='w'

while resp not in 'nNНн':
    
    a=get_number('Введіть перше число a: ')
    b=get_number('Введіть друге число b: ')
      
    summ=sum_of_natural_numbers(a,b)
    
    print('summ= ',summ)
   
    resp='w'
    print('Повторити чи вийти з програми?')
    while resp not in 'nNНнyYДд':       
        resp=input('Для повтору введіть одну з букв Д/д/Y/y, для виходу з програми Н/н/N/n: ')
        resp=resp.upper()



