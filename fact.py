#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:51:50 2020

@author: nia
"""

def fact(n):
    if n==1:
        return 1;
    else:
        return n*fact(n-1)
    

x=int(input("Input the number: "))

print(fact(x))

abracadabra=list('abracadabra')
print(abracadabra.index('a', 2))


a=list('AEaezjhgfdshfdskukj')
print(a)
for ch in a:
    print(ord(ch), ' ',end='')
print()
a.sort()
print(a)
for ch in a:
   print(ord(ch), ' ',end='') 

print(chr(122))
