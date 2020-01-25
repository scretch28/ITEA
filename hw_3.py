#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:36:38 2020

@author: nia
"""
#відображення прямокутника
def scquare(a, b):
    print ('scquare(%s, %s)' % (a, b))
    
    print('*' *b)
    for i in range(a-2):
         print('*'+ ' '*(b-2)+ '*')
   
    print('*' * b)

#відображення трикутника

def triangle(a,b):
    print ('triangle(%s, %s)' % (a, b))
    print('*')
    m=(b//(a-1))
    for i in range(1, a-1):
        print('*'*(i*m))
    print('*'*(b))
    
   
    

a=''
while not a.isdigit ():
    a=input('Введіть  а= ')
a=int(a)
b=''
while not b.isdigit ():
    b=input('Введіть  b= ')
b=int(b)
s=scquare(a, b)
v=triangle(a,b)


