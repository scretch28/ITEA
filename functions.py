#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 23:36:51 2020

@author: nia
"""

def sqX(a, b, c):  
    D=b**2-4*a*c
    #print(D)
    x1=(-b+D**0.5)/(2*a)
    #print(x1)
    x2=(-b-D**0.5)/(2*a)
    #print(x2)
    return (x1,x2)

b=12
a=10
c=3
print(sqX(a,b,c))


b=1
a=16
c=4
print(sqX(3,8,5))
