# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:48:59 2020

@author: nia
"""

def getDate():
    day=int(input('Enter the day: '))
    month=int(input('Enter the month: '))
    year=int(input('Enter the year: '))
    return (day,month,year)


#1 запрос імені та прізвища користувача:
name=input('Enter first name and last name: ')

#2 привітання користувача з використанням прізвища та імені
print('Hello!', name)

#запит дня дати народження:
print('Enter your birsday')
dateB=getDate()

print('Enter current day: ')
dateL=getDate()

