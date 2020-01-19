#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:00:11 2020

@author: nia
"""

#1.1 запит імені та прізвища користувача:
name=input('Enter first name and last name: ')

#1.2 привітання користувача з використанням прізвища та імені
print('Hello!', name)

#2.1 запит дати народження:
day=int(input('Enter the day of birsday: '))
month=int(input('Enter the month of birsday: '))
year=int(input('Enter the year of birsday: '))


#2.2 запит поточної дати:
dayL=int(input('Enter current day: '))
monthL=int(input('Enter current month: '))
yearL=int(input('Enter current year: '))


#2.3 розрахунок та вивід місяця та року народження:
numdays=(yearL-year)*360+(monthL-month)*30+ (dayL-day)  #з огляду на умови завдання, 12міс*30=360 днів
if dayL<day:
    numdays+=1
nummonths=numdays//30
numyears=nummonths//12
print(nummonths, numyears)

#3.1 запит дати народження:
day=int(input('Enter the day of birsday: '))
month=int(input('Enter the month of birsday: '))
year=int(input('Enter the year of birsday: '))


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
print(numdays, nummonths, numyears)
