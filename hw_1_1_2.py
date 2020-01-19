# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:48:59 2020

@author: nia
"""

def get_dates():
    day1=int(input('Enter the day  of birsday: '))
    month1=int(input('Enter the month of birsday: '))
    year1=int(input('Enter the year of birsday: '))
    day2=int(input('Enter the current day: '))
    month2=int(input('Enter the current month: '))
    year2=int(input('Enter the current year: '))
    return {'day1':day1,'month1':month1,'year1':year1,'day2':day2,'month2':month2,'year2':year2}
    
def count_dates(dates):
    numdays=(dates['year2']-dates['year1'])*360+(dates['month2']-dates['month1'])*30+ (dates['day2']-dates['day1'])  #з огляду на умови завдання, 12міс*30=360 днів
    if dates['day2']<dates['day1']:
        numdays+=1
    nummonths=numdays//30
    numyears=nummonths//12
    return{'days':numdays,'month':nummonths,'years': numyears}


#1 запрос імені та прізвища користувача:
name=input('Enter first name and last name: ')

#2 привітання користувача з використанням прізвища та імені
print('Hello!', name)

#запит дня дати народження:
dates=get_dates()
q=count_dates(dates)
#print('days: ', q['days'])
print('month: ', q['month'])
print('years: ', q['years'])

dates['day1']=10
dates['month1']=1
dates['year1']=2020

q=count_dates(dates)
print('days: ', q['days'])
print('month: ', q['month'])
print('years: ', q['years'])






