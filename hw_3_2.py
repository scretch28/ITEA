#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:41:12 2020

@author: nia
"""

#Задача №2 (Статистика слов с сортировкой)¶
#filename: hw_3_2.py
#Изменить программу из Задачи №1 для сортировки слов из текста.
#Пользователь вводит с клавиатуры строки, состоящие из слов.
#Пустая строка означает прекратить ввод текста.
#Программа выводит на экран слова из текста, отсортированные по алфавиту.


list_words=list()
while True:
    s=input('Enter the words: ')
    if s=='':
        break
#    list_words=s.split()
    s=s.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ')
    list_words+=s.split()
list_words.sort()
print(list_words)

    
    


    
    
 