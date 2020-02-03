#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:01:11 2020

@author: nia
"""

#Задача №3 (Статистика уникальных слов с сортировкой)¶
#filename: hw_3_3.py
#Изменить программу из Задачи №2 так, чтобы слова не повторялись.


list_words=list()
while True:
    s=input('Enter the words: ')
    if s=='':
        break
#    list_words=s.split()
    s=s.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ')
    list_words+=s.split()
list_words=list(set(list_words))
list_words.sort()

print(list_words)