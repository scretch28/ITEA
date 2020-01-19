#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 00:45:19 2020

@author: nia
"""
#запрос введення  цілого числа
a=int(input('Enter the number: '))

#вивід числа у вигляді цілого, вещ-го, логічного та строкі
print(int(a))
print(float(a))
print(bool(a))
print(str(a))

#запрос ще одного цілого числа
#операції додавання
b=int(input('Enter the number: '))
print(int(a)+int(b))
print(int(a)+float(b))
print(int(a)+bool(b))
print(type(a))
#print(int(a)+str(b)) #неможлива операція зі строкою
print(float(a)+float(b))
print(float(a)+bool(b)) 
#print(float(a)+str(b))# неможлива операція зі строкою
print(bool(a)+bool(b))
print(bool(a)+float(b))
#print(bool(a)+str(b)) # неможлива операція зі строкою
print(str(a)+str(b)) 
#print(str(a)-str(b)) # неможлива операція зі строкою

#операції множення
print(int(a)*int(b))
print(int(a)*float(b))
print(int(a)*bool(b))
print(int(a)*str(b)) #2 раза по 3
print(float(a)*float(b))
print(float(a)*bool(b))
#print(float(a)*str(b)) # неможлива операція зі строкою
print(bool(a)*bool(b))
print(bool(a)*float(b))

