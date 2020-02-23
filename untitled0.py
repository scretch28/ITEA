#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:16:42 2020

@author: nia
"""



with open ('temp.txt', 'w') as f:
    print('Вивід на екранб а не в файл!', file=f)
    print('Вивід на екранб а не в файл!', file=f)
print(f.closed)

DEBAG=True

import sys

if DEBAG:
    out=sys.stdout
else:
    out=open('print_io.log,"w")
    
print('jhgkgf', file=out)