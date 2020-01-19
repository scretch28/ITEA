#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:53:41 2020

@author: nia
"""
# функція, що здійснює запит и повертає введену користувачем дату
def get_date(date_name):
    print (date_name)
    day=int(input('Enter the day: '))
    month=int(input('Enter the month: '))
    year=int(input('Enter the year: '))
    return {'day':day,'month':month,'year':year}


# функція, що здійснює розрахунок днів, місяців, років між двома датами
def date_diff(date1, date2):
    numdays=(date2['year']-date1['year'])*360+(date2['month']-date1['month'])*30+ (date2['day']-date1['day'])  #з огляду на умови завдання, 12міс*30=360 днів
    if date2['day']<date1['day']:
        numdays+=1
    nummonths=numdays//30
    numyears=nummonths//12
    return{'days':numdays,'month':nummonths,'years': numyears}


#1 запрос імені та прізвища користувача:
name=input('Enter first name and last name: ')

#2 привітання користувача з використанням прізвища та імені
print('Hello!', name)

#3 запит дня дати народження:
date1=get_date('Enter birsday date')

#4 запит актуальної дати
date2=get_date('Enter current date')

#5 розрахунок кількості місяців та років, що пройшли з дати народження
deteDiff=date_diff(date1,date2)

#6 вивід інформації
print('month from birsday: ', deteDiff['month'])
print('years from birsday: ', deteDiff['years'])

#7 розрахунок кількості днів, місяців та років, що пройшли з дати народження
date3={'day':10,'month':1,'year':2020}
deteDiff=date_diff(date3,date2)

#8 вивід інформації
print('days from start: ', deteDiff['days'])
print('month from start: ', deteDiff['month'])
print('years from start: ', deteDiff['years'])