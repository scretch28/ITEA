#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:05:38 2020

@author: nia
"""

#Задача №4 (Словарь переводов слов)¶
#filename: hw_3_4.py
#Создать функцию, которая принимает в качестве параметра текст и возвращает словарь 
#переводов слов из введённого пользователем текста.
#Для демонстрации текст задаётся в программе как переменная TEXT (см. шаблон).
#В функции для каждого уникльного слова (т.е. ранее не встречавшегося и для которого
#                                        не был дан перевод) запрашивает перевод этого слова,
#                                        например на английский.
#Если в качестве перевода была дана пустая строка, или строка из знаков пунктуации, то 
#перевод надо перезапросить.
#Программа вызывает функцию, получает результат и красиво выводит на экран сформированный 
#словарь переводов слов из текста.
#Подсказка: отдельная или вложенная функция для запроса перевода слова приветсвуется, 
#но не обязательна.


# hw_3_4.py
# Используйте этот шаблон, дополняя, но не изменяя его в основной части.

from string import whitespace, punctuation  # это часть шаблона
                                            # и можно дополнить перечнем импортированных
#                                            переменных модуля strings
                                            
def get_vocabluary(text):  # это часть шаблона
    result = {}  # это часть шаблона
    # Ниже вместо ... вставьте блок кода - релизация логики функции
    ...
    return result  # это часть шаблона

if __name__ == "__main__":  # это часть шаблона
    # переменную TEXT надо определить своим тестовым значением
    TEXT = """Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
    Текст должен быть многострочным.
    
    В тексте должны быть пустые строки
    и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""
    vocabluary = get_vocabluary(TEXT)  # это часть шаблона
    # Ниже вместо ... вставьте блок кода - релизация вывода на экран полученного словаря слов
    ...
