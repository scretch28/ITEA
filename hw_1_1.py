#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:00:11 2020

@author: nia
"""
def get_number(text):
    lol=''
    while not lol.isdigit():
        lol=input(text)
    return int(lol)

#1.1 запит імені та прізвища користувача:
name=input('Enter first name and last name: ')

#1.2 привітання користувача з використанням прізвища та імені
print('Hello!', name)

#2.1 запит дати народження:
day=get_number('Enter the day of birsday: ')
month=get_number('Enter the month of birsday: ')
year=get_number('Enter the year of birsday: ')


#2.2 запит поточної дати:
dayL=get_number('Enter current day: ')
monthL=get_number('Enter current month: ')
yearL=get_number('Enter current year: ')

#2.3 розрахунок та вивід місяця та року народження:
numdays=(yearL-year)*360+(monthL-month)*30+ (dayL-day)  #з огляду на умови завдання, 12міс*30=360 днів
if dayL<day:
    numdays+=1
nummonths=numdays//30
numyears=nummonths//12
print('''кількість місяців = %s,\n 
         кількість років = %s від дати народження''' % (nummonths, numyears))

#3.1 запит дати народження:
day=get_number('Enter the day of birsday: ')
month=get_number('Enter the month of birsday: ')
year=get_number('Enter the year of birsday: ')


#3.2 запит дати початку курсу:
dayL=int(10)
monthL=int(1)
yearL=int(2020)

#3.3 розрахунок та вивід прожитої кількості днів, місяців та років до початку курсу:
numdays=(yearL-year)*360+(monthL-month)*30+ (dayL-day)  #з огляду на умови завдання, 12міс*30=360 днів
if dayL<day:
    numdays+=1
nummonths=numdays//30
numyears=nummonths//12
print('''кількість днів= %s, 
      кількість місяців = %s, 
      кількість років = %s від дати народження до початку курсу''' %(numdays,nummonths, numyears))
